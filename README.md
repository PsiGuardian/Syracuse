# SYRACUSE

### Une exploration structurelle et multidimensionnelle de la conjecture de Collatz

**Mathématiques · Théorie des nombres · Systèmes dynamiques discrets · Recherche algorithmique**

*Une transformation élémentaire. Une dynamique complexe. Une architecture mathématique à explorer.*

**[🇫🇷 Français](README.md)  ·  [🇬🇧 English](README.en.md)  ·  [🇩🇪 Deutsch](README.de.md)  ·  [🇪🇸 Español](README.es.md)  ·  [🇮🇱 עברית](README.he.md)  ·  [🇯🇵 日本語](README.ja.md)  ·  [🇨🇳 简体中文](README.zh-CN.md)  ·  [🇮🇳 हिन्दी](README.hi.md)  ·  [🇮🇹 Italiano](README.it.md)  ·  [🇬🇪 ქართული](README.ka.md)**

---

## Présentation

La conjecture de Syracuse, également appelée **conjecture de Collatz** ou problème **3n+1**, est l’un des problèmes ouverts les plus célèbres des mathématiques.

Son énoncé est remarquablement simple : à partir d’un entier naturel strictement positif, on applique successivement deux opérations :

- Si le nombre est pair, on le divise par deux.
- Si le nombre est impair, on le multiplie par trois et on ajoute un.

La conjecture affirme que toute trajectoire ainsi obtenue finit par atteindre **1**, puis entre dans le cycle **1 → 4 → 2 → 1**.

Malgré la simplicité de ces règles, aucune démonstration générale de cette convergence n’est actuellement reconnue.

Ce dépôt rassemble une recherche consacrée à l’étude structurelle des trajectoires de Syracuse, à leur décomposition en transitions élémentaires et à la construction de modèles multidimensionnels capables de représenter leurs interactions.

## I. Une autre manière d’étudier Syracuse

L’approche développée dans ce projet ne consiste pas uniquement à calculer les trajectoires d’entiers successifs.

Elle cherche à comprendre les mécanismes qui gouvernent ces trajectoires.

Plutôt que de considérer chaque nombre comme un objet isolé, nous étudions les relations entre :

- Les chiffres qui composent un entier.
- Les transitions de parité.
- Les retenues et les dépendances positionnelles.
- Les structures dyadiques.
- Les phases de croissance et de décroissance.
- Les corridors de transitions.
- Les compositions temporelles.
- L’expansion combinatoire des structures lorsque la longueur des entiers augmente.

L’objectif est de passer d’une observation numérique à une **description mathématique exacte des mécanismes de transition**.

## II. Les matrices Φ et Ψ

Une partie centrale des recherches repose sur les structures désignées par **Φ (Phi)** et **Ψ (Psi)**.

Elles constituent des outils de classification et de représentation des transitions, des dépendances et de leurs compositions.

Le programme de recherche examine notamment :

**1. Les transitions élémentaires**

L’étude des transformations possibles pour chaque chiffre, état de parité et configuration de retenue.

**2. Les dépendances multidimensionnelles**

L’étude des interactions entre plusieurs positions décimales et plusieurs niveaux de transition.

**3. L’emboîtement des structures**

La manière dont les comportements observés pour des entiers de longueur $n$ interviennent dans les structures associées aux entiers de longueur $n+1$.

**4. L’expansion combinatoire**

La croissance du nombre de configurations et de chaînes possibles lorsque la longueur des entiers augmente.

**5. La superposition et la composition temporelle**

La combinaison de structures locales et de leurs évolutions au cours de plusieurs transitions.

Ces travaux visent à construire une représentation cohérente des trajectoires, depuis les opérations locales jusqu’aux comportements de longue durée.

## III. La dynamique de Syracuse

Pour tout entier $n\geq1$, la transformation classique est définie par :

