# Functional Programming

see [[functor]] & [[map]], [[monad]] & [[bind]], [[monoid]] & [[reduce]], [[effect-type]] & [[return]]

see [[currying]], [[partial-application]], [[pure-function]]

see [[function]], [[type]], [[composition]], [[apply]]

see [[refactoring-to-immutability]]

&mdash; <https://youtu.be/Nrp_LZ-XGsY>

&mdash; <https://youtu.be/srQt1NAHYC0>

## principles

[[function]]s are things

- they are meant to do one thing and do it well
- they are meant to work well with other [[function]]s

[[composition]] is used everywhere

- allows for [[abstraction]] and [[encapsulation]]

functional languages support [[first-class-function]]s

design for totality, see [[function]]

parameterize all the things, including **both** data and behavior

### consequences

as all [[function]]s are isolated from any other parts of a program, they can be combined to build larger functions without having to worry about anything breaking. this also allows for testability and reusability.

[[functional-programming]] [[function]]s and [[object-oriented-programming]] [[object]]s can be compared to Lego bricks, except bricks in [[object-oriented-programming]] are likely not going to fit with other bricks in the program, and all bricks are joined by strings and rubber bands wating to become a fragile tangled mess.
