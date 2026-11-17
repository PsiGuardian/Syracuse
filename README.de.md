# SYRACUSE

### Eine strukturelle und multidimensionale Erforschung der Collatz-Vermutung

**Mathematik · Zahlentheorie · Diskrete dynamische Systeme · Algorithmische Forschung**

*Eine elementare Transformation. Eine komplexe Dynamik. Eine mathematische Architektur, die es zu erforschen gilt.*

**[🇫🇷 Français](README.md)  ·  [🇬🇧 English](README.en.md)  ·  [🇩🇪 Deutsch](README.de.md)  ·  [🇪🇸 Español](README.es.md)  ·  [🇮🇱 עברית](README.he.md)  ·  [🇯🇵 日本語](README.ja.md)  ·  [🇨🇳 简体中文](README.zh-CN.md)**

---

## Überblick

Die Syracuse-Vermutung, auch **Collatz-Vermutung** oder **3n+1-Problem** genannt, gehört zu den bekanntesten offenen Problemen der Mathematik.

Ihre Formulierung ist erstaunlich einfach. Ausgehend von einer positiven ganzen Zahl wird wiederholt eine von zwei Operationen ausgeführt:

- Ist die Zahl gerade, wird sie durch zwei geteilt.
- Ist die Zahl ungerade, wird sie mit drei multipliziert und um eins erhöht.

Die Vermutung besagt, dass jede so entstehende Folge schließlich **1** erreicht und dann in den Zyklus **1 → 4 → 2 → 1** übergeht.

Trotz dieser einfachen Regeln gibt es bisher keinen allgemein anerkannten Beweis der universellen Konvergenz.

Dieses Repository dokumentiert die strukturelle Untersuchung der Folgen, ihre Zerlegung in elementare Übergänge und multidimensionale Modelle ihrer Wechselwirkungen.

## I. Syracuse anders untersuchen

Dieser Ansatz beschränkt sich nicht auf die Berechnung einzelner Zahlenfolgen. Er untersucht die Mechanismen, die sie bestimmen. Anstatt jede Zahl isoliert zu betrachten, erforschen wir die Zusammenhänge zwischen:

- Den Ziffern einer Zahl.
- Paritätsübergängen.
- Überträgen und positionsabhängigen Beziehungen.
- Dyadischen Strukturen.
- Wachstums- und Abnahmephasen.
- Übergangskorridoren.
- Zeitlichen Kompositionen.
- Kombinatorischer Expansion bei wachsender Ziffernlänge.

Ziel ist der Übergang von numerischer Beobachtung zu einer **exakten mathematischen Beschreibung der Übergangsmechanismen**.

## II. Die Matrizen Φ und Ψ

Ein zentraler Teil der Forschung beruht auf **Φ (Phi)** und **Ψ (Psi)**. Diese Strukturen klassifizieren Übergänge, Abhängigkeiten und ihre Zusammensetzung. Das Forschungsprogramm betrachtet:

**1. Elementare Übergänge**

Mögliche Transformationen jeder Ziffer, jedes Paritätszustands und jeder Übertragskonfiguration.

**2. Multidimensionale Abhängigkeiten**

Wechselwirkungen zwischen Dezimalstellen und Übergangsebenen.

**3. Verschachtelte Strukturen**

Beziehungen zwischen Zahlen der Länge $n$ und Strukturen der Länge $n+1$.

**4. Kombinatorische Expansion**

Wachstum der möglichen Konfigurationen und Ketten bei zunehmender Länge.

**5. Überlagerung und zeitliche Komposition**

Verbindung lokaler Strukturen über mehrere Übergänge hinweg.

Ziel ist eine kohärente Darstellung der Folgen, von lokalen Operationen bis zu langfristigen Verhaltensweisen.

## III. Die Syracuse-Dynamik

Für jede ganze Zahl $n\geq1$ gilt die klassische Abbildung:

