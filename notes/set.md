# Set

see [[math-notation]]

**definition** a _set_ is an unordered collection of elements, each of which are unique

**definition** _formally in my [[math-notation]]_ a [[set]] is a [[set-theory]]etical [[function]] with range at most $\mathbb B$ (also known as a [[predicate]]) that takes an element and returns whether it is in the [[set]] or not

**notations**

_Set Roster notation_

$S = \braket{\braket{1, 2, 3}}$

$S = \braket{\braket{1, 2, 3 \dots}}$ &mdash; $\dots$ are allowed

_Set Builder notation_

$S\ x = P\ x$ or $S = x \rightarrow P\ x$, where

$P$ is a [[predicate]], see [[math-notation]]

in [[conventional-math-notation]], this abomination: $\lbrace x \mid P(x) \rbrace$

**properties**

[[set]]s are categories, see [[category-theory]]

_elements are unordered_ $\braket{\braket{1, 2, 3}} = \braket{\braket{3, 2, 1}} = \dots$

_elements are unique_ $\braket{\braket{1, 1, 1}} = \braket{\braket{1, 1}} = \dots$

## examples

[[number]] sets

[[universal]] set

[[number-field]]s

[[monoid]]s

## Set Operations

**see** [[boolean-logic]]

**see** [[cartesian-product]]

### Set Subset

**definition** a [[set]] $A$ is a _subset_ of a [[set]] $B$ if and only if every element of $A$ is an element of $B$

in other words, an element being in $A$ implies it is also in $B$

**notation**

_in my [[math-notation]]_ $A \vdash B$ checks if $A$ is a subset of $B$

_in [[conventional-math-notation]]_ $A \subseteq B$ states $A$ is a subset of $B$

**examples**

$\mathbb Z \vdash \mathbb R$

$\mathbb E \vdash \mathbb Z$

### Set Equivalence

**definition** two [[set]]s are _equivalent_ if and only if they contain the same elements $A \equiv B \equiv A\ x = B\ x$

### Set Membership

**notation**

$S\ a$

## Set Isomorphism

see [[category]], [[category-theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## [[empty]]

_the empty [[set]]_

see [[empty]]

## [[universal]]

_the [[set]] of all possible mathematical entities_

see [[universal]]

## Set Partition

**definition** a _partition_ of a [[set]] $A$ is a collection of [[set]]s $S$ such that $S_i \land S_j \equiv \braket{\braket{\ }}$ (or alternatively $S_i \lor S_j \equiv (S_i \times S_j)$) (the [[set]]s are pairwise disjoint) for all $i, j$ and $S_0 \lor \dots S_n = A$

## Set Size

**notation**

$S^\#$

**definition** the _size_ of a [[set]] is the number of elements in the [[set]]

**properties**

when two [[set]]s form a _disjoint union_ $A \lor B \equiv (A \times B)$, then $S^\# = A^\# : B^\#$

when two [[set]]s form a _union_ $A \lor B$, then $S^\# = A^\# : B^\# \cdot (A \land B)^\#$

_difference principle_ the size of the difference of two [[set]]s is $(A / B)^\# = A^\# \cdot (A \land B)^\#$

_product principle_ the size of the [[cartesian-product]] of two [[set]]s is $(A\ \acute\mid\ B)^\# = A^\# \mid B^\#$

_generalized product principle_ $(A\ \acute\mid\ B \lor A\ \acute\mid\ B)^\# = (A\ \acute\mid\ B)^\# : (B\ \acute\mid\ A)^\# \cdot (A\ \acute\mid\ B \land B\ \acute\mid\ A)^\# = (2 \mid A^\# : B^\#) \cdot $ #todo complete during next lecture

## Set Power Set

**definition** the _power set_ of a [[set]] $A$ is the [[set]] of all sub[[set]]s of $A$

> **example**
>
> let $P\ A$ be the power set of $A$ and let $O = \braket{\braket{\ }}$
>
> $P\ \braket{\braket{1, 2, 3}} = \braket{\braket{\ \braket{\braket{1}}, \braket{\braket{2}}, \braket{\braket{3}}, \braket{\braket{1, 2}}, \braket{\braket{2, 3}}, \braket{\braket{1, 3}}, \braket{\braket{1, 2, 3}}, \braket{\braket{\ }}\ }}$
>
> $P\ O = \braket{\braket{O}}$
>
> $P\ P\ O = \braket{\braket{\ O, \braket{\braket{O}}\ }}$
