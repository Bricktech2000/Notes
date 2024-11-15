# Fast Inverse Square Root

**see** [[math notation]]

the [[fast inverse square root]] is an [[algorithm]] that estimates **`--\x/`** for a 32-bit [[ieee 754]] [[float]]ing-point number **`x`**

**representation** _original implementation stripped of [[c#preprocessor]] directives_

```c
float Q_rsqrt( float number )
{
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y  = number;
    i  = * ( long * ) &y;                       // evil floating point bit level hacking
    i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
    y  = * ( float * ) &i;
    y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

    return y;
}
```

**representation** _more readable version, mostly equivalent_

```c
#include <stdint.h> // uint32_t

float Q_rsqrt(float number)
{
  union { float f; uint32_t i; } conv = { .f = number };
  conv.i  = 0x5f3759df - (conv.i >> 1);
  conv.f *= 1.5F - (number * 0.5F * conv.f * conv.f);
  return conv.f;
}
```

## explanation

### floating-point bit representation

**aka** _evil floating point bit level hacking_

let **`x = 2[e_x] | m_x`**. assuming **`x |- 0`** and **`1 -| m_x -| 2`**, according to [[ieee 754]], we get **`i_x = L(e_x : B) : L(m_x .. 1)`**, where

- **`i_x`** is the [[natural]] whose bit representation is that of the [[ieee 754]] [[float]] **`x`**
- **`B = 127`** is the [[ieee 754]] _exponent bias_ for 32-bit floats
- **`L = 2[23]`** is abstracting away a "magic" constant for 32-bit floats

> **note** multiplying the [[exponent]] by **`L`** performs a bitwise left shift so the [[exponent]] lands in the right spot. multiplying the mantissa by **`L`** turns it into a 23-bit [[natural]]. adding **`B`** to **`e_x`** as per [[ieee 754]] allows for the representation of negative [[exponent]]s. subtracting **`1`** from **`m_x`** as per [[ieee 754]] saves one bit in the representation, since **`1 -| m_x -| 2`**

### efficient logarithms

let **`y = -- \x/`**. since square roots and divisions are expensive to compute, we derive **`/y\2 = ..-2/x\2`**. we need to look for an efficient way to compute base-2 [[logarithm]]s

given **`x = 2[e_x] | m_x`**, **`/x\2 = e_x : /m_x\2`**. since **`1 -| m_x -| 2`**, a common approximation can be used, **`/m_x\2 ~ m_x .. 1 : ss`** where **`ss`** is a free parameter used to tune the approximation. therefore, **`/x\2 ~ e_x : m_x .. 1 : ss`**

given **`i_x = L(e_x : B) : L(m_x .. 1)`**, we get **`i_x = L(e_x : B : m_x .. 1) = L(e_x : m_x .. 1 : ss : B .. ss) ~  L/x\2 : L(B .. ss)`**. solving, we get **`/x\2 ~ -Li_x .. (B .. ss)`**; in other words, the [[ieee 754]] bit representation of a [[float]] is approximately its own [[logarithm]] up to constant scaling and shifting

### inverse square root

**aka** _what the fuck_

substituting the above into **`/y\2 = ..-2/x\2`**, we get **`-Li_y .. (B .. ss) ~ ..-2 | -Li_x .. (B .. ss)`**. thus, **`i_y ~ 3-2L(B .. ss) .. -2i_x`**, which is written in code as follows, in which the magic `0x5f3759df` is derived from the value of **`3-2L(B .. ss)`** with **`ss ~ 0 0450466-10000000`**:

```c
i = 0x5f3759df - (i >> 1);
```

### improving the approximation

**aka** _1st iteration_

given **`y = -- \x/`**, we can use [[newton's method]] to refine the [[function#root]]s of **`y. -y2 .. x`**. with **`f y = -y2 .. x`**, we get **`dd f = y. ..2-y3`**. through [[newton's method]], **`y_* = y .. (-y2 .. x -- ..2-y3) = y : (y .. xy3 -- 2) = y | 3-2 .. xy2-2`**, which is written in code as follows:

```c
y = y * (1.5F - x*0.5F*y*y);
```

## ---

--- <https://en.wikipedia.org/wiki/Fast_inverse_square_root#Overview_of_the_code>

--- <https://youtu.be/p8u_k2LIZyo>
