# Syracuse Φ–Ψ — Étude de compatibilité et certification du déficit (travail v15)

**Base :** complément v14, théorème 5.49 et corollaire 5.50. Cette note n'est pas une preuve de la conjecture de Syracuse. Les nombres de la matrice de modes à quatre états sont ceux de v14 ; les calculs suivants sont indépendants et reproductibles avec le script fourni.

## 1. Cadre

On ne considère que les états impairs positifs `u>1` et l'application d'un bloc impair à l'impair suivant :

`F(u) = (3u+1)/2^a`, `a = v2(3u+1)`.

Pour K blocs terminés avant une éventuelle arrivée à 1 :

`D_K = log2(u_0/u_K) = sum(a_j) - sum(log2(3+1/u_j))`.

Chaque triplet terminal fournit la profondeur *certifiée* `alpha_j = min(3,a_j)`. On pose `Amin=sum(alpha_j)`.

## 2. Théorème : toute suite finie de profondeurs est réalisable

Soit `(a_0,...,a_{K-1})`, avec tous les `a_j>=1`, et `A=sum(a_j)`.

Définir `B_0=0`, `A_0=0` et pour `j=0,...,K-1` :

- `B_{j+1}=3 B_j + 2^(A_j)` ;
- `A_{j+1}=A_j+a_j`.

Alors `F^K(u)=(3^K*u+B_K)/2^A` dès lors que les profondeurs prescrites sont effectivement celles de l'orbite.

Le résidu

`r = (2^A-B_K) * (3^K)^(-1) (mod 2^(A+1))`

est l'unique classe impaire modulo `2^(A+1)` réalisant exactement ce mot de profondeurs. Elle contient une infinité d'entiers positifs. L'énoncé se démontre par relèvement dyadique : pour une profondeur `a`, `3u+1=2^a v` avec `v` impair fixe une classe modulo `2^(a+1)` ; le transfert inverse est bijectif entre les classes impaires pertinentes, et chaque nouvelle profondeur impose `a` bits supplémentaires.

**Conclusion** : malgré l'élimination de chaînes fictives dans l'espace enrichi des modes `(B,p,c,r)`, *aucune suite finie de profondeurs strictement positives n'est interdite*. Une contrainte de compensation universelle ne peut donc porter seulement sur l'existence de préfixes finis de profondeurs.

Contre-exemple à un horizon universel : le départ `u_0=2^(K+1)-1` réalise `a_0=...=a_(K-1)=1`. Son déficit est négatif aux K premières étapes impair→impair. En faisant tendre K vers l'infini, les résidus initiaux tendent 2-adiquement vers `-1`, qui n'est pas un entier positif : cette limite ne démontre aucune trajectoire positive divergente.

## 3. Certificats du déficit : trois niveaux

### A — Borne universelle à partir des triplets terminaux

Si `u_j>=3` pour `0<=j<K`, alors

`D_K >= Amin - K*log2(10/3)`.

Le certificat peut être vérifié en **arithmétique entière**, sans logarithme :

`2^Amin * 3^K > 10^K`.

### B — Borne de tête, état par état

Si les têtes ou les chiffres connus garantissent `u_j>=ell_j>=3`, alors

`D_K >= Amin - sum_j log2(3+1/ell_j)`.

Certificat équivalent entièrement entier :

`2^Amin * product(ell_j) > product(3 ell_j+1)`.

**Exemple de 39 :**

- États : `39, 59, 89, 67, 101, 19`.
- Profondeurs exactes : `(1,1,2,1,4)` ; garanties à trois chiffres : `(1,1,2,1,3)`.
- `Amin=8` ; borne uniforme `-0,6848279708`.
- Bornes de têtes aux dizaines `ell=(30,50,80,60,100)` ; nouveau certificat `+0,0308673861`.
- Déficit exact `log2(39/19)=+1,0374747054`.

Ainsi un certificat devient positif *sans prolonger* le triplet terminal de 101 : la tête fournit l'information qui manquait au pied.

### C — Certificat conditionnel par la seule tête initiale

Supposons qu'aucun état impair n'ait encore été inférieur à `u_0`. Alors pour chaque `j<K`, `u_j>=u_0>=N`, et

`D_K >= Amin - K*log2(3+1/N)`.

La négation de la descente est donc impossible si

`2^Amin * N^K > (3N+1)^K`.

Même si une descente a déjà eu lieu, la propriété recherchée est satisfaite. Ainsi **le critère précédent garantit une première descente au plus tard au rang K** ; il ne garantit pas nécessairement `D_K>0` au dernier rang si une descente a déjà eu lieu avant.

Lorsqu'`Amin/K > log2(3)`, ce critère est satisfait pour tout départ assez grand :

`N > 1/(2^(Amin/K)-3)`.

Exemple `K=5`, `Amin=8` : le seuil est `N>31,813564...`; tout départ impair `u_0>=33` avec ce budget certifie une première descente au plus tard au cinquième bloc. Le départ 39 vérifie cette propriété.

## 4. Répartition exacte des profondeurs certifiées parmi les classes résiduelles

À chaque bloc impair→impair, `alpha=min(3,a)` prend les valeurs 1,2,3 avec les poids de densité naturelle `1/2,1/4,1/4` parmi les départs impairs. Pour tout nombre fini de blocs, les profondeurs successives ont la distribution *produit* : chaque mot exact de profondeurs `(a_0,...,a_(K-1))` occupe une unique classe modulo `2^(A+1)` et sa densité conditionnelle parmi les impairs vaut `2^(-A)`.

Avec `Y=alpha-1`, on obtient :

