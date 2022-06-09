# Function

see [[math-notation]]

## types

[[boolean]] [[function]]

[[rational-function]]

[[piecewise-function]]

[[pure-function]]

[[trigonometric-function]]

## applications

[[curve-sketching]]

[[optimizing-a-function]]

[[functional-programming]]

[[function-vector-space]]

## operations

see [[function-vector-space]], [[vector-space]]

### Zero Function

$O x = 0 \dashv \mathbb R x$

### Function Addition

$(f \cdot g)\ x = f\ x \cdot g\ x$

### Multiplication by a Scalar

$(cf)\ x = c \mid f\ x$

## Function Parity

### Even Function

_an even function is symmetrical about the y axis_

$f x = f (\circ x) \dashv \mathbb R x$

### Odd Function

_an odd function is symmetrical about the y axis, but also flipped about the x axis_

$\circ f x = f (\circ x) \dashv \mathbb R x$

## Increasing and Decreasing Functions

### definition

see [[calculus-notation]]

a [[function]] $f$ is _increasing_ on an interval $a \le x \le b$ if $x_1 < x_2 \vdash f\ x_1 < f\ x_2$, or $\delta\ f\ x - \delta x > 0$ on that interval

a [[function]] $f$ is _decreasing_ on an interval $a \le x \le b$ if $x_1 > x_2 \vdash f\ x_1 > f\ x_2$, or $\delta\ f\ x - \delta x < 0$ on that interval

## Concavity

### definition

see [[calculus-notation]]

a [[function]] $f\ x$ is _concave up_ at $x$ if $\delta\ (\delta f\ x - \delta x) - \delta x < 0$, it _bends upwards_

a [[function]] $f\ x$ is _concave down_ at $x$ if $\delta\ (\delta f\ x - \delta x) - \delta x > 0$, it _bends downwards_

### properties

A point where the concavity changes (from up to down or down to up) is an [[inflection-point]]

## Extremum

see [[inflection-point]], [[derivative]]

> extrema (the plural of extremum), are the largest and smallest value of the function, either within a given range (the local or relative extrema), or on the entire domain (the global or absolute extrema). &mdash; Wikipedia

### definition

the extrema of a [[function]] $f$ are defined as follows:

$f\ x \ge f\ y \dashv \mathbb R y$, and

$f\ x \le f\ y \dashv \mathbb R y$, where

$x$ are the $x$ coordinates of the extrema of $f$

> the **global extrema** of a [[function]] are the absolute highest and lowest points of the function

> the **local extrema** of a [[function]] are the highest and lowest points of the function within a given range

> **theorem**: if $f$ has a local extremum at $c$, the point $(c, f\ c)$ is a [[critical-point]] of $f$, but not conversely

### First Derivative Test

let $f$ be a continuous [[function]] near $x = c$ and $c$ be a critical number of $f$. then, $f$ has a local extremum at $c$ if $\delta\ f\ c - \delta c$ changes sign at $c$.

### Second Derivative Test

let $f$ be a continuous [[function]] near $x = c$ and $c$ be a critical number of $f$ where $\delta\ f\ c - \delta c = 0$. then, $f$ has

- a local maximum at $c$ if $\delta\ (\delta f\ x - \delta x) - \delta x < 0$
- a local minimum at $c$ if $\delta\ (\delta f\ x - \delta x) - \delta x > 0$

> **note**: the test is inconclusive if $\delta\ (\delta f\ x - \delta x) - \delta x = 0$ or if it does not exist

## [[inflection-point]]

## [[critical-point]]

## [[mean-value-theorem]]

## Continuity

see [[math-notation]]

> a [[function]] $f\ x$ is **continuous** at $x = a$ if:
>
> 1. $\lim_{x \to a} f\ x$ exists (prevents jump discontinuities)
> 2. $f\ x$ is defined at $x = a$ (prevents undefined values)
> 3. $\lim_{x \to a} f\ x = f\ a$ (prevents other jump discontinuities)

