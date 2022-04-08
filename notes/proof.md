# Proof

see [[improvability-theory]]

> A mathematical proof is an inferential argument for a mathematical statement, showing that the stated assumptions logically guarantee the conclusion. &mdash; Wikipedia

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

> **theorem**: let $n$ be an [[integer]]. if $n$ is odd, then $n2$ is odd

$\Z n$ and assume $\mathbb{O}n$

according to definition of [[odd-number]]s, $\mathbb{O}n \equiv \Z k \land n = 2k \cdot 1$

then, $n2 = [2k \circ 1] = 4k2 \cdot 4k \cdot 1 = 2(2k2 \cdot 2k) \cdot 1$

we know $\Z (2k2 \cdot 2k)$, as it is the result of multiplication and addition of [[integer]]s

therefore, $\mathbb{O}n \vdash \mathbb{O}n2$

### proving an expression is an [[even-number]]

prove $n2 \cdot 3n \cdot 8$ is an [[even-number]] for all $\Z n$

let $n = 2k \cdot q \land \Z k \land \Z q$

$(2k \cdot q)2 \cdot 3(2k \cdot q) \cdot 8$

$4k2 \cdot 4kq \cdot q2 \cdot 6k \cdot 3q \cdot 8$

$(2\ |\ 2k2 \cdot 2kq \cdot 3k \cdot 4 \cdot q) \cdot q2 \cdot q$

---

$n2 \cdot n$

let $n = 2k \land \Z k$

$(2k)2 \cdot 2k$

$4k2 \cdot 2k$

$2\ |\ 2k2 \cdot k$

since $\Z (2k2 \cdot k)$, the above must be an [[even-number]]

let $n = 2k \cdot 1 \land \Z k$

$(2k \cdot 1)2 \cdot 2k \cdot 1$

$4k2 \cdot 4k \cdot 1 \cdot 2k \cdot 1$

$2\ |\ 2k2 \cdot 3k \cdot 1$

since $\Z (2k2 \cdot 3k \cdot 1)$, the above must be an [[even-number]]
