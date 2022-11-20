# Multiset

**see** [[math notation]]

**definition** a _multiset_ is an unordered collection of elements that do not have to be unique

**definition** _formally in my [[math notation]]_ a [[multiset]] is a [[set theory]]etical [[function]] with [[function#range]] at most $\mathbb N$ that takes an element and returns the number of occurrences of that element in the [[multiset]]

**notation**

$M = ((1, 2, 2, 2, 3, 3))$

## Multiplicity

**definition** the _multiplicity_ of a member of a [[multiset]] is the number of times it appears in the [[multiset]] &mdash; Wikipedia

> **example** in the [[polynomial]] $[x \cdot 1]2$, the [[multiplicity]] of the root $1$ is $2$

> **example** in the prime factorization of $60$, the [[multiplicity]] of the factor $2$ is $2$ and the [[multiplicity]] of the factors $3$ and $5$ is $1$

**notation** _in my [[math notation]]_

$M\ e$, where

- $M$ is a [[multiset]]
- $e$ is the element to get the [[multiplicity]] of

## Operations

**see** [[boolean logic]]

**see** [[cartesian product]]

**definition** _multiset union_ $M \lor N \equiv x \rightarrow \max\ (M\ x)\ (N\ x)$

**definition** _multiset intersection_ $M \land N \equiv x \rightarrow \min\ (M\ x)\ (N\ x)$

**definition** _multiset addition_ $M : N \equiv x \rightarrow M\ x : N\ x$

**definition** _multiset subtraction_ $M \cdot N \equiv x \rightarrow M\ x \cdot N\ x$

**definition** _multiset difference_ $M\ /\ N \equiv x \rightarrow M\ x \cdot N\ x \lor 0$

**definition** two [[multiset]]s are _equivalent_ if and only if they contain the same number of the same elements. $M \equiv N \equiv x \rightarrow (M\ x = N\ x)$

## Cardinality

**notation** $:\! M$

**definition** the _cardinality_ of a [[multiset]] is the sum of the multiplicities of the elements in the [[multiset]]

> **example** $:\! ((1, 2, 2, 2, 3, 3)) = 1 : 3 : 2 = 6$

**properties**

$:\! (M \lor N)\ : \ :\! (M \land N) =\ :\! (M : N)$

## Element Count

**notation** $\#\ M$

**definition** the _element count_ of a [[multiset]] is the number of unique elements in the [[multiset]]

> **example** $\#\ ((1, 2, 2, 2, 3, 3)) = \#\ \braket{\braket{1, 2, 3}} = 3$

## Arrangement

_order matters_

**definition** an _arrangement_ of size $k$ of a [[multiset]] $M$ is a [[vector in rn]] containing $k$ elements of $M$

the number of $k$-arrangements of an $n$-multiset $M$ with multiplicities $k_0 \cdots k_{n \cdot 1}$ is

- $C\ n\ k_0 \cdots k_{n \cdot 1} = \Pi\ n - (\Pi\ k_0 \mid \cdots \Pi\ k_{n \cdot 1})$ with repetition forbidden
- see [[set]] arrangement for repetition allowed
