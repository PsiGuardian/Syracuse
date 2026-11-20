# Syracuse — Inventaire des lemmes et des énoncés numérotés

Dépôt [PsiGuardian/Syracuse](https://github.com/PsiGuardian/Syracuse), branche `main`, [commit `6e123ae17ae6`](https://github.com/PsiGuardian/Syracuse/commit/6e123ae17ae6960ca66dda8f1f024d155c974a38). Le recensement couvre les 48 fichiers suivis à cette révision, y compris les publications et sources présentes dans les six archives ZIP.

Le registre contient **137 lemmes** selon leur identification éditoriale, avec **185 passages d’énoncé dans les PDF** et **20 emplacements LaTeX**. Le lemme sans numéro de la section 28.4 est inclus. Les lemmes ayant la même portée mathématique peuvent porter des intitulés distincts dans deux ouvrages. Leur équivalence reste à examiner.

L’index complémentaire porte le total à **401 entrées**. Les catégories suivent la manière dont les sources présentent les énoncés. Les théorèmes-programmes, hypothèses et conjectures conservent ce statut. Le travail porte sur le recensement des énoncés et de leurs emplacements.

| Catégorie | Entrées |
|---|---:|
| Lemme | 137 |
| Théorème | 59 |
| Proposition | 118 |
| Corollaire | 62 |
| Théorème-programme | 21 |
| Hypothèse | 2 |
| Conjecture | 2 |

## Comment retrouver un passage

- **PDF.** `M01 p. 39, l. 10` désigne la page 39 du fichier, comptée depuis la couverture, et la dixième ligne de sa transcription avec Poppler. Les lignes vides et les en-têtes sont comptés. La page imprimée peut avoir un autre numéro. Les lignes repèrent le début de l’énoncé ou le titre sur plusieurs lignes.
- **LaTeX ou Markdown.** Les numéros sont ceux du fichier source. Pour un environnement LaTeX, l’intervalle va de son ouverture à sa fermeture. Les liens des fichiers textes publiés directement pointent vers les lignes GitHub.
- **Fichiers en ZIP.** Le lien ouvre l’archive GitHub. La table des sources indique le nom exact du fichier à ouvrir à l’intérieur.

Pour reproduire un repère PDF, remplacer `39` et `document.pdf` dans cette commande. Avec le PDF M01, la ligne 10 de la sortie commence par « Lemme 3.9 ». Les repères ont été établis avec Poppler 25.03.0.

```bash
pdftotext -f 39 -l 39 -layout document.pdf - | tr -d '\014' | nl -ba
```

Repères imprimés de la monographie indiqués par `impr.`.

Les rééditions d’un même énoncé de Φ–Ψ sont regroupées selon leur numéro et leur intitulé. Les identifiants locaux de la monographie, du recueil Rouages et de Mécanique sont propres à chaque ouvrage. Les liens des copies strictement identiques figurent dans les sources. Les titres de couverture, tables des matières et mentions de renvoi sont écartés du comptage. Le passage de certification associé à 5.41 est signalé comme application.

## Sources et fichiers à ouvrir

| Code | Ouvrage ou édition | Fichier et emplacement |
|---|---|---|
| M01 | Monographie complète | [`syracuse_monographie_complete_ch53_audit_sorties_forcees_compensees.pdf`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/syracuse_monographie_complete_ch53_audit_sorties_forcees_compensees.pdf) |
| R01 | Recueil rouages et réarmement | [`syracuse_branche_rouages_rearmement_lemmes.pdf`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/syracuse_branche_rouages_rearmement_lemmes.pdf) |
| D01 | Mécanique de Syracuse | [`mecanique_syracuse.pdf`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/mecanique_syracuse.pdf)<br>[Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip) → `mecanique_syracuse.pdf` |
| P01 | Complément v6 et annexe v17 | [`Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf)<br>[`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/PDF/Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/PDF/Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf)<br>[Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas.zip) → `PDF/Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf` |
| P02 | Complément v10 | [Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip) → `Syracuse_PhiPsi_Complement_v10.pdf` |
| P03 | Manuscrit complet v10 | [Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip) → `Syracuse_PhiPsi_Manuscrit_Complet_v10.pdf` |
| P04 | Fascicule autonome du lemme 5.38 | [Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip) → `Syracuse_PhiPsi_Lemme_5_38.pdf` |
| P05 | Complément v14 | [Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip) → `Syracuse_PhiPsi_Complement_v14.pdf` |
| P06 | Manuscrit complet v14 | [Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip) → `Syracuse_PhiPsi_Manuscrit_Complet_v14.pdf` |
| P07 | Fascicule autonome 5.49–5.50 | [Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip) → `Syracuse_PhiPsi_Theoreme_5_49_50.pdf` |
| E01 | Deux réarmements | [Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip) → `Syracuse_PhiPsi_Deux_Rearmements_Etude.pdf` |
| V01 | Atlas des excursions mixtes v17 | [`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/PDF/Syracuse_PhiPsi_Excursions_Mixtes_v17.pdf`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/PDF/Syracuse_PhiPsi_Excursions_Mixtes_v17.pdf)<br>[Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas.zip) → `PDF/Syracuse_PhiPsi_Excursions_Mixtes_v17.pdf` |
| P08 | Source LaTeX du complément v10 | [Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip) → `Syracuse_PhiPsi_Theoremes_v10.tex` |
| P09 | Source LaTeX du lemme 5.38 | [Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip) → `Syracuse_PhiPsi_Lemme_5_38.tex` |
| P10 | Source LaTeX du complément v14 | [Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip) → `Syracuse_PhiPsi_Theoremes_v14.tex` |
| P11 | Source LaTeX du fascicule 5.49–5.50 | [Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip) → `Syracuse_PhiPsi_Theoreme_5_49_50.tex` |
| E02 | Source LaTeX de l’étude de deux réarmements | [Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip) → `Syracuse_PhiPsi_Deux_Rearmements_Etude.tex` |
| E03 | Version Markdown de l’étude de deux réarmements | [Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip) → `Syracuse_PhiPsi_Deux_Rearmements_Etude.md` |
| V02 | Source LaTeX de l’atlas v17 | [`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex)<br>[Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas.zip](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas.zip) → `LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex` |
| N01 | Note v15 de compatibilité et déficit | [`testing/Syracuse_PhiPsi_Etude_Compatibilite_Deficit_v15.md`](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Etude_Compatibilite_Deficit_v15.md) |

## Registre des lemmes

### Monographie complète, chapitres 1–53

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| L001 | Lemme 3.9 | Valeurs possibles de la poussée intermédiaire | [M01 p. 39 (impr. 22)][M01], l. 10 |
| L002 | Lemme 3.10 | Partitions exactes selon la retenue entrante | [M01 p. 39 (impr. 22)][M01], l. 30 |
| L003 | Lemme 3.11 | Réduction exacte des 300 états bruts aux 90 états enrichis | [M01 p. 40 (impr. 23)][M01], l. 23 |
| L004 | Lemme 4.11 | Réduction exacte des états bruts vers les états enrichis | [M01 p. 47 (impr. 30)][M01], l. 22 |
| L005 | Lemme 4.12 | Réduction exacte des états enrichis vers les types fondamentaux | [M01 p. 48 (impr. 31)][M01], l. 5 |
| L006 | Lemme 4.14 | Saturation locale complète dès trois chiffres | [M01 p. 48 (impr. 31)][M01], l. 24 |
| L007 | Lemme 5.5 | Fermeture de T30 sur E30 | [M01 p. 54 (impr. 37)][M01], l. 46 |
| L008 | Lemme 5.8 | Structure de permutation | [M01 p. 56 (impr. 39)][M01], l. 15 |
| L009 | Lemme 5.11 | Les deux points fixes | [M01 p. 57 (impr. 40)][M01], l. 9 |
| L010 | Lemme 6.2 | Point fixe bas | [M01 p. 60 (impr. 43)][M01], l. 30 |
| L011 | Lemme 6.3 | Point fixe haut | [M01 p. 60 (impr. 43)][M01], l. 38 |
| L012 | Lemme 7.6 | Longueur locale exacte | [M01 p. 65 (impr. 48)][M01], l. 17 |
| L013 | Lemme 8.8 | Comptage total des occurrences | [M01 p. 70 (impr. 53)][M01], l. 4 |
| L014 | Lemme 8.17 | Loi uniforme du squelette | [M01 p. 73 (impr. 56)][M01], l. 30 |
| L015 | Lemme 8.18 | Équilibre pondéré sur le cycle pur | [M01 p. 73 (impr. 56)][M01], l. 47 |
| L016 | Lemme 8.19 | Masse positive totale | [M01 p. 74 (impr. 57)][M01], l. 13 |
| L017 | Lemme 8.20 | Masse négative totale | [M01 p. 74 (impr. 57)][M01], l. 29 |
| L018 | Lemme 8.29 | Miroir combinatoire non pondéré | [M01 p. 77 (impr. 60)][M01], l. 29 |
| L019 | Lemme 8.31 | Équilibre pondéré sur le cycle pur | [M01 p. 78 (impr. 61)][M01], l. 4 |
| L020 | Lemme 9.5 | Version regroupée de la table | [M01 p. 86 (impr. 69)][M01], l. 16 |
| L021 | Lemme 9.9 | Identification exacte des classes dures | [M01 p. 89 (impr. 72)][M01], l. 29 |
| L022 | Lemme 10.3 | Temps exact d’un déplacement impair | [M01 p. 92 (impr. 75)][M01], l. 25 |
| L023 | Lemme 13.2 | Transitions spectrales pour j = 0 | [M01 p. 125 (impr. 108)][M01], l. 16 |
| L024 | Lemme 13.3 | Transitions spectrales pour j = 1 | [M01 p. 125 (impr. 108)][M01], l. 27 |
| L025 | Lemme 13.4 | Transitions spectrales pour j = 2 | [M01 p. 125 (impr. 108)][M01], l. 39 |
| L026 | Lemme 14.2 | Non-négativité et localité de χ | [M01 p. 130 (impr. 113)][M01], l. 22 |
| L027 | Lemme 15.9 | Lemme canonique de chaîne admissible | [M01 p. 141 (impr. 124)][M01], l. 12 |
| L028 | Lemme 17.3 | Finitude uniforme des fibres | [M01 p. 156 (impr. 139)][M01], l. 27 |
| L029 | Lemme 18.6 | Aucune transition dure majorante vers p5 | [M01 p. 166 (impr. 149)][M01], l. 34 |
| L030 | Lemme 18.7 | Le tournoi futur se rabat sur {p7, p9} | [M01 p. 166 (impr. 149)][M01], l. 46 |
| L031 | Lemme 19.2 | Réduction effective du tournoi dur | [M01 p. 171 (impr. 154)][M01], l. 28 |
| L032 | Lemme 21.5 | Version regroupée de la table | [M01 p. 185 (impr. 168)][M01], l. 36 |
| L033 | Lemme 22.5 | Identification exacte des classes dures | [M01 p. 189 (impr. 172)][M01], l. 29 |
| L034 | Lemme 25.14 | Tête et queue bornées | [M01 p. 206 (impr. 189)][M01], l. 31 |
| L035 | Lemme 36.10 | Non-création locale au-delà de la saturation | [M01 p. 282 (impr. 265)][M01], l. 43 |
| L036 | Lemme 37.13 | La tête n’est pas une mécanique nouvelle | [M01 p. 294 (impr. 277)][M01], l. 23 |
| L037 | Lemme 37.20 | Premier chiffre du quotient | [M01 p. 296 (impr. 279)][M01], l. 16 |
| L038 | Lemme 37.41 | Admissibilité par fibre non vide | [M01 p. 303 (impr. 286)][M01], l. 16 |
| L039 | Lemme 37.45 | Compatibilité avec les pas pairs | [M01 p. 304 (impr. 287)][M01], l. 19 |
| L040 | Lemme 37.48 | Finitude des sorties | [M01 p. 305 (impr. 288)][M01], l. 4 |
| L041 | Lemme 37.59 | Normalisation terminale | [M01 p. 309 (impr. 292)][M01], l. 4 |
| L042 | Lemme 38.9 | Compatibilité nécessaire | [M01 p. 313 (impr. 296)][M01], l. 54 |
| L043 | Lemme 38.11 | Séparation des régimes fixes et mobiles | [M01 p. 314 (impr. 297)][M01], l. 30 |
| L044 | Lemme 38.14 | Caractère exact des lignes orientées | [M01 p. 315 (impr. 298)][M01], l. 50 |
| L045 | Lemme 38.20 | Sûreté du majorant spectral profond | [M01 p. 317 (impr. 300)][M01], l. 45 |
| L046 | Lemme 38.24 | Décomposition enrichie de l’incrément | [M01 p. 318 (impr. 301)][M01], l. 56 |
| L047 | Lemme 38.31 | Sûreté du majorant coordonné enrichi | [M01 p. 320 (impr. 303)][M01], l. 64 |
| L048 | Lemme 39.7 | Majoration profonde | [M01 p. 327 (impr. 310)][M01], l. 44 |
| L049 | Lemme 40.2 | Fermeture des rouages | [M01 p. 330 (impr. 313)][M01], l. 33 |
| L050 | Lemme 40.6 | Ajout d’un chiffre et ajout d’un rouage | [M01 p. 332 (impr. 315)][M01], l. 36 |
| L051 | Lemme 40.13 | Compatibilité des deux lectures terminales | [M01 p. 333 (impr. 316)][M01], l. 40 |
| L052 | Lemme 41.2 | Premier rang de saturation positionnelle | [M01 p. 338 (impr. 321)][M01], l. 4 |
| L053 | Lemme 41.6 | Stabilité de la loi locale par prolongement | [M01 p. 339 (impr. 322)][M01], l. 29 |
| L054 | Lemme 42.4 | Finitude de la tension locale | [M01 p. 345 (impr. 328)][M01], l. 26 |
| L055 | Lemme 42.13 | Perte d’une rencontre élémentaire | [M01 p. 347 (impr. 330)][M01], l. 18 |
| L056 | Lemme 42.16 | Perte locale sous condition de marge | [M01 p. 347 (impr. 330)][M01], l. 49 |
| L057 | Lemme 43.2 | Finitude de l’alphabet local | [M01 p. 353 (impr. 336)][M01], l. 14 |
| L058 | Lemme 43.8 | Bien-fondation | [M01 p. 354 (impr. 337)][M01], l. 23 |
| L059 | Lemme 44.8 | La neutralité digitique n’est pas une neutralité d’état | [M01 p. 361 (impr. 344)][M01], l. 43 |
| L060 | Lemme 44.14 | Finitude du graphe projeté | [M01 p. 363 (impr. 346)][M01], l. 14 |
| L061 | Lemme 44.21 | Chemin infini dans un graphe fini | [M01 p. 364 (impr. 347)][M01], l. 29 |
| L062 | Lemme 45.5 | Contrôle de cardinalité | [M01 p. 369 (impr. 352)][M01], l. 18 |
| L063 | Lemme 46.7 | Séparation des bords atomiques | [M01 p. 379 (impr. 362)][M01], l. 11 |
| L064 | Lemme 47.8 | Inclusion exhaustive | [M01 p. 385 (impr. 368)][M01], l. 45 |
| L065 | Lemme 48.5 | Fermeture brute | [M01 p. 391 (impr. 374)][M01], l. 25 |
| L066 | Lemme 49.3 | Complétude brute | [M01 p. 397 (impr. 380)][M01], l. 47 |
| L067 | Lemme 49.6 | Déterminisme local | [M01 p. 399 (impr. 382)][M01], l. 20 |
| L068 | Lemme 50.2 | Obstruction minimale | [M01 p. 403 (impr. 386)][M01], l. 16 |
| L069 | Lemme 50.7 | Dissymétrie de bord | [M01 p. 404 (impr. 387)][M01], l. 53 |
| L070 | Lemme 50.11 | Propagation vers la tête macro | [M01 p. 406 (impr. 389)][M01], l. 8 |
| L071 | Lemme 51.5 | Neutralité locale et obstruction globale | [M01 p. 411 (impr. 394)][M01], l. 20 |
| L072 | Lemme 52.4 | Obstruction au prolongement neutre de 51 | [M01 p. 417 (impr. 400)][M01], l. 15 |

### Rouages et réarmement

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| L073 | Lemme 1.2 | Decomposition locale de la montee impaire | [R01 p. 2][R01], l. 4 |
| L074 | Lemme 1.3 | Bornitude absolue de la retenue | [R01 p. 2][R01], l. 16 |
| L075 | Lemme 1.4 | Propagation lineaire sans retour interne | [R01 p. 2][R01], l. 30 |
| L076 | Lemme 1.5 | Saturation positionnelle a partir de zba | [R01 p. 2][R01], l. 37 |
| L077 | Lemme 2.1 | Cycle pur modulo 10 de la multiplication par 3 | [R01 p. 2][R01], l. 48 |
| L078 | Lemme 2.2 | Le cycle pur oublie la retenue | [R01 p. 3][R01], l. 1 |
| L079 | Lemme 2.3 | Brisure terminale par l’injection +1 | [R01 p. 3][R01], l. 5 |
| L080 | Lemme 2.4 | Incompatibilite du cycle pur avec Syracuse | [R01 p. 3][R01], l. 9 |
| L081 | Lemme 2.5 | Table des portes impaires avec retenue | [R01 p. 3][R01], l. 15 |
| L082 | Lemme 2.6 | La colonne ε = 1 est le briseur principal | [R01 p. 3][R01], l. 25 |
| L083 | Lemme 2.7 | Retenue forte et cycle projete | [R01 p. 3][R01], l. 28 |
| L084 | Lemme 2.8 | Rouage local maximal | [R01 p. 3][R01], l. 34 |
| L085 | Lemme 2.9 | Bande de maintien fort | [R01 p. 3][R01], l. 38 |
| L086 | Lemme 3.1 | La tete ferme l’onde de retenue | [R01 p. 4][R01], l. 2 |
| L087 | Lemme 3.2 | Fermeture d’une retenue forte en tete | [R01 p. 4][R01], l. 7 |
| L088 | Lemme 3.3 | Croissance decimale maximale d’une montee | [R01 p. 4][R01], l. 15 |
| L089 | Lemme 3.4 | Survie du nouveau rang | [R01 p. 4][R01], l. 20 |
| L090 | Lemme 3.5 | Critere modulo 4 de survie | [R01 p. 4][R01], l. 30 |
| L091 | Lemme 3.6 | Le pied seul ne determine pas le modulo 4 | [R01 p. 4][R01], l. 37 |
| L092 | Lemme 3.7 | Gain survivant implique tete 1 | [R01 p. 4][R01], l. 43 |
| L093 | Lemme 3.8 | Tete 1 anti-croissance immediate | [R01 p. 5][R01], l. 1 |
| L094 | Lemme 3.10 | Rearmement differe | [R01 p. 5][R01], l. 12 |
| L095 | Lemme 4.1 | Rearmement minimal des tetes faibles | [R01 p. 5][R01], l. 21 |
| L096 | Lemme 4.2 | Valuations minimales du rearmement | [R01 p. 5][R01], l. 29 |
| L097 | Lemme 4.3 | Neutralite en rang du rearmement | [R01 p. 5][R01], l. 37 |
| L098 | Lemme 4.4 | Motif productif compact | [R01 p. 5][R01], l. 44 |
| L099 | Lemme 4.5 | Condition de depart du motif compact | [R01 p. 6][R01], l. 1 |
| L100 | Lemme 4.6 | Non-repetition immediate du motif compact | [R01 p. 6][R01], l. 21 |
| L101 | Lemme 5.2 | Condition multiplicative d’une phase froide | [R01 p. 6][R01], l. 43 |
| L102 | Lemme 5.3 | Premiere phase froide multiplicative | [R01 p. 6][R01], l. 56 |
| L103 | Lemme 5.4 | Structure interne du couple (41, 64) | [R01 p. 7][R01], l. 5 |
| L104 | Lemme 5.5 | Existence d’un mot froid interne admissible | [R01 p. 7][R01], l. 13 |
| L105 | Lemme 6.2 | Facteur normalise d’un cycle compose | [R01 p. 7][R01], l. 35 |
| L106 | Lemme 6.3 | Absence de neutralite exacte | [R01 p. 7][R01], l. 44 |
| L107 | Lemme 6.7 | Arretes montantes et descendantes | [R01 p. 8][R01], l. 6 |
| L108 | Lemme 6.8 | Premiere boucle de derive candidate | [R01 p. 8][R01], l. 12 |
| L109 | Lemme 6.9 | Non-fermeture de la premiere boucle de derive | [R01 p. 8][R01], l. 25 |
| L110 | Lemme 6.10 | Absence de neutralite exacte des boucles mixtes | [R01 p. 8][R01], l. 34 |
| L111 | Lemme 6.11 | Existence de quasi-boucles mixtes | [R01 p. 8][R01], l. 40 |
| L112 | Lemme 6.12 | Corridor multiplicatif confine | [R01 p. 8][R01], l. 46 |
| L113 | Lemme 7.1 | Forme affine exacte d’un mot de valuations | [R01 p. 9][R01], l. 2 |
| L114 | Lemme 7.2 | Positivite et decroissance du terme affine normalise | [R01 p. 9][R01], l. 17 |
| L115 | Lemme 7.3 | Les boucles montantes sont amplifiees par le terme affine | [R01 p. 9][R01], l. 27 |
| L116 | Lemme 7.4 | Sensibilite finie des quasi-boucles descendantes | [R01 p. 9][R01], l. 35 |
| L117 | Lemme 7.5 | Cylindre congruentiel d’un mot de valuations | [R01 p. 9][R01], l. 46 |
| L118 | Lemme 7.6 | Condition post-gain compacte | [R01 p. 9][R01], l. 58 |
| L119 | Lemme 7.7 | Pression dyadique des cycles composes | [R01 p. 10][R01], l. 6 |

### Mécanique de Syracuse

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| L120 | Lemme 2.6 | Effet de la retenue sur une parité | [D01 p. 6][D01], l. 1 · [P03 p. 6][P03], l. 1 · [P06 p. 6][P06], l. 1 |
| L121 | Lemme 5.2 | Division locale d’un pied pair | [D01 p. 12][D01], l. 24 · [P03 p. 12][P03], l. 24 · [P06 p. 12][P06], l. 24 |
| L122 | Lemme 5.5 | Portée propagative d’une descente dyadique | [D01 p. 13][D01], l. 25 · [P03 p. 13][P03], l. 25 · [P06 p. 13][P06], l. 25 |
| L123 | Lemme 6.1 | Équilibre du pied | [D01 p. 14][D01], l. 2 · [P03 p. 14][P03], l. 2 · [P06 p. 14][P06], l. 2 |
| L124 | Lemme 6.2 | Équilibre du corps sous l’indice Π | [D01 p. 14][D01], l. 21 · [P03 p. 14][P03], l. 21 · [P06 p. 14][P06], l. 21 |
| L125 | Lemme 7.5 | Domination élémentaire de la descente | [D01 p. 17][D01], l. 29 · [P03 p. 17][P03], l. 29 · [P06 p. 17][P06], l. 29 |
| L126 | Lemme 8.3 | Absence de deux portes impaires consécutives | [D01 p. 18][D01], l. 30 · [P03 p. 18][P03], l. 30 · [P06 p. 18][P06], l. 30 |

### Compléments Φ–Ψ v6, v10 et v14

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| L127 | Lemme 5.6 | Cône d’influence dyadique | [P01 p. 3][P01], l. 14 · [P02 p. 3][P02], l. 25 · [P03 p. 25][P03], l. 25 · [P05 p. 3][P05], l. 25 · [P06 p. 25][P06], l. 25 · [P08][P08], l. 166–172 · [P10][P10], l. 178–184 |
| L128 | Lemme 5.9 | Invariance mécanique et retard exact de la tête | [P01 p. 6][P01], l. 15 · [P02 p. 6][P02], l. 15 · [P03 p. 28][P03], l. 15 · [P05 p. 6][P05], l. 15 · [P06 p. 28][P06], l. 15 · [P08][P08], l. 326–332 · [P10][P10], l. 338–344 |
| L129 | Lemme 5.23 | Localité stricte et horizon de la tête | [P01 p. 18][P01], l. 7 · [P02 p. 18][P02], l. 7 · [P03 p. 40][P03], l. 7 · [P05 p. 18][P05], l. 7 · [P06 p. 40][P06], l. 7 · [P08][P08], l. 898–904 · [P10][P10], l. 910–916 |
| L130 | Lemme 5.24 | Invariance temporelle et propagation différée du cône | [P01 p. 18][P01], l. 22 · [P02 p. 18][P02], l. 22 · [P03 p. 40][P03], l. 22 · [P05 p. 18][P05], l. 22 · [P06 p. 40][P06], l. 22 · [P08][P08], l. 909–915 · [P10][P10], l. 921–927 |
| L131 | Lemme 5.30 | Clôture locale du triplet décimal à une transition | [P01 p. 22][P01], l. 11 · [P02 p. 22][P02], l. 11 · [P03 p. 44][P03], l. 11 · [P05 p. 22][P05], l. 11 · [P06 p. 44][P06], l. 11 · [P08][P08], l. 1084–1090 · [P10][P10], l. 1096–1102 |
| L132 | Lemme 5.31 | Autosuffisance de l’état et antécédents dyadiques | [P01 p. 23][P01], l. 18 · [P02 p. 23][P02], l. 18 · [P03 p. 45][P03], l. 18 · [P05 p. 23][P05], l. 18 · [P06 p. 45][P06], l. 18 · [P08][P08], l. 1142–1152 · [P10][P10], l. 1154–1164 |
| L133 | Lemme 5.37 | Emboîtement universel des cônes décimaux et invariance mécanique | [P02 p. 31][P02], l. 7 · [P03 p. 53][P03], l. 7 · [P05 p. 31][P05], l. 7 · [P06 p. 53][P06], l. 7 · [P08][P08], l. 1421–1457 · [P10][P10], l. 1433–1469 |
| L134 | Lemme 5.38 | Superposition exacte des triplets décimaux chevauchants | [P02 p. 39][P02], l. 28 · [P03 p. 61][P03], l. 28 · [P04 p. 1][P04], l. 38 · [P05 p. 39][P05], l. 28 · [P06 p. 61][P06], l. 28 · [P08][P08], l. 1737–1750 · [P09][P09], l. 95–108 · [P10][P10], l. 1749–1762 |
| L135 | Lemme 5.41 | Fidélité et prolongements des suffixes | [P05 p. 49][P05], l. 34 · [P06 p. 71][P06], l. 34 · [P10][P10], l. 2160–2179 · [E03][E03], l. 60 (application) |
| L136 | Lemme 5.48 | Non-composabilité des arcs temporels locaux | [P05 p. 56][P05], l. 51 · [P06 p. 78][P06], l. 51 · [P10][P10], l. 2426–2437 |
| L137 | Lemme § 28.4 | Fermeture à horizon fini | [P05 p. 57][P05], l. 60 (titre l. 58) · [P06 p. 79][P06], l. 60 (titre l. 58) · [P10][P10], l. 2493–2506 (titre l. 2492) |

## Index complémentaire des énoncés

Les propositions, corollaires et théorèmes figurent ici avec les énoncés dont la source indique un statut d’hypothèse, de conjecture ou de programme.

Dans la monographie, le « Lemme de non-neutralité persistante du carry » est intitulé **Théorème-programme 50.10**. Son énoncé décrit une fermeture à établir et figure donc dans cet index.

### Monographie complète, chapitres 1–53

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| E001 | Corollaire 3.12 | Préparation à la réduction ultérieure | [M01 p. 41 (impr. 24)][M01], l. 21 |
| E002 | Proposition 4.6 | Table exacte des types fondamentaux | [M01 p. 45 (impr. 28)][M01], l. 35 |
| E003 | Théorème 4.15 | Absence de loi locale nouvelle au-delà de trois chiffres | [M01 p. 49 (impr. 32)][M01], l. 12 |
| E004 | Corollaire 4.16 | Stabilité d’échelle de la mécanique locale | [M01 p. 49 (impr. 32)][M01], l. 34 |
| E005 | Proposition 5.4 | Table exacte des 30 transitions | [M01 p. 53 (impr. 36)][M01], l. 43 |
| E006 | Corollaire 5.6 | Déterminisme | [M01 p. 55 (impr. 38)][M01], l. 11 |
| E007 | Proposition 5.9 | Spectre de A30 | [M01 p. 56 (impr. 39)][M01], l. 27 |
| E008 | Corollaire 5.10 | Rayon spectral | [M01 p. 56 (impr. 39)][M01], l. 38 |
| E009 | Proposition 5.12 | Existence du cycle principal exact | [M01 p. 57 (impr. 40)][M01], l. 23 |
| E010 | Corollaire 5.13 | Classification complète des cycles | [M01 p. 57 (impr. 40)][M01], l. 35 |
| E011 | Théorème 5.14 | Théorème de fermeture locale complète | [M01 p. 57 (impr. 40)][M01], l. 46 |
| E012 | Proposition 6.5 | Décomposition dynamique de l’espace local | [M01 p. 61 (impr. 44)][M01], l. 22 |
| E013 | Proposition 7.5 | Passage du local complet à la fenêtre mobile | [M01 p. 64 (impr. 47)][M01], l. 43 |
| E014 | Corollaire 7.7 | Croissance purement linéaire de la longueur | [M01 p. 65 (impr. 48)][M01], l. 33 |
| E015 | Corollaire 7.8 | Fenêtres de longueur r − 1 sur le cycle principal | [M01 p. 66 (impr. 49)][M01], l. 13 |
| E016 | Théorème 7.9 | Théorème de squelette mobile des mots exacts | [M01 p. 66 (impr. 49)][M01], l. 25 |
| E017 | Proposition 8.9 | Loi exacte des occurrences par fenêtre | [M01 p. 70 (impr. 53)][M01], l. 29 |
| E018 | Corollaire 8.10 | Croissance linéaire uniforme par arête | [M01 p. 70 (impr. 53)][M01], l. 48 |
| E019 | Proposition 8.13 | Lois uniformes non pondérées sur le squelette | [M01 p. 71 (impr. 54)][M01], l. 46 |
| E020 | Corollaire 8.14 | Moyenne exacte sur les phases | [M01 p. 72 (impr. 55)][M01], l. 12 |
| E021 | Proposition 8.16 | Loi uniforme pondérée générale | [M01 p. 72 (impr. 55)][M01], l. 52 |
| E022 | Théorème 8.24 | Loi induite positive non pondérée | [M01 p. 75 (impr. 58)][M01], l. 34 |
| E023 | Corollaire 8.25 | Rareté moyenne des sauts positifs | [M01 p. 75 (impr. 58)][M01], l. 50 |
| E024 | Théorème 8.26 | Loi induite positive pondérée | [M01 p. 76 (impr. 59)][M01], l. 17 |
| E025 | Théorème-programme 8.30 | Loi induite négative non pondérée | [M01 p. 77 (impr. 60)][M01], l. 35 |
| E026 | Théorème-programme 8.32 | Loi induite négative pondérée | [M01 p. 78 (impr. 61)][M01], l. 18 |
| E027 | Théorème-programme 8.33 | Domination dissipative pondérée | [M01 p. 78 (impr. 61)][M01], l. 32 |
| E028 | Corollaire 8.35 | Sous-langage mince | [M01 p. 79 (impr. 62)][M01], l. 36 |
| E029 | Théorème-programme 8.36 | Principe de dissipation structurelle | [M01 p. 80 (impr. 63)][M01], l. 7 |
| E030 | Proposition 9.3 | Séparation immédiate des portes | [M01 p. 85 (impr. 68)][M01], l. 7 |
| E031 | Proposition 9.7 | Toutes les portes impaires rencontrent toutes les classes impaires modulo 16 | [M01 p. 88 (impr. 71)][M01], l. 12–13 |
| E032 | Théorème 9.11 | Régimes exacts modulo 16 pour la profondeur dyadique locale | [M01 p. 90 (impr. 73)][M01], l. 19 |
| E033 | Corollaire 9.12 | Hiérarchie des profondeurs locales | [M01 p. 91 (impr. 74)][M01], l. 4 |
| E034 | Théorème 10.4 | Identité exacte du temps total | [M01 p. 92 (impr. 75)][M01], l. 36 |
| E035 | Théorème 10.8 | Décomposition exacte du temps total | [M01 p. 94 (impr. 77)][M01], l. 15 |
| E036 | Corollaire 10.9 | Lecture additive du temps | [M01 p. 94 (impr. 77)][M01], l. 32 |
| E037 | Proposition 11.3 | Primauté de la tête pour le raccord local–macro | [M01 p. 96 (impr. 79)][M01], l. 26 |
| E038 | Proposition 11.7 | Liste minimale des paramètres | [M01 p. 98 (impr. 81)][M01], l. 13 |
| E039 | Théorème 11.9 | Finitude de l’alphabet des têtes | [M01 p. 99 (impr. 82)][M01], l. 9 |
| E040 | Corollaire 11.10 | Réduction du raccord à un problème fini | [M01 p. 99 (impr. 82)][M01], l. 24 |
| E041 | Proposition 11.12 | Finitude de la table de raccord | [M01 p. 101 (impr. 84)][M01], l. 38 |
| E042 | Proposition 11.15 | Passage fini vers la famille macro de sortie | [M01 p. 102 (impr. 85)][M01], l. 45 |
| E043 | Proposition 11.18 | Finitude des incréments énergétiques de raccord | [M01 p. 104 (impr. 87)][M01], l. 7 |
| E044 | Corollaire 11.19 | Lecture énergétique pilotée par la tête | [M01 p. 104 (impr. 87)][M01], l. 21 |
| E045 | Théorème 11.20 | Fermeture du raccord local–macro | [M01 p. 104 (impr. 87)][M01], l. 40 |
| E046 | Corollaire 11.21 | Déplacement du problème global | [M01 p. 105 (impr. 88)][M01], l. 19 |
| E047 | Proposition 12.8 | Bien-définition du passage macro de tête | [M01 p. 108 (impr. 91)][M01], l. 37 |
| E048 | Proposition 12.9 | Rôle structural de la profondeur dyadique | [M01 p. 109 (impr. 92)][M01], l. 13 |
| E049 | Corollaire 12.11 | Régimes macroscopiques de tête | [M01 p. 109 (impr. 92)][M01], l. 32 |
| E050 | Proposition 12.14 | Finitude de la table macro | [M01 p. 110 (impr. 93)][M01], l. 24 |
| E051 | Théorème 12.16 | Interface macro finie de la tête | [M01 p. 111 (impr. 94)][M01], l. 10 |
| E052 | Proposition 12.19 | Finitude de la donnée de lecture | [M01 p. 113 (impr. 96)][M01], l. 17 |
| E053 | Proposition 12.21 | Bien-définition de la famille de tête | [M01 p. 114 (impr. 97)][M01], l. 15 |
| E054 | Théorème 12.22 | Hiérarchie dissipative héritée par la tête | [M01 p. 114 (impr. 97)][M01], l. 22 |
| E055 | Proposition 12.24 | Compatibilité avec la table spectrale locale | [M01 p. 115 (impr. 98)][M01], l. 31 |
| E056 | Proposition 12.27 | Borne canonique sur le saut familial de tête | [M01 p. 116 (impr. 99)][M01], l. 33 |
| E057 | Théorème 12.28 | Lecture énergétique finie de la tête | [M01 p. 116 (impr. 99)][M01], l. 53 |
| E058 | Corollaire 15.10 | Version canonique minimale | [M01 p. 141 (impr. 124)][M01], l. 44 |
| E059 | Proposition 16.4 | Existence du successeur majorant | [M01 p. 146 (impr. 129)][M01], l. 11 |
| E060 | Proposition 16.8 | Borne uniforme sur la variation de tension | [M01 p. 148 (impr. 131)][M01], l. 28 |
| E061 | Théorème 16.10 | Condition uniforme simple sur la table close | [M01 p. 149 (impr. 132)][M01], l. 46 |
| E062 | Corollaire 16.11 | Forme numérique | [M01 p. 150 (impr. 133)][M01], l. 29 |
| E063 | Proposition 17.6 | Compatibilité dynamique du relèvement | [M01 p. 157 (impr. 140)][M01], l. 44 |
| E064 | Corollaire 17.7 | Cardinal du relèvement | [M01 p. 158 (impr. 141)][M01], l. 25 |
| E065 | Proposition 17.10 | Finitude et taille du relèvement dur | [M01 p. 159 (impr. 142)][M01], l. 31 |
| E066 | Théorème-programme 18.8 | Prolifération dure majorante | [M01 p. 167 (impr. 150)][M01], l. 36 |
| E067 | Proposition 19.3 | Symétrie effective | [M01 p. 172 (impr. 155)][M01], l. 9 |
| E068 | Théorème 19.4 | Invariance spectrale sous réduction effective | [M01 p. 173 (impr. 156)][M01], l. 9 |
| E069 | Proposition 20.8 | Portée structurale de la mémoire enrichie | [M01 p. 179 (impr. 162)][M01], l. 48 |
| E070 | Théorème-programme 20.9 | Programme mémoire-enrichi | [M01 p. 180 (impr. 163)][M01], l. 31 |
| E071 | Proposition 21.3 | Séparation immédiate des portes | [M01 p. 184 (impr. 167)][M01], l. 45 |
| E072 | Proposition 22.3 | Toutes les portes impaires rencontrent toutes les classes impaires modulo 16 | [M01 p. 188 (impr. 171)][M01], l. 12–13 |
| E073 | Théorème 22.7 | Régimes exacts modulo 16 pour la profondeur dyadique locale | [M01 p. 190 (impr. 173)][M01], l. 19 |
| E074 | Corollaire 22.8 | Hiérarchie des profondeurs locales | [M01 p. 191 (impr. 174)][M01], l. 4 |
| E075 | Théorème 23.4 | Décomposition exacte du temps total | [M01 p. 193 (impr. 176)][M01], l. 9 |
| E076 | Corollaire 23.5 | Lecture additive du temps | [M01 p. 193 (impr. 176)][M01], l. 26 |
| E077 | Proposition 24.6 | Loi exacte de montée de rang | [M01 p. 197 (impr. 180)][M01], l. 25 |
| E078 | Corollaire 24.7 | Affinité d’échelle | [M01 p. 197 (impr. 180)][M01], l. 45 |
| E079 | Proposition 24.13 | Principe de cassure par couture | [M01 p. 199 (impr. 182)][M01], l. 10 |
| E080 | Proposition 25.5 | Orientation de propagation | [M01 p. 203 (impr. 186)][M01], l. 37 |
| E081 | Proposition 25.10 | Rôle de la projection | [M01 p. 205 (impr. 188)][M01], l. 35 |
| E082 | Proposition 25.13 | Rôle structurel de Φ | [M01 p. 206 (impr. 189)][M01], l. 18 |
| E083 | Corollaire 25.15 | Finitude de l’alphabet serpent | [M01 p. 207 (impr. 190)][M01], l. 10 |
| E084 | Proposition 26.2 | Primauté de la tête pour le raccord local–macro | [M01 p. 210 (impr. 193)][M01], l. 37 |
| E085 | Proposition 26.6 | Liste minimale des paramètres | [M01 p. 212 (impr. 195)][M01], l. 32 |
| E086 | Théorème 26.8 | Finitude de l’alphabet des têtes | [M01 p. 213 (impr. 196)][M01], l. 27 |
| E087 | Corollaire 26.9 | Réduction du raccord à un problème fini | [M01 p. 213 (impr. 196)][M01], l. 42 |
| E088 | Proposition 27.4 | Exhaustion par longueur et famille | [M01 p. 216 (impr. 199)][M01], l. 27 |
| E089 | Proposition 27.7 | Finitude des fibres brutes | [M01 p. 217 (impr. 200)][M01], l. 19 |
| E090 | Corollaire 27.8 | Table brute finie | [M01 p. 217 (impr. 200)][M01], l. 32 |
| E091 | Proposition 27.11 | Stratification des têtes par carry | [M01 p. 218 (impr. 201)][M01], l. 24 |
| E092 | Proposition 27.13 | Quatre régimes bruts de tête | [M01 p. 219 (impr. 202)][M01], l. 8 |
| E093 | Théorème 27.15 | Existence d’une classification exhaustive des têtes brutes | [M01 p. 219 (impr. 202)][M01], l. 33 |
| E094 | Proposition 28.5 | Bien-définition du passage macro de tête | [M01 p. 223 (impr. 206)][M01], l. 4 |
| E095 | Proposition 28.6 | Rôle structural de la profondeur dyadique | [M01 p. 223 (impr. 206)][M01], l. 27 |
| E096 | Corollaire 28.8 | Régimes macroscopiques de tête | [M01 p. 223 (impr. 206)][M01], l. 46 |
| E097 | Proposition 28.11 | Finitude de la table macro | [M01 p. 224 (impr. 207)][M01], l. 37 |
| E098 | Théorème 28.13 | Interface macro finie de la tête | [M01 p. 225 (impr. 208)][M01], l. 23 |
| E099 | Proposition 29.4 | Finitude de la donnée de lecture | [M01 p. 228 (impr. 211)][M01], l. 33 |
| E100 | Proposition 29.6 | Bien-définition de la famille de tête | [M01 p. 229 (impr. 212)][M01], l. 31 |
| E101 | Théorème 29.7 | Hiérarchie dissipative héritée par la tête | [M01 p. 229 (impr. 212)][M01], l. 38 |
| E102 | Proposition 29.9 | Compatibilité avec la table spectrale locale | [M01 p. 230 (impr. 213)][M01], l. 46 |
| E103 | Proposition 29.12 | Borne canonique sur le saut familial de tête | [M01 p. 231 (impr. 214)][M01], l. 51 |
| E104 | Théorème 29.13 | Lecture énergétique finie de la tête | [M01 p. 232 (impr. 215)][M01], l. 19 |
| E105 | Proposition 30.3 | Finitude de la table de raccord | [M01 p. 235 (impr. 218)][M01], l. 42 |
| E106 | Proposition 30.6 | Passage fini vers la famille macro de sortie | [M01 p. 236 (impr. 219)][M01], l. 48 |
| E107 | Proposition 30.9 | Finitude des incréments énergétiques de raccord | [M01 p. 238 (impr. 221)][M01], l. 10 |
| E108 | Corollaire 30.10 | Lecture énergétique pilotée par la tête | [M01 p. 238 (impr. 221)][M01], l. 24 |
| E109 | Théorème 30.11 | Fermeture du raccord local–macro | [M01 p. 238 (impr. 221)][M01], l. 42 |
| E110 | Corollaire 30.12 | Déplacement du problème global | [M01 p. 239 (impr. 222)][M01], l. 21 |
| E111 | Théorème 31.2 | Théorème-cadre unifié | [M01 p. 242 (impr. 225)][M01], l. 9 |
| E112 | Théorème-programme 31.5 | Principe de réduction finale | [M01 p. 245 (impr. 228)][M01], l. 28 |
| E113 | Proposition 32.2 | Triptyque de fermeture | [M01 p. 247 (impr. 230)][M01], l. 18 |
| E114 | Théorème 32.4 | Condition locale suffisante | [M01 p. 248 (impr. 231)][M01], l. 11 |
| E115 | Théorème 32.7 | Condition suffisante de classe | [M01 p. 249 (impr. 232)][M01], l. 31 |
| E116 | Théorème-programme 32.10 | Théorème-cible de fermeture mixte | [M01 p. 251 (impr. 234)][M01], l. 18 |
| E117 | Théorème 32.12 | Insertion des trois voies dans le théorème-cadre | [M01 p. 252 (impr. 235)][M01], l. 36 |
| E118 | Proposition 33.2 | Principe minimal de fermeture | [M01 p. 255 (impr. 238)][M01], l. 18 |
| E119 | Théorème 33.4 | Condition minimale de couverture locale | [M01 p. 256 (impr. 239)][M01], l. 13 |
| E120 | Théorème 33.5 | Condition minimale sur les chaînes admissibles | [M01 p. 257 (impr. 240)][M01], l. 8 |
| E121 | Théorème 33.6 | Condition minimale sur le régime dur | [M01 p. 258 (impr. 241)][M01], l. 9 |
| E122 | Théorème 33.7 | Condition minimale de raccord | [M01 p. 259 (impr. 242)][M01], l. 10 |
| E123 | Théorème 33.8 | Forme minimale de la réinjection universelle | [M01 p. 260 (impr. 243)][M01], l. 8 |
| E124 | Théorème 33.9 | Conditions minimales d’une fermeture complète | [M01 p. 260 (impr. 243)][M01], l. 39 |
| E125 | Théorème 36.8 | Suffisance d’une énergie uniformément décroissante | [M01 p. 281 (impr. 264)][M01], l. 31 |
| E126 | Corollaire 36.9 | Forme finie de la dernière vérification | [M01 p. 282 (impr. 265)][M01], l. 15 |
| E127 | Proposition 36.12 | Forme nécessaire d’une énergie mixte | [M01 p. 283 (impr. 266)][M01], l. 42 |
| E128 | Proposition 36.15 | Réduction à une marge finie | [M01 p. 285 (impr. 268)][M01], l. 46 |
| E129 | Corollaire 36.16 | Exclusion des cycles par énergie stricte | [M01 p. 286 (impr. 269)][M01], l. 25 |
| E130 | Corollaire 36.17 | Exclusion des errances infinies par bien-fondation | [M01 p. 287 (impr. 270)][M01], l. 4 |
| E131 | Théorème-programme 36.18 | Énoncé cible de fermeture | [M01 p. 288 (impr. 271)][M01], l. 18 |
| E132 | Proposition 37.7 | Décomposition de l’espace local | [M01 p. 292 (impr. 275)][M01], l. 17 |
| E133 | Proposition 37.9 | Activation positionnelle de la matrice locale | [M01 p. 292 (impr. 275)][M01], l. 57 |
| E134 | Proposition 37.16 | Table finie de la tête brute | [M01 p. 295 (impr. 278)][M01], l. 26 |
| E135 | Proposition 37.22 | Table exacte de tête macro | [M01 p. 296 (impr. 279)][M01], l. 42 |
| E136 | Proposition 37.24 | Structure par blocs | [M01 p. 297 (impr. 280)][M01], l. 25 |
| E137 | Corollaire 37.25 | Répartition familiale sur une tranche | [M01 p. 297 (impr. 280)][M01], l. 39 |
| E138 | Proposition 37.28 | Finitude de l’ombre de tête | [M01 p. 298 (impr. 281)][M01], l. 46 |
| E139 | Proposition 37.37 | Finitude de la projection | [M01 p. 301 (impr. 284)][M01], l. 20 |
| E140 | Proposition 37.42 | Caractère effectif de l’admissibilité | [M01 p. 303 (impr. 286)][M01], l. 29 |
| E141 | Proposition 37.51 | Critère tabulaire de fermeture | [M01 p. 306 (impr. 289)][M01], l. 13 |
| E142 | Proposition 37.53 | Incrément exact lorsque la tranche est lue | [M01 p. 306 (impr. 289)][M01], l. 52 |
| E143 | Corollaire 37.54 | Borne uniforme du cas profond | [M01 p. 307 (impr. 290)][M01], l. 11 |
| E144 | Théorème-programme 37.56 | Raffinement fini | [M01 p. 308 (impr. 291)][M01], l. 7 |
| E145 | Théorème-programme 37.60 | Projection finale fermante | [M01 p. 309 (impr. 292)][M01], l. 30 |
| E146 | Proposition 38.16 | Décidabilité à profondeur fixée | [M01 p. 316 (impr. 299)][M01], l. 45 |
| E147 | Proposition 38.28 | Critère local enrichi par maximum sortant | [M01 p. 319 (impr. 302)][M01], l. 63 |
| E148 | Corollaire 38.32 | Fermeture par majorant enrichi | [M01 p. 321 (impr. 304)][M01], l. 10 |
| E149 | Proposition 38.35 | Terminaison à profondeur fixée | [M01 p. 323 (impr. 306)][M01], l. 12 |
| E150 | Théorème 38.36 | Fermeture par table orientée enrichie | [M01 p. 323 (impr. 306)][M01], l. 38 |
| E151 | Corollaire 38.37 | Retour à la dynamique classique | [M01 p. 324 (impr. 307)][M01], l. 21 |
| E152 | Théorème-programme 38.38 | Données à produire | [M01 p. 324 (impr. 307)][M01], l. 46 |
| E153 | Proposition 39.4 | Traitement tabulaire des points fixes | [M01 p. 326 (impr. 309)][M01], l. 39 |
| E154 | Théorème-programme 39.9 | Fermeture tabulaire au niveau deux | [M01 p. 328 (impr. 311)][M01], l. 20 |
| E155 | Proposition 39.11 | Composition par rouages locaux | [M01 p. 329 (impr. 312)][M01], l. 7 |
| E156 | Proposition 40.4 | Reconstruction exacte de 3n + 1 | [M01 p. 331 (impr. 314)][M01], l. 38 |
| E157 | Corollaire 40.7 | Invariance de loi par croissance décimale | [M01 p. 332 (impr. 315)][M01], l. 51 |
| E158 | Proposition 40.10 | Exactitude de la transition calculée | [M01 p. 333 (impr. 316)][M01], l. 13 |
| E159 | Théorème 40.14 | Schéma de calcul par longueur | [M01 p. 334 (impr. 317)][M01], l. 13 |
| E160 | Corollaire 40.15 | Application à l’infini par ajout de rouages | [M01 p. 334 (impr. 317)][M01], l. 26 |
| E161 | Théorème-programme 40.19 | Génération effective des orbites | [M01 p. 335 (impr. 318)][M01], l. 48 |
| E162 | Proposition 41.4 | Sortie brute de la cellule | [M01 p. 338 (impr. 321)][M01], l. 52 |
| E163 | Corollaire 41.7 | Non-infinité des lois locales | [M01 p. 339 (impr. 322)][M01], l. 44 |
| E164 | Proposition 41.8 | Réduction de tout rouage à E30 | [M01 p. 340 (impr. 323)][M01], l. 16 |
| E165 | Théorème 41.14 | Réduction finie du cycle mobile | [M01 p. 341 (impr. 324)][M01], l. 18 |
| E166 | Proposition 41.15 | Condamnation locale du régime zba | [M01 p. 342 (impr. 325)][M01], l. 5 |
| E167 | Corollaire 41.16 | Forme exacte de la difficulté restante | [M01 p. 342 (impr. 325)][M01], l. 17 |
| E168 | Proposition 42.19 | Réduction finie de la vérification | [M01 p. 348 (impr. 331)][M01], l. 49 |
| E169 | Proposition 42.20 | Condition suffisante grossière | [M01 p. 349 (impr. 332)][M01], l. 21 |
| E170 | Théorème 42.25 | Fermeture par table close | [M01 p. 350 (impr. 333)][M01], l. 22 |
| E171 | Théorème-programme 42.26 | Rôle de Ωγ | [M01 p. 351 (impr. 334)][M01], l. 14 |
| E172 | Proposition 43.14 | Inégalité fondamentale | [M01 p. 355 (impr. 338)][M01], l. 22 |
| E173 | Corollaire 43.15 | Absence de stagnation énergétique | [M01 p. 355 (impr. 338)][M01], l. 30 |
| E174 | Proposition 43.16 | Exclusion tabulaire des cycles non triviaux | [M01 p. 355 (impr. 338)][M01], l. 44 |
| E175 | Proposition 43.17 | Exclusion des trajectoires infinies non terminales | [M01 p. 356 (impr. 339)][M01], l. 19 |
| E176 | Théorème 43.19 | Fermeture globale par certificat énergétique fini | [M01 p. 356 (impr. 339)][M01], l. 40 |
| E177 | Théorème-programme 43.20 | Protocole de certification | [M01 p. 357 (impr. 340)][M01], l. 34 |
| E178 | Proposition 44.4 | Finitude locale | [M01 p. 360 (impr. 343)][M01], l. 55 |
| E179 | Proposition 44.9 | Effet de dissymétrie du pied | [M01 p. 362 (impr. 345)][M01], l. 7 |
| E180 | Proposition 44.17 | Réduction de la dynamique à la table odd-to-odd | [M01 p. 363 (impr. 346)][M01], l. 43 |
| E181 | Proposition 44.24 | Critère de fermeture combinatoire | [M01 p. 365 (impr. 348)][M01], l. 7 |
| E182 | Corollaire 44.25 | Exclusion des cycles non triviaux | [M01 p. 365 (impr. 348)][M01], l. 17 |
| E183 | Théorème 44.26 | Fermeture globale par graphe fini | [M01 p. 365 (impr. 348)][M01], l. 26 |
| E184 | Proposition 45.13 | Critère de fuite dans un graphe fini | [M01 p. 371 (impr. 354)][M01], l. 13 |
| E185 | Théorème 45.16 | Fermeture combinatoire certifiée | [M01 p. 371 (impr. 354)][M01], l. 37 |
| E186 | Proposition 46.4 | Lecture expérimentale du terminal unique | [M01 p. 377 (impr. 360)][M01], l. 33 |
| E187 | Proposition 46.8 | Rôle de la concordance | [M01 p. 379 (impr. 362)][M01], l. 32 |
| E188 | Théorème-programme 46.10 | Passage du certificat expérimental au certificat global | [M01 p. 380 (impr. 363)][M01], l. 43 |
| E189 | Proposition 47.5 | Saturation des rouages | [M01 p. 384 (impr. 367)][M01], l. 38 |
| E190 | Proposition 47.9 | Critère SCC certifiant | [M01 p. 386 (impr. 369)][M01], l. 21 |
| E191 | Corollaire 47.10 | Équivalence fonctionnelle | [M01 p. 386 (impr. 369)][M01], l. 43 |
| E192 | Théorème 47.11 | Passage certifiant | [M01 p. 387 (impr. 370)][M01], l. 12 |
| E193 | Hypothèse 48.9 | Exhaustivité dyadique | [M01 p. 392 (impr. 375)][M01], l. 29 |
| E194 | Proposition 48.13 | Acceptation du certificat | [M01 p. 394 (impr. 377)][M01], l. 31 |
| E195 | Théorème 48.14 | Validation mécanique du certificat final | [M01 p. 394 (impr. 377)][M01], l. 41 |
| E196 | Proposition 49.5 | Audit des classes | [M01 p. 398 (impr. 381)][M01], l. 40 |
| E197 | Proposition 49.8 | Insuffisance de la projection locale | [M01 p. 400 (impr. 383)][M01], l. 31 |
| E198 | Théorème 49.10 | Audit de Πcert | [M01 p. 401 (impr. 384)][M01], l. 13 |
| E199 | Proposition 50.6 | Réduction à l’absence de fuite neutre | [M01 p. 404 (impr. 387)][M01], l. 24 |
| E200 | Hypothèse 50.8 | Non-neutralité persistante | [M01 p. 405 (impr. 388)][M01], l. 24 |
| E201 | Théorème-programme 50.10 | Lemme de non-neutralité persistante du carry | [M01 p. 405 (impr. 388)][M01], l. 37 |
| E202 | Proposition 50.13 | Critère d’exclusion | [M01 p. 406 (impr. 389)][M01], l. 36 |
| E203 | Théorème 50.14 | Fermeture par impossibilité d’obstruction | [M01 p. 406 (impr. 389)][M01], l. 46 |
| E204 | Corollaire 50.15 | Rôle de l’énergie | [M01 p. 407 (impr. 390)][M01], l. 18 |
| E205 | Corollaire 50.16 | Rôle du graphe | [M01 p. 407 (impr. 390)][M01], l. 22 |
| E206 | Proposition 51.6 | Dichotomie locale | [M01 p. 411 (impr. 394)][M01], l. 44 |
| E207 | Théorème 51.10 | Absence d’obstruction fermée par certificat de carry | [M01 p. 412 (impr. 395)][M01], l. 35 |
| E208 | Corollaire 51.11 | Fermeture conditionnelle | [M01 p. 412 (impr. 395)][M01], l. 46 |
| E209 | Théorème-programme 51.12 | Audit tabulaire | [M01 p. 413 (impr. 396)][M01], l. 14 |
| E210 | Corollaire 52.5 | Unicité du mot neutre non atomique | [M01 p. 417 (impr. 400)][M01], l. 36 |
| E211 | Proposition 52.6 | Absence de SCC neutre non terminale | [M01 p. 417 (impr. 400)][M01], l. 54 |
| E212 | Théorème-programme 52.7 | Relèvement après exclusion du neutre strict | [M01 p. 419 (impr. 402)][M01], l. 4 |
| E213 | Proposition 53.7 | Critère de rejet d’une projection | [M01 p. 423 (impr. 406)][M01], l. 13 |
| E214 | Corollaire 53.8 | Nécessité d’une projection plus fine | [M01 p. 423 (impr. 406)][M01], l. 31 |
| E215 | Théorème-programme 53.9 | Prochaine projection | [M01 p. 424 (impr. 407)][M01], l. 29 |

### Rouages et réarmement

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| E216 | Corollaire 3.9 | Deux gains consecutifs impossibles | [R01 p. 5][R01], l. 7 |
| E217 | Corollaire 6.4 | Aucun cycle compose fixe n’est parfaitement periodique | [R01 p. 7][R01], l. 51 |

### Mécanique de Syracuse

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| E218 | Théorème 3.2 | Transition locale exhaustive du pied | [D01 p. 7][D01], l. 24 · [P03 p. 7][P03], l. 24 · [P06 p. 7][P06], l. 24 |
| E219 | Théorème 4.2 | Transition exhaustive du corps | [D01 p. 9][D01], l. 44 · [P03 p. 9][P03], l. 44 · [P06 p. 9][P06], l. 44 |
| E220 | Proposition 6.3 | Matrice globale pied-corps | [D01 p. 15][D01], l. 1 · [P03 p. 15][P03], l. 1 · [P06 p. 15][P06], l. 1 |
| E221 | Proposition 7.6 | Bilan énergétique d’un tour du pied | [D01 p. 17][D01], l. 44 · [P03 p. 17][P03], l. 44 · [P06 p. 17][P06], l. 44 |
| E222 | Proposition 8.6 | Borne de fréquence des portes impaires | [D01 p. 20][D01], l. 1 · [P03 p. 20][P03], l. 1 · [P06 p. 20][P06], l. 1 |
| E223 | Théorème 8.8 | Verrou énergétique par portes directionnelles | [D01 p. 21][D01], l. 1 · [P03 p. 21][P03], l. 1 · [P06 p. 21][P06], l. 1 |
| E224 | Corollaire 8.9 | Contradiction d’un réarmement perpétuel favorable | [D01 p. 22][D01], l. 1 · [P03 p. 22][P03], l. 1 · [P06 p. 22][P06], l. 1 |
| E225 | Théorème 8.10 | Clôture par portes directionnelles | [D01 p. 22][D01], l. 28 · [P03 p. 22][P03], l. 28 · [P06 p. 22][P06], l. 28 |

### Compléments Φ–Ψ v6, v10 et v14

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| E226 | Corollaire 5.7 | Exhaustivité à horizon fini | [P01 p. 4][P01], l. 64 · [P02 p. 5][P02], l. 7 · [P03 p. 27][P03], l. 7 · [P05 p. 5][P05], l. 7 · [P06 p. 27][P06], l. 7 · [P08][P08], l. 277–287 · [P10][P10], l. 289–299 |
| E227 | Proposition 5.8 | Renouvellement des historiques de parité | [P01 p. 5][P01], l. 17 · [P02 p. 5][P02], l. 23 · [P03 p. 27][P03], l. 23 · [P05 p. 5][P05], l. 23 · [P06 p. 27][P06], l. 23 · [P08][P08], l. 292–294 · [P10][P10], l. 304–306 |
| E228 | Proposition 5.10 | Portée d’une tête ajoutée | [P01 p. 6][P01], l. 37 · [P02 p. 6][P02], l. 37 · [P03 p. 28][P03], l. 37 · [P05 p. 6][P05], l. 37 · [P06 p. 28][P06], l. 37 · [P08][P08], l. 341–343 · [P10][P10], l. 353–355 |
| E229 | Proposition 5.11 | Montées nettes arbitrairement longues | [P01 p. 7][P01], l. 51 · [P02 p. 7][P02], l. 51 · [P03 p. 29][P03], l. 51 · [P05 p. 7][P05], l. 51 · [P06 p. 29][P06], l. 51 · [P08][P08], l. 412–417 · [P10][P10], l. 424–429 |
| E230 | Corollaire 5.12 | Critère exact de descente | [P01 p. 8][P01], l. 36 · [P02 p. 8][P02], l. 36 · [P03 p. 30][P03], l. 36 · [P05 p. 8][P05], l. 36 · [P06 p. 30][P06], l. 36 · [P08][P08], l. 450–456 · [P10][P10], l. 462–468 |
| E231 | Conjecture 5.13 | Principe d’écoulement terminal du cône | [P01 p. 9][P01], l. 31 · [P02 p. 9][P02], l. 31 · [P03 p. 31][P03], l. 31 · [P05 p. 9][P05], l. 31 · [P06 p. 31][P06], l. 31 · [P08][P08], l. 503–509 · [P10][P10], l. 515–521 |
| E232 | Théorème 5.14 | Exponentialité combinatoire compatible de Φ–Ψ | [P01 p. 10][P01], l. 20 · [P02 p. 10][P02], l. 20 · [P03 p. 32][P03], l. 20 · [P05 p. 10][P05], l. 20 · [P06 p. 32][P06], l. 20 · [P08][P08], l. 534–540 · [P10][P10], l. 546–552 |
| E233 | Proposition 5.15 | Composition affine exacte des transitions | [P01 p. 12][P01], l. 29 · [P02 p. 12][P02], l. 29 · [P03 p. 34][P03], l. 29 · [P05 p. 12][P05], l. 29 · [P06 p. 34][P06], l. 29 · [P08][P08], l. 618–625 · [P10][P10], l. 630–637 |
| E234 | Corollaire 5.16 | Amplification et retard d’une perturbation de tête | [P01 p. 13][P01], l. 8 · [P02 p. 13][P02], l. 8 · [P03 p. 35][P03], l. 8 · [P05 p. 13][P05], l. 8 · [P06 p. 35][P06], l. 8 · [P08][P08], l. 656–662 · [P10][P10], l. 668–674 |
| E235 | Corollaire 5.17 | Critère de descente à profondeur fixée | [P01 p. 13][P01], l. 37 · [P02 p. 13][P02], l. 37 · [P03 p. 35][P03], l. 37 · [P05 p. 13][P05], l. 37 · [P06 p. 35][P06], l. 37 · [P08][P08], l. 678–687 · [P10][P10], l. 690–699 |
| E236 | Proposition 5.18 | Exhaustivité des paramètres locaux au premier étage | [P01 p. 14][P01], l. 11 · [P02 p. 14][P02], l. 11 · [P03 p. 36][P03], l. 11 · [P05 p. 14][P05], l. 11 · [P06 p. 36][P06], l. 11 · [P08][P08], l. 704–716 · [P10][P10], l. 716–728 |
| E237 | Théorème 5.19 | Récurrence universelle à opérateur unique | [P01 p. 15][P01], l. 43 · [P02 p. 15][P02], l. 43 · [P03 p. 37][P03], l. 43 · [P05 p. 15][P05], l. 43 · [P06 p. 37][P06], l. 43 · [P08][P08], l. 779–794 · [P10][P10], l. 791–806 |
| E238 | Corollaire 5.20 | Stabilité des règles et expansion des historiques | [P01 p. 16][P01], l. 33 · [P02 p. 16][P02], l. 33 · [P03 p. 38][P03], l. 33 · [P05 p. 16][P05], l. 33 · [P06 p. 38][P06], l. 33 · [P08][P08], l. 832–834 · [P10][P10], l. 844–846 |
| E239 | Théorème 5.21 | Atténuation relative du terme additif | [P01 p. 17][P01], l. 12 · [P02 p. 17][P02], l. 12 · [P03 p. 39][P03], l. 12 · [P05 p. 17][P05], l. 12 · [P06 p. 39][P06], l. 12 · [P08][P08], l. 858–865 · [P10][P10], l. 870–877 |
| E240 | Conjecture 5.22 | Écoulement terminal indépendamment de la longueur | [P01 p. 17][P01], l. 52 · [P02 p. 17][P02], l. 52 · [P03 p. 39][P03], l. 52 · [P05 p. 17][P05], l. 52 · [P06 p. 39][P06], l. 52 · [P08][P08], l. 891–893 · [P10][P10], l. 903–905 |
| E241 | Proposition 5.25 | Deux cônes de vingt et un chiffres | [P01 p. 19][P01], l. 18 · [P02 p. 19][P02], l. 18 · [P03 p. 41][P03], l. 18 · [P05 p. 19][P05], l. 18 · [P06 p. 41][P06], l. 18 · [P08][P08], l. 956–969 · [P10][P10], l. 968–981 |
| E242 | Proposition 5.26 | Absence de délai périodique universel | [P01 p. 19][P01], l. 50 · [P02 p. 19][P02], l. 50 · [P03 p. 41][P03], l. 50 · [P05 p. 19][P05], l. 50 · [P06 p. 41][P06], l. 50 · [P08][P08], l. 994–996 · [P10][P10], l. 1006–1008 |
| E243 | Proposition 5.32 | Historiques finis et leurs extensions | [P01 p. 24][P01], l. 12 · [P02 p. 24][P02], l. 12 · [P03 p. 46][P03], l. 12 · [P05 p. 24][P05], l. 12 · [P06 p. 46][P06], l. 12 · [P08][P08], l. 1182–1188 · [P10][P10], l. 1194–1200 |
| E244 | Corollaire 5.33 | Longueur exacte d’une suite initiale impaire | [P01 p. 24][P01], l. 29 · [P02 p. 24][P02], l. 29 · [P03 p. 46][P03], l. 29 · [P05 p. 24][P05], l. 29 · [P06 p. 46][P06], l. 29 · [P08][P08], l. 1193–1199 · [P10][P10], l. 1205–1211 |
| E245 | Théorème 5.34 | Décomposition bidirectionnelle à profondeur élémentaire | [P02 p. 26][P02], l. 60 · [P03 p. 48][P03], l. 60 · [P05 p. 26][P05], l. 60 · [P06 p. 48][P06], l. 60 · [P08][P08], l. 1268–1287 · [P10][P10], l. 1280–1299 |
| E246 | Corollaire 5.35 | Classification finie des données de tête | [P02 p. 28][P02], l. 41 · [P03 p. 50][P03], l. 41 · [P05 p. 28][P05], l. 41 · [P06 p. 50][P06], l. 41 · [P08][P08], l. 1350–1356 · [P10][P10], l. 1362–1368 |
| E247 | Proposition 5.39 | Certificat local de profondeur dyadique | [P02 p. 42][P02], l. 34 · [P03 p. 64][P03], l. 34 · [P04 p. 4][P04], l. 42 · [P05 p. 42][P05], l. 34 · [P06 p. 64][P06], l. 34 · [P08][P08], l. 1878–1887 · [P09][P09], l. 236–245 · [P10][P10], l. 1890–1899 |
| E248 | Théorème 5.40 | Certificats affines par classes dyadiques | [P05 p. 45][P05], l. 27 · [P06 p. 67][P06], l. 27 · [P10][P10], l. 1974–1981 |
| E249 | Corollaire 5.42 | Déficit inférieur certifié | [P05 p. 50][P05], l. 48 · [P06 p. 72][P06], l. 48 · [P10][P10], l. 2216–2227 |
| E250 | Proposition 5.43 | Répartition des profondeurs visibles | [P05 p. 51][P05], l. 26 · [P06 p. 73][P06], l. 26 · [P10][P10], l. 2242–2252 |
| E251 | Théorème 5.44 | Budget de compensation par triplets | [P05 p. 52][P05], l. 19 · [P06 p. 74][P06], l. 19 · [P10][P10], l. 2285–2306 |
| E252 | Proposition 5.45 | Corridors arbitrairement longs | [P05 p. 53][P05], l. 15 · [P06 p. 75][P06], l. 15 · [P10][P10], l. 2330–2332 |
| E253 | Proposition 5.46 | Compatibilité des profondeurs finies | [P05 p. 53][P05], l. 39 · [P06 p. 75][P06], l. 39 · [P10][P10], l. 2345–2347 · [N01](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Etude_Compatibilite_Deficit_v15.md#L17), l. 17 (reformulation sous l’intitulé Théorème) |
| E254 | Proposition 5.47 | Transport inter-blocs des contraintes dyadiques | [P05 p. 54][P05], l. 7 · [P06 p. 76][P06], l. 7 · [P10][P10], l. 2360–2366 |
| E255 | Théorème 5.49 | Opérateur exact de prolongement temporel | [P05 p. 61][P05], l. 33 · [P06 p. 83][P06], l. 33 · [P07 p. 1][P07], l. 40 · [P10][P10], l. 2592–2606 · [P11][P11], l. 105–119 |
| E256 | Corollaire 5.50 | Certificats de déficit sur classes relevées | [P05 p. 63][P05], l. 25 · [P06 p. 85][P06], l. 25 · [P07 p. 3][P07], l. 35 · [P10][P10], l. 2675–2689 · [P11][P11], l. 188–202 |

### Étude de deux réarmements

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| E257 | Corollaire 1 | Coût exact du second prolongement | [E01 p. 2][E01], l. 10 · [E02][E02], l. 83–89 · [E03][E03], l. 39 |
| E258 | Proposition 1 | Certificat de descente sur deux corridors | [E01 p. 2][E01], l. 25 · [E02][E02], l. 96–108 · [E03][E03], l. 41 |
| E259 | Théorème 1 | Fidélité de deux réarmements | [E01 p. 1][E01], l. 43 · [E02][E02], l. 61–75 · [E03][E03], l. 16 |
| E260 | Proposition 2 | Fidélité globale d’un chemin infini | [E01 p. 3][E01], l. 24 · [E02][E02], l. 150–156 · [E03][E03], l. 97 |

### Annexe v17 sur les excursions mixtes

| N° | Référence d’origine | Intitulé | Passages |
|---:|---|---|---|
| E261 | Proposition 1.1 | Trichotomie qualitative exacte | [P01 p. 28][P01], l. 45 · [V01 p. 1][V01], l. 45 · [V02](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex#L32-L34), l. 32–34 |
| E262 | Proposition 3.1 | Première descente et compensation cumulée | [P01 p. 29][P01], l. 52 · [V01 p. 2][V01], l. 52 · [V02](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex#L68-L78), l. 68–78 |
| E263 | Corollaire 3.2 | Nombre exact des représentants non certifiés | [P01 p. 30][P01], l. 20 · [V01 p. 3][V01], l. 20 · [V02](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex#L90-L96), l. 90–96 |
| E264 | Théorème 4.1 | Excursion critique, sans compensation multiplicative sur aucun préfixe | [P01 p. 30][P01], l. 47 · [V01 p. 3][V01], l. 47 · [V02](https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex#L107-L113), l. 107–113 |

[M01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/syracuse_monographie_complete_ch53_audit_sorties_forcees_compensees.pdf
[R01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/syracuse_branche_rouages_rearmement_lemmes.pdf
[D01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/mecanique_syracuse.pdf
[P01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_Complement_v6_et_Annexe_v17.pdf
[P02]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip
[P03]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip
[P04]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip
[P05]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip
[P06]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip
[P07]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip
[E01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip
[V01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/PDF/Syracuse_PhiPsi_Excursions_Mixtes_v17.pdf
[P08]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip
[P09]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Matrice_Multidimensionnelle_v10.zip
[P10]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip
[P11]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Operateur_Temporel_v14_Complet.zip
[E02]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip
[E03]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Deux_Rearmements_Etude_Complete.zip
[V02]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LaTeX/Syracuse_PhiPsi_Excursions_Mixtes_v17.tex
[N01]: https://github.com/PsiGuardian/Syracuse/blob/6e123ae17ae6960ca66dda8f1f024d155c974a38/testing/Syracuse_PhiPsi_Etude_Compatibilite_Deficit_v15.md
