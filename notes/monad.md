# Monad

see [[functional-programming]], [[return]], [[bind]]

[[todo]]: <https://en.wikipedia.org/wiki/Monad_transformer>

a [[monad]]:

- is an [[effect-type]]
- has a [[return]] [[function]]
- has a [[bind]] [[function]] that converts a "diagonal" function ("world-crossing", that goes from "normal" world to "effects" world) into a "horizontal" function (in the "effects" world only)
- must have a sensible implementation following the Monad laws

## Kleisli Composition

_an alternative to the [[bind]] [[function]]_

> **AKA**: `>=>`

the Kleisli Composition is an alternative to the [[bind]] [[function]] that uses [[composition]] to turn two "world-crossing" [[function]]s into a single "world-crossing" [[function]] by short-circuiting their alternative outputs (see [[bind]])

Kleisli Composition is a [[monoid]]

## applications

see [[bind]]
