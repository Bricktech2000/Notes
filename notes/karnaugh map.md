# Karnaugh Map

_a 2D version of a [[truth table]]_

> **AKA** K Map (informal abbreviation)

**representation**

_with exactly two variables_

| A/B | 0   | 1   |
| --- | --- | --- |
| 0   |     |     |
| 1   |     |     |

_with more than two variables_

as [[karnaugh map]]s are difficult to represent in more than two dimensions, multiple [[variable]]s must be grouped on a single axis when more than two [[variable]]s are present. variable groups must be chosen carefully; only one bit can change from one row and column to the next, explaining the $00, 01, 11, 10$ columns

| A/BC | 00  | 01  | 11  | 10  |
| ---- | --- | --- | --- | --- |
| 0    |     |     |     |     |
| 1    |     |     |     |     |

**applications**

[[karnaugh map]]s allow the simplification of [[boolean]] expressions without using [[boolean logic]]

> **procedure** _simplifying a [[boolean]] expression_
>
> 1. draw the [[boolean]] expression as a [[karnaugh map]], see [[disjunctive normal form]]
> 2. find “rectangles” of the same value, which can actually wrap around the edges of the [[karnaugh map]]. use the AND [[operator]] to group them together.
> 3. use the OR [[operator]] to join the “rectangles” together

## Implicant

see [[math notation]]

in a [[karnaugh map]],

**definition** an _Implicant_ is a product term that, if true, implies the [[boolean]] [[function]] represented is true (informally, $I = \top \vdash f x = \top$). it is a rectangle of $2[n] \equiv 1, 2, 4, 8 \dots$ values

**definition** a _Prime Implicant_ is an implicant (rectangle) that “can’t be explanded any larger”. more formally, it cannot be covered entirely by any other implicant.

**definition** an _Essential Prime Implicant_ is a prime implicant that cannot be removed without leaving a $1$ not covered. for all the $1$ values to be covered in a [[karnaugh map]], all essential prime implicants must be present, but all essential prime implicants being present does not imply all $1$ values have been covered. prime implicants that can be removed without leaving a $1$ not covered are known as _Non-Essential Prime Implicants_