- `P(Y=0)=1/2`, `P(Y=1)=1/4`, `P(Y=2)=1/4` ;
- `E(Y)=3/4` et `Var(Y)=11/16` ;
- `E(alpha)=7/4=1,75` ;
- seuil universel `beta=log2(5/3)=0,736965594...` pour `sum(Y)>K beta`.

L'indépendance concerne **les classes initiales dans la limite de densité**, pas un phénomène de hasard attaché à une trajectoire déterministe.

La programmation dynamique exacte de l'événement « le budget a été positif au moins une fois dans les K premiers blocs » suit les poids `(2,1,1)/4` et élimine les états franchissant le seuil `sum(Y)>K beta`. Les résultats sont dans `PhiPsi_v15_Proportions_Certificats_Dyadiques.csv`.

| Nombre de blocs K | Couverture par budget uniforme, au moins une fois | Couverture asymptotique, départ suffisamment grand, par coefficient de tête |
|---:|---:|---:|
| 1 | 50,0000 % | 50,0000 % |
| 2 | 62,5000 % | 62,5000 % |
| 3 | 65,6250 % | 75,0000 % |
| 5 | 76,1719 % | 83,5938 % |
| 10 | 82,4898 % | 90,8569 % |
| 20 | 87,7273 % | 95,7584 % |
| 50 | 92,6365 % | 99,0587 % |
| 100 | 95,0828 % | 99,8490 % |
| 1000 | 99,0482 % | > 99,9999 % |

Ces pourcentages mesurent des **densités exactes à horizon fini** obtenues via les classes de résidus et les poids dyadiques, pas des fréquences garanties le long de chaque trajectoire. La deuxième colonne asymptotique n'est pas un certificat universel pour tous les petits entiers : elle mesure les mots qui acquièrent un certificat lorsque le départ initial est suffisamment grand.

L'écart positif `E(alpha)-log2(10/3)=0,0130344058...` implique, par la loi des grands nombres appliquée aux classes initiales, que les premiers certificats uniformes couvrent asymptotiquement une densité 1 des départs impairs. Cela **ne dit pas que chaque entier positif** obtient un certificat. L'ensemble non certifié peut être de densité nulle tout en restant infini.

## 5. Audit arithmétique de 50 000 départs impairs

Départs : `u_0=3,5,...,100001`. Les premières descentes ont été suivies sous `F`; les certificats acquis restent comptabilisés à tous les horizons supérieurs. Tous les calculs de certification sont faits par comparaisons entières.

| Horizon (blocs) | Départs ayant connu une descente | Certifiés par pied seul | Certifiés par pied + tête |
|---:|---:|---:|---:|
| 5 | 42 579 | 38 085 | 41 795 |
| 10 | 46 770 | 41 269 | 45 433 |
| 20 | 49 046 | 43 906 | 47 943 |

**Ce dénombrement est une vérification finie, pas une preuve de densité ni de convergence générale.**

## 6. État exact du problème

1. **Établi** : l'opérateur des modes temporels du complément v14 conserve l'origine des chaînes, et exclut les raccords fictifs.
2. **Établi** : aucune suite finie de profondeurs n'est impossible après projection depuis ces modes ; chaque suite se réalise sur une classe résiduelle infinie.
3. **Établi** : le budget universel est améliorable en exploitant les bornes de la tête ; la condition sur le départ initial `N` fournit un certificat de première descente après au plus K blocs.
4. **Établi** : la couverture en densité naturelle tend vers 1 pour les certificats de budget obtenus par triplets, par la combinatoire exacte des mots finis.
5. **Non démontré** : pour chaque entier positif fixé, une chaîne de blocs compatible atteint nécessairement un déficit positif. La densité 1 et la fidélité locale ne suffisent pas à conclure pour les exceptions éventuelles.

L'étape suivante consiste à étudier **les branches non certifiées après K blocs en les stratifiant par taille minimale de tête et mot complet de frontières**, plutôt que de chercher une interdiction universelle de certaines suites finies de profondeurs : elles sont toutes réalisables.

## 7. Reproductibilité

```bash
python3 Syracuse_PhiPsi_Etude_Chaines_Deficit_v15.py --max-k 1000 --small-limit 100001 --horizon 20 --output resultats_phi_psi_v15
```

Le programme utilise uniquement la bibliothèque standard de Python, produit trois CSV et contrôle par construction tous les mots de profondeurs `a_j ∈ {1,...,5}` de longueur 1 à 4.

## 8. Exemple de classification de toutes les chaînes au cinquième bloc

Pour `K=5`, les trois zones du budget `Amin=sum(min(3,a_j))` se séparent **exactement** :

- `Amin<=7` : `2^Amin<=3^5`. Le seul budget tronqué à trois ne certifie pas la descente, quelle que soit la taille de la tête. Cela ne signifie pas que les chaînes sont divergentes, ni qu'une descente antérieure n'a pas déjà eu lieu.
- `Amin=8` : `3^5<2^8`, mais `2^8<=(10/3)^5`. Pour certifier **une première descente au plus tard au rang 5**, la seule borne initiale `u_0>=33` suffit (si aucune descente antérieure n'a eu lieu, chaque état précédent est >=u_0).
- `Amin>=9` : `2^Amin>(10/3)^5`. Le déficit `D_5` est strictement positif tant que les cinq blocs se déroulent avant la première arrivée à 1.

Parmi les mots de valeurs tronquées possibles à cinq blocs (pondérés par les classes résiduelles initiales), les parts de ces trois catégories sont respectivement `272/1024 = 26,5625 %`, `200/1024 = 19,53125 %` et `552/1024 = 53,90625 %`.

La **couverture cumulée avant ou au rang 5** est différente de cette classification au dernier rang, car un certificat peut avoir été acquis dès un préfixe antérieur : `76,171875 %` pour la borne uniforme et `83,59375 %` à taille initiale suffisamment grande.
