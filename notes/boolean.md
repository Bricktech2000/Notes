# Boolean

_the [[set]] of [[boolean]]s_

**see** [[math notation]]

**definition**

_either true or false_

**`BB == {{ I, O }}`**

**properties**

**`BB < UU`**, see [[set#universal set]]

[[boolean]]s can be manipulated through [[boolean algebra]]

---

# Operators

## operator precedence

see [[math notation]] for [[infix notation#precedence]] in my [[math notation]]

in [[conventional math notation]]: $' \cdot + \oplus$

## Conjunction

**aka** _AND_, _**`"min"`**_

**notation** _in my [[math notation]]_ **`/\`** and **`__`**

**notation** _in [[conventional math notation]]_ $\cdot$ or $\cap$ (may be omitted)

**representation** _[[truth table]]_

| **`A`** | **`B`** | **`A /\ B`** |
| ------- | ------- | ------------ |
| 0       | 0       | 0            |
| 0       | 1       | 0            |
| 1       | 0       | 0            |
| 1       | 1       | 1            |

## Disjunction

**aka** _OR_, _**`"max"`**_

**notation** _in my [[math notation]]_ **`\/`** and **`^^`**

**notation** _in [[conventional math notation]]_ $+$ or $\cup$

**representation** _[[truth table]]_

| **`A`** | **`B`** | **`A \/ B`** |
| ------- | ------- | ------------ |
| 0       | 0       | 0            |
| 0       | 1       | 1            |
| 1       | 0       | 1            |
| 1       | 1       | 1            |

## Negation

**aka** _NOT_

**notation** _in my [[math notation]]_ **`><`** and **`+`**

**notation** _in [[conventional math notation]]_ $a'$ or $\bar a$ or $a^c$

**representation** _[[truth table]]_

| **`A`** | **`+A`** |
| ------- | -------- |
| 0       | 1        |
| 1       | 0        |

**properties**

## Symmetric Difference

**aka** _exclusive or_, _XOR_, _disjunctive union_

**notation** _in my [[math notation]]_ **`><`** and **`+`**

**notation** _in [[conventional math notation]]_ $\oplus$ or $\vartriangle$

**representation** _[[truth table]]_

| **`A`** | **`B`** | **`A + B`** |
| ------- | ------- | ----------- |
| 0       | 0       | 0           |
| 0       | 1       | 1           |
| 1       | 0       | 1           |
| 1       | 1       | 0           |

## Implication

**aka** _conditional statement_, _logical consequence_

**definition** if **`x = I`**, then the conditional statement **`x < y`** is said to be _vacuously true_

**definition** **`+x > +y`** is the _contrapositive_ of the statement **`x < y`**. they are logically equivalent

**definition** **`x > y`** is the _converse_ of the statement **`x < y`**. they are **not** logically equivalent

**definition** **`+x < +y`** is the _inverse_ of the statement **`x < y`**. they are **not** logically equivalent

> **note** even though the converse and inverse of a conditional statement are not logically equivalent, the converse of a statement is logically equivalent to the inverse of that statement

**definition**

let **`S < R < Q`** (square implies rectangle implies quadrilateral). then,

**`S`** is said to be a _sufficient condition_ for **`R`**---knowing that **`S`** is true allows the deduction that **`R`** is true

**`Q`** is said to be a _necessary condition_ for **`R`**---for **`R`** to be true, **`Q`** must be true

alternatively, let **`A < B`**. then,

**`A`** is said to be a _sufficient condition_ for **`B`**

**`B`** is said to be a _necessary condition_ for **`A`**

**notation** _in my [[math notation]]_ **`<`** and **`-|`** and **`>`** and **`|-`**

**notation** _in [[conventional math notation]]_ $\to$ and $\implies$

**representation** _[[truth table]]_

| **`A`** | **`B`** | **`A < B`** |
| ------- | ------- | ----------- |
| 0       | 0       | 1           |
| 0       | 1       | 1           |
| 1       | 0       | 0           |
| 1       | 1       | 1           |

**properties**

[[boolean#implication]] is a [[partial order]]

## Equivalence

**aka** _XNOR_, _double implication_, _equivalence_, _biconditional statement_, _bidirectional implication_

**notatio** _in my [[math notation]]_ **`==`** and **`=`**

**notation** _in [[conventional math notation]]_ $\Leftrightarrow$ or $\odot$ or $=$

**representation** _[[truth table]]_

| **`A`** | **`B`** | **`A == B`** |
| ------- | ------- | ------------ |
| 0       | 0       | 1            |
| 0       | 1       | 0            |
| 1       | 0       | 0            |
| 1       | 1       | 1            |

**properties**

[[boolean#equivalence]] is a [[relation#equivalence relation]]

## Difference

**notation** _in my [[math notation]]_ **`/\ +`**

**notation** _in [[conventional math notation]]_ $\backslash$

**representation** _[[truth table]]_

| **`A`** | **`B`** | **`A /\ +B`** |
| ------- | ------- | ------------- |
| 0       | 0       | 0             |
| 0       | 1       | 0             |
| 1       | 0       | 1             |
| 1       | 1       | 0             |

## identities

**properties**

identities below hold for all **`BB {x /\ y}`**

_identity_ **`x \/ O == x`**

_identity_ **`x /\ I == x`**

_excluded middle_ **`x \/ +x == I`**

_excluded middle_ **`x /\ +x == O`**

_double negation_ **`+I == O`**

_double negation_ **`+O == I`**

_[[idempotence]]_ **`x \/ x == x`**

_[[idempotence]]_ **`x /\ x == x`**

_domination_ **`x \/ I == I`**

_domination_ **`x /\ O == O`**

_[[involution]]_ **`++x == x`**

## properties

**properties**

properties below hold for all **`BB {x /\ y /\ z}`**

_commutativity_ **`x \/ y == y \/ x`**

_commutativity_ **`x /\ y == y /\ x`**

_associativity_ **`x \/ y^^z == x^^y \/ z`**

_associativity_ **`x /\ y__z == x__y /\ z`**

_distributivity_ **`x /\ y^^z == x__y \/ x__z`**

_distributivity_ **`x \/ y__z == x^^y /\ x^^z`**

_De Morgan's_ **`+x^^y == +x /\ +y`**

_De Morgan's_ **`+x__y == +x \/ +y`**

_absorption_ **`x \/ +x__y == x`**

_absorption_ **`x /\ +x^^y == x`**

_xor_ **`x >< y == x__+y \/ y__+x`** --- me

_xor_ **`x >< y == >< x = y`** --- me

_implication_ **`x < y == +x \/ y`**

_implication_ **`x > y == x \/ +y`**

_biconditional_ **`x = y == +x /\ +y \/ x __ y`**

_biconditional_ **`x = y == x -| y /\ x |- y`**

_and-implies_ **`x__y -| z == x -| z \/ y -| z`** --- me

_or-implies_ **`x^^y -| z == x -| z /\ y -| z`** --- me

_implies-or_ **`x -| y^^z == x -| y \/ x -| z`** --- me

_implies-and_ **`x -| y__z == x -| y /\ x -| z`** --- me

_portation_ **`x < y -| z == x__y -| z`** --- <https://www.cs.toronto.edu/~hehner/BAUA.pdf>

> **note** many [[boolean]] laws based on [[boolean#implication]]s become painfully obvious when seen from the perspective of [[type theory]] by the Curry--Howard correspondence. for instance, the [[boolean]] portation law corresponds to [[currying]] in [[type theory]]
