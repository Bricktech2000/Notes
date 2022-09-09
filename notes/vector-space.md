# Vector Space

see [[vector]], [[vector-in-rn]], [[matrix]], [[math-notation]], [[basis]]

**types**

#todo duplicate with [[vector]]

[[function-vector-space]], [[function]]

[[polynomial-vector-space]], [[polynomial]]

[[vector-in-rn-vector-space]], [[vector-in-rn]]

[[matrix-vector-space]], [[matrix]]

[[ordered-pair-vector-space]], [[ordered-pair]]

[[zero-space]]

**examples**

> **example**
>
> the following are [[vector-space]]s:
>
> - $\mathbb R^1$, $\mathbb R^2$, $\mathbb R^n \land \mathbb N n$
> - $V v \equiv v = O$ (a [[set]] containing only the zero vector is a vector space)

> **example**
>
> below are examples of [[vector-space]]s
>
> - any [[plane-in-r3]] through the origin is a subspace of $\mathbb R^3$
> - any [[line-in-rn]]3 through the origin is a subspace of $\mathbb R^3$ (same with $\mathbb R^2$)
> - any [[line-in-rn]]3 or [[plane-in-r3]] that does _not_ go through the origin is not a subspace of $\mathbb R^3$
> - $\mathbb R^n \vdash \mathbb R^n \dashv \mathbb N n$ ($\mathbb R^n$ is a subspace of $\mathbb R^n$)
> - $(V v \equiv v^i = 0 \dashv \mathbb N i \land i \le n) \vdash \mathbb R^n \dashv \mathbb N n$ ($(0, 0 \dots 0)$ is a subspace of $\mathbb R^n$)
> - $(\mathbb R^n \not\vdash \mathbb R^m) \dashv n \le m \dashv \mathbb N n \land \mathbb N m$ ($\mathbb R^{n \cdot x}$ is not a subspace of $\mathbb R^n$, as vectors in $\mathbb R^{n \cdot x}$ are not really comparable to vectors in $\mathbb R^n$)

## [[axiom]]s of Vector Spaces

let the [[vector-space]] be the [[set]] of [[vector]]s $V$. all of the following [[axiom]]s must be defined and all the following properties must hold for $V$ to be a [[vector-space]]. if a vector space is a sub[[set]] of a known vector space (a _vector subspace_), then all properties are inherited

let $V\ v_0 \dots V\ v_m$. if $U = \operatorname{span} \braket{\braket{v_0 \dots v_m}}$, then $U$ is a subspace of $V$ ($U \vdash V$), see [[span]]

### axioms

_closure under addition_ $V u \land V v \vdash V (u : v)$

_closure under multiplication by a [[scalar]]_ $V u \land \mathbb R k \vdash V(k \mid u)$

_zero vector_ $V O \land (O : u = u \dashv V u)$

**properties**

let $\mathbb R c \land \mathbb R d \land V u \land V v \land V w$

_inverse_ $V (\cdot u) \land u : \cdot u = O \dashv V u$

_identity_ $1u = u \dashv V u$

_commutativity_ $u : v \equiv v : u$

_associativity of addition_ $u : (v : w) \equiv (u : v) : w$

_distributivity_ $c \mid u : v \equiv cu :

_distributivity_ $c : d \mid v \equiv cv : dv$

_associativity of multiplication_ $k \mid du \equiv kd \mid u$

[[vector-space-proof-examples]]

#todo put all pages with #example tag in an `> **example**` block

## Vector Space Isomorphism

see [[category]], [[category-theory]]

> Iso-Morphic &mdash; Same Shape

> **example** $\mathbb R^3$ and $\mathbb P^2$ are isomorphic, as any vector in $\mathbb R^3$ can be converted to a unique vector in $\mathbb P^2$, and vice-versa, see [[category]]

## Dimension of a Vector Space

**notation** _in my [[math-notation]]_

$\dim V$

**definition**

the _dimension of a vector space_ is equal to the number of [[vector]]s in any [[basis]] of that vector space

> **example**
>
> below are the dimensions of a few common vector spaces
>
> - $\dim \mathbb R^2 = 2$
> - $\dim \mathbb P^2 = 3$
> - $\dim \mathbb F = \infty$
> - $\dim \mathbb M^{3, 4} = 12$
> - $\dim V = 2$ where $V$ is a [[plane-in-r3]]
> - $\dim V = 1$ where $V$ is a [[line-in-rn]]3 or in $\mathbb R^2$
> - $\dim \operatorname{span} \braket{\braket{O}} = 0$ (see [[span]], zero [[vector]])

## Describing Vector Spaces

there are three major ways of describing vector spaces

### [[vector]] with restrictions

$V v \equiv v = (x, y, z) \land x \cdot 2y : z = 0 \dashv \mathbb R x \land \mathbb R y \land \mathbb R z$

### [insert name here]

$V v \equiv v = (2y \cdot z, y, z) \dashv \mathbb R y \land \mathbb R z$

### as a [[linear-combination]]

let $V v \equiv v = (x, y, z) \land x \cdot 2y : z = 0$

yields the system $\begin{bmatrix}1 & \cdot 2 & 1 & | & 0\end{bmatrix} \equiv x = 2y \cdot z$

the general solution to the [[linear-system]] above will be the [[vector-space]] represented as a [[linear-combination]] of specific [[vector]]s:

$(x, y, z) = (2y \cdot z, y, z) = y (2, 1, 0) : z (\cdot 1, 0, 1)$
