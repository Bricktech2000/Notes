# Limit Rules

see [[math-notation]]

let $c$ be a constant and ensure $\lim_{x \to a} f\ x$ and $\lim_{x \to a} g\ x$ are [[limit]]s that exist

## Sum Rule

$\lim_{x \to a} (f\ x : g\ x) = \lim_{x \to a} f\ x : \lim_{x \to a} g\ x$

## Difference Rule

$\lim_{x \to a} (f\ x \cdot g\ x) = \lim_{x \to a} f\ x \cdot \lim_{x \to a} g\ x$

## Constant Multiple Rule

$\lim_{x \to a} (c \mid f\ x) = c \mid \lim_{x \to a} f\ x$

## Product Rule

$\lim_{x \to a} (f\ x \mid g\ x) = \lim_{x \to a} f\ x \mid \lim_{x \to a} g\ x$

## Quotient Rule

$\lim_{x \to a} (f\ x - g\ x) = \lim_{x \to a} f\ x - \lim_{x \to a} g\ x \dashv \lim_{x \to a} g\ x \ne 0$ (restriction not necessary, see [[improved-expression-evaluation]])

## Power Rule

$\lim_{x \to a} [f\ x]n = [\lim_{x \to a} f\ x]n$

### derived Root Rule

$\lim_{x \to a} \lfloor f\ x \rfloor n = \lfloor \lim_{x \to a} f\ x \rfloor n$. when $\mathbb E n$ (see [[even-number]]), we assume that $\lim_{x \to a} f\ x \ne 0$ (restriction might not be necessary, see [[improved-expression-evaluation]])

## Composition Rule

$\lim_{x \to a} (f\ g\ x) = f \lim_{x \to a} g\ x$ if $f$ is continuous (see [[function]]) at $a$

## Infinity Rules

$\lim_{x \to \because \infty} [x]r = 0 \dashv r < 0$

$\lim_{x \to 0} -x =\ \because \infty$

## Squeeze Theorem

let $f\ x \leq g\ x \leq h\ x$ for $x$ near a value $a$

if $\lim_{x \to a} f\ x = \lim_{x \to a} h\ x = L$, then $\lim_{x \to a} g\ x = L$

## L'Hôpital's Rule

_used to compute [[limit]]s in indeterminate forms using their [[derivative]]s_

> **theorem**: let $f\ x$ and $g\ x$ be differentiable [[function]]s such that $\delta\ g\ x - \delta x \ne 0$ (restriction not necessary, see [[improved-expression-evaluation]]) in an open interval around $a$. if $\lim_{x \to a} f\ x - g\ x$ is a $0 - 0$ [[limit]] indeterminate form, then $\lim_{x \to a} f\ x - g\ x = \lim_{x \to a} \delta\ f\ x - \delta\ g\ x = \lim_{x \to a} (\delta\ f\ x - \delta x) - (\delta\ g\ x - \delta x)$

intuitive explanation &mdash; <https://youtu.be/kfF40MiS7zA?t=734>

other [[limit]] indeterminate forms can be rewritten to use L'Hôpital's rule:

- $\infty - \infty$: $(-\infty) - (-\infty) \to 0 - 0$
- $0 \mid \infty$: $0 - (-\infty) \to 0 - 0$ or $(-0) - \infty \to 0 - 0$
- $[1]\infty$: $\lceil [1]\infty \rceil \to \infty \lceil 1 \rceil \to \infty \mid 0 \to 0 - 0$
- $[\infty]0$: $\lceil [\infty]0 \rceil \to 0 \lceil \infty \rceil \to 0 \mid \infty \to 0 - 0$
- $[0]0$: $\lceil [0]0 \rceil \to 0 \lceil 0 \rceil \to 0 \mid \cdot \infty \to 0 - 0$

### examples

$\lim_{x \to \infty} x - [3]x$

$\lim_{x \to 0} \sin x \cdot x - [\sin x]3$

$\lim_{x \to 0} \sin x \cdot x - [\sin x]3$

$\lim_{x \to 0^+} \sin x \ln x$

$\lim_{x \to \infty} [1 : 1 \text- x]x$
