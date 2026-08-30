# Guía teórica — Espacios vectoriales, subespacios, bases y dimensión

Esta guía resume todos los conceptos que necesitás para el TP N°1, en el orden en que aparecen las actividades. Cada sección tiene: la idea intuitiva, la definición formal, el método de resolución paso a paso, y un ejemplo resuelto.

---

## 1. Espacio vectorial (Actividad 1)

### Idea intuitiva
Un espacio vectorial es un conjunto de "objetos" (vectores, matrices, polinomios, funciones, lo que sea) que se pueden **sumar entre sí** y **multiplicar por un número real (escalar)**, y esas dos operaciones se comportan "como uno espera" — igual que los vectores de toda la vida en $\mathbb{R}^2$ o $\mathbb{R}^3$.

### Los 10 axiomas
Sea $V$ un conjunto con una suma $+$ y un producto por escalar $\cdot$. $V$ es espacio vectorial si para todo $u,v,w \in V$ y $\alpha,\beta \in \mathbb{R}$ se cumple:

| # | Axioma | Qué dice |
|---|--------|----------|
| 1 | Cerradura de la suma | $u+v \in V$ |
| 2 | Conmutatividad | $u+v = v+u$ |
| 3 | Asociatividad de la suma | $(u+v)+w = u+(v+w)$ |
| 4 | Neutro aditivo | $\exists\, \theta \in V \;/\; u+\theta = u$ |
| 5 | Inverso aditivo | $\exists\, -u \in V \;/\; u+(-u)=\theta$ |
| 6 | Cerradura del producto | $\alpha u \in V$ |
| 7 | Distributiva (vectores) | $\alpha(u+v) = \alpha u + \alpha v$ |
| 8 | Distributiva (escalares) | $(\alpha+\beta)u = \alpha u + \beta u$ |
| 9 | Asociativa del producto | $(\alpha\beta)u = \alpha(\beta u)$ |
| 10 | Neutro del producto | $1\cdot u = u$ |

**Método:** tomás elementos genéricos del conjunto, aplicás la operación, y verificás que el resultado siga cumpliendo la definición del conjunto y que la igualdad se sostenga.

### Ejemplo resuelto (resumido)
$L=\{(x,y)\in\mathbb{R}^2 : y=mx\}$ con $m$ fijo. Cualquier elemento se escribe $(x_1, mx_1)$. Sumando dos elementos: $(x_1,mx_1)+(x_2,mx_2) = (x_1+x_2,\, m(x_1+x_2))$ — sigue siendo de la forma $(x, mx)$, por lo tanto es cerrado. Repitiendo esto para los 10 axiomas, se concluye que $L$ **es** espacio vectorial.

### Cómo demostrar que NO es espacio vectorial
No hace falta revisar los 10 axiomas: **con encontrar un solo axioma que falle alcanza**. Los más fáciles de romper primero:
1. ¿Contiene al elemento neutro (el "cero" de ese conjunto)?
2. ¿Es cerrado bajo el producto por escalar?
3. ¿Es cerrado bajo la suma?

**Ejemplo:** $V=\{1\}\subset\mathbb{R}$. Tomando $u=v=1$: $u+v=2\notin V$. Ya alcanza para concluir que no es espacio vectorial.

---

## 2. Subespacio vectorial (Actividades 2 y 3)

### Idea intuitiva
Un subespacio es un subconjunto $W$ de un espacio vectorial $V$ ya conocido (como $\mathbb{R}^n$, $\mathbb{R}^{m\times n}$, o $P_n$) que **por sí mismo también es espacio vectorial**, con las mismas operaciones.

### El atajo (teorema del subespacio)
Como $W \subseteq V$ y $V$ ya cumple los 10 axiomas, **no hace falta volver a probar los 10** — alcanza con verificar 3 condiciones:

