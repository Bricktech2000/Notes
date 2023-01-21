# Matrix

**see** [[math notation]], [[eigen]]

**definition** _formally in my [[math notation]]_ a [[matrix]] is a [[set theory]]etical [[function]] that takes two [[natural]] indices and returns the element at that index

**notation**

$\begin{bmatrix}a & b \\\ c & d\end{bmatrix}$

## Vector Space

**notation** _in my [[math notation]]_ $\mathbb M^{m, n}$

**notation** _in [[math notation]]_ $M_{m\ n}(\mathbb R)$

### Multiplication by Scalar

**see** [[vector]], [[vector space]]

**definition**

$kA$

**properties**

_commutativity with [[scalar]]s_ $kA = Ak$

### Addition

**see** [[vector]], [[vector space]]

**definition**

$A : B$

## Multiplication

#todo mm

**see** [[dot product]], [[vector in rn]]

**definition**

$AB = \,:(A\ \circ)(\rho\ B\ \circ)$, see [[dot product]]

intuitively, matrix multiplication is the [[dot product]] of **every row** of the first [[matrix]] by **every column** of the second [[matrix]]

**properties**

$AB + \varnothing =\!= \mathbb M^{m, n}A \land \mathbb M^{n, p}B \land \mathbb M^{m, p}AB$ ($AB$ is defined if the number of columns in $A$ is equal to the number of rows in $B$. their product will be an $m$ by $p$ [[matrix]])

_not commutative_ $\times (\mathbb M A \land \mathbb M B < AB = BA)$

$\times (AB = 0 < A = 0 \lor B = 0)$ (it can happen that $AB = 0$, but $A + 0$ and $B + 0$) ($AB$ being equal to $0$ does not imply that $A = 0$ or that $B = 0$)

$\times (AC = BC \land C + 0 < A = B)$ ($AC = BC$ and $C + 0$ does not imply that $A = B$)

_associative_ $(AB)C = A(BC)$

_distributive_ $A(B : C) = AB : AC$

_distributive_ $(B : C)A = BA : CA$

_associative with [[scalar]]s_ $k(AB) = (kA)B = A(kB)$

**applications**

