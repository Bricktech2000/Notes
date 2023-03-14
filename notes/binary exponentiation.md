# Binary Exponentiation

**aka** _exponentiation by squaring_

[[binary exponentiation]] is an [[algorithm]] to repeatedly apply [[monoid#operation]]s in [[logarithm]]ic time [[computational complexity]]

[[binary exponentiation]] requires its binary [[operator]] to be associative and requires the existence of an identity element; this corresponds to a [[monoid]]. [[binary exponentiation]] can be modified to work with [[semigroup]]s such as those formed by [[convolution]] by handling differently the case where $n = 0$. [[binary exponentiation]] can also be extended to work with negative exponents by ensuring the elements form a [[group]]s

[[binary exponentiation]] achieves [[logarithm]]ic time [[computational complexity]] by taking advantage of the fact that repeated [[monoid#operation]] applications can be represented as a [[tree#binary tree]]: $x * x * x * x * x * x * x * x =\!= (x * x * x) * (x * x * x) =\!= (x * (x * x)) * (x * (x * x))$

**representation** _using [[recursion]]_

the time [[computational complexity]] of [[binary exponentiation]] is $O\ \lceil \circ \rceil$

```python
def monoid_reduce(multiply, identity, x, n):
    # if n < 0: return monoid_reduce(multiply, identity, inverse(x), -n)  # for groups
    if n == 0: return identity
    if n % 2 == 0: return monoid_reduce(multiply, identity, multiply(x, x), n // 2)
    if n % 2 == 1: return multiply(x, monoid_reduce(multiply, identity, multiply(x, x), n // 2))
```

> **example**
>
> ```python
> binary_exponentiation = lambda x, n: monoid_reduce(lambda x, y: x * y, 1, x, n)
> binary_multiplication = lambda a, b: monoid_reduce(lambda a, b: a + b, 0, a, b)
> binary_concatenation = lambda s, n: monoid_reduce(lambda s, n: s + n, '', s, n)
> ```

# &mdash;

<https://en.wikipedia.org/wiki/Exponentiation_by_squaring>

<https://youtu.be/GrNJE6ogyQU>
