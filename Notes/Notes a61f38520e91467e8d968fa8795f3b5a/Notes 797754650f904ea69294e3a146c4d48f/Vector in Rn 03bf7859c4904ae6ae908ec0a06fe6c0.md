# Vector in Rn

*Vectors in $\R^n$*

see [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md), [Classical Math Notation](../Tags%20b793d46ea133446daa88889450d15033/Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md)

## notation

$(1, 2)$

$\begin{bmatrix}1 & 2\end{bmatrix}$

$\begin{bmatrix}1 \\ 2 \\ 3\end{bmatrix}$

## operations

$(a, b) = (c, d) \equiv a = c \land b = d$ (equality)

$(a, b) \cdot (c, d) \equiv (a \cdot c, b \cdot d)$ (addition)

$0 \equiv (0, 0)$ (the zero vector)

$\circ(a, b) \equiv (\circ a, \circ b)$ (negation)

$c(a, b) \equiv (ca, cb) \dashv \R c$ (multiplication by a scalar)

### properties

let $\R^n (u, v, w) \dashv \Z n$

let $\R (c1, c2)$

$u \cdot 0 = 0$

$u \cdot \circ u = 0$

$(u \cdot v) \cdot w = u \cdot (v \cdot w)$

$u \cdot v = v \cdot u$

$c\ |\ u \cdot v = cu \cdot cv$

$c_1 \cdot c_2\ |\ u = c_1u \cdot c_2u$

$c_1 c_2\ |\ u = c_1\ |\ c_2u$

$1u = u$

## Magnitude

$|V|$, where

$V$ is the vector to find the magnitude of

$|V| = \sqrt{u \cdot u}$

**Unit Vector**

where $|V| = 1$

## Orientation

$\frac{V}{|V|} = (cos(\theta), sin(\theta))$, where

$V$ is the vector to find the direction of

$\theta$ is the angle of the vector

note that $\frac{\vec V}{|\vec V|}$ is just notation for the direction of the vector $V$

## Dot Product

$a \cdot b = \sum_{i = 1}^{n}a_ib_i$

$a \cdot b = |a||b|\cos \theta$, where

$\theta$ is the angle between $a$ and $b$

*If vectors are identified with row matrices, the dot product can also be written as a matrix product* — Wikipedia

$a \cdot b = ab^\intercal$

### examples

$[3, 2, -1] \cdot [4, -6, 3] = 3 \times 4 + 2 \times -6 + -1 \times 3 = -3$

$\begin{bmatrix} 3 & 2 & -1\end{bmatrix} \cdot \begin{bmatrix} 4 & -6 & 3\end{bmatrix} = \begin{bmatrix} 3 & 2 & -1\end{bmatrix} \begin{bmatrix} 4 \\ -6 \\ 3\end{bmatrix} = -3$

## Cross Product

*the cross product is only defined with vectors in $\R^3$*

*results in a vector of length (area of the parallelogram formed by the two vectors) and of orientation (perpendicular to the plane formed by the two vectors)* — 3B1B

> the [Determinant](Determinant%207e4da0265a0b481486e967f785f812fc.md) is all about measuring how areas change during a transformation. after the transformation, the $1 \times 1$ unit square formed by $\vec i$ and $\vec j$ gets turned into the parallelogram formed by the two vectors — 3B1B
> 

$|a \times b| = \det(\begin{bmatrix} a\ |\ b\end{bmatrix})$

$a \times b = \det(\begin{bmatrix}B\ |\  a\ |\ b\end{bmatrix})$, where

$B$ is the basis vector, i.e. $\begin{bmatrix}\hat i \\ \hat j  \\ \dots\end{bmatrix}$

### shortcut for calculating cross product

$\begin{bmatrix}a_1 \\ a_2 \\ a_3\end{bmatrix} \times \begin{bmatrix}b_1 \\ b_2 \\ b_3\end{bmatrix} = \begin{bmatrix}a_2b_3 - b_2a_3 \\ a_3b_1 - b_3a_1 \\ a_1b_2 - b_1a_2\end{bmatrix}$

### **properties**

$a \times b = -b \times a$

$a \times (b + c) = a \times b + a \times c$, and

$(b + c) \times a = b \times a + c \times a$

$k(a \times b) = (ka) \times b = a \times (kb)$, think of this intuitively

## Angles Between two Vectors

*no idea why this actually works*

$\cos \theta = \frac{a \cdot b}{|a||b|}$

$\sin \theta = \frac{a \times b}{|a||b|}$

### Orthogonal Vectors

notation: $u \perp v$

*a pair of vectors offset by $90\degree$*

$u$ and $v$ are orthogonal if $u \cdot v = 0$

**Collinear Vectors**

*a pair of parallel vectors*

$u$ and $v$ are colinear if $u = kv$

## Projections

*The scalar projection is equal to the length of the vector projection* — Wikipedia

$|proj_ba| = |a|\cos\theta$, and

$proj_ba = (|a|\cos\theta) \hat b = (a \cdot \hat b) \hat b =   \frac{a \cdot b}{b \cdot b}b$, where

$proj_ba$ is the *vector projection of $a$ on $b$*

$|proj_ba|$ is the *scalar projection of $a$ on $b$*

$\hat b$ is the unit vector in the direction of $b$, $\frac{b}{|b|}$

## volume of the [Parallelepiped](Parallelepiped%20dfa13f7a10f64238bca3e8dda00922bb.md) defined by 3 vectors in  $\R^3$

*does this seem random? well, it is.*

$V = |w \cdot (u \times v)|$, where

$V$ is the volume calculated

$u$, $v$ and $w$ are the three vectors in $\R^3$