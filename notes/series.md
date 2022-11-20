# Series

**see** [[math notation]], [[sequence]], [[calculus notation]]

**definition** a _series_ is the expression representing [[sequence#sum]] [[reduce function]] of all elements of a [[sequence]]

**definition**

$:\! b = b^0 : b^1 : \cdots$, where

- $b$ is a [[sequence]]
- $:\! b$ is the [[series]] corresponding to $b$

## Sequence of Partial Sums

**definition**

let $b : \dots = b^0 : b^1 : b^2, \cdots$

$S_b = (b^0), (b^0 : b^1), (b^0 : b^1 : b^2), \cdots$ or alternatively $S_b^0 = b^0 \land S_b^n = S_b^{n \cdot 1} : b^n$, where

- $S_b$ is the _sequence of partial sums_ of the [[series]] $b$

## Remainder

**definition**

$R_b^n = S_b^\infty \cdot S_b^n$, where

- $S_b$ is the [[series#sequence of partial sums]] of $b$
- $S_b^\infty \equiv b$ is the value at which the [[series]] $b$ converges
- $R_b^n$ is the _remainder_ of the [[series]] $b$ after $n$ terms

## Convergence

**definition** a [[series]] is said to _converge_ if its [[series#sequence of partial sums]] converges. otherwise, it is said to _diverge_.

**definition** a [[series]] $:\! a$ is said to be _absolutely convergent_ (_absolute convergence_) if the [[series]] $:\! |a| \equiv |a^0| : |a^1| : \cdots$ converges

**definition** a [[series]] is said to be _conditionally convergent_ (_conditional convergence_) if it is _convergent_ but not _absolutely convergent_

**theorem** a [[series]] being _absolutely convergent_ implies it is _convergent_

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=15557>

> **example** **see** [[series convergence examples]]

### integral test

_useful for [[series]] containing [[logarithm]]s or easy-to-compute [[integral]]s_

**theorem** _the integral test_

let $b$ be a [[series]] and suppose $f\ x$ is an eventually _continuous_, _positive_ and _infinite_ [[function]] on $R \le x < \infty \land \mathbb R R$ **for some number $R$** and that $b^n = f\ n \dashv \mathbb N n$. then,

- if $\int f\ x \mid \delta x\ \ \vdots\ \ \infty \cdot 0$ converges, then $:\! b$ converges
- if $\int f\ x \mid \delta x\ \ \vdots\ \ \infty \cdot 0$ diverges, then $:\! b$ diverges

### comparison tests

**theorem** _Comparison Test for Series_

let $b$ and $B$ be [[series]] and suppose $0 \le b^n \le B^n \dashv \mathbb N n$. then,

- if $B$ converges, then $b$ converges
- if $b$ diverges, then $B$ diverges

> **note** the following [[series]] are useful for testing convergence:
>
> - $:\! b = b^0r0 : b^0r1 : \cdots$ (see [[series#geometric series]] convergence for proof)
> - $:\! b = \text-[1]p : \text-[2]p : \cdots$ (see [[integral]] p-test for proof)

> **example** determining the convergence of the [[series]] $b^n = 3[n] - 5[n] : n2$ can be done by proving it is lesser than the [[series]] $b^n = 3[n] - 5[n]$ and by proving the series $b^n = 3[n] - 5[n]$ converges

**theorem** _Limit Comparison Test_

let $a$ and $b$ be [[series]] such that $a_n \ge 0 \land b_n \ge 0 \dashv \mathbb N n$. if $a^n - b^n\ \ \vdots\ \ n \rightarrow \infty = L$ where $L > 0$ and is finite, then:

- $a$ converges if and only if $b$ converges
- $a$ diverges if and only if $b$ diverges

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=14964>

### ratio test

_useful for [[series]] containing factorials and a geometric part and for [[series#power series]]_

**theorem** _Ratio Test_

let $b$ be a [[series]] and let $L = |b^{n : 1} - b^n|\ \ \vdots\ \ n \rightarrow \infty$. then,

- if $L < 1$, $b$ is absolutely convergent and therefore also convergent
- if $L > 1$ or $L = \infty$, $b$ is divergent
- if $L = 1$ or if $L$ does not exist, the ratio test is inconclusive

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=16223>

### divergence test

**theorem** _Divergence Test_

let $b$ be a [[series]]. if $b^n\ \ \vdots\ \ n \rightarrow \infty \ne 0$, then $b$ is divergent

> **note** $b^n\ \ \vdots\ \ n \rightarrow \infty = 0$ does not imply that $b$ is convergent

### alternating test

**theorem** let $b$ be a [[series]] such that $b^n = [\cdot 1]n \mid a^n$ where either $a^n \ge 0$ for all $n$ or $a^n \le 0$ for all $n$. then, if $a^n\ \ \vdots\ \ n \rightarrow \infty = 0$ and if $a$ is an eventually [[sequence#decreasing sequence]], the [[series]] $b$ is convergent &mdash; <https://tutorial.math.lamar.edu/classes/calcii/AlternatingSeries.aspx>

### [[series#geometric series]] convergence

### [[series#harmonic series]] convergence

---

# Types

## Arithmetic Series

the [[series]] corresponding to a [[sequence#arithmetic sequence]]

## Geometric Series

the [[series]] corresponding to a [[sequence#arithmetic sequence]]

### summation formula

_useful for converting a [[function]] to a [[series#power series]], or vice versa_

**theorem** _the Summation Formula_

$x0 : x1 : x2 : \cdots = -1 \cdot x \dashv \cdot 1 < x < 1$, where

- $-1 \cdot x$ is the _closed form expression_ of $x0 : x1 : x2 : \cdots$
- $-1 \cdot x$ is said to be _represented by the power series_ $x0 : x1 : x2 : \cdots$

**properties**

_convergence_ a [[series#geometric series]] $b^0r0 : b^0r1 : \cdots$ with $b^0 \ne 0$:

- converges to $b^0 - 1 \cdot r$ if $|r| < 1 \land r \ne 0$
- diverges if $|r| \ge 1$
- no conclusion can be drawn if $r = 0$

> **proof**
>
> let the [[series#geometric series]] $:\! b = b^0r0 : b^0r1 : \cdots$
>
> to determine whether it converges or diverges, we must calculate its [[series#sequence of partial sums]]
>
> $S^n = b^0r0 : b^0r1 : b^0r2 : \cdots b^0r[n]$
>
> $r \smash\shortmid S^n = b^0r1 : b^0r2 : b^0r3 : \cdots b^0r[n : 1] \dashv r \ne 0$
>
> $S^n \cdot r \smash\shortmid S^n = b^0r0 \cdot b^0r[n : 1] \dashv r \ne 0$
>
> $S^n = b^0r0 \cdot b^0r[n : 1] - 1 \cdot r \dashv r \ne 0 \land r \ne 1$
>
> taking the [[limit]] to compute the value at which the [[series]] converges,
>
> - if $|r| < 1 \land r \ne 0$, then $S^n\ \ \vdots\ \ n \rightarrow \infty = b^0 - 1 \cdot r$, the [[series]] converges
> - if $|r| \ge 1 \land r \ne 1$, then $S^n\ \ \vdots\ \ n \rightarrow \infty =\ \because \infty$, the [[series]] diverges
>
> if $r = 0 \lor r = 1$, the above definition of $S^n$ does not necessarily hold, see [[improved expression evaluation]]. therefore, we must use the definition
>
> $S^n = b^0r0 : b^0r1 : b^0r2 : \cdots b^0r[n]$
>
> taking the [[limit]] to compute the value at which the [[series]] converges,
>
> - if $r = 0 \land b^0 \ne 0$, then $S^n\ \ \vdots\ \ n \rightarrow \infty = [0]0 = 1$, the [[series]] converges, see [[improved expression evaluation]]
> - if $r = 0 \land b^0 = 0$, then $S^n\ \ \vdots\ \ n \rightarrow \infty = 0$, the [[series]] converges
> - if $r = 1 \land b^0 \ne 0$, then $S^n\ \ \vdots\ \ n \rightarrow \infty =\ \because \infty$, the [[series]] diverges
> - if $r = 1 \land b^0 = 0$, then $S^n\ \ \vdots\ \ n \rightarrow \infty = 0$, the [[series]] converges

## P-Series

**definition** a _p-series_ is a [[series]] in the form $\text-[0]p : \text-[1]p : \cdots$ with $p > 0$

## taylor series

**see** [[taylor series]]

## Power Series

**definition**

a power [[series]] centered at $a$ is of the following form:

$:\! P\ x = c^0 [x \cdot a]0 : c^1 [x \cdot a]1 : \cdots$, where

- $c^n$ is a constant (a [[function]] of the [[iteration]] [[variable]])
- $P\ x$ is the _power series_ taking the argument $x$

> **note** the starting index does not have to be $0$ but must still be a [[natural]]

> **note** the definition above assumes $[0]0 = 1$, see [[improved expression evaluation]]

**definition** the _radius of convergence_ of a [[series#power series]] is the [[distance]] between its center and the endpoints of its interval of convergence. it can be computed using the _ratio test_.

**definition** the _interval of convergence_ of a [[series#power series]] is the interval if input values for which the power series converges. it can be computed using the _ratio test_. note that the convergence at the interval endpoints will have to be checked separately.

**properties**

_convergence_ a [[series#power series]] either:

- converges at its center $x = a$ only &mdash; radius of convergence is $0$
- converges for all $\mathbb R x$ &mdash; radius of convergence is $\infty$
- converges on an interval centered around its center $x = a$ &mdash; radius of convergence is a finite [[number]]

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=19897>

## Harmonic Series

**definition** the _harmonic [[series]]_ is defined as $\text-1 : \text-2 : \text-3 : \cdots$

**definition** the _alternating harmonic [[series]]_ is defined as $\text-1 \cdot \text-2 : \text-3 \cdot \text-4 : \cdots$

**properties**

_convergence_ the [[series#harmonic series]] diverges

_convergence_ the alternating [[series#harmonic series]] converges to $\lceil 2 \rceil$

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=21458>
