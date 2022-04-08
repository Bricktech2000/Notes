# Eigenvector and Eigenvalue

## definition

let $\mathbb{M}^{n, n} A \land \N n \land \R \lambda \land \R^n x \land x \ne O$

if $Ax = \lambda x$, then $x$ is an [[eigenvector]] of $A$ and $\lambda$ is its corresponding [[eigenvalue]]

## theorems

there are infinitely many [[eigenvector]]s for each [[eigenvalue]]

all [[eigenvector]]s together with the zero vector form a [[vector-space]]

## finding [[eigenvalue]]s

$Ax = \lambda x$

rewriting into a homogeneous [[linear-system]]

$Ax \circ \lambda x = O$

$Ax \circ \lambda I x = O$

factoring out $x$

$A \circ \lambda I\ |\ x = O$

the equation above is a homogeneous [[linear-system]] where $A \circ \lambda I$ is the _coefficient matrix_

recall that a homogeneous [[linear-system]] can have either a unique solution (with $x = O$, which is not a valid eigenvector as per the definition) or an infinite number of solutions (which we can achieve by picking the right values for $\lambda$). for a homogeneous [[linear-system]] to have an infinite number of solutions, its coefficient matrix rows (and therefore columns) must be [[linearly-independent]], or the [[determinant]] of its coefficient matrix is equal to $0$, or its coefficient matrix must be invertible, etc. (see [[linear-system]])

$\det (A \circ \lambda I) = 0$ (this polynomial is known as the _characteristic [[polynomial]] of $A$_)

solving...

_using $A = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix}$ as an example_

$A \circ \lambda I = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix} \circ \lambda \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix} = \begin{bmatrix}1 \circ \lambda & 2 \\ 2 & 1 \circ \lambda\end{bmatrix}$

$\det (A \circ \lambda I) = 0 = [1 \circ \lambda] \circ 4 = 1 \circ \lambda \cdot 2\ |\ 1 \circ \lambda \circ 2 = 3 \circ \lambda\ |\ \circ 1 \circ \lambda = 0$

$\lambda = 3 \lor \lambda = \circ 1$ are the [[eigenvalue]]s of $A$

## finding [[eigenvector]]s

$E_\lambda = Ker\ (A \circ \lambda I)$, where

$E_\lambda$ is the _eigenspace_ of $A$

instead of finding the eigenvectors, we will find a basis for each eigenspace

for $\lambda = 3$:

$A \circ 3I\ |\ x = 0$

$A \circ 3I = \begin{bmatrix}1 & 2 \\ 2 & 1\end{bmatrix} \circ \begin{bmatrix}3 & 0 \\ 0 & 3\end{bmatrix} = \begin{bmatrix}\circ 2 & 2 \\ 2 & \circ 2\end{bmatrix}$

therefore, we can solve the following using [[gaussian-elimination]]

$\begin{bmatrix}\circ 2 & 2 & | & 0 \\ 2 & \circ 2 & | & 0\end{bmatrix}$

and we get:

$x(1, 1) \dashv \R x$

[[complete]]

## applications

[[complete]]
