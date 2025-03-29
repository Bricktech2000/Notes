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

[[monad]]s are [[applicative]]s because the [[apply function]] can be defined in terms of the [[bind function]] and [[return function]]

## Kleisli Composition

_an alternative to the [[bind function]]_

**aka** _`>=>`_, _fish operator_, _Kleisli operator_

the Kleisli Composition is an alternative to the [[bind function]] that uses [[composition]] to turn two "world-crossing" [[function]]s into a single "world-crossing" [[function]] by short-circuiting their alternative outputs (see [[bind function]])

**properties**

a [[set]] of [[monad]]s with Kleisli Composition form a [[monoid]] whose [[monoid#identity element]] is the [[return function]]

## Transformer

monad transformer #todo <https://en.wikipedia.org/wiki/Monad_transformer> and <https://en.wikibooks.org/wiki/Haskell/Monad_transformers>

## Laws

--- <https://youtu.be/vhVG6sFeA58?t=3m50s>

--- <https://en.m.wikibooks.org/wiki/Haskell/Understanding_monads>

```haskell
return x >>= f = f x -- left identity
m >>= return = m -- right identity
(m >>= f) >>= g = m >>= (\x -> f x >>= g) -- associativity
```
