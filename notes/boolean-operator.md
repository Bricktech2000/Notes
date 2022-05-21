# Boolean Operator

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

$\lnot$ in my [[math-notation]]

### representation

triangle-circle logic [[gate]]. may only take one input

| $A$ | $\lnot A$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

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

> **AKA**: Double Implication, Equivalent, Biconditional Statement

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

## operator precedence

in [[classical-math-notation]] $' \cdot + \oplus$

in my [[math-notation]]: $\lnot \land \lor \times$

```python
expression: term + term
term: literal . literal
literal: 'literal | atom
atom: variable | (expression)
```

## identities

$x \vdash y \equiv \lnot x \lor y$ &mdash; implication

$(x \equiv y) \equiv x \land y \lor \lnot x \land \lnot y$ &mdash; biconditional

$(x \equiv y) \equiv (x \vdash y) \land (x \dashv y)$ &mdash; biconditional

$x \lor \bot \equiv x$ &mdash; identity

$x \land \top \equiv x$ &mdash; identity

$x \lor \lnot x \equiv \top$ &mdash; negation

$x \land \lnot x \equiv \bot$ &mdash; negation

$x \lor x \equiv x$ &mdash; idempotence

$x \land x \equiv x$ &mdash; idempotence

$x \lor \top \equiv \top$ &mdash; domination

$x \land \bot \equiv \bot$ &mdash; domination

$\lnot \lnot x \equiv x$ &mbash; double negation

## properties

$x \lor y \equiv y \lor x$ &mdash; commutativity

$x \land y \equiv y \land x$ &mdash; commutativity

$x \lor (y \lor z) \equiv (x \lor y) \lor z$ &mdash; associativity

$x \land (y \lor z) \equiv (x \land y) \land z$ &mdash; associativity

$x \land (y \lor z) \equiv x \land y \lor x \land z$ &mdash; distributivity

$z \lor y \land z \equiv (x \lor y) \land (x \lor z)$ &mdash; distributivity

$\lnot(x \lor y) \equiv \lnot x \land \lnot y$ &mdash; DeMorgan

$\lnot(x \land y) \equiv \lnot x \lor \lnot y$ &mdash; DeMorgan

$x \lor x \land y \equiv x$ &mdash; absorption

$x \land (x \lor y) \equiv x$ &mdash; absorption

$x \times y \equiv x \land \lnot y \lor \lnot x \land y$ &mdash; exclusive or

$x \times y \equiv \lnot (x \equiv y)$ &mdash; exclusive or
