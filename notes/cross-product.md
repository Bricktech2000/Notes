# Cross Product

see [[math-notation]], [[determinant]]

the cross product is only defined for [[vector-in-rn]]3

### definitions

_results in a vector of length (area of the parallelogram formed by the two vectors) and of orientation (perpendicular to the plane formed by the two vectors)_ — 3B1B

> the [[determinant]] is all about measuring how areas change during a transformation. after the transformation, the $1 \times 1$ unit square formed by $\vec i$ and $\vec j$ gets turned into the parallelogram formed by the two vectors — 3B1B

$|a \times b| = \det \begin{bmatrix} a\ |\ b\end{bmatrix}$

$a \times b = \det \begin{bmatrix}B\ |\  a\ |\ b\end{bmatrix}$, where

$B$ is the basis vector, i.e. $\begin{bmatrix}\hat i \\ \hat j  \\ \dots\end{bmatrix}$

### shortcut

$\begin{bmatrix}a_1 \\ a_2 \\ a_3\end{bmatrix} \times \begin{bmatrix}b_1 \\ b_2 \\ b_3\end{bmatrix} = \begin{bmatrix}a_2b_3 \circ b_2a_3 \\ a_3b_1 \circ b_3a_1 \\ a_1b_2 \circ b_1a_2\end{bmatrix}$

### **properties**

$a \times b = \circ b \times a$

$u \times v\ |\ u = 0$ and $u \times v\ |\ v = 0$ (orthogonal to both vectors)

$a \times (b \cdot c) = a \times b \cdot a \times c$ and $(b \cdot c) \times a = b \times a \cdot c \times a$

$k(a \times b) = (ka) \times b = a \times (kb)$, think of this intuitively

### uses

$|u \times v|$ is the area of the parallelogram with sides $u$ and $v$

for volume of parallelepiped from 3 vectors in $\R^3$, see [[vector-in-rn]]

$u \times v$ is orthogonal to both $u$ and $v$, see [[vector-in-rn]]
