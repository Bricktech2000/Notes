# Field

**see** [[math notation]], [[set]], [[number]], [[algebraic structure]]

loosely speaking, a [[field]] is a [[set]] of numbers with certain properties and two operations defined: addition and multiplication

> **example**
>
> the following are common [[field]]s:
>
> - the [[set]] of [[real]] numbers
> - the [[set]] of [[complex]] numbers
> - the [[set]] of [[integer]]s modulo a prime [[number]]
> - the [[set]] of [[rational]] numbers &mdash; <https://youtu.be/vdjYiU6skgE>
> - the [[set]] of [[p-adic]] numbers

**applications**

[[field]]s are use as [[scalar]]s in [[linear algebra]]

> **note** in [[mat1341 d introduction to linear algebra]], the [[field]] of [[real]]s was used for all computations. the [[field]] of [[complex]] numbers could've been used instead

## [[axiom]]s

&mdash; Encode x Solana Bootcamp

let **`a, b, c`** be numbers in a [[field]] **`FF`**

_associativity of addition_ **`a : (b : c) = (a : b) : c`**

_associativity of multiplication_ **`a(bc) = (ab)c`**

_commutativity of addition_ **`a : b = b : a`**

_commutativity of multiplication_ **`ab = ba`**

_additive identity_ **`FF O /\ a : O = a`**

_multiplicative identity_ **`FF I /\ aI = a`**

_additive inverse_ **`FF (.a) /\ a : (.a) = O`**

_multiplicative inverse_ **`FF (-a) /\ a(-a) = I`**

_distributivity of multiplication over addition_ **`a(b : c) = ab : ac`**

## Absolute Value

&mdash; <https://youtu.be/vdjYiU6skgE?t=28>

&mdash; <https://en.wikipedia.org/wiki/Absolute_value_(algebra)>

**definition**

an _absolute value_ on a [[field]] is a [[function]] that [[map]]s elements of the [[field]] to the [[set]] of [[real]] numbers and satisfies the following [[axiom]]s:

_positive_ **`||x|| |- 0`**

_positive definite_ **`||x|| = 0 == x = 0`**

_multiplicative_ **`||xy|| = ||x||||y||`**

_triange inequality_ **`||x : y|| -| ||x|| : ||y||`**
