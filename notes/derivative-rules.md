# Derivative Rules

see [[derivative]] notation, [[math-notation]]

## Power Rule

$\delta\ x[n] - \delta x= nx[n \cdot 1]$

### derived shortcuts

$\delta\ c - \delta x= 0$

$\delta\ x - \delta x = 1$

## [[exponent]]ial Rule

$\delta\ a[x] - \delta x = a[x] \mid \lceil a \rceil$

> **proof**:
>
> $a[x] = e[\lceil a[x] \rceil] = e[x\lceil a \rceil]$
>
> $\delta\ a[x] - \delta x = e[x\lceil a \rceil] \mid \delta\ x\lceil a \rceil - \delta x = [a]x \mid \lceil a \rceil$
>
> &mdash; me

### derived shortcuts

$\delta\ e[x] - \delta x = e[x]$

$\delta\ f\ x - \delta x = m f\ x \equiv f\ x = e[mx]$

## [[logarithm]] Rule

$\delta\ \lceil x \rceil b - \delta x = - x\lceil b \rceil$

### derived shortcuts

$\delta\ \lceil x \rceil - \delta x = -x$

> **proof**: let $y = \lceil x \rceil$. then,
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

> **proof**: define as a piecewise [[function]] and compute both [[derivative]]s

$\delta\ (\lceil |x| \rceil : c\ x) - \delta x = -x$ and therefore

$\int -x \mid \delta x = \lceil |x| \rceil : c\ x$, where

$c\ x = c_0$ if $x < 0$ and $c\ x = c_1$ if $x > 0$

> **proof**: &mdash; <https://youtu.be/u4kex7hDC2o>

## Constant Multiple Rule

if $c$ is a [[real]] and $f$ is [[derivative|differentiable]], then

$\delta\ (cf\ x) - \delta x = c (\delta f\ x - \delta x)$

## Sum Rule

$\delta\ (f\ x : g\ x) - \delta x = \delta\ f\ x \text- \delta x : \delta\ g\ x \text- \delta x$

## Difference Rule

$\delta\ (f\ x \cdot g\ x) - \delta x = \delta\ f\ x \text- \delta x \cdot \delta\ g\ x \text- \delta x$

> **proof**: derive from the sum rule, $f\ x \cdot g\ x = f\ x : (\cdot 1 \mid g\ x)$

## Product Rule

$\delta\ (f\ x \mid g\ x) - \delta x = (f\ x \mid \delta\ g\ x - \delta x) : (g\ x \mid \delta\ f\ x - \delta x)$

## Quotient Rule

$\delta\ (f\ x - g\ x) - \delta x = (g\ x \mid \delta\ f\ x - \delta x) \cdot (f\ x \mid \delta\ g\ x - \delta x) - [g\ x]2$

> **proof**: derive from the product and power rules, $f\ x - g\ x = f\ x \mid [g\ x](\cdot 1)$

### [[mnemonic]]

> lo d-hi, minus hi d-lo, over lo-lo

### derived Reciprocal Rule

$\delta\ (-f\ x) - \delta x = \cdot \delta\ f\ x - \delta x - [f\ x]2$

> **proof**: derive from the power rule, $-f\ x = [f\ x](\cdot 1)$

## Chain Rule

$\delta\ f\ g\ x - \delta x = \delta\ g\ x - \delta x \mid \delta f\ g\ x - \delta\ g\ x$

> **proof**: $(\delta\ g\ x) - \delta x \mid \delta f\ g\ x - (\delta\ g\ x) = \delta\ f\ g\ x - \delta x$

## Derivatives of Trig Functions

see [[trigonometric-function]]s

$\delta\ \sin x - \delta x = \cos x$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21115>

$\delta\ \cos x - \delta x = \cdot \sin x$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21193>

$\delta\ \tan x - \delta x = [\text-\cos x]2$

$\delta\ \text-\sin x - \delta x = \cdot \mid \text-\sin x \mid \text-\tan x$

$\delta\ \text-\cos x - \delta x = \text-\cos\ x \mid \tan x$

$\delta\ \text-\tan x - \delta x = \cdot [\text-\sin x]2$

$\delta\ \operatorname{asin} x - \delta x = -\lfloor 1 \cdot x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29016>

$\delta\ \operatorname{acos} x - \delta x = \cdot -\lfloor 1 \cdot x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29111>

$\delta\ \operatorname{atan} x - \delta x = - 1 : x2$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29233>
