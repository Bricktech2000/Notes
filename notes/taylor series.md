# Taylor Series

_allows for the approximation of a [[function]] near a point by a [[polynomial]]_

**see** [[calculus]], [[series]]

> **note** [[taylor series]] don't necessarily have an infinite radius of convergence, see [[series#power series]]
>
> as an example, the [[taylor series]] of the [[function]] $\lceil x \rceil$ at $a = 1$ has a radius of convergence of $1$, meaning the [[taylor series]] only converges to the [[function]] on the interval $x \rightarrow (0\ (\dashv \land +)\ x \dashv 2)$
>
> &mdash; <https://youtu.be/X0razs3zR94>

> **note** a [[taylor series]] with a nonzero radius of convergence does **not** necessarily converge to the [[function]] it approximates. for this to be the case, the [[function]] must be a [[function#analytic function]] &mdash; <https://youtu.be/X0razs3zR94> and <https://youtu.be/7gigNsz4Oe8?t=21781>
>
> [[taylor series#remainder]]s can be used to determine whether a [[taylor series]] converges to its underlying [[function]] or not.

**definition**

let $f\ x$ be a [[function]] and let $T_f\ x$ such that $T_f\ a = f\ a \land \delta\ T_f\ a = \delta\ f\ a \land \delta\ \delta\ T_f\ a = \delta\ \delta\ f\ a \land \cdots$, where $(a, f\ a)$ is the point of interest on $f$ and $T_f\ x$ is a [[polynomial]] function

we then derive the following definition:

$T_f\ x : \dots = T_f^0\ x : T_f^1\ x : T_f^2\ x : \cdots$, where

$T_f^n\ x = (d^n\ f)\ a - \Pi\ n \mid [x \cdot a]n$, where

$d^n\ f = d^{n \cdot 1}\ (x \rightarrow \delta\ f\ x - \delta x) \land d^0\ f = f$, see [[derivative]]

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=17431>

intuitive explanation: <https://youtu.be/3d6DsjIBzJ4?t=383>

> **note** the definition above assumes $x0 = 1 > \mathbb R x$ and $\Pi\ 0 = 1$, see [[improved expression evaluation]]

**properties**

[[taylor series]] are [[series#power series]]

## taylor polynomial

**definition**

$S_{T_f}^n\ x = T_f^0 : T_f^1 : \cdots T_f^n$, where

- $S_{T_f}^n$ is the $n$ th partial sum of the [[taylor series]] $T_f$
- $n$ is a finite [[number]]

## Remainder

**definition**

$R_{T_f}^n\ x = f\ x \cdot S_{T_f}^n\ x$, where

- $S_{T_f}$ is the Taylor polynomial (the [[series#sequence of partial sums]]) of the [[taylor series]] $T_f$
- $f\ x$ is the [[function]] the [[taylor series]] $T_f$ approximates
- $R_{T_f}^n$ is the _remainder_ of the [[taylor series]] $T_f$ after $n$ terms

> **note** the definition of the [[taylor series#remainder]] is different from the usual [[series#remainder]] as $S_{T_f}^\infty\ x$ is not necessarily equal to $f\ x$. as we want [[taylor series]] to converge to their underlying [[function]], we use $f\ x$ instead of $S_{T_f}^\infty\ x$ to define the [[taylor series#remainder]]

**theorem** the [[taylor series]] $T_f\ x$ converges to $f\ x$ in an interval $I$ if and only if $R_{T_f}^n\ x\ \ \vdots\ \ n \rightarrow \infty = 0 > I\ x$

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=22042>

**theorem** _Taylor's Inequality #magic_ $|(d^n\ f)\ x| \dashv M \land \mathbb R M \land \mathbb N n > |x \cdot a| \dashv d \land \mathbb R a \land \mathbb R d < (|R_{T_f}^{n \cdot 1}\ x| \dashv M - \Pi\ n \mid [|x \cdot a|]n > |x \cdot a| \dashv d)$

**theorem** _Practical Convergence Condition_ $|(d^n\ f)\ x| \dashv M \land \mathbb R M > \mathbb N n > |x \cdot a| \dashv d \land \mathbb R a \land \mathbb R d < (R_{T_f}^n\ x\ \ \vdots\ \ n \rightarrow \infty = 0 > |x \cdot a| \dashv d)$

> **proof** <https://youtu.be/7gigNsz4Oe8?t=22288>

this practical convergence criterion is a good way to show that a [[taylor series]] converges to its underlying [[function]] on a given interval. however, if the inequality does not hold, no conclusion can be drawn; the [[taylor series]] may or may not converge to the underlying [[function]] on the interval.