1. **$W \neq \emptyset$** (en la práctica: contiene al vector nulo $\theta$)
2. **Cerrado bajo la suma:** $u,v\in W \Rightarrow u+v \in W$
3. **Cerrado bajo el producto por escalar:** $u\in W,\, k\in\mathbb{R} \Rightarrow ku \in W$

Si se cumplen las tres, $W$ es subespacio (y por lo tanto espacio vectorial). Este es el método que usamos en toda la Actividad 3.

### Para demostrar que NO es subespacio (Actividad 2)
Igual que antes: **un solo contraejemplo que rompa una condición alcanza.** No hace falta revisar las tres.

**Orden recomendado para buscar la falla:**
1. Vector nulo — es la más rápida de chequear.
2. Producto por escalar — probar con $k$ negativo suele romperlo.
3. Suma — a veces es la única que falla.

### Ejemplos de conjuntos que NO son subespacios (y por qué)

| Conjunto | Qué falla | Contraejemplo |
|---|---|---|
| $A=\{(x,y): \lvert y\rvert=\lvert x\rvert\}$ (unión de 2 rectas) | Suma | $(1,1)+(1,-1)=(2,0) \notin A$ |
| $C=\{A\in\mathbb{R}^{2\times2} : \det(A)=0\}$ | Suma | $\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, con $\det=1\neq0$ |
| $D=\{(x,y): y=x^2\}$ (parábola) | Suma | $(1,1)+(1,1)=(2,2)$, pero $2\neq 2^2$ |
| $E=\{(x,y,z): x+y+z=1\}$ (plano que no pasa por el origen) | Vector nulo | $0+0+0=0\neq1$ |

**Regla general importante:** cualquier condición que sea una ecuación **lineal homogénea** (igualada a 0, sin términos independientes, sin productos entre variables) define un subespacio. Si la ecuación:
- tiene un término independiente distinto de 0 (como $x+y+z=1$), o
- involucra potencias o productos de las variables (como $y=x^2$, o $\det(A)=0$), o
- involucra valor absoluto (como $|y|=|x|$),

**entonces casi seguro NO es subespacio.**

---

## 3. Combinación lineal (Actividades 4, 5 y 6)

### Idea intuitiva
$W$ es combinación lineal de $U$ y $V$ si podés "armar" $W$ mezclando $U$ y $V$ con algunos escalares: estirándolos, achicándolos o invirtiéndolos, y sumándolos.

### Definición
$W$ es combinación lineal de $v_1, v_2, \dots, v_n$ si existen escalares $\alpha_1,\dots,\alpha_n \in \mathbb{R}$ tales que:
$$W = \alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n$$

### Método de resolución
1. Planteás la igualdad $\alpha U + \beta V = W$ (con incógnitas $\alpha,\beta$).
2. Igualás componente a componente (o coeficiente a coeficiente, si son polinomios/matrices) y armás un **sistema de ecuaciones lineales**.
3. Resolvés el sistema:
   - Si tiene **solución** (aunque sea con infinitas soluciones) → $W$ **sí** es combinación lineal.
   - Si el sistema es **incompatible** (sin solución) → $W$ **no** es combinación lineal.

### Ejemplo resuelto
$U=(1,2,-2)$, $V=(0,1,1)$, $W=(0,0,0)$.

Planteamos $\alpha U + \beta V = W$:
$$\alpha(1,2,-2)+\beta(0,1,1)=(0,0,0) \;\Rightarrow\; (\alpha,\; 2\alpha+\beta,\; -2\alpha+\beta)=(0,0,0)$$

Sistema:
$$\alpha=0, \qquad 2\alpha+\beta=0, \qquad -2\alpha+\beta=0$$

De la primera: $\alpha=0$. Sustituyendo en la segunda: $\beta=0$. Verificando en la tercera: se cumple.

**Conclusión:** $W$ sí es combinación lineal ($W=0\cdot U + 0\cdot V$, la combinación trivial — esto siempre pasa con el vector nulo, para cualquier $U,V$).

