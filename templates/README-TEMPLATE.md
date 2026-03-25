# Template LaTeX para Trabajos Prácticos

## 📋 Descripción

Template completo y flexible para trabajos prácticos académicos, con soporte para código de programación, entornos matemáticos (teoremas, definiciones), tablas, gráficos y espaciado optimizado para mejor legibilidad.

---

## 🚀 Inicio Rápido

### Paso 1: Completar datos del trabajo

Editar las líneas 124-130:

```latex
\newcommand{\universidad}{Universidad Católica de Salta}
\newcommand{\carrera}{Licenciatura en Ciencia de Datos}
\newcommand{\materia}{Nombre de la Materia}           % ← CAMBIAR
\newcommand{\trabajo}{Trabajo Práctico N°}            % ← CAMBIAR
\newcommand{\profesor}{Nombre del Profesor}           % ← CAMBIAR
\newcommand{\alumno}{Facundo Luna}
\newcommand{\fecha}{\today}
```

### Paso 2: Configurar el logo

**Opción A - Con logo:**
```latex
\newcommand{\logoportada}{\logoincluido}
```

**Opción B - Sin logo:**
```latex
\newcommand{\logoportada}{\logoomitido}
```

### Paso 3: Escribir el contenido

Reemplazar los ejemplos con tus ejercicios.

---

## 📚 Guía de Uso por Tipo de Materia

### Para Materias de Programación (Python, Java, C, etc.)

**Usar principalmente:**
- Entorno `ejercicio` / `resolucion`
- Bloques de código con `lstlisting`

**Ejemplo:**

```latex
\section{Ejercicio 1}

\begin{ejercicio}
Escribir una función que calcule el factorial de un número.
\end{ejercicio}

\begin{resolucion}

\begin{lstlisting}[style=python, caption={Función factorial}]
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
\end{lstlisting}

\end{resolucion}
```

**Estilos de código disponibles:**
- `style=python` → Python
- `style=java` → Java
- `style=c` → C
- `style=r` → R
- `style=bash` → Bash/Terminal

---

### Para Materias Matemáticas (Álgebra, Cálculo, Estadística)

**Usar principalmente:**
- Entornos de teorema: `teorema`, `lema`, `proposicion`, `corolario`
- Entornos de definición: `definicion`, `ejemplo`
- Entorno de observación: `observacion`

**Ejemplo:**

```latex
\section{Límites}

\begin{definicion}[Límite de una función]
Sea $f$ una función definida en un intervalo abierto que contiene a $a$...
\end{definicion}

\begin{teorema}
El límite de una suma es la suma de los límites.
\[
    \lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)
\]
\end{teorema}

\begin{ejemplo}
Calcular $\lim_{x \to 2} (x^2 + 3x)$...
\end{ejemplo}
```

---

### Para Materias Mixtas (Ciencia de Datos, Machine Learning)

**Combinar ambos estilos:**

```latex
\section{Regresión Lineal}

\begin{definicion}[Regresión Lineal Simple]
Modelo estadístico que relaciona una variable dependiente $y$ con una 
variable independiente $x$ mediante la ecuación:
\[
    y = \beta_0 + \beta_1 x + \epsilon
\]
\end{definicion}

\begin{ejercicio}
Implementar regresión lineal en Python usando NumPy.
\end{ejercicio}

\begin{resolucion}

\begin{lstlisting}[style=python, caption={Regresión lineal con NumPy}]
import numpy as np

def regresion_lineal(x, y):
    n = len(x)
    beta_1 = (n * np.sum(x*y) - np.sum(x) * np.sum(y)) / \
             (n * np.sum(x**2) - np.sum(x)**2)
    beta_0 = np.mean(y) - beta_1 * np.mean(x)
    return beta_0, beta_1
\end{lstlisting}

\end{resolucion}
```

---

## 🎨 Elementos Disponibles

### Entornos de Ejercicio
```latex
\begin{ejercicio}[Título opcional]
Enunciado del ejercicio...
\end{ejercicio}

\begin{resolucion}
Desarrollo de la solución...
\end{resolucion}
```

