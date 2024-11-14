# Halting Problem

**see** [[turing machine]], [[lambda calculus]]

the [[halting problem]] is is _undecideable_. that is, there exists no general [[algorithm]] that can determine whether an arbitrary program halts

> **proof** (that doesn't prove much of anything but gives an intuition)
>
> ```python
> # assume there exists a general algorithm that can determine whether
> # an arbitrary program halts
> import halts
>
> # then, define the following adversarial program `p`
> def p(q):
>   if halts(q(q)):
>     while True:
>       pass
>
> # finally, consider the program `p(p)`. it halts if and only if
> # it doesn't halt; a contradiction. therefore, the assumption that
> # `halts` exists must be incorrect
> ```
