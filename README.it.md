# SYRACUSE

### Un'esplorazione strutturale e multidimensionale della congettura di Collatz

**Matematica · Teoria dei numeri · Sistemi dinamici discreti · Ricerca algoritmica**

*Una trasformazione elementare. Una dinamica complessa. Un'architettura matematica da esplorare.*

**[🇫🇷 Français](README.md) · [🇬🇧 English](README.en.md) · [🇩🇪 Deutsch](README.de.md) · [🇪🇸 Español](README.es.md) · [🇮🇱 עברית](README.he.md) · [🇯🇵 日本語](README.ja.md) · [🇨🇳 简体中文](README.zh-CN.md) · [🇮🇳 हिन्दी](README.hi.md) · [🇮🇹 Italiano](README.it.md) · [🇬🇪 ქართული](README.ka.md)**

---

## Presentazione

La congettura di Syracuse, nota come congettura di Collatz o problema 3n+1, afferma che ogni traiettoria da un intero positivo raggiunga 1 e poi il ciclo 1 → 4 → 2 → 1. La convergenza universale rimane un problema aperto.

- Se il numero è pari, dividerlo per due.
- Se il numero è dispari, moltiplicarlo per tre e aggiungere uno.

## I. Un altro modo di studiare Syracuse

La ricerca non si limita a calcolare traiettorie: analizza le relazioni tra cifre, parità, riporti, dipendenze posizionali, strutture diadiche, crescita e discesa, corridoi, composizioni temporali ed espansione combinatoria.

## II. Le matrici Φ e Ψ

Φ e Ψ classificano transizioni, dipendenze e composizioni. Il programma comprende transizioni elementari, dipendenze multidimensionali, strutture annidate da n a n+1 cifre, espansione combinatoria, sovrapposizione e composizione temporale.

## III. La dinamica di Syracuse

$$
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\3n+1&n\equiv1\pmod2.\end{cases}
\qquad
S(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
$$

- $n\mapsto n/2$.
- $n\mapsto(3n+1)/2$.

## IV. Le cifre e le loro interazioni

Le cifre di un intero non si trasformano indipendentemente: i riporti collegano posizioni diverse. Qui b è una cifra decimale ed ε uno stato di riporto secondo la convenzione adottata.

$$\kappa_\varepsilon(b)=\left\lfloor\frac{3b+\varepsilon}{10}\right\rfloor.$$

## V. La struttura multidimensionale

Le quattro dimensioni sono locale (regole esatte), spaziale (dipendenze fra posizioni), combinatoria (configurazioni ammissibili) e temporale (composizione delle transizioni).

## VI. Obiettivo matematico

Caratterizzare universalmente le traiettorie a partire dalle strutture elementari. Occorre distinguere rappresentazione esatta, esaustività, fedeltà delle composizioni per ogni lunghezza e tempo, traiettorie infinite ammissibili e dimostrazione della convergenza. La descrizione esatta non è di per sé una prova.

### Ricerche e risultati documentati (v15–v17)

La v15 dimostra la compatibilità di ogni sequenza finita di profondità positive con una classe residua infinita e fornisce criteri aritmetici di prima discesa. La v17 presenta un doppio certificato (limite inferiore di compatibilità e superiore di non-discesa), un audit di 199.287 motivi limitati per K=1…5 e sette famiglie su 300 orizzonti. Una parola critica non definitivamente periodica ha prefissi moltiplicativamente espansivi, ma la sua realizzazione infinita da un unico intero positivo non è dimostrata. Nessuno di questi risultati prova la convergenza universale.

$$D_Kq_K=A_Kq_0+C_K,\qquad q_{0,\min}(K)\leq q_0\leq Q_K.$$

## VII. Organizzazione del repository

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
└── testing/
```

- [mecanique_syracuse.pdf](mecanique_syracuse.pdf)
- [Atlas Φ/Ψ v17](Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md)
- [testing/](testing/)

## VIII. Riproducibilità scientifica

Definizioni, ipotesi, script, matrici e domini verificati devono essere accessibili. Una verifica esaustiva limitata va distinta da una dimostrazione universale; gli eventuali controesempi devono essere documentati.

```bash
cd Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/Code
python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 5 --max-rt 3 --path-horizon 300
```

## IX. Contributi

Sono benvenuti verifiche delle dimostrazioni, riproduzioni indipendenti, segnalazioni di errori, nuove classificazioni, miglioramenti algoritmici e Pull Requests giustificate. Pubblicare un contributo non significa convalidarlo matematicamente.

## X. Filosofia della ricerca

La semplicità di una regola non implica strutture semplici. L'obiettivo non è soltanto calcolare altre traiettorie, ma comprendere le leggi che rendono possibile ogni loro movimento.

---

## Autore

**Andrew Caron**

GitHub: [PsiGuardian](https://github.com/PsiGuardian)

Syracuse: [PsiGuardian/Syracuse](https://github.com/PsiGuardian/Syracuse)

---

**SYRACUSE — Dalla transizione elementare alla struttura universale.**
