# Predicate

_a [[function]] that returns a [[boolean]]_

&mdash; <https://youtu.be/aIOMRqiwziM?t=560>

## definitions

see [[logic-statement]], [[math-notation]]

let $f$ be a [[predicate]]. then, $\mathbb B f\ x \dashv x$

in [[discrete-mathematics]], a _predicate_ is a sentence depending on variables which becomes a [[logic-statement]] upon substituting values in the domain. $x = 5$ is a predicate and would become a [[logic-statement]] by substituting $x = 3$. quantifying a [[predicate]] (with $\exists$ or $\forall$) turns it into a [[logic-statement]].

## examples

in Haskell, the library `Data.Char` is full of [[predicate]]s such as `isAlpha` or `isDigit`.

in my [[math-notation]], [[set]]s are [[predicate]]s

## Truth Set

see [[math-notation]], [[set]], [[predicate]]

> **definition**: the _truth set_ of a [[predicate]] is the set of all possible values making the [[predicate]] a true [[logic-statement]]. $x \rightarrow P\ x$, where $P\ x$ is a [[predicate]] and $x$ is a value of the domain of the [[predicate]]

> **note**: in my [[math-notation]], as [[set]]s are [[predicate]]s, a [[predicate]] is its own truth set: $x \rightarrow P\ x \equiv P$
