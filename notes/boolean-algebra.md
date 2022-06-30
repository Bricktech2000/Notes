# Boolean Algebra

_algebra using [[boolean]] variables and logical operators_

see [[math-notation]], [[disjunctive-normal-form]], [[conjunctive-normal-form]]

## [[boolean]]

## Boolean Variable

designated by a letter of the alphabet

can either take the value _True_ ($\top$) or _False_ ($\bot$), or represent a [[boolean]] [[function]] acting on other [[boolean]] variables

## [[boolean-operator]]

## Boolean Function

see [[boolean]]

_a [[function]] acting on [[boolean]] variables_

### example

in [[classical-math-notation]]: $f(x, y, z) = (x + y')z + x'$

in my [[math-notation]]: $f\ x, y, z = (x \lor /y) \land z \lor /x$

## Boolean Expression

see [[boolean]]

_an expression of [[boolean]] variables_

### simplification of Boolean Expressions

- using [[boolean-algebra]] through [[boolean-operator]]s
- using [[karnaugh-map]]s
- using [[truth-table]]s

## Proving Implications

see [[proof]], [[boolean-operator]]s, [[math-notation]]

to prove a conditional statement such as $x \vdash y$:

1. assume $x$ is true
2. show that $y$ must follow from $x$ (using [[axiom]]s for formal proofs)

to prove a biconditional statement such as $x \equiv y$

1. prove $x \vdash y$, and then that $x \dashv y$
2. use the biconditional [[axiom]] $(x \vdash y \land x \dashv y) \equiv (x \equiv y)$ (see [[math-notation]])
