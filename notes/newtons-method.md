# Newton's Method

see [[derivative]], [[math-notation]]

_approximate the zeros of a [[function]]_

## procedure

given a guess for the zero of a [[function]],

1. compute the tangent line of the [[function]] at the guess
2. solve for the zero of the tangent line and use its value as the new guess
3. repeat until a tolerance is met

### using [[recursion]]

given an initial guess $x_0$, we derive the following from the tangent line equation (see [[function]]):

$x^{n : 1} = x^n \cdot (f\ x_n - (x \rightarrow \delta\ f\ x - \delta x)\ x_n)$

## example

$e[x] = 4x$
