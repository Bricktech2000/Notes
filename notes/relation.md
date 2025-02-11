# Relation

**see** [[set]], [[math notation]]

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

## Homogeneous Relation

**aka** _endorelation_, _relation on a set_

**definition** a _homogeneous relation_ on a [[set]] **`A`** is a [[relation]] from **`A`** to **`A`**

## Reflexive Relation

_every element is related to itself_

**equiv** _[[category#identity law]]_

**definition** a [[relation#homogeneous relation]] is said to be _reflexive_ if **`RR x x`** for all **`x`**

### Reflexive Closure

**definition** the _reflexive closure_ of a [[relation]] is the smallest [[relation#reflexive relation]] that contains it --- Wikipedia

**definition** the _reflexive closure_ of a [[relation]] **`R`** is **`R \/ {=}`**

## Symmetric Relation

_swapping arguments never changes the result_

**equiv** _undirected [[graph]]_

**equiv** _symmetric [[matrix]]_

**equiv** _[[category#isomorphism]]_

**definition** a [[relation#homogeneous relation]] is said to be _symmetric_ if **`RR x y < RR y x`** for all **`x`** and **`y`**

**definition** a [[relation#homogeneous relation]] is said to be _symmetric_ if **`{= rr} RR`**

### Symmetric Closure

**definition** the _symmetric closure_ of a [[relation]] is the smallest [[relation#symmetric relation]] that contains it --- Wikipedia

**definition** the _symmetric closure_ of a [[relation]] **`R`** is **`{\/ rr} R`**

## Transitive Relation

_middleman can always be cut out_

**equiv** _[[category#composition]]_

**definition** a [[relation#homogeneous relation]] is said to be _transitive_ if **`RR x y /\ RR y z < RR x z`** for all **`x`**, **`y`**, and **`z`**

### Transitive Closure

**definition** the _transitive closure_ of a [[relation]] is the smallest [[relation#transitive relation]] that contains it --- Wikipedia

## Equivalence Relation

--- <https://en.wikipedia.org/wiki/Partition_of_a_set>

**definition** a [[relation#homogeneous relation]] is said to be an _equivalence relation_ if it is _reflexive_, _symmetric_ and _transitive_

**properties**

every _equivalence relation_ on a [[set]] induces a [[set#partition]] of that [[set]]

## Antisymmetric Relation

_distinct elements can't be related in both directions_

_if related both ways then must be identical_

--- <https://en.wikipedia.org/wiki/Antisymmetric_relation>

**definition** a [[relation#homogeneous relation]] is said to be _antisymmetric_ if **`RR x y /\ RR y x < x = y`** for all **`x`** and **`y`**

**properties**

an _antisymmetric relation_ is a weaker _asymmetric relation_ that allows for _reflexivity_

## Asymmetric Relation

_elements can't be related in both directions_

_if related one way then not related the other_

--- <https://en.wikipedia.org/wiki/Asymmetric_relation>

**definition** a [[relation#homogeneous relation]] is said to be _asymmetric_ if **`RR x y < +RR y x`** for all **`x`** and **`y`**

**definition** a [[relation#homogeneous relation]] is said to be _asymmetric_ if **`{+ > rr} RR`**

**properties**

a relation is _asymmetric_ if and only if it is both _antisymmetric_ and _irreflexive_

## Irreflexive Relation

_no element is related to itself_

**definition** a [[relation#homogeneous relation]] on said to be _irreflexive_ if **`+RR x x`** for all **`x`**

## Connected Relation

_distinct elements are related in at least one direction_

--- <https://en.wikipedia.org/wiki/Connected_relation>

**definition** a [[relation#homogeneous relation]] is said to be _connected_ if **`x + y < {\/ rr} RR x y`** for all **`x`** and **`y`**

**properties**

a _connected relation_ is a weaker _strongly connected relation_ that allows for _irreflexivity_ --- me

## Strongly Connected Relation

_elements are related in at least one direction_

--- <https://en.wikipedia.org/wiki/Connected_relation>

**definition** a [[relation#homogeneous relation]] is said to be _strongly connected_ if **`{\/ rr} RR x y`** for all **`x`** and **`y`**
