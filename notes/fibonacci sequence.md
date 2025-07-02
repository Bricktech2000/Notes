# Fibonacci Sequence

**see** [[sequence]]

**definition** $F_{n + 1} = F_n + F_{n - 1} \land F_0 = 0 \land F_1 = 1$

## self-reference

**see** [[functional programming]], [[lambda-calculus]]

the [[fibonacci sequence]] can be defined in a self-referencial form that can be operationalized with a [[fixed point]] [[combinator]] like the [[combinator#y combinator]]:

```haskell
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
fib n = fibs!!n
```

this gives a natural derivation of the generating function for the [[fibonacci sequence]], $G\ x = \sum_{n = 0}^\infty F_nx^n$. we translate over the self-referential form to get $G\ x = 0 + x + x^2(G\ x) + x(G\ x)$, then solve $G\ x = \frac{x}{1 - x - x^2}$ --- me

## diagonalization

**see** [[linear algebra]], [[eigen]]

as a [[linear map]], $\begin{bmatrix}F_n \\ F_{n + 1}\end{bmatrix} = \begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix} \begin{bmatrix}F_{n - 1} \\ F_n\end{bmatrix}$, and so $\begin{bmatrix}F_n \\ F_{n + 1}\end{bmatrix} = \begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix}^n \begin{bmatrix}F_0 \\ F_1\end{bmatrix}$. the [[linear map#standard matrix]] is a [[matrix#diagonalizable matrix]] because it has two distinct [[eigen#value]]s, namely $\varphi = \frac{1 + \sqrt 5}{2}$ and $\psi = \frac{1 - \sqrt 5}{2} = 1 - \varphi = -\overline\varphi$ with [[eigen#vector]]s $\begin{bmatrix}1 \\ \varphi\end{bmatrix}$ and $\begin{bmatrix}1 \\ \psi\end{bmatrix}$. this means we can:

$$
\begin{align*}
\begin{bmatrix}F_n \\ F_{n + 1}\end{bmatrix}
&= \begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix}^n \begin{bmatrix}F_0 \\ F_1\end{bmatrix} \\
&= \left(\begin{bmatrix}1 & 1 \\ \varphi & \psi\end{bmatrix} \begin{bmatrix}\varphi & 0 \\ 0 & \psi\end{bmatrix} \begin{bmatrix}1 & 1 \\ \varphi & \psi\end{bmatrix}^{-1}\right)^n \begin{bmatrix}0 \\ 1\end{bmatrix} \\
&= \begin{bmatrix}1 & 1 \\ \varphi & \psi\end{bmatrix} \begin{bmatrix}\varphi^n & 0 \\ 0 & \psi^n\end{bmatrix} \left(\overline{\psi - \varphi}\begin{bmatrix}\psi & -1 \\ -\varphi & 1\end{bmatrix}\right) \begin{bmatrix}0 \\ 1\end{bmatrix} \\
&= \overline{\psi - \varphi}\begin{bmatrix}\psi^n - \varphi^n \\ \psi^{n + 1} - \varphi^{n + 1}\end{bmatrix}
\end{align*}
$$

and get the closed-form $\displaystyle F_n = \frac{\varphi^n - \psi^n}{\varphi - \psi}$ "Binet's formula" --- <https://youtu.be/KzT9I1d-LlQ?t=1194>

## binary exponentiation

**see** [[linear algebra]], [[binary exponentiation]], [[karatsuba algorithm]]

as a [[linear map]], $\begin{bmatrix}F_n \\ F_{n + 1}\end{bmatrix} = \begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix} \begin{bmatrix}F_{n - 1} \\ F_n\end{bmatrix}$, and so $\begin{bmatrix}F_{n + k} \\ F_{n + k + 1}\end{bmatrix} = \begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix}^n \begin{bmatrix}F_k \\ F_{k + 1}\end{bmatrix}$. by setting $k := -1$ then $k := 0$ to extract columns, we get $\begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix}^n = \begin{bmatrix}F_{n - 1} & F_n \\ F_n & F_{n + 1}\end{bmatrix}$, and we observe that any [[iteration]] of our [[linear map]] will be of the form $\begin{bmatrix}a & b \\ b & a + b\end{bmatrix}$ with $a, b \in \mathbb N$. we can take advantage of this to derive efficient "double" and "increment" operations for [[binary exponentiation]] that operate [[under]] the bijection $(a, b) \leftrightarrow \begin{bmatrix}a & b \\ b & a + b\end{bmatrix}$:

- $\begin{bmatrix}a & b \\ b & a + b\end{bmatrix}^2 = \begin{bmatrix}a^2 + b^2 & (a + b)^2 - a ^2 \\ (a + b)^2 - a ^2 & b^2 + (a + b)^2\end{bmatrix}$, giving $(a, b).\ (a^2 + b^2, (a + b)^2 - a ^2)$
- $\begin{bmatrix}a & b \\ b & a + b\end{bmatrix} \begin{bmatrix}0 & 1 \\ 1 & 1\end{bmatrix} = \begin{bmatrix}b & a + b \\ a + b & a + 2b\end{bmatrix}$, giving $(a, b).\ (b, a + b)$

in the [[python]] implementation we use $b(2a + b) = (a + b)^2 - a^2$ just to avoid having to store the temporary value $a^2$:

```python
def fib(n):
  def fib2(n):
    if n == 0: return (1, 0)
    if n == -1: return (-1, 1)
    a, b = fib2(n // 2)
    a, b = a**2 + b**2, b * (2 * a + b)
    return (b, a + b) if n % 2 else (a, b)
  a, b = fib2(n - 1)
  return a + b
```

> **note** the key here is that [[matrix#multiplication]] is a [[monoid]], and is thus associative: not only can you iterate a [[linear map]] on a base case, you can also compose [[linear map]]s together into new [[linear map]]s that are no more expensive to iterate

### ---

--- <https://en.wikipedia.org/wiki/Fibonacci_sequence#Matrix_form>

--- <https://youtu.be/KzT9I1d-LlQ>

--- <https://youtu.be/LXm6ygZ3h7A>

--- <https://gmplib.org/manual/Fibonacci-Numbers-Algorithm>
