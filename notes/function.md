# Function

## types of functions

[[boolean-function]]

[[rational-function]]

[[function-vector-space]]

[[piecewise-function]]

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

## continuity

see [[math-notation]]

> a function is continuous at $a$ when $\lim_{x \to a} f\ x = f\ a$. both [[limit]]s must exist.

> a function is continuous **from the left** at $a$ when $\lim_{x \to a^-} f\ x = f\ a$. both [[limit]]s must exist

> a function is continuous **from the right** at $a$ when $\lim_{x \to a^+} f\ x = f\ a$. both [[limit]]s must exist

> **theorem**: if $f\ x$ and $g\ x$ are continuous at $a$, then the following functions are also continuous at $a$:
>
> - $f \dot \circ g$
> - $f'g$
> - $c f$ where $c$ is a constant
> - $f \text- g$ if $g\ a \ne 0$

## Inverse (or Reciprocal) Function

_multiplicative inverse_

### definition

let $f\ x$ be a function

if $y = f\ x \land y = 1 - f^-\ x$, then $f^-$ is the _inverse_ (or _reciprocal_) of $f$

### properties

$f^-\ x = 1 - f\ x$

## Reciprocal (or Inverse) Function

_switching input and output_

### definition

let $f\ x$ be a function

if $y = f\ x \land x = f^\times\ y$, then $f^\times$ is the _reciprocal_ (or _inverse_) of $f$

### properties

$f\ f^\times\ x = x$

$f^\times\ f\ x = x$

the graph of $y = f\ x$ and $y = f^\times\ x$ are symmetric about the line $y = x$

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
