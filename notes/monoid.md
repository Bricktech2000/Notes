# Monoid

## Operation

## Identity Element

**see** [[math notation]], [[algebraic structure]], [[binary exponentiation]]

it is said that _[elements of a [[set]]] with [an identity] form a [[monoid]] under [an [[operator]]]_. for example, _[[natural]]s with **`0`** form a [[monoid]] under addition_

**definition** a [[monoid]] is a finite or infinite [[set]] equipped with a closed associative binary operation and an identity element --- Wikipedia

**definition**

let a binary [[operator]] **`{\*}`** on a [[set]] **`S`**. for them to form a [[monoid]], the following [[axiom]]s must be satisfied for all **`S a /\ S b /\ S c`**:

_associativity_ **`(a \* b) \* c = a \* (b \* c)`**

_identity element_ **`a \* I = a /\ S I`**

_closure_ **`S (a \* b)`**

--- Wikipedia

--- <https://youtu.be/Nrp_LZ-XGsY?t=1041>

**applications**

_closure_ allows the binary operation to be used on a list of elements of the set **`S`**. this is known as the _[[reduce function]]_ in [[functional programming]]. as examples, `[1, 2, 3].reduce(+) = 1 + 2 + 3 = 6` and `["a", "b", "c"].reduce(&) = "a" & "b" & "c" = "abc"`.

_associativity_ allows for [[divide and conquer]] [[algorithm]]s

_associativity_ allows for automatic parallelization of operations throughout multiple threads, CPUs, GPUs...

_associativity_ allows for incremental accumulation. if we have already computed `(1 + 2 + 3) = 6`, we can compute `(1 + 2 + 3) + 4 = 6 + 4 = 10` without having to recompute the result of `(1 + 2 + 3)`

_identity element_ allows for the binary operation to be used when data is empty or missing; on an empty list, for instance. this is known as the _fold function_ in [[functional programming]]. as examples, `[].reduce(+) = 0` and `[].reduce(&) = ""`.

**examples**

> **example** the following data [[type]]s and binary [[operator]]s are examples of [[monoid]]s:
>
> - `String` and [[string#concatenation]], see [[string]]
> - `u32` and addition, see [[natural]]
> - `f64` and multiplication, see [[float]]
> - `Fn` and [[composition]], see [[function]]

## Free Monoid

--- <https://en.wikipedia.org/wiki/Free_monoid>

**see** [[semigroup#free semigroup]]

**notation** _in [[conventional math notation]]_ $S^*$

**definition** the _free monoid_ on a [[set]] is its smallest [[set#superset]] forming a [[monoid]] under [[string#concatenation]]

**definition** $S^* = S^+ \cup \{\epsilon\}$, see [[semigroup#free semigroup]]

> **note** $\{\epsilon\}^+ = \{\epsilon\}$ and therefore it is not always the case that $S^* = S^+ \sqcup \{\epsilon\}$, see [[set#disjoint union]] --- <https://cs.stackexchange.com/questions/35600/kleene-star-and-kleene-plus>

**equiv** _`*` operator in [[regular expression]]s_

**properties**

the [[monoid#free monoid]] [[operator]] is a [[function#idempotent function]]

## Homomorphism

--- <https://en.wikipedia.org/wiki/Monoid#Monoid_homomorphisms>

**see** [[morphism#homomorphism]]

**definition** a _monoid homomorphism_ from a [[monoid]] **`M`** to a [[monoid]] **`N`** is a [[function]] **`f`** such that **`f I = I /\ f (a \* b) = f a \* f b > M {a /\ b}`** #todo id
