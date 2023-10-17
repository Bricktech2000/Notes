# IEEE 754

**aka** _IEEE Standard for Floating-Point Arithmetic_

**see** [[math notation]], [[float]]

> **resource** parody of the [[ieee 754]] standard by tom7 &mdash; <http://tom7.org/nand/nand.pdf>

[[ieee 754]] defines arithmetic formats, interchange formats, rounding rules, operations, and [[exception]] handling for [[float]]ing-point arithmetic &mdash; <https://en.wikipedia.org/wiki/IEEE_754>. it is the standard for [[float]]ing-point arithmetic used by most modern computers

**properties** &mdash; <http://tom7.org/nand/nand.pdf> and <https://youtu.be/Ae9EKCyI1xU?t=272> and Effective C, p. 47

_equality is not a [[relation#reflexive relation]]_ **`"NaN" + "NaN"`**

_equality does not obey substitution_ **`0 = .0`** but **`1 -- 0 + 1 -- .0`**

_not associative_ **`(a : b) : c + a : (b : c)`** for some **`a, b, c`**

_not distributive_ **`m(a : b) + ma : mb`** for some **`a, b, m`**
