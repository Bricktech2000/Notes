# Complement

**see** [[math notation]]

_used to simplify subtraction by instead performing addition with the number’s complement_

it is one of the ways of representing negative [[number]]s in [[digital system]]s and is usually preferred over [[sign-magnitude notation]]

there are two different [[complement]]s for a given [[positional numeral system]], outlined below.

&mdash; <https://www.quora.com/In-computing-what-is-16-s-complement-Why-is-it-used>

## Radix Complement

_2’s [[complement]] in base 2, 16’s [[complement]] in base 16_

**definition**

> **procedure** _computing the [[complement#radix complement]] of an [[integer]]_
>
> subtract each digit from the largest digit in the base and add $1$
>
> ```rust
> digits.map(|digit| base - digit) + 1
> ```

> **equivalence** _[[complement#radix complement]] and modular arithmetic_
>
> [[complement#radix complement]]s can be thought of as modular arithmetic where the $n$'s complement of an [[integer]] $A$ of $p$ bits is the [[integer]] $B$ such that $\bmod [n]p\ \braket{A : B = 0}$ &mdash; me

**properties**

let $(\cdot A)$ be the [[complement#radix complement]] of $A$. then,

$A : (\cdot A) = 0$

$(\cdot (\cdot A)) = A$

$A \cdot B = A : (\cdot B)$

**applications**

[[complement#radix complement]]s can be used to easily **build adder-subtracters**

- to add $A$ and $B$, feed in $A$ and $B$ to get $A : B$ as output
- to subtract $B$ from $A$, feed in $A$ and $\times B$ and set the _CARRY IN_ bit to get $A \cdot B$ as output

> **note** in [[binary]], “subtract each digit from the largest digit in the base” can be thought of as “swap zeroes for ones and ones for zeros”
>
> in [[hexadecimal]], the bit pattern of the 16’s [[complement]] is the same as the bit pattern of the 2’s [[complement]], and so the 16’s [[complement]] is almost never used in [[computer science]]

**examples**

> **example**
>
> finding the 16’s [[complement]] of $1234_{16}$, see [[positional numeral system]]
>
> ```python
> 0xFFFF - 0x1234 + 1 = 0xEDCB + 1 = 0xEDCC
> ```

## Diminished Radix Complement

_1’s [[complement]] in base 2, 15’s [[complement]] in base 16_

> **note** [[complement#diminished radix complement]]s do **not** have the same properties as [[complement#radix complement]]s

> **procedure** identical to [[complement#radix complement]]s, but without adding $1$ at the end (or without setting the _CARRY IN_ bit of an adder)
