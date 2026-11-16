#!/usr/bin/env python3
"""Audit de la compatibilite des blocs impairs Phi-Psi, parites et deficits.
Python standard; pas de bibliotheques tierces. Sorties en CSV.
"""
import math, csv, itertools, argparse
from pathlib import Path

TWO_ALPHA_CATS=((0,.5),(1,.25),(2,.25))
BETA=math.log2(5/3)

def odd_step(u):
    assert u>0 and (u&1)
    z=3*u+1
    a=(z&-z).bit_length()-1
    return z>>a,a

def budget_certificate(alphas):
    k=len(alphas)
    amin=sum(min(3,a) for a in alphas)
    return (1<<amin)*pow(3,k)>pow(10,k)

def head_budget_certificate(alphas, lowerbounds):
    amin=sum(min(3,a) for a in alphas)
    lhs=1<<amin
    rhs=1
    for L in lowerbounds:
        lhs*=L; rhs*=3*L+1
    return lhs>rhs

def conditional_initial_certificate(alphas, initial_lower):
    k=len(alphas); A=sum(min(3,a) for a in alphas)
    return (1<<A)*initial_lower**k>(3*initial_lower+1)**k

def class_for_valuation_word(aa):
    A=0;B=0
    for a in aa:
        assert a>=1
        B=3*B+(1<<A)
        A+=a
    modulus=1<<(A+1)
    r=(((1<<A)-B)*pow(pow(3,len(aa),modulus),-1,modulus))%modulus
    return r,modulus,B

def dp(max_k,checkpoints,beta=BETA):
    fixed=[1.]; survive=[1.]
    for k in range(1,max_k+1):
        new=[0.0]*(len(fixed)+2)
        for i,p in enumerate(fixed):
            new[i]+=p*.5;new[i+1]+=p*.25;new[i+2]+=p*.25
        fixed=new
        bound=math.floor(k*beta)
        next_survive=[0.0]*(bound+1)
        for i,p in enumerate(survive):
            next_survive[i]+=p*.5
            if i+1<=bound:next_survive[i+1]+=p*.25
            if i+2<=bound:next_survive[i+2]+=p*.25
        survive=next_survive
        if k in checkpoints:
            yield k,bound,1-sum(fixed[:bound+1]),1-sum(survive)

def audit_prefixes(limit,horizon):
    result={k:dict(n=0,down=0,uniform=0,head=0,initial=0) for k in (1,2,3,5,10,20)}
    examples=[]
    for u0 in range(3,limit+1,2):
        u=u0;alphas=[];low=[]
        got_uniform=got_head=got_initial=got_down=False
        seen={}
        for k in range(1,horizon+1):
            if u==1:break
            lb=(u//10)*10 if u>=10 else 3
            low.append(lb)
            v,a=odd_step(u)
            alphas.append(a)
            u=v
            if budget_certificate(alphas):got_uniform=True
            if head_budget_certificate(alphas,low):got_head=True
            if conditional_initial_certificate(alphas,u0):got_initial=True
            if u<u0:got_down=True
            assert (not got_uniform or got_down), ('uniforme incorrect',u0,k)
            assert (not got_head or got_down), ('tete incorrecte',u0,k)
            assert (not got_initial or got_down), ('initial incorrect',u0,k)
            if k in result:
                # We are tracking all starting n, irrespective of later actual descent.
                seen[k]=(got_down,got_uniform,got_head,got_initial)
        for k in result:
            x=result[k];x['n']+=1
            status=seen.get(k)
            if status is None:
                # Si la trajectoire a déjà atteint 1, la descente et les
                # certificats acquis restent vrais pour tout horizon supérieur.
                status=(got_down,got_uniform,got_head,got_initial)
            for key,v in zip(('down','uniform','head','initial'),status):x[key]+=int(v)
        if u0 in (7,15,27,39,63,101,451,5461,4984461):
            examples.append([u0,','.join(map(str,alphas)),len(alphas),int(got_down),int(got_uniform),int(got_head),int(got_initial)])
    return result,examples

def write_csv(path,headers,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        wr=csv.writer(f,delimiter=';');wr.writerow(headers);wr.writerows(rows)

def main():
    a=argparse.ArgumentParser();a.add_argument('--max-k',type=int,default=1000);a.add_argument('--small-limit',type=int,default=100001);a.add_argument('--horizon',type=int,default=20);a.add_argument('--output',default='resultats_phi_psi_v15')
    opt=a.parse_args();out=Path(opt.output);out.mkdir(exist_ok=True,parents=True)
    cps={1,2,3,4,5,8,10,12,16,20,30,50,100,200,500,1000,2000,5000,10000}
    rows=list(dp(opt.max_k,cps))
    rows_head=list(dp(opt.max_k,cps,beta=math.log2(3/2)))
    combined=[(*x,y[2],y[3]) for x,y in zip(rows,rows_head)]
    write_csv(out/'PhiPsi_v15_Proportions_Certificats_Dyadiques.csv',
              ['K','Seuil_universel','Part_universelle_au_rang_K','Part_universelle_une_fois_avant_K','Part_asymptotique_tete_grande_au_rang_K','Part_asymptotique_tete_grande_une_fois_avant_K'],combined)
    for K in range(1,5):
        for arr in itertools.product((1,2,3,4,5),repeat=K):
            r,m,B=class_for_valuation_word(arr)
            n=r+m
            for target in arr:
                n,a=odd_step(n)
                assert a==target,(arr,r,m)
    result,examples=audit_prefixes(opt.small_limit,opt.horizon)
    write_csv(out/'PhiPsi_v15_Audit_Entiers_Impairs.csv', ['K','Entiers_de_depart','Descente_avant_K','Certificat_uniforme_avant_K','Certificat_tete_pied_avant_K','Certificat_depuis_tete_initiale_avant_K'],[(k,*v.values()) for k,v in result.items()])
    write_csv(out/'PhiPsi_v15_Exemples.csv', ['u0','profondeurs_a','nombre_blocs','descente','certificat_uniforme','certificat_tete_pied','certificat_tete_initiale'],examples)
    print('DP:',combined)
    print('AUDIT:',result)
    for arr in ((1,)*10,(1,)*20,(1,1,1,1,3),(1,1,2,1,4),(1,3,1,3,1)):
        r,m,B=class_for_valuation_word(arr)
        print('WORD',arr,'residue',r,'mod',m,'affine B',B,'witness',r+m)

if __name__=='__main__':main()
