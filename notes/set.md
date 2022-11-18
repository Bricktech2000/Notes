# Set

**see** [[abstract data type]]

**see** [[math notation]]

**definition** a _set_ is an unordered collection of elements, each of which are unique

**definition** _formally in my [[math notation]]_ a [[set]] is a [[set theory]]etical [[function]] with range at most $\mathbb B$ (also known as a [[predicate]]) that takes an element and returns whether it is in the [[set]] or not

**notations**

_Set Roster notation_

$S = \braket{\braket{1, 2, 3}}$

$S = \braket{\braket{1, 2, 3 \cdots}}$ &mdash; $\cdots$ are allowed

_Set Builder notation_

$S\ x = P\ x$ or $S = x \rightarrow P\ x$, where

$P$ is a [[predicate]], see [[math notation]]

in [[conventional math notation]], this abomination: $\lbrace x \mid P(x) \rbrace$

**types**

[[binary search tree]] [[set]]

[[hash table]] [[set]]

**properties**

[[set]]s are categories, see [[category theory]]

_elements are unordered_ $\braket{\braket{1, 2, 3}} = \braket{\braket{3, 2, 1}} = \dots$

_elements are unique_ $\braket{\braket{1, 1, 1}} = \braket{\braket{1, 1}} = \dots$

**see**

[[number]] sets

[[universal]] set

[[number field]]s

[[monoid]]s

## Set Operations

**see** [[boolean logic]]

**see** [[cartesian product]]

### Subset

**definition** a [[set]] $A$ is a _subset_ of a [[set]] $B$ if and only if every element of $A$ is an element of $B$

in other words, an element being in $A$ implies it is also in $B$

**notation**

_in my [[math notation]]_ $A \vdash B$ checks if $A$ is a subset of $B$

_in [[conventional math notation]]_ $A \subseteq B$ states $A$ is a subset of $B$

**examples**

$\mathbb Z \vdash \mathbb R$

$\mathbb E \vdash \mathbb Z$

### Set Equivalence

**definition** two [[set]]s are _equivalent_ if and only if they contain the same elements $A \equiv B \equiv A\ x = B\ x$

### Set Membership

**notation**

$S\ a$

## Set Isomorphism

**see** [[category]], [[category theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## [[empty]]

_the empty [[set]]_

**see** [[empty]]

## [[universal]]

_the [[set]] of all possible mathematical entities_

**see** [[universal]]

## Set Partition

**definition** a _partition_ of a [[set]] $A$ is a collection of [[set]]s $S$ such that $S^i \land S^j \equiv \braket{\ }$ for all $i, j$ (the [[set]]s are pairwise disjoint) and $\lor\!\ S = A$

**definition** a _partition_ of a [[set]] $A$ is a collection of [[set]]s $S$ such that $A =\ :\! S$

## Set Cardinality

**notation**

$\#\ S$

**definition** the _cardinality_ of a [[set]] is the number of elements in the [[set]]

**properties**

when two [[set]]s form a _disjoint union_ $A : B$, then $\#\ S = \#\ A : \#\ B$

when two [[set]]s form a _union_ $A \lor B$, then $\#\ S = \#\ A : \#\ B \cdot \#\ (A \land B)$

_difference principle_ the cardinality of the difference of two [[set]]s is $\#\ (A / B) = \#\ A \cdot \#\ (A \land B)$

_product principle_ the cardinality of the [[cartesian product]] of two [[set]]s is $\#\ A\ \acute\shortmid\ B = \#\ A \mid \#\ B$

_generalized product principle_ $\#\ (A\ \acute\shortmid\ B \lor A\ \acute\shortmid\ B) = \#\ A\ \acute\shortmid\ B : \#\ B\ \acute\shortmid\ A \cdot \#\ (A\ \acute\shortmid\ B \land B\ \acute\shortmid\ A) = (2 \mid \#\ A : \#\ B) \cdot $ #todo complete during next lecture

## Set Power Set

**definition** the _power set_ of a [[set]] $A$ is the [[set]] of all sub[[set]]s of $A$

> **example**
>
> let $P\ A$ be the power set of $A$ and let $O = \braket{\ }$
>
> $P\ \braket{\braket{1, 2, 3}} = \braket{\braket{\ \braket{\braket{1}}, \braket{\braket{2}}, \braket{\braket{3}}, \braket{\braket{1, 2}}, \braket{\braket{2, 3}}, \braket{\braket{1, 3}}, \braket{\braket{1, 2, 3}}, \braket{\ }\ }}$
>
> $P\ O = \braket{\braket{O}}$
>
> $P\ P\ O = \braket{\braket{\ O, \braket{\braket{O}}\ }}$

## Set Arrangement

_order matters_

**definition** an _arrangement_ of size $k$ of a [[set]] $A$ is a [[vector in rn]] containing $k$ elements of $A$

the number of $k$-arrangements of an $n$-set is

- $P\ n\ k = \Pi\ n - \Pi\ (n \cdot k)$ with repetition forbidden. also called _.$k$-permutations_
- $P'\ n\ k = [n]k$ with repetition allowed also called _.$k$-tuples_

## Set Combination

_order does not matter_

**definition** a _combination_ of size $k$ of a [[set]] $A$ is a [[multiset]] containing $k$ elements of $A$

the number of $k$-combinations of an $n$-set is

- $C\ n\ k = P\ n\ k - P\ k\ k = \Pi\ n - \Pi\ (n \cdot k) - \Pi\ k$ with repetition forbidden. also called _.$k$-subsets_
- $C'\ n\ k = C\ (n : k \cdot 1)\ (k \cdot 1)$ with repetition allowed. also called _.$k$-multisubsets_

> **proof** _stars and bars [[proof]] sketch_
>
> given a [[multiset]] of elements,
>
> $a\ e\ b\ a\ d\ b\ b\ a\ c\ e$
>
> rewriting in order as order does not matter,
>
> $a\ a\ a\ b\ b\ b\ c\ d\ e\ e$
>
> represented as _stars and bars_,
>
> $\cdot \cdot \cdot \mid \cdot \cdot \cdot \mid \cdot \mid \cdot \mid \cdot\ \cdot$
>
> there are $n : k \cdot 1$ choose $k \cdot 1$ ways to arrange the bars

> **proof** _alternative [[proof]] sketch with bijections_
>
> the following are equivalent:
>
> - the number of $k$-combinations from an $n$-[[set]] with repetition allowed
> - the number of $k$-[[multiset]]s from an $n$-[[set]]
> - the number of ways of distributing $n$ identical marbles into $k$ distinguishable boxes
> - the number of solutions to $:\! x = n$ with $\mathbb N x^i$ for all $i$
> - the number of $n$-sub[[set]]s of an $n : k \cdot 1$-[[set]]
> - the number of $k \cdot 1$-sub[[set]]s of an $n : k \cdot 1$-[[set]]

**theorem**

$C\ n\ k = C\ n\ (n \cdot k)$

## theorems

**theorem**

- let $P\ n\ k$ be the $k$-permutations of an $n$-[[set]]
- let $C\ n\ k$ be the $k$-subsets of an $n$-[[set]]
- let $P\ k\ k$ be the $k$-permutations of a $k$-[[set]]

then, there exists a bijection between $P\ n\ k$ and $C\ n\ k\ \acute\mid\ P\ k\ k$

moreover, $\#\ C\ n\ k = \#\ C\ n\ (n \cdot k)$. the number of $k$-subsets of an $n$-[[set]] is equal to the number of $n \cdot k$-subsets of an $n$-[[set]]
