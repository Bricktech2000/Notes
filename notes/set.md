# Set

see [[math-notation]]

## definition

a _set_ is an unordered collection of elements, each of which are unique

formally, in my [[math-notation]], a [[set]] is a [[set-theory]]etical [[function]] with range at most $\mathbb B$ (also known as a [[predicate]]) that takes an element and returns whether it is in the set or not

## notation

### Set Roster notation

$S = \lbrace 1, 2, 3 \rbrace$

$S = \lbrace 1, 2, 3 \dots \rbrace$ &mdash; $\dots$ are allowed

### Set Builder notation

$S\ x = P\ x$ or $S = x \rightarrow P\ x$, where

$P$ is a [[predicate]], see [[math-notation]]

in [[classical-math-notation]], this abomination: $\lbrace x \mid P(x) \rbrace$

### membership

$S\ a$ checks if $a$ is an element of $S$

## properties

[[set]]s are categories, see [[category-theory]]

$\lbrace 1, 2, 3 \rbrace = \lbrace 3, 2, 1 \rbrace = \dots$ &mdash; elements are unordered

$\lbrace 1, 1, 1 \rbrace = \lbrace 1, 1 \rbrace = \dots$ &mdash; element are unique

## examples

[[number]] sets

[[universal]] set

[[number-field]]s

[[monoid]]s

## set isomorphism

see [[category]], [[category-theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## subset

### definition

a [[set]] $A$ is a _subset_ of a [[set]] $B$ if and only if every element of $A$ is an element of $B$

in other words, an element being in $A$ implies it is also in $B$

### notation

$A \vdash B$ checks if $A$ is a subset of $B$

in [[classical-math-notation]], $A \subseteq B$ states $A$ is a subset of $B$

### examples

$\mathbb Z \vdash \mathbb R$

$\mathbb E \vdash \mathbb Z$

## empty set

_the [[set]] containing no elements_

### notation

$\lbrace \rbrace$ or $(x \rightarrow \bot)$ in my [[math-notation]]

$\lbrace \rbrace$ or $\varnothing$ in [[classical-math-notation]]

### properties

$\lbrace \rbrace \vdash A$, for all [[set]] $A$

## [[universal]]

_the [[set]] of all possible mathematical entities_

see [[universal]]

## set power set

### definition

the _power set_ of a [[set]] $A$ is the [[set]] of all sub[[set]]s of $A$

### examples

let $P\ A$ be the power set of $A$ and let $O = \lbrace \rbrace$

$P\ \lbrace 1, 2, 3 \rbrace = \lbrace \lbrace 1 \rbrace, \lbrace 2 \rbrace, \lbrace 3 \rbrace, \lbrace 1, 2 \rbrace, \lbrace 2, 3 \rbrace, \lbrace 1, 3 \rbrace, \lbrace 1, 2, 3 \rbrace, \lbrace \rbrace \rbrace$

$P\ O = \lbrace O \rbrace$

$P\ P\ O = \lbrace O, \lbrace O \rbrace \rbrace$
