# SYRACUSE

### Una exploración estructural y multidimensional de la conjetura de Collatz

**Matemáticas · Teoría de números · Sistemas dinámicos discretos · Investigación algorítmica**

*Una transformación elemental. Una dinámica compleja. Una arquitectura matemática por explorar.*

**[🇫🇷 Français](README.md)  ·  [🇬🇧 English](README.en.md)  ·  [🇩🇪 Deutsch](README.de.md)  ·  [🇪🇸 Español](README.es.md)  ·  [🇮🇱 עברית](README.he.md)  ·  [🇯🇵 日本語](README.ja.md)  ·  [🇨🇳 简体中文](README.zh-CN.md)  ·  [🇮🇳 हिन्दी](README.hi.md)  ·  [🇮🇹 Italiano](README.it.md)  ·  [🇬🇪 ქართული](README.ka.md)**

---

## Presentación

La conjetura de Syracuse, también llamada **conjetura de Collatz** o problema **3n+1**, es uno de los problemas abiertos más conocidos de las matemáticas.

Su enunciado es extraordinariamente simple. A partir de un entero positivo, se repite una de dos operaciones:

- Si el número es par, se divide entre dos.
- Si es impar, se multiplica por tres y se suma uno.

La conjetura afirma que toda trayectoria así obtenida acaba alcanzando **1** y entra en el ciclo **1 → 4 → 2 → 1**.

Pese a la sencillez de las reglas, todavía no se conoce una demostración general aceptada de la convergencia.

Este repositorio reúne una investigación sobre la estructura de las trayectorias, su descomposición en transiciones elementales y modelos multidimensionales de sus interacciones.

## I. Otra forma de estudiar Syracuse

El enfoque no consiste únicamente en calcular trayectorias de enteros sucesivos. Busca comprender los mecanismos que las gobiernan. En lugar de considerar cada número de forma aislada, estudiamos relaciones entre:

- Los dígitos que componen un entero.
- Las transiciones de paridad.
- Los acarreos y las dependencias posicionales.
- Las estructuras diádicas.
- Las fases de crecimiento y descenso.
- Los corredores de transición.
- Las composiciones temporales.
- La expansión combinatoria al aumentar la longitud de los enteros.

El objetivo es pasar de la observación numérica a una **descripción matemática exacta de los mecanismos de transición**.

## II. Las matrices Φ y Ψ

Una parte central del estudio se basa en **Φ (Phi)** y **Ψ (Psi)**, herramientas para clasificar y representar transiciones, dependencias y composiciones. El programa examina:

**1. Transiciones elementales**

Transformaciones posibles para cada dígito, estado de paridad y configuración de acarreo.

**2. Dependencias multidimensionales**

Interacciones entre posiciones decimales y niveles de transición.

**3. Anidamiento de estructuras**

Relación entre los comportamientos de longitud $n$ y los de longitud $n+1$.

**4. Expansión combinatoria**

Crecimiento del número de configuraciones y cadenas posibles.

**5. Superposición y composición temporal**

Combinación de estructuras locales a lo largo de varias transiciones.

El propósito es representar coherentemente las trayectorias, desde las operaciones locales hasta el comportamiento a largo plazo.

## III. La dinámica de Syracuse

Para todo entero $n\geq1$, la transformación clásica es:

