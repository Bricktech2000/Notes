# Determinant

**see** [[math notation]], [[matrix]]

**notation**

**`"det" A`** where **`A`** is a square [[matrix]]

**properties**

**`"det" A = "det" (\r A)`**, see [[matrix#transpose]]

**`"det" cA = c^n | "det" A`**, where **`n`** is the width and height of the [[matrix]]

**properties**

**see** [[linear system#elementary operation]]

_adding a multiple of a row or column to another row or column_ **`"det" A = "det" A'`**

_swapping any two rows or two columns_ **`"det" A = ."det" A'`**

_multiplying a row or a column by a [[scalar]] **`c`**_ **`"det" A = c"det" A'`**

#todo mm

**`"det" AB = "det" A | "det" B`**

#todo mm

**`"det" [A]m = ["det" A]m -| NN m`**

**`"det" A = 0`** if and only if **`A`** is not invertible, see [[matrix]]

#todo mm

**`"det" -A = -"det" A`** if and only if **`A`** is invertible, see [[matrix]]

> **note** the equation above is beautiful, as in [[conventional math notation]], $A^{-1}$ is a [[matrix#inverse]] whereas $"det"(A)^{-1}$ is $\frac 1 {"det"(A)}$

## Computation

> **procedure** _computing the determinant using [[recursion]]_ see #magic
>
> _Laplace expansion_
>
> note the alternating **`{:}`** and **`{.}`** below. the following sign [[matrix]] can be used to determine the signs of the cofactors:
>
> **`[]{:} & {.} & {:} & {.} & ... && {.} & {:} & {.} & {:} & ... && {:} & {.} & {:} & {.} & ... && {.} & {:} & {.} & {:} & ... && ... & ... & ... & ... & ...[]`**
>
> the first row was chosen below, but any row or column can be used. _cofactor expansion along the first row_
>
> **`MM^3,3 A < "det" A = "det" []a & b & c && d & e & f && g & h & i[] = a"det" []e & f && h & i[] . b"det" []d & f && g & i[] : c"det" []d & e && g & h[]`**
>
> the base case for the [[algorithm]] is **`"det" []s[] = s`**, where **`s`** is a [[scalar]]

> **procedure** _computing the determinant of a **`2`** by **`2`** [[matrix]]_
>
> **`"det" []a & b && c & d[] = ad . bc`**

> **procedure** _computing the determinant, triangular method_ see #magic
>
> the [[determinant]] of a [[matrix#triangular matrix]] is the product of its [[matrix#diagonal]] entries
>
> [[linear system#elementary operation]]s have a consistent effect on the [[determinant]] of a [[matrix]] (see properties above). therefore, it can be easier to row-reduce the [[matrix]] to compute its [[determinant]]

## Intuition

> the [[determinant]] is all about measuring how [[area]]s change during a [[linear transformation]] represented as [[matrix#multiplication]]. after the transformation, the **`1`** by **`1`** unit square formed by the [[vector in rn#unit vector]]s **`(0, 1)`** and **`(1, 0)`** gets turned into a parallelogram whose [[area]] is the [[determinant]] of the [[linear transformation#standard matrix]] &mdash; 3B1B
