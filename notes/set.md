# Set

see [[math-notation]]

## definition

a _set_ is an unordered collection of elements, each of which are unique

formally, in my [[math-notation]], a [[set]] is a [[set-theory]]etical [[function]] with range at most $\mathbb B$ (also known as a [[predicate]]) that takes an element and returns whether it is in the [[set]] or not

## notation

### Set Roster notation

$S = \braket{\braket{1, 2, 3}}$

$S = \braket{\braket{1, 2, 3 \dots}}$ &mdash; $\dots$ are allowed

### Set Builder notation

$S\ x = P\ x$ or $S = x \rightarrow P\ x$, where

$P$ is a [[predicate]], see [[math-notation]]

in [[conventional-math-notation]], this abomination: $\lbrace x \mid P(x) \rbrace$

### membership

$S\ a$ checks if $a$ is an element of $S$

## properties

[[set]]s are categories, see [[category-theory]]

$\braket{\braket{1, 2, 3}} = \braket{\braket{3, 2, 1}} = \dots$ &mdash; elements are unordered

$\braket{\braket{1, 1, 1}} = \braket{\braket{1, 1}} = \dots$ &mdash; element are unique

## examples

[[number]] sets

[[universal]] set

[[number-field]]s

[[monoid]]s

## set isomorphism

see [[category]], [[category-theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## Subset

### definition

a [[set]] $A$ is a _subset_ of a [[set]] $B$ if and only if every element of $A$ is an element of $B$

in other words, an element being in $A$ implies it is also in $B$

### notation

$A \vdash B$ checks if $A$ is a subset of $B$

in [[conventional-math-notation]], $A \subseteq B$ states $A$ is a subset of $B$

### examples

$\mathbb Z \vdash \mathbb R$

$\mathbb E \vdash \mathbb Z$

## Empty Set

_the [[set]] containing no elements_

### notation

$\braket{\braket{\ }}$ or $(x \rightarrow \bot)$ in my [[math-notation]]

$\lbrace \rbrace$ or $\varnothing$ in [[conventional-math-notation]]

### properties

$\braket{\braket{\ }} \vdash A$, for all [[set]] $A$

## [[universal]]

_the [[set]] of all possible mathematical entities_

see [[universal]]

## set Power Set

### definition

the _power set_ of a [[set]] $A$ is the [[set]] of all sub[[set]]s of $A$

### examples

let $P\ A$ be the power set of $A$ and let $O = \braket{\braket{\ }}$

$P\ \braket{\braket{1, 2, 3}} = \braket{\braket{\ \braket{\braket{1}}, \braket{\braket{2}}, \braket{\braket{3}}, \braket{\braket{1, 2}}, \braket{\braket{2, 3}}, \braket{\braket{1, 3}}, \braket{\braket{1, 2, 3}}, \braket{\braket{\ }}\ }}$

$P\ O = \braket{\braket{O}}$

$P\ P\ O = \braket{\braket{\ O, \braket{\braket{O}}\ }}$
