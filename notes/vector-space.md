# Vector Space

see [[vector]], [[vector-in-rn]], [[matrix]], [[math-notation]], [[basis]]

## types

[[function-vector-space]], [[function]]

[[polynomial-vector-space]], [[polynomial]]

[[vector-in-rn-vector-space]], [[vector-in-rn]]

[[matrix-vector-space]], [[matrix]]

[[zero-space]]

### examples

$\mathbb R^1$, $\mathbb R^2$, $\mathbb R^n \land \mathbb N n$

$V v \equiv v = O$ (a [[set]] containing only the zero vector is a vector space)

## Isomorphic Vector Spaces

> Iso-Morphic &mdash; Same Shape

### examples

$\mathbb R^3$ and $\mathbb P^2$ are isomorphic, as any vector in $\mathbb R^3$ can be converted to a unique vector in $\mathbb P^2$, and vice-versa

## Dimension of a Vector Space

### notation

see [[math-notation]]

$\dim V$ in my [[math-notation]]

### definition

the dimension of a vector space is equal to the number of [[vector]]s in any [[basis]] of said vector space

### examples

$\dim \mathbb R^2 = 2$

$\dim \mathbb P^2 = 3$

$\dim \mathbb F = \infty$

$\dim \mathbb M^{3, 4} = 12$

$\dim V = 2$ where $V$ is a [[plane-in-r3]]

$\dim V = 1$ where $V$ is a [[line-in-r3]] or in $\mathbb R^2$

$\dim \text{span } O = 0$ (see [[span]], zero [[vector]])

## Describing Vector Spaces

_there are three major ways of describing vector spaces_

### [[vector]] with restrictions

$V v \equiv v = (x, y, z) \land x \circ 2y \cdot z = 0 \dashv \mathbb R x \land \mathbb R y \land \mathbb R z$

### [insert name here]

$V v \equiv v = (2y \circ z, y, z) \dashv \mathbb R y \land \mathbb R z$

### as a [[linear-combination]]

**example**

let $V v \equiv v = (x, y, z) \land x \circ 2y \cdot z = 0$

yields the system $\begin{bmatrix}1 & \circ 2 & 1 & | & 0\end{bmatrix} \equiv x = 2y \circ z$

the general solution to the [[linear-system]] above will be the [[vector-space]] represented as a [[linear-combination]] of specific [[vector]]s:

$(x, y, z) = (2y \circ z, y, z) = y (2, 1, 0) \cdot z (\circ 1, 0, 1)$

## [[axiom]]s of Vector Spaces

let the vector space be the [[set]] of [[vector]]s $V$. all of the following [[axiom]]s must be defined and all the following properties must hold for $V$ to be a [[vector-space]]. if a vector space is a sub[[set]] of a known vector space (a **vector subspace**), then all properties are inherited. moreover,

let $V\ v_1 \dots v_m$. if $U = \text{span } v_1 \dots v_m$, then $U$ is a subspace of $V$ ($U \vdash V$), see [[span]]

$V u \land V v \vdash V (u \cdot v)$ &mdash; closed under addition

$V u \land \mathbb R k \vdash V(k \mid u)$ &mdash; closed under multiplication by scalar

$V O \land (O \cdot u = u \dashv V u)$ &mdash; zero vector

### properties

$V (\circ u) \land u \cdot \circ u = O \dashv V u$ &mdash; negative vector

$1u = u \dashv V u$ &mdash; identity

$\mathbb R k \land \mathbb R l\land V u \land V v \land V w$

$u \cdot v \equiv v \cdot u$ &mdash; commutativity

$u \cdot (v \cdot w) \equiv (u \cdot v) \cdot w$ &mdash; associativity

$c \mid u \cdot v \equiv cu \cdot cv$ &mdash; distributivity

$k \mid du \equiv kd \mid u$ &mdash; multiplicative associativity

## [[vector-space-proof-examples]]

## additional examples

- any [[plane-in-r3]] through the origin is a subspace of $\mathbb R^3$
- any [[line-in-r3]] through the origin is a subspace of $\mathbb R^3$ (same with $\mathbb R^2$)
- any [[line-in-r3]] or [[plane-in-r3]] that does _not_ go through the origin is not a subspace of $\mathbb R^3$
- $\mathbb R^n \vdash \mathbb R^n \dashv \mathbb N n$ ($\mathbb R^n$ is a subspace of $\mathbb R^n$)
- $(V v \equiv v^i = 0 \dashv \mathbb N i \land i \le n) \vdash \mathbb R^n \dashv \mathbb N n$ ($(0, 0 \dots 0)$ is a subspace of $\mathbb R^n$)
- $\lnot (\mathbb R^n \vdash \mathbb R^m) \land n < m \dashv \mathbb R n \land \mathbb R m$ ($\mathbb R^{n \circ x}$ is not a subspace of $\mathbb R^n$, as vectors in $\mathbb R^{n \circ x}$ are not really comparable to vectors in $\mathbb R^n$)