### Entornos Matemáticos
```latex
\begin{teorema}[Nombre del teorema]
Enunciado...
\end{teorema}

\begin{definicion}[Concepto]
Definición...
\end{definicion}

\begin{ejemplo}
Ejemplo concreto...
\end{ejemplo}

\begin{observacion}
Nota o aclaración...
\end{observacion}
```

### Código
```latex
% Código en bloque
\begin{lstlisting}[style=python, caption={Descripción}]
# Código aquí
\end{lstlisting}

% Código inline
El comando \codigo{print("Hola")} imprime texto.
```

### Tablas
```latex
\begin{table}[H]
    \centering
    \caption{Título de la tabla}
    \label{tab:etiqueta}
    \begin{tabular}{lcc}
        \toprule
        \textbf{Col 1} & \textbf{Col 2} & \textbf{Col 3} \\
        \midrule
        Dato 1 & Dato 2 & Dato 3 \\
        Dato 4 & Dato 5 & Dato 6 \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Gráficos con TikZ/pgfplots
```latex
\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \begin{axis}[
            width=10cm, height=6cm,
            xlabel={$x$}, ylabel={$y$},
            title={Título del gráfico},
            grid=major,
        ]
            \addplot[blue, thick] {x^2};
        \end{axis}
    \end{tikzpicture}
    \caption{Descripción del gráfico}
    \label{fig:etiqueta}
\end{figure}
```

### Imágenes externas
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{ruta/a/imagen.png}
    \caption{Descripción de la imagen}
    \label{fig:etiqueta}
\end{figure}
```

---

## 🔧 Personalización

### Cambiar el interlineado
```latex
\setstretch{1.15}  % Cambiar a 1.0 (simple) o 1.5 (más espaciado)
```

### Cambiar espaciado entre párrafos
```latex
\setlength{\parskip}{0.5em}  % Aumentar o disminuir
```

### Agregar sangría a párrafos
```latex
\setlength{\parindent}{1.5em}  % En lugar de 0pt
```

### Comentar entornos matemáticos si no se usan
```latex
% Si tu materia NO usa teoremas, comentar las líneas 56-64:
% \newtheorem{teorema}{Teorema}[section]
% \newtheorem{lema}[teorema]{Lema}
% ...
```

---

## 📁 Estructura Recomendada de Carpetas

```
mi-materia/
├── assets/
│   └── ucasal-logo.png
├── tp-1/
│   ├── tp-1.tex          (copia del template)
│   └── tp-1.pdf          (compilado)
├── tp-2/
│   ├── tp-2.tex
│   └── tp-2.pdf
└── template-unificado.tex (este archivo)
```

---

## 🆘 Solución de Problemas

### Error: "File ucasal-logo.png not found"
**Solución:** Cambiar `\logoportada` a `\logoomitido`

### El índice no se genera
**Solución:** Compilar **dos veces** (LaTeX necesita dos pasadas para generar el índice)

### Los acentos no se ven bien
**Solución:** Asegurarse de que el archivo esté guardado en UTF-8

### El código se sale de los márgenes
**Solución:** Ya está configurado `breaklines=true`, pero puedes ajustar el tamaño:
```latex
basicstyle=\ttfamily\footnotesize,  % En lugar de \small
```

---

## 📖 Recursos Adicionales

- **Símbolos matemáticos:** [Detexify](http://detexify.kirelabs.org/classify.html)
- **Tablas LaTeX:** [TablesGenerator](https://www.tablesgenerator.com/)
- **Colores:** [LaTeX Color](https://latexcolor.com/)
- **TikZ/pgfplots:** [pgfplots Gallery](http://pgfplots.sourceforge.net/gallery.html)

---

## 📝 Notas Finales

Este template está diseñado para ser **flexible**. No necesitas usar todos los elementos en cada trabajo:

- **TP de Programación:** Usa solo `ejercicio/resolucion` + código
- **TP de Matemática:** Usa `teorema/definicion/ejemplo` + fórmulas
- **TP Mixto:** Combina ambos según necesites