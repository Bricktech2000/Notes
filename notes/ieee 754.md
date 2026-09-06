# IEEE 754

**aka** _IEEE Standard for Floating-Point Arithmetic_

**see** [[floating-point number]]

> **resource** parody of the [[ieee 754]] standard by tom7 --- [[../references/nand.pdf]] --- <http://tom7.org/nand/nand.pdf>

[[ieee 754]] defines arithmetic formats, interchange formats, rounding rules, operations, and exception handling for [[floating-point number]] arithmetic --- <https://en.wikipedia.org/wiki/IEEE_754>. it is the standard for [[floating-point number]] arithmetic used by most modern computers

[[ieee 754]] perfectly specifies $+$, $-$, $\times$, $\div$, $\sqrt \cdot$ and $\cdot \times \cdot + \cdot$ (fused multiply-add)---they behave as if performed [[under]] infinite precision then rounded back at the end, according to the current rounding mode. any other operations are not strictly portable. --- IEEE Std 754-2008 and <https://youtu.be/gmAgvHaw9w4?t=995> and <https://youtu.be/gmAgvHaw9w4?t=2243> and <https://stackoverflow.com/questions/42181795/is-ieee-754-2008-deterministic>

[[ieee 754]] specifies four rounding modes: _roundTiesToEven_ `RN`, _roundTowardNegative_ `RD`, _roundTowardPositive_ `RU` and _roundTowardZero_ `RZ` --- IEEE Std 754-2008. _roundTiesToEven_ `RN` is the default and most [[programming language]]s don't support changing it --- <https://youtu.be/gmAgvHaw9w4?t=1069>. in [[c]], the functions `fegetround` and `fesetround` provide control of rounding modes; they can only be called under `#pragma STDC FENV_ACCESS ON`, otherwise the behavior is [[c#undefined behavior]] --- ISO/IEC 9899:TC3, $7.6 'Floating-point environment \<fenv.h\>'

> **resource** "semifloats" by l-m, on using _error-free transforms (EFTs)_ to implement `RD`, `RU` and `RZ` in terms of `RN`, with performance on the order of hardware floats --- <https://youtu.be/gmAgvHaw9w4?t=1555>

**properties** --- <http://tom7.org/nand/nand.pdf> and <https://youtu.be/Ae9EKCyI1xU?t=272> and Effective C, p. 47 and <https://youtu.be/gmAgvHaw9w4?t=959>

_equality is not a [[relation#reflexive relation]]_ `NAN != NAN`

_equality does not obey substitution_ `0.0 == -0.0` but `1.0 / 0.0 != 1.0 / -0.0`

_less-than is not inverse to at-least_ neither `0.0 < NAN` nor `0.0 >= NAN`

_not associative_ `(a + b) + c != a + (b + c)` for some `a, b, c`

_not distributive_ `m * (a + b) != m * a + m * b` for some `a, b, m`

## logarithmic property

**see** [[logarithmic number system]]

--- me

--- <https://youtu.be/p8u_k2LIZyo>

--- <https://en.wikipedia.org/wiki/Fast_inverse_square_root#Algorithm>

the bit representation of a positive normalized [[ieee 754]] [[floating-point number]] is a piecewise-linear approximation of its [[logarithm]], up to constant scaling (by the exponential of the width of the mantissa, $2^{23}$ for single-precision) and shifting (by the exponent bias, $127$ for single-precision, plus a tuning parameter $\sigma = 0.0430$). the intuition is that the most significant bits of the representation are the exponent, which stores the floor of the [[logarithm]] of the number (thus giving a step [[function]]), and the remaining bits uniformly count up from `...000000` to `...111111` within each exponent step (turning the step [[function]] into a piecewise-linear [[function]]). that piecewise-linear [[function]] ends up on the concave side of the [[logarithm]] [[function]], so the tuning parameter $\sigma$ nudges it back up
