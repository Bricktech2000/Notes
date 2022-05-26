# Derivative

see [[math-notation]], [[classical-math-notation]], [[derivative-rules]]

## definition

[[classical-math-notation]]: $\frac{df}{dx} = f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$

my [[math-notation]]: $\delta f\ x - \delta x = \lim_{h \to 0} f (x \cdot h) \circ f\ x - h = \lim_{x \to a} f\ x \circ f\ a - x \circ a$

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

see [[calculus-notation]]

$\delta f\ x - \delta x$, $\delta (\delta f - \delta x) - \delta x$

## Differentiation

to differentiate a [[function]], apply [[derivative-rules]] recursively, see [[recursion]]

### differentiability

> a [[function]] $f$ is **differentiable** at $a$ if $\delta f\ a - \delta x$ exists

> a [[function]] is **differentiable** on an interval $a \le x \le b$ if it is differentiable on every point from $a$ to $b$

> **theorem**: if $f\ x$ is not continuous at $x = a$, then it is not differentiable at $x = a$

> **theorem**: if $f\ x$ is differentiable at $x = a$, then it is continuous at $x = a$

> **theorem**: if $f\ x$ is continuous at $x = a$, then it may or may not be differentiable at $x = a$

## Logarithmic Differentiation

_differentiating the [[logarithm]] of a [[function]] instead of the [[function]] itself_

_useful for computing the [[derivative]] of an [[exponent]]ial [[function]]_

### example with $[x][e]x$

$y = [x][e]x$

$\lceil y \rceil = \lceil [x][e]x \rceil = \lceil x \rceil ' [e]x$

$\delta\ \lceil y \rceil - \delta x = \delta\ [e]x ' \lceil x \rceil - \delta x$

$-y\ |\ \delta\ y - \delta x = ([e]x - x) \cdot \lceil x \rceil ' [e]x$

$\delta\ y - \delta x = [x][e]x\ |\ ([e]x - x) \cdot \lceil x \rceil ' [e]x$

the alternative would be the following, by transforming and using the chain rule, see [[derivative-rules]]

$y = [x][e]x$

$[x][e]x = [e] \lceil [x][e]x \rceil = [e](\lceil x \rceil ' [e]x)$

$\delta\ y - \delta x = \delta\ [e](\lceil x \rceil ' [e]x) - \delta x$

$\delta\ y - \delta x = [e](\lceil x \rceil ' [e]x)\ |\ \delta\ \lceil x \rceil ' [e]x - \delta x$

$\delta\ y - \delta x = [x][e]x\ |\ ([e]x - x) \cdot \lceil x \rceil ' [e]x$

### example with $[x]x$

$y = [x]x$

$\lceil y \rceil = x \lceil x \rceil$

$\delta\ \lceil y \rceil - \delta x = \delta\ x \lceil x \rceil - \delta x$

$-y\ |\ \delta y - \delta x = 1 \cdot \lceil x \rceil$

$\delta y - \delta x = y\ |\ 1 \cdot \lceil x \rceil = [x]x\ |\ 1 \cdot \lceil x \rceil$

## Implicit Differentiation

> Differentiation of an implicit equation (where the dependent variable is not isolated). Works with both [[function]]s and relations that aren't [[function]]s.

### example

$x2 \cdot y2 = 2$

$\delta\ (x2 \cdot y2) - \delta x = \delta 2 - \delta x$

$2x \cdot 2y(\delta y - \delta x) = 0$

$\delta y - \delta x = \circ x - y$

> **note**: as both $x$ and $y$ are present in the equation, the [[derivative]] at $\circ y$ will be different from the one at $\cdot y$

## Partial Differentiation

[[todo]]

### example

[[todo]]

<https://en.wikipedia.org/wiki/Partial_derivative>
