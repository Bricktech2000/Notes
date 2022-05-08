# Linear System

a set of [[linear-equation]]s

see [[row-reduction]], [[math-notation]], [[matrix]]

### definitions

> the **general solution** is the [[set]] of all solutions to a system

> an **Inconsistent System** has no solutions

> a **Consistent System** has at least one solution

> a **Homogeneous System** has only zeros as constants on the right hand side. the zero vector is always a solution

> two matrices $A$, $B$ are **Row Equivalent** $A \sim B$ if $B$ can be obtained from $A$ by a finite sequence of _elementary row operations_

> a **Leading Variable** is the variable associated with a _pivot_ in a matrix in [[REF]]

### notation

the following linear system:

$x \cdot y \cdot 2z = 3$

$x \circ y \cdot z = 2$

$y \circ z = 1$

can be represented by the following _augmented [[matrix]]_:

$\begin{bmatrix} 1 & 1 & 2 & | & 3 \\\  1 & \circ 1 & 1 & | & 2 \\\  0 & 1 & \circ 1 & | & 1\end{bmatrix}$

can be represented by the following [[vector-in-rn]] equation:

$x \begin{bmatrix}1 \\\  1 \\\  0\end{bmatrix} \cdot y \begin{bmatrix}1 \\\  \circ 1 \\\  1\end{bmatrix} \cdot z \begin{bmatrix}2 \\\  1 \\\  \circ 1\end{bmatrix} = \begin{bmatrix}3 \\\  2 \\\  1\end{bmatrix}$

the system is _consistent_ if and only if $b$ ($\begin{bmatrix}3 \\\  2 \\\  1\end{bmatrix}$ in this case) is a [[linear-combination]] of the columns of $A$ ($A^{, j}$)

## Elementary Operations

_operations we’re allowed to do and that don’t change the general solution of the system_

- add a multiple of a row to another row
- swap the position of two rows
- multiply a row by a non-zero scalar

## Row Echelon Form

_REF_

a [[matrix]] (augmented or not) is in [[REF]] if:

- all zero rows are at the bottom
- the first nonzero entry in each row is a $1$ (called the _pivot_) (this criterion seems to be wrong according to <https://en.wikipedia.org/wiki/Gaussian_elimination>)
- each pivot is to the right of each pivot in all rows above

### putting a [[matrix]] in [[REF]]

use [[row-reduction]]

### determining the type of the general solution

- if the [[matrix]] contains a row in the form $\begin{bmatrix}0 & \dots & 0 & | & b\end{bmatrix} \land b \ne 0$, the system has no solutions
- else, if every column has a pivot, the system has one unique solution
- else, if there is a column with no pivot, the system has an infinite number of solutions

## Reduced Row Echelon Form

_RREF_

a [[matrix]] is in [[RREF]] if:

- the [[matrix]] is in [[REF]]
- each pivot is the only nonzero entry in its column

### finding the general solution

- if there is a unique solution, then the solution is the [[vector]] in the augmented column (ignore the $\begin{bmatrix}0 & \dots & 0 & | & 0\end{bmatrix}$ rows, if any)
- else, each pivot corresponds to one row of the augmented [[matrix]]. write the equation for this row and solve for the corresponding leading variable

### putting a [[matrix]] in [[RREF]]

use [[row-reduction]]

## Augmented Matrix

a [[linear-system]] can be represented using an augmented [[matrix]]

### determining the type of the general solution

let $\begin{bmatrix}A & | & b\end{bmatrix}$ be an augmented [[matrix]].

notation [[todo]]

- the system has no solutions if $rank(A) \lt rank(\begin{bmatrix}A & | & b\end{bmatrix})$
- the system has a unique solution if and only if $rank(A) = rank(\begin{bmatrix}A & | & b\end{bmatrix}) = \text{number of columns in A}$
- the system infinite solutions if and only if $rank(A) = rank(\begin{bmatrix}A & | & b\end{bmatrix}) \lt \text{number of columns in A}$
