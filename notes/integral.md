# Integral

see [[math-notation]], [[function]], [[antiderivative]], [[calculus-notation]]

> **note**:
>
> _integrating_ refers to calculating the are under a [[function]], **not** computing the [[antiderivative]] and plugging stuff in. this is why indefinite [[integral]]s must include that $\cdot c$ whereas [[antiderivative]]s don't have to.
>
> "[[antiderivative]]s can be used to **find** areas ([[integral]]s) and areas ([[integral]]s) can be used to **define** [[antiderivative]]s." this is the essence of the [[fundamental-theorem-of-calculus]]
>
> I was taught [[integral]]s went hand-in-hand with [[derivative]]s, but I now see that [[integral]]s as we are taught them are a mere side effect of [[antiderivative]]s. what a mess!
>
> &mdash; me and <https://www.quora.com/Is-there-any-difference-whatsoever-between-an-indefinite-integral-and-an-antiderivative> and <https://socratic.org/questions/what-is-the-difference-between-an-antiderivative-and-an-integral>

## notation

see [[calculus-notation]]

in [[classical-math-notation]], with $\delta\ F\ x - \delta x = f$,

$F\ x\ \bigr|_{a}^{b} \dots = F\ b \circ F\ a$

## definitions

> **definition**: a _definite [[integral]]_ has its two endpoints present

> **definition**: an _indefinite [[integral]]_ has its two endpoints missing

> **definition**: the _integrand_ is the [[function]] being integrated. it would be $f\ x$ in the [[integral]] $\int f\ x \mid \delta x$

# Integration

## [[antiderivative]] Antidifferentiation

## Improper Integration

### Type I

an [[integral]] with at least one endpoint being infinite

$\int_{x = a}^{x = \infty} f\ x \mid \delta x = \lim_{t \to \infty} \int_{x = a}^{x = t} f\ x \mid \delta x$

$\int_{x = \infty}^{x = b} f\ x \mid \delta x = \lim_{t \to \infty} \int_{x = t}^{x = b} f\ x \mid \delta x$

a Type I improper [[integral]] is said to:

- converge if the [[limit]] exists
- diverge if the [[limit]] does not exist (including when the [[limit]] is infinite)

### Type II

an integral whose integrand has a [[function]] discontinuity on the integration interval

if $\lim_{x \to b^-} f\ x = \dot \circ \infty$ [[think]] [[improved-expression-evaluation]], $\int_{x = a}^{x = b} f\ x \mid \delta x = \lim_{t \to b^-} \int_{x = a}^{x = t} f\ x \mid \delta x$

if $\lim_{x \to a^+} f\ x = \dot \circ \infty$ [[think]] [[improved-expression-evaluation]], $\int_{x = a}^{x = b} f\ x \mid \delta x = \lim_{t \to a^+} \int_{x = t}^{x = b} f\ x \mid \delta x$

### Comparison Test

> **theorem**: let $0 \le g\ x \le f\ x$ on an interval $a < x < b$, where $a$ and $b$ are not necessarily finite. then,
>
> - if $\int_{x = a}^{x = b} f\ x \mid \delta x$ converges, so does $\int_{x = a}^{x = b} g\ x \mid \delta x$, but not conversely
> - if $\int_{x = a}^{x = b} g\ x \mid \delta x$ diverges, so does $\int_{x = a}^{x = b} f\ x \mid \delta x$, but not conversely
