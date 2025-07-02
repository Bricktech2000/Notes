# Monad

**see** [[functional programming]]

**definition** a _monad_ is an [[effect type]] that has an [[applicative#pure]] and either a [[monad#join]] or a [[monad#bind]] that uphold the [[monad#laws]]

**properties**

[[monad]]s are [[functor]]s because the [[functor#map]] can be defined in terms of the [[monad#bind]] and [[applicative#return]]: given [[function]] `f :: a -> m b` and [[monad]] `ma`, we have `fmap f ma = ma >>= (return . f)` --- me, Simon Discord DM

[[monad]]s are [[applicative]]s because the [[applicative#apply]] can be defined in terms of the [[monad#bind]] and [[functor#map]]: given [[function]] `mf :: m (a -> b)` and [[monad]] `ma`, we have `apply mf ma = mf >>= \f -> (fmap f ma)` --- <https://youtu.be/caSOTjr1z18?t=21m12s> and me

## Join

_turns a nested [[effect type]] into a normal [[effect type]]_

**aka** _`flatten`_ in Rust

**definition** `join :: Monad m => m (m b) -> m b`

**definition** _in terms of the [[monad#bind]]_ given the [[function#identity]] `id` and [[monad]] `mmb`, we have `join mmb = mmb >>= id`

## Bind

_turns a diagonal [[function]] into horizontal [[function]] in the effects world_

**aka** _`>>=`_, _`flatMap`_, _`SelectMany`_, _Sequential Composition_, _`and_then`_ in Rust

**definition** `(>>=) :: Monad m => m a -> (a -> m b) -> m b`

**definition** _in terms of the [[monad#join]]_ given [[function]] `f :: a -> m b` and [[monad]] `ma`, we have `bind f ma = join (fmap f ma)` --- Simon and <https://youtu.be/3ynPUN64eTA?t=8m5s>

**applications**

let a [[function]] `f` that takes as input [[type]] `T` and returns an [[effect type]] `E<e>`. "connecting" the output of one of such functions to the input of another is an issue, as `f` has one input `T` but multiple outputs `E<e>` (`Some` and `None` with `Option<T>`, "Done" and "Not Done" with `Async`, etc.)

this often leads to deeply nested `if` checks with [[null]] values in languages like [[c]] and [[java]] or deeply nested callbacks in languages like [[javascript]]

the [[monad#bind]] fixes this issue by providing a way to connect the meaningful output of such [[function]]s to the input of the next one and to short-circuit the alternative output. it makes "world-crossing" [[function]]s composable by turning them into "effects-world"-only [[function]]s

> **note** the name `flatMap` comes from the fact that the [[monad#bind]] can be defined as the [[function#composition]] of the [[monad#join]] and [[functor#map]] --- <https://youtu.be/C2w45qRc3aU?t=808>

## Kleisli Composition

_composes two diagonal [[function]]s into a single diahonal [[function]]_

**aka** _`>=>`_, _fish operator_, _Kleisli operator_

**definition** `(>=>) :: Monad m => (a -> m b) -> (b -> m c) -> a -> m c`

**definition** _in terms of the [[monad#bind]]_ given [[function]]s `f :: a -> m b` and `g :: b -> m c`, we have `kleisli f g a = f a >>= g`

diagonal [[function]]s of [[type]] `a -> m a` with the [[monad#kleisli composition]] form a [[monoid]] whose [[monoid#identity element]] is the [[applicative#pure]] function

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
