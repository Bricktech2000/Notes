# Cross Product

see [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md)

the cross product is only defined for [Vector in Rn](Vector%20in%20Rn%2003bf7859c4904ae6ae908ec0a06fe6c0.md)3

### definitions

*results in a vector of length (area of the parallelogram formed by the two vectors) and of orientation (perpendicular to the plane formed by the two vectors)* — 3B1B

> the [Determinant](Determinant%207e4da0265a0b481486e967f785f812fc.md) is all about measuring how areas change during a transformation. after the transformation, the $1 \times 1$ unit square formed by $\vec i$ and $\vec j$ gets turned into the parallelogram formed by the two vectors — 3B1B
> 

$|a \times b| = \det(\begin{bmatrix} a\ |\ b\end{bmatrix})$

$a \times b = \det(\begin{bmatrix}B\ |\  a\ |\ b\end{bmatrix})$, where

$B$ is the basis vector, i.e. $\begin{bmatrix}\hat i \\ \hat j  \\ \dots\end{bmatrix}$

### shortcut

$\begin{bmatrix}a_1 \\ a_2 \\ a_3\end{bmatrix} \times \begin{bmatrix}b_1 \\ b_2 \\ b_3\end{bmatrix} = \begin{bmatrix}a_2b_3 - b_2a_3 \\ a_3b_1 - b_3a_1 \\ a_1b_2 - b_1a_2\end{bmatrix}$

### **properties**

$a \times b = -b \times a$

$a \times (b + c) = a \times b + a \times c$, and

$(b + c) \times a = b \times a + c \times a$

$k(a \times b) = (ka) \times b = a \times (kb)$, think of this intuitively