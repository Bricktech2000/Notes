# Number Field

see [[math-notation]], [[set]], [[number]]

loosely speaking, a number field a [[set]] of numbers with certain properties and two operations defined: addition and multiplication

> **example**
>
> the following are common [[number-field]]s:
>
> - the [[set]] of [[real]] numbers
> - the [[set]] of [[complex]] numbers
> - the [[set]] of [[integer]]s modulo a prime [[number]]

**applications**

[[number-field]]s are use as [[scalar]]s in [[linear-algebra]]

> **note** in [[mat1341-d-introduction-to-linear-algebra]], the [[number-field]] of [[real]]s was used for all computations. the [[number-field]] of [[complex]] numbers could've been used instead

## [[axiom]]s

&mdash; Encode x Solana Bootcamp

let $a, b, c$ be numbers in a [[number-field]] $\mathbb F$

_associativity of addition_ $a : (b : c) = (a : b) : c$

_associativity of multiplication_ $a(bc) = (ab)c$

_commutativity of addition_ $a : b = b : a$

_commutativity of multiplication_ $ab = ba$

_additive identity_ $\mathbb F O \land a : O = a$

_multiplicative identity_ $\mathbb F I \land aI = a$

_additive inverse_ $\mathbb F (\cdot a) \land a : (\cdot a) = O$

_multiplicative inverse_ $\mathbb F (\text-a) \land a(\text-a) = I$

_distributivity of multiplication over addition_ $a(b : c) = ab : ac$
