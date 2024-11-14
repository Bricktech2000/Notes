# Semigroup

## Operation

_a [[monoid]] without necessarily having a [[monoid#identity element]]_

_a [[group]] without necessarily having a [[group#identity element]] or [[group#inverse element]]s_

&mdash; <https://en.wikipedia.org/wiki/Semigroup>

**see** [[math notation]], [[algebraic structure]]

**definition** a [[semigroup]] is a finite or infinite [[set]] of elements equipped with a closed associative binary operation &mdash; Wikipedia and me

**definition**

let a binary [[operator]] **`{:}`** on a [[set]] **`G_*`**. for them to form a [[semigroup]], the following [[axiom]]s must be satisfied for all **`G_* {a /\ b /\ c}`**:

_associativity_ **`(a : b) : c = a : (b : c)`**

_closure_ **`G_* (a : b)`**

## Free Semigroup

&mdash; <https://en.wikipedia.org/wiki/Free_monoid>

**see** [[monoid#free monoid]]

**notation** _in [[conventional math notation]]_ $S^+$

**definition** the _free semigroup_ on a [[set]] is its smallest [[set#superset]] forming a [[semigroup]] under [[string#concatenation]]

**definition** $S^+ = S^*S = SS^*$, see [[monoid#free monoid]]

> **note** $\{\epsilon\}^+ = \{\epsilon\}$ and therefore it is not always the case that $S^+ = S^* \setminus \{\epsilon\}$ &mdash; <https://cs.stackexchange.com/questions/35600/kleene-star-and-kleene-plus>

**equiv** _`+` operator in [[regular expression]]s_

**properties**

the [[semigroup#free semigroup]] [[operator]] is a [[function#idempotent function]]
