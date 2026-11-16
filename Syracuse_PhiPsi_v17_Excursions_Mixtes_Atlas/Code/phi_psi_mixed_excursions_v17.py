#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Φ–Ψ — matrice exacte des excursions mixtes (v17).

Transformation U: U(n)=(3n+1)//2 pour n impair ; n//2 pour n pair.
Cellules de corridors (r,t), toujours dans l'ordre reel et sous fidelite des
classes congruentielles initiales. Aucun résultat asymptotique universel
n'est affirmé.

Usage:
  python3 phi_psi_mixed_excursions_v17.py --out resultats_v17
  python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 6 --max-rt 3
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path
import argparse, csv, json, math, random


def ceildiv(a:int,b:int)->int:
    assert b>0
    return -((-a)//b)


def v2(a:int)->int:
    assert a>0
    return (a & -a).bit_length()-1


def U(a:int)->int:
    assert a>0
    return (3*a+1)//2 if a&1 else a//2


def U_block1000(a:int)->int:
    """Calcul indépendant en blocs décimaux Φ–Ψ, retenues puis restes."""
    assert a>0
    odd=a&1; mult=1+2*odd
    b=[];x=a
    while x:
        b.append(x%1000);x//=1000
    b.append(0)
    after=[];carry=odd
    for digit in b:
        z=mult*digit+carry
        after.append(z%1000);carry=z//1000
    assert carry==0
    out=0;rest=0
    for block in reversed(after):
        out=1000*out+(rest*1000+block)//2
        rest=block&1
    assert rest==0
    return out


@dataclass
class State:
    k:int; r0:int; rn:int; A:int; D:int; C:int; R:int; T:int
    threshold_nonterminal:int; rho:int; M:int; qmin:int
    qcap:int|None; forced_first_descent:bool; survivors:int|None
    expanded:int;contracted:int

    @property
    def bits(self):return self.M.bit_length()-1

    @property
    def u0(self):return (1<<self.r0)*self.qmin-1

    @property
    def uk(self):
        num=self.A*self.qmin+self.C
        assert num%self.D==0
        qk=num//self.D
        return (1<<self.rn)*qk-1

    @property
    def type(self):
        if self.qcap is None:return 'sans_prefixe_multiplicativement_contractant'
        if self.forced_first_descent:return 'premiere_descente_certifiee_pour_toute_la_classe'
        return 'representants_sans_descente_en_nombre_fini'


class Mixed:
    """Traitement incrémental des corridors, sans stocker tous les entiers."""
    def __init__(self,r0:int):
        assert r0>=1
        self.k=0;self.r0=r0;self.rn=r0
        self.A=1;self.D=1;self.C=0;self.R=0;self.T=0
        self.threshold=1;self.rho_prev=1;self.mod_prev=2
        self.qcap=None;self.expanded=0;self.contracted=0

    def append(self,r:int,t:int,rnext:int)->State:
        if r!=self.rn or min(r,t,rnext)<1:raise ValueError('Incompatibilité de frontière')
        # Avant d'entamer ce corridor, u_j=2**r*q_j -1 doit être >1.
        # C'est automatique pour r>=2; pour r=1 il faut q_j>=3.
        if r==1:
            self.threshold=max(self.threshold,ceildiv(3*self.D-self.C,self.A))
        a=3**r;b=(1<<t)-1;d=1<<(t+rnext)
        self.C=a*self.C+b*self.D
        self.A*=a;self.D*=d;self.R+=r;self.T+=t
        self.k+=1;self.rn=rnext
        self.expanded+=int(3**r>1<<(r+t))
        self.contracted+=int(3**r<1<<(r+t))
        M=2*self.D
        rho=((self.D-self.C)*pow(self.A,-1,M))%M
        assert rho&1 and rho>0
        assert rho%self.mod_prev==self.rho_prev
        self.rho_prev,self.mod_prev=rho,M
        qmin=rho+max(0,ceildiv(self.threshold-rho,M))*M
        assert qmin&1
        G=(1<<(self.R+self.T))-self.A
        # Condition exact de DESCENTE EFFECTIVE au rang k : G*q0 > C.
        # Pour la NEGATION de toute première descente jusqu'au rang k:
        # q0 <= min_{i:G_i>0} floor(C_i/G_i).
        if G>0:
            cap=self.C//G
            self.qcap=cap if self.qcap is None else min(self.qcap,cap)
        forced=(self.qcap is not None and qmin>self.qcap)
        survivors=None if self.qcap is None else max(0,(self.qcap-qmin)//M+1)
        assert forced==(survivors==0 if survivors is not None else False)
        return State(self.k,self.r0,self.rn,self.A,self.D,self.C,self.R,self.T,
                     self.threshold,rho,M,qmin,self.qcap,forced,survivors,
                     self.expanded,self.contracted)


def verify_state(path,st,extra_lifts=2,decimal=False):
    assert len(path)>=st.k+1
    for lift in range(extra_lifts+1):
        q0=st.qmin+lift*st.M
        q=q0
        for i in range(st.k):
            r,t=path[i];rp=path[i+1][0]
            ui=(1<<r)*q-1
            assert ui>1,(i,ui)
            if decimal and lift==0:
                n=ui
                for _ in range(r+t):
                    assert U(n)==U_block1000(n)
                    n=U(n)
            y=3**r*q-1
            assert v2(y)==t,(i,r,t,q,y)
            v=y>>t
            assert v2(v+1)==rp
            if decimal and lift==0:assert n==v
            q=(v+1)>>rp
            assert q&1
        uk=(1<<st.rn)*q-1
        assert uk>=1
        assert (st.A*q0+st.C)==st.D*q
        if lift==0:assert uk==st.uk
        # Verifier toutes les premieres descentes de cette classe pour les prefixes
        q=q0;ever=False
        for i in range(st.k):
            r,t=path[i];rp=path[i+1][0]
            v=(3**r*q-1)>>t
            q=(v+1)>>rp
            ever|=((1<<rp)*q-1)<((1<<st.r0)*q0-1)
        assert ever==(st.qcap is not None and q0>st.qcap)


def sample_path(kind:str,K:int):
    assert K>=1
    if kind=='thue':
        return [(1+(1-(j.bit_count()&1)),1) for j in range(K+1)]
    if kind=='fib':
        bits='0'
        while len(bits)<K+1:bits=''.join('01' if c=='0' else '0' for c in bits)
        return [(2 if x=='0' else 1,1) for x in bits[:K+1]]
    if kind=='islands':
        s=[];m=0
        while len(s)<K+1:
            s.extend([(2,1)]*(1<<m));s.append((1,1));m+=1
        return s[:K+1]
    if kind.startswith('mechanical_'):
        slope=kind.split('_',1)[1]
        with localcontext() as ctx:
            ctx.prec=80
            theta=ctx.ln(2)/ctx.ln(Decimal(3)/Decimal(2))-1
            if slope=='sub':theta-=Decimal('0.01')
            elif slope=='super':theta+=Decimal('0.01')
            elif slope not in ('critical','ceiling_critical'):raise ValueError(kind)
            rounder='ROUND_CEILING' if slope=='ceiling_critical' else 'ROUND_FLOOR'
            marks=[int(((j+1)*theta).to_integral_value(rounding=rounder))
                   -int((j*theta).to_integral_value(rounding=rounder)) for j in range(K+1)]
        return [(1+bit,1) for bit in marks]
    raise ValueError(kind)


def to_row(st:State,family:str):
    return {
        'famille':family,'horizon_K':st.k,'r_final':st.rn,
        'R_total_impair':st.R,'T_total_pair':st.T,
        'bits_modulo':st.bits,'bits_q0_min':st.qmin.bit_length(),
        'rho':str(st.rho),'module':str(st.M),'q0_min':str(st.qmin),
        'u0_min':str(st.u0),'uK_min':str(st.uk),
        'G_2H_moins_3R':str((1<<(st.R+st.T))-st.A),
        'C_additif':str(st.C),
        'plafond_sans_descente':str(st.qcap) if st.qcap is not None else '',
        'reste_plafond_moins_qmin':str(st.qcap-st.qmin) if st.qcap is not None else '',
        'survivants_sans_descente':str(st.survivors) if st.survivors is not None else 'tous_les_representants',
        'types_expansifs':st.expanded,'types_contractants':st.contracted,
        'classe':st.type,
        'deficit_temoin':f'{math.log2(st.u0)-math.log2(st.uk):.10f}',
    }


def write_csv(p,rows):
    if not rows:return
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        keys=list(dict.fromkeys(k for row in rows for k in row))
        w=csv.DictWriter(f,fieldnames=keys,delimiter=';');w.writeheader();w.writerows(rows)


def exhaustive(K=5,L=3):
    stat=Counter();examples={};rows=[]
    for word in product(range(1,L+1),repeat=2*K+1):
        path=[(word[2*i],word[2*i+1]) for i in range(K)]+[(word[-1],1)]
        b=Mixed(path[0][0]);states=[]
        for j in range(K):states.append(b.append(path[j][0],path[j][1],path[j+1][0]))
        s=states[-1];stat['totaux']+=1;stat[s.type]+=1
        is_mixed=s.expanded>0 and s.contracted>0
        stat['excursion_mixtes' if is_mixed else 'non_mixtes']+=1
        if is_mixed:stat['mixtes_'+s.type]+=1
        for key in [s.type, 'mixtes_'+s.type if is_mixed else 'non_mixtes_'+s.type]:
            if key not in examples: examples[key]=to_row(s,'exhaustif_K'+str(K))
    return dict(stat),examples


def tests():
    rng=random.Random(17112026)
    num=0
    for _ in range(250):
        K=rng.randint(1,8)
        path=[(rng.randint(1,5),rng.randint(1,5)) for _ in range(K+1)]
        b=Mixed(path[0][0]);states=[]
        for j in range(K):
            st=b.append(path[j][0],path[j][1],path[j+1][0]);states.append(st)
            verify_state(path,st,2,decimal=j<2 and _<50)
            if len(states)>1:
                prev=states[-2];assert st.qmin>=prev.qmin
                assert prev.qcap is None or st.qcap is not None and st.qcap<=prev.qcap
            num+=1
    # Contrôle brute-force indépendant sur mots courts et petites classes :
    independent=0
    for _ in range(60):
        K=rng.randint(1,3)
        path=[(rng.randint(1,3),rng.randint(1,3)) for _ in range(K+1)]
        b=Mixed(path[0][0]);s=None
        for j in range(K):s=b.append(path[j][0],path[j][1],path[j+1][0])
        for q0 in range(1,400,2):
            q=q0;real=True;seen_drop=False
            for j in range(K):
                r,t=path[j];rp=path[j+1][0];ui=(1<<r)*q-1
                y=3**r*q-1
                if ui<=1 or v2(y)!=t:
                    real=False;break
                v=y>>t
                if v2(v+1)!=rp:real=False;break
                q=(v+1)>>rp
                seen_drop|=((1<<rp)*q-1)<((1<<s.r0)*q0-1)
            pred=(q0%s.M==s.rho and q0>=s.threshold_nonterminal)
            assert real==pred,(path,q0,real,pred)
            if real:assert seen_drop==(s.qcap is not None and q0>s.qcap)
            independent+=1
    return {'mots_aleatoires':250,'prefixes_verifies':num,'tests_brute_force_independants':independent,
            'verifications_decimal_phi_psi':'100 premiers pas de corridors et relèvements'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=Path('/mnt/data/mixed_research'))
    ap.add_argument('--max-horizon',type=int,default=5)
    ap.add_argument('--max-rt',type=int,default=3)
    ap.add_argument('--path-horizon',type=int,default=300)
    args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    assert args.max_horizon<=6 and args.max_rt**(2*args.max_horizon+1)<=400000
    verified=tests()
    summary={}
    aggregate=[]
    for k in range(1,args.max_horizon+1):
        stat,examples=exhaustive(k,args.max_rt)
        summary[str(k)]=stat
        aggregate.append({'K':k,**stat})
        print('EXHAUSTIF',k,stat,flush=True)
    kinds=['thue','fib','islands','mechanical_sub','mechanical_critical','mechanical_super','mechanical_ceiling_critical']
    trajectories=[];checkpoints={1,2,3,4,5,8,10,16,20,32,50,64,100,128,200,256,300}
    series={}
    for kind in kinds:
        path=sample_path(kind,args.path_horizon)
        b=Mixed(path[0][0]);points=[];milestones=[]
        for j in range(args.path_horizon):
            s=b.append(path[j][0],path[j][1],path[j+1][0])
            row=to_row(s,kind);points.append(row)
            if kind=='mechanical_ceiling_critical':
                assert (1<<(s.R+s.T))<3**s.R, 'Un préfixe de pente critique supérieure devient contractant'
            if s.k in checkpoints:
                verify_state(path,s,decimal=j<5)
                milestones.append({key:row[key] for key in ('famille','horizon_K','bits_q0_min','bits_modulo','survivants_sans_descente','types_expansifs','types_contractants','classe','deficit_temoin','reste_plafond_moins_qmin')})
        trajectories.extend(milestones)
        count=Counter(p['classe'] for p in points)
        series[kind]={'classes':dict(count),'fin':points[-1],
                      'premiere_contraction_multiplicative':next((p['horizon_K'] for p in points if p['plafond_sans_descente']),None),
                      'premiere_certification_complete':next((p['horizon_K'] for p in points if p['classe']=='premiere_descente_certifiee_pour_toute_la_classe'),None),
                      'paliers_qmin':sum(points[i]['q0_min']==points[i-1]['q0_min'] for i in range(1,len(points)))}
        write_csv(args.out/('PhiPsi_v17_'+kind+'_classes.csv'),points)
        print('FAMILLE',kind,series[kind]['premiere_certification_complete'], series[kind]['fin']['bits_q0_min'],flush=True)
    write_csv(args.out/'PhiPsi_v17_Classification_Exhaustive.csv',aggregate)
    write_csv(args.out/'PhiPsi_v17_Excursions_Mixtes_Echantillons.csv',trajectories)
    output={'definition':'Les classifications portent sur les classes initiales entieres, non sur des probabilites de trajectoire.',
            'tests':verified,'comptages_exhaustifs':summary,'familles_nonperiodiques':series}
    (args.out/'PhiPsi_v17_Bilan.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
    print('TESTS',verified)

if __name__=='__main__':main()
