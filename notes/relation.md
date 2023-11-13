# Relation

**see** [[set]], [[cartesian product]], [[math notation]]

**equiv** _[[graph]]_

**definition** a _relation_ **`RR`** between two [[set]]s **`A`** and **`B`** is a [[set#subset]] of the [[cartesian product]] of those [[set]]s

**definition** _formally in my [[math notation]]_ a [[relation]] is a [[set theory]]etical [[function]] that takes two objects and returns whether they are related

**definition**

**`RR a b = A a /\ B b /\ P a b`**, where

- **`RR`** is a _relation_ between elements of **`A`** and **`B`**
- **`P`** is a [[predicate]]

**notation**

_membership in my [[math notation]]_ **`RR x y`**

_membership in [[conventional math notation]]_ $x \mathcal R y$

## Inverse Relation

**equiv** _[[matrix#transpose]]_

**equiv** _[[combinator#c combinator]]_

**definition** **`rr RR`**

**notation** **`rr RR`**

## Homogenous Relation

**aka** _endorelation_, _relation on a set_

**definition** a _homogenous relation_ on a [[set]] **`A`** is a [[relation]] from **`A`** to **`A`**

## Reflexive Relation

_every element is related to itself_

**equiv** _[[category#identity law]]_

**definition** a [[relation#homogenous relation]] is said to be _reflexive_ if **`RR x x`** for all **`x`**

## Symmetric Relation

_swapping arguments never changes the result_

**equiv** _undirected [[graph]]_

**equiv** _symmetric [[matrix]]_

**equiv** _[[category#isomorphism]]_

**definition** a [[relation#homogenous relation]] is said to be _symmetric_ if **`RR x y < RR y x`** for all **`x`** and **`y`**

**definition** a [[relation#homogenous relation]] is said to be _symmetric_ if **`{= rr} RR`**

## Transitive Relation

_middleman can always be cut out_

**equiv** _[[category#composition]]_

**definition** a [[relation#homogenous relation]] is said to be _transitive_ if **`RR x y /\ RR y z < RR x z`** for all **`x`**, **`y`**, and **`z`**

## Equivalence Relation

&mdash; <https://en.wikipedia.org/wiki/Partition_of_a_set>

**definition** a [[relation#homogenous relation]] is said to be an _equivalence relation_ if it is _reflexive_, _symmetric_ and _transitive_

**properties**

every _equivalence relation_ on a [[set]] induces a [[set#partition]] of that [[set]]

## Antisymmetric Relation

_distinct elements can't be related in both directions_

&mdash; <https://en.wikipedia.org/wiki/Antisymmetric_relation>

**definition** a [[relation#homogenous relation]] is said to be _antisymmetric_ if **`RR x y /\ RR y x < x = y`** for all **`x`** and **`y`**

**properties**

an _antisymmetric relation_ is a weaker _asymmetric relation_ that allows for _reflexivity_

## Asymmetric Relation

_elements can't be related in both directions_

_if related one way then not related the other_

&mdash; <https://en.wikipedia.org/wiki/Asymmetric_relation>

**definition** a [[relation#homogenous relation]] is said to be _asymmetric_ if **`RR x y < +RR y x`** for all **`x`** and **`y`**

**definition** a [[relation#homogenous relation]] is said to be _asymmetric_ if **`{+ > rr} RR`**

**properties**

a relation is _asymmetric_ if and only if it is both _antisymmetric_ and _irreflexive_

## Irreflexive Relation

_no element is related to itself_

**definition** a [[relation#homogenous relation]] on said to be _irreflexive_ if **`+RR x x`** for all **`x`**
