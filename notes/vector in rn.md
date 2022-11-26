# Vector in Rn

_Vectors in $\mathbb R^n$_

**see** [[math notation]], [[math notation]], [[vector]] properties

**definition** a _vector in $\mathbb R^n$_ is an ordered collection of elements that do not have to be unique

**definition** _formally in my [[math notation]]_ a [[vector]] in $\mathbb R^n$ is a [[set theory]]etical [[function]] with [[function#domain]] at least $x \rightarrow \mathbb N x \land 0 \le x < n$ that takes an index and returns the element at that index

> **equivalence** _[[list]]s and [[vector in rn]]s_

**notation** _in my [[math notation]]_

$(1, 2)$

**properties**

_equality_ $(a, b) = (c, d) \equiv a = c \land b = d$

_negation_ $\cdot(a, b) \equiv (\cdot a, \cdot b)$

## Vector Space

**see** [[vector]], [[vector space]]

**properties**

_zero [[vector in rn]]_ $O\ \dot=\ 0 \equiv O^m = 0$

_[[vector in rn]] addition_ $(a, b) : (c, d) \equiv (a : c, b : d)$

_multiplication by a [[scalar]]_ $c(a, b) \equiv (ca, cb) \dashv \mathbb R c$

## Magnitude

**definition**

$|V|$, where

- $V$ is the [[vector in rn]] to find the magnitude of
- $|V| = \lfloor :\! V2 \rfloor$ (derived from the Pythagoras theorem), see [[dot product]]

### Unit Vector

**definition**

$|V| = 1$, where

- $V$ is a _unit vector_

## Orientation

**definition**

$V - |V| = (\cos \theta, \sin \theta)$, where

- $V$ is the vector to find the direction of
- $\theta$ is the angle of the vector

## Angle

_angle between two [[vector in rn]]s_

**see** [[dot product]], [[cross product]], #magic

**definition**

$\cos \theta =\ :\! ab - |a|\ |b|$

> **note**: use $\cos \theta =\ |:\! ab| - |a|\ |b|$ to always get the acute angle solution

**definition**

$\sin \theta = a\ \check\mid\ b - |a|\ |b|$, see [[cross product]]

### Orthogonal Vectors

_a pair of vectors offset by $90^\circ$_

**notation**

$u \perp v$

**definition** $u$ and $v$ are _orthogonal_ if and only if $:\! uv = 0$ (see [[dot product]]), or $u \perp v \equiv\ :\! uv = 0$

**definition** a [[set]] of [[vector]]s is _orthogonal_ if and only if it does not contain the zero [[vector]] and all [[vector]]s in the [[set]] are orthogonal to all other [[vector]]s

**theorem** an orthogonal [[set]] of [[vector]]s is [[linearly independent]] (think of this visually)

**theorem** any orthogonal [[set]] of [[vector]]s in $\mathbb R^n$ contains at most $n$ [[vector]]s

**theorem** any orthogonal [[set]] of $n$ [[vector]]s in $\mathbb R^n$ is a [[basis#orthogonal basis]] of $\mathbb R^n$

**theorem** orthogonal [[set]] $\vdash$ [[linearly independent]], but not the inverse

**theorem** suppose $w_0 \cdots w_m$ is a [[basis#orthogonal basis]] for a [[vector space#subspace]] $W$ of $\mathbb R^n$. then, $w = w_0 (:\! ww_0 - :\! w_0w_0) : \cdots w_m (:\! ww_m - :\! w_mw_m)$, see [[dot product]]

### Colinear Vectors

_a pair of parallel vectors_

**definition**

$u$ and $v$ are colinear if $u = kv \land \mathbb R k$

**properties**

$u$ and $v$ are colinear if $u$ is a [[linear combination]] of the [[set]] $\braket{\braket{v}}$

## Projection

_The scalar projection is equal to the [[vector in rn#magnitude]] of the [[vector in rn#projection]]_ &mdash; Wikipedia

**see** [[dot product]]

[[vector in rn#projection]]s are [[linear transformation]]s, and therefore can be turned into [[matrix#multiplication]]

**definition** _projection onto another [[vector]]_

$|proj_b\ a| = |a| \cos \theta$, and

$proj_b\ a = |a| \cos \theta \mid \hat b =\ :\! a \hat b \mid \hat b =\ :\! ab - :\! bb \mid b$ (see [[dot product]]), where

- $proj_b\ a$ is the _vector projection of $a$ on $b$ ._
- $|proj_b\ a|$ is the _scalar projection of $a$ on $b$ ._
- $\hat b$ is the [[vector in rn#unit vector]] in the direction of $b$, $b - |b|$

**definition** _projection onto a [[vector space]]_

$proj_W\ v = (:\! vw_0 - :\! w_0w_0) : \cdots (:\! vw_n - :\! w_nw_n)$, where

- $proj_W\ v$ is the projection of $v$ on the [[vector space]] $W$
- $W = \operatorname{span} \braket{\braket{w_0 \cdots w_n}}$ and $(w_0 \cdots w_n)$ is a [[basis#orthogonal basis]] for $W$

**properties**

$proj_b\ a$ is parallel to $b$

$a \cdot proj_b\ a$ is orthogonal to $b$

$W\ (proj_W\ v)$

$v \cdot proj_W\ v$ is orthogonal to every [[vector]] in $W$

the [[vector]] $proj_W\ v$ is the only [[vector]] in $\mathbb R^n$ that satisfies the two properties above

$proj_W\ v$ is the "best approximation" to $v$ by [[vector]]s in $W$
