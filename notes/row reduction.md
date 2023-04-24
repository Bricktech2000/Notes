# Row Reduction

_a process for putting a [[matrix]] in [[linear system#reduced row echelon form]]_

## Gaussian Elimination

**see** [[linear system]], [[linear equation]], [[matrix]]

[[row reduction#gaussian elimination]] has a time [[computational complexity]] of **`O [*]3`**. this makes it unfeasible for large [[matrix]]es. there exist many alternatives, such as:

- the _Gauss-Seidel_ method (numerical approximation through [[iteration]])
- the _Conjugate Gradient_ method (for _sparse_ [[matrix]]es, numerical approximation often through [[iteration]])

&mdash; <https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method> and <https://en.wikipedia.org/wiki/Conjugate_gradient_method> &mdash; <https://youtu.be/oulfRfqTxJA?t=159>

> **procedure** _putting a [[matrix]] in [[linear system#row echelon form]]_
>
> _eliminate **`x_0`** from all lines below **`L_0`**, eliminate **`x_1`** from all lines below **`L_1`**, and so on_
>
> - if the [[matrix]] is zero, stop. if one row remains, stop.
> - bring a non-zero entry to the first row of the left-most non-zero column
> - annihilate the rest of the column using the first row
> - ignore the first row and go back to the first step

> **procedure** _putting a [[matrix]] in [[linear system#reduced row echelon form]] from [[linear system#row echelon form]]_
>
> _make all pivots be a **`1`**. make all pivot columns contain only zeros (apart from their pivot)_
>
> - if the right-most pivot is in the first row, stop
> - multiply the row containing the right-most pivot by a [[scalar]] to make the pivot a **`1`**
> - take this pivot to annihilate all other entries in the column
> - ignore the row with the right-most pivot and go back to the first step
