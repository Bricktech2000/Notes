# Monoid

it is said that _[elements of a [[set]]] with [an identity] form a [[monoid]] under [an [[operator]]]_. for example, _[[natural]]s with $0$ for a [[monoid]] under addition_

## definition

> A [[monoid]] is a finite or infinite [[set]] equipped with a closed associative binary operation and an identity element. &mdash; Wikipedia

let a binary [[operator]] $\oplus$ on a [[set]] $S$. the following axioms must be respected:

- $(a \oplus b) \oplus c = a \oplus (b \oplus c) \dashv S\ a \land S\ b \land S\ c$ &mdash; associativity
- $a \oplus I = I \oplus a = a \land S\ I \dashv S\ a$ &mdash; identity element
- $S\ (a \oplus b) \dashv S\ a \land S\ b$ &mdash; closure

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
