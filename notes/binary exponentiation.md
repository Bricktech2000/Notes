# Binary Exponentiation

**aka** _exponentiation by squaring_, _square-and-multiply algorithm_

**see** [[monoid#fold]], [[semigroup#fold]]

[[binary exponentiation]] is an [[algorithm]] for repeatedly applying [[semigroup#operation]]s on a single element in [[logarithm]]ic time [[computational complexity]]. for [[semigroup]]s the count is a strictly positive [[natural]], for [[monoid]]s (when a [[monoid#identity element]] is provided) the count is a [[natural]], and for [[group]]s (when a [[group#identity element]] and [[group#inverse]]s are provided) the count is an [[integer]]

[[binary exponentiation]] achieves [[logarithm]]ic time [[computational complexity]] by taking advantage of the fact that repeated [[semigroup#operation]] applications can be represented as a [[tree#binary tree]]: $x^6 = xxxxxx = (xxx)(xxx) = (x(xx))(x(xx))$

**representation** _using [[recursion]]_

the time [[computational complexity]] of [[binary exponentiation]] is $O\ (n.\ n)$

```python
def fastpow(mul, inv, id, x, n):
  if n == 0: return id  # for monoids and groups
  if n < 0: return fastpow(mul, inv, id, inv(x), -n)  # for groups
  x2 = fastpow(mul, inv, id, mul(x, x), n // 2)
  return mul(x, x2) if n % 2 else x2
```

> **example**
>
> ```python
> binary_exponentiation = lambda x, n: fastpow(lambda x, y: x * y, lambda x: 1 / x, 1, x, n)
> binary_multiplication = lambda a, b: fastpow(lambda a, b: a + b, lambda a: -a, 0, a, b)
> binary_concatenation = lambda s, n: fastpow(lambda s, c: s + c, None, '', s, n)
> ```

**equiv** _pencil-and-paper multiplication, in [[binary]]_ pencil-and-paper [[binary]] multiplicatiion consists of repeatedly doubling the multiplicand and adding it to the product if the corresponding bit in the multiplier is set; this corresponds to [[binary exponentiation]] on [[monoid]]s. if the multiplier is negative, the multiplicand is replaced by its additive inverse; this corresponds to [[binary exponentiation]] to [[group]]s

**equiv** _Russian multiplication_ Russian multiplication is a specialization of [[binary exponentiation]] to the [[monoid]] formed by the [[natural]]s under addition. the _mediation_ and _duplation_ steps along with "striking out the even rows" forms a one-to-one correspondence with the above [[python]] implementation of [[binary exponentiation]]

# ---

--- <https://en.wikipedia.org/wiki/Exponentiation_by_squaring>

--- <https://youtu.be/GrNJE6ogyQU>

--- <https://youtu.be/cbGB__V8MNk>

--- <https://youtu.be/HJ_PP5rqLg0>
