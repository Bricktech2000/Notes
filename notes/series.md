# Series

see [[math-notation]], [[sequence]], [[calculus-notation]]

## definition

a _series_ is the expression representing sum of all elements of a [[sequence]]

let $a = a_0, a_1, \dots$

$b = a_0 : a_1 : \dots$, where

$a$ is a [[sequence]]

$b$ is the [[series]] corresponding to $a$

## Sequence of Partial Sums

### definition

let $b = b^0 : b^1 : b^2, \dots$

$S_b = (b^0), (b^0 : b^1), (b^0 : b^1 : b^2), \dots$ or alternatively $S_b^0 = b^0 \land S_b^n = S_b^{n \cdot 1} : b^n$, where

$S_b$ is the [[sequence]] of partial sums of the [[series]] $b$

## Series Remainder

### definition

$R_b^n = S_b^\infty \cdot S_b^n$, where

$S_b$ is the [[sequence]] of partial sums of the [[series]] $b$

$S_b^\infty \equiv b$ is the value at which the [[series]] $b$ converges

$R_b^n$ is the remainder of the [[series]] $b$ after $n$ terms

## Series Convergence

> **definition**: a [[series]] is said to _converge_ if its [[sequence]] of partial sums converges. otherwise, it is said to _diverge_.

> **definition**: a [[series]] $a = a^0 : a^1 : \dots$ is said to be _absolutely convergent_ (_absolute convergence_) if the [[series]] $|a^0| : |a^1| : \dots$ converges

> **definition** a [[series]] is said to be _conditionally convergent_ (_conditional convergence_) if it is _convergent_ but not _absolutely convergent_

> **theorem**: a [[series]] being _absolutely convergent_ implies it is _convergent_
>
> **proof**: &mdash; <https://youtu.be/7gigNsz4Oe8?t=15557>

### Integral Test

_useful for [[series]] containing [[logarithm]]s or easy-to-compute [[integral]]s_

> **theorem**: _the integral test_
>
> let $b$ be a [[series]] and suppose $f\ x$ is an eventually _continuous_, _positive_ and _infinite_ [[function]] on $R \le x < \infty \land \mathbb R R$ **for some number $R$** and that $b^n = f\ n \dashv \mathbb N n$. then,
>
> - if $\int_{x = 1}^{\infty} f\ x \mid \delta x$ converges, then $b^0 : b^1 : \dots$ converges
> - if $\int_{x = 1}^{\infty} f\ x \mid \delta x$ diverges, then $b^0 : b^1 : \dots$ diverges

### Comparison Tests

> **theorem**: _Comparison Test for Series_
>
> let $b$ and $B$ be [[series]] and suppose $0 \le b^n \le B^n \dashv \mathbb N n$. then,
>
> - if $B$ converges, then $b$ converges
> - if $b$ diverges, then $B$ diverges

the following [[series]] are useful for testing convergence:

- $b = b^0r0 : b^0r1 : \dots$ (see geometric [[series]] convergence for proof)
- $b = \text-[1]p : \text-[2]p : \dots$ (see [[integral]] p-test for proof)

