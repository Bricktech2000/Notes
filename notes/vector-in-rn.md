# Vector in Rn

_Vectors in $\mathbb{R}^n$_

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

$c(a, b) \equiv (ca, cb) \dashv \mathbb{R} c$ (multiplication by a scalar)

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

_a pair of vectors offset by $90^\circ$_

$u$ and $v$ are orthogonal if and only if $u \cdot v = 0$ (see [[dot-product]]), or $u \perp v \equiv u \cdot v = 0$

a set of [[vector]]s is orthogonal if and only if it does not contain the zero [[vector]] and all [[vector]]s in the set are orthogonal to all other [[vector]]s

> **theorem**: an orthogonal set of [[vector]]s is [[linearly-independent]] (think of this visually)

### Theorems

any orthogonal set of [[vector]]s in $\mathbb{R}^n$ contains at most $n$ [[vector]]s

any orthogonal set of $n$ [[vector]]s in $\mathbb{R}^n$ is an orthogonal [[basis]] of $\mathbb{R}^n$

orthogonal set $\vdash$ [[linearly-independent]], but not the inverse

> **theorem**: suppose $w_0 \dots w_m$ is an orthogonal [[basis]] for a subspace $W$ of $\mathbb{R}^n$. then, $w = w_0\frac{w \cdot w_0}{w_0 \cdot w_0} + \dots w_m\frac{w \cdot w_m}{w_m \cdot w_m}$ (see [[dot-product]])

### Collinear Vectors

_a pair of parallel vectors_

$u$ and $v$ are colinear if $u = kv$. $u$ is a [[linear-combination]] of the set $\{v\}$

## Projections

_The scalar projection is equal to the length of the vector projection_ &mdash; Wikipedia

see [[dot-product]]

$|proj_ba| = |a|\cos\theta$, and

$proj_ba = (|a|\cos\theta) \hat b = (a \cdot \hat b) \hat b =   \frac{a \cdot b}{b \cdot b}b$, where

$proj_ba$ is the _vector projection of $a$ on $b$_

$|proj_ba|$ is the _scalar projection of $a$ on $b$_

$\hat b$ is the unit vector in the direction of $b$, $\frac{b}{|b|}$

> **theorem**: suppose $w_0 \dots w_m$ is an orthogonal [[basis]] for a subspace $W$ of $\mathbb{R}^n$. then for any $\mathbb{R}^n v$, $proj_Wv = w_0\frac{v \cdot w_0}{w_0 \cdot w_0} + \dots w_m\frac{v \cdot w_m}{w_m \cdot w_m}$ (see [[dot-product]])

### properties

see [[math-notation]]

$proj_ba$ is parallel to $b$

$a \circ proj_ba$ is orthogonal to $b$

$W (proj_Wv)$

$v \circ proj_Wv$ is orthogonal to every [[vector]] in $W$

the [[vector]] $proj_Wv$ is the only [[vector]] in $\mathbb{R}^n$ that satisfies the two properties above

$proj_Wv$ is the "best approximation" to $v$ by [[vector]]s in $W$

## volume of the [[parallelepiped]] defined by 3 vectors in $\mathbb{R}^3$

_does this seem random? well, it is._

see [[dot-product]], [[cross-product]]

$V = |w \cdot (u \times v)|$, where

$V$ is the volume calculated

$u$, $v$ and $w$ are the three vectors in $\mathbb{R}^3$

# todos

replace `\R \N \Z` with `\mathbb{R} \mathbb{N} \mathbb{Z}`

replace `\degree` with `^\circ`

page breaks:

<div class="page"/>

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>
