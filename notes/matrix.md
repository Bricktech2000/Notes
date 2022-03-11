# Matrix

see [[math-notation]]

## notation

[[vector-space]] of $m \times n$ matrices:

$\mathbb{M}^{m, n}$ in my [[math-notation]]

$M_{m\ n}(\R)$ in [[classical-math-notation]]

## Rank of a Matrix

_the number of pivots in any REF of the matrix_

### notation

$rank\ A$, where

$A$ is the matrix to find the rank of

### determining the type of the general solution

see [[linear-system]]

let $[A\ |\ b]$ be an augmented matrix.

- the system has no solutions if $rank(A) \lt rank([A|b])$
- the system has a unique solution if and only if $rank(A) = rank([A|b]) = \text{number of columns in A}$
- the system infinite solutions if and only if $rank(A) = rank([A|b]) \lt \text{number of columns in A}$

## Multiplication by a Scalar

### definition

$(kA)^{i, j} = kA^{i, j} \dashv \N i \land \N j \land \R k \land \mathbb{M} A$

## Matrix Addition

### definition

$(A \cdot B)^{i, j} = A^{i, j} \cdot B^{i, j} \dashv \N i \land \N j \land \mathbb{M}^{m, n} A \land \mathbb{M}^{m, n} B$ (matrix addition)

## Matrix Multiplication

see [[dot-product]], [[vector-in-rn]]

### definition

$AB \ne \varnothing \equiv \mathbb{M}^{m, n}A \land \mathbb{M}^{n, p}B \land \N n \vdash \mathbb{M}^{m, p}AB$ ($AB$ is defined if the number of columns in $A$ is equal to the number of rows in $B$. their product will be an $m ' p$ matrix)

$(AB)^{i, j} = A^{i, }\ |\ B^{, j} \dashv \N i \land \N j$, see [[dot-product]] (the $|$ here is a vector [[dot-product]], [[think]])

### notation

$AA = A2 = \braket A2 \dashv \mathbb{M} A$

therefore,

$AA \dots A = \braket A n \land \N n \dashv \mathbb{M} A$

### properties

$AB = BA \dashv \mathbb{M} A \land \mathbb{M} B \equiv \bot$ or $AB \ne BA \land \mathbb{M} A \land \mathbb{M} B$ (not commutative)

$AB = 0 \vdash A = 0 \lor B = 0 \equiv \bot$ (it can happen that $AB = 0$, but $A \ne 0$ and $B \ne 0$) ($AB$ being equal to $0$ does not imply that $A = 0$ or that $B = 0$)

$AC = BC \land C \ne 0 \vdash A = B \equiv \bot$ ($AC = BC$ and $C \ne 0$ does not imply that $A = B$)

$(AB)C = A(BC)$ (associative)

$A(B \cdot C) = AB \cdot AC$ (distributive)

$(B \cdot C)A = BA \cdot CA$ (distributive)

$k(AB) = (kA)B = A(kB)$ (associative with scalars)

### examples

can be used to represent a [[linear-system]] of [[linear-equation]]s:

$\begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{bmatrix}\begin{bmatrix}x \\ y \\ z\end{bmatrix}$

## Identity Matrix

$I^{a, b} = 1 \land a = b \lor I^{a, b} = 0 \land a \ne b \dashv \N a \land \N b \land \mathbb{M}^{n, n} I$

### examples

$\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}$

$\begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}$

$\dots$

### properties

$AI = A \land IA = A \dashv \mathbb{M} A$

## Zero Matrix

$O^{a, b} = 0 \dashv \N a \land \N b \land \mathbb{M}^{n, m} O$

### examples

$\begin{bmatrix}0 & 0 \\ 0 & 0\end{bmatrix}$

$\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{bmatrix}$

$\dots$

### properties

$A \cdot O = A \land O \cdot A = A \dashv \mathbb{M} A$

$A_{m, n}O_{n, p} = O_{m, p} \dashv \mathbb{M}^{n, p} O_{n, p} \land \mathbb{M}^{m, p} O_{m, p} \land \mathbb{M}^{m, n} A_{m, n}$

$O_{q, m}A_{m, n} = O_{q, n} \dashv \mathbb{M}^{q, m} O_{q, m} \land \mathbb{M}^{q, n} O_{q, n} \land \mathbb{M}^{m, n} A_{m, n}$

## Nullspace (Kernel)

### notation

$Ker\ A \equiv Null\ A$

### definition

$Ker\ A = x \equiv Null\ A = x \equiv Ax = 0 \land \mathbb{M}^{m, n}A \land \mathbb{M}^{n, 1} x$

the Kernel of a matrix can be calculated using [[gaussian-elimination|row-reduction]]

### properties

the Null Space of a [[matrix]] is always a [[vector-space]]

> **theorem**: the [[span]]ning set of $Null\ A$ obtained from applying [[gaussian-elimination|row-reduction]] on the system $Ax = 0$ is a [[basis]] for $Null\ A$

> therefore, as $\dim Null\ A = \text{number of free variables in } Ax = 0$, we deduce that $\dim Null\ A \cdot rank\ A = \text{number of columns in } A$

### example

_transforming a vector space into the null space of a certain matrix_

let $W = span\{(1, 0, 0, 1), (1, 1, 1, 0), (2, 1, \circ 1, 1)\}$

after solving the [[linear-system]], we get $W (x, y, z, w) \equiv \circ x \cdot y \cdot w = 0$. therefore, $W$ is the nullspace of $A = \begin{bmatrix}\circ 1 & 1 & 0 & 1\end{bmatrix}$

## Column Space, Row Space

see [[vector-in-rn-vector-space]]

### notation

$Col\ A$

$Row\ A$

### definition

$Col\ A = span\{A^{, n}\} \dashv \N n$

$Row\ A = span\{A^{n,}\} \dashv \N n$

### properties

$Col\ A = Row\ A^\intercal \land Row\ A = Col\ A^\intercal$, see transpose [[matrix]]

> **theorem**: $Row\ A$ does not change when doing [[linear-system|elementary-operations]] on the rows of $A$ (if $A$ and $B$ are [[linear-system|row-equivalent]], $Row\ A = Row\ B$

> **theorem**: the nonzero rows in any [[linear-system|REF]] of a [[matrix]] $A$ forms a [[basis]] for $Row\ A$. therefore, $\dim Row\ A = rank\ A$ (see rank of a [[matrix]])

row spaces can be used to find a [[basis]] for a [[span]]ning set of vectors through [[gaussian-elimination|row-reduction]]

the basis for the column space of a [[matrix]] can be found by applying [[gaussian-elimination|row-reduction]] and [[span]]ning the **row-reduced columns** in the [[linear-system|REF]] form of the [[matrix]]

the basis for the column space of a [[matrix]] can be found by applying [[gaussian-elimination|row-reduction]] and [[span]]ning the **original columns** that became pivots in the [[linear-system|REF]] form of the [[matrix]]

the same can be said for $Col\ A$

## Transpose Matrix

_the Transpose of a Matrix_

### definition

$(A^\intercal)^{i, j} = (A)^{j, i} \dashv \N i \land \N j \land \mathbb{M} A$

### properties

$A^{\intercal^\intercal} = A \dashv \mathbb{M} A$

$(AB)^\intercal = B^\intercal A^\intercal \dashv \mathbb{M} A \land \mathbb{M} B$

### example

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Matrix_transpose.gif/200px-Matrix_transpose.gif)