$$
T(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
3n+1 & n\equiv1\pmod2.
\end{cases}
$$

Una versión condensada se define como:

$$
S(n)=\begin{cases}
\dfrac n2 & n\equiv0\pmod2,\\[5pt]
\dfrac{3n+1}{2} & n\equiv1\pmod2.
\end{cases}
$$

Esta segunda forma permite distinguir dos tipos de transiciones:

- **Descenso diádico:** $n\mapsto n/2$.
- **Ascenso impar condensado:** $n\mapsto(3n+1)/2$.

La alternancia de estas transformaciones es fundamental para el estudio.

## IV. Los dígitos y sus interacciones

Un entero de varias cifras no se transforma como una simple colección de dígitos independientes. Una posición puede depender de los acarreos y estados procedentes de otras. Por ello estudiamos las transformaciones decimales como sistemas de dependencias locales que pueden componerse. Un acarreo asociado a una operación afín local puede expresarse así:

$$
\kappa_\varepsilon(b)=\left\lfloor\frac{3b+\varepsilon}{10}\right\rfloor.
$$

donde $b$ es un dígito decimal y $\varepsilon$ es el estado de acarreo correspondiente según la convención utilizada.

Esta expresión permite analizar la propagación de información entre posiciones. La intención es caracterizar transformaciones de enteros de longitud arbitraria mediante reglas locales exactas y sus composiciones.

## V. La estructura multidimensional

El proyecto explora cuatro dimensiones complementarias:

**Estructura local** — Reglas exactas para cada dígito y estado.

**Estructura espacial** — Interacciones entre posiciones y dependencias.

**Estructura combinatoria** — Configuraciones admisibles, expansiones y anidamientos.

**Estructura temporal** — Transiciones sucesivas, composiciones y trayectorias.

Estas dimensiones no son independientes: sus interacciones son precisamente objeto de la investigación.

*¿Cómo puede una dinámica determinista definida por dos operaciones elementales generar tanta diversidad de estructuras y trayectorias?*

## VI. Objetivo matemático

El programa persigue un objetivo principal:

**Establecer una caracterización universal de las trayectorias de Syracuse a partir de estructuras elementales y leyes de composición.**

Para ello se debe distinguir entre:

1. Representación exacta de las transiciones.
2. Exhaustividad de las configuraciones representadas.
3. Fidelidad de las composiciones para cualquier longitud y duración.
4. Análisis de las trayectorias infinitas admisibles.
5. Demostración, o no, de su convergencia al ciclo terminal.

Una descripción exacta de la dinámica no es, por sí sola, una demostración de la conjetura. La convergencia universal requiere un argumento adicional que excluya rigurosamente toda trayectoria positiva no convergente.

### Trabajos y resultados documentados (v15–v17)

Los documentos distinguen identidades exactas, certificados de horizonte finito y cuestiones abiertas. Algunos puntos destacados:

- **v15 — Compatibilidad diádica:** toda secuencia finita de profundidades impares estrictamente positivas se realiza en una clase residual infinita.
- **v15 — Certificados de primer descenso:** criterios aritméticos basados en profundidades y cotas inferiores de las cifras iniciales; los resultados de densidad no garantizan cada caso individual.
- **v17 — Certificado doble:** un límite inferior de compatibilidad y un límite superior de no descenso certifican el primer descenso en los extremos de los corredores cuando se vuelven incompatibles.
- **v17 — Auditoría finita:** 199 287 patrones acotados para $K=1$ a $5$; siete familias analizadas durante 300 horizontes cada una.
- **v17 — Palabra crítica superior:** construcción no finalmente periódica cuyos prefijos finitos son multiplicativamente expansivos; no se ha demostrado que un mismo entero positivo realice toda la secuencia.

**Estado general:** estos resultados no prueban la convergencia universal ni excluyen ciclos no terminales o toda divergencia positiva.

$$
D_Kq_K=A_Kq_0+C_K,
\qquad q_{0,\min}(K)\leq q_0\leq Q_K.
$$

## VII. Organización del repositorio

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

### Manuscrito principal

[`mecanique_syracuse.pdf`](mecanique_syracuse.pdf) — Documento dedicado al estudio matemático y estructural de la dinámica de Syracuse.

### Atlas Φ/Ψ v17

[`Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md`](Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/LISEZMOI.md) — Complemento científico sobre excursiones mixtas, certificados aritméticos y configuraciones críticas.

### Directorio experimental

[`testing/`](testing/) — Contiene programas, matrices, resultados numéricos, estudios intermedios y archivos de investigación.

Los resultados experimentales deben distinguirse de las proposiciones demostradas formalmente.

## VIII. Reproducibilidad científica

La reproducibilidad es un principio esencial. Los trabajos deben permitir:

- Consultar las hipótesis y definiciones utilizadas.
- Reproducir los cálculos con los scripts.
- Comprobar las matrices y transiciones generadas.
- Identificar los dominios realmente verificados.
- Distinguir una verificación exhaustiva acotada de una demostración universal.
- Documentar posibles contraejemplos de proposiciones intermedias.

La investigación matemática adquiere valor cuando sus resultados pueden examinarse, reproducirse, criticarse y mejorarse de forma independiente.

### Reproducción del estudio v17

El script Python del atlas utiliza la biblioteca estándar y se ejecuta desde el directorio `Code/`:

```bash
cd Syracuse_PhiPsi_v17_Excursions_Mixtes_Atlas/Code
python3 phi_psi_mixed_excursions_v17.py --out resultats_v17 --max-horizon 5 --max-rt 3 --path-horizon 300
```

## IX. Contribuciones

Las contribuciones científicas y técnicas son bienvenidas. Se puede:

- Examinar definiciones y demostraciones.
- Reproducir experimentos numéricos.
- Notificar errores o hipótesis insuficientemente justificadas.
- Proponer nuevas clasificaciones.
- Mejorar los algoritmos.
- Enviar una Pull Request con justificación matemática o técnica.

Toda propuesta se revisa antes de su integración. **Publicar una contribución no implica validar matemáticamente su contenido.**

## X. Filosofía de investigación

La simplicidad de una regla no garantiza la simplicidad de las estructuras que genera. Syracuse es un ejemplo especialmente notable. Esta investigación pretende comprender cómo las operaciones elementales, las dependencias locales, las estructuras multidimensionales y las composiciones temporales interactúan para producir la dinámica global. No se trata solamente de calcular más trayectorias, sino de comprender qué las hace posibles.

---

## Autor

**Andrew Caron**

GitHub : [PsiGuardian](https://github.com/PsiGuardian)

Syracuse : [PsiGuardian/Syracuse](https://github.com/PsiGuardian/Syracuse)

---

*«Comprender una trayectoria no es solo conocer su destino, sino entender las leyes que hacen posible cada uno de sus movimientos».*

**SYRACUSE — De la transición elemental a la estructura universal.**