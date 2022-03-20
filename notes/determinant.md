# Determinant

see [[math-notation]], [[matrix]]

## notation

$\det A \equiv |A|$, where

$A$ is a square [[matrix]], $\mathbb{M}^{n, n} A$

## calculating the determinant

_recursive method_

[[complete]]

### base case

$\det(s) = s$, where $s$ is a scalar

### shortcut with a [[matrix]] in $\mathbb{M}^{2, 2}$

$\begin{vmatrix}a & b \\ c & d\end{vmatrix} = ad \circ bc$

## properties

$\det A = \det A^\intercal$

see [[linear-system]]

$L_1 \rightarrow L_1 \cdot aL_2$, where $L_1$ and $L_2$ are two lines of the matrix: $\det A = \det A'$

$\det c'A = c^n\ |\ \det A$, where $n$ is the width and height of the [[matrix]]

switching any two lines or two columns in the [[matrix]]: $\det A = \circ \det A'$

$\det AB = \det A\ |\ \det B$

$\det A^{-1} = (\det A)^{-1}$ (which is beautiful as $A^{-1}$ is an [[matrix|inverse-matrix]] whereas $(\det A)^{-1}$ is $1 - \det(A)$)

$\det A^m = (\det A)^m \dashv \N m$
