# Polymorphism

--- <https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>

## Ad Hoc Polymorphism

_[[trait]]s, type classes_

**definition** _ad hoc polymorphism_ allows a [[function]] to be applied to arguments of different [[type]]s, but behave differently depending on the [[type]] of the argument to which it is applied

## Parametric Polymorphism

_[[generic]]s_

**definition** _parametric polymorphism_ allows a [[function]] to be written generally so that it can handle values uniformly regardless of their [[type]]

a [[function]] is said to be _parametrically polymorphic_ if it is possible to replace the [[type]] of its input with a different [[type]] without having any effect on its behavior. such [[function]]s can be implemented with the same "formula" for any [[type]]. --- <https://youtu.be/aIOMRqiwziM?t=540>

## Subtype Polymorphism

_[[object-oriented programming]] inheritance and [[interface]]s, often [[type system#structural type system]]s_

**definition** _subtype polymorphism_ allows a [[function]] to be written to take an instance of a certain [[type]] and automatically work with instances of any [[type#subtype]] of that [[type]]

## Rank Polymorphism

**definition** _rank polymorphism_ allows a [[function]] to be polymorphic in the _rank_ of its arguments

> **example**
>
> $1 \lfloor\ \mathbb x$ in BQN (supports [[polymorphism#rank polymorphism]]) is equivalent to **`1 __ x`** in my [[math notation]] (supports [[polymorphism#rank polymorphism]]) which is equivalent to `map (map (min 1)) x` in Haskell (does not support [[polymorphism#rank polymorphism]])
>
> --- <https://youtu.be/8ynsN4nJxzU?t=812>

### ---

--- <https://youtu.be/8ynsN4nJxzU?t=612>

--- <https://prl.ccs.neu.edu/blog/2017/05/04/rank-polymorphism/>

--- <https://youtu.be/8Ab3ArE8W3s?t=659>
