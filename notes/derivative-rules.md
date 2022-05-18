# Derivative Rules

see [[derivative]] notation, [[math-notation]]

## Power Rule

$\delta\ [x]n - \delta x= n[x](n \circ 1)$

### derived shortcuts

$\delta\ c - \delta x= 0$

$\delta\ x - \delta x = 1$

## Exponential Rule

$\delta\ [a]x - \delta x = [a]x\ |\ \lceil a \rceil$

### derived shortcuts

$\delta\ [e]x - \delta x = [e]x$

## Logarithm Rule

$\delta\ \lceil x \rceil b - \delta x = - x\lceil b \rceil$

### derived shortcuts

$\delta\ \lceil x \rceil - \delta x = -x$

## Constant Multiple Rule

if $c$ is a [[real-number]] and $f$ is [[derivative|differentiable]], then

$\delta\ (cf\ x) - \delta x = c (\delta f\ x - \delta x)$

## Sum Rule

$\delta\ (f\ x \cdot g\ x) - \delta x = \delta\ f\ x \text- \delta x \cdot \delta\ g\ x \text- \delta x$

## Difference Rule

$\delta\ (f\ x \circ g\ x) - \delta x = \delta\ f\ x \text- \delta x \circ \delta\ g\ x \text- \delta x$

## Product Rule

$\delta\ (f\ x\ |\ g\ x) - \delta x = (f\ x\ |\ \delta\ g\ x - \delta x) \cdot (g\ x\ |\ \delta\ f\ x - \delta x)$

## Quotient Rule

> chant to remember the quotient rule: lo d-hi, minus hi d-lo, over lo-lo

$\delta\ (f\ x - g\ x) - \delta x = (g\ x\ |\ \delta\ f\ x - \delta x) \circ (f\ x\ |\ \delta\ g\ x - \delta x) - [g\ x]2$

### derived Reciprocal Rule

$\delta\ (-f\ x) \delta x = \circ \delta\ f\ x - \delta x - [f\ x]2$

## Chain Rule

$\delta\ (f\ g\ x) - \delta x = (\delta\ f\ x - \delta x)\ g\ x\ |\ \delta\ g\ x - \delta x$

## Squeeze Theorem

let $f\ x \leq g\ x \leq h\ x$

if $\lim_{x \to a} f\ x = \lim_{x \to a} h\ x = L$, then $\lim_{x \to a} g\ x = L$

## Derivatives of Trig Functions

see [[trigonometric-identity]]es

$\delta\ \sin x - \delta x = \cos x$

$\delta\ \cos x - \delta x = \circ \sin x$

$\delta\ \tan x - \delta x = [-\cos x]2$

$\delta\ 1\text-\sin x - \delta x = \circ \text-\sin x\ |\ \text-\tan x$

$\delta\ 1\text-\cos x - \delta x = \text-\cos\ x\ |\ \tan x$

$\delta\ 1\text-\tan x - \delta x = \circ [\text-\sin x]2$
