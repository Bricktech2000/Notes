# Relation

**see** [[set]], [[cartesian product]], [[math notation]]

**definition**

a _relation_ $\mathcal R$ between two [[set]]s $A$ and $B$ is a [[set#subset]] of the [[cartesian product]] of the two [[set]]s: $\,\land\ \mathcal R \dashv \braket{A\ \dot,\ B}$

**definition**

$\mathcal R\ x = \braket{A\ \dot,\ B}\ x \land P\ x$, where

- $\mathcal R$ is a _relation_ between elements of $A$ and $B$
- $P$ is a [[predicate]]

**definition** a _relation on a set_ $A$ is a [[relation]] from $A$ to $A$

**notation**

_membership in my [[math notation]]_ $\mathcal R \braket{x, y}$, see [[ordered pair]]

_membership in my [[math notation]]_ $x \mathcal R y$

## Inverse Relation

**definition**

let $\mathcal R^\times$ be the inverse of the [[relation]] $\mathcal R$ from $A$ to $B$

then, $\mathcal R \braket{x, y} = \mathcal R^\times \braket{y, x}$

**properties**

$\,\land\ \mathcal R^\times \dashv \braket{B\ \dot,\ A}$

#todo **equivalence** for the three following sections

## Reflexive Relation

similar to identities in [[category theory]]

**definition** a [[relation]] on $A$ is said to be _reflexive_ if $\mathcal R \braket{x, x}$ for all $x$

## Symmetric Relation

similar to isomorphisms in [[category theory]]

**definition** a [[relation]] on $A$ is said to be _symmetric_ if $\mathcal R \braket{x, y} < \mathcal R \braket{y, x}$ for all $x$ and $y$

## Transitive Relation

similar to composition in [[category theory]]

**definition** a [[relation]] on $A$ is said to be _transitive_ if $\mathcal R \braket{x, y} \land \mathcal R \braket{y, z} < \mathcal R \braket{x, z}$ for all $x$, $y$, and $z$

## Equivalent Relation

**definition** a [[relation]] on $A$ is said to be _equivalent_ if it is _reflexive_, _symmetric_ and _transitive_
