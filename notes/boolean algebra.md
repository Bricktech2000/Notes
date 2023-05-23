# Boolean Algebra

**see** [[boolean]]

**see** [[math notation]], [[disjunctive normal form]], [[conjunctive normal form]], [[quantifier]], [[algebraic structure]]

**definition** two boolean expressions (or [[logic statement]]s) are said to be _logically equivalent_ if they yield the same output for every input. in other words, two boolean expressions (or [[logic statement]]s) are _logically equivalent_ if they share the same [[truth table]]

boolean expressions can be simplified to a different but logically equivalent expression using [[boolean algebra]] through [[boolean algebra#operators]], or alternatively visually using [[karnaugh map]]s or [[truth table]]s

---

# Operators

**see** [[boolean]], [[boolean algebra]]

boolean [[operator]]s can be modeled in [[logic circuit]]s through [[logic gate]]s

## operator precedence

see [[math notation]] for [[infix notation#precedence]] in my [[math notation]]

in [[conventional math notation]]: $' \cdot + \oplus$

## Conjunction

**aka** _AND, **`"min"`**_

**notations**

_in my [[math notation]]_ **`/\`** and **`__`**

_in [[conventional math notation]]_ $\cdot$ or $\cap$ (may be omitted)

**representation**

straight-curve [[logic gate]]. may take more than one input

| **`A`** | **`B`** | **`A /\ B`** |
| ------- | ------- | ------------ |
| 0       | 0       | 0            |
| 0       | 1       | 0            |
| 1       | 0       | 0            |
| 1       | 1       | 1            |

## Disjunction

**aka** _OR, **`"max"`**_

**notations**

_in my [[math notation]]_ **`\/`** and **`^^`**

_in [[conventional math notation]]_ $+$ or $\cup$

**representation**

concave-pointycurve [[logic gate]]. may take more than one input

| **`A`** | **`B`** | **`A \/ B`** |
| ------- | ------- | ------------ |
| 0       | 0       | 0            |
| 0       | 1       | 1            |
| 1       | 0       | 1            |
| 1       | 1       | 1            |

## Negation

**aka** _NOT_

**notations**

_in my [[math notation]]_ **`><`** and **`+`**

_in [[conventional math notation]]_ $a'$ or $\bar a$ or $a^c$

**representation**

triangle-circle [[logic gate]]. may only take one input

| **`A`** | **`+A`** |
| ------- | -------- |
| 0       | 1        |
| 1       | 0        |

**properties**

## Exclusive OR

**aka** _XOR, symmetric difference, disjunctive union_

**notations**

_in my [[math notation]]_ **`><`** and **`+`**

_in [[conventional math notation]]_ $\oplus$ or $\vartriangle$

**representation**

doubleconcave-pointycurve [[logic gate]]. if the [[logic gate]] does not take exactly two inputs, the output of the [[logic gate]] can be thought of as "is the number of true inputs odd?"

| **`A`** | **`B`** | **`A + B`** |
| ------- | ------- | ----------- |
| 0       | 0       | 0           |
| 0       | 1       | 1           |
| 1       | 0       | 1           |
| 1       | 1       | 0           |

## Implication

**aka** _conditional [[logic statement]], logical consequence_

**definition** if **`x = ^^`**, then the conditional [[logic statement]] **`x < y`** is said to be _vacuously true_, see [[boolean algebra]]

**definition** **`+x > +y`** is the _contrapositive_ of the [[logic statement]] **`x < y`**. they are logically equivalent

**definition** **`x > y`** is the _converse_ of the [[logic statement]] **`x < y`**. they are **not** logically equivalent

**definition** **`+x < +y`** is the _inverse_ of the [[logic statement]] **`x < y`**. they are **not** logically equivalent

> **note** even though the converse and inverse of a conditional [[logic statement]] are not logically equivalent, the converse of a [[logic statement]] is logically equivalent to the inverse of that [[logic statement]]

**definition**

let **`S < R < Q`** be a [[logic statement]] (square implies rectangle implies quadrilateral). then,

**`S`** is said to be a _sufficient condition_ for **`R`** &mdash; knowing that **`S`** is true allows the deduction that **`R`** is true.

**`Q`** is said to be a _necessary condition_ for **`R`** &mdash; for **`R`** to be true, **`Q`** must be true.

alternatively, let **`A < B`** be a [[logic statement]]. then,

**`A`** is said to be a _sufficient condition_ for **`B`**

**`B`** is said to be a _necessary condition_ for **`A`**

**notations**

_in my [[math notation]]_ **`<`** and **`-|`** and **`>`** and **`|-`**

_in [[conventional math notation]]_ $\to$ and $\implies$

**representation**

can be built by combining multiple [[logic gate]]s. may only take one input

| **`A`** | **`B`** | **`A < B`** |
| ------- | ------- | ----------- |
| 0       | 0       | 1           |
| 0       | 1       | 1           |
| 1       | 0       | 0           |
| 1       | 1       | 1           |

## Equivalence

**aka** _XNOR, double implication, equivalence, biconditional [[logic statement]], bidirectional implication_

**notations**

_in my [[math notation]]_ **`==`** and **`=`**

_in [[conventional math notation]]_ $\Leftrightarrow$ or $\odot$ or $=$

**representation**

doubleconcave-pointycurve-circle [[logic gate]]. if the [[logic gate]] does not take exactly two inputs, the output of the [[logic gate]] can be thought of as "is the number of true inputs even?"

| **`A`** | **`B`** | **`A == B`** |
| ------- | ------- | ------------ |
| 0       | 0       | 1            |
| 0       | 1       | 0            |
| 1       | 0       | 0            |
| 1       | 1       | 1            |

## Difference

**notations**

_in my [[math notation]]_ **`/\ +`**

_in [[conventional math notation]]_ $\backslash$

**representation**

| **`A`** | **`B`** | **`A /\ +B`** |
| ------- | ------- | ------------- |
| 0       | 0       | 0             |
| 0       | 1       | 0             |
| 1       | 0       | 1             |
| 1       | 1       | 0             |

## identities

**properties**

identities below hold for all **`BB x /\ BB y`**

_identity_ **`x \/ __ == x`**

_identity_ **`x /\ ^^ == x`**

_complement_ **`x \/ +x == ^^`**

_complement_ **`x /\ +x == __`**

_idempotence_ **`x \/ x == x`**

_idempotence_ **`x /\ x == x`**

_domination_ **`x \/ ^^ == ^^`**

_domination_ **`x /\ __ == __`**

_involution_ **`++x == x`**

## properties

**properties**

properties below hold for all **`BB x /\ BB y`**

_commutativity_ **`x \/ y == y \/ x`**

_commutativity_ **`x /\ y == y /\ x`**

_associativity_ **`x \/ y ^^ z == x ^^ y \/ z`**

_associativity_ **`x /\ y __ z == x __ y /\ z`**

_distributivity_ **`x /\ y ^^ z == x __ y \/ x __ z`**

_distributivity_ **`z \/ y __ z == x ^^ y /\ x ^^ z`**

_De Morgan's_ **`>< x \/ y == +x /\ +y`**

_De Morgan's_ **`>< x /\ y == +x \/ +y`**

_absorption_ **`x \/ >< x /\ y == x`**

_absorption_ **`x /\ >< x \/ y == x`**

_xor_ **`x >< y == x __ +y \/ y __ +x`** &mdash; me

_xor_ **`x >< y == >< x = y`** &mdash; me

_implication_ **`x < y == +x \/ y`**

_implication_ **`x > y == x \/ +y`**

_biconditional_ **`x = y == +x /\ +y \/ x __ y`**

_biconditional_ **`x = y == x -| y /\ x |- y`**
