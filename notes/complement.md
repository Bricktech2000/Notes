# Complement

_used to simplify subtraction by instead performing addition with the number’s complement_

it is one of the ways of representing negative [[number]]s in [[digital system]]s and is usually preferred over [[sign-magnitude notation]]

there are two different [[complement]]s for a given [[positional numeral system]], outlined below.

&mdash; <https://www.quora.com/In-computing-what-is-16-s-complement-Why-is-it-used>

## Radix Complement

_2’s [[complement]] in base 2, 16’s [[complement]] in base 16_

> **procedure**
>
> subtract each digit from the largest digit in the base and add 1
>
> ```python
> digit.map(max_digit - digit) + 1
> ```

**properties**

**see** [[math notation]]

let $[A]$ be the [[complement#radix complement]] of $A$ for all $A$, and assume $\mathbb R A$

$A : [A] = 0$

$[[A]] = A$

$A \cdot B = A : [B]$

**applications**

[[complement#radix complement]]s can be used to easily **build adder-subtracters**

- to add $A$ and $B$, feed in $A$ and $B$ to get $A + B$ as output
- to subtract $B$ from $A$, feed in $A$ and $\sim B$ and set the _CARRY IN_ bit to get $A - B$ as output

> **note** in [[binary]], “subtract each digit from the largest digit in the base” can be thought of as “swap zeroes for ones and ones for zeros”
>
> in **hex**, the bit pattern of the 16’s [[complement]] is the same as the bit pattern of the 2’s [[complement]], and so the 16’s [[complement]] is almost never used in [[computer science]]

**examples**

> **example**
>
> finding the 16’s [[complement]] of $1234_{16}$:
>
> ```python
> 0xFFFF - 0x1234 + 1 = 0xEDCB + 1 = 0xEDCC
> ```

## Diminished Radix Complement

_1’s [[complement]] in base 2, 15’s [[complement]] in base 16_

> **note** [[complement#diminished radix complement]]s do **not** have the same properties as [[complement#radix complement]]s

> **procedure** identical to [[complement#radix complement]]s, but without adding $1$ at the end (or without setting the _CARRY IN_ bit of an adder)
