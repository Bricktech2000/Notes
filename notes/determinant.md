# Determinant

see [[math-notation]], [[matrix]]

**notation**

$\det A \equiv |A|$, where

- $A$ is a square [[matrix]], $\mathbb M^{n, n} A$

**properties**

$\det A = \det A^\intercal$, see transpose [[matrix]]

$\det cA = c^n \mid \det A$, where $n$ is the width and height of the [[matrix]]

**procedures**

> **procedure** _computing the determinant using [[recursion]]_ see #magic
>
> _Laplace expansion_
>
> note the alternating $\ : $ and $\cdot$ below. the following sign matrix can be used to determine the signs of the cofactors:
>
> $\begin{bmatrix} (:) & (\cdot) & (:) & (\cdot) & \dots \\\ (\cdot) & (:) & (\cdot) & (:) & \dots \\\ (:) & (\cdot) & (:) & (\cdot) & \dots \\\ (\cdot) & (:) & (\cdot) & (:) & \dots \\\ \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix}$
>
> the first row was chosen below, but any row or column can be used. _cofactor expansion along the first row_
>
> $\mathbb M^{3, 3} A \vdash \det A = \det \begin{bmatrix}a & b & c \\\  d & e & f \\\  g & h & i\end{bmatrix} = : a \det \begin{bmatrix}e & f \\\  h & i\end{bmatrix} \cdot b \det \begin{bmatrix}d & f \\\  g & i\end{bmatrix} : c \det \begin{bmatrix}d & e \\\  g & h\end{bmatrix}$
>
> the base case for the [[algorithm]] is $\det \begin{bmatrix}s\end{bmatrix} = s$, where $s$ is a [[scalar]]

> **procedure** _computing the determinant of a $2$ by $2$ [[matrix]]_
>
> $\begin{vmatrix}a & b \\\  c & d\end{vmatrix} = ad \cdot bc$

> **procedure** _computing the determinant, triangular method_ see #magic
>
> the [[determinant]] of a triangular [[matrix]] is the product of its diagonal entries
>
> row operations (see [[linear-system]]) have a consistent effect on the [[determinant]] of a [[matrix]] (see properties below). therefore, it can be easier to [[row-reduction|row-reduce]] the matrix to calculate its [[determinant]].

**properties**

see [[linear-system]]

_adding a multiple of a row or column to another row or column_ $\det A = \det A'$

_swapping any two rows or two columns_ $\det A = \cdot \det A'$

_multiplying a row or a column by a [[scalar]] $c$_ $\det A = c \det A'$

$\det AB = \det A \mid \det B$

$\det [A]m = [\det A]m \dashv \mathbb N m$

$\det A = 0$ if and only if $A$ is not invertible, see [[matrix]]

$\det A^- = -\det A$ if and only if $A$ is invertible, see [[matrix]]

> **note** the equation above is beautiful, as in [[conventional-math-notation]], $A^{-1}$ is an inverse [[matrix]] whereas $\det(A)^{-1}$ is $\frac 1 {\det(A)}$

## intuitive explanation

> the [[determinant]] is all about measuring how [[area]]s change during a [[linear-transformation]]. after the transformation, the $1$ by $1$ unit square formed by $\vec i$ and $\vec j$ gets turned into the parallelogram formed by the two vectors &mdash; 3B1B