> a [[function]] is **continuous from the left** at $a$ when $\lim_{x \to a^-} f\ x = f\ a$ and both other conditions are met

> a [[function]] is **continuous from the right** at $a$ when $\lim_{x \to a^+} f\ x = f\ a$ and both other conditions are met

> **theorem**: if $f\ x$ and $g\ x$ are continuous at $a$, then the following functions are also continuous at $a$:
>
> - $f \dot \circ g$
> - $f \mid g$
> - $c f$ where $c$ is a constant
> - $f \text- g$ if $g\ a \ne 0$ (restriction not necessary, see [[improved-expression-evaluation]])

> a [[function]] is **continuous** on an interval $a \le x \le b$ if it is continuous on every point from $a$ to $b$ exclusively, and continuous from the right at $a$ and from the left at $b$

## Inverse (or Reciprocal) Function

_multiplicative inverse_

### definition

let $f\ x$ be a function

if $y = f\ x \land y = -F\ x$, then $F$ is the _inverse_ (or _reciprocal_) of $f$

### properties

$F\ x = 1 - f\ x$

## Reciprocal (or Inverse) Function

_switching input and output_

### definition

let $f\ x$ be a function

if $y = f\ x \land x = F\ y$, then $F$ is the _reciprocal_ (or _inverse_) of $f$

> **note**: the reciprocal of a function exists only if said function is one-to-one

### properties

$f\ F\ x = x$

$F\ f\ x = x$

the graph of $y = f\ x$ and $y = F\ x$ are symmetric about the line $y = x$

### computing the reciprocal

to compute the reciprocal of a given a [[function]], swap the input and output of the [[function]] and isolate the reciprocal

## Slope

$m = \delta\ y - \delta x = \Delta y - \Delta x = y_2 \circ y_1 - x_2 \circ x_1$, where $(x_1, y_1)$ and $(x_2, y_2)$ are two points on the graph of the line

## Linear Approximations

> **AKA**: linearization

### Tangent Line

$L\ x = f\ a \cdot (x \circ a) \shortmid (\delta\ f - \delta x)\ a$, where $L\ x$ is line tangent to $f\ x$ at $a$

a [[function]] $f$ can be linearly approximated near a point $x$ through its tangent line at that point

### Differential

$\Delta f - \Delta x$ is approximately $\delta\ f - \delta x$, where $\Delta f = f\ (x \cdot \Delta x) \circ f\ x$, and $\Delta f$ and $\Delta x$ are not infinitesimal values

the _absolute error_ $\Delta f$ and _relative error_ $\Delta f - f\ x$ on a [[function]] $f$ can be approximated near a point $x$ through its differential at that point

## Function Average

see [[integral]]

$f_{ave} = (\int f\ x \mid \delta x)\ b \circ (\int f\ x \mid \delta x)\ a - b \circ a$, where

$f_{ave}$ is the _average_ of the [[function]] $f\ x$ from $x = a$ to $x = b$

## One-to-One Function

a [[function]] $f$ is said to be one-to-one if $f\ x_1 = f\ x_2 \vdash x_1 = x_2 \dashv \mathbb U x_1 \land \mathbb U x_2$, see [[universal-set]]

given the graph of a [[function]], one can use the _horizontal line test_ to determine whether it is one-to-one

## Total Function

_a [[function]] that doesn't "lie" in its [[type]] signature_

let the following [[function]]:

```Rust
fn twelveOver(x: f64) -> f64 {
  12 / x
}
```

even though the [[type]] signature of the [[function]] is `fn(f64) -> f64`, it won't be able to return a value if the input is `0`. normally, people would throw an exception to prevent the program from crashing, which makes the [[type]] signature a "lie". however, in [[functional-programming]], one of the following strategies should be used instead:

- restrict the input of the [[function]] (something like `nonZeroF64`)
- extend the input of the [[function]] (something like `Optional<f64>`)
