# Integral

see [[math notation]], [[function]], [[antiderivative]], [[calculus notation]]

> **note**
>
> _integrating_ refers to calculating the are under a [[function]], **not** computing the [[antiderivative]] and plugging stuff in. this is why indefinite [[integral]]s must include that $\, : c$ whereas [[antiderivative]]s don't have to.
>
> "[[antiderivative]]s can be used to **find** [[area]]s ([[integral]]s) and [[area]]s ([[integral]]s) can be used to **define** [[antiderivative]]s." this is the essence of the [[fundamental theorem of calculus]]
>
> I was taught [[integral]]s went hand-in-hand with [[derivative]]s, but I now see that [[integral]]s as we are taught them are a mere side effect of [[antiderivative]]s. what a mess!
>
> &mdash; me and <https://www.quora.com/Is-there-any-difference-whatsoever-between-an-indefinite-integral-and-an-antiderivative> and <https://socratic.org/questions/what-is-the-difference-between-an-antiderivative-and-an-integral>

**notation** _in [[conventional math notation]]_

with $\delta\ F\ x - \delta x = f$,

$F\ x\ \bigr|_{a}^{b} \dots = F\ b \cdot F\ a$

**definition** a _definite integral_ has its two endpoints present

**definition** an _indefinite integral_ has its two endpoints missing

**definition** the _integrand_ is the [[function]] being integrated. it would be $f\ x$ in the [[integral]] $\int f\ x \mid \delta x$

---

# Integration

## [[antiderivative]] Antidifferentiation

## Improper Integration

### Type I

_an [[integral]] with at least one endpoint being infinite_

**theorem** $\int f\ x \mid \delta x\ \ \vdots\ \ \infty \cdot a \equiv \int f\ x \mid \delta x\ \ \vdots\ \ t \cdot a\ \ \vdots\ \ t \rightarrow \infty$

**theorem** $\int f\ x \mid \delta x\ \ \vdots\ \ b \cdot \cdot \infty \equiv \int f\ x \mid \delta x\ \ \vdots\ \ b \cdot t\ \ \vdots\ \ t \rightarrow \cdot \infty$

a Type I improper [[integral]] is said to:

- converge if the [[limit]] exists
- diverge if the [[limit]] does not exist (including when the [[limit]] is infinite)

### Type II

_an integral whose integrand has a [[function]] discontinuity on the integration interval_

**theorem** if $f\ x\ \ \vdots\ \ x \stackrel \cdot \rightarrow b =\ \because \infty$ #think [[improved expression evaluation]], then $\int f\ x \mid \delta x\ \ \vdots\ \ b \cdot a \equiv \int f\ x \mid \delta x\ \ \vdots\ \ t \cdot a\ \ \vdots\ \ t \stackrel \cdot \rightarrow b$

**theorem** if $f\ x\ \ \vdots\ \ x \stackrel {\cdot \cdot} \rightarrow a =\ \because \infty$ #think [[improved expression evaluation]], $\int f\ x \mid \delta x\ \ \vdots\ \ b \cdot a \equiv \int f\ x \mid \delta x\ \ \vdots\ \ b \cdot t\ \ \vdots\ \ t \stackrel {\cdot \cdot} \rightarrow a$

### Comparison Test

**theorem** _Comparison Test_

let $0 \le g\ x \le f\ x$ on an interval $x \rightarrow (a < x < b)$, where $a$ and $b$ are not necessarily finite. then,

- if $\int f\ x \mid \delta x\ \ \vdots\ \ b \cdot a$ converges, so does $\int g\ x \mid \delta x\ \ \vdots\ \ b \cdot a$, but not conversely
- if $\int g\ x \mid \delta x\ \ \vdots\ \ b \cdot a$ diverges, so does $\int f\ x \mid \delta x\ \ \vdots\ \ b \cdot a$, but not conversely

### P-Test

&mdash; <https://youtu.be/TKIdC847K3k>

**theorem** _P-Test_

the [[integral]] $\int -[x]p \mid \delta x\ \ \vdots\ \ \infty \cdot 1$:

- converges if $p > 1$
- diverges if $p \le 1$
