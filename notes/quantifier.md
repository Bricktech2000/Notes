# Quantifier

see [[math-notation]], [[boolean-logic]]

> **definition**: In [[boolean-logic]], a _quantifier_ is an operator that specifies how many individuals in the domain of discourse satisfy an open formula. &mdash; Wikipedia

> **note**: an _open formula_ is an expression with at least one free variable, see [[linear-system]]

## Universal Quantifier

_expresses that every item in the domain satisfies a condition_

### notation

in my [[math-notation]]: $P\ x \dashv \mathbb R x$

in [[classical-math-notation]]: $\forall x \in \mathbb R, P(x)$

## Existential Quantifier

_expresses that at least one item in the domain satisfies a condition_

### notation

in my [[math-notation]]: $P\ x \land \mathbb R x$

in [[classical-math-notation]]: $\exists x \in \mathbb R, P(x)$

## quantifier negation

$B \vdash C \equiv /B \lor C$ means “for all $B$, $C$”. negating, we get $/(B \vdash C) \equiv B \land /C$, which means “there exists a $B$ such that $/C$”

the inverse is true
