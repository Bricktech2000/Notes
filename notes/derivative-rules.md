# Derivative Rules

see [[derivative]] notation, [[math-notation]]

## Power Rule

$d\text-dx\ [x]n = n[x](n \circ 1)$

### derived shortcuts

$d\text-dx\ c = 0$

$d\text-dx\ x = 1$

## Exponential Rule

$d\text-dx\ [a]x = [a]x\ |\ \lceil a \rceil$

### derived shortcuts

$d\text-dx\ [e]x = [e]x$

## Logarithm Rule

$d\text-dx\ \lceil x \rceil b = - x\lceil b \rceil$

### derived shortcuts

$d\text-dx\ \lceil x \rceil = -x$

## Constant Multiple Rule

if $c$ is a [[real-number]] and $f$ is [[derivative|differentiable]], then

$d\text-dx\ (cf\ x) = c\ |\ d\text-dx\ f\ x$

## Sum Rule

$d\text-dx\ (f\ x \cdot g\ x) = d\text-dx\ f\ x \cdot d\text-dx\ g\ x$

## Difference Rule

$d\text-dx\ (f\ x \circ g\ x) = d\text-dx\ f\ x \circ d\text-dx\ g\ x$

## Product Rule

$d\text-dx\ (f\ x\ |\ g\ x) = (f\ x\ |\ d\text-dx\ g\ x) \cdot (g\ x\ |\ d\text-dx\ f\ x)$

## Quotient Rule

> chant to remember the quotient rule: lo d-hi, minus hi d-lo, over lo-lo

$d\text-dx\ (f\ x - g\ x) = g\ x\ '\ d\text-dx\ f\ x \circ f\ x\ '\ d\text-dx\ g\ x - [g\ x]2$

### derived Reciprocal Rule

$d\text-dx\ (-f\ x) = \circ d\text-dx\ f\ x - [f\ x]2$

## Chain Rule

derivative notation [[think]]

$\frac{d}{dx}[f(g(x))] = \frac{d}{dx}f(g(x)) \times \frac{d}{dx}g(x)$

$f(g(x))' = f'(g(x)) \times g'(x)$

$d\text-dx\ (f\ g\ x) = (d\text-dx\ f)\ g\ x\ |\ d\text-dx\ g\ x$

## Squeeze Theorem

let $f\ x \leq g\ x \leq h\ x$

if $\lim_{x \to a} f\ x = \lim_{x \to a} h\ x = L$, then $\lim_{x \to a} g\ x = L$

## Derivatives of Trig Functions

see [[trigonometric-identity]]es

$d\text-dx\ \sin x = \cos x$

$d\text-dx\ \cos x = \circ \sin x$

$d\text-dx\ \tan x = [\sec x]2$

$d\text-dx\ \csc x = \circ \csc\ x\ |\ \cot\ x$

$d\text-dx\ \sec x = \sec\ x\ |\ \tan\ x$

$d\text-dx\ \cot x = \circ [\csc x]2$

## special limits

[[todo]]

let $\theta$ be an angle in radians

$\lim_{\theta \to 0} \sin \theta - \theta = 1$

$\lim_{\theta \to 0} \cos\ (\theta \circ 1) - \theta = 0$

### intuitive shortcuts derived

$\lim_{\theta \to 0} \sin \theta = \theta$, or

$\sin \theta \approx \theta$ when $\theta$ is near $0$
