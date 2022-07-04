# Type Theory

see [[type]]

values in [[type-theory]] are [[type]]s

## assumptions

> - some idea of abstract syntax with bindings and scope (substitution for variables)
>
> forms of expression:
>
> - `E` is an expression
>
> judgement forms:
>
> - `E val` means that `E` is fully evaluated (`tt val`, `ff val` to define booleans)
> - `E -> E'` means one step of simplification of `E` according to a _deterministic rule_
>
> derived notion:
>
> - `E => E0` (or `E => V`) means `E -> ... -> E0 val`
