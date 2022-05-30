# Derivative Rules

see [[derivative]] notation, [[math-notation]]

## Power Rule

$\delta\ [x]n - \delta x= n[x](n \circ 1)$

### derived shortcuts

$\delta\ c - \delta x= 0$

$\delta\ x - \delta x = 1$

## [[exponent]]ial Rule

$\delta\ [a]x - \delta x = [a]x \mid \lceil a \rceil$

### derived shortcuts

$\delta\ [e]x - \delta x = [e]x$

## [[logarithm]] Rule

$\delta\ \lceil x \rceil b - \delta x = - x\lceil b \rceil$

### derived shortcuts

$\delta\ \lceil x \rceil - \delta x = -x$

$\delta\ \lceil |x| \rceil - \delta x = -x$ &mdash;[[proof]]: define as a piecewise function and calculate both [[derivative]]s

## Constant Multiple Rule

if $c$ is a [[real]] and $f$ is [[derivative|differentiable]], then

$\delta\ (cf\ x) - \delta x = c (\delta f\ x - \delta x)$

## Sum Rule

$\delta\ (f\ x \cdot g\ x) - \delta x = \delta\ f\ x \text- \delta x \cdot \delta\ g\ x \text- \delta x$

## Difference Rule

$\delta\ (f\ x \circ g\ x) - \delta x = \delta\ f\ x \text- \delta x \circ \delta\ g\ x \text- \delta x$

## Product Rule

$\delta\ (f\ x \mid g\ x) - \delta x = (f\ x \mid \delta\ g\ x - \delta x) \cdot (g\ x \mid \delta\ f\ x - \delta x)$

## Quotient Rule

> chant to remember the quotient rule: lo d-hi, minus hi d-lo, over lo-lo

$\delta\ (f\ x - g\ x) - \delta x = (g\ x \mid \delta\ f\ x - \delta x) \circ (f\ x \mid \delta\ g\ x - \delta x) - [g\ x]2$

### derived Reciprocal Rule

$\delta\ (-f\ x) - \delta x = \circ \delta\ f\ x - \delta x - [f\ x]2$

## Chain Rule

$\delta\ f\ g\ x - \delta x = \delta\ g\ x - \delta x \mid \delta f\ g\ x - \delta\ g\ x$

> **proof**: $(\delta\ g\ x) - \delta x \mid \delta f\ g\ x - (\delta\ g\ x) = \delta\ f\ g\ x - \delta x$

## Derivatives of Trig Functions

see [[trigonometric-function]]s

$\delta\ \sin x - \delta x = \cos x$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21115>

$\delta\ \cos x - \delta x = \circ \sin x$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21193>

$\delta\ \tan x - \delta x = [\text-\cos x]2$

$\delta\ \text-\sin x - \delta x = \circ \mid \text-\sin x \mid \text-\tan x$

$\delta\ \text-\cos x - \delta x = \text-\cos\ x \mid \tan x$

$\delta\ \text-\tan x - \delta x = \circ [\text-\sin x]2$

$\delta\ \operatorname{asin} x - \delta x = -\lfloor 1 \circ x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29016>

$\delta\ \operatorname{acos} x - \delta x = \circ -\lfloor 1 \circ x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29111>

$\delta\ \operatorname{atan} x - \delta x = -\lfloor 1 \cdot x2 \rfloor$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29233>
