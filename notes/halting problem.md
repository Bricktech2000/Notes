# Halting Problem

**see** [[turing machine]], [[lambda calculus]]

the [[halting problem]] is is _undecideable_. that is, no general [[algorithm]] exists that can determine whether a given program halts

> **proof** (that doesn't prove much of anything but gives an intuition)
>
> ```python
> # assume there exists a general algorithm that can determine
> # whether a given program halts
> import halts
>
> # then, define the following program `p`
> def p():
>   if halts(p):
>     while True:
>       pass
>
> # `p` will halt if and only if it doesn't halt; a contradiction.
> # therefore, the assumption that `halts` exists must be incorrect
> ```
