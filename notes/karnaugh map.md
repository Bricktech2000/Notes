# Karnaugh Map

_2D [[truth table]]s_

**see** [[math notation]]

**representation**

_with exactly two variables_

| **`A/B`** | **`0`** | **`1`** |
| --------- | ------- | ------- |
| **`0`**   |         |         |
| **`1`**   |         |         |

_with more than two variables_

as [[karnaugh map]]s are difficult to represent in more than two dimensions, multiple [[variable]]s must be grouped on a single axis when more than two [[variable]]s are present. variable groups must be chosen carefully; only one bit can change from one row and column to the next, explaining the **`00, 01, 11, 10`** columns

| **`A/BC`** | **`00`** | **`01`** | **`11`** | **`10`** |
| ---------- | -------- | -------- | -------- | -------- |
| **`0`**    |          |          |          |          |
| **`1`**    |          |          |          |          |

**applications**

[[karnaugh map]]s help simplify [[boolean]] expressions to [[disjunctive normal form]] and [[conjunctive normal form]] through [[karnaugh map#implicant]]s

## Implicant

**see** [[math notation]]

in a [[karnaugh map]],

**definition** an _implicant_ is a product term that, if true, implies the [[boolean]] [[function]] represented is true. it is a rectangle of **`{{1, 2, 4, 8 ...}}`** values

**definition** a _prime implicant_ is an implicant (rectangle) that "can't be explanded any larger". more formally, it cannot be covered entirely by any other implicant.

**definition** an _essential prime implicant_ is a prime implicant that cannot be removed without leaving a **`1`** not covered. for all the **`1`** values to be covered in a [[karnaugh map]], all essential prime implicants must be present, but all essential prime implicants being present does not imply all **`1`** values have been covered. prime implicants that can be removed without leaving a **`1`** not covered are known as _non-essential prime implicants_
