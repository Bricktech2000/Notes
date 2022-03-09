# Vector Space

see [[vector]], [[vector-in-rn]], [[matrix]], [[math-notation]], [[basis]]

## Types of Vector Spaces

[[function-vector-space]]

[[polynomial-vector-space]]

[[vector-in-rn-vector-space]]

[[zero-space]]

### examples

$\R^1$, $\R^2$, $\R^n \land \N n$

$V v \equiv v = O$ (a set containing only the zero vector is a vector space)

## Isomorphic Vector Spaces

> Iso-Morphic &mdash; Same Shape

### examples

$\R^3$ and $\mathbb{P}^2$ are isomorphic, as any vector in $\R^3$ can be converted in a unique vector in $\mathbb{P}^2$, and vice-versa

## Dimension of a Vector Space

### notation

$\dim V$ in my [[math-notation]]

$\dim(V)$ in [[classical-math-notation]]

### definition

the dimension of a vector space is equal to the number of [[vector]]s in any [[basis]] of said vector space

### examples

$\dim \R^2 = 2$

$\dim \mathbb{P}^2 = 3$

$\dim \mathbb{F} = \infty$

$\dim \mathbb{M}^{3, 4} = 12$

$\dim V = 2$ where $V$ is a [[plane-in-r3]]

$\dim V = 1$ where $V$ is a [[line-in-r3]] or in $\R^2$

$\dim span\{0\} = 0$ ([[think]], see [[span]])

## Describing Vector Spaces

_there are three major ways of describing vector spaces_

### [[vector]] with restrictions

$V v \equiv v = (x, y, z) \land x \circ 2y \cdot z = 0 \dashv \R x \land \R y \land \R z$

### [insert name here]

$V v \equiv v = (2y \circ z, y, z) \dashv \R y \land \R z$

### as a [[linear-combination]]

**example**

let $V v \equiv v = (x, y, z) \land x \circ 2y \cdot z = 0$

yields the system $\begin{bmatrix}1 & \circ 2 & 1 & | & 0\end{bmatrix} \equiv x = 2y \circ z$

the general solution to the [[linear-system]] above will be the [[vector-space]] represented as a [[linear-combination]] of specific [[vector]]s:

$(x, y, z) = (2y \circ z, y, z) = y (2, 1, 0) \cdot z (\circ 1, 0, 1)$

## [[axiom]]s of Vector Spaces

let the vector space be the set of [[vector]]s $V$. all of the following [[axiom]]s must be defined and all the following properties must hold for $V$ to be a [[vector-space]]. if a vector space is a subset of a known vector space (a **vector subspace**), then all properties are inherited. moreover,

let $V(v_1 \dots v_m)$. if $U = Span\{v_1 \dots v_m\}$, then $U$ is a subspace of $V$ ($U \vdash V$), see [[span]]

_closed under addition_

$V u \land V v \vdash V (u \cdot v)$

_closed under multiplication_

$V u \land \R k \vdash V(k\ |\ u)$

_zero vector_

$V O \land (O \cdot u = u \dashv V u)$

### properties

_negative vector_

$V (\circ u) \land u \cdot \circ u = O \dashv V u$

_identity_

$1u = u \dashv V u$

$\R k \land \R l\land V u \land V v \land V w$

_commutativity_

$u \cdot v \equiv v \cdot u$

_associativity_

$u \cdot (v \cdot w) \equiv (u \cdot v) \cdot w$

_distributivity_

$c\ |\ u \cdot v \equiv cu \cdot cv$

_multiplicative associativity_

$k\ |\ du \equiv kd\ |\ u$

---

## [[proof]]s

### example

$u = (x, 2x) \land v = (y, y2) \land \R k$

prove $V v \equiv v = (x, 2x) \land \R x$ is a [[vector-space]]

_closed under addition_

$u \cdot v = (x \cdot y, 2\ |\ x \cdot y)$

therefore, $V (u \cdot v)$

_closed under multiplication_

$ku = k(x, 2x) = (kx, 2kx)$

therefore, $V (ku)$

_zero vector_

$x = 0 \land y = 0 \vdash V (0, 0)$

_properties_

$V \vdash \R^2$

therefore, all properties are inherited from $\R^2$

### counterexample

$u = (x, x \cdot 2) \land v = (y, y \cdot 2)$

prove $V v \equiv v = (x, x \cdot 2) \land \R x$ is a [[vector-space]]

_closed under addition_

$u \cdot v = (x \cdot y, x \cdot y \cdot 4) \vdash \lnot V (u \cdot v)$

therefore, $V$ is not a [[vector-space]] as at least one [[axiom]] has been proved $\bot$

### example

