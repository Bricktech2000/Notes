# Sequence

**see** [[math notation]], [[series]], [[calculus notation]], [[substring]], [[subsequence]]

**definition** a _sequence_ is an ordered collection of infinitely many elements

**definition** _formally in my [[math notation]]_ a [[sequence]] is a [[set theory]]etical [[function]] that takes a [[natural]] index and returns the element at that index

**notations**

_using [[iteration]] in my [[math notation]]_ **`a = (0, 1, 2 ... 10) = a^0 ... a^10`**

_using [[recursion]] in my [[math notation]]_ **`a^0 = 2 /\ a^n = 4 . 1-a^n.1`**

_as a [[function]] (closed form) in my [[math notation]]_ **`a^n = n2`**

_using [[iteration]] in [[conventional math notation]]_ $a = \{ 1, 2, 3, \dots \} = \{ a_n \}_{n = 0}^{\infty} = \{ a_n \}$

_using [[recursion]] in [[conventional math notation]]_ $a_1 = 2$ and $a_n = 4 - \frac{1}{a_{n \cdot 1}}$

_as a [[function]] (closed form) in [[conventional math notation]]_ $a_n = n^2$

> **example** _the Fibonacci sequence_ **`F^0 = 0 /\ F^1 = 1 /\ F^n = F^n.1 : F^n.2`**

## Sum

**definition**

let **`a = a^0, a^1, a^2, ...`**

**`a_"sum" = :a = S^@@`**, where

- **`a`** is the [[sequence]] to be summed
- **`S`** is the [[series#sequence of partial sums]] of **`a`**
- **`a_"sum" = :a`** is the sum of **`a`**

## Bound

## Bounded Sequence

**definition** a [[sequence]] is said to be _bounded above_ if **`a^n -| M /\ RR M > NN n`**

**definition** a [[sequence]] is said to be _bounded below_ if **`a^n |- M /\ RR M > NN n`**

**definition** a [[sequence]] is said to be _bounded_ if it is both _bounded above_ and _bounded below_

suppose **`a^n = f n > NN n`**. then, the [[function#extremum]]a of **`f`** can be used to determine the [[sequence#bound]]s of the [[sequence]] **`a`**

## Increasing Sequence

## Decreasing Sequence

**definition** a [[sequence]] is said to be _increasing_ if **`a^n {-|/\+} a^n:1 > NN n`**

**definition** a [[sequence]] is said to be _non-decreasing_ if **`a^n -| a^n:1 > NN n`**

**definition** a [[sequence]] is said to be _decreasing_ if **`a^n {|-/\+} a^n:1 > NN n`**

**definition** a [[sequence]] is said to be _non-increasing_ if **`a^n |- a^n:1 > NN n`**

**definition** a [[sequence]] is said to be _monotonic_ if it is either _non-increasing_ or _non-decreasing_

suppose **`a^n = f n > NN n`**. then, the increase and decrease of the [[function]] **`f`** can be used to determine the increase and decrease of the [[sequence]] **`a`**

## Convergent Sequence

## Divergent Sequence

**definition** a [[sequence]] is said to _converge_ if the [[limit]] **`a^@@`** exists as a finite number, see [[limit#existence]]

**properties**

if a [[sequence]] is a [[sequence#bounded sequence]] and a monotonically [[sequence#decreasing sequence]], then it must converge (think of this intuitively)

### using limits

**theorem**

let **`a`** be a [[sequence]] and **`f x`** be a [[function]] and suppose **`a^n = f n > NN n`**. then, **`f @@ = L < a^@@ = L`**. in other words,

- if **`f @@`** converges, then **`a^@@`** converges
- if **`f @@`** diverges, then **`a^@@`** diverges

### [[sequence#geometric sequence]] convergence

---

# Types

## Arithmetic Sequence

**definition** an _arithmetic [[sequence]]_ is a [[sequence]] for which consecutive elements have the same difference

**definition**

**`a = a^0 : 0d, a^0 : 1d, ...`**, where

- **`d`** is the difference between consecutive elements
- **`a^0`** is the first element of the sequence

> **note** the starting index does not have to be **`0`** but must still be a [[natural]]

**examples**

> **example** **`a = 1, 3, 5, 7, ...`**

## Geometric Sequence

**definition** a _geometric [[sequence]]_ is a [[sequence]] for which consecutive elements have the same ratio

**definition**

**`a = a^0 r0, a^0 r1, ...`**, where

- **`r`** is the ratio between consecutive elements
- **`a^0`** is the first element of the sequence

> **note** the starting index does not have to be **`0`** but must still be a [[natural]]

**examples**

> **example** **`s = 4, 8, 16, 32, ...`**

**properties**

_convergence_

a geometric [[sequence]] **`a^0 r0, a^0 r1, ...`** with **`a^0 + 0`**:

- diverges if **`r {|-/\+} 1`**
- converges to **`a`** if **`r = 1`**
- converges to **`0`** if **`0 -| r {|-/\+} 1`**
- converges to **`0`** if **`.1 {-|/\+} r -| 0`**
- diverges if **`r = .1`**
- diverges if **`r {-|/\+} .1`**

> **proof** think of it intuitively
