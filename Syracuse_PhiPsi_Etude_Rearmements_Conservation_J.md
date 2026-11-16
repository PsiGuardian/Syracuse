# Syracuse Φ–Ψ — Étude des réarmements et du déficit (note indépendante)

Cette étude utilise les conventions du complément Φ–Ψ v14 et de la note v15. Ce document **n'est pas une preuve** de convergence universelle.

## 1. Deux quantités exactes

On utilise la transformation accélérée `U(n)=(3n+1)/2` si `n` est impair, et `U(n)=n/2` si `n` est pair.

Le stock `r(n)=ν₂(n+1)` et le potentiel auxiliaire

    J(n) = log₂(n+1) + log₂(3/2) ν₂(n+1)

vérifient `J(U(n))=J(n)` pour **chaque transition impaire**, y compris lorsque sa sortie est paire. Cette loi locale est indépendante des dimensions du nombre et des fenêtres décimales qui la calculent.

Le déficit d'une portion quelconque de trajectoire de `a` à `b` est `D(a,b)=log₂(a/b)`. Il est positif si et seulement si `b<a`.

## 2. Transfert d'un corridor au corridor suivant

Pour un départ impair `u>1`, écrire

    u = 2^r q - 1,  q impair positif, r=ν₂(u+1)≥1.

Après `r` transitions impaires accélérées, on atteint l'entier pair

    e = 3^r q - 1.

Avec `t=ν₂(e)≥1`, les `t` transitions paires aboutissent à l'impair

    w = (3^r q - 1)/2^t,
    r' = ν₂(w+1) ≥ 1.

Le mot de parité exact commence par `I^r P^t I^r' P`, et la cellule de réarmement se note `(r,q)→(r,t,w,r')`.

### Déficit exact

    D_corr = log₂(u/w)
           = t-r log₂(3/2) + log₂[(1-1/(2^r q))/(1-1/(3^r q))].

Ce dernier logarithme est strictement négatif. Une descente exige et équivaut à

    (2^(r+t)-3^r) q > 2^t-1.

Le simple coefficient `2^(r+t)>3^r` est nécessaire mais doit être complété par cette inégalité avec `q`.

### Variation exacte de J

`J` est constant pendant la portion `I^r`. Toute sa variation se produit donc pendant `P^t` :

    ΔJ = J(w)-J(u)
       = log₂[(w+1)/(2^t w+1)] + r' log₂(3/2)
       = r' log₂(3/2)-t + log₂[1+(2^t-1)/(3^r q)].

La correction finale est strictement comprise entre 0 et 1. Ainsi :

    r' log₂(3/2)-t < ΔJ < r' log₂(3/2)-t+1.

Le **signe exact**, sans logarithme flottant, résulte de la comparaison entre

    3^r' (w+1)    et    2^r' (2^t w+1).

**Distinction :** une hausse de `J` ne garantit pas une baisse numérique, ni l'inverse.

## 3. Tous les triplets finis de réarmement sont réalisables

