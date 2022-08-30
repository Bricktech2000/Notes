# Set

see [[math-notation]]

> **definition**: a _set_ is an unordered collection of elements, each of which are unique

> **definition**: _formally in my [[math-notation]]_
>
> a [[set]] is a [[set-theory]]etical [[function]] with range at most $\mathbb B$ (also known as a [[predicate]]) that takes an element and returns whether it is in the [[set]] or not

> **notation**: _Set Roster notation_
>
> $S = \braket{\braket{1, 2, 3}}$
>
> $S = \braket{\braket{1, 2, 3 \dots}}$ &mdash; $\dots$ are allowed

> **notation**: _Set Builder notation_
>
> $S\ x = P\ x$ or $S = x \rightarrow P\ x$, where
>
> $P$ is a [[predicate]], see [[math-notation]]
>
> in [[conventional-math-notation]], this abomination: $\lbrace x \mid P(x) \rbrace$

> **notation**: _set membership_ $S\ a$

> **property**: [[set]]s are categories, see [[category-theory]]

> **property**: _elements are unordered_ $\braket{\braket{1, 2, 3}} = \braket{\braket{3, 2, 1}} = \dots$

> **property**: _elements are unique_ $\braket{\braket{1, 1, 1}} = \braket{\braket{1, 1}} = \dots$

## examples

[[number]] sets

[[universal]] set

[[number-field]]s

[[monoid]]s

## Set Isomorphism

see [[category]], [[category-theory]]

two [[set]]s are isomorphic if they contain the same elements "labeled" in different ways

&mdash; <https://youtu.be/yAi3XWCBkDo?t=998>

## Subset

> **definition**: a [[set]] $A$ is a _subset_ of a [[set]] $B$ if and only if every element of $A$ is an element of $B$

in other words, an element being in $A$ implies it is also in $B$

> **notation**: _in my [[math-notation]]_ $A \vdash B$ checks if $A$ is a subset of $B$

> **notation**: _in [[conventional-math-notation]]_ $A \subseteq B$ states $A$ is a subset of $B$

> **example**: $\mathbb Z \vdash \mathbb R$

> **example**: $\mathbb E \vdash \mathbb Z$

## Empty Set

_the [[set]] containing no elements_

> **notation**: _in my [[math-notation]]_ $\braket{\braket{\ }}$ or $(x \rightarrow \bot)$

> **notation**: _in [[conventional-math-notation]]_ $\lbrace \rbrace$ or $\varnothing$ =

> **property**: $\braket{\braket{\ }} \vdash A$, for all [[set]] $A$

## [[universal]]

_the [[set]] of all possible mathematical entities_

see [[universal]]

## Set Power Set

> **definition**: the _power set_ of a [[set]] $A$ is the [[set]] of all sub[[set]]s of $A$

> **example**:
>
> let $P\ A$ be the power set of $A$ and let $O = \braket{\braket{\ }}$
>
> $P\ \braket{\braket{1, 2, 3}} = \braket{\braket{\ \braket{\braket{1}}, \braket{\braket{2}}, \braket{\braket{3}}, \braket{\braket{1, 2}}, \braket{\braket{2, 3}}, \braket{\braket{1, 3}}, \braket{\braket{1, 2, 3}}, \braket{\braket{\ }}\ }}$
>
> $P\ O = \braket{\braket{O}}$
>
> $P\ P\ O = \braket{\braket{\ O, \braket{\braket{O}}\ }}$
