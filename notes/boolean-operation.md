# Boolean Operation

see [[math-notation]], [[classical-math-notation]]

## AND (Conjunction)

### notation

$\cdot$ in [[classical-math-notation]] (may be omitted)

$\land$ in my [[math-notation]]

### representation

straight-curve logic gate. may take more than one input

| A   | B   | A AND B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |

## OR (Disjunction)

### notation

$+$ in [[classical-math-notation]]

$\land$ in my [[math-notation]]

### representation

concave-pointycurve logic gate. may take more than one input

| A   | B   | A OR B |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |

## NOT (Negation)

### notation

$a'$ or $\bar a$ in [[classical-math-notation]]

$\lnot$ in my [[math-notation]]

### representation

triangle-circle logic gate. may only take one input

| A   | NOT A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

## XOR (Exclusive OR)

### notation

$\oplus$ in [[classical-math-notation]]

$\times$ in my [[math-notation]]

### representation

doubleconcave-pointycurve logic gate. if the gate does not take exactly two inputs, the output of the gate can be thought of as “is the number of true inputs odd?”

| A   | B   | A XOR B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

## Implication (Conditional Statement)

### notation

$\to$ in [[classical-math-notation]]

$\vdash$ and $\dashv$ in my [[math-notation]]

### definitions

if $x = \top$, then $x \vdash y$ is _vacuously true_

if $x = \bot$, then $x \vdash y$ is _trivially true_

### representation

can be built by combining multiple logic gates. may only take one input

| A   | B   | A IMPL B |
| --- | --- | -------- |
| 0   | 0   | 1        |
| 0   | 1   | 1        |
| 1   | 0   | 0        |
| 1   | 1   | 0        |

## XNOR, Double Implication (Biconditional Statement)

### notation

$\leftrightarrow$ or $\odot$ in [[classical-math-notation]]

$\equiv$ in my [[math-notation]]

### representation

doubleconcave-pointycurve-circle logic gate. if the gate does not take exactly two inputs, the output of the gate can be thought of as “is the number of true inputs even?”

| A   | B   | A EQUIV B |
| --- | --- | --------- |
| 0   | 0   | 1         |
| 0   | 1   | 0         |
| 1   | 0   | 0         |
| 1   | 1   | 1         |

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

_implication_

$x \vdash y \equiv \lnot x \lor y$

_biconditional_

$(x \equiv y) \equiv x \land y \lor \lnot x \land \lnot y$

$(x \equiv y) \equiv (x \vdash y) \land (x \dashv y)$

_identity_

$x \lor \bot \equiv x$

$x \land \top \equiv x$

_negation_

$x \lor \lnot x \equiv \top$

$x \land \lnot x \equiv \bot$

_idempotence_

$x \lor x \equiv x$

$x \land x \equiv x$

_domination_

$x \lor \top \equiv \top$

$x \land \bot \equiv \bot$

_double negation_

$\lnot \lnot x \equiv x$

## properties

_commutativity_

$x \lor y \equiv y \lor x$

$x \land y \equiv y \land x$

_associativity_

$x \lor (y \lor z) \equiv (x \lor y) \lor z$

$x \land (y \lor z) \equiv (x \land y) \land z$

_distributivity_

$x \land (y \lor z) \equiv x \land y \lor x \land z$

$z \lor y \land z \equiv (x \lor y) \land (x \lor z)$

_DeMorgan_

$\lnot(x \lor y) \equiv \lnot x \land \lnot y$

$\lnot(x \land y) \equiv \lnot x \lor \lnot y$

_absorption_

$x \lor x \land y \equiv x$

$x \land (x \lor y) \equiv x$

_exclusive or_

$x \times y \equiv x \land \lnot y \lor \lnot x \land y$

$x \times y \equiv \lnot (x \equiv y)$
