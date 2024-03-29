# Linear System

a set of [[linear equation]]s

**see** [[row reduction]], [[math notation]], [[matrix]]

**definition** the _general solution_ is the [[set]] of all solutions to a system

**definition** an _inconsistent system_ has no solutions

**definition** a _consistent system_ has at least one solution

**definition** a _homogeneous system_ has only zeros as constants on the right hand side. the zero vector is always a solution

**definition** two [[matrix]]es **`A`**, **`B`** are _row equivalent_ $A \sim B$ if **`B`** can be obtained from **`A`** by a finite sequence of [[linear system#elementary operation]]s

**definition** a _leading variable_ is the [[variable]] associated with a _pivot_ in a matrix in [[linear system#row echelon form]]

**notation**

the following linear system:

**`x : y : 2z = 3`**

**`x . y : z = 2`**

**`y . z = 1`**

can be represented by the following _augmented [[matrix]]_:

**`[]1 & 1 & 2 & || & 3 && 1 & .1 & 1 & || & 2 && 0 & 1 & .1 & || & 1[]`**

which can be represented by the following [[euclidean vector]] equation:

**`x[]1 && 1 && 0[] : y[]1 && .1 && 1[] : z[]2 && 1 && .1[] = []3 && 2 && 1[]`**

the system is _consistent_ if and only if **`b`** (**`[]3 && 2 && 1[]`** in this case) is a [[linear combination]] of the columns of **`A`** (**`rr A`**)

## Elementary Operation

_operations that don't change the general solution of a [[linear system]]_

- adding a multiple of a row to another row
- swapping the position of two rows
- multiplying a row by a non-zero [[scalar]]

## Row Echelon Form

**aka** _REF_

**definition**

a [[matrix]] (augmented or not) is in [[linear system#row echelon form]] if all:

- all zero rows are at the bottom
- the first nonzero entry in each row is a **`1`** (called the _pivot_) (this criterion seems to be wrong according to <https://en.wikipedia.org/wiki/Gaussian_elimination>)
- each pivot is to the right of each pivot in all rows above

> **procedure** _putting a [[matrix]] in [[linear system#row echelon form]]_ use [[row reduction]]

> **procedure** _determining the type of the general solution_
>
> - if the [[matrix]] contains a row of the form **`[]0 & ... & 0 & || & b[]`** with **`b + 0`**, the system has no solutions
> - else, if every column has a pivot, the system has one unique solution
> - else, if there is a column with no pivot, the system has an infinite number of solutions

## Reduced Row Echelon Form

**aka** _RREF_

**definition** a [[matrix]] is in [[linear system#reduced row echelon form]] if all:

- the [[matrix]] is in [[linear system#row echelon form]]
- each pivot is the only nonzero entry in its column

> **procedure** _finding the general solution_
>
> - if there is a unique solution, then the solution is the [[vector]] in the augmented column (ignore the **`[]0 & ... & 0 & || & 0[]`** rows, if any)
> - else, each pivot corresponds to one row of the augmented [[matrix]]. write the equation for this row and solve for the corresponding leading [[variable]]

> **procedure** _putting a [[matrix]] in [[linear system#reduced row echelon form]]_ use [[row reduction]]

## Augmented Matrix

a [[linear system]] can be represented using an augmented [[matrix]]

> **procedure** _determining the type of the general solution_
>
> let **`[]A & || & b[]`** be an augmented [[matrix]].
>
> - the system has no solutions if **`"rank" A -| "rank" []A & || & b[] . 1`**
> - the system has a unique solution if and only if **`"rank" A = "rank" []A & || & b[] = "number of columns in" A`**
> - the system has infinite solutions if and only if **`"rank" A = "rank" []A & || & b[] -| "number of columns in" A . 1`**
