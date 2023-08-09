# Relation

**see** [[set]], [[cartesian product]], [[math notation]]

**definition**

a _relation_ **`RR`** between two [[set]]s **`A`** and **`B`** is a [[set#subset]] of the [[cartesian product]] of those [[set]]s: **`/\ RR -| (__ {A, B} *)`**

**definition**

**`RR {a, b} = A a /\ B b /\ P {a, b}`**, where

- **`RR`** is a _relation_ between elements of **`A`** and **`B`**
- **`P`** is a [[predicate]]

**definition** a _relation on a set_ **`A`** is a [[relation]] from **`A`** to **`A`**

**notation**

_membership in my [[math notation]]_ **`RR {x, y}`**, see [[ordered pair]]

_membership in [[conventional math notation]]_ $x \mathcal R y$

## Inverse Relation

**equiv** _[[ordered pair#inverse]]_

**definition** **`RR {+} *`**

**notation** **`RR {+} *`**

**properties**

**`RR {x, y} = (RR {+} *) {y, x}`**

**`/\ (RR {+} *) -| (__ {B, A} *)`**

#todo **equivalence** for the three sections below

## Reflexive Relation

_every element is related to itself_

similar to identities in [[category theory]]

**definition** a [[relation]] on **`A`** is said to be _reflexive_ if **`RR {x, x}`** for all **`x`**

## Symmetric Relation

_swapping arguments never changes the result_

similar to isomorphisms in [[category theory]]

**definition** a [[relation]] on **`A`** is said to be _symmetric_ if **`RR {x, y} < RR {y, x}`** for all **`x`** and **`y`**

## Transitive Relation

_middleman can always be cut out_

similar to composition in [[category theory]]

**definition** a [[relation]] on **`A`** is said to be _transitive_ if **`RR {x, y} /\ RR {y, z} < RR {x, z}`** for all **`x`**, **`y`**, and **`z`**

## Equivalence Relation

&mdash; <https://en.wikipedia.org/wiki/Partition_of_a_set>

**definition** a [[relation]] on **`A`** is said to be an _equivalence relation_ if it is _reflexive_, _symmetric_ and _transitive_

**properties**

every _equivalence relation_ on a [[set]] induces a [[set#partition]] of that [[set]]

## Antisymmetric Relation

_distinct elements can't be related in both directions_

&mdash; <https://en.wikipedia.org/wiki/Antisymmetric_relation>

**definition** a [[relation]] on **`A`** is said to be _antisymmetric_ if **`RR {x, y} /\ RR {y, x} < x = y`** for all **`x`** and **`y`**

## Asymmetric Relation

_swapping arguments always changes the result_

&mdash; <https://en.wikipedia.org/wiki/Asymmetric_relation>

**definition** a [[relation]] on **`A`** is said to be _asymmetric_ if **`RR {x, y} < +RR {y, x}`** for all **`x`** and **`y`**

## Irreflexive Relation

_no element is related to itself_

**definition** a [[relation]] on **`A`** is said to be _irreflexive_ if **`+RR {x, x}`** for all **`x`**
