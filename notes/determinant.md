# Determinant

**see** [[math notation]], [[matrix]]

the [[determinant]] is a [[morphism#homomorphism]] from [[matrix]]es with [[matrix#multiplication]] to [[scalar]]s with multiplication. similarly, the [[determinant]] is a [[morphism#homomorphism]] from [[linear transformation]]s with [[composition]] to their effect on [[area]]s with multiplication

**notation**

**`"det" A`** where **`A`** is a square [[matrix]]

**properties**

**`"det" A = "det" (rr A)`**, see [[matrix#transpose]]

**`"det" cA = [c]n | "det" A`**, where **`n`** is the width and height of the [[matrix]]

**`"det" AB = "det" A | "det" B`** #todo mm

**`"det" [A]m = ["det" A]m -| NN m`** #todo mm

**`"det" A = 0`** if and only if **`A`** is not invertible, see [[matrix]]

**`"det" -A = -"det" A`** #todo mm if and only if **`A`** is invertible, see [[matrix]]

> **note** the equation above is beautiful because, in [[conventional math notation]], $A^{-1}$ is a [[matrix#inverse]] whereas $\det(A)^{-1}$ is $\frac 1 {\det(A)}$

**properties** _[[linear system#elementary operation]]_

_adding a multiple of a row or column to another row or column_ **`"det" A = "det" A_*`**

_swapping any two rows or two columns_ **`"det" A = ."det" A_*`**

_multiplying a row or a column by a [[scalar]] **`c`**_ **`"det" A = c"det" A_*`**

## Computation

> **procedure** _computing the determinant using [[recursion]]_ #magic
>
> _Laplace expansion_
>
> note the alternating **`(:)`** and **`(.)`** below. the following sign [[matrix]] can be used to determine the signs of the cofactors:
>
> **`[](:) & (.) & (:) & (.) & ... && (.) & (:) & (.) & (:) & ... && (:) & (.) & (:) & (.) & ... && (.) & (:) & (.) & (:) & ... && ... & ... & ... & ... & ...[]`**
>
> the first row was chosen below, but any row or column can be used. _cofactor expansion along the first row_
>
> **`MM^3,3 A < "det" A = "det" []a & b & c && d & e & f && g & h & i[] = a"det" []e & f && h & i[] .. b"det" []d & f && g & i[] : c"det" []d & e && g & h[]`**
>
> the base case for the [[algorithm]] is **`"det" []s[] = s`**, where **`s`** is a [[scalar]]

> **procedure** _computing the determinant, triangular method_ #magic
>
> the [[determinant]] of a [[matrix#triangular matrix]] is the product of its [[matrix#diagonal]] entries
>
> [[linear system#elementary operation]]s have a consistent effect on the [[determinant]] of a [[matrix]] (see properties above). therefore, it can be easier to row-reduce the [[matrix]] to compute its [[determinant]]
