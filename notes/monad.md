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

## Free Monad

--- <https://stackoverflow.com/questions/13352205/what-are-free-monads>

**see** [[semigroup#free semigroup]], [[monoid#free monoid]]

> **resource** _Why free monads matter_, and a motivation for wanting a [[monad]] that doesn't compute --- [[Haskell for all_ Why free monads matter.pdf]] --- <https://www.haskellforall.com/2012/06/you-could-have-invented-free-monads.html>

> **resource** _Beyond Free Monads_ by John DeGoes at λC Winter Retreat 2017, with a focus on free [[monad]]s for I/O --- <https://youtu.be/A-lmrvsUi2Y>

> **resource** the `Free` and `Cofree` types in the PNLC prelude --- <https://github.com/Bricktech2000/PNLC/blob/master/prelude.pnlc>

[[monad#free monad]]s are a general way of turning [[functor]]s into [[monad]]s

_A Monad is something that "computes" when monadic context is collapsed by `join :: m (m a) -> m a` (recalling that `>>=` can be defined as `x >>= y = join (fmap y x)`). This is how Monads carry context through a sequential chain of computations: because at each point in the series, the context from the previous call is collapsed with the next. A **free monad** satisfies all the Monad laws, but does not do any collapsing (i.e., computation). It just builds up a nested series of contexts. The user who creates such a free monadic value is responsible for doing something with those nested contexts, so that the **meaning** of such a composition can be deferred until after the monadic value has been created._ --- <https://stackoverflow.com/questions/13352205/what-are-free-monads>

## Kleisli Composition

_composes two diagonal [[function]]s into a single diahonal [[function]]_

**aka** _`>=>`_, _fish operator_, _Kleisli operator_

**definition** `(>=>) :: Monad m => (a -> m b) -> (b -> m c) -> a -> m c`

**definition** _in terms of the [[monad#bind]]_ given [[function]]s `f :: a -> m b` and `g :: b -> m c`, we have `kleisli f g a = f a >>= g`

```haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b -- monadic bind
(>=>) :: Monad m => (a -> m b) -> (b -> m c) -> a -> m c -- kleisli composition
f >=> g = \x -> f x >>= g -- kleisli composition in terms of monadic bind
ma >>= f = (id >=> f) ma -- monadic bind in terms of kleisli composition
```

diagonal [[function]]s of [[type]] `a -> m a` with the [[monad#kleisli composition]] form a [[monoid]] whose [[monoid#identity element]] is the [[applicative#pure]] function

### as a category

--- <https://wiki.haskell.org/index.php?title=Monad_laws#Is_that_really_an_%22associative_law%22?>

diagonal [[function]]s of [[type]] `a -> m b` with the [[monad#kleisli composition]] form a [[category]] whose [[category#identity morphism]]s are [[applicative#pure]] functions

when stating the [[monad#laws]] using [[monad#kleisli composition]]s, we get exactly the [[category]] laws:

```haskell
return >=> h = h -- left identity
f >=> return = f -- right identity
(f >=> g) >=> h = f >=> (g >=> h) -- associativity
```

_Monad axioms: Kleisli composition forms a category._ --- <https://wiki.haskell.org/index.php?title=Monad_laws>

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
