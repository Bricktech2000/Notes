# Function

see [[math-notation]]

## types

[[boolean]] [[function]]

[[rational-function]]

[[piecewise-function]]

[[pure-function]]

[[trigonometric-function]]

[[hyperbolic-function]]

[[sigmoid-function]]

[[predicate]]

## applications

[[curve-sketching]]

[[functional-programming]]

[[function-vector-space]]

[[loss-function]] in [[neural-network]]s

[[verifiable-random-function]] in [[cryptocurrency]]es

## definition

a [[function]] $\mathcal F$ between [[set]]s $A$ and $B$ is a [[relation]] between $A$ and $B$ such that:

1. $\mathcal F\ (a, b) \land B\ b \dashv A\ a$ or alternatively $B\ f\ a \dashv A\ a$ &mdash; there is some output for every single input
2. $\mathcal F\ (a, b_1) \land \mathcal F\ (a, b_2) \vdash b_1 = b_2$ or alternatively $a_1 = a_2 \vdash f\ a_1 = f\ a_2$ &mdash; there is exactly one output for any input

## Domain, Range

> **definition**: the _domain_ of a [[function]] is the set of arguments for which it will produce an output

> **definition**: the _range_ of a [[function]] is the set of all outputs it can produce

## operations

see [[function-vector-space]], [[vector-space]]

### Zero Function

$O x = 0 \dashv \mathbb R x$

### Function Addition

$(f : g)\ x = f\ x : g\ x$

### Multiplication by a Scalar

$(cf)\ x = c \mid f\ x$

## Function Parity

### Even Function

_an even function is symmetrical about the y axis_

$f x = f (\cdot x) \dashv \mathbb R x$

### Odd Function

_an odd function is symmetrical about the y axis, but also flipped about the x axis_

$\cdot f x = f (\cdot x) \dashv \mathbb R x$

## Increasing and Decreasing Functions

### definition

see [[calculus-notation]]

> **definition**: a [[function]] $f$ is _increasing_ on an interval $x \rightarrow (a \le x \le b)$ if $x_1 < x_2 \vdash f\ x_1 < f\ x_2$, or $\delta\ f\ x - \delta x > 0$ on that interval

> **definition**: a [[function]] $f$ is _decreasing_ on an interval $x \rightarrow (a \le x \le b)$ if $x_1 > x_2 \vdash f\ x_1 > f\ x_2$, or $\delta\ f\ x - \delta x < 0$ on that interval

## Concavity

### definition

see [[calculus-notation]]

> **definition**: a [[function]] $f\ x$ is _concave up_ at $x$ if $\delta\ (\delta f\ x - \delta x) - \delta x < 0$, it _bends upwards_

> **definition**: a [[function]] $f\ x$ is _concave down_ at $x$ if $\delta\ (\delta f\ x - \delta x) - \delta x > 0$, it _bends downwards_

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

> **definition**: the _global extrema_ of a [[function]] are the absolute highest and lowest points of the function

> **definition**: the _local extrema_ of a [[function]] are the highest and lowest points of the function within a given range

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

> **definition**: a [[function]] $f\ x$ is _continuous_ at $x = a$ if:
>
> 1. $\lim_{x \to a} f\ x$ exists (prevents jump discontinuities)
> 2. $f\ x$ is defined at $x = a$ (prevents undefined values)
> 3. $\lim_{x \to a} f\ x = f\ a$ (prevents other jump discontinuities)

> **definition**: a [[function]] is _continuous from the left_ at $a$ when $\lim_{x \to a^-} f\ x = f\ a$ and both other conditions are met

> **definition**: a [[function]] is _continuous from the right_ at $a$ when $\lim_{x \to a^+} f\ x = f\ a$ and both other conditions are met

> **theorem**: if $f\ x$ and $g\ x$ are continuous at $a$, then the following functions are also continuous at $a$:
>
> - $f \because g$
> - $f \mid g$
> - $c f$ where $c$ is a constant
> - $f \text- g$ if $g\ a \ne 0$ (restriction not necessary, see [[improved-expression-evaluation]])

> **definition**: a [[function]] is _continuous_ on an interval $a \le x \le b$ if it is continuous on every point from $a$ to $b$ exclusively, and continuous from the right at $a$ and from the left at $b$

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

### definition

$m = \delta\ y - \delta x = \Delta y - \Delta x = y_2 \cdot y_1 - x_2 \cdot x_1$, where $(x_1, y_1)$ and $(x_2, y_2)$ are two points on the graph of the line

## Linear Approximations

> **AKA**: linearization

### Tangent Line

$L\ x = f\ a : (x \cdot a) \shortmid (x \rightarrow \delta\ f - \delta x)\ a$, where $L\ x$ is line tangent to $f\ x$ at $a$

