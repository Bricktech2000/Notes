# Boolean Logic

see [[boolean]]

see [[math-notation]], [[disjunctive-normal-form]], [[conjunctive-normal-form]], [[quantifier]]

> **definition**: two boolean expressions (or [[logic-statement]]s) are said to be _logically equivalent_ if they yield the same output for every input. in other words, two boolean expressions (or [[logic-statement]]s) are _logically equivalent_ if they share the same [[truth-table]]

boolean expressions can be simplified to a different but logically equivalent expression using [[boolean-logic]] through [[boolean]] [[operator]]s, or alternatively visually using [[karnaugh-map]]s or [[truth-table]]s

---

# Boolean Operators

see [[boolean]], [[boolean-logic]]

boolean [[operator]]s can be modeled in [[logic-circuit]]s through [[logic-gate]]s

## AND

> **AKA**: Conjunction

> **notation**: _in my [[math-notation]]_ $\land$

> **notation**: _in [[conventional-math-notation]]_ $\cdot$ or $\cap$ (may be omitted)

> **representation**: straight-curve [[logic-gate]]. may take more than one input

| $A$ | $B$ | $A \land B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

## OR

> **AKA**: Disjunction

> **notation**: _in my [[math-notation]]_ $\lor$

> **notation**: _in [[conventional-math-notation]]_ $+$ or $\cap$

> **representation**: concave-pointycurve [[logic-gate]]. may take more than one input

| $A$ | $B$ | $A \lor B$ |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

## NOT

> **AKA**: Negation

> **notation**: _in my [[math-notation]]_ $/$

> **notation**: _in [[conventional-math-notation]]_ $a'$ or $\bar a$ or $a^c$

> **representation**: triangle-circle [[logic-gate]]. may only take one input

| $A$ | $/A$ |
| --- | ---- |
| 0   | 1    |
| 1   | 0    |

## XOR

> **AKA**: Exclusive OR, symmetric difference, disjunctive union

> **notation**: _in my [[math-notation]]_ $\times$

> **notation**: _in [[conventional-math-notation]]_ $\oplus$ or $\vartriangle$

> **representation**: doubleconcave-pointycurve [[logic-gate]]. if the [[logic-gate]] does not take exactly two inputs, the output of the [[logic-gate]] can be thought of as "is the number of true inputs odd?"

| $A$ | $B$ | $A \times B$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

## Implication

> **AKA**: Conditional [[logic-statement]]

> **definition**: if $x = \top$, then the conditional [[logic-statement]] $x \vdash y$ is said to be _vacuously true_, see [[boolean-logic]]

> **definition**: $/x \dashv /y$ is the _contrapositive_ of the [[logic-statement]] $x \vdash y$. they are logically equivalent

> **definition**: $x \dashv y$ is the _converse_ of the [[logic-statement]] $x \vdash y$. they are **not** logically equivalent

> **definition**: $/x \vdash /y$ is the _inverse_ of the [[logic-statement]] $x \vdash y$. they are **not** logically equivalent

> **note**: even though the converse and inverse of a conditional [[logic-statement]] are not logically equivalent, the converse of a [[logic-statement]] is logically equivalent to the inverse of that [[logic-statement]].

> **definition**:
>
> let $S \vdash R \vdash Q$ be a [[logic-statement]] (square implies rectangle implies quadrilateral). then,
>
> $S$ is said to be a _sufficient condition_ for $R$ &mdash; knowing that $S$ is true allows the deduction that $R$ is true.
>
> $Q$ is said to be a _necessary condition_ for $R$ &mdash; for $R$ to be true, $Q$ must be true.
>
> alternatively, let $A \vdash B$ be a [[logic-statement]]. then,
>
> $A$ is said to be a _sufficient condition_ for $B$
>
> $B$ is said to be a _necessary condition_ for $A$

> **notation**: _in my [[math-notation]]_ $\vdash$ and $\dashv$

> **notation**: _in [[conventional-math-notation]]_ $\to$ and $\implies$

> **representation**: can be built by combining multiple [[logic-gate]]s. may only take one input

| $A$ | $B$ | $A \vdash B$ |
| --- | --- | ------------ |
| 0   | 0   | 1            |
| 0   | 1   | 1            |
| 1   | 0   | 0            |
| 1   | 1   | 1            |

## XNOR

> **AKA**: Double Implication, Equivalent, Biconditional [[logic-statement]], Bidirectional Implication

> **notation**: _in my [[math-notation]]_ $\equiv$

> **notation**: _in [[conventional-math-notation]]_ $\harr$ or $\odot$ or $=$

> **representation**: doubleconcave-pointycurve-circle [[logic-gate]]. if the [[logic-gate]] does not take exactly two inputs, the output of the [[logic-gate]] can be thought of as “is the number of true inputs even?”

| $A$ | $B$ | $A \equiv B$ |
| --- | --- | ------------ |
| 0   | 0   | 1            |
| 0   | 1   | 0            |
| 1   | 0   | 0            |
| 1   | 1   | 1            |

## [[operator]] precedence

see [[math-notation]] for operator precedence in my [[math-notation]]

in [[conventional-math-notation]]: $' \cdot + \oplus$

## identities

identities below hold for all $\mathbb B x$ and for all $\mathbb B y$

> **property**: _identity_ $x \lor \bot \equiv x$

> **property**: _identity_ $x \land \top \equiv x$

> **property**: _complement_ $x \lor /x \equiv \top$

> **property**: _complement_ $x \land /x \equiv \bot$

> **property**: _idempotence_ $x \lor x \equiv x$

> **property**: _idempotence_ $x \land x \equiv x$

> **property**: _domination_ $x \lor \top \equiv \top$

> **property**: _domination_ $x \land \bot \equiv \bot$

> **property**: _involution_ $//x \equiv x$

## properties

properties below hold for all $\mathbb B x$ and for all $\mathbb B y$

> **property**: _commutativity_ $x \lor y \equiv y \lor x$

> **property**: _commutativity_ $x \land y \equiv y \land x$

> **property**: _associativity_ $x \lor (y \lor z) \equiv (x \lor y) \lor z$

> **property**: _associativity_ $x \land (y \lor z) \equiv (x \land y) \land z$

> **property**: _distributivity_ $x \land (y \lor z) \equiv (x \land y) \lor (x \land z)$

> **property**: _distributivity_ $z \lor (y \land z) \equiv (x \lor y) \land (x \lor z)$

> **property**: _DeMorgan_ $\times\ x \lor y \equiv /x \land /y$

> **property**: _DeMorgan_ $\times x \land y \equiv /x \lor /y$

> **property**: _absorption_ $x \lor \times\ x \land y \equiv x$

> **property**: _absorption_ $x \land \times\ x \lor y \equiv x$

> **property**: _or_ $x \times y \equiv (x \land /y) \lor (/x \land y)$ &mdash; e

> **property**: _or_ $x \times y \equiv / x = y$ &mdash; e

> **property**: _implication_ $x \vdash y \equiv /x \lor y$

> **property**: _implication_ $x \dashv y \equiv x \lor /y$

> **property**: _biconditional_ $(x \equiv y) \equiv (x \land y) \lor (/x \land /y)$

> **property**: _biconditional_ $(x \equiv y) \equiv (x \vdash y) \land (x \dashv y)$
