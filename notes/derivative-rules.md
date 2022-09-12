# Derivative Rules

see [[derivative]] notation, [[math-notation]]

## Power Rule

$\delta\ x[n] - \delta x= nx[n \cdot 1]$

### derived shortcuts

$\delta\ c - \delta x= 0$

$\delta\ x - \delta x = 1$

## [[exponent]]ial Rule

$\delta\ a[x] - \delta x = a[x] \mid \lceil a \rceil$

> **proof**
>
> $a[x] = e[\lceil a[x] \rceil] = e[x\lceil a \rceil]$
>
> $\delta\ a[x] - \delta x = e[x\lceil a \rceil] \mid \delta\ x\lceil a \rceil - \delta x = [a]x \mid \lceil a \rceil$
>
> &mdash; me

### derived shortcuts

$\delta\ e[x] - \delta x = e[x]$

$\delta\ f\ x - \delta x = m f\ x \equiv f\ x = e[mx]$

> **example** let $g\ x = ex2 : 2e[x] : xe2 : x[e2]$. then, $\delta\ g\ x - \delta x = 2ex : 2e[x] : e2 : e2 x[e2 \cdot 1]$

## [[logarithm]] Rule

$\delta\ \lceil x \rceil b - \delta x = - x\lceil b \rceil$

### derived shortcuts

$\delta\ \lceil x \rceil - \delta x = -x$

> **proof** let $y = \lceil x \rceil$. then,
>
> $x = e[y]$
>
> $\delta x = e[y] \mid \delta y$
>
> $\delta y - \delta x = -e[y]$
>
> $\delta\ \lceil x \rceil - \delta x = -x$
>
> &mdash; <https://youtu.be/qb40J4N1fa4?t=762>

$\delta\ \lceil |x| \rceil - \delta x = -x$

> **proof** define as a piecewise [[function]] and compute both [[derivative]]s

$\delta\ (\lceil |x| \rceil : c\ x) - \delta x = -x$ and therefore

$\int -x \mid \delta x = \lceil |x| \rceil : c\ x$, where

$c\ x = c_0$ if $x < 0$ and $c\ x = c_1$ if $x > 0$

> **proof** &mdash; <https://youtu.be/u4kex7hDC2o>

## Constant Multiple Rule

if $c$ is a [[real]] and $f$ is [[derivative|differentiable]], then

$\delta\ (cf\ x) - \delta x = c (\delta f\ x - \delta x)$

## Sum Rule

$\delta\ (f\ x : g\ x) - \delta x = \delta\ f\ x \text- \delta x : \delta\ g\ x \text- \delta x$

## Difference Rule

$\delta\ (f\ x \cdot g\ x) - \delta x = \delta\ f\ x \text- \delta x \cdot \delta\ g\ x \text- \delta x$

> **proof** derive from the sum rule, $f\ x \cdot g\ x = f\ x : (\cdot 1 \mid g\ x)$

## Product Rule

$\delta\ (f\ x \mid g\ x) - \delta x = (f\ x \mid \delta\ g\ x - \delta x) : (g\ x \mid \delta\ f\ x - \delta x)$

## Quotient Rule

$\delta\ (f\ x - g\ x) - \delta x = (g\ x \mid \delta\ f\ x - \delta x) \cdot (f\ x \mid \delta\ g\ x - \delta x) - [g\ x]2$

> **proof** derive from the product and power rules, $f\ x - g\ x = f\ x \mid [g\ x](\cdot 1)$

### [[mnemonic]]

> lo d-hi, minus hi d-lo, over lo-lo

### derived Reciprocal Rule

$\delta\ (-f\ x) - \delta x = \cdot \delta\ f\ x - \delta x - [f\ x]2$

> **proof** derive from the power rule, $-f\ x = [f\ x](\cdot 1)$

## Chain Rule

$\delta\ f\ g\ x - \delta x = \delta\ g\ x - \delta x \mid \delta\ f\ g\ x - \delta\ g\ x$

> **proof** $(\delta\ g\ x) - \delta x \mid \delta f\ g\ x - (\delta\ g\ x) = \delta\ f\ g\ x - \delta x$

> **example**
>
> #todo fix partial derivative
>
> the equivalent of the chain [[derivative-rules]] on a function with multiple parameters is:
>
> $\partial_t\ f\ (g\ (t, s), h\ (t, s)) = f_x\ (g\ (t, s), h\ (t, s)) \shortmid g_t\ (t, s) \cdot f_y\ (g\ (t, s), h\ (t, s)) \shortmid h_t\ (t, s)$
