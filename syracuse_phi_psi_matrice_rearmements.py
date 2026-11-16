#!/usr/bin/env python3
"""Syracuse Phi-Psi: certificat exact des corridors impairs et rearmements pairs.
Aucune dependance externe. Les CSV sont reproductibles.
"""
from __future__ import annotations
import argparse, csv, math
from collections import Counter
from pathlib import Path

ALPHA = math.log2(1.5)

def v2(n: int) -> int:
    if n <= 0: raise ValueError(n)
    return (n & -n).bit_length() - 1

def U(n: int) -> int:
    return (3*n+1)//2 if n&1 else n//2

def U_blocs(n: int) -> int:
    """Equivalent exact de U par cellules de base 1000, avec frontieres."""
    assert n >= 1
    p=n&1; lam=1+2*p
    blocks=[]; temp=n
    while temp:
        blocks.append(temp%1000); temp//=1000
    blocks.append(0)  # tete supplementaire
    mult=[]; carry=p
    for b in blocks:
        z=lam*b+carry
        mult.append(z%1000)
        carry=z//1000
    assert carry == 0
    rem=0; out=0
    for b in reversed(mult):
        q=(1000*rem+b)//2
        rem=b&1
        out=1000*out+q
    assert rem==0
    return out

def corridor(n: int):
    """Retour de l'impair n au prochain impair (r impaires, t paires)."""
    assert n>=1 and n%2
    r=v2(n+1); q=(n+1)>>r
    ev=3**r*q-1
    assert ev%2 ==0
    t=v2(ev); w=ev>>t
    rp=v2(w+1)
    assert U(n) == ((3*n+1)//2)
    assert w%2 ==1
    return r,q,ev,t,w,rp

def congruence_q(r:int, t:int, rp:int):
    """Tous les q impairs positifs du motif I^r P^t I^rp...
    q = [3^-r * (1-2^t+2^(t+rp))] mod 2^(t+rp+1).
    """
    mod=1 << (t+rp+1)
    inv=pow(pow(3,r,mod),-1,mod)
    res=(inv*(1-(1<<t)+(1<<(t+rp))))%mod
    assert res&1
    return res,mod

def one_row(r,t,rp):
    q0, modulus=congruence_q(r,t,rp)
    if r==1 and q0==1:
        q_min=q0+modulus # ne pas inclure n=1
    else:
        q_min=q0
    n=(1<<r)*q_min-1
    rr,qq,even,tt,w,rrp=corridor(n)
    assert (rr,qq,tt,rrp)==(r,q_min,t,rp)
    delta_d=math.log2(n/w)
    delta_j=math.log2(w+1)+ALPHA*rp - (math.log2(n+1)+ALPHA*r)
    formula_d=t-r*ALPHA + math.log2((1-1/(2**r*q_min))/(1-1/(3**r*q_min)))
    formula_j=ALPHA*rp-t+math.log2(1+(2**t-1)/(3**r*q_min))
    assert abs(delta_d-formula_d)<1e-11
    assert abs(delta_j-formula_j)<1e-11
    num_coef=(1<<(r+t))-3**r
    offset=(1<<t)-1
    # w<n iff num_coef*q > offset
    assert (w<n)==(num_coef*q_min>offset)
    # pour tous les q >0 de cette classe, si minimal certifie descente alors c'est universel
    # Sinon peut etre n'y a pas descente au q minimal, mais pour des q plus grands.
    universal_desc=(num_coef*q_min>offset)
    all_expansion=(num_coef<=0)
    # Comparaison du changement de J en arithmetique entiere :
    # Delta J > 0 iff 3^rp*(w+1) > 2^rp*(2^t*w+1).
    jnum=(3**rp)*(w+1)
    jden=(1<<rp)*((1<<t)*w+1)
    jsign=1 if jnum>jden else (-1 if jnum<jden else 0)
    # Pour une classe (r,t,r'), w croît avec q et Delta J est strictement décroissant.
    # Son signe limite vaut celui de rp*log2(3/2)-t.
    universal_j_plus=(pow(3,rp)>1<<(rp+t))
    universal_j_minus=(not universal_j_plus and jsign<0)
    j_mix=(not universal_j_plus and jsign>0)
    assert (jsign>0)==(delta_j>1e-10)
    return {
        'r_impaires':r,'t_paires':t,'r_suivant':rp,
        'q_residu':q0,'q_modulo':modulus,'q_min_n_gt_1':q_min,
        'n_temoin':n,'even_apres_r':even,'impair_suivant':w,
        'triplet_initial':f'{n%1000:03d}','triplet_suivant':f'{w%1000:03d}',
        'alpha3_initial':min(3,v2(3*n+1)),
        'deficit_D_corridor':f'{delta_d:.12f}',
        'variation_J_corridor':f'{delta_j:.12f}',
        'coef_2r+t_moins_3r':num_coef,'terme_additif_2t_moins_1':offset,
        'descente_pour_tous_n_gt_1_de_la_classe':int(universal_desc),
        'croissance_pour_tous_n_de_la_classe':int(all_expansion),
        'J_croissance_tous':int(universal_j_plus),
        'J_decroissance_tous':int(universal_j_minus),
        'J_signe_temoin':jsign,
        'J_signe_depend_du_contexte':int(j_mix),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-r',type=int,default=8)
    ap.add_argument('--max-t',type=int,default=8)
    ap.add_argument('--max-rprime',type=int,default=8)
    ap.add_argument('--test-n',type=int,default=100000)
    ap.add_argument('--out',default='/mnt/data')
    a=ap.parse_args()
    dest=Path(a.out); dest.mkdir(parents=True,exist_ok=True)
    rows=[one_row(r,t,rp) for r in range(1,a.max_r+1) for t in range(1,a.max_t+1) for rp in range(1,a.max_rprime+1)]
    file=dest/'Syracuse_PhiPsi_Matrice_Rearmements_r_t_rprime.csv'
    with file.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    # Confirmation de tous les temoins des cellules r,t,r' par l'operateur local.
    for row in rows:
        n=int(row['n_temoin']); r=int(row['r_impaires']); t=int(row['t_paires']); w=int(row['impair_suivant'])
        z=n
        for _ in range(r+t): z=U_blocs(z)
        assert z==w
    # Verification d'etats successifs par le moteur Phi-Psi base 1000 et l'operateur U
    counts=Counter(); exemples=[]
    for n in range(3,a.test_n+1,2):
        assert U_blocs(n)==U(n)
        r,q,ev,t,w,rp=corridor(n)
        x=n
        for _ in range(r):
            x=U_blocs(x)
        assert x==ev
        for _ in range(t):
            x=U_blocs(x)
        assert x==w
        counts['entiers_impairs_testes']+=1
        counts['corridors_descendants' if w<n else 'corridors_croissants_ou_egaux']+=1
        counts['portes_pairs_J_plus' if (v2((ev//2)+1)>=2) else 'portes_pairs_dernier_J_nonplus']+=1
        if n in {3,7,11,15,19,27,31,39,63,67,101,5461}:
            dd=math.log2(n/w)
            dj=math.log2(w+1)+ALPHA*rp-(math.log2(n+1)+ALPHA*r)
            exemples.append({'n':n,'r':r,'q':q,'t':t,'n_impair_suivant':w,'r_suivant':rp,'D_corridor':f'{dd:.12f}','delta_J':f'{dj:.12f}','alpha3':min(3,v2(3*n+1)),'triplet':f'{n%1000:03d}'})
    xfile=dest/'Syracuse_PhiPsi_Rearmements_Exemples.csv'
    with xfile.open('w',newline='',encoding='utf-8') as f:
        wr=csv.DictWriter(f,fieldnames=list(exemples[0]));wr.writeheader();wr.writerows(exemples)
    import json
    stats={'triples_r_t_rprime':len(rows),'triples_realises':len(rows), 'n_tests':dict(counts),
            'coef_expansion_universel_cases':sum(row['croissance_pour_tous_n_de_la_classe'] for row in rows),
            'descente_universelle_cases':sum(row['descente_pour_tous_n_gt_1_de_la_classe'] for row in rows),
            'delta_J_plus_universel_cases':sum(row['J_croissance_tous'] for row in rows),
            'delta_J_moins_universel_cases':sum(row['J_decroissance_tous'] for row in rows),
            'delta_J_signe_contextuel_cases':sum(row['J_signe_depend_du_contexte'] for row in rows),
            'parameters':vars(a)}
    (dest/'Syracuse_PhiPsi_Rearmements_Controle.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(stats,ensure_ascii=False,indent=2))
    print('CSV',file, xfile)

if __name__=='__main__': main()
