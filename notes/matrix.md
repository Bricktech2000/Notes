# Matrix

see [[math notation]]

**definition** _formally in my [[math notation]]_ a [[matrix]] in $\mathbb R^{m, n}$ is a [[set theory]]etical [[function]] with domain at least $\braket{x, y} \rightarrow \mathbb N x \land \mathbb N y \land 0 \le x < m \land 0 \le y < n$ that takes an [[ordered pair]] as an index and returns the element at that index

**notation**

$\begin{bmatrix}a & b \\\ c & d\end{bmatrix}$

## Multiplication by a Scalar

see [[matrix vector space]], [[vector space]]

**definition**

$(kA)^{i, j} = kA^{i, j} \dashv \mathbb N i \land \mathbb N j \land \mathbb R k \land \mathbb M A$

**properties**

_commutativity with [[scalar]]s_ $kA = Ak$

## Matrix Addition

see [[matrix vector space]], [[vector space]]

**definition**

$(A : B)^{i, j} = A^{i, j} : B^{i, j} \dashv \mathbb N i \land \mathbb N j \land \mathbb M^{m, n} A \land \mathbb M^{m, n} B$

## Matrix Multiplication

see [[dot product]], [[vector in rn]]

**definition**

$AB \ne \varnothing \equiv \mathbb M^{m, n}A \land \mathbb M^{n, p}B \land \mathbb M^{m, p}AB$ ($AB$ is defined if the number of columns in $A$ is equal to the number of rows in $B$. their product will be an $m$ by $p$ [[matrix]])

$(AB)^{i, j} = A^{i, }\ \dot\mid\ B^{, j} \dashv \mathbb N i \land \mathbb N j$, see [[dot product]]

intuitively, matrix multiplication is the [[dot product]] of **every row** of the first [[matrix]] by **every column** of the second [[matrix]]

**notation**

$AA = A2 = [A]2 \dashv \mathbb M A$

and therefore $AA \dots A = [A]n \land \mathbb N n \dashv \mathbb M A$

**properties**

_not commutative_ $AB = BA \not\dashv \mathbb M A \land \mathbb M B$ or $AB \ne BA \land \mathbb M A \land \mathbb M B$

$AB = 0 \not\vdash A = 0 \lor B = 0$ (it can happen that $AB = 0$, but $A \ne 0$ and $B \ne 0$) ($AB$ being equal to $0$ does not imply that $A = 0$ or that $B = 0$)

$AC = BC \land C \ne 0 \not\vdash A = B$ ($AC = BC$ and $C \ne 0$ does not imply that $A = B$)

_associative_ $(AB)C = A(BC)$

_distributive_ $A(B : C) = AB : AC$

_distributive_ $(B : C)A = BA : CA$

_associative with [[scalar]]s_ $k(AB) = (kA)B = A(kB)$

**applications**

matrix multiplication can be used to represent a [[linear system]] of [[linear equation]]s:

$\begin{bmatrix}1 & 2 & 3 \\\  4 & 5 & 6\end{bmatrix}\begin{bmatrix}x \\\  y \\\  z\end{bmatrix}$

matrix multiplication can be used to represent any [[linear transformation]]

## Identity Matrix

**definition**

$(I^{a, b} = 1 \land a = b) \lor (I^{a, b} = 0 \land a \ne b) \dashv \mathbb N a \land \mathbb N b \land \mathbb M^{n, n} I$

**examples**

$\begin{bmatrix}1 & 0 \\\  0 & 1\end{bmatrix}$

$\begin{bmatrix}1 & 0 & 0 \\\  0 & 1 & 0 \\\  0 & 0 & 1\end{bmatrix}$

**properties**

$AI = A \land IA = A \dashv \mathbb M A$

## Zero Matrix

see [[matrix vector space]], [[vector space]]

**definition**

$O^{a, b} = 0 \dashv \mathbb N a \land \mathbb N b \land \mathbb M^{n, m} O$

**examples**