### Variante con parámetro (como la Actividad 6)
Cuando te piden "¿para qué valores de $k$...?", el procedimiento es igual, pero uno de los términos del sistema queda en función de $k$. Resolvés el sistema en términos de $k$ y despejás qué valor(es) de $k$ hacen que el sistema tenga solución.

---

## 4. Subespacio generado / conjunto generador (Actividades 5b y 10)

### Idea intuitiva
El **conjunto de todas las combinaciones lineales posibles** de un grupo de vectores forma, en sí mismo, un subespacio. A ese subespacio se lo llama "subespacio generado" por esos vectores, y se anota $\operatorname{gen}\{v_1,\dots,v_n\}$ o $\langle v_1,\dots,v_n\rangle$.

### Método para encontrar el subespacio generado por $\{u,v\}$
1. Planteás un vector genérico como combinación lineal: $(x,y,z) = \alpha u + \beta v$.
2. Igualás componente a componente y obtenés un sistema (con $\alpha,\beta$ como incógnitas y $x,y,z$ como parámetros).
3. Resolvés el sistema por sustitución o eliminación, buscando qué condición deben cumplir $x,y,z$ para que el sistema tenga solución (esto suele hacerse con eliminación gaussiana, dejando una fila en 0 = algo).
4. Esa condición final es la **ecuación del subespacio generado**.

### Ejemplo resuelto
$u=(1,3,-2)$, $v=(0,1,-2)$. Buscamos $\operatorname{gen}\{u,v\} \subset \mathbb{R}^3$.

Planteamos $(x,y,z)=\alpha(1,3,-2)+\beta(0,1,-2)$:
$$x=\alpha, \qquad y=3\alpha+\beta, \qquad z=-2\alpha-2\beta$$

De la primera: $\alpha=x$. Sustituyendo en la segunda: $\beta=y-3x$. Sustituyendo ambas en la tercera:
$$z = -2x-2(y-3x) = -2x-2y+6x = 4x-2y$$

**Conclusión:** $\operatorname{gen}\{u,v\} = \{(x,y,z)\in\mathbb{R}^3 : 4x-2y-z=0\}$ (un plano que pasa por el origen).

### Relación con "¿$w$ es combinación lineal de $u,v$?"
Una vez que tenés la ecuación del subespacio generado, para saber si un vector $w$ pertenece a él, **simplemente reemplazás sus coordenadas en la ecuación** y verificás si se cumple. Es un atajo más rápido que resolver el sistema desde cero cada vez.

---

## 5. Dependencia e independencia lineal (Actividades 7, 8 y 9)

### Idea intuitiva
- **Independientes (LI):** ningún vector del conjunto "sobra" — ninguno se puede escribir en términos de los demás. Cada uno aporta una dirección genuinamente nueva.
- **Dependientes (LD):** al menos un vector "sobra" — se puede escribir como combinación lineal de los otros.

### Definición formal
$\{v_1,\dots,v_n\}$ es:
- **LI** si $\alpha_1 v_1+\cdots+\alpha_n v_n = \theta \;\Rightarrow\; \alpha_1=\cdots=\alpha_n=0$ (única solución: la trivial).
- **LD** si existe alguna combinación con **no todos** los $\alpha_i=0$ que da $\theta$.

### Método general de resolución
1. Planteás $\alpha_1 v_1 + \alpha_2 v_2 + \cdots + \alpha_n v_n = \theta$.
2. Igualás componente a componente (o coeficiente a coeficiente) y armás un sistema homogéneo.
3. Resolvés el sistema:
   - **Solución única (todos los $\alpha_i=0$)** → LI.
   - **Infinitas soluciones (algún $\alpha_i$ queda libre)** → LD.

**Atajo con determinante (cuando hay tantos vectores como dimensiones, ej. 3 vectores en $\mathbb{R}^3$):** armás una matriz con los vectores como filas (o columnas) y calculás el determinante.
- $\det \neq 0$ → LI.
- $\det = 0$ → LD.

