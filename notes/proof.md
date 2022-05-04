# Proof

see [[improvability-theory]], [[zero-knowledge-proof]]

> A mathematical proof is an inferential argument for a mathematical statement, showing that the stated assumptions logically guarantee the conclusion. &mdash; Wikipedia

## Conditionals

see [[boolean-algebra]], [[boolean-operator]]s, [[math-notation]], [[boolean-expression]]

to prove a conditional statement such as $x \vdash y$:

1. assume $x$ is true
2. show that $y$ must follow from $x$ (using [[axiom]]s for formal proofs)

to prove a biconditional statement such as $x \equiv y$

1. prove $x \vdash y$, and then that $x \dashv y$
2. use the biconditional [[axiom]] $(x \vdash y \land x \dashv y) \equiv (x \equiv y)$ (see [[math-notation]])
