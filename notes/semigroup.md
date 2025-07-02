# Semigroup

## Operation

_a [[monoid]] that doesn't need a [[monoid#identity element]]_

_a [[group]] that doesn't need a [[group#identity element]] or [[group#inverse]]s_

--- <https://en.wikipedia.org/wiki/Semigroup>

**see** [[algebraic structure]]

**definition** a [[semigroup]] is a [[set]] of elements equipped with a closed associative binary operation --- Wikipedia and me

**definition**

a _semigroup_ is a [[set]] $S$ equipped with a binary [[operator]] $\cdot$ that satisfies the following [[axiom]]s for all $a, b, c \in S$

_associativity_ $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

_closure_ $a \cdot b \in S$

## Fold

**aka** _reduce_

**see** [[monoid#fold]], [[binary exponentiation]]

#stub

## Free Semigroup

--- <https://en.wikipedia.org/wiki/Free_monoid>

**see** [[monoid#free monoid]]

**notation** $S^+$

**definition** the _free semigroup_ on a [[set]] is its smallest [[set#superset]] that forms a [[semigroup]] under [[list#concatenation]]

**definition** $S^+ = S^*S = SS^*$, see [[monoid#free monoid]]

> **note** $\{\varepsilon\}^+ = \{\varepsilon\}$ and therefore it is not always the case that $S^+ = S^* \setminus \{\varepsilon\}$ --- <https://cs.stackexchange.com/questions/35600/kleene-star-and-kleene-plus>

**equiv** _`+` operator in [[regular expression]]s_

**properties**

the [[semigroup#free semigroup]] [[operator]] has [[idempotence]]
