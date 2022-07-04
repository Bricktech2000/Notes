# Monoid

## definition

> A [[monoid]] is a [[set]] equipped with an associative binary operation and an identity element. &mdash; Wikipedia

### axioms

let a binary operation $\times$ on a set $S$

- $(a \times b) \times c = a \times (b \times c) \dashv S\ a \land S\ b \land S\ c$ &mdash; associativity
- $a \times I = I \times a = a \land S\ I \dashv S\ a$ &mdash; identity element

moreover, the result the binary operation yields must be an element of the set $S$ &mdash; closure

&mdash; Wikipedia

&mdash; <https://youtu.be/Nrp_LZ-XGsY?t=1041>

## advantages and applications

### closure

allows the binary operation to be used on a list of elements of the set $S$. this is known as a `reduce` operation in [[functional-programming]]. as examples, `[1, 2, 3].reduce(+) = 1 + 2 + 3 = 6` and `["a", "b", "c"].reduce(&) = "a" & "b" & "c" = "abc"`.

### associativity

allows for divide and conquer [[algorithm]]s

allows for automatic parallelization of operations throughout multiple threads, CPUs, GPUs...

allows for incremental accumulation. if we have already computed `(1 + 2 + 3) = 6`, we can compute `(1 + 2 + 3) + 4 = 6 + 4 = 10` without having to recompute the result of `(1 + 2 + 3)`

### identity element

allows for the binary operation to be used when data is empty or missing; on an empty list, for instance. this is known as a `fold` operation in [[functional-programming]]. as examples, `[].reduce(+) = 0` and `[].reduce(&) = ""`.

## examples

the following data [[type]]s and binary [[operator]]s are examples of [[monoid]]s: `String` and concatenation, `u32` and addition, `f64` and multiplication...