### Atajos rápidos
- **2 vectores:** son LD si y solo si uno es múltiplo escalar del otro.
- **1 vector:** es LI si y solo si es distinto del vector nulo.
- Si el vector nulo **está incluido** en el conjunto → automáticamente LD.
- Si hay **más vectores que la dimensión del espacio** (ej. 4 vectores en $\mathbb{R}^3$) → automáticamente LD.

### Ejemplo resuelto
$\{(1,3,5),(2,1,-1),(4,7,9)\}\subset\mathbb{R}^3$.

Armamos la matriz y calculamos el determinante:
$$\begin{vmatrix} 1 & 3 & 5 \\ 2 & 1 & -1 \\ 4 & 7 & 9 \end{vmatrix}$$

Si al calcularlo da $0$, son LD (de hecho en este caso vale la pena notar que $(4,7,9) = 2(1,3,5) - (2,1,-1) \cdot ... $ — conviene siempre chequear primero si algún vector es combinación de los otros a simple vista, antes de calcular el determinante).

### Actividad 8 (con parámetro $k$)
Se resuelve igual, pero el sistema/determinante queda en función de $k$. Buscás los valores de $k$ que hacen que el determinante sea 0 (LD) o distinto de 0 (LI).

### Actividad 9 (propiedad teórica)
Si $\{U,V,W\}$ es LI, y formás nuevos vectores como combinaciones lineales de ellos (ej. $\{U,\, U+2V,\, U+V-3W\}$), para saber si el nuevo conjunto sigue siendo LI, planteás $\alpha_1 U + \alpha_2(U+2V)+\alpha_3(U+V-3W)=\theta$, agrupás por $U,V,W$, y como $\{U,V,W\}$ es LI, cada coeficiente que multiplica a $U$, $V$ y $W$ debe ser 0 por separado. Esto te da un sistema en $\alpha_1,\alpha_2,\alpha_3$ que resolvés para concluir si el nuevo conjunto es LI o LD.

---

## 6. Base y dimensión (Actividades 3, 11 y 12)

### Idea intuitiva
Una **base** es un conjunto de vectores que:
1. **Genera** todo el espacio/subespacio (con combinaciones lineales de ellos podés construir cualquier elemento), y
2. Es **linealmente independiente** (no tiene vectores redundantes).

Es la forma "más eficiente" de describir un espacio: el número mínimo de vectores necesarios para generarlo todo, sin desperdiciar ninguno.

La **dimensión** es simplemente la **cantidad de vectores** que tiene una base de ese espacio (todas las bases de un mismo espacio tienen la misma cantidad de elementos).

### Método para encontrar base y dimensión de un subespacio dado por una ecuación
1. Despejás una variable en función de las otras (usando la ecuación que define al subespacio).
2. Reescribís el vector genérico separando según los parámetros libres.
3. Cada "parámetro libre" te da un vector generador.
4. Verificás que esos vectores sean LI (para conjuntos chicos, alcanza con ver que ninguno es múltiplo del otro).
5. **Base** = ese conjunto de vectores. **Dimensión** = cantidad de vectores = cantidad de parámetros libres.

### Ejemplo resuelto
$A=\{(x,y,z)\in\mathbb{R}^3 : 2x-y+z=0\}$.

Despejamos $y$: $y=2x+z$. Entonces todo vector es $(x,\,2x+z,\,z)$, con $x,z$ libres:
$$(x,\,2x+z,\,z) = x(1,2,0)+z(0,1,1)$$

Los vectores $(1,2,0)$ y $(0,1,1)$ generan $A$ y son LI (ninguno es múltiplo del otro).

**Base de $A=\{(1,2,0),(0,1,1)\}$, $\dim(A)=2$.**