$\begin{bmatrix}0 & 0 \\\  0 & 0\end{bmatrix}$

$\begin{bmatrix}0 & 0 & 0 \\\  0 & 0 & 0 \\\  0 & 0 & 0 \\\  0 & 0 & 0\end{bmatrix}$

**properties**

$A_{m, n}O_{n, p} = O_{m, p} \dashv \mathbb M^{n, p} O_{n, p} \land \mathbb M^{m, p} O_{m, p} \land \mathbb M^{m, n} A_{m, n}$

$O_{q, m}A_{m, n} = O_{q, n} \dashv \mathbb M^{q, m} O_{q, m} \land \mathbb M^{q, n} O_{q, n} \land \mathbb M^{m, n} A_{m, n}$

## Rank of a Matrix

_the number of pivots in any [[REF]] of the [[matrix]]_

**notation**

$rank\ A$, where

- $A$ is the [[matrix]] to find the rank of

## Matrix Vector Spaces

_Null Space (Nullspace, Kernel), Column Space, Row Space_

**notations**

_kernel_ $Ker\ A \equiv Null\ A$

_column space_ $Col\ A$

_row space_ $Row\ A$

**definitions**

_kernel_ $(Ker\ A)\ x \equiv (Null\ A)\ x \equiv Ax = O \land \mathbb M^{m, n}A \land \mathbb M^{n, 1} x$

_column space_ $Col\ A = \operatorname{span} A^{, n} \dashv \mathbb N n$

_row space_ $Row\ A = \operatorname{span} A^{n,} \dashv \mathbb N n$

**procedure** _computing the kernel of a [[matrix]]_ use [[row reduction]]

**theorems**

the Null Space, Row Space and Column Space of a [[matrix]] are always [[vector space]]s

$\text{number of free variables in } A : \text{number of pivots in } A = \text{number of columns in } A$

$\dim Null\ A = \text{number of free variables in } A$

$rank\ A = \text{number of pivots in } A$

the nonzero rows in any [[REF]] of a [[matrix]] $A$ forms a [[basis]] for $Row\ A$. therefore, $\dim Row\ A = rank\ A$ (see rank of a [[matrix]])

if $A$ and $B$ are row-equivalent, then $Row\ A = Row\ B$, see [[linear system]]

the [[span]]ning [[set]] of $Null\ A$ obtained from applying [[row reduction]] on the system $Ax = O$ is a [[basis]] for $Null\ A$

$Row\ A$ does not change when applying elementary operations on the rows of $A$, see [[linear system]]

**properties**

$Col\ A = Row\ A^\intercal \land Row\ A = Col\ A^\intercal \dashv \mathbb M A$, see transpose [[matrix]]

**applications**

row spaces can be used to find a [[basis]] for a [[span]]ning [[set]] of vectors through [[row reduction]]

the [[basis]] for the row space of a [[matrix]] can be found by applying [[row reduction]] and [[span]]ning the **row-reduced columns** in the [[REF]] form of the [[matrix]]

the [[basis]] for the column space of a [[matrix]] can be found by applying [[row reduction]] and [[span]]ning the **original columns** that became pivots in the [[REF]] form of the [[matrix]]

the same can be said for $Col\ A$

> **example** _transforming a [[vector space]] into the null space of a certain [[matrix]]_
>
> let $W = \operatorname{span} \braket{\braket{\ (1, 0, 0, 1), (1, 1, 1, 0), (2, 1, \cdot 1, 1)\ }}$
>
> after solving the [[linear system]], we get $W\ (x, y, z, w) \equiv \cdot x : y : w = 0$. therefore, $W$ is the null space of $A = \begin{bmatrix}\cdot 1 & 1 & 0 & 1\end{bmatrix}$

## Transpose Matrix

_the transpose of a [[matrix]]_

_flips a [[matrix]] around its diagonal_

> **note** the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element (triplicate)

**definition**

$(A^\intercal)^{i, j} = (A)^{j, i} \dashv \mathbb N i \land \mathbb N j \land \mathbb M A$

