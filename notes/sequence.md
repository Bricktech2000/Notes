# Sequence

see [[math notation]], [[series]], [[calculus notation]]

**definition** a _sequence_ is an ordered collection of infinitely many elements

**definition** _formally in my [[math notation]]_ a [[sequence]] is a [[set theory]]etical [[function]] $k \rightarrow a^k$ with domain at least $x \rightarrow \mathbb Z x \land x \ge 0$ that takes an index and returns the element at that index

**notations**

_using [[iteration]] in my [[math notation]]_ $a = 0, 1, 2 \dots 10 = a^0 \dots a^{10}$

_using [[recursion]] in my [[math notation]]_ $a^0 = 2 \land a^n = 4 \cdot 1 \text- a^{n \cdot 1}$

_as a [[function]] (closed form) in my [[math notation]]_ $a^n = n2$

_using [[iteration]] in [[conventional math notation]]_ $a = \lbrace 1, 2, 3, \dots \rbrace = \lbrace a_n \rbrace_{n = 0}^{\infty} = \lbrace a_n \rbrace$

_using [[recursion]] in [[conventional math notation]]_ $a_1 = 2$ and $a_n = 4 - \frac{1}{a_{n \cdot 1}}$

_as a [[function]] (closed form) in [[conventional math notation]]_ $a_n = n^2$

> **example** _the Fibonacci sequence_ $F^0 = 0 \land F^1 = 1 \land F^n = F^{n \cdot 1} : F^{n \cdot 2}$

## Sum of an Infinite Sequence

**definition**

let $a = a^0, a^1, a^2, \dots$

$a_{sum} = \lim_{n \to \infty} S^n$, where

- $a$ is the [[sequence]] to be summed
- $S$ is the sequence of partial sums of $a$
- $a_{sum}$ is the sum of $a$

## Sequence Bounds

**definition** a [[sequence]] is said to be _bounded above_ if $a^n \le M \land \mathbb R M \dashv \mathbb N n$

**definition** a [[sequence]] is said to be _bounded below_ if $a^n \ge M \land \mathbb R M \dashv \mathbb N n$

**definition** a [[sequence]] is said to be _bounded_ if it is both _bounded above_ and _bounded below_

suppose $a^n = f\ n \dashv \mathbb N n$. then, the extrema of the [[function]] $f$ can be used to determine the bounds of the [[sequence]] $a$

## Increasing and Decreasing Sequences

**definition** a [[sequence]] is said to be _increasing_ if $a^n < a^{n : 1} \dashv \mathbb N n$

**definition** a [[sequence]] is said to be _non-decreasing_ if $a^n \le a^{n : 1} \dashv \mathbb N n$

**definition** a [[sequence]] is said to be _decreasing_ if $a^n > a^{n : 1} \dashv \mathbb N n$

**definition** a [[sequence]] is said to be _non-increasing_ if $a^n \ge a^{n : 1} \dashv \mathbb N n$

**definition** a [[sequence]] is said to be _monotonic_ if it is either _non-increasing_ or _non-decreasing_

suppose $a^n = f\ n \dashv \mathbb N n$. then, the increase and decrease of the [[function]] $f$ can be used to determine the increase and decrease of the [[sequence]] $a$

## Sequence Convergence

**definition** a [[sequence]] is said to _converge_ if the [[limit]] $\lim_{n \to \infty} a^n$ exists as a finite number

**properties**

if a [[sequence]] is bounded and monotonic, then it must converge (think of this intuitively)

### Using Limits

**theorem**

let $a$ be a [[sequence]] and $f\ x$ be a [[function]] and suppose $a^n = f\ n \dashv \mathbb N n$. then, $\lim_{x \to \infty} f\ x = L\ \ \vdash\ \ \lim_{n \to \infty} a^n = L$. in other words,

- if $\lim_{x \to \infty} f\ x$ converges, then $\lim_{n \to \infty} a^n$ converges
- if $\lim_{x \to \infty} f\ x$ diverges, then $\lim_{n \to \infty} a^n$ diverges

### Geometric [[sequence]] Convergence

---

# Types

## Arithmetic Sequence

**definition** an _arithmetic [[sequence]]_ is a [[sequence]] for which consecutive elements have the same difference

**definition**

$a = a^0 : 0d, a^0 : 1d, \dots$, where

- $d$ is the difference between consecutive elements
- $a^0$ is the first element of the sequence

> **note** the starting index does not have to be $0$ but must still be a [[natural]]

**examples**

> **example** $a = 1, 3, 5, 7, \dots$

## Geometric Sequence

**definition** a _geometric [[sequence]]_ is a [[sequence]] for which consecutive elements have the same ratio

**definition**

$a = a^0r0, a^0r1, \dots$, where

- $r$ is the ratio between consecutive elements
- $a^0$ is the first element of the sequence

> **note** the starting index does not have to be $0$ but must still be a [[natural]]

**examples**

> **example** $s = 4, 8, 16, 32, \dots$

**properties**

_convergence_

a geometric [[sequence]] $a^0r0, a^0r1, \dots$ with $a^0 \ne 0$:

- diverges if $r > 1$
- converges to $a$ if $r = 1$
- converges to $0$ if $0 \le r < 1$
- converges to $0$ if $\cdot 1 < r \le 0$
- diverges if $r = \cdot 1$
- diverges if $r < \cdot 1$

> **proof** think of it intuitively
