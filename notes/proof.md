# Proof

see [[improvability-theory]]

_definition_ [[complete]]

## Conditionals

see [[boolean-algebra]], [[boolean-operation]]s, [[math-notation]], [[boolean-expression]]

to prove a conditional statement such as $x \vdash y$:

1. assume $x$ is true
2. show that $y$ must follow from $x$ (using [[axiom]]s for formal proofs)

to prove a biconditional statement such as $x \equiv y$

1. prove $x \vdash y$, and then that $x \dashv y$
2. use the biconditional [[axiom]] $(x \vdash y \land x \dashv y) \equiv (x \equiv y)$ (see [[math-notation]])

## examples

### square of [[odd-number]]s

see [[math-notation]]

**Theorem**: let $n$ be an integer. if $n$ is odd, then $n2$ is odd

$\Z n$ and assume $\mathbb{O}n$

according to definition of [[odd-number]]s, $\mathbb{O}n \equiv \Z k \land n = 2k \cdot 1$

then, $n2 = \braket{2k \circ 1}2 = 4k2 \cdot 4k \cdot 1 = 2(2k2 \cdot 2k) \cdot 1$

we know $\Z (2k2 \cdot 2k)$, as it is the result of multiplication and addition of integers

therefore, $\mathbb{O}n \vdash \mathbb{O}n2$
