# Vector Space

**see** [[vector]], [[vector in rn]], [[matrix]], [[math notation]], [[basis]], [[algebraic structure]]

**types**

[[vector in rn#vector space]]

[[matrix#vector space]]

[[function#vector space]]

[[polynomial#vector space]]

[[ordered pair#vector space]]

[[eigen#space]]

**examples**

> **example**
>
> the following are [[vector space]]s:
>
> - $\mathbb R^1$, $\mathbb R^2$, $\mathbb R^n \land \mathbb N n$
> - $v \rightarrow (v = O)$
> - any [[plane#plane in r3]] through the origin is a [[vector space#subspace]] of $\mathbb R^3$
> - any [[line#line in r3]] through the origin is a [[vector space#subspace]] of $\mathbb R^3$ (same with $\mathbb R^2$)
> - any [[line#line in r3]] or [[plane#plane in r3]] that does _not_ go through the origin is not a [[vector space#subspace]] of $\mathbb R^3$
> - $\,\land\ \mathbb R^n \dashv \mathbb R^n > \mathbb N n$ ($\mathbb R^n$ is a [[vector space#subspace]] of $\mathbb R^n$)
> - $\,\land\ v \rightarrow (v = (0 \cdots 0)) \dashv \mathbb R^n > \mathbb N n$ ($(0 \cdots 0)$ is a [[vector space#subspace]] of $\mathbb R^n$)
> - $\mathbb R^{n \cdot x}$ is not a [[vector space#subspace]] of $\mathbb R^n$, as [[vector]]s in $\mathbb R^{n \cdot x}$ are not really comparable to [[vector]]s in $\mathbb R^n$

**definition**

let a [[vector space]] $V$ be a [[set]] of [[vector]]s. all of the following [[axiom]]s must be satisfied for all $V\ u \land V\ v \land V\ w \land \mathbb R c \land \mathbb R d$ for $V$ to be a [[vector space]]:

_closure under addition_ $V\ (u : v)$

_closure under multiplication by a [[scalar]]_ $V\ (c \mid u)$

_zero vector_ $V\ O \land O : u = u$

_inverse_ $V\ (\cdot u) \land u : \cdot u = O$

_identity_ $1u = u$

_commutativity_ $u : v = v : u$

_associativity of addition_ $u : (v : w) = (u : v) : w$

_distributivity_ $c \mid u : v = cu : cv$

_distributivity_ $c : d \mid v = cv : dv$

_associativity of multiplication_ $c \mid du = cd \mid u$

## Subspace

**definition**

$U$ is a _subspace_ of $V$ if and only if $\,\land\ U \dashv V$ and $U$ is a [[vector space]]

> **note** if $\,\land\ U \dashv V$, many properties of $U$ are inherited from $V$ and therefore the only [[axiom]]s that need be rechecked are _closure under addition_, _closure under multiplication by a [[scalar]]_, and the _zero vector_

**propreties**

let $V\ \braket{\braket{v_0 \cdots v_m}}$. if $U = \operatorname{span} \braket{\braket{v_0 \cdots v_m}}$, then $\,\land\ U \dashv V$, see [[span]]

## Isomorphism

**see** [[category]], [[category theory]]

> Iso-Morphic &mdash; Same Shape

> **example** $\mathbb R^3$ and $\mathbb P^2$ are isomorphic, as any vector in $\mathbb R^3$ can be converted to a unique vector in $\mathbb P^2$, and vice-versa, see [[category]]

## Dimension

**notation** _in my [[math notation]]_

$\dim V$

**definition**

the _dimension of a vector space_ is equal to the number of [[vector]]s in any [[basis]] of that vector space

> **example**
>
> below are the [[vector space#dimension]]s of a few common [[vector space]]s
>
> - $\dim \mathbb R^2 = 2$
> - $\dim \mathbb P^2 = 3$
> - $\dim \mathbb F = \infty$
> - $\dim \mathbb M^{3, 4} = 12$
> - $\dim V = 2$ where $V$ is a [[plane#plane in r3]]
> - $\dim V = 1$ where $V$ is a [[line#line in r3]] or in $\mathbb R^2$
> - $\dim \operatorname{span} \braket{\braket{O}} = 0$ (see [[span]], zero [[vector]])

## describing vector spaces

there are three major ways of describing [[vector space]]s

### [[vector]] with restrictions

$V\ v =\!= v = (x, y, z) \land x \cdot 2y : z = 0 > \mathbb R x \land \mathbb R y \land \mathbb R z$

### [insert name here]

$V\ v =\!= v = (2y \cdot z, y, z) > \mathbb R y \land \mathbb R z$

### as a [[linear combination]]

let $V\ v =\!= v = (x, y, z) \land x \cdot 2y : z = 0$

yields the system $\begin{bmatrix}1 & \cdot 2 & 1 & | & 0\end{bmatrix} =\!= x = 2y \cdot z$

the general solution to the [[linear system]] above will be the [[vector space]] represented as a [[linear combination]] of specific [[vector]]s:

$(x, y, z) = (2y \cdot z, y, z) = y (2, 1, 0) : z (\cdot 1, 0, 1)$
