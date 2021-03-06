# Monad

see [[functional-programming]], [[return]], [[bind]], [[join]]

## definition

a [[monad]]:

- is an [[effect-type]]
- has a [[return]] [[function]]
- has a [[bind]] or a [[join]] [[function]], or both
- must have a sensible implementation following the Monad laws

## applications

see [[bind]]

## properties

[[monad]]s are [[functor]]s.

let a [[function]] `f :: a -> b` and a [[monad]] `ma = M a`. then, `f` can be [[map]]ped to that [[monad]] using only [[bind]] and [[return]] and [[function]] [[composition]] as follows:

`map :: (a -> b) -> M a -> M b`

`map f ma = bind (return . f) ma`

&mdash; me, DM with Simon

## Kleisli Composition

_an alternative to the [[bind]] [[function]]_

> **AKA**: `>=>`, fish operator, Kleisli operator

the Kleisli Composition is an alternative to the [[bind]] [[function]] that uses [[composition]] to turn two "world-crossing" [[function]]s into a single "world-crossing" [[function]] by short-circuiting their alternative outputs (see [[bind]])

Kleisli Composition is a [[monoid]]

## Monad Transformer

#todo

<https://en.wikipedia.org/wiki/Monad_transformer>