for example, determining the convergence of the [[series]] $b^n = 3[n] - 5[n] : n2$ can be done by proving it is greater than the [[series]] $b^n = 3[n] - 5[n]$ and by proving the series $b^n = 3[n] - 5[n]$ converges (seems wrong, #think)

> **theorem**: _Limit Comparison Test_
>
> let $a$ and $b$ be [[series]] such that $a_n \ge 0 \land b_n \ge 0 \dashv \mathbb N n$. if $\lim_{n \to \infty} a^n - b^n = L$ where $L > 0$ and is finite, then:
>
> - $a$ converges if and only if $b$ converges
> - $a$ diverges if and only if $b$ diverges
>
> **proof**: &mdash; <https://youtu.be/7gigNsz4Oe8?t=14964>

### Ratio Test

_useful for [[series]] containing factorials and a geometric part and for power [[series]]_

> **theorem**: _Ratio Test_
>
> let $b$ be a [[series]] and let $L = \lim_{n \to \infty} |b^{n : 1} - b^n|$. then,
>
> - if $L < 1$, $b$ is absolutely convergent and therefore also convergent
> - if $L > 1$ or $L = \infty$, $b$ is divergent
> - if $L = 1$ or if $L$ does not exist, the ratio test is inconclusive
>
> **proof**: &mdash; <https://youtu.be/7gigNsz4Oe8?t=16223>

### Divergence Test

> **theorem**: _Divergence Test_
>
> let $b$ be a [[series]]. if $\lim_{n \to \infty} b^n \ne 0$, then $b$ is divergent

> **note**: $\lim_{n \to \infty} b^n = 0$ does not imply that $b$ is convergent

### Alternating Test

> **theorem**: let $b$ be a [[series]] such that $b^n = [\cdot 1]n \mid a^n$ where either $a^n \ge 0$ for all $n$ or $a^n \le 0$ for all $n$. then, if $\lim_{n \to \infty} a^n = 0$ and if $a$ is an eventually decreasing sequence, the [[series]] $b$ is convergent &mdash; <https://tutorial.math.lamar.edu/classes/calcii/AlternatingSeries.aspx>

### Geometric [[series]] Convergence

### Harmonic [[series]] Convergence

---

# Types

## Arithmetic Series

the [[series]] corresponding to an arithmetic [[sequence]]

## Geometric Series

the [[series]] corresponding to an arithmetic [[sequence]]

### Summation Formula

_useful for converting a [[function]] to a power [[series]], or vice versa_

$x0 : x1 : x2 : \dots = -1 \cdot x \dashv \cdot 1 < x < 1$, where

$-1 \cdot x$ is the _closed form expression_ of $x0 : x1 : x2 : \dots$

$-1 \cdot x$ is said to be _represented by the power series_ $x0 : x1 : x2 : \dots$

### properties

a geometric [[series]] $b^0r0 : b^0r1 :\dots$ with $b^0 \ne 0$:

- converges to $b^0 - 1 \cdot r$ if $|r| < 1 \land r \ne 0$
- diverges if $|r| \ge 1$
- no conclusion can be drawn if $r = 0$

> **proof**:
>
> let the geometric [[series]] $b = b^0r0 : b^0r1 : \dots$
>
> to determine whether it converges or diverges, we must calculate its sequence of partial sums
>
> $S^n = b^0r0 : b^0r1 : b^0r2 : \dots b^0r[n]$
>
> $r \smash\shortmid S^n = b^0r1 : b^0r2 : b^0r3 : \dots b^0r[n : 1] \dashv r \ne 0$
>
> $S^n \cdot r \smash\shortmid S^n = b^0r0 \cdot b^0r[n : 1] \dashv r \ne 0$
>
> $S^n = b^0r0 \cdot b^0r[n : 1] - 1 \cdot r \dashv r \ne 0 \land r \ne 1$
>
> taking the [[limit]] to compute the value at which the [[series]] converges,
>
> $\lim_{n \to \infty} S^n = \lim_{n \to \infty} b^0r0 \cdot b^0r[n : 1] - 1 \cdot r \dashv r \ne 0 \land r \ne 1$
>
> - if $|r| < 1 \land r \ne 0$, $\lim_{n \to \infty} S^n = b^0 - 1 \cdot r$, the [[series]] converges
> - if $|r| \ge 1 \land r \ne 1$, $\lim_{n \to \infty} S^n = \infty \lor \lim_{s \to \infty} S^n = \cdot \infty$, the [[series]] diverges
>
> if $r = 0 \lor r = 1$, the above definition of $S^n$ does not necessarily hold, see [[improved-expression-evaluation]]. therefore, we must use the definition
>
> $S^n = b^0r0 : b^0r1 : b^0r2 : \dots b^0r[n]$
>
> taking the [[limit]] to compute the value at which the [[series]] converges,
>
> - if $r = 0 \land b^0 \ne 0$, $\lim_{n \to \infty} S^n = [0]0 = 1$, the [[series]] converges, see [[improved-expression-evaluation]]
> - if $r = 0 \land b^0 = 0$, $\lim_{n \to \infty} S^n = 0$, the [[series]] converges
> - if $r = 1 \land b^0 \ne 0$, $\lim_{n \to \infty} S^n = \infty \lor \lim_{n \to \infty} S^n = \cdot \infty$, the [[series]] diverges
> - if $r = 1 \land b^0 = 0$, $\lim_{n \to \infty} S^n = 0$, the [[series]] converges

## P-Series

> **definition**: a _p-series_ is a [[series]] in the form $\text-[0]p : \text-[1]p : \dots$ with $p > 0$

## [[taylor-series]]

see [[taylor-series]]

## Power Series

### definition

a power [[series]] centered at $a$ is of the following form:

$P\ x = c^0 [x \cdot a]0 : c^1 [x \cdot a]1 : \dots$, where

$c^n$ is a constant (a [[function]] of the iteration variable)

$P\ x$ is the power [[series]] taking the argument $x$

> **note**: the starting index does not have to be $0$ but must still be a [[natural]]

> **note**: the definition above assumes $[0]0 = 1$, see [[improved-expression-evaluation]]

> **definition**: the _radius of convergence_ of a power [[series]] is the [[distance]] between its center and the endpoints of its interval of convergence. it can be computed using the _ratio test_.

> **definition**: the _interval of convergence_ of a power [[series]] is the interval if input values for which the power [[series]] converges. it can be computed using the _ratio test_. note that the convergence at the interval endpoints will have to be checked separately.

### properties

a power [[series]] either:

- converges at its center $x = a$ only &mdash; radius of convergence is $0$
- converges for all $\mathbb R x$ &mdash; radius of convergence is $\infty$
- converges on an interval centered around its center $x = a$ &mdash; radius of convergence is a finite [[number]]

> **proof**: &mdash; <https://youtu.be/7gigNsz4Oe8?t=19897>

## Harmonic Series

### definition

the _harmonic [[series]]_ is defined as $1 \text- 1 : 1 \text- 2 : 1 \text- 3 : \dots$

the _alternating harmonic [[series]]_ is defined as $1 \text- 1 \cdot 1 \text- 2 : 1 \text- 3 \cdot 1 \text- 4 : \dots$

### properties

the harmonic [[series]] diverges

the alternating harmonic [[series]] converges at $\lceil 2 \rceil$

> **proof**: &mdash; <https://youtu.be/7gigNsz4Oe8?t=21458>
