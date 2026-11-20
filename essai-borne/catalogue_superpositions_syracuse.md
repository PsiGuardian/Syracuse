# Syracuse — Catalogue des superpositions et de leurs durées

Une opération brute est soit un calcul de 3n + 1, soit une division par 2. Une transition entre impairs de valuation a coûte a + 1 opérations brutes. On s'arrête à l'arrivée à 1. Les maxima par longueur ci-dessous concernent des départs impairs strictement supérieurs à 1.

## Le recouvrement d'une ligne de chiffres avec la suivante

Numérotons les chiffres depuis les unités. Pour 3n + 1, le chiffre d_i et la retenue entrante c_i donnent e_i = (3d_i + c_i) mod 10 et c_{i+1} = ⌊(3d_i + c_i)/10⌋. La retenue initiale c_0 vaut 1. Les retenues suivantes appartiennent à {0, 1, 2}. Deux fenêtres de trois chiffres qui se chevauchent doivent donc transmettre la même retenue sur leur bord commun.

Pour /2, le chiffre de quotient à la position i vaut ⌊e_i/2⌋ + 5(e_{i+1} mod 2), avec un zéro au-delà de la tête de la ligne. Le chiffre supérieur e_{i+1} fournit le report. Les deux règles couvrent chaque fenêtre locale par substitution. Elles s'appliquent à chaque nouvelle ligne, en retirant les zéros en tête. Après le premier /2, un quotient pair impose une division supplémentaire. Une seule division ramène à un impair exactement quand le départ est congru à 3 modulo 4.

Exemple au franchissement de 10²⁶. Le départ se termine par 287. Depuis les unités, 3×7+1 donne 22, 3×8+2 donne 26, et 3×2+2 donne 8. Le résultat se termine bien par 862. La retenue commune est propagée de position en position. Le report de division donne une unité 1 et la baisse suivante ramène le nombre à 26 chiffres.

| Impair de départ | Valeur brute 3n + 1 | Valuation | Impair obtenu |
|---:|---:|---:|---:|
| 24 911 558 240 340 082 488 338 191 | 74 734 674 721 020 247 465 014 574 | 1 | 37 367 337 360 510 123 732 507 287 |
| 37 367 337 360 510 123 732 507 287 | **112 102 012 081 530 371 197 521 862** | 1 | 56 051 006 040 765 185 598 760 931 |
| 56 051 006 040 765 185 598 760 931 | 168 153 018 122 295 556 796 282 794 | 1 | 84 076 509 061 147 778 398 141 397 |
| 84 076 509 061 147 778 398 141 397 | **252 229 527 183 443 335 194 424 192** | 7 | 1 970 543 181 120 651 056 206 439 |

