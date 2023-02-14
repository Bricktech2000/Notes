# Sequence

**see** [[math notation]], [[series]], [[calculus notation]], [[substring]], [[subsequence]]

**definition** a _sequence_ is an ordered collection of infinitely many elements

**definition** _formally in my [[math notation]]_ a [[sequence]] is a [[set theory]]etical [[function]] that takes a [[natural]] index and returns the element at that index

**notations**

_using [[iteration]] in my [[math notation]]_ $a = 0, 1, 2 \cdots 10 = a^0 \cdots a^{10}$

_using [[recursion]] in my [[math notation]]_ $a^0 = 2 \land a^n = 4 \cdot 1 \text- a^{n \cdot 1}$

_as a [[function]] (closed form) in my [[math notation]]_ $a^n = n2$

_using [[iteration]] in [[conventional math notation]]_ $a = \lbrace 1, 2, 3, \dots \rbrace = \lbrace a_n \rbrace_{n = 0}^{\infty} = \lbrace a_n \rbrace$

_using [[recursion]] in [[conventional math notation]]_ $a_1 = 2$ and $a_n = 4 - \frac{1}{a_{n \cdot 1}}$

_as a [[function]] (closed form) in [[conventional math notation]]_ $a_n = n^2$

> **example** _the Fibonacci sequence_ $F^0 = 0 \land F^1 = 1 \land F^n = F^{n \cdot 1} : F^{n \cdot 2}$

## Sum

**definition**

let $a = a^0, a^1, a^2, \cdots$

$a_{sum} = \,: a = S^n\ \braket{n \rightarrow \infty}$, where

- $a$ is the [[sequence]] to be summed
- $S$ is the [[series#sequence of partial sums]] of $a$
- $a_{sum} = \,: a$ is the sum of $a$

## Bound

**definition** a [[sequence]] is said to be _bounded above_ if $a^n \dashv M \land \mathbb R M > \mathbb N n$

**definition** a [[sequence]] is said to be _bounded below_ if $a^n \vdash M \land \mathbb R M > \mathbb N n$

**definition** a [[sequence]] is said to be _bounded_ if it is both _bounded above_ and _bounded below_

suppose $a^n = f\ n > \mathbb N n$. then, the [[function#extremum]]a of $f$ can be used to determine the [[sequence#bound]]s of the [[sequence]] $a$

## Increasing Sequence

## Decreasing Sequence

**definition** a [[sequence]] is said to be _increasing_ if $a^n\ (\dashv \land +)\ a^{n : 1} > \mathbb N n$

**definition** a [[sequence]] is said to be _non-decreasing_ if $a^n \dashv a^{n : 1} > \mathbb N n$

**definition** a [[sequence]] is said to be _decreasing_ if $a^n\ (\vdash \land +)\ a^{n : 1} > \mathbb N n$

**definition** a [[sequence]] is said to be _non-increasing_ if $a^n \vdash a^{n : 1} > \mathbb N n$

**definition** a [[sequence]] is said to be _monotonic_ if it is either _non-increasing_ or _non-decreasing_

suppose $a^n = f\ n \dashv \mathbb N n$. then, the increase and decrease of the [[function]] $f$ can be used to determine the increase and decrease of the [[sequence]] $a$

## Convergent Sequence

## Divergent Sequence

**definition** a [[sequence]] is said to _converge_ if the [[limit]] $a^n\ \braket{n \rightarrow \infty}$ exists as a finite number, see [[limit#existence]]

**properties**

if a [[sequence]] is [[sequence#bound]]ed and monotonic (see [[sequence#decreasing sequence]]), then it must converge (think of this intuitively)

### using limits

**theorem**

let $a$ be a [[sequence]] and $f\ x$ be a [[function]] and suppose $a^n = f\ n > \mathbb N n$. then, $f\ x\ \braket{x \rightarrow \infty} = L\ \ <\ \ a^n\ \braket{n \rightarrow \infty} = L$. in other words,

- if $f\ x\ \braket{x \rightarrow \infty}$ converges, then $a^n\ \braket{n \rightarrow \infty}$ converges
- if $f\ x\ \braket{x \rightarrow \infty}$ diverges, then $a^n\ \braket{n \rightarrow \infty}$ diverges

### [[sequence#geometric sequence]] convergence

---

# Types

## Arithmetic Sequence

**definition** an _arithmetic [[sequence]]_ is a [[sequence]] for which consecutive elements have the same difference

**definition**

$a = a^0 : 0d, a^0 : 1d, \cdots$, where

- $d$ is the difference between consecutive elements
- $a^0$ is the first element of the sequence

> **note** the starting index does not have to be $0$ but must still be a [[natural]]

**examples**

> **example** $a = 1, 3, 5, 7, \cdots$

## Geometric Sequence

**definition** a _geometric [[sequence]]_ is a [[sequence]] for which consecutive elements have the same ratio

**definition**

$a = a^0r0, a^0r1, \cdots$, where

- $r$ is the ratio between consecutive elements
- $a^0$ is the first element of the sequence

> **note** the starting index does not have to be $0$ but must still be a [[natural]]

**examples**

> **example** $s = 4, 8, 16, 32, \cdots$

**properties**

_convergence_

a geometric [[sequence]] $a^0r0, a^0r1, \cdots$ with $a^0 + 0$:

- diverges if $r\ (\vdash \land +)\ 1$
- converges to $a$ if $r = 1$
- converges to $0$ if $0 \dashv r\ (\dashv \land +)\ 1$
- converges to $0$ if $\cdot 1\ (\dashv \land +)\ r \dashv 0$
- diverges if $r = \cdot 1$
- diverges if $r\ (\dashv \land +)\ \cdot 1$

> **proof** think of it intuitively
