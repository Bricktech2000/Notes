# Vector Space Proof Examples

## [[proof]]s

### example

$u = (x, 2x) \land v = (y, y2) \land \mathbb R k$

prove $V v \equiv v = (x, 2x) \land \mathbb R x$ is a [[vector-space]]

_closed under addition_

$u \cdot v = (x \cdot y, 2\ |\ x \cdot y)$

therefore, $V (u \cdot v)$

_closed under multiplication_

$ku = k(x, 2x) = (kx, 2kx)$

therefore, $V (ku)$

_zero vector_

$x = 0 \land y = 0 \vdash V (0, 0)$

_properties_

$V \vdash \mathbb R^2$

therefore, all properties are inherited from $\mathbb R^2$

### counterexample

$u = (x, x \cdot 2) \land v = (y, y \cdot 2)$

prove $V v \equiv v = (x, x \cdot 2) \land \mathbb R x$ is a [[vector-space]]

_closed under addition_

$u \cdot v = (x \cdot y, x \cdot y \cdot 4) \vdash \lnot V (u \cdot v)$

therefore, $V$ is not a [[vector-space]] as at least one [[axiom]] has been proved $\bot$

### example

$u = x_1(1, 2, 3) \cdot y_1(0, \circ 1, 4)\ \land\ v = x_2(1, 2, 3) \cdot y_2(0, \circ 1, 4)\ \land\ \mathbb R k$

prove $V v \equiv v = x(1, 2, 3) \cdot y(0, \circ 1, 4) \land \mathbb R x \land \mathbb R y$ (see [[linear-combination]])

_closed under addition_

$u \cdot v = (x_1 \cdot x_2)(1, 2, 3) \cdot (y_1 \cdot y_2)(0, \circ 1, 4)$

therefore, $V (u \cdot v)$

_closed under multiplication_

$ku = cx_1(1, 2, 3) \cdot cy_1(0, \circ 1, 4)$

_zero vector_

$x = 0 \land y = 0 \vdash V (0, 0, 0)$

_properties_

$V \vdash \mathbb R^3$

therefore, all properties are inherited from $\mathbb R^3$

### counterexample

$T u \land T v \equiv u(1, 2, 3) = 0 \land v(1, 2, 3) = 0$

$\mathbb R k$

prove $T u \equiv \mathbb R^3 u \land u(1, 2, 3) = 0$ (see [[dot-product]]) is a [[vector-space]]

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

$T \vdash \mathbb R^3$

therefore, all properties are inherited from $\mathbb R^3$

### example with [[matrix]]es

$M m \equiv m = \mathbb M^{2, 2} m \land m^{0, 0} \cdot m^{1, 1} = m^{1, 0} \cdot m^{0, 1}$

_zero vector_

$m = \begin{bmatrix}0 & 0 \\\  0 & 0\end{bmatrix} \vdash m^{0, 0} \cdot m^{1, 1} = m^{1, 0} \cdot m^{0, 1}$

therefore, $M O$

_closed under addition_

$M m_1 \land M m_2$

$m_1^{0, 0} \cdot m_1^{1, 1} = m_1^{1, 0} \cdot m_1^{0, 1}$

$m_2^{0, 0} \cdot m_2^{1, 1} = m_2^{1, 0} \cdot m_2^{0, 1}$

$(m_1^{0, 0} \cdot m_2^{0, 0}) \cdot (m_1^{1, 1} \cdot m_2^{1, 1}) = (m_1^{1, 0} \cdot m_2^{1, 0}) \cdot (m_1^{0, 1} \cdot m_2^{0, 1})$

therefore, $M (m_1 \cdot m_2)$

_closed under multiplication_

$km = k \begin{bmatrix}m^{0, 0} & m^{0, 1} \\\  m^{1, 0} & m^{1, 1}\end{bmatrix} = \begin{bmatrix}km^{0, 0} & km^{0, 1} \\\  km^{1, 0} & km^{1, 1}\end{bmatrix}$

$km^{0, 0} \cdot km^{1, 1} = km^{1, 0} \cdot km^{0, 1}$

$k\ |\ m^{0, 0} \cdot m^{1, 1} = k\ |\ m^{1, 0} \cdot km^{0, 1}$

$k\ |\ m^{0, 0} \cdot m^{1, 1} = k\ |\ m^{0, 0} \cdot km^{1, 1}$

therefore, $M(km)$
