# Bezier Curve

**aka** _Bézier Curve_

--- <https://en.wikipedia.org/wiki/B%C3%A9zier_curve>

--- <https://youtu.be/jvPPXbo87ds?t=191>

**see** [[math notation]], [[spline]], [[curve]]

**representation**

![[bezier_curve.gif]]

## DeCasteljau's Algorithm

DeCasteljau's algorithm is a recursive [[algorithm]] for evaluating [[bezier curve]]s, see [[recursion]]. it is the most intuitive way to understand how [[bezier curve]]s work

**definition** _DeCasteljau's [[algorithm]]_

the [[bezier curve]] **`B p`** of degree **`n`** with [[list]] of control points **`p`** at point **`t`** can be defined as:

**`B (p^0,) = t. p^0`**, and

**`B (p^0 ... p^n) = t. "lerp"  (B (p^0 ... p^n..1) t)  (B (p^1 ... p^n) t)  t`**, where

- **`"lerp" a b = t. (1..t)a : tb`**

> **example** _DeCasteljau's [[algorithm]] for [[bezier curve#cubic bezier curve]]s_
>
> ![[Pasted image 20221223230657.png]]

## Bernstein Polynomial

Bernstein polynomials can be used to graphically represent the "influence" of each control point on the [[bezier curve]]. Bernstein polynomials are easy to derive from DeCasteljau's [[algorithm]] --- <https://youtu.be/aVwxzDHniEw?t=262>

**definition** _Bernstein polynomials_

the [[bezier curve]] **`B p`** of degree **`n`** with [[list]] of control points **`p`** at point **`t`** can be defined as:

**`B p = t. :p(P t)`**, where

- **`P t`** are the Bernstein polynomials **`P t = k. C n k | [1..t](n..k) | [t]k`** of the [[bezier curve]]
- **`C n k`** is [[set#combination]] "**`n`** choose **`k`**"

> **example** _Bernstein polynomials for [[bezier curve#cubic bezier curve]]s_
>
> ![[Pasted image 20221223230728.png]]

## Polynomial Form

the [[polynomial]] form of a [[bezier curve]] is useful because, given a [[list]] of control points, one can cache the coefficients of the [[polynomial]] and use them to evaluate the [[curve]] at any point **`t`**

**definition** _polynomial form_

the [[bezier curve]] **`B p`** of degree **`n`** with [[list]] of control points **`p`** at point **`t`** can be defined as:

**`B p = t. :t[0...n](C p)`**, where

- **`C p`** are the [[polynomial]] cofficients of the [[bezier curve]]

> **example** _[[polynomial]] form of [[bezier curve#cubic bezier curve]]s_
>
> ![[Pasted image 20221223230759.png]]

## Matrix Form

the [[matrix]] form of a [[bezier curve]] consists of two [[matrix#multiplication]]s. in the definition below, computing the first yields the _Bernstein polynomials_ whereas computing the second yields the _polynomial form_

**definition** _matrix form_

the [[bezier curve]] **`B p`** of degree **`n`** with [[list]] of control points **`p`** at point **`t`** can be defined as:

**`B p = t. :(:t[0...n]M)p`**, where

- **`p`** are the control points as a column [[euclidean vector]] #todo mm
- **`t[0...n]`** are powers of **`t`** as a row [[euclidean vector]] #todo mm
- **`M`** is the _characteristic matrix_ of the [[bezier curve]]

> **example** _[[matrix]] form of [[bezier curve#cubic bezier curve]]s_
>
> ![[Pasted image 20221223231125.png]]

---

# Types

## Linear Bezier Curve

**equiv** _linear interpolation **`"lerp"`**_

**definition** a _linear bezier curve_ is a [[bezier curve]] of degree **`1`**

**representation**

![[bezier_1_big.gif]]

--- Wikipedia

## Quadratic Bezier Curve

**definition** a _quadratic bezier curve_ is a [[bezier curve]] of degree **`2`**

**representation**

![[bezier_2_big.gif]]

--- Wikipedia

## Cubic Bezier Curve

**definition** a _cubic bezier curve_ is a [[bezier curve]] of degree **`3`**

**representation**

![[bezier_3_big.gif]]

--- Wikipedia
