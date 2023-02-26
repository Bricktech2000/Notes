# Vector in Rn

_Vectors in $\mathbb R^n$_

**see** [[math notation]], [[math notation]], [[vector]] properties

**definition** a _vector in $\mathbb R^n$_ is an ordered collection of elements that do not have to be unique

**definition** _formally in my [[math notation]]_ a [[vector]] is a [[set theory]]etical [[function]] that takes a [[natural]] index and returns the element at that index

> **equivalence** _[[list]]s and [[vector in rn]]s_

> **equivalence** _[[vector in rn]] [[vector space#dimension]] and [[list]] length_

**notation** _in my [[math notation]]_

$(1, 2)$

## Vector Space

**see** [[vector]], [[vector space]]

**properties**

_zero [[vector in rn]]_ $O$ such that $O \circ \circ = 0$

_[[vector in rn]] addition_ $(a, b) : (c, d) =\!= (a : c, b : d)$

_multiplication by a [[scalar]]_ $c(a, b) =\!= (ca, cb) > \mathbb R c$

## Magnitude

**see** [[dot product]]

**definition**

$|V| = \lfloor \,: V2 \rfloor$, where

### Unit Vector

**definition**

a _unit vector_ is a [[vector in rn]] $V$ such that $|V| = 1$

a [[vector in rn]] can be _normalized_ (scaled into into a [[vector in rn#unit vector]]) through $(\circ - ||)$

## Angle

_angle between two [[vector in rn]]s_

**definition**

$\cos \theta = \,: ab - |a| |b|$, see [[dot product]] #magic

> **note**: use $\cos \theta =\ |\,: ab| - |a| |b|$ to always get the acute angle solution

**definition**

$\sin \theta = a\ \check\mid\ b - |a| |b|$, see [[cross product]] #magic

### Orthogonal Vectors

_a pair of vectors offset by $\tau\text-4\ \text{rad}$_

**definition** $u$ and $v$ are _orthogonal_ if and only if $\,: uv = 0$, see [[dot product]]

**definition** a [[set]] of [[vector]]s is _orthogonal_ if and only if it does not contain the zero [[vector]] and all [[vector]]s in the [[set]] are orthogonal to all other [[vector]]s

**theorem** any orthogonal [[set]] of [[vector]]s in $\mathbb R^n$ contains at most $n$ [[vector]]s

**theorem** any orthogonal [[set]] of $n$ [[vector]]s in $\mathbb R^n$ is a [[basis#orthogonal basis]] of $\mathbb R^n$

**theorem** a [[set]] of [[vector]]s being orthogonal implies the [[vector]]s are [[linearly independent]], but not conversely

**theorem** suppose $(w_0 \cdots w_m)$ is a [[basis#orthogonal basis]] for a [[vector space#subspace]] $W$ of $\mathbb R^n$. then, $w = w_0 (\,: ww_0\ - \,: w_0w_0) : \cdots w_m (\,: ww_m\ - \,: w_mw_m)$, see [[dot product]]

### Colinear Vectors

_a pair of parallel vectors_

**definition** $u$ and $v$ are _colinear_ if and only if $\,: uv = |u| |v|$, see [[dot product]]

**definition** $u$ and $v$ are _colinear_ if and only if $u = kv$ given a [[scalar]] $k$

**properties**

$u$ and $v$ are colinear if $u$ is a [[linear combination]] of the [[set]] $\braket{\braket{v}}$

## Projection

_The scalar projection is equal to the [[vector in rn#magnitude]] of the [[vector in rn#projection]]_ &mdash; Wikipedia

**see** [[dot product]]

[[vector in rn#projection]]s are [[linear transformation]]s, and therefore can be turned into [[matrix#multiplication]]

**definition** _projection onto another [[vector]]_

$|proj_b\ a| = |a| \cos \theta$, and

$proj_b\ a = |a| \cos \theta \mid \hat b = \,: a \hat b \mid \hat b = \,: ab\ - \,: bb \mid b$ (see [[dot product]]), where

- $proj_b\ a$ is the _vector projection of $a$ on $b$_
- $|proj_b\ a|$ is the _scalar projection of $a$ on $b$_
- $\hat b$ is the [[vector in rn#unit vector]] in the direction of $b$, $b - |b|$

**definition** _projection onto a [[vector space]]_

$proj_W\ v = (\,: vw_0\ - \,: w_0w_0) : \cdots (\,: vw_n\ - \,: w_nw_n)$, where

- $proj_W\ v$ is the projection of $v$ on the [[vector space]] $W$
- $W = \operatorname{span} \braket{\braket{w_0 \cdots w_n}}$ and $(w_0 \cdots w_n)$ is a [[basis#orthogonal basis]] for $W$

**properties**

$proj_b\ a$ is parallel to $b$

$a \cdot proj_b\ a$ is orthogonal to $b$

$W\ (proj_W\ v)$

$v \cdot proj_W\ v$ is orthogonal to every [[vector]] in $W$

the [[vector]] $proj_W\ v$ is the only [[vector]] in $\mathbb R^n$ that satisfies the two properties above

$proj_W\ v$ is the "best approximation" to $v$ by [[vector]]s in $W$
