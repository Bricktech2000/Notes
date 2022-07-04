# Derivative

see [[math-notation]], [[derivative-rules]], [[function]], [[calculus-notation]]

## notations

### Lagrange's notation

see [[classical-math-notation]]

$f'(x)$, $f''(x)$, $f'''(x)$

$f^{(n)}(x)$

### Leibniz's Notation

see [[classical-math-notation]]

$\frac{d}{dx}f(x) = \frac{df}{dx}$

$\frac{d^n}{dx^n} = \frac{d^nf}{dx^n}$

### in my [[math-notation]]

$\delta\ f\ x - \delta x$, see [[calculus-notation]]

$d^n f = d^{n \cdot 1} (\delta\ f\ x - \delta x) \land d^0 f = f$

$d^n f$ would then be the $n$ th [[derivative]] of $f x$ with respect to $x$

## definition

[[classical-math-notation]]: $\frac{df}{dx} = f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$

my [[math-notation]]: $\delta\ f\ x - \delta x = \lim_{h \to 0} f\ (x : h) \cdot f\ x - h = \lim_{x \to a} f\ x \cdot f\ a - x \cdot a$

## directional [[derivative]]

see [[gradient]]

let $f$ be a [[function]] differentiable at $(x, y)$. then,

$D\ x\ y = \nabla f\ x\ y\ \dot\mid\ v - |v|$, where

$D\ x\ y$ is the [[derivative]] of $f$ in direction $v$

$\nabla f\ x\ y$ is the [[gradient]] of $f$ at $(x, y)$

$v$ is the direction [[vector-in-rn]]

---

# Differentiation

to differentiate a [[function]], apply [[derivative-rules]] recursively, see [[recursion]]

## differentiability

> **definition**: a [[function]] $f$ is _differentiable_ at $a$ if $\delta f\ a - \delta x$ exists

> **definition**: a [[function]] is _differentiable_ on an interval $a \le x \le b$ if it is differentiable on every point from $a$ to $b$

> **theorem**: if $f\ x$ is not continuous at $x = a$, then it is not differentiable at $x = a$

> **theorem**: if $f\ x$ is differentiable at $x = a$, then it is continuous at $x = a$

> **theorem**: if $f\ x$ is continuous at $x = a$, then it may or may not be differentiable at $x = a$

## Logarithmic Differentiation

_differentiating the [[logarithm]] of a [[function]] instead of the [[function]] itself_

_useful for computing the [[derivative]] of an [[exponent]]ial [[function]]_

### example with $x[e[x]]$

$y = x[e[x]]$

$\lceil y \rceil = \lceil x[e[x]] \rceil = \lceil x \rceil e[x]$

$\delta\ \lceil y \rceil - \delta x = \delta\ \lceil x \rceil e[x] - \delta x$

$-y \mid \delta\ y - \delta x = e[x] \text- x : \lceil x \rceil e[x]$

$\delta\ y - \delta x = x[e[x]] \mid e[x] \text- x : \lceil x \rceil e[x]$

the alternative would be the following, by transforming and using the chain rule, see [[derivative-rules]]

$y = x[e[x]]$

$x[e[x]] = e[\lceil x[e[x]] \rceil] = e[\lceil x \rceil e[x]]$

$\delta\ y - \delta x = \delta\ e[\lceil x \rceil e[x]] - \delta x$

$\delta\ y - \delta x = e[\lceil x \rceil e[x]] \mid \delta\ \lceil x \rceil e[x] - \delta x$

$\delta\ y - \delta x = x[e[x]] \mid e[x] \text- x : \lceil x \rceil e[x]$

#### example with $[x]x$

$y = [x]x$

$\lceil y \rceil = x \lceil x \rceil$

$\delta\ \lceil y \rceil - \delta x = \delta\ x \lceil x \rceil - \delta x$

$-y \mid \delta y - \delta x = 1 : \lceil x \rceil$

$\delta y - \delta x = y \mid 1 : \lceil x \rceil = [x]x \mid 1 : \lceil x \rceil$

## Implicit Differentiation

> Differentiation of an implicit equation (where the dependent variable is not isolated). Works with both [[function]]s and relations that aren't [[function]]s.

### example

$x2 : y2 = 2$

$\delta\ (x2 : y2) - \delta x = \delta 2 - \delta x$

$2x : 2y(\delta y - \delta x) = 0$

$\delta y - \delta x = \cdot x - y$

or alternatively,

$x2 : y2 = 2$

$\delta x2 : \delta y2 = \delta 2$

$2x \delta x : 2y \delta y = 0$

$\delta y - \delta x = \cdot x - y$

> **note**: as both $x$ and $y$ are present in the equation, the [[derivative]] at $\cdot y$ will be different from the one at $y$

## Partial Differentiation

#todo

### example

#todo

<https://en.wikipedia.org/wiki/Partial_derivative>
