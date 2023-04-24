# Relation

**see** [[set]], [[cartesian product]], [[math notation]]

**definition**

a _relation_ **`rr`** between two [[set]]s **`A`** and **`B`** is a [[set#subset]] of the [[cartesian product]] of the two [[set]]s: **`/\ rr -| (__ {A, B} *)`**

**definition**

**`rr {a, b} = A a /\ B b /\ P {a, b}`**, where

- **`rr`** is a _relation_ between elements of **`A`** and **`B`**
- **`P`** is a [[predicate]]

**definition** a _relation on a set_ **`A`** is a [[relation]] from **`A`** to **`A`**

**notation**

_membership in my [[math notation]]_ **`rr {x, y}`**, see [[ordered pair]]

_membership in [[conventional math notation]]_ $x \mathcal R y$

## Inverse Relation

**definition**

let **`rr^-`** be the inverse of the [[relation]] **`rr`** from **`A`** to **`B`**

then, **`rr {x, y} = rr^- {y, x}`**

**properties**

**`/\ rr^- -| (__ {B, A} *)`**

#todo **equivalence** for the three sections below

## Reflexive Relation

similar to identities in [[category theory]]

**definition** a [[relation]] on **`A`** is said to be _reflexive_ if **`rr {x, x}`** for all **`x`**

## Symmetric Relation

similar to isomorphisms in [[category theory]]

**definition** a [[relation]] on **`A`** is said to be _symmetric_ if **`rr {x, y} < rr {y, x}`** for all **`x`** and **`y`**

## Transitive Relation

similar to composition in [[category theory]]

**definition** a [[relation]] on **`A`** is said to be _transitive_ if **`rr {x, y} /\ rr {y, z} < rr {x, z}`** for all **`x`**, **`y`**, and **`z`**

## Equivalence Relation

**definition** a [[relation]] on **`A`** is said to be an _equivalence relation_ if it is _reflexive_, _symmetric_ and _transitive_

## Antisymmetric Relation

&mdash; <https://en.wikipedia.org/wiki/Antisymmetric_relation>

**definition** a [[relation]] on **`A`** is said to be _antisymmetric_ if **`rr {x, y} /\ rr {y, x} < x = y`** for all **`x`** and **`y`**

## Asymmetric Relation

&mdash; <https://en.wikipedia.org/wiki/Asymmetric_relation>

**definition** a [[relation]] on **`A`** is said to be _asymmetric_ if **`rr {x, y} < +rr {y, x}`** for all **`x`** and **`y`**
