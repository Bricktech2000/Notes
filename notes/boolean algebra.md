## Boolean Algebra

**see** [[boolean]]

**see** [[math notation]], [[disjunctive normal form]], [[conjunctive normal form]], [[quantifier]], [[algebraic structure]]

**definition** two boolean expressions (or [[logic statement]]s) are said to be _logically equivalent_ if they yield the same output for every input. in other words, two boolean expressions (or [[logic statement]]s) are _logically equivalent_ if they share the same [[truth table]]

boolean expressions can be simplified to a different but logically equivalent expression using [[boolean algebra]] through [[boolean algebra#operators]], or alternatively visually using [[karnaugh map]]s or [[truth table]]s

---

# Operators

**see** [[boolean]], [[boolean algebra]]

boolean [[operator]]s can be modeled in [[logic circuit]]s through [[logic gate]]s

## operator precedence

see [[math notation]] for [[operator]] precedence in my [[math notation]]

in [[conventional math notation]]: $' \cdot + \oplus$

## AND

**aka** _Conjunction, $\min$_

**notations**

_in my [[math notation]]_ $\land$ and $\bot$

_in [[conventional math notation]]_ $\cdot$ or $\cap$ (may be omitted)

**representation**

straight-curve [[logic gate]]. may take more than one input

| $A$ | $B$ | $A \land B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

## OR

**aka** _Disjunction, $\max$_

**notations**

_in my [[math notation]]_ $\lor$ and $\top$

_in [[conventional math notation]]_ $+$ or $\cup$

**representation**

concave-pointycurve [[logic gate]]. may take more than one input

| $A$ | $B$ | $A \lor B$ |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

## NOT

**aka** _Negation_

**notations**

_in my [[math notation]]_ $\times$ and $+$

_in [[conventional math notation]]_ $a'$ or $\bar a$ or $a^c$

**representation**

triangle-circle [[logic gate]]. may only take one input

| $A$ | $+A$ |
| --- | ---- |
| 0   | 1    |
| 1   | 0    |

**properties**

## XOR

**aka** _Exclusive OR, symmetric difference, disjunctive union_

**notations**

_in my [[math notation]]_ $\times$ and $+$

_in [[conventional math notation]]_ $\oplus$ or $\vartriangle$

**representation**

doubleconcave-pointycurve [[logic gate]]. if the [[logic gate]] does not take exactly two inputs, the output of the [[logic gate]] can be thought of as "is the number of true inputs odd?"

| $A$ | $B$ | $A + B$ |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

## Implication

**aka** _Conditional [[logic statement]]_

**definition** if $x = \top$, then the conditional [[logic statement]] $x < y$ is said to be _vacuously true_, see [[boolean algebra]]

**definition** $+x > +y$ is the _contrapositive_ of the [[logic statement]] $x < y$. they are logically equivalent

**definition** $x > y$ is the _converse_ of the [[logic statement]] $x < y$. they are **not** logically equivalent

**definition** $+x < +y$ is the _inverse_ of the [[logic statement]] $x < y$. they are **not** logically equivalent

> **note** even though the converse and inverse of a conditional [[logic statement]] are not logically equivalent, the converse of a [[logic statement]] is logically equivalent to the inverse of that [[logic statement]]

**definition**

let $S < R < Q$ be a [[logic statement]] (square implies rectangle implies quadrilateral). then,

$S$ is said to be a _sufficient condition_ for $R$ &mdash; knowing that $S$ is true allows the deduction that $R$ is true.

$Q$ is said to be a _necessary condition_ for $R$ &mdash; for $R$ to be true, $Q$ must be true.

alternatively, let $A < B$ be a [[logic statement]]. then,

$A$ is said to be a _sufficient condition_ for $B$

$B$ is said to be a _necessary condition_ for $A$

**notations**

_in my [[math notation]]_ $<$ and $\dashv$ and $>$ and $\vdash$

_in [[conventional math notation]]_ $\to$ and $\implies$

**representation**

can be built by combining multiple [[logic gate]]s. may only take one input

| $A$ | $B$ | $A < B$ |
| --- | --- | ------- |
| 0   | 0   | 1       |
| 0   | 1   | 1       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |

## XNOR

**aka** _Double Implication, Equivalent, Biconditional [[logic statement]], Bidirectional Implication_

**notations**

_in my [[math notation]]_ $=\!=$ and $=$

_in [[conventional math notation]]_ $\Leftrightarrow$ or $\odot$ or $=$

**representation**

doubleconcave-pointycurve-circle [[logic gate]]. if the [[logic gate]] does not take exactly two inputs, the output of the [[logic gate]] can be thought of as “is the number of true inputs even?”

| $A$ | $B$ | $A =\!= B$ |
| --- | --- | ---------- |
| 0   | 0   | 1          |
| 0   | 1   | 0          |
| 1   | 0   | 0          |
| 1   | 1   | 1          |

## Difference

**notations**

_in my [[math notation]]_ $\land +$

_in [[conventional math notation]]_ $\backslash$

**representation**

| $A$ | $B$ | $A \land +B$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 0            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

## Addition

**aka**:_ disjoint union_

**notation** _in my [[math notation]]_ $\, : \,$

**representation**

| $A$ | $B$ | $A : B$       |
| --- | --- | ------------- |
| 0   | 0   | 0             |
| 0   | 1   | 1             |
| 1   | 0   | 1             |
| 1   | 1   | $\varnothing$ |

## Subtraction

**notation** _in my [[math notation]]_ $\cdot$

**representation**

| $A$ | $B$ | $A \cdot B$   |
| --- | --- | ------------- |
| 0   | 0   | 0             |
| 0   | 1   | $\varnothing$ |
| 1   | 0   | 1             |
| 1   | 1   | 0             |

## identities

**properties**

identities below hold for all $\mathbb B x \land \mathbb B y$

_identity_ $x \lor \bot =\!= x$

_identity_ $x \land \top =\!= x$

_complement_ $x \lor +x =\!= \top$

_complement_ $x \land +x =\!= \bot$

_idempotence_ $x \lor x =\!= x$

_idempotence_ $x \land x =\!= x$

_domination_ $x \lor \top =\!= \top$

_domination_ $x \land \bot =\!= \bot$

_involution_ $+\smash+x =\!= x$

## properties

**properties**

properties below hold for all $\mathbb B x \land \mathbb B y$

_commutativity_ $x \lor y =\!= y \lor x$

_commutativity_ $x \land y =\!= y \land x$

_associativity_ $x \lor y\ \top\ z =\!= x \top y \lor z$

_associativity_ $x \land y\ \bot\ z =\!= x\ \bot\ y \land z$

_distributivity_ $x \land y\ \top\ z =\!= x\ \bot\ y \lor x\ \bot\ z$

_distributivity_ $z \lor y\ \bot\ z =\!= x\ \top\ y \land x\ \top\ z$

_De Morgan's_ $\times\ x \lor y =\!= +x \land +y$

_De Morgan's_ $\times x \land y =\!= +x \lor +y$

_absorption_ $x \lor \times\ x \land y =\!= x$

_absorption_ $x \land \times\ x \lor y =\!= x$

_xor_ $x \times y =\!= x\ \bot\ \smash+y \lor y\ \bot\ \smash+x$ &mdash; me

_xor_ $x \times y =\!= \times\ x = y$ &mdash; me

_implication_ $x < y =\!= +x \lor y$

_implication_ $x > y =\!= x \lor +y$

_biconditional_ $x = y =\!= +x \land +y \lor x\ \bot\ y$

_biconditional_ $x = y =\!= x \dashv y \land x \vdash y$