$$
T(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
3n+1 & n\equiv1\pmod2.
\end{cases}
$$

Die verdichtete Abbildung lautet:

$$
S(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
\dfrac{3n+1}{2} & n\equiv1\pmod2.
\end{cases}
$$

Sie unterscheidet zwei Übergangsarten:

- **Dyadischer Abwärtsschritt:** $n\mapsto n/2$.
- **Verdichteter ungerader Aufwärtsschritt:** $n\mapsto(3n+1)/2$.

Ihr Wechselspiel ist ein grundlegender Gegenstand dieser Untersuchung.

## IV. Ziffern und ihre Wechselwirkungen

Eine mehrstellige Zahl verändert sich nicht wie eine Ansammlung unabhängiger Ziffern. Eine Position kann von Überträgen und Zuständen anderer Positionen abhängen. Daher untersuchen wir Dezimaltransformationen als zusammensetzbare Systeme lokaler Abhängigkeiten. Ein Übertrag bei einer lokalen affinen Operation lässt sich schreiben als:

$$
\kappa_\varepsilon(b)=\left\lfloor\frac{3b+\varepsilon}{10}\right\rfloor.
$$

Dabei ist $b$ eine Dezimalziffer und $\varepsilon$ der jeweils relevante Übertragszustand gemäß der verwendeten Konvention.

Diese Darstellung macht die Informationsweitergabe zwischen Positionen untersuchbar. Ziel ist die Beschreibung von Transformationen beliebig langer Zahlen durch exakte lokale Regeln und ihre Komposition.

## V. Multidimensionale Struktur

Das Projekt betrachtet vier sich ergänzende Dimensionen:

**Lokale Struktur** — Exakte Regeln für jede Ziffer und jeden Zustand.

**Räumliche Struktur** — Wechselwirkungen zwischen den Ziffernpositionen.

**Kombinatorische Struktur** — Zulässige Konfigurationen, Expansion und Verschachtelung.

**Zeitliche Struktur** — Aufeinanderfolgende Übergänge, ihre Komposition und die erzeugten Folgen.

Diese Dimensionen sind nicht unabhängig: Gerade ihre Wechselwirkungen sind Forschungsgegenstand.

*Wie erzeugt eine deterministische Dynamik aus zwei elementaren Operationen eine solche Vielfalt von Strukturen und Folgen?*

## VI. Mathematisches Ziel

Das Programm verfolgt ein Hauptziel:

**Eine universelle Charakterisierung der Syracuse-Folgen durch ihre elementaren Strukturen und Kompositionsgesetze.**

Dazu müssen unterschieden werden:

1. Exakte Darstellung der Übergänge.
2. Vollständigkeit der dargestellten Konfigurationen.
3. Treue der Kompositionen bei beliebigen Längen und Zeiträumen.
4. Analyse zulässiger unendlicher Folgen.
5. Beweis oder Nichtbeweis ihrer Konvergenz zum Endzyklus.

Eine exakte Beschreibung der Dynamik ist für sich genommen kein Beweis der Vermutung. Universelle Konvergenz verlangt ein zusätzliches strenges Argument, das jede positive nicht konvergente Folge ausschließt.

### Dokumentierte Forschungsarbeiten und Ergebnisse (v15–v17)

Die Dokumente unterscheiden exakte Identitäten, Zertifikate für endliche Horizonte und offene Fragen. Ausgewählte Punkte:

- **v15 — Dyadische Kompatibilität:** Jede endliche Folge strikt positiver ungerader Schritttiefen wird durch eine unendliche Restklasse realisiert.
- **v15 — Zertifikate des ersten Abstiegs:** Arithmetische Kriterien mit Schritttiefen und unteren Schranken führender Stellen; Dichteaussagen sind keine Garantie für jede einzelne Zahl.
- **v17 — Doppelzertifikat:** Eine Kompatibilitätsuntergrenze und eine Obergrenze ohne Abstieg zertifizieren den ersten Abstieg an Korridorenden, sobald sie unvereinbar werden.
- **v17 — Endliche Prüfung:** 199.287 begrenzte Muster für $K=1$ bis $5$; sieben Familien über je 300 Horizonte.
- **v17 — Oberes kritisches Wort:** Nicht letztlich periodische Konstruktion mit multiplikativ expansiven endlichen Präfixen; ihre Realisierung durch eine einzelne positive Zahl ist nicht gezeigt.

**Gesamtstatus:** Diese Ergebnisse beweisen weder universelle Konvergenz noch den Ausschluss nichtterminaler Zyklen oder aller positiven divergenten Bahnen.

$$
D_Kq_K=A_Kq_0+C_K,
\qquad q_{0,\min}(K)\leq q_0\leq Q_K.
$$

## VII. Aufbau des Repositorys

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

### Hauptmanuskript

[`mecanique_syracuse.pdf`](mecanique_syracuse.pdf) — Dokument zur mathematischen und strukturellen Untersuchung der Syracuse-Dynamik.

### Φ/Ψ-Atlas v17

[`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md`](Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md) — Wissenschaftlicher Anhang zu gemischten Exkursionen, arithmetischen Zertifikaten und kritischen Konfigurationen.

### Experimentelles Verzeichnis

[`testing/`](testing/) — Hier befinden sich Programme, Matrizen, numerische Ergebnisse, Zwischenstudien und Forschungsarchive.

Experimentelle Ergebnisse sind von formell bewiesenen Aussagen zu unterscheiden.

## VIII. Wissenschaftliche Reproduzierbarkeit

Reproduzierbarkeit ist ein grundlegendes Prinzip. Die Arbeiten sollen Folgendes ermöglichen:

- Verwendete Annahmen und Definitionen nachvollziehen.
- Berechnungen mit Skripten reproduzieren.
- Erzeugte Matrizen und Übergänge prüfen.
- Tatsächlich überprüfte Bereiche benennen.
- Beschränkte vollständige Prüfung vom universellen Beweis unterscheiden.
- Gegenbeispiele zu Zwischenaussagen dokumentieren.

Mathematische Forschung gewinnt an Wert, wenn ihre Ergebnisse unabhängig geprüft, reproduziert, kritisiert und verbessert werden können.

### Reproduktion der v17-Untersuchung

Das Python-Skript des Atlas benötigt nur die Standardbibliothek und kann im Verzeichnis `Code/` gestartet werden:

```bash
cd Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/Code
python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 5 --max-rt 3 --path-horizon 300
```

## IX. Beiträge

Wissenschaftliche und technische Beiträge sind willkommen. Möglich sind:

- Definitionen und Beweise prüfen.
- Numerische Experimente reproduzieren.
- Fehler oder unzureichend begründete Annahmen melden.
- Neue Klassifikationen vorschlagen.
- Algorithmen verbessern.
- Pull Requests mit mathematischer oder technischer Begründung einreichen.

Jede Änderung wird vor der Übernahme geprüft. **Die Veröffentlichung eines Beitrags bedeutet keine mathematische Bestätigung.**

## X. Forschungsphilosophie

Die Einfachheit einer Regel garantiert nicht die Einfachheit der erzeugten Strukturen. Syracuse illustriert dies besonders eindrucksvoll. Unsere Forschung untersucht, wie elementare Operationen, lokale Abhängigkeiten, multidimensionale Strukturen und zeitliche Kompositionen die globale Dynamik hervorbringen. Es geht nicht bloß darum, mehr Zahlenfolgen zu berechnen, sondern die Gesetze ihrer Entstehung zu verstehen.

---

## Autor

**Andrew Caron**

GitHub : [PsiGuardian](https://github.com/PsiGuardian)

Syracuse : [PsiGuardian/Syracuse](https://github.com/PsiGuardian/Syracuse)

---

*„Eine Folge zu verstehen bedeutet nicht nur, ihr Ziel zu kennen, sondern die Gesetze, die jeden ihrer Schritte ermöglichen.“*

**SYRACUSE — Vom elementaren Übergang zur universellen Struktur.**