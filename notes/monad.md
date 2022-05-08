# Monad

see [[functional-programming]], [[return]], [[bind]]

a [[monad]]:

- is an [[effect-type]]
- has a [[return]] [[function]] (sometimes called `pure`, `unit`)
- has a [[bind]] [[function]] (sometimes called `>>=`, `flatMap`, `SelectMany`) that converts a "diagonal" function ("world-crossing", that goes from "normal" world to "effects" world) into a "horizontal" function (in the "effects" world only)
- must have a sensible implementation following the Monad laws

## Kleisli Composition

_an alternative to the [[bind]] [[function]]_

the Kleisli Composition (sometimes called `>=>`) is an alternative to the [[bind]] [[function]] that uses [[function-composition]] to turn two "world-crossing" [[function]]s into a single "world-crossing" [[function]] by short-circuiting their alternative outputs (see [[bind]])

Kleisli Composition is a [[monoid]]