Fixons librement trois entiers `r,t,r'≥1`. Définissons `M=2^(t+r'+1)`. La condition nécessaire et suffisante sur le quotient impair `q` est :

    q ≡ (3^r)^(-1) · (1-2^t+2^(t+r')) (mod M),

l'inverse étant pris modulo `M`. Le résidu est nécessairement impair.

**Preuve :** `w+1` doit être divisible exactement par `2^r'`. Comme `3^r q-1=2^t w`, imposer `w+1≡2^r' (mod 2^(r'+1))` équivaut à la congruence affichée. En choisissant un représentant impair positif `q` et ses relèvements `q+kM`, on construit une infinité de départs `u=2^r q-1` dont les trois longueurs sont exactement `r,t,r'`. On écarte `u=1` lorsqu'il apparaît.

Par conséquent, il n'existe aucune obstruction de compatibilité à la réalisation d'un triplet fini arbitraire `(r,t,r')`. Les éventuelles contraintes globales sur le déficit doivent provenir du suivi d'un *même entier* sur une infinité potentielle de corridors, pas d'une interdiction locale de triplets.

## 4. Matrice bornée, exhaustive dans son domaine

Le CSV `Syracuse_PhiPsi_Matrice_Rearmements_r_t_rprime.csv` contient les **512 triplets** `1≤r,t,r'≤8` et, pour chaque triplet : congruence exacte, plus petit témoin positif `u>1`, triplets décimaux de départ et d'arrivée, déficit, variation de `J` et certificats universels pour la classe congruentielle. Il s'agit d'une **énumération de paramètres**, et non d'une distribution de probabilité sur les trajectoires.

Pour ces 512 familles :

- 376 impliquent une descente de `u` vers `w` pour chaque entier positif de la classe construite ;
- 136 impliquent au contraire une croissance de `u` vers `w` ;
- 136 familles imposent `ΔJ>0`, tandis que 376 imposent `ΔJ<0` ;
- les quatre combinaisons des signes de `D_corr` et `ΔJ` sont représentées :

| Signe du déficit | Signe de ΔJ | Familles parmi les 512 |
| --- | --- | ---: |
| D>0 | ΔJ<0 | 327 |
| D>0 | ΔJ>0 | 49 |
| D<0 | ΔJ<0 | 49 |
| D<0 | ΔJ>0 | 87 |

Ces chiffres sont **exacts pour ce domaine borné**. Ils n'ont aucune interprétation de fréquence temporelle universelle.

## 5. Quatre témoins explicites

| u | r | t | w | r' | Signe D_corr | Signe ΔJ |
| ---: | ---: | ---: | ---: | ---: | :---: | :---: |
| 3 | 2 | 3 | 1 | 1 | + | − |
| 7 | 3 | 1 | 13 | 1 | − | − |
| 9 | 1 | 1 | 7 | 3 | + | + |
| 27 | 2 | 1 | 31 | 5 | − | + |

Les exemples démontrent l'absence de dépendance monotone simple entre `J` et le déficit. En particulier, `27→31` réarme fortement le stock tout en augmentant le nombre.

## 6. Raccordement à la superposition décimale Φ–Ψ

Pour `u` donné, l'exactitude des cellules locales de base 1000 permet de reconstruire toutes les transitions `I^r P^t` sans stocker une trajectoire externe. La donnée initiale modulo `2^(r+t+r'+1)` suffit pour déterminer le mot `I^r P^t I^r' P`; les `s≥r+t+r'+1` derniers chiffres décimaux suffisent donc aussi, car `2^s | 10^s`.

Dans la matrice CSV, les colonnes `triplet_initial`, `triplet_suivant`, `alpha3_initial` relient les cellules de réarmement aux fenêtres terminales des lemmes 5.38 et 5.41. Le script vérifie tous les témoins par un moteur Φ–Ψ exact en base 1000, puis 50 000 autres entiers impairs de 3 à 100 001.

## 7. Identité de bord entre J et le déficit cumulé

Pour un départ impair `u_0` et un état impair ultérieur `u_K`, posons `r_j=ν₂(u_j+1)` et `α=log₂(3/2)`. Nous avons **exactement** :

    D_K = -(J(u_K)-J(u_0)) + α(r_K-r_0)
          + log₂[(1+1/u_K)/(1+1/u_0)].

Preuve : substituer `J(u)=log₂(u+1)+αr(u)` et simplifier. Cette identité est une équivalence algébrique ; elle souligne que `J` n'est **pas un second invariant global indépendant** du déficit. L'intérêt de `J` est opérationnel : toutes ses variations se concentrent sur les portes paires et rendent les événements de réarmement observables.

## 8. Suite de l'étude

Le résultat suivant qui pourrait être utile serait une **contrainte de taille de tête** pour une succession prolongée de corridors, formulée sur les variables `(q_j, r_j, t_j, r_{j+1})` et respectant toutes les congruences emboîtées. L'existence de tous les motifs finis interdit de prétendre qu'une certaine séquence locale de profondeurs est universellement impossible. Le problème restant est de contrôler les tailles et le déficit d'un *entier fixe* lorsque la profondeur temporelle croît.
