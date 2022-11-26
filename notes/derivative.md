# Derivative

**see** [[math notation]], [[derivative rules]], [[function]], [[calculus notation]]

**definition** _in [[conventional math notation]]_

$\frac{df}{dx} = f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$

**definition** _in my [[math notation]]_

$\delta\ f\ x - \delta x = f\ (x : h) \cdot f\ x - h\ \ \vdots\ \ h \rightarrow 0 = f\ x \cdot f\ a - x \cdot a\ \ \vdots\ \ x \rightarrow a$

**definition** _with a multivariable [[function]] in my [[math notation]]_

let $p = (x \cdots)$

$\delta\ f\ p - \delta p = (\delta\ f\ p - \delta p^0, \delta\ f\ p - \delta p^1, \cdots)$

**notations**

_[[conventional math notation]] Lagrange's notation_

$f'(x)$, $f''(x)$, $f'''(x)$

$f^{(n)}(x)$

_[[conventional math notation]] Leibniz's Notation_

$\frac{d}{dx}f(x) = \frac{df}{dx}$

$\frac{d^n}{dx^n} = \frac{d^nf}{dx^n}$

_in my [[math notation]]_

$\delta\ f\ x - \delta x$, see [[calculus notation]]

$d^n\ f = d^{n \cdot 1}\ (x \rightarrow \delta\ f\ x - \delta x) \land d^0\ f = f$

$d^n f$ would then be the $n$ th [[derivative]] of $f\ x$ with respect to $x$

## Directional Derivative

**see** [[gradient]]

**definition**

let $f$ be a [[function]] differentiable at $p \equiv (x \cdots)$ and let $v$ be a **[[vector in rn#unit vector]]**. then,

$D^v\ f\ p =\ :\! v (\delta\ f\ p - \delta p)$, where

- $D^v\ f\ p$ is the [[derivative]] of $f$ in direction $v$ at $p$
- $\delta\ f\ p - \delta p$ is the [[gradient]] of $f$ at $p$
- $v$ is the direction [[vector in rn]], see [[dot product]]

> **examples**
>
> $D^{(1, 0)}\ f\ (x, y) = \delta f\ (x, y) - \delta x$
>
> $D^{(0, 1)}\ f\ (x, y) = \delta f\ (x, y) - \delta y$

## Partial Derivative

> **note** partial differentiation is not a thing. unless I'm missing something major, all it means is:
>
> > differentiate this [[function]] with respect to this [[variable]], and please blindly assume the derivative of the [[variable]] with respect to any other parameter is $0$
>
> partial differentiation is equivalent to a [[derivative#directional derivative]] with direction $(0 \cdots 0, 1, 0 \cdots 0)$
>
> &mdash; <https://www.reddit.com/r/mathematics/comments/oxj88q/why_are_partial_derivatives_a_separate_thing_than/>

**notation**

_in [[conventional math notation]]_

in [[conventional math notation]], use the following abomination:

$f_x = f'_x = \partial_x f = D_x f = D_1 f = \frac{\partial}{\partial x}f = \frac{\partial f}{\partial x}$

$\frac{\partial^2 f}{\partial x^2} = f^n_{x x} = \partial_{x x} f = \partial^2_x f$ &mdash; Wikipedia

_in my [[math notation]]_

in my [[math notation]], it's just a [[derivative]]:

$\delta\ f\ x\ y - \delta x$, see [[calculus notation]]

**definition**

the _partial derivative_ of $f\ (x, y)$ with respect to $x$ is defined as follows:

$f\ (x : h, y) \cdot f\ (x, y) - h\ \ \vdots\ \ h \rightarrow 0$

the same is true with any other parameter and with any number of parameters

---

# Differentiation

> **procedure** _computing a [[derivative]]_
>
> to differentiate a [[function]], apply [[derivative rules]] recursively, see [[recursion]]

## differentiability

**definition** a [[function]] $f$ is _differentiable_ at $a$ if $\delta f\ a - \delta x$ exists

**definition** a [[function]] is _differentiable_ on an interval $x \rightarrow (a \le x \le b)$ if it is differentiable on every point from $a$ to $b$

**theorem** if $f\ x$ is not continuous at $x = a$, then it is not differentiable at $x = a$

**theorem** if $f\ x$ is differentiable at $x = a$, then it is continuous at $x = a$

**theorem** if $f\ x$ is continuous at $x = a$, then it may or may not be differentiable at $x = a$

## Logarithmic Differentiation

_differentiating the [[logarithm]] of a [[function]] instead of the [[function]] itself_

**application**

useful for computing the [[derivative]] of an [[exponent]]ial [[function]]

**examples**

> **example** _logarithmic differentiation of $x[e[x]]$._
>
> $y = x[e[x]]$
>
> $\lceil y \rceil = \lceil x[e[x]] \rceil = \lceil x \rceil e[x]$
>
> $\delta\ \lceil y \rceil - \delta x = \delta\ \lceil x \rceil e[x] - \delta x$
>
> $-y \mid \delta\ y - \delta x = e[x] \text- x : \lceil x \rceil e[x]$
>
> $\delta\ y - \delta x = x[e[x]] \mid e[x] \text- x : \lceil x \rceil e[x]$
>
> the alternative would be the following, by transforming and using the chain [[derivative rules]]:
>
> $y = x[e[x]]$
>
> $x[e[x]] = e[\lceil x[e[x]] \rceil] = e[\lceil x \rceil e[x]]$
>
> $\delta\ y - \delta x = \delta\ e[\lceil x \rceil e[x]] - \delta x$
>
> $\delta\ y - \delta x = e[\lceil x \rceil e[x]] \mid \delta\ \lceil x \rceil e[x] - \delta x$
>
> $\delta\ y - \delta x = x[e[x]] \mid e[x] \text- x : \lceil x \rceil e[x]$

> **example** _logarithmic differentiation of $[x]x$._
>
> $y = [x]x$
>
> $\lceil y \rceil = x \lceil x \rceil$
>
> $\delta\ \lceil y \rceil - \delta x = \delta\ x \lceil x \rceil - \delta x$
>
> $-y \mid \delta y - \delta x = 1 : \lceil x \rceil$
>
> $\delta y - \delta x = y \mid 1 : \lceil x \rceil = [x]x \mid 1 : \lceil x \rceil$

## Implicit Differentiation

differentiation of an implicit equation (where the dependent [[variable]] is not isolated). works with both [[function]]s and [[relation]]s that aren't [[function]]s.

> **example**
>
> $x2 : y2 = 2$
>
> $\delta\ (x2 : y2) - \delta x = \delta 2 - \delta x$
>
> $2x : 2y(\delta y - \delta x) = 0$
>
> $\delta y - \delta x = \cdot x - y$
>
> or alternatively,
>
> $x2 : y2 = 2$
>
> $\delta x2 : \delta y2 = \delta 2$
>
> $2x \delta x : 2y \delta y = 0$
>
> $\delta y - \delta x = \cdot x - y$
>
> > **note** as both $x$ and $y$ are present in the equation, the [[derivative]] at $\cdot y$ will be different from the one at $y$
