# Matrix

see [[math-notation]]

## notation

[[vector-space]] of $m \times n$ matrices:

$\mathbb M^{m, n}$ in my [[math-notation]]

$M_{m\ n}(\mathbb R)$ in [[classical-math-notation]]

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

$(kA)^{i, j} = kA^{i, j} \dashv \mathbb N i \land \mathbb N j \land \mathbb R k \land \mathbb M A$

## Matrix Addition

### definition

$(A \cdot B)^{i, j} = A^{i, j} \cdot B^{i, j} \dashv \mathbb N i \land \mathbb N j \land \mathbb M^{m, n} A \land \mathbb M^{m, n} B$ (matrix addition)

## Matrix Multiplication

see [[dot-product]], [[vector-in-rn]]

### definition

$AB \ne \varnothing \equiv \mathbb M^{m, n}A \land \mathbb M^{n, p}B \land \mathbb N n \vdash \mathbb M^{m, p}AB$ ($AB$ is defined if the number of columns in $A$ is equal to the number of rows in $B$. their product will be an $m ' p$ matrix)

$(AB)^{i, j} = A^{i, }\ |\ B^{, j} \dashv \mathbb N i \land \mathbb N j$, see [[dot-product]] (the $|$ here is a vector [[dot-product]], [[think]])

### notation

$AA = A2 = [A] 2 \dashv \mathbb M A$

therefore,

$AA \dots A = [A] n \land \mathbb N n \dashv \mathbb M A$

### properties

$AB = BA \dashv \mathbb M A \land \mathbb M B \equiv \bot$ or $AB \ne BA \land \mathbb M A \land \mathbb M B$ (not commutative)

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

$I^{a, b} = 1 \land a = b \lor I^{a, b} = 0 \land a \ne b \dashv \mathbb N a \land \mathbb N b \land \mathbb M^{n, n} I$

### examples

$\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}$

$\begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}$

$\dots$

### properties

$AI = A \land IA = A \dashv \mathbb M A$

## Zero Matrix

$O^{a, b} = 0 \dashv \mathbb N a \land \mathbb N b \land \mathbb M^{n, m} O$

### examples

$\begin{bmatrix}0 & 0 \\ 0 & 0\end{bmatrix}$

$\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{bmatrix}$

$\dots$

### properties

$A \cdot O = A \land O \cdot A = A \dashv \mathbb M A$

$A_{m, n}O_{n, p} = O_{m, p} \dashv \mathbb M^{n, p} O_{n, p} \land \mathbb M^{m, p} O_{m, p} \land \mathbb M^{m, n} A_{m, n}$

$O_{q, m}A_{m, n} = O_{q, n} \dashv \mathbb M^{q, m} O_{q, m} \land \mathbb M^{q, n} O_{q, n} \land \mathbb M^{m, n} A_{m, n}$

## Nullspace (Kernel)

### notation

$Ker\ A \equiv Null\ A$

### definition

$Ker\ A = x \equiv Null\ A = x \equiv Ax = 0 \land \mathbb M^{m, n}A \land \mathbb M^{n, 1} x$

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

$Col\ A = span\{A^{, n}\} \dashv \mathbb N n$

$Row\ A = span\{A^{n,}\} \dashv \mathbb N n$

### properties

$Col\ A = Row\ A^\intercal \land Row\ A = Col\ A^\intercal$, see transpose [[matrix]]

> **theorem**: $Row\ A$ does not change when doing [[linear-system|elementary-operations]] on the rows of $A$ (if $A$ and $B$ are [[linear-system|row-equivalent]], $Row\ A = Row\ B$

> **theorem**: the nonzero rows in any [[linear-system|REF]] of a [[matrix]] $A$ forms a [[basis]] for $Row\ A$. therefore, $\dim Row\ A = rank\ A$ (see rank of a [[matrix]])

row spaces can be used to find a [[basis]] for a [[span]]ning set of vectors through [[gaussian-elimination|row-reduction]]

the basis for the row space of a [[matrix]] can be found by applying [[gaussian-elimination|row-reduction]] and [[span]]ning the **row-reduced columns** in the [[linear-system|REF]] form of the [[matrix]]

the basis for the column space of a [[matrix]] can be found by applying [[gaussian-elimination|row-reduction]] and [[span]]ning the **original columns** that became pivots in the [[linear-system|REF]] form of the [[matrix]]

the same can be said for $Col\ A$

## Transpose Matrix

_the Transpose of a Matrix_

### definition

_flips a matrix around its diagonal_

$(A^\intercal)^{i, j} = (A)^{j, i} \dashv \mathbb N i \land \mathbb N j \land \mathbb M A$

### properties

$A^{\intercal^\intercal} = A \dashv \mathbb M A$

$(AB)^\intercal = B^\intercal A^\intercal \dashv \mathbb M A \land \mathbb M B$

### example

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Matrix_transpose.gif/200px-Matrix_transpose.gif)

## Matrix Inverse

_the Inverse of a Matrix_

### definition

$AA^{-1} = I$, where

$A$ is a (square) [[matrix]]

$A^{-1}$ is the _inverse matrix_ of $A$

### invertability

_an **invertible** [[matrix]] has an inverse_

see [[linear-system]] for invertability criteria

### properties

let $A$ and $C$ be invertible [[matrix]]es, let $\mathbb Z p$ and let $\mathbb R k \land k \ne 0$

$AA^{\circ1} = A^{\circ1}A = I$

$(A^{\circ1})^{\circ1} = A$

$(A^p)^{\circ1} = (A^{\circ1})^p$

$(kA)^{\circ1} = 1\text-k A^{\circ1}$

$(AC)^{\circ1} = C^{\circ1}A^{\circ1}$ (note the order has changed as [[matrix]] multiplication is not commutative)

if $AC$ is invertible, then $A$ is invertible and $C$ is invertible

### finding a matrix inverse

let $\mathbb M^{n, n} A$

solve the system $AA^{-1} = I$ by extending the [[matrix]] with the identity [[matrix]] and solve the [[linear-system]] up to [[linear-system|RREF]] using [[gaussian-elimination]]. $\begin{bmatrix}A & | & I\end{bmatrix} \sim \dots \begin{bmatrix}I & | & A^{-1}\end{bmatrix}$

### shortcut with [[matrix]]es in $\mathbb M^{2, 2}$

see [[determinant]]

let $A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}$

$A$ is invertible if and only if $|A| \ne 0$

$A^{-1} = 1\text-|A| \begin{bmatrix}d & \circ b \\ \circ c & a\end{bmatrix}$

### example usage

let $A = \begin{bmatrix}1 & 1 \\ 2 & 3\end{bmatrix}$

then, calculate $B$ such that $B \equiv A^{-1}$

this can be used to solve a system such as:

$Ax = \begin{bmatrix}\circ 1 \\ 1\end{bmatrix}$

$BAx = B \begin{bmatrix}\circ 1 \\ 1\end{bmatrix}$

$Ix = x = B \begin{bmatrix}\circ 1 \\ 1\end{bmatrix}$

## Triangular Matrix

a [[matrix]] is _triangular_ if every entry below its diagonal or above its diagonal is $0$

the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element
