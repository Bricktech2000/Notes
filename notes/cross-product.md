# Cross Product

see [[math-notation]], [[determinant]], [[vector]]

the cross product is only defined for [[vector-in-rn]]3

### definitions

_results in a [[vector]] of length (area of the parallelogram formed by the two [[vector]]s) and of orientation (perpendicular to the [[plane-in-r3]] formed by the two [[vector]]s)_ — 3B1B

see [[determinant]]

$|a\ |^\times\ b| = \det \begin{bmatrix} a\ |\ b\end{bmatrix}$

$a\ |^\times\ b = \det \begin{bmatrix}B\ |\  a\ |\ b\end{bmatrix}$, where

$B$ is the basis [[vector]], i.e. $\begin{bmatrix}\hat i \\\  \hat j  \\\  \dots\end{bmatrix}$

### shortcut

$\begin{bmatrix}a_1 \\\  a_2 \\\  a_3\end{bmatrix}\ |^\times\ \begin{bmatrix}b_1 \\\  b_2 \\\  b_3\end{bmatrix} = \begin{bmatrix}a_2b_3 \circ b_2a_3 \\\  a_3b_1 \circ b_3a_1 \\\  a_1b_2 \circ b_1a_2\end{bmatrix}$

### properties

$a\ |^\times\ b = \circ b\ |^\times\ a$ &mdash; not commutative

$u\ |^\times\ v\ |'\ u = 0$ and $u\ |^\times\ v\ |'\ v = 0$, see [[dot-product]] &mdash; orthogonal to both [[vector]]s

$a\ |^\times\ b \cdot c = a '^\times b \cdot a '^\times c$ &mdash; multiplication distributive over addition

$b \cdot c\ |^\times\ a = b '^\times a \cdot c '^\times a$ &mdash; multiplication distributive over addition

$k\ |\ a '^\times b = ka\ |^\times\ b = a\ |^\times\ kb$ &mdash; associative with scalar multiplication (think of this intuitively)

### uses

$|u '^\times v|$ is the area of the parallelogram with sides $u$ and $v$

for volume of [[parallelepiped]] from 3 [[vector]]s in $\mathbb R^3$, see [[vector-in-rn]]

orthogonality to both vectors, see properties above
