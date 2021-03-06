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

### notation

$\cdot$ or $\cap$ in [[classical-math-notation]] (may be omitted)

$\land$ in my [[math-notation]]

### representation

straight-curve [[logic-gate]]. may take more than one input

| $A$ | $B$ | $A \land B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

## OR

> **AKA**: Disjunction

### notation

$+$ or $\cap$ in [[classical-math-notation]]

$\land$ in my [[math-notation]]

### representation

concave-pointycurve [[logic-gate]]. may take more than one input

| $A$ | $B$ | $A \lor B$ |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

## NOT

> **AKA**: Negation

### notation

$a'$ or $\bar a$ or $a^c$ in [[classical-math-notation]]

$/$ in my [[math-notation]]

### representation

triangle-circle [[logic-gate]]. may only take one input

| $A$ | $/A$ |
| --- | ---- |
| 0   | 1    |
| 1   | 0    |

## XOR

> **AKA**: Exclusive OR, symmetric difference, disjunctive union

### notation

$\oplus$ or $\vartriangle$ in [[classical-math-notation]]

$\times$ in my [[math-notation]]

### representation

doubleconcave-pointycurve [[logic-gate]]. if the [[logic-gate]] does not take exactly two inputs, the output of the [[logic-gate]] can be thought of as "is the number of true inputs odd?"

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

### notation

$\to$ in [[classical-math-notation]]

$\vdash$ and $\dashv$ in my [[math-notation]]

### representation

can be built by combining multiple [[logic-gate]]s. may only take one input

| $A$ | $B$ | $A \vdash B$ |
| --- | --- | ------------ |
| 0   | 0   | 1            |
| 0   | 1   | 1            |
| 1   | 0   | 0            |
| 1   | 1   | 1            |

## XNOR

> **AKA**: Double Implication, Equivalent, Biconditional [[logic-statement]], Bidirectional Implication

### notation

$\harr$ or $\odot$ or $=$ in [[classical-math-notation]]

$\equiv$ in my [[math-notation]]

### representation

doubleconcave-pointycurve-circle [[logic-gate]]. if the [[logic-gate]] does not take exactly two inputs, the output of the [[logic-gate]] can be thought of as ???is the number of true inputs even????

| $A$ | $B$ | $A \equiv B$ |
| --- | --- | ------------ |
| 0   | 0   | 1            |
| 0   | 1   | 0            |
| 1   | 0   | 0            |
| 1   | 1   | 1            |

## [[operator]] precedence

see [[math-notation]] for operator precedence in my [[math-notation]]

in [[classical-math-notation]]: $' \cdot + \oplus$

## identities

identities below hold for all $\mathbb B x$ and for all $\mathbb B y$

$x \lor \bot \equiv x$ &mdash; identity

$x \land \top \equiv x$ &mdash; identity

$x \lor /x \equiv \top$ &mdash; complement

$x \land /x \equiv \bot$ &mdash; complement

$x \lor x \equiv x$ &mdash; idempotence

$x \land x \equiv x$ &mdash; idempotence

$x \lor \top \equiv \top$ &mdash; domination

$x \land \bot \equiv \bot$ &mdash; domination

$//x \equiv x$ &mdash; involution

## properties

properties below hold for all $\mathbb B x$ and for all $\mathbb B y$

$x \lor y \equiv y \lor x$ &mdash; commutativity

$x \land y \equiv y \land x$ &mdash; commutativity

$x \lor (y \lor z) \equiv (x \lor y) \lor z$ &mdash; associativity

$x \land (y \lor z) \equiv (x \land y) \land z$ &mdash; associativity

$x \land (y \lor z) \equiv (x \land y) \lor (x \land z)$ &mdash; distributivity

$z \lor (y \land z) \equiv (x \lor y) \land (x \lor z)$ &mdash; distributivity

$\times\ x \lor y \equiv /x \land /y$ &mdash; DeMorgan

$\times x \land y \equiv /x \lor /y$ &mdash; DeMorgan

$x \lor \times\ x \land y \equiv x$ &mdash; absorption

$x \land \times\ x \lor y \equiv x$ &mdash; absorption

$x \times y \equiv (x \land /y) \lor (/x \land y)$ &mdash; exclusive or

$x \times y \equiv / x = y$ &mdash; exclusive or

$x \vdash y \equiv /x \lor y$ &mdash; implication

$x \dashv y \equiv x \lor /y$ &mdash; implication

$(x \equiv y) \equiv (x \land y) \lor (/x \land /y)$ &mdash; biconditional

$(x \equiv y) \equiv (x \vdash y) \land (x \dashv y)$ &mdash; biconditional