### Cómo verificar si un conjunto dado ES base de un subespacio (Actividad 11)
Hay que chequear **dos cosas**:
1. **¿Los vectores pertenecen al subespacio?** (reemplazás cada uno en la ecuación que define al subespacio).
2. **¿Son linealmente independientes?** (con el método de la sección 5).
3. Como extra, conviene verificar que la **cantidad de vectores coincida con la dimensión** del subespacio — si no coincide, no puede ser base (podría generar solo una parte, o ser un conjunto redundante).

Si se cumplen 1 y 2 (y la cantidad correcta), **sí es base**.

---

## 7. Coordenadas en una base (Actividad 13)

### Idea intuitiva
Un mismo vector se puede "describir" de formas distintas según qué base uses como referencia — como describir una ubicación en distintos sistemas de coordenadas. Las **coordenadas de $v$ en la base $\beta$** son los escalares que necesitás para reconstruir $v$ a partir de los vectores de $\beta$.

### Método: de la base canónica a otra base $\beta$
Si $\beta=\{b_1,b_2\}$ y querés las coordenadas de $v$ en $\beta$:
1. Planteás $v = \alpha_1 b_1 + \alpha_2 b_2$.
2. Resolvés el sistema para $\alpha_1,\alpha_2$.
3. Las coordenadas de $v$ en la base $\beta$ son $[v]_\beta = (\alpha_1,\alpha_2)$.

### Método inverso: de coordenadas en $\beta$ a la base canónica
Si te dan que $[v]_\beta=(\alpha_1,\alpha_2)$, simplemente calculás:
$$v = \alpha_1 b_1 + \alpha_2 b_2$$
y ese resultado son las coordenadas de $v$ en la base canónica.

### Ejemplo resuelto
$v=(3,2)$ en la base canónica, $\beta=\{(1,2),(1,-2)\}$.

Planteamos $(3,2)=\alpha(1,2)+\beta(1,-2)$:
$$3=\alpha+\beta, \qquad 2=2\alpha-2\beta$$

De la segunda: $1=\alpha-\beta$. Sumando con la primera ($3=\alpha+\beta$): $2\alpha=4 \Rightarrow \alpha=2$, y $\beta=1$.

**Coordenadas de $v$ en la base $\beta$: $(2,1)$.**

Para la parte inversa (coordenadas $(1,1)$ en $\beta$ → base canónica):
$$v = 1\cdot(1,2)+1\cdot(1,-2) = (2,0)$$

---

## Resumen de "qué método usar según la consigna"

| Si te piden... | Usá el método de la sección... |
|---|---|
| "¿Es espacio vectorial?" | 1 (10 axiomas), o el atajo de subespacio si ya es subconjunto de algo conocido |
| "Demostrar que NO es subespacio" | 2 (un solo contraejemplo alcanza) |
| "Demostrar que SÍ es subespacio + base + dimensión" | 2 (atajo, 3 condiciones) + 6 |
| "¿$W$ es combinación lineal de $U,V$?" | 3 (sistema de ecuaciones) |
| "Subespacio generado por..." | 4 |
| "¿Son LI o LD?" | 5 |
| "Encontrar base y dimensión" | 6 |
| "¿Este conjunto es base de...?" | 6 (verificar pertenencia + independencia) |
| "Coordenadas en una base" | 7 |

---

## Consejo general para todo el TP

Fijate que casi todos los ejercicios (excepto el 1) terminan reduciéndose a lo mismo: **plantear una combinación lineal igualada a algo, armar un sistema de ecuaciones, y resolverlo.** La diferencia está en qué preguntás con ese sistema:

- ¿Tiene solución? → combinación lineal (sección 3).
- ¿Tiene solución única (la trivial)? → independencia lineal (sección 5).
- ¿Qué condición sobre $x,y,z$ hace que tenga solución? → subespacio generado (sección 4).
- ¿Cuáles son los valores de las incógnitas? → coordenadas en una base (sección 7).

Dominar bien cómo plantear y resolver esos sistemas te resuelve la mayoría del trabajo práctico.
