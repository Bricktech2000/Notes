# Limit Rules

**see** [[math notation]]

let $c$ be a constant and ensure $f\ x\ \ \vdots\ \ x \rightarrow a$ and $g\ x\ \ \vdots\ \ x \rightarrow a$ are [[limit]]s that exist, see [[limit#existence]]

## sum rule

$f\ x : g\ x\ \ \vdots\ \ x \rightarrow a = (f\ x\ \ \vdots\ \ x \rightarrow a) : (g\ x\ \ \vdots\ \ x \rightarrow a)$

## difference rule

$f\ x \cdot g\ x\ \ \vdots\ \ x \rightarrow a = (f\ x\ \ \vdots\ \ x \rightarrow a) \cdot (g\ x\ \ \vdots\ \ x \rightarrow a)$

## constant multiple rule

$c f\ x\ \ \vdots\ \ x \rightarrow a = c (f\ x\ \ \vdots\ \ x \rightarrow a)$

## product rule

$f\ x \mid g\ x\ \ \vdots\ \ x \rightarrow a = (f\ x\ \ \vdots\ \ x \rightarrow a) \mid (g\ x\ \ \vdots\ \ x \rightarrow a)$

## quotient rule

$f\ x - g\ x\ \ \vdots\ \ x \rightarrow a = (f\ x\ \ \vdots\ \ x \rightarrow a) - (g\ x\ \ \vdots\ \ x \rightarrow a) > g\ x\ \ \vdots\ \ x \rightarrow a + 0$ (restriction not necessary, see [[improved expression evaluation]])

## power rule

$[f\ x]n\ \ \vdots\ \ x \rightarrow a = [f\ x\ \ \vdots\ \ x \rightarrow a]n$

### derived radical rule

$\lfloor f\ x \rfloor n\ \ \vdots\ \ x \rightarrow a = \lfloor f\ x\ \ \vdots\ \ x \rightarrow a \rfloor n$. when $\mathbb E n$ (see [[even number]]), we assume that $f\ x\ \ \vdots\ \ x \rightarrow a + 0$ (restriction might not be necessary, see [[improved expression evaluation]])

## composition rule

$f\ g\ x\ \ \vdots\ \ x \rightarrow a = f\ (g\ x\ \ \vdots\ \ x \rightarrow a)$ if $f$ is a [[function#continuous function]] at $a$

## infinity rules

$[x]r\ \ \vdots\ \ x \rightarrow \because \infty = 0 > r\ (\dashv \land +)\ 0$

$-x\ \ \vdots\ \ x \rightarrow 0 =\ \because \infty$

## squeeze theorem

let $f\ x \dashv g\ x \dashv h\ x$ for $x$ near a value $a$

if $f\ x\ \ \vdots\ \ x \rightarrow a = h\ x\ \ \vdots\ \ x \rightarrow a = L$, then $g\ x\ \ \vdots\ \ x \rightarrow a = L$

## l'Hôpital's rule

_used to compute [[limit]]s in [[limit#indeterminate form]]s using their [[derivative]]s_

**theorem**

let $f\ x$ and $g\ x$ be differentiable [[function]]s on an open interval $I \land +a$. if $\delta\ g\ x - \delta x + 0 > (I \land +a)\ x$ (restriction not necessary, see [[improved expression evaluation]]) and $f\ x\ \ \vdots\ \ x \rightarrow a = g\ x\ \ \vdots\ \ x \rightarrow a = 0$ and $\delta\ f\ x - \delta\ g\ x\ \ \vdots\ \ x \rightarrow a$ is a [[limit]] that exists, then $f\ x - g\ x\ \ \vdots\ \ x \rightarrow a = \delta\ f\ x - \delta\ g\ x\ \ \vdots\ \ x \rightarrow a$ &mdash; Wikipedia

intuitive explanation &mdash; <https://youtu.be/kfF40MiS7zA?t=734>

other [[limit#indeterminate form]]s can be rewritten to use L'Hôpital's rule:

- $\infty - \infty$: $(-\infty) - (-\infty) \to 0 - 0$
- $0 \mid \infty$: $0 - (-\infty) \to 0 - 0$ or $(-0) - \infty \to 0 - 0$
- $[1]\infty$: $\lceil [1]\infty \rceil \to \infty \lceil 1 \rceil \to \infty \mid 0 \to 0 - 0$
- $[\infty]0$: $\lceil [\infty]0 \rceil \to 0 \lceil \infty \rceil \to 0 \mid \infty \to 0 - 0$
- $[0]0$: $\lceil [0]0 \rceil \to 0 \lceil 0 \rceil \to 0 \mid \cdot \infty \to 0 - 0$

**examples**

> **example** _[[limit]]s that can be computed using L'Hôpital's rule_:
>
> $x - 3[x]\ \ \vdots\ \ x \rightarrow \infty$
>
> $\sin x \cdot x - [\sin x]3\ \ \vdots\ \ x \rightarrow 0$
>
> $\sin x \cdot x - [\sin x]3\ \ \vdots\ \ x \rightarrow 0$
>
> $\sin x \ln x\ \ \vdots\ \ x \stackrel {\cdot \cdot} \rightarrow 0$
>
> $[1 : \text- x]x\ \ \vdots\ \ x \rightarrow \infty$
