# Relation

**see** [[set]], [[cartesian product]], [[math notation]]

**definition**

a _relation_ $\mathcal R$ between two [[set]]s $A$ and $B$ is a [[set#subset]] of the [[cartesian product]] of the two [[set]]s: $\,\land\ \mathcal R \dashv (\bot \braket{A, B}\ \circ)$

**definition**

$\mathcal R \braket{a, b} = A\ a \land B\ b \land P\ \braket{a, b}$, where

- $\mathcal R$ is a _relation_ between elements of $A$ and $B$
- $P$ is a [[predicate]]

**definition** a _relation on a set_ $A$ is a [[relation]] from $A$ to $A$

**notation**

_membership in my [[math notation]]_ $\mathcal R \braket{x, y}$, see [[ordered pair]]

_membership in [[conventional math notation]]_ $x \mathcal R y$

## Inverse Relation

**definition**

let $\mathcal R^\times$ be the inverse of the [[relation]] $\mathcal R$ from $A$ to $B$

then, $\mathcal R \braket{x, y} = \mathcal R^\times \braket{y, x}$

**properties**

$\,\land\ \mathcal R^\times \dashv (\bot \braket{B, A}\ \circ)$

#todo **equivalence** for the three sections below

## Reflexive Relation

similar to identities in [[category theory]]

**definition** a [[relation]] on $A$ is said to be _reflexive_ if $\mathcal R \braket{x, x}$ for all $x$

## Symmetric Relation

similar to isomorphisms in [[category theory]]

**definition** a [[relation]] on $A$ is said to be _symmetric_ if $\mathcal R \braket{x, y} < \mathcal R \braket{y, x}$ for all $x$ and $y$

## Transitive Relation

similar to composition in [[category theory]]

**definition** a [[relation]] on $A$ is said to be _transitive_ if $\mathcal R \braket{x, y} \land \mathcal R \braket{y, z} < \mathcal R \braket{x, z}$ for all $x$, $y$, and $z$

## Equivalence Relation

**definition** a [[relation]] on $A$ is said to be an _equivalence relation_ if it is _reflexive_, _symmetric_ and _transitive_

## Antisymmetric Relation

&mdash; <https://en.wikipedia.org/wiki/Antisymmetric_relation>

**definition** a [[relation]] on $A$ is said to be _antisymmetric_ if $\mathcal R \braket{x, y} \land \mathcal R \braket{y, x} < x = y$ for all $x$ and $y$

## Asymmetric Relation

&mdash; <https://en.wikipedia.org/wiki/Asymmetric_relation>

**definition** a [[relation]] on $A$ is said to be _asymmetric_ if $\mathcal R \braket{x, y} < + \mathcal R \braket{y, x}$ for all $x$ and $y$
