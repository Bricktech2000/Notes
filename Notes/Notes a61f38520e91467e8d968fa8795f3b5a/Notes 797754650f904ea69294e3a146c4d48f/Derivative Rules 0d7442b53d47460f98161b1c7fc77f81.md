# Derivative Rules

see [Derivative Notation](Derivative%20Notation%203fb6a05f74d3431396514e1ef2af24d4.md), [Classical Math Notation](../Tags%20b793d46ea133446daa88889450d15033/Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md)

## Power Rule

$y = x^n$

$\frac{dy}{dx} = nx^{n-1}$

some shortcuts derived from the power rule:

- $\frac{d(c)}{dx} = 0$
- $\frac{d(x)}{dx} = 1$

## Exponential Rule

$(a^x)' = a^{x}\ln(a)$

some shortcuts derived from the exponential rule:

- $\frac{d(e^x)}{dx} = e^x$

## Constant Multiple Rule

if $c$ is a real number and $f$ is a [Differentiable Function](Differentiable%20Function%20f678cccd6d6941e3b2027c2f4a6ce004.md), then

$\frac{d}{dx} [c \times f(x)] = c \times \frac{d}{dx} f(x)$

## Sum Rule

$\frac{d}{dx} [f(x) + g(x)] = \frac{d}{dx} f(x) + \frac{d}{dx} g(x)$

## Difference Rule

$\frac{d}{dx} [f(x) - g(x)] = \frac{d}{dx} f(x) - \frac{d}{dx} g(x)$

## Product Rule

$\frac{d}{dx}[f(x)g(x)] = f(x)\frac{d}{dx}g(x) + g(x)\frac{d}{dx}f(x)$

$[f(x)g(x)]' = f(x)g'(x) + f'(x)g(x)$

## Quotient Rule

> chant to remember the quotient rule: lo d-hi, minus hi d-lo, over lo-lo
> 

$\frac{d}{dx}[\frac{f(x)}{g(x)}] = \frac{g(x)\frac{d}{dx}f(x) - f(x)\frac{d}{dx}g(x)}{g(x)^2}$

$[\frac{f(x)}{g(x)}]' = \frac{g(x)f'(x) - f(x)g'(x)}{g(x)^2}$

## Reciprocal Rule

$\frac{d}{dx}[\frac{1}{f(x)}] = -\frac{\frac{d}{dx}f(x)}{f(x)^2}$

$[\frac{1}{f(x)}]' = -\frac{f'(x)}{f(x)^2}$

## Chain Rule

$\frac{d}{dx}[f(g(x))] = \frac{d}{dx}f(g(x)) \times \frac{d}{dx}g(x)$

$f(g(x))' = f'(g(x)) \times g'(x)$

## Squeeze Theorem

$f(x) \leq g(x) \leq h(x)$

$\lim_{x -> a}f(x) = \lim_{x -> a}h(x) = L$ then $\lim_{x -> a} g(x) = L$

## Derivatives of Trig Functions

$(\sin x)' = \cos x$

$(\cos x)' = -\sin x$

$(\tan x)' = \sec^2x$

$(\csc x)' = -\csc(x) \cot(x)$

$(\sec x)' = \sec(x) \tan(x)$

$(\cot x)' = -csc^2x$

## special limits

if $\theta$ is in radians:

$\lim_{\theta \to 0}\frac{\sin\theta}{\theta} = 1$

$\lim_{\theta \to 0} \frac{\cos\theta - 1}{\theta} = 0$

intuitive shortcuts derived from the special limits above:

$\sin\theta = \theta\ when\ \theta\ is\ near\ 0$