$$
T(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
3n+1 & n\equiv1\pmod2.
\end{cases}
$$

Une version condensée permet de représenter la dynamique sous la forme :

$$
S(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
\dfrac{3n+1}{2} & n\equiv1\pmod2.
\end{cases}
$$

Cette seconde formulation permet d’étudier directement deux types de transitions :

- **Descente dyadique** : $n\mapsto n/2$.
- **Montée impaire condensée** : $n\mapsto(3n+1)/2$.

L’alternance de ces transformations constitue l’un des objets fondamentaux de notre étude.

## IV. Les chiffres et leurs interactions

Un entier de plusieurs chiffres ne se transforme pas comme une simple collection de chiffres indépendants.

La transformation d’une position peut dépendre des retenues et des états propagés depuis d’autres positions.

Nous étudions donc les transformations décimales comme des systèmes de dépendances locales composables.

Une retenue associée à une transformation affine peut notamment s’écrire :

$$
\kappa_\varepsilon(b)=\left\lfloor\frac{3b+\varepsilon}{10}\right\rfloor.
$$

où $b$ représente un chiffre décimal et $\varepsilon$ un état de retenue. Cette écriture s’applique à l’opération locale correspondante, avec la convention de retenue utilisée.

Cette représentation permet d’examiner la propagation de l’information entre les positions d’un entier. L’ambition est de caractériser les transformations d’entiers de longueur arbitraire à partir de lois locales exactes et de leurs compositions.

## V. La structure multidimensionnelle

Le projet explore quatre dimensions complémentaires :

**Structure locale** — Les règles exactes applicables à chaque chiffre et à chaque état.

**Structure spatiale** — Les interactions entre les positions d’un entier et leurs dépendances.

**Structure combinatoire** — L’ensemble des configurations admissibles, leurs expansions et leurs emboîtements.

**Structure temporelle** — Les transitions successives, leurs compositions et les trajectoires qu’elles engendrent.

Ces dimensions ne doivent pas être étudiées indépendamment : leurs interactions constituent précisément l’un des objets de la recherche.

*Comment une dynamique déterministe définie par deux opérations élémentaires engendre-t-elle une telle diversité de structures et de trajectoires ?*

## VI. Objectif mathématique

Le programme poursuit un objectif principal :

**Établir une caractérisation universelle des trajectoires de Syracuse à partir de leurs structures élémentaires et de leurs lois de composition.**

Pour atteindre cet objectif, il est nécessaire de distinguer :

1. La représentation exacte des transitions.
2. L’exhaustivité des configurations représentées.
3. La fidélité des compositions pour toute longueur et toute durée.
4. L’analyse des trajectoires infinies admissibles.
5. La démonstration, ou non, de leur convergence vers le cycle terminal.

Une description exacte de la dynamique ne constitue pas, à elle seule, une preuve de la conjecture. Le passage de la caractérisation des trajectoires à une démonstration universelle exige un argument supplémentaire excluant rigoureusement toute trajectoire positive non convergente.

### Travaux et résultats documentés (v15–v17)

Les documents du dépôt distinguent les identités exactes, les certificats à horizon fini et les problèmes ouverts. Quelques points de repère :

- **v15 — Compatibilité dyadique :** toute suite finie de profondeurs impaires strictement positives est réalisable par une classe résiduelle infinie.
- **v15 — Certificats de première descente :** critères arithmétiques exploitant les profondeurs et les bornes de tête ; les résultats de densité ne constituent pas une garantie individuelle.
- **v17 — Certificat double :** un plancher de fidélité et un plafond de non-descente permettent de certifier une première descente aux fins de corridors lorsqu’ils deviennent incompatibles.
- **v17 — Audit fini :** 199 287 motifs bornés pour $K=1$ à $5$ ; sept familles suivies sur 300 horizons chacune.
- **v17 — Mot critique supérieur :** construction non ultimement périodique, dont les préfixes finis sont multiplicativement expansifs ; la réalisation de toute la suite par un même entier positif n’est pas établie.

**Statut général :** ces résultats ne prouvent pas la convergence universelle, ni l’inexistence de cycles non terminaux, ni l’exclusion de toute divergence positive.

$$
D_Kq_K=A_Kq_0+C_K,
\qquad q_{0,\min}(K)\leq q_0\leq Q_K.
$$

## VII. Organisation du dépôt

```text
Syracuse/
├── README.md
├── README.en.md
├── README.de.md
├── README.es.md
├── README.he.md
├── README.ja.md
├── README.zh-CN.md
├── README.hi.md
├── README.it.md
├── README.ka.md
├── mecanique_syracuse.pdf
├── Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf
├── Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/
│   ├── LISEZMOI.md
│   ├── Code/
│   ├── Donnees/
│   ├── Figures/
│   ├── LaTeX/
│   ├── Laboratoire/
│   └── PDF/
└── testing/
    ├── Matrices et audits Φ/Ψ
    ├── Études des chaînes et des corridors
    ├── Scripts Python
    └── Archives expérimentales
```

### Manuscrit principal

[`mecanique_syracuse.pdf`](mecanique_syracuse.pdf) — Document consacré à l’étude mathématique et structurelle de la dynamique de Syracuse.

### Atlas Φ/Ψ v17

[`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md`](Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md) — Complément scientifique consacré aux excursions mixtes, aux certificats arithmétiques et aux configurations critiques.

### Dossier expérimental

[`testing/`](testing/) — Ce répertoire rassemble les programmes, matrices, résultats numériques, études intermédiaires et archives de recherche.

Les résultats expérimentaux doivent être distingués des propositions mathématiques formellement démontrées.

## VIII. Reproductibilité scientifique

La reproductibilité constitue un principe essentiel du projet. Les travaux doivent permettre, autant que possible :

- De retrouver les hypothèses et définitions utilisées.
- De reproduire les calculs à partir des scripts.
- De contrôler les matrices et les transitions générées.
- D’identifier les domaines effectivement vérifiés.
- De distinguer une vérification exhaustive bornée d’une démonstration universelle.
- De documenter les éventuels contre-exemples aux propositions intermédiaires.

Une recherche mathématique gagne en valeur lorsque ses résultats peuvent être examinés, reproduits, critiqués et améliorés indépendamment.

### Reproduction de l’étude v17

Le script Python de l’atlas utilise la bibliothèque standard et peut être exécuté depuis son répertoire `Code/` :

```bash
cd Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/Code
python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 5 --max-rt 3 --path-horizon 300
```

## IX. Contributions

Les contributions scientifiques et techniques sont les bienvenues. Vous pouvez :

- Examiner les définitions et démonstrations.
- Reproduire les expériences numériques.
- Signaler une erreur ou une hypothèse insuffisamment justifiée.
- Proposer de nouvelles classifications.
- Améliorer les algorithmes.
- Soumettre une Pull Request accompagnée d’une justification mathématique ou technique.

Toute proposition de modification doit pouvoir être examinée avant son intégration. **La publication d’une contribution ne vaut pas validation mathématique de son contenu.**

## X. Philosophie de recherche

La simplicité d’une règle ne garantit pas la simplicité des structures qu’elle engendre.

Syracuse en constitue une illustration particulièrement remarquable.

L’objectif de cette recherche est de comprendre comment les opérations élémentaires, les dépendances locales, les structures multidimensionnelles et les compositions temporelles interagissent pour produire la dynamique globale.

Il ne s’agit pas seulement de calculer davantage de trajectoires.

Il s’agit de comprendre ce qui rend ces trajectoires possibles.

---

## Auteur

**Andrew Caron**

GitHub : [PsiGuardian](https://github.com/PsiGuardian)

Syracuse : [PsiGuardian/Syracuse](https://github.com/PsiGuardian/Syracuse)

---

*« Comprendre une trajectoire, ce n’est pas seulement connaître sa destination. C’est comprendre les lois qui rendent chacun de ses mouvements possible. »*

**SYRACUSE — De la transition élémentaire à la structure universelle.**