**properties**

$(A^\intercal)^\intercal = A \dashv \mathbb M A$

$(AB)^\intercal = B^\intercal A^\intercal \dashv \mathbb M A \land \mathbb M B$

**representation** ![[200px-Matrix_transpose.gif]] &mdash; <https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Matrix_transpose.gif/200px-Matrix_transpose.gif>

## Matrix Inverse

_the inverse of a [[matrix]]_

**definition**

$AA^- = A^-A = I \dashv \mathbb M A$, where

- $A$ is a square [[matrix]]
- $A^-$ is the _inverse matrix_ of $A$

### Invertability

**definition** an _invertible matrix_ has a corresponding inverse [[matrix]]

see theorems below for invertability criteria

**properties**

let $A$ and $C$ be invertible [[matrix]]es, let $\mathbb Z p$ and let $\mathbb R k \land k \ne 0$. then,

$AA^- = A^-A = I$

$(A^-)^- = A$

$(A^p)^- = (A^-)^p$

$(kA)^- = \text-k \mid A^-$ (see [[improved expression evaluation]])

$(AC)^- = C^-A^-$

> **note** in the equation above, the order of the [[matrix]]es has changed. this is significant as [[matrix]] multiplication is not commutative

if $AC$ is invertible, then $A$ is invertible and $C$ is invertible

> **procedure** _computing the inverse of a [[matrix]]_
>
> let $\mathbb M^{n, n} A$
>
> solve the system $AA^- = I$ by extending the [[matrix]] with the identity [[matrix]] and solve the [[linear system]] up to [[RREF]] using [[row reduction]]. $\begin{bmatrix}A & | & I\end{bmatrix} \sim \dots \begin{bmatrix}I & | & A^-\end{bmatrix}$

> **procedure** _computing the inverse of a $2$ by $2$ [[matrix]]_
>
> see [[determinant]]
>
> let $A = \begin{bmatrix}a & b \\\  c & d\end{bmatrix}$
>
> $A$ is invertible if and only if $|A| \ne 0$
>
> $A^- = - |A|\ \mid\ \begin{bmatrix}d & \cdot b \\\  \cdot c & a\end{bmatrix}$

**applications** _using a matrix inverse to solve a linear system_

let $A = \begin{bmatrix}1 & 1 \\\  2 & 3\end{bmatrix}$

then, calculate $B$ such that $B \equiv A^-$

this can be used to solve a [[linear system]] such as:

$Ax = \begin{bmatrix}\cdot 1 \\\ 1\end{bmatrix}$

$BAx = B \begin{bmatrix}\cdot 1 \\\ 1\end{bmatrix}$

$Ix = x = B \begin{bmatrix}\cdot 1 \\\ 1\end{bmatrix}$

## Triangular Matrix

**definition** a [[matrix]] is said to be _triangular_ if every entry below its diagonal **or** above its diagonal is $0$

> **note** the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element (triplicate)

## Diagonal Matrix

**definition** a [[matrix]] is said to be _diagonal_ if every entry below its diagonal **and** above its diagonal is $0$

> **note** the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element (triplicate)

let $D$ be a diagonal [[matrix]]

**applications**

$[D]x$ can be calculated by raising every entry of $D$ to the power $x$

## Diagonalizable Matrix

see [[eigenvector]]

**definition** an $n$ by $n$ [[matrix]] $A$ is said to be _diagonalizable over the reals_ if there exists a [[basis]] of $\mathbb R^n$ consisting entirely of [[eigenvector]]s of $A$

a [[matrix]] is _diagonalizable_ if and only if the geometic [[multiplicity]] of an [[eigenvalue]] is equal to the algebraic [[multiplicity]] of said [[eigenvalue]], for every [[eigenvalue]] of the [[matrix]] (see [[eigenvector and eigenvalue]])

> **note** a [[matrix]] may also be diagonalizable over other [[number field]]s such as the [[set]] of [[complex]] numbers $\mathbb C$

