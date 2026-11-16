# Syracuse Φ–Ψ — Étude des excursions mixtes v17

**Statut : annexe scientifique autonome.** Les théorèmes, dénombrements et expériences de ce complément ne démontrent **ni** la convergence universelle de Syracuse, **ni** l'inexistence de cycles non terminaux, **ni** l'impossibilité générale d'une divergence positive.

## Contenu

- `Syracuse_PhiPsi_Excursions_Mixtes_v17.pdf` (5 pages) : définitions, théorèmes, preuve du certificat double, contre-exemple méthodologique du mot critique supérieur, tableaux et figures.
- `Syracuse_PhiPsi_Excursions_Mixtes_v17.tex` : LaTeX intégralement éditable.
- `Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf` (32 pages) : le PDF de 27 pages **fourni dans cette conversation** suivi de l'annexe v17. Cette compilation n'est pas un remplacement intégral des anciennes versions v14–v16 ; elle conserve simplement le document réellement accessible ici.
- `Syracuse_PhiPsi_Laboratoire_Excursions_Mixtes_v17.html` : explorateur autonome des sept familles, 300 horizons chacune, export CSV, sans serveur. Les entiers exacts pré-calculés sont embarqués dans le HTML.
- `phi_psi_mixed_excursions_v17.py` : générateur Python 3 standard, sans dépendance Python externe.
- `Donnees/PhiPsi_v17_Classification_Exhaustive.csv` : 199 287 motifs bornés répartis sur K = 1 à 5, paramètres entre 1 et 3.
- `Donnees/PhiPsi_v17_Excursions_Mixtes_Echantillons.csv` : horizons sélectionnés des sept familles.
- `Donnees/PhiPsi_v17_*_classes.csv` : 300 classes par famille, soit 2 100 états temporels exacts ; entiers stockés en colonnes texte.
- `Donnees/PhiPsi_v17_Bilan.json` : audit de référence.
- `Figures/*.png` : progression du coût initial et frontière multiplicative critique.
- `SHA256SUMS.txt` : contrôle d'intégrité de l'archive.

## Résultats arithmétiques exacts

Pour un mot de corridors `(r0,t0,...,rK-1,tK-1,rK)`, la matrice affine calcule `D_K q_K=A_K q_0+C_K`, puis le résidu `q_0≡(D_K-C_K) A_K^{-1} (mod 2D_K)` et le plus petit témoin initial non terminal `q0_min(K)`.

La descente sous la valeur initiale au rang `j` est exactement `(2^(R_j+T_j)-3^R_j) q0 > C_j`. Le plafond de **non-descente à tous les rangs 1..K** est le minimum des `floor(C_j/G_j)` lorsque `G_j>0`, avec `G_j=2^(R_j+T_j)-3^R_j`. Nous conservons la convention `Q_K=∞` lorsque tous les `G_j≤0`. La fenêtre `[q0_min(K), Q_K]` se referme monotoniquement : son bas ne décroît pas, son haut ne croît pas.

**Mot adversarial critique supérieur** : `r_j=1+ceil((j+1)θ)-ceil(jθ)`, `t_j=1`, `θ=1/log2(3/2)-1`. Chaque préfixe est strictement multiplicativement expansif, mais le mot n'est pas ultimement périodique et la plus longue suite consécutive `(2,1)` est de trois corridors. Ses 300 premiers horizons sont calculés : à K=300 le plus petit quotient initial compatible possède 814 bits. **La divergence de ce minimum à l'horizon infini n'est pas démontrée.**

## Installation et reproduction sur Arch Linux

Python standard suffit :

```bash
python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 5 --max-rt 3 --path-horizon 300
```

L'exécution contrôle 250 mots aléatoires, 12 000 combinaisons indépendantes par énumération de petits témoins, des transmissions Φ–Ψ sur blocs de base 1000 et les congruences de 199 287 motifs.

Pour visualiser les séries sans outil supplémentaire, ouvrir le fichier HTML local dans Firefox ou Chromium et utiliser le curseur de profondeur.

## Ce qui reste ouvert

- L'exclusion d'une trajectoire positive non terminale infinie, cyclique ou divergente.
- L'évolution de `q0_min(K)` pour le mot critique supérieur lorsque `K→∞`.
- Une contrainte temporelle **globale** qui force la fermeture du certificat double ou la fuite du plus petit représentant pour toutes les suites compatibles.
