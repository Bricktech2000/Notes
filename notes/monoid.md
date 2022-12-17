# Monoid

## Operation

## Identity Element

**see** [[math notation]], [[algebraic structure]]

it is said that _[elements of a [[set]]] with [an identity] form a [[monoid]] under [an [[operator]]]_. for example, _[[natural]]s with $0$ form a [[monoid]] under addition_

**definition** a [[monoid]] is a finite or infinite [[set]] equipped with a closed associative binary operation and an identity element &mdash; Wikipedia

**definition**

let a binary [[operator]] $\circ$ on a [[set]] $S$. for them to form a [[monoid]], the following [[axiom]]s must be satisfied for all $S\ a \land S\ b \land S\ c$:

_associativity_ $(a \circ b) \circ c = a \circ (b \circ c)$

_identity element_ $a \circ I = a \land S\ I$

_closure_ $S\ (a \circ b)$

&mdash; Wikipedia

&mdash; <https://youtu.be/Nrp_LZ-XGsY?t=1041>

**applications**

_closure_ allows the binary operation to be used on a list of elements of the set $S$. this is known as a `reduce` operation in [[functional programming]]. as examples, `[1, 2, 3].reduce(+) = 1 + 2 + 3 = 6` and `["a", "b", "c"].reduce(&) = "a" & "b" & "c" = "abc"`.

_associativity_ allows for divide and conquer [[algorithm]]s

_associativity_ allows for automatic parallelization of operations throughout multiple threads, CPUs, GPUs...

_associativity_ allows for incremental accumulation. if we have already computed `(1 + 2 + 3) = 6`, we can compute `(1 + 2 + 3) + 4 = 6 + 4 = 10` without having to recompute the result of `(1 + 2 + 3)`

_identity element_ allows for the binary operation to be used when data is empty or missing; on an empty list, for instance. this is known as a `fold` operation in [[functional programming]]. as examples, `[].reduce(+) = 0` and `[].reduce(&) = ""`.

**examples**

> **example** the following data [[type]]s and binary [[operator]]s are examples of [[monoid]]s:
>
> - `String` and concatenation
> - `u32` and addition
> - `f64` and multiplication
