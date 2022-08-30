# Relation

see [[set]], [[cartesian-product]], [[math-notation]]

> **definition**: a _relation_ $\mathcal R$ between two [[set]]s $A$ and $B$ is a subset of the [[cartesian-product]] of the two [[set]]s: $\mathcal R \vdash A\ \acute\mid\ B$

> **definition**:
>
> $\mathcal R\ x = (A\ \acute\mid\ B)\ x \land P\ x$, where
>
> - $\mathcal R$ is a _relation_ between elements of $A$ and $B$
> - $P$ is a [[predicate]]

> **definition**: a _relation on a set_ $A$ is a [[relation]] from $A$ to $A$

> **notation**: _membership in my [[math-notation]]_ $\mathcal R \braket{x, y}$, see [[ordered-pair]]

> **notation**: _membership in my [[math-notation]]_ $x \mathcal R y$

## Inverse Relation

> **definition**:
>
> let $\mathcal R^-$ be the inverse of the [[relation]] $\mathcal R$ from $A$ to $B$
>
> then, $\mathcal R \braket{x, y} \equiv \mathcal R^- \braket{y, x}$

> **property**: $\mathcal R^- \vdash B\ \acute\mid\ A$

## reflexivity

similar to identities in [[category-theory]]

> **definition**: a [[relation]] on $A$ is said to be _reflexive_ if $\mathcal R \braket{x, x} \dashv A x$

## symmetricality

similar to isomorphisms in [[category-theory]]

> **definition**: a [[relation]] on $A$ is said to be _symmetric_ if $\mathcal R \braket{x, y} \vdash \mathcal R \braket{y, x}$

## transitivity

similar to composition in [[category-theory]]

> **definition**: a [[relation]] on $A$ is said to be _transitive_ if $\mathcal R \braket{x, y} \land \mathcal R \braket{y, z} \vdash \mathcal R \braket{x, z}$

## equivalence

> **definition**: a [[relation]] on $A$ is said to be _equivalent_ if it is _reflexive_, _symmetric_ and _transitive_
