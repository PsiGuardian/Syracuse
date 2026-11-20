#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phi-Psi: prolongement exact de rearmements non periodiques.

Regles: U(n) = (3*n+1)//2 si n impair, n//2 sinon.
Chaque corridor: u_j=2**r_j*q_j-1 (q_j impair), puis
q_{j+1}=(3**r_j*q_j + 2**t_j-1)/2**(t_j+r_{j+1}).
Sans modules externes. Les cas etudies ne prouvent pas Collatz.
"""
from __future__ import annotations
import argparse, csv, json, math, random
from dataclasses import dataclass
from pathlib import Path


def ceildiv(a:int,b:int)->int:
    if b<=0: raise ValueError('b>0 requis')
    return -((-a)//b)

def U(n:int)->int:
    return (3*n+1)//2 if n&1 else n//2


def U_blocs(n:int)->int:
    """Reconstruction indépendante en blocs décimaux de 3 chiffres."""
    if n<1:raise ValueError('n>=1')
    p=n&1;lam=1+2*p;c=p;blocs=[];x=n
    while x:
        blocs.append(x%1000);x//=1000
    blocs.append(0)
    produits=[]
    for b in blocs:
        z=lam*b+c;produits.append(z%1000);c=z//1000
    assert c==0
    sortie=0;retenue=0
    for b in reversed(produits):
        sortie=sortie*1000+(1000*retenue+b)//2
        retenue=b&1
    assert retenue==0
    return sortie


def v2(n:int)->int:
    if n<=0:raise ValueError('v2(n) exige n>0')
    return (n & -n).bit_length()-1

@dataclass
class Etat:
    k:int
    A:int
    D:int
    C:int
    r0:int
    rfin:int
    rho:int
    mod:int
    seuil:int
    qmin:int
    R:int
    T:int

    @property
    def bits_mod(self):return self.mod.bit_length()-1
    @property
    def bits_qmin(self):return self.qmin.bit_length()
    @property
    def u0(self):return (1<<self.r0)*self.qmin-1
    @property
    def qfin(self):
        z=self.A*self.qmin+self.C
        assert z%self.D==0
        return z//self.D
    @property
    def ufin(self):return (1<<self.rfin)*self.qfin-1
    @property
    def deficit_signe(self):
        z=((1<<(self.R+self.T))-3**self.R)*self.qmin-self.C
        return 1 if z>0 else -1 if z<0 else 0

class Prolongement:
    def __init__(self,r0:int):
        if r0<1:raise ValueError('r0>=1')
        self.k=0;self.r0=r0;self.r=r0
        self.A=1;self.D=1;self.C=0;self.R=0;self.T=0
        self.seuil=1
        self.previous_mod=2;self.previous_rho=1

    def ajouter(self,r:int,t:int,r_suivant:int)->Etat:
        if r!=self.r or min(r,t,r_suivant)<1:
            raise ValueError(f'frontiere incompatibile: attend r={self.r}, obtenu {(r,t,r_suivant)}')
        # Exclure le 1 parmi les DEPARTS de corridor, et non a la fin.
        if r==1:
            self.seuil=max(self.seuil,ceildiv(3*self.D-self.C,self.A))
        a=3**r; d=1<<(t+r_suivant); b=(1<<t)-1
        self.C=a*self.C+b*self.D
        self.A*=a;self.D*=d;self.R+=r;self.T+=t
        self.k+=1;self.r=r_suivant
        m=2*self.D
        rho=((self.D-self.C)*pow(self.A,-1,m))%m
        assert rho&1 and 0<rho<m
        assert rho%self.previous_mod == self.previous_rho
        self.previous_mod=m;self.previous_rho=rho
        qmin=rho+max(0,ceildiv(self.seuil-rho,m))*m
        return Etat(self.k,self.A,self.D,self.C,self.r0,r_suivant,rho,m,self.seuil,qmin,self.R,self.T)


def mot_iles(niveaux:int):
    """Ilots: (2,1)^1,(1,1),(2,1)^2,(1,1),(2,1)^4,..."""
    p=[]; snapshots=[]
    for m in range(niveaux):
        depart=len(p)
        L=1<<m
        p.extend([(2,1)]*L)
        snapshots.append((m,L,depart,len(p)))
        p.append((1,1))
    return p,snapshots

def mot_thue(k:int):
    return [(2 if j.bit_count()%2==0 else 1,1) for j in range(k+1)]

def mot_fibonacci(k:int):
    bits='0'
    while len(bits)<k+1:
        bits=''.join('01' if c=='0' else '0' for c in bits)
    return [(2 if c=='0' else 1,1) for c in bits[:k+1]]


def moments(paires, moments):
    moments=set(moments)
    pr=Prolongement(paires[0][0])
    result=[]
    for j in range(len(paires)-1):
        r,t=paires[j];next_r=paires[j+1][0]
        e=pr.ajouter(r,t,next_r)
        if e.k in moments:
            result.append(e)
    return result


def verification_independante(paires, e:Etat):
    q=e.qmin;r0=paires[0][0]
    assert q>0 and q&1
    for j in range(e.k):
        r,t=paires[j];rp=paires[j+1][0]
        assert q&1
        u=(1<<r)*q-1
        assert u>1,(j,u)
        z=3**r*q-1
        assert v2(z)==t,(j,t,v2(z))
        v=z>>t
        assert v>=1 and v2(v+1)==rp
        q=(v+1)>>rp
    assert q==e.qfin
    assert e.ufin==(1<<e.rfin)*q-1
    assert e.deficit_signe == (1 if e.u0>e.ufin else -1 if e.u0<e.ufin else 0)


def ilots_audit(niveaux):
    p,snaps=mot_iles(niveaux)
    snapshots={end:(m,L,depart) for m,L,depart,end in snaps}
    pr=Prolongement(p[0][0]); results=[]
    for j in range(len(p)-1):
        e=pr.ajouter(p[j][0],p[j][1],p[j+1][0])
        if e.k in snapshots:
            m,L,depart=snapshots[e.k]
            lower_num=1<<(3*L-1+2*depart)
            lower_den=9**depart
            lower_ceil=ceildiv(lower_num,lower_den)
            assert e.qmin+1>=lower_ceil
            verification_independante(p,e)
            results.append((e,m,L,depart,lower_ceil))
    return p,results


def lignes_iles(results):
    rows=[]
    for e,m,L,depart,lower in results:
        rows.append({
            'niveau_m':m,'longueur_ilot_L':L,'position_depart_j':depart,
            'horizon_corridors_K':e.k,'bits_mod':e.bits_mod,
            'bits_q0_min':e.bits_qmin,'q0_min':str(e.qmin),
            'u0_min':str(e.u0),'uK':str(e.ufin),
            'borne_entiere_q0_plus1':str(lower),
            'borne_bits_q0_plus1':lower.bit_length(),
            'marge_theorique_bits':f'{3*L-1-depart*math.log2(9/4):.9f}',
            'deficit_signe':e.deficit_signe,
            'taux_R_sur_H':f'{e.R/(e.R+e.T):.9f}',
        })
    return rows


def lignes_apparentes(pattern,selection):
    p=pattern(max(selection))
    states=moments(p,selection)
    for e in states:verification_independante(p,e)
    return [{
        'horizon_K':e.k,'bits_mod':e.bits_mod,'bits_q0_min':e.bits_qmin,
        'q0_min':str(e.qmin),'u0_min':str(e.u0),'uK':str(e.ufin),
        'R':e.R,'T':e.T,'drift_log2_A_sur_D':f'{e.R*math.log2(3)-(e.T+e.R-e.r0+e.rfin):.9f}',
        'deficit_signe':e.deficit_signe
    } for e in states]


def verifications():
    rng=random.Random(160026)
    # Conditions de frontieres et relèvement, meme avec toutes profondeurs >1.
    for z in range(400):
        k=rng.randint(1,6)
        p=[(rng.randint(1,5),rng.randint(1,5)) for _ in range(k+1)]
        pr=Prolongement(p[0][0]);state=None
        for j in range(k):
            state=pr.ajouter(*p[j],p[j+1][0])
            verification_independante(p,state)
            if z<120:
                u=(1<<p[0][0])*state.qmin-1
                for jj in range(j+1):
                    r,t=p[jj]
                    for _ in range(r+t):
                        assert U_blocs(u)==U(u)
                        u=U(u)
                assert u==state.ufin
            # Un autre representant de la meme classe doit convenir.
            etat_alter=Etat(state.k,state.A,state.D,state.C,state.r0,state.rfin,
                            state.rho,state.mod,state.seuil,state.qmin+state.mod,state.R,state.T)
            verification_independante(p,etat_alter)
            assert state.qmin-state.mod<state.seuil or state.qmin==state.rho
    # Verification exhaustive independante sur petites classes, sans reutiliser la congruence.
    for z in range(80):
        k=rng.randint(1,3)
        p=[(rng.randint(1,3),rng.randint(1,3)) for _ in range(k+1)]
        pr=Prolongement(p[0][0]);state=None
        for j in range(k):state=pr.ajouter(*p[j],p[j+1][0])
        for q0 in range(1,514,2):
            q=q0;possible=True
            for j in range(k):
                r,t=p[j];rp=p[j+1][0]
                u=(1<<r)*q-1
                zeta=3**r*q-1
                if u<=1 or zeta<=0 or v2(zeta)!=t:
                    possible=False;break
                v=zeta>>t
                if v2(v+1)!=rp:
                    possible=False;break
                q=(v+1)>>rp
                if not q&1:possible=False;break
            prevu=(q0%state.mod==state.rho and q0>=state.seuil)
            assert possible==prevu,(p,q0,possible,prevu)
    # Ilot expansif a frontiere de sortie r=1: la valuation est EXACTEMENT 3L-1.
    for m in range(9):
        p,results=ilots_audit(m+1)
        e,mm,L,depart,lower=results[-1]
        # q au debut du dernier ilot calculé en suivant les corridors precedents.
        q=e.qmin
        for j in range(depart):
            r,t=p[j];rnext=p[j+1][0]
            q=(3**r*q+(1<<t)-1)//(1<<(t+rnext))
        assert v2(q+1)==3*L-1
    return {'tests_aleatoires':400, 'comparaisons_exhaustives':80*257,'tests_decimaux_phi_psi':120, 'tests_releves_etats': 'chaque prefixe', 'ilots_jusqua_longueur':256}


def csv_write(path,rows):
    if not rows:return
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter=';');w.writeheader();w.writerows(rows)


def construire(sortie:Path,niveaux:int=9,profondeur:int=512,verifier=True):
    sortie.mkdir(parents=True,exist_ok=True)
    tests=verifications() if verifier else None
    p,ils=ilots_audit(niveaux)
    li=lignes_iles(ils)
    sample=[x for x in [1,2,4,8,16,32,64,128,256,512,1024] if x<=profondeur]
    th=lignes_apparentes(mot_thue,sample)
    fi=lignes_apparentes(mot_fibonacci,sample)
    csv_write(sortie/'PhiPsi_v16_Ilots_Exponentiels.csv',li)
    csv_write(sortie/'PhiPsi_v16_Thue_Morse.csv',th)
    csv_write(sortie/'PhiPsi_v16_Fibonacci.csv',fi)
    # Série intégrale des préfixes finis : voir exactement les marches et les plateaux.
    complet=[]
    for label,pattern in [('ilots',lambda n:p),('thue_morse',mot_thue),('fibonacci',mot_fibonacci)]:
        fin=len(p)-1 if label=='ilots' else profondeur
        print(f'[calcul classes complètes] {label}: {fin} niveaux',flush=True)
        for item in lignes_apparentes(pattern, list(range(1,fin+1))):
            complet.append({'famille':label,**item})
    csv_write(sortie/'PhiPsi_v16_Toutes_Classes_Emboitees.csv',complet)
    result={
        'mecanique':'U(n)=(3n+1)/2 si impair, n/2 si pair',
        'ilots':[{k:v for k,v in row.items() if k not in ['q0_min','u0_min','uK','borne_entiere_q0_plus1']} for row in li],
        'thue_morse':th,
        'fibonacci':fi,
        'delta_thue_morse':1-1.5*(math.log2(3)-1),
        'series_completes':{x:sum(i['famille']==x for i in complet) for x in ('ilots','thue_morse','fibonacci')},
        'plateaux_de_q0_min':{x:sum(complet[i]['q0_min']==complet[i-1]['q0_min']
                 for i in range(1,len(complet)) if complet[i]['famille']==x and complet[i-1]['famille']==x)
                 for x in ('ilots','thue_morse','fibonacci')},
        'tests':tests,
        'limite':'Ces resultats prouvent seulement des exclusions de familles non periodiques explicites; conjecture de Syracuse ouverte.'
    }
    (sortie/'PhiPsi_v16_Resultats.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--niveaux',type=int,default=9)
    ap.add_argument('--profondeur',type=int,default=512)
    ap.add_argument('--sortie',type=Path,default=Path('phi_psi_v16_resultats'))
    ap.add_argument('--sans-tests',action='store_true')
    ns=ap.parse_args()
    d=construire(ns.sortie,ns.niveaux,ns.profondeur,not ns.sans_tests)
    print('VERIFICATIONS:',d['tests'])
    for x in d['ilots']:print('ILOT',x['niveau_m'],'L',x['longueur_ilot_L'], 'K',x['horizon_corridors_K'],'bits q0min',x['bits_q0_min'],'borne bits',x['borne_bits_q0_plus1'])
    for label in ['thue_morse','fibonacci']:
        for x in d[label]:print(label,x['horizon_K'],x['bits_q0_min'],x['deficit_signe'])