> **note** some [[matrix]]es do not have "enough" real [[eigenvalue]]s or "enough" [[eigenvector]]s to be diagonalizable

> **example** the [[matrix]] $A = \begin{bmatrix}1 & 2 \\\ 2 & 1\end{bmatrix}$ is diagonalizable over the reals as $\braket{\braket{\ (1, 1), (1, \cdot 1)\ }}$ is a [[basis]] of $\mathbb R^2$ consisting entirely of [[eigenvector]]s of $A$

> **example** the [[matrix]] $A = \begin{bmatrix}1 & 1 \\\ \cdot 1 & 1\end{bmatrix}$ is not diagonalizable over the reals as it does not have any real [[eigenvalue]]s

> **example** the [[matrix]] $A = \begin{bmatrix}3 & 1 \\\ 0 & 3\end{bmatrix}$ is not diagonalizable over the reals as it only has one [[eigenvalue]], and therefore only one set of [[linearly dependent]] [[eigenvector]]s (see [[eigenvector and eigenvalue]])

> **example** the [[matrix]] $A = \begin{bmatrix}1 & 0 \\\ 0 & 1\end{bmatrix}$ is diagonalizable over the reals as, even though $A$ has a single [[eigenvalue]] $\lambda = 1$, its [[eigenspace]] [[span]]s $\mathbb R^2$. this is the case for both $A = I \land \lambda = 1$ and $A = O \land \lambda = 0$
>
> > **proof** let $A = I \land \lambda = 1 \land E_1 = x$. we then have $O = A \cdot \lambda I \mid x = I \cdot 1I \mid E_1= O \mid E_1$. therefore, $E_1 \equiv \mathbb R^2$. see [[eigenvector and eigenvalue]]

> **example** let $\mathbb M^{n, n} A \land \mathbb N n$ and suppose $A$ has $n$ distinct [[eigenvalue]]s. deduce that $A$ is diagonalizable over the reals
>
> > **proof** $A$ has at most $n$ [[eigenvalue]]s $\to$ the algebraic [[multiplicity]] of every [[eigenvalue]] of $A$ is $1$ as they are all distinct and must be greater than $1$ $\to$ the geometric [[multiplicity]] of every [[eigenvalue]] of $A$ is $1$ as it must be greater than $1$ and less than its algebraic [[multiplicity]] $\to$ all algebraic [[multiplicity]]es and geometric [[multiplicity]]es are equal $\to$ $A$ is diagonalizable. see [[eigenvector and eigenvalue]]

## [[eigenvector and eigenvalue]]s

## theorems

see [[linear system]]

**theorem**

let $\mathbb M^{m, n}A$ (see [[matrix]]). the following [[logic statement]]s are equivalent:

- every [[variable]] is a leading [[variable]]
- there is a leading [[variable]] in every column of the [[RREF]] of $A$
- the system $Ax = O$ has a unique solution
- the columns of $A$ are [[linearly independent]]
- $Ker\ A = \braket{\braket{0}}$
- $\dim Ker\ A = 0$
- $rank\ A = n$

see [[linear system theorem proof]]

**theorem**

let $\mathbb M^{n, n} A$ (see [[matrix]]). the following [[logic statement]]s are equivalent:

> **note** all [[logic statement]]s below are valid for both $A$ and $A^\intercal$, see transpose [[matrix]]

- $rank\ A = n$
- every linear system of the form $Ax = b$ has a unique solution
- the [[RREF]] of $A$ is the identity [[matrix]]
- $Ker\ A = \braket{\braket{0}}$
- $Col\ A = \mathbb R^n$
- $Row\ A = \mathbb R^n$
- the columns of $A$ are [[linearly independent]]
- the rows of $A$ are [[linearly independent]]
- the columns of $A$ form a [[basis]] for $\mathbb R^n$
- the rows of $A$ form a [[basis]] for $\mathbb R^n$
- $A$ is an invertible [[matrix]]
- $\det A \ne 0$

<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
