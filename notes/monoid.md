# Monoid

## Operation

## Identity Element

**see** [[algebraic structure]]

**definition** a _monoid_ is a [[semigroup]] that has an identity element

**definition** a _monoid_ is a [[set]] equipped with a closed associative binary operation and an identity element --- Wikipedia

**definition**

a _monoid_ is a [[set]] $S$ equipped with a binary [[operator]] $\cdot$ that satisfies the following [[axiom]]s for some $e \in S$ for all $a, b, c \in S$:

_associativity_ $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

_identity_ $a \cdot e = e \cdot a = a$

_closure_ $a \cdot b \in S$

--- Wikipedia

--- <https://youtu.be/Nrp_LZ-XGsY?t=1041>

## Fold

**aka** _reduce_

**see** [[semigroup#fold]], [[binary exponentiation]]

#stub

## Free Monoid

--- <https://en.wikipedia.org/wiki/Free_monoid>

--- <https://ncatlab.org/nlab/show/free+monoid>

**see** [[semigroup#free semigroup]]

**notation** $S^*$

**definition** the _free monoid_ on a [[set]] is its smallest [[set#superset]] that forms a [[monoid]] under [[list#concatenation]]

**definition** $S^* = S^+ \cup \{\varepsilon\}$, see [[semigroup#free semigroup]]

> **note** $\{\varepsilon\}^+ = \{\varepsilon\}$ and therefore it is not always the case that $S^* = S^+ \sqcup \{\varepsilon\}$, see [[set#disjoint union]] --- <https://cs.stackexchange.com/questions/35600/kleene-star-and-kleene-plus>

**equiv** _`*` operator in [[regular expression]]s_

**properties**

the [[monoid#free monoid]] [[operator]] has [[idempotence]]

## Homomorphism

--- <https://en.wikipedia.org/wiki/Monoid#Monoid_homomorphisms>

**see** [[morphism#homomorphism]]

**definition** a _monoid homomorphism_ from a [[monoid]] $M$ to a [[monoid]] $N$ is a [[function]] $f : M \to N$ such that $f\ e_M = e_N \land \forall a, b \in M.\ f\ (a \cdot_M b) = f\ a \cdot_N f\ b$
