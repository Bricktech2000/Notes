# Vector in Rn

*Vectors in $\R^n$*

see [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md), [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md), [Vector](Vector%208f57230e24a8497192bb7f33a34e40f8.md) properties

## notation

$(1, 2)$

$\begin{bmatrix}1 & 2\end{bmatrix}$

$\begin{bmatrix}1 \\ 2 \\ 3\end{bmatrix}$

## operations

$(a, b) = (c, d) \equiv a = c \land b = d$ (equality)

$(a, b) \cdot (c, d) \equiv (a \cdot c, b \cdot d)$ (addition)

$0 \equiv (0, 0)$ (the zero vector)

$0^m = 0 \land m = 0 \dots n$, where $n$ is the dimension of the zero vector

$\circ(a, b) \equiv (\circ a, \circ b)$ (negation)

$c(a, b) \equiv (ca, cb) \dashv \R c$ (multiplication by a scalar)

## Magnitude

$|V|$, where

$V$ is the vector to find the magnitude of

$|V| = \sqrt{V \cdot V}$ (derived from the Pythagoras theorem)

**Unit Vector**

where $|V| = 1$

## Orientation

$\frac{V}{|V|} = (cos(\theta), sin(\theta))$, where

$V$ is the vector to find the direction of

$\theta$ is the angle of the vector

note that $\frac{\vec V}{|\vec V|}$ is just notation for the direction of the vector $V$

## Angles Between two Vectors

*no idea why this actually works*

see [Dot Product](Dot%20Product%20c191d041a51341038d2cf7fbaa008502.md), [Cross Product](Cross%20Product%202be01b6689df4f0d826cacb6f2a09c1a.md)

$\cos \theta = \frac{a \cdot b}{|a||b|}$ (use $\cos \theta = \frac{|a \cdot b|}{|a||b|}$ to always get the acute angle solution)

$\sin \theta = \frac{a \times b}{|a||b|}$

### Orthogonal Vectors

notation: $u \perp v$

*a pair of vectors offset by $90\degree$*

$u$ and $v$ are orthogonal if $u \cdot v = 0$ (see [Dot Product](Dot%20Product%20c191d041a51341038d2cf7fbaa008502.md))

### Collinear Vectors

*a pair of parallel vectors*

$u$ and $v$ are colinear if $u = kv$

## Projections

*The scalar projection is equal to the length of the vector projection* — Wikipedia

see [Dot Product](Dot%20Product%20c191d041a51341038d2cf7fbaa008502.md)

$|proj_ba| = |a|\cos\theta$, and

$proj_ba = (|a|\cos\theta) \hat b = (a \cdot \hat b) \hat b =   \frac{a \cdot b}{b \cdot b}b$, where

$proj_ba$ is the *vector projection of $a$ on $b$*

$|proj_ba|$ is the *scalar projection of $a$ on $b$*

$\hat b$ is the unit vector in the direction of $b$, $\frac{b}{|b|}$

### properties

$proj_ba$ is parallel to $b$

$a - proj_ba$ is orthogonal to $b$

## volume of the [Parallelepiped](Parallelepiped%20dfa13f7a10f64238bca3e8dda00922bb.md) defined by 3 vectors in  $\R^3$

*does this seem random? well, it is.*

see [Dot Product](Dot%20Product%20c191d041a51341038d2cf7fbaa008502.md), [Cross Product](Cross%20Product%202be01b6689df4f0d826cacb6f2a09c1a.md)

$V = |w \cdot (u \times v)|$, where

$V$ is the volume calculated

$u$, $v$ and $w$ are the three vectors in $\R^3$