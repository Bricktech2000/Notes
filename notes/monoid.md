# Monoid

## Operation

## Identity Element

**see** [[algebraic structure]], [[reduce function]], [[binary exponentiation]]

it is said that _[elements of a [[set]]] with [an identity] form a [[monoid]] under [an [[operator]]]_. for example, _[[natural]]s with $0$ form a [[monoid]] under addition_

**definition** a [[monoid]] is a finite or infinite [[set]] equipped with a closed associative binary operation and an identity element --- Wikipedia

**definition**

let a binary [[operator]] $\cdot$ on a [[set]] $S$. for them to form a [[monoid]], the following [[axiom]]s must be satisfied for all $a, b, c \in S$ for some $e \in S$:

_associativity_ $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

_identity element_ $a \cdot e = e \cdot a = a$

_closure_ $a \cdot b \in S$

--- Wikipedia

--- <https://youtu.be/Nrp_LZ-XGsY?t=1041>

**examples**

> **example** the following data [[type]]s and binary [[operator]]s are examples of [[monoid]]s:
>
> - `String` and [[string#concatenation]], see [[string]]
> - `u32` and addition, see [[natural]]
> - `f64` and multiplication, see [[floating-point number]]
> - `Fn` and [[composition]], see [[function]]

## Free Monoid

--- <https://en.wikipedia.org/wiki/Free_monoid>

**see** [[semigroup#free semigroup]]

**notation** _in [[conventional math notation]]_ $S^*$

**definition** the _free monoid_ on a [[set]] is its smallest [[set#superset]] forming a [[monoid]] under [[string#concatenation]]

**definition** $S^* = S^+ \cup \{\varepsilon\}$, see [[semigroup#free semigroup]]

> **note** $\{\varepsilon\}^+ = \{\varepsilon\}$ and therefore it is not always the case that $S^* = S^+ \sqcup \{\varepsilon\}$, see [[set#disjoint union]] --- <https://cs.stackexchange.com/questions/35600/kleene-star-and-kleene-plus>

**equiv** _`*` operator in [[regular expression]]s_

**properties**

the [[monoid#free monoid]] [[operator]] is a [[function#idempotent function]]

## Homomorphism

--- <https://en.wikipedia.org/wiki/Monoid#Monoid_homomorphisms>

**see** [[morphism#homomorphism]]

**definition** a _monoid homomorphism_ from a [[monoid]] $M$ to a [[monoid]] $N$ is a [[function]] $f : M \to N$ such that $f\ e_M = e_N \land \forall a, b \in M.\ f\ (a \cdot_M b) = f\ a \cdot_N f\ b$