L'audit antérieur donne les valeurs et rangs des 42 blocs jusqu'au pic. [audit_syracuse_13_vers_27.md](https://chatgpt.com/library?file_id=libfile_0b570557869481919baf60e5e9b38dd5&account_id=personal)

## Les blocs (k,a) et leurs trois formes

Un bloc (k,a) comprend k valuations 1 puis une valuation de sortie a ≥ 2. Il dure 2k + 1 + a opérations brutes et k + 1 transitions entre impairs. Un bloc (0,a) descend immédiatement sous son départ. Un bloc (k,2) avec k ≥ 1 finit au-dessus du départ. Pour k ≥ 1 et a ≥ 3, le bloc finit sous son départ n exactement quand (2^(k+a) − 3^(k+1))n > 3^(k+1) − 2^(k+1).

On calcule le bloc directement en écrivant n + 1 = 2^(k+1)q avec q impair. On a k = v₂(n+1) − 1 et a = 1 + v₂(3^(k+1)q − 1). Cela donne la règle exhaustive pour un premier bloc à x chiffres. Pour chaque k, chaque a correspond à une seule classe donnée par

[
qequiv 3^{-(k+1)}(1+2^{a-1})pmod{2^a},qquad n=2^{k+1}q-1.
]

L'inverse est pris modulo 2^a. En notant q₀ le représentant de cette classe, le bloc existe à la longueur x si la classe n ≡ 2^(k+1)q₀ − 1 (mod 2^(k+a+1)) rencontre l'intervalle de départ. Il suffit d'essayer 0 ≤ k ≤ ⌊log₂(10^x)⌋ − 1, puis 2 ≤ a ≤ ⌊log₂(3^(k+1)⌊10^x/2^k⌋ − 2)⌋. Ce dernier majorant utilise la valeur brute maximale possible pour ce k. L'inégalité k ≤ ⌊log₂(10^x)⌋ − 1 est atteinte au départ 2^⌊log₂(10^x)⌋ − 1.

## Durées maximales exactes pour 1 à 21 chiffres

Les colonnes « k max » et « a max » sont des maxima pris séparément. La durée maximale est calculée pour une paire réellement admissible. Le préfixe commun désigne le nombre d'opérations brutes correspondant aux valuations terminées et identiques, pour deux départs distincts de même longueur.

| x | Paires admissibles | k max | a max | Durée brute maximale d'un premier bloc | Un départ qui atteint ce maximum | Durée maximale d'un préfixe commun |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 2 | 4 | 7 | 3 | 2 |
| 2 | 21 | 5 | 8 | 15 | 63 | 9 |
| 3 | 44 | 8 | 10 | 21 | 255 | 15 |
| 4 | 80 | 12 | 14 | 28 | 4 095 | 23 |
| 5 | 129 | 15 | 18 | 38 | 65 535 | 29 |
| 6 | 185 | 18 | 22 | 39 | 262 143 | 35 |
| 7 | 259 | 22 | 24 | 47 | 4 194 303 | 42 |
| 8 | 335 | 25 | 28 | 55 | 67 108 863 | 49 |
| 9 | 425 | 28 | 30 | 60 | 268 435 455 | 55 |
| 10 | 530 | 32 | 34 | 71 | 4 294 967 295 | 63 |
| 11 | 643 | 35 | 38 | 76 | 68 719 476 735 | 69 |
| 12 | 769 | 38 | 40 | 79 | 274 877 906 943 | 75 |
| 13 | 905 | 42 | 44 | 87 | 4 398 046 511 103 | 83 |
| 14 | 1050 | 45 | 48 | 95 | 70 368 744 177 663 | 89 |
| 15 | 1201 | 48 | 50 | 102 | 281 474 976 710 655 | 95 |
| 16 | 1379 | 52 | 54 | 108 | 4 503 599 627 370 495 | 102 |
| 17 | 1553 | 55 | 58 | 117 | 72 057 594 037 927 935 | 109 |
| 18 | 1741 | 58 | 60 | 119 | 288 230 376 151 711 743 | 115 |
| 19 | 1952 | 62 | 64 | 127 | 4 611 686 018 427 387 903 | 122 |
| 20 | 2163 | 65 | 68 | 136 | 18 446 744 073 709 551 615 | 129 |
| 21 | 2385 | 68 | 70 | 140 | 295 147 905 179 352 825 855 | 135 |

## Enchaîner plusieurs blocs

Un mot de m valuations (a₁, …, aₘ) impose une seule classe de départ modulo 2^(s+1), où s = a₁ + … + aₘ. Le mot dure exactement m+s opérations brutes. Pour prolonger un préfixe, écrivons le départ n = r + 2^(s+1)t et son image impaire u + 2·3^m t. La prochaine valuation vaut a exactement si

\[
(3u+1)/2 + 3^{m+1}t\equiv 2^{a-1}\pmod{2^a}.
\]

Le coefficient de t est impair, ce qui donne une unique classe de t à intersecter avec l'intervalle des départs. Pour un préfixe vide, on part de r = u = 1, m = s = 0. Pour une classe donnée, la plus grande image impaire admissible borne les valeurs de a à essayer via la longueur binaire de son 3n + 1. En recalculant ces contraintes à chaque prolongement, on peut énumérer exhaustivement les mots compatibles avec x chiffres jusqu'à une profondeur fixée. Si une image atteint 1, on clôt la trajectoire de ce départ.

Pour un mot constitué de blocs (k_i,a_i), m = Σ(k_i+1) et s = Σ(k_i+a_i). En laissant varier le nombre de chiffres, toute liste finie de valuations positives est réalisable. Sa classe contient des départs arbitrairement grands, dont les images aux étapes du préfixe sont elles aussi arbitrairement grandes. La présence d'un bloc au début d'une chaîne ne dispense donc jamais de vérifier sa compatibilité avec les précédents à longueur fixée.

Si deux départs de même longueur partagent le mot, ils diffèrent d'au moins 2^(s+1). En notant W la distance entre les extrémités impaires de l'intervalle de départ, on obtient s ≤ S = ⌊log₂ W⌋ − 1 et m+s ≤ 2S. Pour calculer exactement le maximum commun, on essaie dans cet ordre S valuations 1, puis toutes les suites de somme S avec un seul 2 et S−2 valuations 1, puis S−1 valuations 1. Dans le dernier cas le module vaut 2^S et la largeur W vaut au moins deux fois ce module, donc deux départs existent. Les trois tests donnent respectivement les durées 2S, 2S−1 et 2S−2.

Cette durée borne la période pendant laquelle deux départs peuvent partager des valuations entièrement terminées. Une classe devenue singleton peut continuer à produire des blocs. Pour borner le premier retour sous le départ, il faut conserver dans chaque classe les points dont l'image reste à hauteur du départ, puis montrer que toutes ces classes s'épuisent avant un horizon donné. Ce catalogue ne certifie pas cet horizon général.

## Mots vérifiés sur les trajectoires étudiées

### Départ 9 016 346 070 511

Le pic intervient au rang 356. Le premier retour sous le départ survient au rang 530. L'arrivée à 1 survient au rang 886. Le mot complet compte 131 blocs. Les 42 premiers blocs vont jusqu'au pic, divisions de sa sortie comprises.

```text
(3,2), (2,2), (0,2), (7,2), (4,2), (7,2), (1,3), (2,2), (4,2), (0,2), (0,2), (2,2)
(3,2), (0,2), (6,4), (1,2), (1,2), (13,2), (1,2), (2,2), (0,2), (3,3), (2,3), (1,2)
(7,2), (0,3), (2,2), (3,2), (2,2), (6,2), (0,2), (2,2), (2,2), (6,2), (7,2), (1,2)
(1,2), (3,2), (0,2), (1,2), (2,2), (3,7), (2,2), (3,9), (3,3), (1,2), (2,2), (2,12)
(0,2), (0,3), (2,2), (0,3), (2,4), (0,2), (1,2), (1,5), (0,5), (0,2), (0,2), (1,2)
(1,5), (1,3), (0,2), (1,3), (0,5), (1,3), (0,6), (0,2), (1,2), (2,3), (1,2), (0,3)
(0,2), (1,2), (0,2), (2,3), (1,4), (3,2), (2,2), (0,3), (0,3), (0,3), (0,2), (2,2)
(0,2), (2,2), (1,2), (2,3), (1,2), (0,4), (0,4), (1,2), (2,2), (5,3), (1,2), (2,5)
(0,2), (1,3), (0,2), (3,2), (0,4), (2,4), (1,2), (0,2), (0,5), (0,3), (2,2), (0,3)
(0,2), (2,2), (1,2), (1,4), (0,2), (2,3), (0,3), (1,3), (0,10), (0,2), (1,2), (2,3)
(0,3), (1,2), (1,3), (0,2), (1,3), (2,3), (0,4), (1,3), (1,2), (0,3), (0,4)
```

### Départ 319 804 831

Le pic intervient au rang 167. Le premier retour sous le départ survient au rang 427. L'arrivée à 1 survient au rang 592. Le mot complet compte 80 blocs. Les 15 premiers blocs vont jusqu'au pic, divisions de sa sortie comprises.

```text
(4,2), (1,2), (7,2), (0,2), (0,2), (0,2), (7,2), (2,2), (2,2), (0,2), (6,2), (20,2)
(3,2), (2,2), (8,4), (0,5), (3,2), (0,3), (0,5), (0,3), (1,2), (1,2), (1,2), (1,5)
(6,2), (3,4), (0,2), (3,2), (7,2), (0,2), (1,4), (2,3), (2,3), (0,2), (5,3), (0,7)
(1,2), (2,4), (0,2), (0,5), (0,3), (0,3), (2,7), (0,2), (0,2), (2,2), (0,2), (2,5)
(0,2), (4,3), (1,3), (0,3), (0,7), (0,2), (5,5), (0,2), (1,2), (1,3), (1,3), (0,3)
(4,3), (2,5), (0,3), (0,3), (4,4), (1,3), (2,2), (2,3), (1,4), (0,2), (0,2), (0,2)
(0,2), (0,4), (1,5), (0,3), (0,3), (1,2), (0,3), (0,4)
```

### Départ 4 618 299 559 407

Le pic intervient au rang 77. Le premier retour sous le départ survient au rang 163. L'arrivée à 1 survient au rang 580. Le mot complet compte 91 blocs. Les 8 premiers blocs vont jusqu'au pic, divisions de sa sortie comprises.

```text
(3,2), (2,2), (0,2), (7,2), (4,2), (7,2), (1,3), (3,5), (0,2), (3,2), (0,6), (0,2)
(1,2), (0,2), (0,2), (1,2), (0,2), (2,2), (1,5), (3,2), (0,3), (2,4), (0,3), (0,6)
(2,4), (0,3), (4,2), (1,2), (0,2), (0,3), (0,2), (3,2), (0,2), (0,2), (1,2), (0,4)
(0,2), (0,2), (0,2), (4,2), (0,3), (0,2), (1,7), (1,3), (4,2), (0,2), (0,2), (0,4)
(2,3), (3,4), (0,7), (0,3), (0,2), (0,2), (1,2), (0,2), (4,3), (3,4), (2,2), (0,3)
(0,3), (2,2), (0,3), (3,2), (1,3), (4,5), (2,4), (3,2), (0,3), (0,2), (1,4), (2,4)
(0,2), (0,3), (0,2), (4,2), (0,2), (1,2), (2,2), (3,2), (0,3), (2,2), (1,2), (5,3)
(3,4), (0,2), (0,2), (0,4), (0,3), (2,5), (0,4)
```

## Catalogue exhaustif des premiers blocs pour 1 à 21 chiffres

Chaque ligne donne k puis les valeurs admissibles de a. Un intervalle a–b inclut les deux bornes.

### 1 chiffre

```text
0: 2, 4
1: 4
2: 2
```

### 2 chiffres

```text
0: 2–6, 8
1: 2–6
2: 2–5
3: 2–3, 5
4: 2, 4
5: 4
```

### 3 chiffres

```text
0: 2–10
1: 2–8, 10
2: 2–7, 10
3: 2–6, 8
4: 2–6
5: 2–3, 6
6: 2–3, 6
7: 2, 6
8: 2
```

### 4 chiffres

```text
0: 2–12, 14
1: 2–12
2: 2–10, 12
3: 2–9, 12
4: 2–8, 12
5: 2–7, 9
6: 2–6, 9
7: 2–5, 7
8: 2–4, 7
9: 2–5
10: 2, 5
11: 5
12: 2
```

### 5 chiffres

```text
0: 2–16, 18
1: 2–16
2: 2–13, 15
3: 2–12, 15
4: 2–11, 13
5: 2–12
6: 2–10
7: 2–10
8: 2–8
9: 2–8
10: 2–6
11: 2–4, 9
12: 2–5
13: 2–4
14: 2, 7
15: 7
```

### 6 chiffres

```text
0: 2–20
1: 2–18, 22
2: 2–18
3: 2–17
4: 2–15, 17
5: 2–13, 15
6: 2–13
7: 2–12, 18
8: 2–12
9: 2–11
10: 2–10
11: 2–8
12: 2–7, 11
13: 2–7
14: 2–5
15: 2–4
16: 2–4
17: 2, 4
18: 2
```

### 7 chiffres

```text
0: 2–22, 24
1: 2–21, 23
2: 2–20, 23
3: 2–21
4: 2–18, 21
5: 2–19
6: 2–18
7: 2–16
8: 2–15
9: 2–13, 17
10: 2–13
11: 2–11, 13
12: 2–10, 12
13: 2–10
14: 2–8, 10
15: 2–8
16: 2–7
17: 2–6
18: 2–5, 7
19: 2–5
20: 2, 4
21: 4
22: 2
```

### 8 chiffres

```text
0: 2–26, 28
1: 2–24, 28
2: 2–23, 28
3: 2–23, 28
4: 2–22
5: 2–22
6: 2–20, 22
7: 2–19
8: 2–18
9: 2–16, 19
10: 2–15, 19
11: 2–15
12: 2–14
13: 2–13
14: 2–12, 14
15: 2–12
16: 2–10, 13
17: 2–8, 13
18: 2–7, 13
19: 2–7
20: 2–6
21: 2–4, 6
22: 2–4, 6
23: 2–3, 6
24: 2
25: 4
```

### 9 chiffres

```text
0: 2–30
1: 2–27, 29
2: 2–27
3: 2–26
4: 2–26
5: 2–24, 29
6: 2–24
7: 2–22, 25
8: 2–22
9: 2–20, 23
10: 2–18, 23
11: 2–18, 23
12: 2–17, 23
13: 2–15, 17
14: 2–15, 17
15: 2–14, 16
16: 2–12, 16
17: 2–12
18: 2–11
19: 2–11
20: 2–9, 11
21: 2–8, 11
22: 2–7, 9
23: 2–5, 9
24: 2–5, 9
25: 2–3, 5
26: 2–3, 5
27: 2, 5
28: 2
```

### 10 chiffres

```text
0: 2–32, 34
1: 2–31, 34
2: 2–31
3: 2–30
4: 2–29
5: 2–28
6: 2–27
7: 2–26
8: 2–24, 26
9: 2–24
10: 2–22, 29
11: 2–22
12: 2–21
13: 2–19, 21
14: 2–19
15: 2–18
16: 2–16, 18
17: 2–15, 18
18: 2–14, 18
19: 2–13, 18
20: 2–12, 14
21: 2–11, 14
22: 2–10, 14
23: 2–10
24: 2–8, 12
25: 2–7, 12
26: 2–7
27: 2–5, 7
28: 2–5
29: 2–4, 8
30: 2, 8
31: 8
32: 2
```

### 11 chiffres

```text
0: 2–36, 38
1: 2–35
2: 2–34
3: 2–32, 34
4: 2–32
5: 2–31
6: 2–30, 32
7: 2–30
8: 2–29
9: 2–27, 29
10: 2–26
11: 2–24, 26
12: 2–23, 26
13: 2–23, 26
14: 2–22, 26
15: 2–21
16: 2–21
17: 2–19
18: 2–17, 22
19: 2–17
20: 2–16, 19
21: 2–15
22: 2–13, 16
23: 2–12, 16
24: 2–11, 13
25: 2–11
26: 2–9, 11
27: 2–9
28: 2–8, 12
29: 2–7
30: 2–6
31: 2–5
32: 2–4, 6
33: 2–4
34: 2
35: 5
```

### 12 chiffres

```text
0: 2–40
1: 2–38, 40
2: 2–36, 38
3: 2–37
4: 2–36
5: 2–34, 38
6: 2–34
7: 2–33
8: 2–31, 33
9: 2–30, 32
10: 2–28, 32
11: 2–29
12: 2–28
13: 2–25, 28
14: 2–25
15: 2–25
16: 2–23, 26
17: 2–22, 26
18: 2–21
19: 2–21
20: 2–18, 20
21: 2–19
22: 2–18
23: 2–15, 18
24: 2–16
25: 2–15
26: 2–12, 14
27: 2–13
28: 2–11
29: 2–11
30: 2–9, 11
31: 2–7, 9
32: 2–7, 9
33: 2–6, 8
34: 2–5, 8
35: 2–4
36: 2–4
37: 2, 4
38: 2
```

### 13 chiffres

```text
0: 2–42, 44
1: 2–42
2: 2–41
3: 2–40
4: 2–39
5: 2–37, 40
6: 2–36, 40
7: 2–36
8: 2–34, 37
9: 2–34
10: 2–32, 34
11: 2–32
12: 2–30, 32
13: 2–29, 32
14: 2–28, 30
15: 2–28
16: 2–26, 28
17: 2–25, 27
18: 2–25
19: 2–23, 26
20: 2–23
21: 2–22
22: 2–21
23: 2–20
24: 2–18, 20
25: 2–17, 20
26: 2–17
27: 2–15, 19
28: 2–14, 19
29: 2–13, 19
30: 2–12, 19
31: 2–11, 19
32: 2–10, 12
33: 2–10
34: 2–8, 10
35: 2–7, 10
36: 2–6, 8
37: 2–6
38: 2–4, 6
39: 2–4, 6
40: 2, 4
41: 4
42: 2
```

### 14 chiffres

```text
0: 2–46, 48
1: 2–46
2: 2–44, 46
3: 2–43
4: 2–41, 45
5: 2–40, 45
6: 2–39, 41
7: 2–40
8: 2–38
9: 2–37
10: 2–36
11: 2–35, 37
12: 2–33, 37
13: 2–32, 37
14: 2–32, 37
15: 2–31, 37
16: 2–29, 31
17: 2–29
18: 2–28
19: 2–26, 28
20: 2–26
21: 2–24, 26
22: 2–23, 25
23: 2–22, 25
24: 2–22
25: 2–20, 22
26: 2–20
27: 2–18, 23
28: 2–18
29: 2–17
30: 2–16
31: 2–15
32: 2–14, 16
33: 2–14
34: 2–11, 13
35: 2–10, 13
36: 2–10, 13
37: 2–8, 10
38: 2–9
39: 2–7
40: 2–7
41: 2–5
42: 2–5
43: 2–3, 5
44: 2
45: 4
```

### 15 chiffres

```text
0: 2–50
1: 2–48
2: 2–48
3: 2–46, 49
4: 2–44, 49
5: 2–44
6: 2–43, 46
7: 2–41, 46
8: 2–41
9: 2–40
10: 2–39
11: 2–39
12: 2–36, 38
13: 2–36
14: 2–35
15: 2–34
16: 2–33, 35
17: 2–33
18: 2–31, 34
19: 2–31
20: 2–29, 31
21: 2–27, 29
22: 2–27
23: 2–27
24: 2–25, 28
25: 2–24
26: 2–23, 25
27: 2–22
28: 2–22
29: 2–20, 22
30: 2–18, 20
31: 2–18
32: 2–18
33: 2–16
34: 2–15
35: 2–15
36: 2–12, 14
37: 2–13
38: 2–10, 13
39: 2–10
40: 2–9, 12
41: 2–9
42: 2–6, 8
43: 2–6, 8
44: 2–5, 7
45: 2–3, 7
46: 2–3, 7
47: 2, 7
48: 2
```

### 16 chiffres

```text
0: 2–52, 54
1: 2–52
2: 2–51
3: 2–50
4: 2–48, 51
5: 2–48
6: 2–47
7: 2–45, 48
8: 2–45
9: 2–43, 45
10: 2–43
11: 2–42
12: 2–40, 42
13: 2–40
14: 2–39
15: 2–37, 39
16: 2–36, 39
17: 2–35, 37
18: 2–34, 37
19: 2–33, 37
20: 2–32, 37
21: 2–31, 37
22: 2–30, 37
23: 2–30
24: 2–29
25: 2–28
26: 2–27
27: 2–26
28: 2–25
29: 2–24
30: 2–22, 24
31: 2–21, 24
32: 2–21
33: 2–20
34: 2–19
35: 2–18
36: 2–17
37: 2–15, 18
38: 2–15
39: 2–13, 16
40: 2–12, 16
41: 2–11, 16
42: 2–10, 12
43: 2–10
44: 2–8, 11
45: 2–7, 11
46: 2–6, 8
47: 2–6
48: 2–4, 6
49: 2–4
50: 2, 5
51: 5
52: 2
```

### 17 chiffres

```text
0: 2–56, 58
1: 2–54, 58
2: 2–54
3: 2–53
4: 2–51, 53
5: 2–50, 53
6: 2–49, 51
7: 2–48, 51
8: 2–47, 51
9: 2–47, 51
10: 2–46, 51
11: 2–45
12: 2–45
13: 2–43, 45
14: 2–42
15: 2–42
16: 2–40
17: 2–40
18: 2–38
19: 2–36, 41
20: 2–36
21: 2–35
22: 2–34
23: 2–32, 34
24: 2–31, 34
25: 2–30, 32
26: 2–30
27: 2–29
28: 2–28
29: 2–26, 28
30: 2–26
31: 2–24, 26
32: 2–24
33: 2–22, 24
34: 2–21, 23
35: 2–20, 23
36: 2–19, 23
37: 2–19
38: 2–17, 19
39: 2–17
40: 2–15, 20
41: 2–15
42: 2–14, 17
43: 2–12, 17
44: 2–11, 17
45: 2–10, 12
46: 2–11
47: 2–10
48: 2–7, 9
49: 2–7
50: 2–5, 7
51: 2–4, 6
52: 2–5
53: 2–4
54: 2
55: 6
```

### 18 chiffres

```text
0: 2–60
1: 2–57, 59
2: 2–56, 59
3: 2–56, 59
4: 2–55, 59
5: 2–54, 56
6: 2–54
7: 2–52, 55
8: 2–50, 55
9: 2–50
10: 2–49
11: 2–49
12: 2–47
13: 2–47
14: 2–45, 48
15: 2–44
16: 2–43, 45
17: 2–41, 45
18: 2–42
19: 2–40
20: 2–38, 40
21: 2–38, 40
22: 2–36, 38
23: 2–37
24: 2–36
25: 2–35
26: 2–33, 35
27: 2–32, 34
28: 2–30, 34
29: 2–31
30: 2–30
31: 2–27, 29
32: 2–28
33: 2–25, 28
34: 2–25
35: 2–25
36: 2–22, 24
37: 2–22, 24
38: 2–21
39: 2–20, 23
40: 2–19
41: 2–17, 19
42: 2–16, 18
43: 2–16
44: 2–15
45: 2–14, 16
46: 2–12, 16
47: 2–13
48: 2–10, 13
49: 2–11
50: 2–8, 11
51: 2–8
52: 2–7
53: 2–6, 8
54: 2–6
55: 2–4
56: 2, 4
57: 2, 4
58: 2
```

### 19 chiffres

```text
0: 2–62, 64
1: 2–61, 64
2: 2–60, 64
3: 2–60
4: 2–58, 62
5: 2–58
6: 2–56, 59
7: 2–54, 59
8: 2–54, 56
9: 2–54
10: 2–52, 54
11: 2–51, 54
12: 2–50, 54
13: 2–50
14: 2–47, 49
15: 2–48
16: 2–47
17: 2–45, 47
18: 2–45
19: 2–44
20: 2–43
21: 2–41, 43
22: 2–40, 43
23: 2–40
24: 2–38, 42
25: 2–37, 42
26: 2–37
27: 2–36
28: 2–34, 36
29: 2–34
30: 2–33
31: 2–32
32: 2–30, 33
33: 2–30
34: 2–28, 31
35: 2–28
36: 2–27
37: 2–26
38: 2–24, 28
39: 2–23, 28
40: 2–22, 28
41: 2–21, 23
42: 2–21
43: 2–19, 21
44: 2–19
45: 2–18
46: 2–16, 18
47: 2–16
48: 2–15
49: 2–14
50: 2–12, 16
51: 2–12
52: 2–11
53: 2–9, 14
54: 2–9
55: 2–8
56: 2–6, 8
57: 2–5, 7
58: 2–5
59: 2–3, 5
60: 2, 4
61: 4
62: 2
```

### 20 chiffres

```text
0: 2–66, 68
1: 2–65
2: 2–63, 66
3: 2–62, 66
4: 2–61, 63
5: 2–61
6: 2–60
7: 2–58, 61
8: 2–58
9: 2–56, 59
10: 2–57
11: 2–55
12: 2–53, 56
13: 2–52, 56
14: 2–51, 56
15: 2–50, 52
16: 2–50
17: 2–49, 54
18: 2–49
19: 2–47, 49
20: 2–46
21: 2–46
22: 2–44
23: 2–43
24: 2–41, 44
25: 2–41
26: 2–39, 41
27: 2–38, 41
28: 2–38, 41
29: 2–37, 41
30: 2–36, 41
31: 2–35
32: 2–34
33: 2–32, 34
34: 2–32
35: 2–31
36: 2–29, 31
37: 2–29
38: 2–27, 34
39: 2–27
40: 2–26
41: 2–25
42: 2–25
43: 2–22, 24
44: 2–23
45: 2–21
46: 2–21
47: 2–19, 21
48: 2–18
49: 2–17
50: 2–15, 18
51: 2–14, 18
52: 2–15
53: 2–13
54: 2–11, 13
55: 2–12
56: 2–9, 12
57: 2–9
58: 2–8
59: 2–7, 9
60: 2–5, 9
61: 2–4, 9
62: 2–3, 9
63: 2–3, 9
64: 2
65: 4
```

### 21 chiffres

```text
0: 2–70
1: 2–68, 70
2: 2–67, 69
3: 2–65, 69
4: 2–66
5: 2–63, 66
6: 2–63
7: 2–63
8: 2–61, 63
9: 2–60, 62
10: 2–60
11: 2–57, 59
12: 2–57, 59
13: 2–55, 57
14: 2–55
15: 2–54, 61
16: 2–54
17: 2–52
18: 2–50, 52
19: 2–50, 52
20: 2–49, 51
21: 2–48
22: 2–47, 49
23: 2–47
24: 2–46
25: 2–44
26: 2–43
27: 2–43
28: 2–40, 42
29: 2–40
30: 2–39
31: 2–39
32: 2–37, 39
33: 2–36, 39
34: 2–35, 39
35: 2–34, 36
36: 2–34
37: 2–32, 34
38: 2–31
39: 2–29, 31
40: 2–29, 31
41: 2–28, 30
42: 2–27
43: 2–26
44: 2–25
45: 2–24
46: 2–23, 25
47: 2–23
48: 2–22
49: 2–21
50: 2–19, 23
51: 2–17, 23
52: 2–18
53: 2–17
54: 2–14, 16
55: 2–14
56: 2–14
57: 2–12
58: 2–12
59: 2–10, 13
60: 2–8, 13
61: 2–8
62: 2–7
63: 2–6
64: 2–6
65: 2–3, 5
66: 2, 5
67: 2, 5
68: 2
```

## Références dans l'inventaire

Le lemme 5.38 traite des triplets décimaux chevauchants. La proposition 5.47 porte sur le transport des contraintes dyadiques entre blocs et le théorème 5.49 sur le prolongement temporel. Les lemmes 7.1 et 7.5 du recueil R01 concernent la formulation affine et le cylindre congruentiel. [Inventaire des lemmes](https://chatgpt.com/library?file_id=libfile_46f89cf2bef08191aa60659c5329dfb0&account_id=personal)
