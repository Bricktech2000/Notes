# Complement

**see** [[math notation]]

_used to simplify subtraction by instead performing addition with the number's complement_

it is one of the ways of representing negative [[number]]s in [[digital system]]s and is usually preferred over [[sign-magnitude notation]]

there are two different [[complement]]s for a given [[positional numeral system]], outlined below.

&mdash; <https://www.quora.com/In-computing-what-is-16-s-complement-Why-is-it-used>

## Radix Complement

_2's [[complement]] in base 2, 16's [[complement]] in base 16_

**definition**

> **procedure** _computing the [[complement#radix complement]] of an [[integer]]_
>
> subtract each digit from the largest digit in the base and add **`1`**
>
> ```rust
> digits.map(|digit| base - digit) + 1
> ```
>
> > **note** in [[binary]], "subtracting each digit from the largest digit in the base" can be thought of as "swap zeroes for ones and ones for zeros"
>
> > **note** the [[complement#radix complement]] of an [[integer]] can be thought of as its representation in a [[positional numeral system]] where the most significant digit is assigned a negative weight. for example, **`1011`**, the 2's complement of **`5`**, can be interpreted as **`(.8) : 2 : 1 = .5`**

> **note** in [[hexadecimal]], the bit pattern of the 16's [[complement]] is the same as the bit pattern of the 2's [[complement]], and so the 16's [[complement]] is rarely used

**equiv** _modular arithmetic_ [[complement#radix complement]]s can be thought of as modular arithmetic where the **`n`**'s complement of an [[integer]] **`A`** of **`p`** bits is the [[integer]] **`B`** such that **`"mod" [n]p {A : B = 0}`** &mdash; me

**equiv** _truncated [[p-adic]]s_ [[complement#radix complement]]s can be thought of as truncated **`2`**-adic numbers:

- `00000010.` is close to **`2`** with respect to **both** the **`2`**-adic metric and the real metric; `11111110.` is close to **`.2`** with respect to **only** the **`2`**-adic metric. consequently, their sum `100000000.` is close to **`0`** with respect to **only** the **`2`**-adic metric
- `00000001.` is close to **`3-3`** with respect to **both** the **`2`**-adic metric and the real metric; `.01010101` is close to **`1-3`** with respect to **only** the real metric. consequently, their sum `00000001.01010101` is close to **`4-3`** with respect to **only** the real metric
- `10101011.` is close to **`1-3`** with respect to **only** the **`2`**-adic metric; consequently, its triple `1000000001.` is close to **`1`** with respect to **only** the **`2`**-adic metric
- `.10101010` is close to **`2-3`** with respect to **only** the real metric; consequently, its triple `1.11111110` is close to **`2`** with respect to **only** the real metric
- `10101011.` is close to **`1-3`** with respect to **only** the **`2`**-adic metric; `.10101010` is close to **`2-3`** with respect to **only** the real metric. consequently, their sum `10101011.01010101` is close to **`1`** with respect to **neither** the **`2`**-adic metric nor the real metric

"ignoring the carry bit" is a hack to make results close with respect to the real metric. those carry bits are tiny rounding errors with respect to the **`2`**-adic metric even though they throw everything off with respect to the real metric

**properties**

let **`(.A)`** be the [[complement#radix complement]] of **`A`**. then,

**`A : (.A) = 0`**

**`(.(.A)) = A`**

**`A.B = A : (.B)`**

**applications**

[[complement#radix complement]]s can be used to easily **build adder-subtracters**

- to add **`A`** and **`B`**, feed in **`A`** and **`B`** to get **`A : B`** as output
- to subtract **`B`** from **`A`**, feed in **`A`** and **`><B`** and set the _CARRY IN_ bit to get **`A.B`** as output

**examples**

> **example**
>
> finding the 16's [[complement]] of `0x1234`
>
> ```python
> 0xFFFF - 0x1234 + 1 = 0xEDCB + 1 = 0xEDCC
> ```

## Diminished Radix Complement

_1's [[complement]] in base 2, 15's [[complement]] in base 16_

> **note** [[complement#diminished radix complement]]s do **not** have the same properties as [[complement#radix complement]]s

> **procedure** identical to [[complement#radix complement]]s, but without adding **`1`** at the end (or without setting the _CARRY IN_ bit of an adder)
