# Vector in Rn

_Vectors in $\R^n$_

see [[math-notation]], [[classical-math-notation]], [[vector]] properties

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

_no idea why this actually works_

see [[dot-product]], [[cross-product]]

$\cos \theta = \frac{a \cdot b}{|a||b|}$ (use $\cos \theta = \frac{|a \cdot b|}{|a||b|}$ to always get the acute angle solution)

$\sin \theta = \frac{a \times b}{|a||b|}$

### Orthogonal Vectors

notation: $u \perp v$

_a pair of vectors offset by $90\degree$_

$u$ and $v$ are orthogonal if $u \cdot v = 0$ (see [[dot-product]])

### Collinear Vectors

_a pair of parallel vectors_

$u$ and $v$ are colinear if $u = kv$

## Projections

_The scalar projection is equal to the length of the vector projection_ — Wikipedia

see [[dot-product]]

$|proj_ba| = |a|\cos\theta$, and

$proj_ba = (|a|\cos\theta) \hat b = (a \cdot \hat b) \hat b =   \frac{a \cdot b}{b \cdot b}b$, where

$proj_ba$ is the _vector projection of $a$ on $b$_

$|proj_ba|$ is the _scalar projection of $a$ on $b$_

$\hat b$ is the unit vector in the direction of $b$, $\frac{b}{|b|}$

### properties

$proj_ba$ is parallel to $b$

$a - proj_ba$ is orthogonal to $b$

## volume of the [[parallelepiped]] defined by 3 vectors in $\R^3$

_does this seem random? well, it is._

see [[dot-product]], [[cross-product]]

$V = |w \cdot (u \times v)|$, where

$V$ is the volume calculated

$u$, $v$ and $w$ are the three vectors in $\R^3$
