# Boolean Algebra

*algebra using boolean variables and logical operators*

see [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md)

## Bolean Variables

designated by a letter of the alphabet

can either take the value *True* ($\top$) or *False* ($\bot$), or represent a boolean function acting on other boolean variables

## Boolean Operations

### AND

represented by $\cdot$ in [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md), and by $\land$ in my [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md). $\cdot$ may be omitted in [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md), but $\land$ may not in my [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md)

represented by straight-curve logic gate. may take more than one input

| A | B | A AND B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### OR

represented by $+$ in [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md), and by $\land$ in my [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md)

represented by concave-pointycurve logic gate. may take more than one input

| A | B | A OR B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### NOT

represented like $a'$ or by $\bar a$ in [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md), and by $\lnot$ in my [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md)

represented by triangle-circle logic gate. may only take one input

| A | NOT A |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

### operator precedence

in [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md) $' \cdot +$

in my [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md): $\lnot \land \lor$

```python
expression: term + term
term: literal . literal
literal: 'literal | atom
atom: variable | (expression)
```

### identities

$x \lor \bot = x$

$x \land \top = x$

$x \lor \lnot x = \top$

$x \land \lnot x = \bot$

*fund*a*mental theorems*

$x \lor x = x$

$x \land x = x$

$x \lor \top = \top$

$x \land \bot = \bot$

$\lnot \lnot x = x$

### properties

*commutativity*

$x \lor y = y \lor x$

$x \land y = y \land x$

*associativity*

$x \lor (y \lor z) = (x \lor y) \lor z$

$x \land (y \lor z) = (x \land y) \land z$

*distributivity*

$x \land (y \lor z) = x \land y \lor x \land z$

$z \lor y \land z = (x \lor y) \land (x \lor z)$

*DeMorgan*

$\lnot(x \lor y) = \lnot x \land \lnot y$

$\lnot(x \land y) = \lnot x \lor \lnot y$

*absorption*

$x \lor x \land y = x$

$x \land (x \lor y) = x$

## Boolean Functions

### example

in [Classical Math Notation](Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md): $f(x, y, z) = (x + y')z + x'$

in my [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md): $f\ x, y, z = (x \lor \lnot y) \land z \lor \lnot x$

## Truth Table to Boolean Expression

*mainly for [ITI1100 [A] Digital Systems I](../ITI1100%20%5BA%5D%20Digital%20Systems%20I%20adf68be5862d422f809db86010db2879.md)*

to get a boolean expression from a truth table, *or* different terms together

see [https://uottawa.brightspace.com/d2l/le/content/285255/viewContent/4324959/View](https://uottawa.brightspace.com/d2l/le/content/285255/viewContent/4324959/View) because my computer doesn’t want to allow me to take screenshots it seems