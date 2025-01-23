# Binary Exponentiation

**aka** _exponentiation by squaring_, _square-and-multiply algorithm_

**see** [[reduce function]]

[[binary exponentiation]] is an [[algorithm]] to repeatedly apply [[monoid#operation]]s in [[logarithm]]ic time [[computational complexity]]

[[binary exponentiation]] requires its binary [[operator]] to be associative and requires the existence of an identity element; this corresponds to a [[monoid]]. [[binary exponentiation]] can be modified to work with [[semigroup]]s such as those formed by [[convolution]] by handling differently the case where **`n = 0`**. [[binary exponentiation]] can also be extended to work with negative exponents by ensuring the elements form a [[group]]

[[binary exponentiation]] achieves [[logarithm]]ic time [[computational complexity]] by taking advantage of the fact that repeated [[monoid#operation]] applications can be represented as a [[tree#binary tree]]: **`{x}6 == xxxxxx == (xxx)(xxx) == (x(xx))(x(xx))`**

**representation** _using [[recursion]]_

the time [[computational complexity]] of [[binary exponentiation]] is **`O /.\`**

```python
def monoid_reduce(mul, id, x, n):
  # if n < 0: return monoid_reduce(mul, id, inverse(x), -n)  # for groups
  if n == 0: return id
  if n % 2 == 0: return monoid_reduce(mul, id, mul(x, x), n // 2)
  if n % 2 == 1: return mul(x, monoid_reduce(mul, id, mul(x, x), n // 2))
```

> **example**
>
> ```python
> binary_exponentiation = lambda x, n: monoid_reduce(lambda x, y: x * y, 1, x, n)
> binary_multiplication = lambda a, b: monoid_reduce(lambda a, b: a + b, 0, a, b)
> binary_concatenation = lambda s, n: monoid_reduce(lambda s, n: s + n, '', s, n)
> ```

**equiv** _pencil-and-paper multiplication, in [[binary]]_ pencil-and-paper [[binary]] multiplicatiion consists of repeatedly doubling the multiplicand and adding it to the product if the corresponding bit in the multiplier is set; this corresponds to [[binary exponentiation]] on [[monoid]]s. if the multiplier is negative, the multiplicand is replaced by its additive inverse; this corresponds to the extension of [[binary exponentiation]] to [[group]]s

**equiv** _Russian multiplication_ Russian multiplication is a specialization of [[binary exponentiation]] to the [[monoid]] formed by the [[natural]]s under addition. the _mediation_ and _duplation_ steps along with "striking out the even rows" forms a one-to-one correspondence with the above [[python]] implementation of [[binary exponentiation]]

# ---

--- <https://en.wikipedia.org/wiki/Exponentiation_by_squaring>

--- <https://youtu.be/GrNJE6ogyQU>

--- <https://youtu.be/cbGB__V8MNk>
