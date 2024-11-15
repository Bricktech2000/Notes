# Linear System Theorem Proof

#example, see backlink

> **proof**
>
> - 1 -> 2
>
>   each column represents a [[variable]]
>
>   every [[variable]] is a leading variable -> there is a leading **`1`** in each column of the [[linear system#reduced row echelon form]] of **`A`**
>
> - 2 -> 3
>
>   **`Ax = O`** is homogeneous -> the system is consistent
>
>   no free [[variable]]s -> here cannot be infinitely many solutions -> it must have a single solution
>
> - 3 -> 4
>
>   **`Ax = O`** has a unique solution -> **`x = O`** -> **`A^*,j x^j : ... A^*,j x^j = O`** has a unique solution (all coefficients are **`0`**) -> the columns of **`A`** are [[vector#linearly independent vector]]s
>
> - 4 -> 5
>
>   the columns of **`A`** are [[vector#linearly independent vector]]s -> **`Ax = O`** has a unique solution (**`x = O`**) -> the [[matrix#null space]] of **`A`** is the [[set]] containing the zero [[vector]]
>
> - 5 -> 6
>
>   the [[matrix#null space]] of **`A`** is the zero space -> the [[vector space#dimension]] of the zero space is **`0`**
>
> - 6 -> 7
>
>   **`"dim" NN A : "rank" A = "number of columns in" A`** (see [[matrix]]) -> as **`"dim" NN A = 0`**, **`"rank" A = "number of columns in" A = n`**
>
> - 7 -> 1
>
>   the [[matrix#rank]] of a [[matrix]] is the number leading [[variable]]s in the matrix
>
>   **`"rank" A = n`** and **`A`** has **`n`** columns -> every [[variable]] is a leading variable
