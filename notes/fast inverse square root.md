# Fast Inverse Square Root

[[fast inverse square root]] is an [[algorithm]] that estimates $\overline{\sqrt x}$ for a 32-bit [[ieee 754]] [[floating-point number]] $x$

> **resource** `Q_rsqrt` in its natural habitat --- <https://github.com/id-Software/Quake-III-Arena/blob/master/code/game/q_math.c#L552-L572>

**representation** _original implementation, tabs expanded_

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
//  y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

#ifndef Q3_VM
#ifdef __linux__
    assert( !isnan(y) ); // bk010122 - FPE?
#endif
#endif
    return y;
}
```

**representation** _more readable version, mostly equivalent_ --- Wikipedia and me

```c
#include <stdint.h>

float Q_rsqrt(float x) {
  union { float f; uint32_t i; } conv = { .f = x };
  conv.i = 0x5f3759df - (conv.i >> 1);
  conv.f *= 1.5f - (x * 0.5f * conv.f * conv.f);
  return conv.f;
}
```

> **note** depending on the cycle count of floating-point multiplies, performance can be improved further by replacing `x * 0.5f` with `x - 0x800000` to decrement the exponent directly --- <https://youtu.be/tmb6bLbxd08&t=416>

## explanation

--- me

--- <https://youtu.be/p8u_k2LIZyo>

--- <https://en.wikipedia.org/wiki/Fast_inverse_square_root#Algorithm>

we have $\log_2 \overline{\sqrt x} = -\overline 2 \log_2 x$ and we know that the bit representation of an [[ieee 754]] [[floating-point number]] is an approximation of its [[logarithm]], so we can implement this in code as `conv.i = -(conv.i >> 1);`. the magic constant `0x5f3759df` is approximately $1.5(127 - \sigma) \cdot 2^{23}$, a fix-up for the exponent bias $127$ in the $23$rd bit and for the tuning parameter $\sigma = 0.0430$, that are off by $-1.5$ because they got halved then negated

we can improve our initial guess using a root-finding method; specifically, $\overline{\sqrt x}$ is a root of the [[function]] $y.\ y - \overline{\sqrt x}$ with [[derivative]] $1$. to apply [[newton's method]] we want the [[derivative]] to contain maximal information, so we solve for $x$ to get $y.\ \overline y^2 - x$ with [[derivative]] $-2\overline y^3$. then, [[newton's method]] gives $y_{n + 1} = y_n - (-\overline 2 y_n^3)(\overline y_n^2 - x) = y_n(\frac 3 2 - \overline 2 xy_n^2)$, which is implemented in code as `conv.f *= 1.5f - (x * 0.5f * conv.f * conv.f);`
