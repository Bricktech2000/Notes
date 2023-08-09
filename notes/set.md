# Set

**see** [[abstract data type]]

**see** [[math notation]], [[boolean algebra]]

**definition** a _set_ is an unordered collection of elements, each of which are unique

**definition** _formally in my [[math notation]]_ a [[set]] is a [[set theory]]etical [[function]] that takes an element and returns whether it is a member of the [[set]]. that ys, [[set]]s are [[predicate]]s

**notation** _set roster notation_ **`S = {{1, 2, 3}}`**

**notation** _set roster notation_ **`S = {{1, 2, 3 ...}}`** &mdash; **`...`** are allowed

**notation** _set builder notation_ **`S x = P x`** or **`S = x -> P x`** where **`P`** is [[predicate]]

**types**

[[binary search tree]] [[set]]

[[hash table]] [[set]]

**properties**

_elements are unordered_ **`{{1, 2, 3}} = {{3, 2, 1}} = ...`**

_elements are unique_ **`{{1, 1, 1}} = {{1, 1}} = ...`**

## Universal Set

**definition** **`UU x = ^^`**

**definition** **`UU x == +{ } == + x -> __ == x -> ^^`**

**properties** **`/\ UU |- A`**, for all [[set]] **`A`**

## Empty Set

**equiv** _[[type#empty type]]_

**definition** **`{{ }}`**

**definition** **`x -> __`**

**properties** **`/\ {{ }} -| A`**, for all [[set]] **`A`**

## Singleton Set

**equiv** _[[type#unit type]]_

**definition** a _singleton set_ is a [[set]] **`A`** with **`# A = 1`**

## Subset

## Superset

**equiv** _[[type#subtype]]_

**equiv** _[[type#supertype]]_

**definition** a [[set]] **`A`** is a _subset_ of a [[set]] **`B`** if and only if every element of **`A`** is an element of **`B`**

**definition** a [[set]] **`B`** is a _superset_ of a [[set]] **`A`** if and only if every element of **`A`** is an element of **`B`**

in other words, an element being in **`A`** implies it is also in **`B`**

**notation** _in my [[math notation]]_ **`/\ A -| B`** checks whether **`A`** is a [[set#subset]] of **`B`**

**notation** _in my [[math notation]]_ **`/\ B |- A`** checks whether **`B`** is a [[set#superset]] of **`A`**

**properties**

both the [[set#subset]] and the [[set#superset]] form a [[partial order]]

## Union

**definition** **`A ^^ B`**

### Disjoint Union

**definition** **`A ^^ B`** with the guarantee that **`A __ B == {{ }}`**

## Intersection

**definition** **`A __ B`**

## Equivalence

**definition** two [[set]]s are _equivalent_ if and only if they contain the same elements; **`A = B == /\ A = B`**

## Membership

**notation** **`S a`**

## Isomorphism

#todo **equivalence**

**see** [[category]], [[category theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## Partition

**definition** a _partition_ of a [[set]] **`A`** is a collection of non-empty [[set#subset]]s of **`A`** such that every element of **`A`** is in exactly one of the [[set#subset]]s

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
> - **`/\ * -| {{ }} = {{ {{ }} }}`**
> - **`/\ * -| (/\ * -| O) = {{ {{ }}, {{ {{ }} }} }}`**

## Arrangement

_order matters_

**definition** an _arrangement_ of size **`k`** of a [[set]] **`A`** is a [[list]] containing **`k`** elements of **`A`**

the number of **`k`**-arrangements of an **`n`**-set is

- **`P n k = PP {n -- n.k}`** with repetition forbidden. also called _**`k`**-permutations_
- **`P_* n k = [n]k`** with repetition allowed. also called _**`k`**-tuples_

## Combination

_order does not matter_

**definition** a _combination_ of size **`k`** of a [[set]] **`A`** is a [[multiset]] containing **`k`** elements of **`A`**

the number of **`k`**-combinations of an **`n`**-set is

- **`C n k = P {n -- k} k = PP {n -- n.k -- k}`** with repetition forbidden. also called _**`k`**-subsets_
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
> - the number of solutions to **`:x = n`** with **`/\ NN x *`**
> - the number of **`n`**-subsets of an **`n:k.1`**-[[set]]
> - the number of **`k.1`**-subsets of an **`n:k.1`**-[[set]]

**theorem**

**`C n k = C n (n.k)`**

## theorems

**theorem**

- let **`P n k`** be the **`k`**-permutations of an **`n`**-[[set]]
- let **`C n k`** be the **`k`**-subsets of an **`n`**-[[set]]
- let **`P k k`** be the **`k`**-permutations of a **`k`**-[[set]]

then, there exists a [[function#bijective function]] between **`P n k`** and **`__ {C n k, P k k} *`**, see [[cartesian product]]

moreover, **`# C n k = # C n (n.k)`**; the number of **`k`**-subsets of an **`n`**-[[set]] is equal to the number of **`n.k`**-subsets of an **`n`**-[[set]]