$u = x_1(1, 2, 3) \cdot y_1(0, \circ 1, 4)\ \land\ v = x_2(1, 2, 3) \cdot y_2(0, \circ 1, 4)\ \land\ \R k$

prove $V v \equiv v = x(1, 2, 3) \cdot y(0, \circ 1, 4) \land \R x \land \R y$ (see [[linear-combination]])

_closed under addition_

$u \cdot v = (x_1 \cdot x_2)(1, 2, 3) \cdot (y_1 \cdot y_2)(0, \circ 1, 4)$

therefore, $V (u \cdot v)$

_closed under multiplication_

$ku = cx_1(1, 2, 3) \cdot cy_1(0, \circ 1, 4)$

_zero vector_

$x = 0 \land y = 0 \vdash V (0, 0, 0)$

_properties_

$V \vdash \R^3$

therefore, all properties are inherited from $\R^3$

### counterexample

$T u \land T v \equiv u(1, 2, 3) = 0 \land v(1, 2, 3) = 0$

$\R k$

prove $T u \equiv \R^3 u \land u(1, 2, 3) = 0$ (see [[dot-product]]) is a [[vector-space]]

> all vectors orthogonal to $(1, 2, 3)$ (see [[vector-in-rn]]), meaning that this [[vector-space]] is a [[plane-in-r3]]

_zero vector_

$O(1, 2, 3) = (0, 0, 0) \cdot (1, 2, 3) = 0$

therefore, $T O$

_closed under addition_

$(u \cdot v)(1, 2, 3) = u(1, 2, 3) \cdot v(1, 2, 3) = 0 \cdot 0 = 0$

therefore, $T (u \cdot v)$

_closed under multiplication_

$(ku)(1, 2, 3) = k(u(1, 2, 3)) = c'0 = 0$

therefore, $T (ku)$

_properties_

$T \vdash \R^3$

therefore, all properties are inherited from $\R^3$

### example with [[matrix]]es

$M m \equiv m = \mathbb{M}^{2, 2} m \land m^{0, 0} \cdot m^{1, 1} = m^{1, 0} \cdot m^{0, 1}$

_zero vector_

$m = \begin{bmatrix}0 & 0 \\ 0 & 0\end{bmatrix} \vdash m^{0, 0} \cdot m^{1, 1} = m^{1, 0} \cdot m^{0, 1}$

therefore, $M O$

_closed under addition_

$M m_1 \land M m_2$

$m_1^{0, 0} \cdot m_1^{1, 1} = m_1^{1, 0} \cdot m_1^{0, 1}$

$m_2^{0, 0} \cdot m_2^{1, 1} = m_2^{1, 0} \cdot m_2^{0, 1}$

$(m_1^{0, 0} \cdot m_2^{0, 0}) \cdot (m_1^{1, 1} \cdot m_2^{1, 1}) = (m_1^{1, 0} \cdot m_2^{1, 0}) \cdot (m_1^{0, 1} \cdot m_2^{0, 1})$

therefore, $M (m_1 \cdot m_2)$

_closed under multiplication_

$km = k \begin{bmatrix}m^{0, 0} & m^{0, 1} \\ m^{1, 0} & m^{1, 1}\end{bmatrix} = \begin{bmatrix}km^{0, 0} & km^{0, 1} \\ km^{1, 0} & km^{1, 1}\end{bmatrix}$

$km^{0, 0} \cdot km^{1, 1} = km^{1, 0} \cdot km^{0, 1}$

$k\ |\ m^{0, 0} \cdot m^{1, 1} = k\ |\ m^{1, 0} \cdot km^{0, 1}$

$k\ |\ m^{0, 0} \cdot m^{1, 1} = k\ |\ m^{0, 0} \cdot km^{1, 1}$

therefore, $M(km)$

### additional examples

- any [[plane-in-r3]] through the origin is a subspace of $\R^3$
- any [[line-in-r3]] through the origin is a subspace of $\R^3$ (same with $\R^2$)
- any [[line-in-r3]] or [[plane-in-r3]] that does _not_ go through the origin is not a subspace of $\R^3$
- $\R^n \vdash \R^n \dashv \N n$ ($\R^n$ is a subspace of $\R^n$)
- $(V v \equiv v^i = 0 \dashv \N i \land i \le n) \vdash \R^n \dashv \N n$ ($(0, 0 \dots 0)$ is a subspace of $\R^n$)
- $\lnot (\R^n \vdash \R^m) \land n < m \dashv \R n \land \R m$ ($\R^{n \circ x}$ is not a subspace of $\R^n$, as vectors in $\R^{n \circ x}$ are not really comparable to vectors in $\R^n$)
