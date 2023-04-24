# Linear System Theorem Proof

#example, see backlink

> **proof**
>
> - 1 &rarr; 2
>
>   each column represents a [[variable]]
>
>   every [[variable]] is a leading variable &rarr; there is a leading **`1`** in each column of the [[linear system#reduced row echelon form]] of **`A`**
>
> - 2 &rarr; 3
>
>   **`Ax = O`** is homogeneous &rarr; the system is consistent
>
>   no free [[variable]]s &rarr; here cannot be infinitely many solutions &rarr; it must have a single solution
>
> - 3 &rarr; 4
>
>   **`Ax = O`** has a unique solution &rarr; **`x = O`** &rarr; **`A^*,j x^j : ... A^*,j x^j = O`** has a unique solution (all coefficients are **`0`**) &rarr; the columns of **`A`** are [[linearly independent]]
>
> - 4 &rarr; 5
>
>   the columns of **`A`** are [[linearly independent]] &rarr; **`Ax = O`** has a unique solution (**`x = O`**) &rarr; the [[matrix#null space]] of **`A`** is the [[set]] containing the zero [[vector]]
>
> - 5 &rarr; 6
>
>   the [[matrix#null space]] of **`A`** is the zero space &rarr; the [[vector space#dimension]] of the zero space is **`0`**
>
> - 6 &rarr; 7
>
>   **`"dim" nn A : "rank" A = "number of columns in" A`** (see [[matrix]]) &rarr; as **`"dim" nn A = 0`**, **`"rank" A = "number of columns in" A = n`**
>
> - 7 &rarr; 1
>
>   the [[matrix#rank]] of a [[matrix]] is the number leading [[variable]]s in the matrix
>
>   **`"rank" A = n`** and **`A`** has **`n`** columns &rarr; every [[variable]] is a leading variable
