# Determinant

see [[classical-math-notation]], [[matrix]]

## notation

$\det(A) = |A|$, where

$A$ is a square [[matrix]]

$A \in M_{n, n}(\R)$

## calculating the determinant

_recursive method_

...

### base case

$\det(s) = s$, where $s$ is a scalar

### shortcut with a [[matrix]] in $M^{2, 2}$

$\begin{vmatrix}a & b \\ c & d\end{vmatrix} = ad - bc$

## properties

$\det(A) = \det(A^\intercal)$

$L_1 \rightarrow L_1 + aL_2$, where $L_1$ and $L_2$ are two lines of the matrix: $\det(A) = \det(A')$

$\det(c \times A) = c^n \times \det(A)$, where $n$ is the width and height of the matrix

switching any two lines or two columns in the matrix: $\det(A) = - \det(A')$

$\det(AB) = \det(A)\det(B)$

TODO:
$\det(A^{-1}) = \det(A)^{-1}$ (which is beautiful as $A^{-1}$ is an _inverse matrix_ whereas $\det(A)^{-1}$ is $\frac{1}{\det(A)}$) [[todo]]

$\det(A^m) = \det(A)^m, m \in \N$
