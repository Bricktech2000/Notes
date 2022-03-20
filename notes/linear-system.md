# Linear System

a set of [[linear-equation]]s

see [[gaussian-elimination]], [[math-notation]], [[matrix]]

### definitions

> the **general solution** is the set of all solutions to a system

> an **Inconsistent System** has no solutions

> a **Consistent System** has at least one solution

> a **Homogeneous System** has only zeros as constants on the right hand side. the zero vector is always a solution

> two matrices $A$, $B$ are **Row Equivalent** $A \sim B$ if $B$ can be obtained from $A$ by a finite sequence of _elementary row operations_

> a **Leading Variable** is the variable associated with a _pivot_ in a matrix in REF

### notation

the following linear system:

$x \cdot y \cdot 2z = 3$

$x \circ y \cdot z = 2$

$y \circ z = 1$

can be represented by the following Augmented [[matrix]]:

$\begin{bmatrix} 1 & 1 & 2 & | & 3 \\ 1 & \circ 1 & 1 & | & 2 \\ 0 & 1 & \circ 1 & | & 1\end{bmatrix}$

can be represented by the following [[vector-in-rn]] equation:

$x \begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix} \cdot y \begin{bmatrix}1 \\ \circ 1 \\ 1\end{bmatrix} \cdot z \begin{bmatrix}2 \\ 1 \\ \circ 1\end{bmatrix} = \begin{bmatrix}3 \\ 2 \\ 1\end{bmatrix}$

the system is _consistent_ if and only if $b$ &mdash; $\begin{bmatrix}3 \\ 2 \\ 1\end{bmatrix}$ is a [[linear-combination]] of the columns of $A$ &mdash; $A^{, j}$

## Elementary Operations

_operations we’re allowed to do and that don’t change the general solution of the system_

- add a multiple of a row to another row
- swap the position of two rows
- multiply a row by a non-zero scalar

## Row Echelon Form

_REF_

a [[matrix]] (augmented or not) is in REF if:

- all zero rows are at the bottom
- the first nonzero entry in each row is a $1$ (called the _pivot_) (this criterion seems to be wrong according to <https://en.wikipedia.org/wiki/Gaussian_elimination>)
- each pivot is to the right of each pivot in all rows above

### putting a [[matrix]] in REF

use [[gaussian-elimination]]

### determining the type of the general solution

- if the matrix contains a row in the form $\begin{bmatrix}0 & \dots & 0 & | & b\end{bmatrix} \land b \ne 0$, the system has no solutions
- else, if every column has a pivot, the system has one unique solution
- else, if there is a column with no pivot, the system has an infinite number of solutions

## Reduced Row Echelon Form

_RREF_

a matrix is in RREF if:

- the matrix is in REF
- each pivot is the only nonzero entry in its column

### finding the general solution

- if there is a unique solution, then the solution is the vector in the augmented column (ignore the $\begin{bmatrix}0 & \dots & 0 & | & 0\end{bmatrix}$ rows, if any)
- else, each pivot corresponds to one row of the augmented matrix. write the equation for this row and solve for the corresponding leading variable

### putting a [[matrix]] in RREF

use [[gaussian-elimination]]

## Theorems

> **theorem**: let $A$ be an $m \times n$ [[matrix]]. the following statements are equivalent:
>
> 1. every variable is a leading variable
> 2. there is a leading variable in every column of the [[linear-system|RREF]] of $A$
> 3. the system $Ax = 0$ has a unique solution
> 4. the columns of $A$ are [[linearly-independent]]
> 5. $Ker\ A = \{0\}$
> 6. $\dim Ker\ A = 0$
> 7. $rank\ A = n$

- $1 \to 2$

  each column represents a variable

  every variable is a leading variable $\to$ there is a leading $1$ in each column of the [[linear-system|RREF]] of $A$

- $2 \to 3$

  $Ax = 0$ is homogeneous $\to$ the system is consistent

  no free variables $\to$ there cannot be infinitely many solutions $\to$ it must have a single solution

- $3 \to 4$

  $Ax = 0$ has a unique solution $\to$ $x = O$ $\to$ $A^{,j}x^j \cdot \dots A^{,j}x^j = 0$ has a unique solution (all coefficients are $0$) $\to$ the columns of $A$ are [[linearly-independent]]

- $4 \to 5$

  the columns of $A$ are [[linearly-independent]] $\to$ $Ax = 0$ has a unique solution ($x = O$) $\to$ the [[matrix|nullspace]] of $A$ is the set containing the zero [[vector]]

- $5 \to 6$

  the [[matrix|nullspace]] of $A$ is the [[zero-space]] $\to$ the dimension of the [[zero-space]] is $0$

- $6 \to 7$

  $\dim Null\ A \cdot rank\ A = \text{number of columns in } A$ (see [[matrix]]) $\to$ as $\dim Null\ A = 0$, $rank\ A = \text{number of columns in } A = n$

- $7 \to 1$

  the [[matrix|rank]] of a [[matrix]] is the number leading variables in the matrix

  $rank\ A = n$ and $A$ has $n$ columns $\to$ every variable is a leading variable

> **theorem**: let $A$ be an $n \times n$ [[matrix]]. the following statements are equivalent:
>
> 1. $rank\ A = n$
> 2. every linear system of the form $Ax = b$ has a unique solution
> 3. the [[linear-system|RREF]] of $A$ is the identity [[matrix]]
> 4. $Ker\ A = \{0\}$
> 5. $Col\ A = \R^n$
> 6. $Row\ A = \R^n$
> 7. $Row\ A = \R^n$
> 8. the columns of $A$ are [[linearly-independent]]
> 9. the rows of $A$ are [[linearly-independent]]
> 10. the columns of $A$ form a [[basis]] for $\R^n$
> 11. the rows of $A$ form a [[basis]] for $\R^n$