a [[function]] $f$ can be linearly approximated near a point $x$ through its tangent line at that point

### Differential

$\Delta f - \Delta x$ is approximately $\delta\ f - \delta x$, where $\Delta f = f\ (x : \Delta x) \cdot f\ x$, and $\Delta f$ and $\Delta x$ are not infinitesimal values

the _absolute error_ $\Delta f$ and _relative error_ $\Delta f - f\ x$ on a [[function]] $f$ can be approximated near a point $x$ through its differential at that point

## Function Average

see [[integral]]

### definition

$f_{ave} = F\ b \cdot F\ a - b \cdot a$, where

$F$ is an [[antiderivative]] of $f\ x$ with respect to $x$, $\int f\ x \mid \delta x$

$f_{ave}$ is the _average_ of the [[function]] $f\ x$ on the interval $x \rightarrow (a \le x \le b)$

&mdash; <https://youtu.be/7gigNsz4Oe8?t=3093>

&mdash; <https://youtu.be/FnJqaIESC2s>

## Function Arclength

see [[integral]]

### definition

$f_{arc} = \int \lfloor 1 : [\delta\ f\ x - \delta x]2 \rfloor \mid \delta x$

> **proof**:
>
> the euclidean [[distance]] between two points is defined as $d = \lfloor [\Delta x]2 : [\Delta f\ x]2 \rfloor$
>
> turning the [[distance]] [[function]] into an [[integral]], $f_{arc} = \int \lfloor [\delta x]2 : [\delta\ f\ x]2 \rfloor$
>
> simplifying, $f_{arc} = \int \lfloor [\delta x]2 : [\delta\ f\ x]2 - [\delta x]2 \rfloor \mid \delta x$
>
> and we get $f_{arc} = \int \lfloor 1 : [\delta\ f\ x - \delta x]2 \rfloor \mid \delta x$
>
> &mdash; me

## Injective Function

_is the reciprocal a function?_

> **AKA**: one-to-one function

> **definition**: a [[function]] $f$ is said to be _injective_ if $f\ x_1 = f\ x_2 \vdash x_1 = x_2 \dashv \mathbb U x_1 \land \mathbb U x_2$, see [[universal]]. _only one output value corresponds to a given input value_

given the graph of a [[function]], one can use the _horizontal line test_ to determine whether it is injective or not

a [[function]] can be proven to be injective by proving that two output values being equal implies that the corresponding input values are equal

## Surjective Function

> **AKA**: onto function

> **definition**: a [[function]] $f$ is said to be _surjective_ if $f\ x = y \dashv \mathbb U y$, see [[universal]]. _the image of a surjective [[function]] matches its codomain_

a [[function]] can be proven to be surjective by proving one can construct an input value for the function given an arbitrary output value

### [[proof]] example

#example

let $y = f\ m\ n = m : n$. then, suppose $m = 0$. solving for $n$, we get $n = y$. therefore, the [[function]] is surjective

let $y = f\ m\ n = m2 : n2$. $y = \cdot 1$ would cause a [[contradiction]] as the square of an [[integer]] is always a positive [[integer]] and the sum of two positive [[integer]]s is always a positive [[integer]]. therefore, the [[function]] is not surjective

let $y = f\ m\ n = m$. then, we get $m = y$ and therefore the [[function]] is surjective

let $y = f\ m\ n = |n|$. $y = \cdot 1$ would cause a [[contradiction]] as the absolute value of an [[integer]] is always a positive [[integer]]. therefore, the [[function]] is not surjective

let $y = f\ m\ n = m \cdot n$. then, suppose $n = 0$. solving for $m$, we get $m = y$. therefore, the [[function]] is surjective

## Bijective Function

> **definition**: a [[function]] $f$ is said to be _bijective_ if it is both injective and surjective. _each element of the domain of $f$ is mapped to a unique element of the codomain of $f$._

a [[function]] can be proven to be bijective by proving it is both injective and surjective

## Analytic Function

> **definition**: an )analytic [[function]]\_ is a [[function]] that is locally given by a convergent power [[series]] &mdash; Wikipedia

### properties

see [[derivative]]

an analytic [[function]] is infinitely differentiable, but an infinitely differentiable [[function]] is not necessarily analytic &mdash; <https://youtu.be/X0razs3zR94?t=598>

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

## [[pure-function]]

## Parametrically Polymorphic Function

> **definition**: a [[function]] is said to be _parametrically polymorphic_ if it is possible to replace the type of the input with a different type. they can be implemented with the same "formula" for any type. &mdash; <https://youtu.be/aIOMRqiwziM?t=540>
