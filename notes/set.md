# Set

**see** [[abstract data type]]

**see** [[math notation]], [[boolean algebra]]

**definition** a _set_ is an unordered collection of elements, each of which are unique

**definition** _formally in my [[math notation]]_ a [[set]] is a [[set theory]]etical [[function]] that takes an element and returns whether it is a member of the [[set]] (a [[predicate]])

**notations**

_Set Roster notation_

**`S = {{1, 2, 3}}`**

**`S = {{1, 2, 3 \cdots}}`** &mdash; **`...`** are allowed

_Set Builder notation_

**`S x = P x`** or **`S = x -> P x`**, where

**`P`** is a [[predicate]], see [[math notation]]

in [[conventional math notation]], this abomination: $\lbrace x \mid P(x) \rbrace$

**types**

[[binary search tree]] [[set]]

[[hash table]] [[set]]

**properties**

_elements are unordered_ **`{{1, 2, 3}} = {{3, 2, 1}} = ...`**

_elements are unique_ **`{{1, 1, 1}} = {{1, 1}} = ...`**

**see**

[[number]] sets

[[universal]] set

[[field]]s

[[monoid]]s

## Subset

## Superset

**definition** a [[set]] **`A`** is a _subset_ of a [[set]] **`B`** if and only if every element of **`A`** is an element of **`B`**

**definition** a [[set]] **`B`** is a _superset_ of a [[set]] **`A`** if and only if every element of **`A`** is an element of **`B`**

in other words, an element being in **`A`** implies it is also in **`B`**

**notation**

_in my [[math notation]]_

**`/\ A -| B`** checks whether **`A`** is a [[set#subset]] of **`B`**

**`/\ B |- A`** checks whether **`B`** is a [[set#superset]] of **`A`**

_in [[conventional math notation]]_

$A \subseteq B$ states **`A`** is a [[set#subset]] of **`B`**

$B \supseteq A$ states **`B`** is a [[set#superset]] of **`A`**

**examples**

**`ZZ < RR`**

**`EE < ZZ`**

**properties**

both the [[set#subset]] and the [[set#superset]] form a [[partial order]]

## Union

**definition** **`A ^^ B`**

### Disjoint Union

**definition** **`A ^^ B`** with the guarantee that **`A __ B == {{ }}`**

## Intersection

**definition** **`A __ B`**

## Equivalence

**definition** two [[set]]s are _equivalent_ if and only if they contain the same elements, **`A = B == x -> (A x = B x)`**

## Membership

**notation**

**`S a`**

## Isomorphism

#todo **equivalence**

**see** [[category]], [[category theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## [[empty]]

_the empty [[set]]_

**see** [[empty]]

## [[universal]]

_the [[set]] of all possible mathematical entities_

**see** [[universal]]

## Partition

**definition** a _partition_ of a [[set]] **`A`** is a collection of [[set]]s **`S`** such that **`S^i /\ S^j == {{ }}`** for all **`i, j`** (the [[set]]s are pairwise disjoint) and **`\/ S = A`**

**definition** a _partition_ of a [[set]] **`A`** is a collection of [[set]]s **`S`** such that **`{0, 1} A = : {0, 1} S`**

## Cardinality

**notation** **`# S`**

**definition** the _cardinality_ of a [[set]] is the number of elements in the [[set]]

**properties**

when two [[set]]s form a [[set#disjoint union]] **`A \/ B`**, then **`# S = # A : # B`**

when two [[set]]s form a [[set#union]] **`A \/ B`**, then **`# S = # A : # B . # (A /\ B)`**

_difference principle_ the cardinality of the difference of two [[set]]s is **`# (A /\ +B) = # A . # (A /\ B)`**

_product principle_ the cardinality of the [[cartesian product]] of two [[set]]s is **`# (__ {A, B} *) = # A | # B`**

## Power Set

**definition** the _power set_ of a [[set]] **`A`** is the [[set]] of all [[set#subset]]s of **`A`**

**definition** **`/\ * -| S`**

**notation** **`/\ * -| S`**

> **examples**
>
> let **`O = {{ }}`**
>
> **`/\ * -| {{1, 2, 3}} = {{ {{1}}, {{2}}, {{3}}, {{1, 2}}, {{2, 3}}, {{1, 3}}, {{1, 2, 3}}, {{ }} }}`**
>
> **`/\ * -| O = {{O}}`**
>
> **`/\ * -| (/\ * -| O) = {{ O, {{O}} }}`**

## Arrangement

_order matters_

**definition** an _arrangement_ of size **`k`** of a [[set]] **`A`** is a [[vector in rn]] containing **`k`** elements of **`A`**

the number of **`k`**-arrangements of an **`n`**-set is

- **`P n k = \P n -- \P (n.k)`** with repetition forbidden. also called _**`k`**-permutations_
- **`P_*  n k = [n]k`** with repetition allowed. also called _**`k`**-tuples_

## Combination

_order does not matter_

**definition** a _combination_ of size **`k`** of a [[set]] **`A`** is a [[multiset]] containing **`k`** elements of **`A`**

the number of **`k`**-combinations of an **`n`**-set is

- **`C n k = P n k -- P k k = \P n -- \P (n.k) -- \P k`** with repetition forbidden. also called _**`k`**-subsets_
- **`C_* n k = C (n:k.1) (k.1)`** with repetition allowed. also called _**`k`**-multisubsets_

> **proof** _stars and bars [[proof]] sketch_
>
> given a [[multiset]] of elements,
>
> **`((a, e, b, a, d, b, b, a, c, e))`**
>
> rewriting in order as order does not matter,
>
> **`((a, a, a, b, b, b, c, d, e, e))`**
>
> represented as _stars and bars_,
>
> **`...|...|.|.|..`**
>
> there are **`n:k.1`** choose **`k.1`** ways to arrange the bars

> **proof** _alternative [[proof]] sketch with bijections_
>
> the following are equivalent:
>
> - the number of **`k`**-combinations from an **`n`**-[[set]] with repetition allowed
> - the number of **`k`**-[[multiset]]s from an **`n`**-[[set]]
> - the number of ways of distributing **`n`** identical marbles into **`k`** distinguishable boxes
> - the number of solutions to **`:x = n`** with **`NN x^i`** for all **`i`**
> - the number of **`n`**-subsets of an **`n:k.1`**-[[set]]
> - the number of **`k.1`**-subsets of an **`n:k.1`**-[[set]]

**theorem**

**`C n k = C n (n.k)`**

## theorems

**theorem**

- let **`P n k`** be the **`k`**-permutations of an **`n`**-[[set]]
- let **`C n k`** be the **`k`**-subsets of an **`n`**-[[set]]
- let **`P k k`** be the **`k`**-permutations of a **`k`**-[[set]]

then, there exists a [[function#bijective function]] between **`P n k`** and **`\_\_ {C n k, P k k} **`\*\*, see [[cartesian product]]

moreover, **`# C n k = # C n (n.k)`**. the number of **`k`**-subsets of an **`n`**-[[set]] is equal to the number of **`n.k`**-subsets of an **`n`**-[[set]]
