# Complement

*used to simplify subtraction by instead performing addition with the number’s complement*

it is one of the ways of representing negative numbers in [Digital System](Digital%20System%20bbedb8f9ddee431180e4d4feffaf88e3.md)s and is usually preferred over [Sign-Magnitude Notation](Sign-Magnitude%20Notation%20dd4d0883753f416b92418bfdcca30649.md)

there are two different complements for a given [Positional Numbering System](Positional%20Numbering%20System%20f9660787af6e443e96ee364c9c36ab9c.md), outlined below.

— [https://www.quora.com/In-computing-what-is-16-s-complement-Why-is-it-used](https://www.quora.com/In-computing-what-is-16-s-complement-Why-is-it-used)

## Radix Complement

*2’s complement in base 2, 16’s complement in base 16*

### calculation

*subtract each digit from the largest digit in the base and add 1*

```python
digit.map(max_digit - digit) + 1
```

### properties

see [Math Notation](Math%20Notation%207bc4575af1e541d6946b955774161a6a.md)

let $[A]$ be the Radix Complement of $A$ for all $A$, and assume $\R A$

$A \cdot [A] = 0$

$[[A]] = A$

$A \circ B = A \cdot [B]$

### notes

in **binary**, “subtract each digit from the largest digit in the base” can be thought of as “swap zeroes for ones and ones for zeros”

in **hex**, the bit pattern of the 16’s complement is the same as the bit pattern of the 2’s complement, and so the 16’s complement is never actually used in Computer Science.

Radix Complements can be used to easily **build adder-subtracters**:

- to add $A$ and $B$, feed in $A$ and $B$ to get $A + B$ as output
- to subtract $B$ from $A$, feed in $A$ and $\sim B$ and set the *CARRY IN* bit to get $A - B$ as output

### example

finding the 16’s complement of $1234_{16}$

```python
0xFFFF - 0x1234 + 1 = 0xEDCB + 1 = 0xEDCC
```

## Diminished Radix Complement

*1’s complement in base 2, 15’s complement in base 16*

### calculation

same as above, but without adding 1 at the end (or without setting the *CARRY IN* bit of an adder)

### notes

Diminished Radix Complements do **not** have the same properties as Radix Complements