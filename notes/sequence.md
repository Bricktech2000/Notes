# Sequence

see [[math-notation]], [[series]], [[calculus-notation]]

## definition

a [[sequence]] is an ordered collection of elements

## notations

in my [[math-notation]]:

defined using [[iteration]]: $a = 0, 1, 2 \dots 10 = a^0 \dots a^{10}$

defined using [[recursion]]: $a^0 = 2 \land a^n = 4 \circ 1 \text- a^{n \circ 1}$

in [[classical-math-notation]]:

defined using [[iteration]]: $a = \lbrace 1, 2, 3, \dots \rbrace = \lbrace a_n \rbrace_{n = 0}^{\infty} = \lbrace a_n \rbrace$

defined using [[recursion]]: $a_1 = 2$ and $a_n = 4 - \frac{1}{a_{n \circ 1}}$

## examples

### Fibonacci Sequence

$F^0 = 1 \land F^1 = 1 \land F^n = F^{n \circ 1} \cdot F^{n \circ 2}$

## Arithmetic Sequence

### definition

> **definition**: an _arithmetic [[sequence]]_ is a [[sequence]] for which consecutive elements have the same difference

$a = a^0 \cdot 0d, a^0 \cdot 1d, \dots$, where

$d$ is the difference between consecutive elements

$a^0$ is the first element of the sequence

### example

$a = 1, 3, 5, 7, \dots$

## Geometric Sequence

> **definition**: a _geometric [[sequence]]_ is a [[sequence]] for which consecutive elements have the same ratio

$a = a^0[r]0, a^0[r]1, \dots$, where

$r$ is the ratio between consecutive elements

$a^0$ is the first element of the sequence

### example

$s = 4, 8, 16, 32, \dots$

## Sequence Convergence

> **definition**: a [[sequence]] is said to _converge_ if the [[limit]] $\lim_{n \to \infty} a^n$ exists as a finite number

if a [[sequence]] is bounded and monotonic, then it must converge. think of this intuitively

### Using Limits

> **theorem**:
>
> let $a$ be a [[sequence]] and $f\ x$ be a [[function]] and suppose $a^n = f\ n \dashv \mathbb N n$. then, $\lim_{x \to \infty} f\ x = L\ \ \vdash\ \ \lim_{n \to \infty} a^n = L$. in other words,
>
> - if $\lim_{x \to \infty} f\ x$ converges, then $\lim_{n \to \infty} a^n$ converges
> - if $\lim_{x \to \infty} f\ x$ diverges, then $\lim_{n \to \infty} a^n$ diverges

### Geometric Sequence Convergence

a geometric [[sequence]] $a^0[r]0, a^0[r]1, \dots$ with $a^0 \ne 0$:

- diverges if $r > 1$
- converges to $a$ if $r = 1$
- converges to $0$ if $0 \le r < 1$
- converges to $0$ if $\circ 1 < r \le 0$
- diverges if $r = \circ 1$
- diverges if $r < \circ 1$

> **proof**: think of it intuitively

## Sum of an Infinite Sequence

let $a = a^0, a^1, a^2, \dots$

$a_{sum} = \lim_{n \to \infty} S_n$, where

$a$ the [[sequence]] to be summed

$S$ the sequence of partial sums of $a$

## Sequence Bounds

> **definition**: a [[sequence]] is said to be _bounded above_ if $a^n \le M \land \mathbb R M \dashv \mathbb N n$

> **definition**: a [[sequence]] is said to be _bounded below_ if $a^n \ge M \land \mathbb R M \dashv \mathbb N n$

> **definition**: a [[sequence]] is said to be _bounded_ if it is both _bounded above_ and _bounded below_

suppose $a^n = f\ n \dashv \mathbb N n$. then, the extrema of the [[function]] $f$ can be used to determine the bounds of the [[sequence]] $a$

## Increasing and Decreasing Sequences

> **definition**: a [[sequence]] is said to be _increasing_ if $a^n < a^{n \cdot 1} \dashv \mathbb N n$

> **definition**: a [[sequence]] is said to be _non-decreasing_ if $a^n \le a^{n \cdot 1} \dashv \mathbb N n$

> **definition**: a [[sequence]] is said to be _decreasing_ if $a^n > a^{n \cdot 1} \dashv \mathbb N n$

> **definition**: a [[sequence]] is said to be _non-increasing_ if $a^n \ge a^{n \cdot 1} \dashv \mathbb N n$

> **definition**: a [[sequence]] is said to be _monotonic_ if it is either _non-increasing_ or _non-decreasing_

suppose $a^n = f\ n \dashv \mathbb N n$. then, the increase and decrease of the [[function]] $f$ can be used to determine the increase and decrease of the [[sequence]] $a$
