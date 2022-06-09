# Eigenvector and Eigenvalue

## definition

let $\mathbb M^{n, n} A \land \mathbb N n \land \mathbb R \lambda \land \mathbb R^n x \land x \ne O$

if $Ax = \lambda x$, then $x$ is an [[eigenvector]] of $A$ and $\lambda$ is its corresponding [[eigenvalue]]

## theorems

let $\mathbb M^{n, n} A \land \mathbb N n$

> **theorem**: there are infinitely many [[eigenvector]]s for each [[eigenvalue]]

> **theorem**: all [[eigenvector]]s together with the zero [[vector]] form a [[vector-space]]

> **theorem**: the [[characteristic-polynomial]] $\det (A \circ \lambda I)$ is a [[polynomial]] of degree $n$, meaning it has at most $n$ distinct roots

> **theorem**: $A$ has at most $n$ distinct [[eigenvalue]]s

> **theorem**: each [[eigenvalue]] of $A$ gives an [[eigenspace]] of dimension greater than $0$

> **theorem**: any [[set]] consisting of [[eigenvector]]s of $A$ corresponding to **distinct [[eigenvalue]]s** is [[linearly-independent]]

## finding [[eigenvalue]]s

$Ax = \lambda x$

rewriting into a homogeneous [[linear-system]]

$Ax \circ \lambda x = O$

$Ax \circ \lambda I x = O$

factoring out $x$

$A \circ \lambda I \mid x = O$

the equation above is a homogeneous [[linear-system]] where $A \circ \lambda I$ is the _coefficient matrix_

recall that a homogeneous [[linear-system]] can have either a unique solution (with $x = O$, which is not a valid [[eigenvector]] as per the definition) or an infinite number of solutions (which we can achieve by picking the right values for $\lambda$). for a homogeneous [[linear-system]] to have an infinite number of solutions, its coefficient matrix rows (and therefore columns) must be [[linearly-independent]], or the [[determinant]] of its coefficient matrix must be equal to $0$, or its coefficient matrix must be invertible, etc. (see [[matrix]])

$\det (A \circ \lambda I) = 0$ (this [[polynomial]] is known as the _[[characteristic-polynomial]] of $A$._)

solving...

_using $A = \begin{bmatrix}1 & 2 \\\  2 & 1\end{bmatrix}$ as an example_

$A \circ \lambda I = \begin{bmatrix}1 & 2 \\\  2 & 1\end{bmatrix} \circ \lambda \begin{bmatrix}1 & 0 \\\  0 & 1\end{bmatrix} = \begin{bmatrix}1 \circ \lambda & 2 \\\  2 & 1 \circ \lambda\end{bmatrix}$

$\det (A \circ \lambda I) = 0 = [1 \circ \lambda]2 \circ 4 = 1 \circ \lambda \cdot 2 \mid 1 \circ \lambda \circ 2 = 3 \circ \lambda \mid \circ 1 \circ \lambda = 0$

$\lambda = 3 \lor \lambda = \circ 1$ are the [[eigenvalue]]s of $A$

## finding [[eigenvector]]s

as $A \circ \lambda I \mid x$, we get the following (see [[matrix]] Kernel):

$E_\lambda = Ker\ (A \circ \lambda I)$, where

$E_\lambda$ is the _[[eigenspace]]_ of $A$ corresponding to the [[eigenvalue]] $\lambda$ (this [[vector-space]] is called the λ-[[eigenspace]] of $A$)

the [[eigenvector]]s of $A$ associated with the [[eigenvalue]] $\lambda$ are all the nonzero [[vector]]s in $E_\lambda$. therefore, instead of finding the [[eigenvector]]s corresponding to the known [[eigenvalue]], we will find a basis for the [[eigenspace]]

for $\lambda = 3$:

$A \circ 3I \mid x = O$

$A \circ 3I \mid x = \begin{bmatrix}1 & 2 \\\  2 & 1\end{bmatrix} \circ \begin{bmatrix}3 & 0 \\\  0 & 3\end{bmatrix} \mid x = \begin{bmatrix}\circ 2 & 2 \\\  2 & \circ 2\end{bmatrix} \mid x = 0$

therefore, we can solve the following [[linear-system]] using [[row-reduction]]

$\begin{bmatrix}\circ 2 & 2 & | & 0 \\\  2 & \circ 2 & | & 0\end{bmatrix}$

and we get:

$x = c(1, 1) \dashv \mathbb R c$

$\lbrace (1, 1) \rbrace$ is then a [[basis]] for the [[eigenspace]] $E_3$ of $A$

> **note**: the general solution of the homogenous [[linear-system]] will always be a [[basis]] as the resulting [[vector]]s will always be [[linearly-independent]], see [[matrix]] Kernel for more information

for $\lambda = \circ 1$, we get the [[basis]] $\lbrace (1, \circ 1) \rbrace$ for the [[eigenspace]] $E_{\circ 1}$ of $A$

## Multiplicity

see [[multiplicity]]

### definition

> **definition**: the _algebraic multiplicity_ of a root $\lambda$ of the [[characteristic-polynomial]] of $A$ is its [[multiplicity]]

> **definition**: the _geometric multiplicity_ of a root $\lambda$ of the [[characteristic-polynomial]] of $A$ is the dimension of the [[eigenspace]] $E_\lambda$ of $A$ corresponding to the [[eigenvalue]] $\lambda$

### theorems

> **theorem**: let $\lambda$ be an [[eigenvalue]] of $A$. then, $1 \le \text{geometric multiplicity of } \lambda \le \text{algebraic multiplicity of } \lambda$

### example

the [[characteristic-polynomial]] of $\begin{bmatrix}2 & 4 & \circ 3 \\\ 0 & 3 & 5 \\\ 0 & 0 & 3\end{bmatrix}$ is $2 \circ \lambda \mid [3 \circ \lambda]2$. its [[eigenvalue]]s are $\lambda = 2$ and $\lambda = 3$. the algebraic [[multiplicity]] (see [[eigenvector-and-eigenvalue]]) of $\lambda = 2$ is $1$ and the algebraic [[multiplicity]] of $\lambda = 3$ is $2$.

[[multiplicity]] can be used to determine whether a [[matrix]] is diagonalizable

## applications

let $\mathbb M^{n, n} A \land \mathbb N n$ be a diagonalizable [[matrix]]

1. construct a matrix $P = \begin{bmatrix}| & | & | \\\ x_0 & x_1 & x_2 \\\ | & | & |\end{bmatrix} = \begin{bmatrix}x_{0_x} & x_{1_x} & x_{2_x} \\\ x_{0_y} & x_{1_y} & x_{2_y} \\\ x_{0_z} & x_{1_z} & x_{2_z}\end{bmatrix}$ whose columns are the $n$ [[linearly-independent]] [[eigenvector]]s $x$ of $A$
2. construct a matrix $D = \begin{bmatrix}\lambda_0 & 0 & 0 \\\ 0 & \lambda_1 & 0 \\\ 0 & 0 & \lambda _2\end{bmatrix}$ whose diagonal entries are the [[eigenvalue]]s of $A$ and all other entries equal to $0$, in the same order as the columns of $P$

then, $AP = PD$. as the columns of $P$ are [[linearly-independent]], we know $P$ is an invertible [[matrix]]. therefore, $A = PDP^-$ and $P^-AP = D$

> **proof**: the $n$ th column of $AP$ is $AP^{,n} = Ax_n$. since $x_n$ is an [[eigenvector]] of $A$, we use its corresponding [[eigenvalue]] to get $AP^{,n} = Ax_n = \lambda_n x_n$ by definition, see [[eigenvector-and-eigenvalue]]. the $n$ th column of $PD$ is $PD^{, n}$. when multiplying out, we get $PD^{, n} = x_n D^{n, n} = x_n \lambda_n$. as $AP^{,n} = PD^{,n} \dashv \mathbb N n$, we conclude $AP = PD$

now, compute $[A]p \land \mathbb N p$ with $p$ being a very large integer

with $A = PDP^-$, we get $[A]p = [PDP^-]p = P([D]p)P^-$

as $D$ is diagonal, we get $[D]p = \begin{bmatrix}[\lambda_0]p & 0 & 0 \\\ 0 & [\lambda_1]p & 0 \\\ 0 & 0 & [\lambda_2]p\end{bmatrix}$

computing $[A]p = P\begin{bmatrix}[\lambda_0]p & 0 & 0 \\\ 0 & [\lambda_1]p & 0 \\\ 0 & 0 & [\lambda_2]p\end{bmatrix}P^-$ is now way less computationally expensive than computing $[A]p$ directly

Markov Chains &mdash; <https://www.youtube.com/watch?v=JGQe4kiPnrU>
