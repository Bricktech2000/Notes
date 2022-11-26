# Linear System

a set of [[linear equation]]s

**see** [[row reduction]], [[math notation]], [[matrix]]

**definition** the _general solution_ is the [[set]] of all solutions to a system

**definition** an _inconsistent system_ has no solutions

**definition** a _consistent system_ has at least one solution

**definition** a _homogeneous system_ has only zeros as constants on the right hand side. the zero vector is always a solution

**definition** two [[matrix]]es $A$, $B$ are _row equivalent_ $A \sim B$ if $B$ can be obtained from $A$ by a finite sequence of [[linear system#elementary operation]]s

**definition** a _leading variable_ is the [[variable]] associated with a _pivot_ in a matrix in [[linear system#row echelon form]]

**notation**

the following linear system:

$x : y : 2z = 3$

$x \cdot y : z = 2$

$y \cdot z = 1$

can be represented by the following _augmented [[matrix]]_:

$\begin{bmatrix} 1 & 1 & 2 & | & 3 \\\  1 & \cdot 1 & 1 & | & 2 \\\  0 & 1 & \cdot 1 & | & 1\end{bmatrix}$

which can be represented by the following [[vector in rn]] equation:

$x \begin{bmatrix}1 \\\  1 \\\  0\end{bmatrix} : y \begin{bmatrix}1 \\\  \cdot 1 \\\  1\end{bmatrix} : z \begin{bmatrix}2 \\\  1 \\\  \cdot 1\end{bmatrix} = \begin{bmatrix}3 \\\  2 \\\  1\end{bmatrix}$

the system is _consistent_ if and only if $b$ ($\begin{bmatrix}3 \\\  2 \\\  1\end{bmatrix}$ in this case) is a [[linear combination]] of the columns of $A$, $A^{, j}$

## Elementary Operation

_operations that don’t change the general solution of a [[linear system]]_

- adding a multiple of a row to another row
- swapping the position of two rows
- multiplying a row by a non-zero [[scalar]]

## Row Echelon Form

> **aka** REF

**definition**

a [[matrix]] (augmented or not) is in [[linear system#row echelon form]] if all:

- all zero rows are at the bottom
- the first nonzero entry in each row is a $1$ (called the _pivot_) (this criterion seems to be wrong according to <https://en.wikipedia.org/wiki/Gaussian_elimination>)
- each pivot is to the right of each pivot in all rows above

> **procedure** _putting a [[matrix]] in [[linear system#row echelon form]]_ use [[row reduction]]

> **procedure** _determining the type of the general solution_
>
> - if the [[matrix]] contains a row in the form $\begin{bmatrix}0 & \cdots & 0 & | & b\end{bmatrix} \land b \ne 0$, the system has no solutions
> - else, if every column has a pivot, the system has one unique solution
> - else, if there is a column with no pivot, the system has an infinite number of solutions

## Reduced Row Echelon Form

> **aka** RREF

**definition** a [[matrix]] is in [[linear system#reduced row echelon form]] if all:

- the [[matrix]] is in [[linear system#row echelon form]]
- each pivot is the only nonzero entry in its column

> **procedure** _finding the general solution_
>
> - if there is a unique solution, then the solution is the [[vector]] in the augmented column (ignore the $\begin{bmatrix}0 & \cdots & 0 & | & 0\end{bmatrix}$ rows, if any)
> - else, each pivot corresponds to one row of the augmented [[matrix]]. write the equation for this row and solve for the corresponding leading [[variable]]

> **procedure** _putting a [[matrix]] in [[linear system#reduced row echelon form]]_ use [[row reduction]]

## Augmented Matrix

a [[linear system]] can be represented using an augmented [[matrix]]

> **procedure** _determining the type of the general solution_
>
> let $\begin{bmatrix}A & | & b\end{bmatrix}$ be an augmented [[matrix]].
>
> - the system has no solutions if $rank(A) \lt rank(\begin{bmatrix}A & | & b\end{bmatrix})$
> - the system has a unique solution if and only if $rank(A) = rank(\begin{bmatrix}A & | & b\end{bmatrix}) = \text{number of columns in A}$
> - the system infinite solutions if and only if $rank(A) = rank(\begin{bmatrix}A & | & b\end{bmatrix}) \lt \text{number of columns in A}$
