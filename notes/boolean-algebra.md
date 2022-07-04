# Boolean Algebra

_algebra using [[boolean]] variables and logical [[operator]]s_

see [[math-notation]], [[disjunctive-normal-form]], [[conjunctive-normal-form]]

values in [[boolean-algebra]] are [[boolean]]s: either _true_ or _false_

## simplifying boolean expressions

boolean expressions can be simplified:

- using [[boolean-algebra]] through [[boolean]] [[operator]]s
- using [[karnaugh-map]]s
- using [[truth-table]]s

## proving implication statements

see [[proof]], [[math-notation]]

to prove a conditional statement such as $x \vdash y$:

1. assume $x$ is true
2. show that $y$ must follow from $x$ (using [[axiom]]s for formal proofs)

to prove a biconditional statement such as $x \equiv y$

1. prove that $x \vdash y$ and that $x \dashv y$
2. use the biconditional [[axiom]] $(x \vdash y \land x \dashv y) \equiv (x \equiv y)$ (see [[math-notation]])

---

# Boolean Operators

see [[boolean]], [[boolean-algebra]]

## AND

> **AKA**: Conjunction

### notation

$\cdot$ in [[classical-math-notation]] (may be omitted)

$\land$ in my [[math-notation]]

### representation

straight-curve logic [[gate]]. may take more than one input

| $A$ | $B$ | $A \land B$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

## OR

> **AKA**: Disjunction

### notation

$+$ in [[classical-math-notation]]

$\land$ in my [[math-notation]]

### representation

concave-pointycurve logic [[gate]]. may take more than one input

| $A$ | $B$ | $A \lor B$ |
| --- | --- | ---------- |
| 0   | 0   | 0          |
| 0   | 1   | 1          |
| 1   | 0   | 1          |
| 1   | 1   | 1          |

## NOT

> **AKA**: Negation

### notation

$a'$ or $\bar a$ in [[classical-math-notation]]

$/$ in my [[math-notation]]

### representation

triangle-circle logic [[gate]]. may only take one input

| $A$ | $/A$ |
| --- | ---- |
| 0   | 1    |
| 1   | 0    |

## XOR

> **AKA**: Exclusive OR

### notation

$\oplus$ in [[classical-math-notation]]

$\times$ in my [[math-notation]]

### representation

doubleconcave-pointycurve logic [[gate]]. if the [[gate]] does not take exactly two inputs, the output of the [[gate]] can be thought of as "is the number of true inputs odd?"

| $A$ | $B$ | $A \times B$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

## Implication

> **AKA**: Conditional Statement

### notation

$\to$ in [[classical-math-notation]]

$\vdash$ and $\dashv$ in my [[math-notation]]

### definitions

if $x = \top$, then $x \vdash y$ is _vacuously true_

if $x = \bot$, then $x \vdash y$ is _trivially true_

### representation

can be built by combining multiple logic [[gate]]s. may only take one input

| $A$ | $B$ | $A \vdash B$ |
| --- | --- | ------------ |
| 0   | 0   | 1            |
| 0   | 1   | 1            |
| 1   | 0   | 0            |
| 1   | 1   | 0            |

## XNOR

> **AKA**: Double Implication, Equivalent, Biconditional Statement, Bidirectional Implication

### notation

$\leftrightarrow$ or $\odot$ in [[classical-math-notation]]

$\equiv$ in my [[math-notation]]

### representation

doubleconcave-pointycurve-circle logic [[gate]]. if the [[gate]] does not take exactly two inputs, the output of the [[gate]] can be thought of as “is the number of true inputs even?”

| $A$ | $B$ | $A \equiv B$ |
| --- | --- | ------------ |
| 0   | 0   | 1            |
| 0   | 1   | 0            |
| 1   | 0   | 0            |
| 1   | 1   | 1            |

## [[operator]] precedence

see [[math-notation]] for operator precedence in my [[math-notation]]

in [[classical-math-notation]] $' : + \oplus$

```python
expression: term + term
term: literal . literal
literal: 'literal | atom
atom: variable | (expression)
```

## identities

identities below hold for all $\mathbb B x$

$x \vdash y \equiv /x \lor y$ &mdash; implication

$(x \equiv y) \equiv (x \land y) \lor (/x \land /y)$ &mdash; biconditional

$(x \equiv y) \equiv (x \vdash y) \land (x \dashv y)$ &mdash; biconditional

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

properties below hold for all $\mathbb B x$

$x \lor y \equiv y \lor x$ &mdash; commutativity

$x \land y \equiv y \land x$ &mdash; commutativity

$x \lor (y \lor z) \equiv (x \lor y) \lor z$ &mdash; associativity

$x \land (y \lor z) \equiv (x \land y) \land z$ &mdash; associativity

$x \land (y \lor z) \equiv (x \land y) \lor (x \land z)$ &mdash; distributivity

$z \lor (y \land z) \equiv (x \lor y) \land (x \lor z)$ &mdash; distributivity

$/(x \lor y) \equiv /x \land /y$ &mdash; DeMorgan

$/(x \land y) \equiv /x \lor /y$ &mdash; DeMorgan

$x \lor (x \land y) \equiv x$ &mdash; absorption

$x \land (x \lor y) \equiv x$ &mdash; absorption

$x \times y \equiv (x \land /y) \lor (/x \land y)$ &mdash; exclusive or

$x \times y \equiv /(x \equiv y)$ &mdash; exclusive or
