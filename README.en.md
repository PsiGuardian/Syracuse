# SYRACUSE

### A structural and multidimensional exploration of the Collatz conjecture

**Mathematics · Number theory · Discrete dynamical systems · Algorithmic research**

*An elementary transformation. A complex dynamic. A mathematical architecture to explore.*

**[🇫🇷 Français](README.md)  ·  [🇬🇧 English](README.en.md)  ·  [🇩🇪 Deutsch](README.de.md)  ·  [🇪🇸 Español](README.es.md)  ·  [🇮🇱 עברית](README.he.md)  ·  [🇯🇵 日本語](README.ja.md)  ·  [🇨🇳 简体中文](README.zh-CN.md)**

---

## Overview

The Syracuse conjecture, also known as the **Collatz conjecture** or the **3n+1 problem**, is one of the best-known open problems in mathematics.

Its statement is remarkably simple. Starting from any positive integer, repeatedly apply one of two operations:

- If the number is even, divide it by two.
- If the number is odd, multiply it by three and add one.

The conjecture asserts that every resulting trajectory eventually reaches **1** and then enters the cycle **1 → 4 → 2 → 1**.

Despite the simplicity of these rules, no generally accepted proof of universal convergence is currently known.

This repository brings together research on the structural analysis of Syracuse trajectories, their decomposition into elementary transitions, and multidimensional models of their interactions.

## I. Another way to study Syracuse

This research does not merely compute successive integer trajectories. It investigates the mechanisms governing them. Instead of treating each integer in isolation, we study relationships among:

- The digits composing an integer.
- Parity transitions.
- Carries and positional dependencies.
- Dyadic structures.
- Growth and descent phases.
- Transition corridors.
- Temporal compositions.
- Combinatorial expansion as the number of digits increases.

The goal is to move from numerical observation to an **exact mathematical description of transition mechanisms**.

## II. The Φ and Ψ matrices

A central part of this work concerns **Φ (Phi)** and **Ψ (Psi)**, structures for classifying and representing transitions, dependencies, and their compositions. The research program examines:

**1. Elementary transitions**

Transformations available to each digit, parity state, and carry configuration.

**2. Multidimensional dependencies**

Interactions between decimal positions and levels of transition.

**3. Nested structures**

How behavior for integers of length $n$ relates to structures of length $n+1$.

**4. Combinatorial expansion**

Growth in the number of configurations and possible chains as digit length increases.

**5. Superposition and temporal composition**

Combination of local structures and their evolution through multiple transitions.

The aim is a coherent representation of trajectories, from local operations to long-term behavior.

## III. Syracuse dynamics

For every integer $n\geq1$, the classical transformation is:

$$
T(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
3n+1 & n\equiv1\pmod2.
\end{cases}
$$

A condensed version of the dynamics is:

$$
S(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
\dfrac{3n+1}{2} & n\equiv1\pmod2.
\end{cases}
$$

The second formulation distinguishes two types of transitions:

- **Dyadic descent:** $n\mapsto n/2$.
- **Condensed odd-step ascent:** $n\mapsto(3n+1)/2$.

The alternation between these transformations is central to this study.

## IV. Digits and their interactions

A multi-digit integer does not transform as a collection of independent digits. A position may depend on carries and states propagated from other positions. We therefore study decimal transformations as composable systems of local dependencies. A carry in a local affine operation may be written as:

$$
\kappa_\varepsilon(b)=\left\lfloor\frac{3b+\varepsilon}{10}\right\rfloor.
$$

where $b$ is a decimal digit and $\varepsilon$ denotes the relevant carry state under the chosen convention.

This representation helps analyze the propagation of information between positions. The objective is to characterize transformations of integers of arbitrary length through exact local rules and their compositions.

## V. Multidimensional structure

The project explores four complementary dimensions:

**Local structure** — Exact rules applying to each digit and state.

**Spatial structure** — Interactions among digit positions and their dependencies.

**Combinatorial structure** — Admissible configurations, expansions, and nested relationships.

**Temporal structure** — Successive transitions, their compositions, and the resulting trajectories.

These dimensions cannot be understood independently: their interactions are a central object of research.

*How can a deterministic dynamic defined by two elementary operations generate such a diversity of structures and trajectories?*

## VI. Mathematical objective

The program pursues a principal goal:

**To establish a universal characterization of Syracuse trajectories from elementary structures and their laws of composition.**

This requires distinguishing:

1. Exact representation of transitions.
2. Exhaustiveness of represented configurations.
3. Fidelity of compositions at arbitrary lengths and times.
4. Analysis of admissible infinite trajectories.
5. Proof, or lack thereof, of convergence to the terminal cycle.

An exact representation of the dynamics is not, by itself, a proof of the conjecture. Universal convergence requires an additional rigorous argument excluding every positive nonconvergent trajectory.

### Documented research and results (v15–v17)

The repository distinguishes exact identities, finite-horizon certificates, and open problems. Selected results:

- **v15 — Dyadic compatibility:** every finite sequence of strictly positive odd-step depths is realized by an infinite residue class.
- **v15 — First-descent certificates:** arithmetic criteria based on depths and leading-digit lower bounds; density results do not guarantee behavior for each integer.
- **v17 — Double certificate:** a compatibility floor and a non-descent ceiling certify first descent at corridor endpoints when they become incompatible.
- **v17 — Finite audit:** 199,287 bounded patterns for $K=1$ through $5$; seven families studied across 300 horizons each.
- **v17 — Upper critical word:** a non-eventually-periodic construction with multiplicatively expansive finite prefixes; realization of the entire word by one positive integer has not been shown.

**Overall status:** these results do not prove universal convergence, exclude nonterminal cycles, or rule out every positive divergent trajectory.

$$
D_Kq_K=A_Kq_0+C_K,
\qquad q_{0,\min}(K)\leq q_0\leq Q_K.
$$

## VII. Repository organization

```text
Syracuse/
├── README.md
├── README.en.md
├── README.de.md
├── README.es.md
├── README.he.md
├── README.ja.md
├── README.zh-CN.md
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

### Main manuscript

[`mecanique_syracuse.pdf`](mecanique_syracuse.pdf) — Document devoted to the mathematical and structural study of Syracuse dynamics.

### Φ/Ψ v17 atlas

[`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md`](Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md) — Scientific supplement covering mixed excursions, arithmetic certificates, and critical configurations.

### Experimental directory

[`testing/`](testing/) — This directory includes programs, matrices, numerical results, intermediate studies, and research archives.

Experimental findings must be distinguished from formally proved mathematical statements.

## VIII. Scientific reproducibility

Reproducibility is a core principle. The research should make it possible to:

- Retrieve the assumptions and definitions used.
- Reproduce calculations using the scripts.
- Check the generated matrices and transitions.
- Identify the domains actually verified.
- Distinguish exhaustive bounded verification from universal proof.
- Document counterexamples to intermediate proposals.

Mathematical research becomes more valuable when its results can be independently examined, reproduced, challenged, and improved.

### Reproducing the v17 study

The atlas Python script uses the standard library and can be run from its `Code/` directory:

```bash
cd Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/Code
python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 5 --max-rt 3 --path-horizon 300
```

## IX. Contributions

Scientific and technical contributions are welcome. You can:

- Review definitions and proofs.
- Reproduce numerical experiments.
- Report an error or insufficiently justified assumption.
- Suggest new classifications.
- Improve algorithms.
- Submit a Pull Request with mathematical or technical justification.

Every proposed change must be reviewed before inclusion. **Publication of a contribution does not imply mathematical validation.**

## X. Research philosophy

The simplicity of a rule does not imply that the structures it generates are simple. Syracuse is a particularly striking illustration. This research seeks to understand how elementary operations, local dependencies, multidimensional structures, and temporal compositions interact to produce the global dynamics. The aim is not merely to compute more trajectories, but to understand what makes them possible.

---

## Author

**Andrew Caron**

GitHub : [PsiGuardian](https://github.com/PsiGuardian)

Syracuse : [PsiGuardian/Syracuse](https://github.com/PsiGuardian/Syracuse)

---

*“Understanding a trajectory is not merely knowing its destination; it is understanding the laws that make each step possible.”*

**SYRACUSE — From elementary transitions to universal structure.**