# Recursion

see [[recursion]]

**definition** _Recursion_ is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. &mdash; Wikipedia

> **example** _common recursion pattern_
>
> 1. implement a base case
> 2. solve one layer of the problem and call recursively
> 3. restore invariants
>
> > **note** invariants are used in recursive [[algorithm]]s that must mutate their parameters to work properly. this is the reason why invariant parameters must be restored before exiting the [[function]]
>
> &mdash; <https://youtu.be/jUM_Dpt6yu0?t=477>

## General Recursion

any [[algorithm]] that uses [[recursion]] can be represented as repeated [[function]] [[composition]]

$\operatorname{rec} f = f\ (\operatorname{rec} f)$, which evaluates to $f\ f\ f\ f\ \dots$

&mdash; <https://youtu.be/9T8A89jgeTI?t=482>
