# Vector in Rn

_Vectors in $\mathbb R^n$_

see [[math-notation]], [[math-notation]], [[vector]] properties

## notation

$(1, 2)$

$\begin{bmatrix}1 & 2\end{bmatrix}$

$\begin{bmatrix}1 \\\  2 \\\  3\end{bmatrix}$

$\dots$

## operations

see [[vector-in-rn-vector-space]], [[vector-space]]

### Zero Vector

$O \equiv (0, 0)$

$O^m = 0 \land m = 0 \dots n$, where $n$ is the dimension of the zero vector

### Vector Addition

$(a, b) : (c, d) \equiv (a : c, b : d)$

### Multiplication by a Scalar

$c(a, b) \equiv (ca, cb) \dashv \mathbb R c$ &mdash; multiplication by a scalar

### Equality

$(a, b) = (c, d) \equiv a = c \land b = d$

### Negation

$\cdot(a, b) \equiv (\cdot a, \cdot b)$

## Magnitude

$|V|$, where

$V$ is the vector to find the magnitude of

$|V| = \lfloor V\ \dot\mid\ V \rfloor$ (derived from the Pythagoras theorem), see [[dot-product]]

**Unit Vector**

where $|V| = 1$

## Orientation

$V - |V| = (\cos \theta, \sin \theta)$, where

$V$ is the vector to find the direction of

$\theta$ is the angle of the vector

note that $V - |V|$ is just notation for the direction of the vector $V$

## Angles Between two Vectors

see [[dot-product]], [[cross-product]], #magic

$\cos \theta = a\ \dot\mid\ b - |a|\ |b|$. use $\cos \theta = |a\ \dot\mid\ b| - |a|\ |b|$ to always get the acute angle solution

$\sin \theta = a \bar\mid b - |a|\ |b|$, see [[cross-product]]

### Orthogonal Vectors

notation: $u \perp v$

_a pair of vectors offset by $90^\cdot$ ._

$u$ and $v$ are orthogonal if and only if $u\ \dot\mid\ v = 0$ (see [[dot-product]]), or $u \perp v \equiv u\ \dot\mid\ v = 0$

a [[set]] of [[vector]]s is orthogonal if and only if it does not contain the zero [[vector]] and all [[vector]]s in the [[set]] are orthogonal to all other [[vector]]s

> **theorem**: an orthogonal [[set]] of [[vector]]s is [[linearly-independent]] (think of this visually)

### theorems

> **theorem**: any orthogonal [[set]] of [[vector]]s in $\mathbb R^n$ contains at most $n$ [[vector]]s

> **theorem**: any orthogonal [[set]] of $n$ [[vector]]s in $\mathbb R^n$ is an orthogonal [[basis]] of $\mathbb R^n$

> **theorem**: orthogonal [[set]] $\vdash$ [[linearly-independent]], but not the inverse

> **theorem**: suppose $w_0 \dots w_m$ is an orthogonal [[basis]] for a subspace $W$ of $\mathbb R^n$. then, $w = w_0 (w \dot\shortmid w_0 - w_0 \dot\shortmid w_0) + \dots w_m (w \dot\shortmid w_m - w_m \dot\shortmid w_m)$, see [[dot-product]]

### Collinear Vectors

_a pair of parallel vectors_

$u$ and $v$ are colinear if $u = kv \land \mathbb R k$

$u$ and $v$ are colinear if $u$ is a [[linear-combination]] of the [[set]] $\lbrace v \rbrace$

## Projections

_The scalar projection is equal to the [[length]] of the vector projection_ &mdash; Wikipedia

see [[dot-product]]

[[vector]] projections are [[linear-transformation]]s. projections can be turned into [[matrix]] multiplication as they are both [[linear-transformation]]s

### definition

$|proj_b\ a| = |a| \cos \theta$ and $proj_b\ a = |a| \cos \theta \mid \hat b = a \dot\shortmid \hat b \mid \hat b = a \dot\shortmid b - b \dot\shortmid b \mid b$ (see [[dot-product]]), where

$proj_b\ a$ is the _vector projection of $a$ on $b$ ._

$|proj_b\ a|$ is the _scalar projection of $a$ on $b$ ._

$\hat b$ is the unit [[vector]] in the direction of $b$, $b - |b|$

$proj_W\ v = v \dot\shortmid w_0 - w_0 \dot\shortmid w_0 : \dots v \dot\shortmid w_n - w_n \dot\shortmid w_n$, where

$proj_W\ v$ is the projection of $v$ on the [[vector-space]] $W$

$W = \operatorname{span} w_0 \dots w_n$ and $w_0 \dots w_n$ form an orthogonal [[basis]] for $W$

### properties

see [[math-notation]]

$proj_b\ a$ is parallel to $b$

$a \cdot proj_b\ a$ is orthogonal to $b$

$W\ (proj_W\ v)$

$v \cdot proj_W\ v$ is orthogonal to every [[vector]] in $W$

the [[vector]] $proj_W\ v$ is the only [[vector]] in $\mathbb R^n$ that satisfies the two properties above

$proj_W\ v$ is the "best approximation" to $v$ by [[vector]]s in $W$

## volume of the [[parallelepiped]] defined by 3 vectors in $\mathbb R^3$

_does this seem random and pointless? well, it is._

see [[dot-product]], [[cross-product]]

$V = |w\ \dot\mid\ u \bar\shortmid v|$ (see [[dot-product]], [[cross-product]]), where

$V$ is the [[volume]] to be calculated

$u$, $v$ and $w$ are the three [[vector]]s in $\mathbb R^3$
