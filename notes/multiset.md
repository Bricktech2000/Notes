# Multiset

see [[math-notation]]

**definition** a _multiset_ is an unordered collection of elements that do not have to be unique

**definition** _formally in my [[math-notation]]_ a [[multiset]] is a [[set-theory]]etical [[function]] with range at most $\mathbb N$ that takes an element and returns the number of occurrences of that element in the [[multiset]]

**notation**

$M = ((1, 2, 2, 2, 3, 3))$

## Multiset Multiplicity

**definition** the _multiplicity_ of a member of a [[multiset]] is the number of times it appears in the [[multiset]] &mdash; Wikipedia

> **example** in the [[polynomial]] $[x \cdot 1]2$, the [[multiplicity]] of the root $1$ is $2$

> **example** in the prime factorization of $60$, the [[multiplicity]] of the factor $2$ is $2$ and the [[multiplicity]] of the factors $3$ and $5$ is $1$

**notation** _in my [[math-notation]]_

$M\ e$, where

- $M$ is a [[multiset]]
- $e$ is the element to get the [[multiplicity]] of

## Multiset Operations

**see** [[boolean-logic]]

**see** [[cartesian-product]]

## Multiset Union and Intersection

**definition** _multiset union_ $M \lor N \equiv x \rightarrow \max\ (M\ x)\ (N\ x)$

**definition** _multiset intersection_ $M \land N \equiv x \rightarrow \min\ (M\ x)\ (N\ x)$

**definition** _multiset addition_ $M : N \equiv x \rightarrow M\ x : N\ x$

**definition** _multiset subtraction_ $M \cdot N \equiv x \rightarrow M\ x \cdot N\ x$

**definition** _multiset difference_ $M\ /\ N \equiv x \rightarrow M\ x \cdot N\ x \lor 0$

**definition** two [[multiset]]s are _equivalent_ if and only if they contain the same number of the same elements. $M \equiv N \equiv x \rightarrow M\ x = N\ x$

## Multiset Cardinality

**notation**

$M^\#$

**definition** the _cardinality_ of a [[multiset]] is the sum of the multiplicities of the elements in the [[multiset]]

> **example** $((1, 2, 2, 2, 3, 3))^\# = 1 : 3 : 2 = 6$

**properties**

$(M \lor N)^\# : (M \land N)^\# = (M : N)^\#$