[[matrix#multiplication]] can be used to represent a [[linear system]] of [[linear equation]]s. matrix-vector products can be seen as yielding a [[linear combination]] of the columns of the [[matrix]]:

$\begin{bmatrix} 1 & 2 & 3 \\\  4 & 5 & 6 \end{bmatrix} \begin{bmatrix} x \\\  y \\\  z \end{bmatrix} = x \begin{bmatrix} 1 \\\ 4 \end{bmatrix} : y \begin{bmatrix} 2 \\\ 5 \end{bmatrix} : z \begin{bmatrix} 3 \\\ 6 \end{bmatrix}$

> **equivalence** _[[matrix#multiplication]] and [[linear transformation]]s_

## Identity Matrix

**definition**

$I = i\ j \rightarrow (i = j)$

**properties**

$AI = A \land IA = A$

## Zero Matrix

**see** [[vector]], [[vector space]]

**definition**

$O = i\ j \rightarrow 0$

**properties**

$A_{m, n}O_{n, p} = O_{m, p} > \mathbb M^{n, p} O_{n, p} \land \mathbb M^{m, p} O_{m, p} \land \mathbb M^{m, n} A_{m, n}$

$O_{q, m}A_{m, n} = O_{q, n} > \mathbb M^{q, m} O_{q, m} \land \mathbb M^{q, n} O_{q, n} \land \mathbb M^{m, n} A_{m, n}$

## Rank

_the number of pivots in any [[linear system#row echelon form]] of the [[matrix]]_

**notation** $\operatorname{rank}\ A$

## Element Count

**notation** $\#\ M$

**definition** the _element count_ of a [[matrix]] is the total number of elements in the [[matrix]]

> **example** let $M = \begin{bmatrix}1 & 2 & 3 \\\ 4 & 5 & 6\end{bmatrix}$. then, $\mathbb M^{2, 3} M \land \#\ M = 2 \mid 3 = 6$

## Null Space

## Column Space

## Row Space

**notations**

_null space_ $\mathcal N A$

_column space_ $\mathcal C A$

_row space_ $\mathcal R A$

**definitions**

_kernel_ $(\mathcal N A)\ x =\!= Ax = O \land \mathbb M^{m, n}A \land \mathbb M^{n, 1} x$

_column space_ $\mathcal C A = \operatorname{span} \braket{\braket{A^{\circ, 0}, A^{\circ, 1}, \dots}}$

_row space_ $\mathcal R A = \operatorname{span} \braket{\braket{A^{0, \circ}, A^{1, \circ}, \dots}}$

**procedure** _computing the null space of a [[matrix]]_ use [[row reduction]]

**theorems**

the [[matrix#null space]], [[matrix#row space]] and [[matrix#column space]] of a [[matrix]] are always [[vector space]]s

$\text{number of free variables in \(A\)} : \text{number of pivots in \(A\)} = \text{number of columns in \(A\)}$

$\dim \mathcal N A = \text{number of free variables in \(A\)}$

$\operatorname{rank}\ A = \text{number of pivots in \(A\)}$

the nonzero rows in any [[linear system#row echelon form]] of a [[matrix]] $A$ forms a [[basis]] for $\mathcal R A$. therefore, $\dim \mathcal R A = \operatorname{rank}\ A$, see [[matrix#rank]]

if $A$ and $B$ are row-equivalent, then $\mathcal R A = \mathcal R B$, see [[linear system]]

the [[span]]ning [[set]] of $\mathcal N A$ obtained from applying [[row reduction]] on the system $Ax = O$ is a [[basis]] for $\mathcal N A$

$\mathcal R A$ does not change when applying [[linear system#elementary operation]]s on the rows of $A$

**properties**

$\mathcal C A = \mathcal R (\rho\ A) \land \mathcal R A = \mathcal C (\rho\ A)$, see [[matrix#transpose]]

**applications**

[[matrix#row space]]s can be used to find a [[basis]] for a [[span]]ning [[set]] of [[vector]]s through [[row reduction]]

the [[basis]] for a [[matrix#row space]] can be found by applying [[row reduction]] and [[span]]ning the **row-reduced columns** in the [[linear system#row echelon form]] of the [[matrix]]

the [[basis]] for a [[matrix#column space]] of a [[matrix]] can be found by applying [[row reduction]] and [[span]]ning the **original columns** that became pivots in the [[linear system#row echelon form]] of the [[matrix]]

the same can be said for $\mathcal C A$

> **example** _transforming a [[vector space]] into the [[matrix#null space]] of a certain [[matrix]]_
>
> let $W = \operatorname{span} \braket{\braket{\ (1, 0, 0, 1), (1, 1, 1, 0), (2, 1, \cdot 1, 1)\ }}$
>
> after solving the [[linear system]], we get $W\ (x, y, z, w) =\!= \cdot x : y : w = 0$. therefore, $W$ is the [[matrix#null space]] of $A = \begin{bmatrix}\cdot 1 & 1 & 0 & 1\end{bmatrix}$

## Diagonal

_the diagonal of a [[matrix]]_

**definition** the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element

## Transpose

_the transpose of a [[matrix]]_

_flips a [[matrix]] around its [[matrix#diagonal]]_

**notation** $\rho\ A$

**definition** $\rho\ A$

**properties**

$\rho\ \rho\ A = A$

$\rho\ AB = \rho\ B \mid \rho\ A$ #todo mm

## Conjugate Transpose

_the [[complex#conjugate]] of every entry of the [[matrix#transpose]] of a [[matrix]]_

**aka** _Hermitian transpose, adjoint matrix, transjugate_

**definition**

$\operatorname{conj}\ \rho\ A$, where

- $A$ is the [[matrix]] to find the [[matrix#conjugate transpose]] of
- $\operatorname{conj}$ is the [[complex#conjugate]] [[function]]
- $\rho$ is the [[matrix#transpose]] [[operator]]

**properties**

let a [[matrix]] of [[real]]s $A$. then, $\operatorname{conj} \rho\ A = \rho\ A$

## Inverse

#todo mm

_the inverse of a [[matrix]]_

**definition**

$AA^- = A^-A = I > \mathbb M A$, where

- $A$ is a square [[matrix]]
- $A^-$ is the _inverse matrix_ of $A$

### Invertability

**definition** an _invertible matrix_ has a corresponding [[matrix#inverse]]

**see** theorems below for invertability criteria

**properties**

let $A$ and $C$ be invertible [[matrix]]es, let $\mathbb Z p$ and let $\mathbb R k \land k + 0$. then,

$AA^- = A^-A = I$

$(A^-)^- = A$

$(A^p)^- = (A^-)^p$

$(kA)^- = \text-k \mid A^-$ (see [[improved expression evaluation]])

$(AC)^- = C^-A^-$

> **note** in the equation above, the order of the [[matrix]]es has changed. this is significant as [[matrix#multiplication]] is not commutative

if $AC$ is invertible, then $A$ is invertible and $C$ is invertible

> **procedure** _computing the [[matrix#inverse]] of a [[matrix]]_
>
> let $\mathbb M^{n, n} A$
>
> solve the system $AA^- = I$ by extending the [[matrix]] with the [[matrix#identity matrix]] and solve the [[linear system]] up to [[linear system#reduced row echelon form]] using [[row reduction]]. $\begin{bmatrix}A & | & I\end{bmatrix} \sim \cdots \begin{bmatrix}I & | & A^-\end{bmatrix}$

> **procedure** _computing the [[matrix#inverse]] of a $2$ by $2$ [[matrix]]_
>
> **see** [[determinant]]
>
> let $A = \begin{bmatrix}a & b \\\  c & d\end{bmatrix}$
>
> $A$ is invertible if and only if $\det A + 0$
>
> $A^- = - \det A\ \mid\ \begin{bmatrix}d & \cdot b \\\  \cdot c & a\end{bmatrix}$

**applications**

> **example** _using a [[matrix#inverse]] to solve a [[linear system]]_
>
> let $A = \begin{bmatrix}1 & 1 \\\  2 & 3\end{bmatrix}$
>
> then, calculate $B$ such that $B = A^-$
>
> this can be used to solve a [[linear system]] such as:
>
> $Ax = \begin{bmatrix}\cdot 1 \\\ 1\end{bmatrix}$
>
> $BAx = B \begin{bmatrix}\cdot 1 \\\ 1\end{bmatrix}$
>
> $Ix = x = B \begin{bmatrix}\cdot 1 \\\ 1\end{bmatrix}$

## Triangular Matrix

**definition** a [[matrix]] is said to be _triangular_ if every entry below its [[matrix#diagonal]] **or** above its [[matrix#diagonal]] is $0$

## Diagonal Matrix

**definition** a [[matrix]] is said to be _diagonal_ if every entry below its [[matrix#diagonal]] **and** above its [[matrix#diagonal]] is $0$

**applications**

$[D]x$ can be calculated by raising every entry of $D$ to the power $x$ #todo mm

## Diagonalizable Matrix

**see** [[eigen#vector]]

**definition** an $n$ by $n$ [[matrix]] $A$ is said to be _diagonalizable over the reals_ if there exists a [[basis]] of $\mathbb R^n$ consisting entirely of [[eigen#vector]]s of $A$

a [[matrix]] is _diagonalizable_ if and only if the geometic [[eigen#multiplicity]] of an [[eigen#value]] is equal to the algebraic [[eigen#multiplicity]] of said [[eigen#value]], for every [[eigen#value]] of the [[matrix]]

> **note** a [[matrix]] may also be diagonalizable over other [[field]]s such as the [[set]] of [[complex]] numbers $\mathbb C$

> **note** some [[matrix]]es do not have "enough" real [[eigen#value]]s or "enough" [[eigen#vector]]s to be diagonalizable

> **example** the [[matrix]] $A = \begin{bmatrix}1 & 2 \\\ 2 & 1\end{bmatrix}$ is diagonalizable over the reals as $\braket{\braket{\ (1, 1), (1, \cdot 1)\ }}$ is a [[basis]] of $\mathbb R^2$ consisting entirely of [[eigen#vector]]s of $A$

> **example** the [[matrix]] $A = \begin{bmatrix}1 & 1 \\\ \cdot 1 & 1\end{bmatrix}$ is not diagonalizable over the reals as it does not have any real [[eigen#value]]s

> **example** the [[matrix]] $A = \begin{bmatrix}3 & 1 \\\ 0 & 3\end{bmatrix}$ is not diagonalizable over the reals as it only has one [[eigen#value]], and therefore only one set of [[linearly dependent]] [[eigen#vector]]s

> **example** the [[matrix]] $A = \begin{bmatrix}1 & 0 \\\ 0 & 1\end{bmatrix}$ is diagonalizable over the reals as, even though $A$ has a single [[eigen#value]] $\lambda = 1$, its [[eigen#space]] [[span]]s $\mathbb R^2$. this is the case for both $A = I \land \lambda = 1$ and $A = O \land \lambda = 0$
>
> > **proof** let $A = I \land \lambda = 1 \land E_1 = x$. we then have $O = A \cdot \lambda I \mid x = I \cdot 1I \mid E_1= O \mid E_1$. therefore, $E_1 = \mathbb R^2$. see [[eigen]]

> **example** let $\mathbb M^{n, n} A \land \mathbb N n$ and suppose $A$ has $n$ distinct [[eigen#value]]s. deduce that $A$ is diagonalizable over the reals
>
> > **proof** $A$ has at most $n$ [[eigen#value]]s $\to$ the algebraic [[eigen#multiplicity]] of every [[eigen#value]] of $A$ is $1$ as they are all distinct and must be greater than $1$ $\to$ the geometric [[eigen#multiplicity]] of every [[eigen#value]] of $A$ is $1$ as it must be greater than $1$ and less than its algebraic [[eigen#multiplicity]] $\to$ all algebraic [[eigen#multiplicity]]es and geometric [[eigen#multiplicity]]es are equal $\to$ $A$ is diagonalizable. see [[eigen]]

## theorems

**see** [[linear system]]

**theorem**

let $\mathbb M^{m, n}A$. the following [[logic statement]]s are equivalent:

- every [[variable]] is a leading [[variable]]
- there is a leading [[variable]] in every column of the [[linear system#reduced row echelon form]] of $A$
- the system $Ax = O$ has a unique solution
- the columns of $A$ are [[linearly independent]]
- $\mathcal N A = \braket{\braket{O}}$
- $\dim \mathcal N A = 0$
- $\operatorname{rank}\ A = n$

**see** [[linear system theorem proof]]

**theorem**

let $\mathbb M^{n, n} A$ (see [[matrix]]). the following [[logic statement]]s are equivalent:

> **note** all [[logic statement]]s below are valid for both $A$ and $\rho\ A$, see [[matrix#transpose]]

> **note** thinking of [[matrix]]es as [[linear transformation]]s makes the following [[logic statement]]s easier to understand intuitively

- $\operatorname{rank}\ A = n$
- every [[linear system]] of the form $Ax = b$ has a unique solution
- the [[linear system#reduced row echelon form]] of $A$ is the [[matrix#identity matrix]]
- $\mathcal N A = \braket{\braket{O}}$
- $\mathcal C A = \mathbb R^n$
- $\mathcal R A = \mathbb R^n$
- the columns of $A$ are [[linearly independent]]
- the rows of $A$ are [[linearly independent]]
- the columns of $A$ form a [[basis]] for $\mathbb R^n$
- the rows of $A$ form a [[basis]] for $\mathbb R^n$
- $A$ is an invertible [[matrix]]
- $\det A + 0$, see [[determinant#intuition]]
