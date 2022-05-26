# Function

## types

[[boolean-function]]

[[rational-function]]

[[function-vector-space]]

[[piecewise-function]]

[[pure-function]]

[[trigonometric-function]]

## applications

[[curve-sketching]]

[[optimizing-a-function]]

[[functional-programming]]

## operations

see [[function-vector-space]], [[vector-space]]

### Zero Function

$O x = 0 \dashv \mathbb R x$

### Function Addition

$(f \cdot g)\ x = f\ x \cdot g\ x$

### Multiplication by a Scalar

$(cf)\ x = c\ |\ f\ x$

## [[even-function]]

## [[odd-function]]

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
> - $f'g$
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
