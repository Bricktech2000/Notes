# Monad

**see** [[functional programming]], [[return function]], [[bind function]], [[join function]]

**definition** a [[monad]]:

- is an [[effect type]]
- has a [[return function]]
- has a [[bind function]] or a [[join function]], or both
- must have a sensible implementation following the [[monad#laws]]

**applications** **see** [[bind function]]

**properties**

[[monad]]s are [[functor]]s because the [[map function]] can be defined in terms of the [[bind function]] and [[return function]]

## Kleisli Composition

_an alternative to the [[bind function]]_

**aka** _`>=>`, fish operator, Kleisli operator_

the Kleisli Composition is an alternative to the [[bind function]] that uses [[composition]] to turn two "world-crossing" [[function]]s into a single "world-crossing" [[function]] by short-circuiting their alternative outputs (see [[bind function]])

**properties**

the [[set]] of [[monad]]s with Kleisli Composition form a [[monoid]]

## Transformer

monad transformer #todo <https://en.wikipedia.org/wiki/Monad_transformer>

## Laws

monad laws #todo
