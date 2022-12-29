# Newton's Method

**see** [[derivative]], [[math notation]]

_method to approximate the zeros of a [[function]]_

> **procedure** _using [[iteration]]_
>
> given a guess for the zero of a [[function]],
>
> 1. compute the [[function#tangent line]] of the [[function]] at the guess
> 2. solve for the zero of the [[function#tangent line]] and use its value as the new guess
> 3. repeat until a tolerance is met

> **procedure** _using [[recursion]]_
>
> given an initial guess $x^0$, we derive the following from the [[function#tangent line]] equation:
>
> $x^{n : 1} = x^n \cdot (f\ x^n - \delta\ f\ x^n \mid \delta x^n)$

> **example** the following equation can be solved easily using [[newton's method]]: $[x] = 4x$
