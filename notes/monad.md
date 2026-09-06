# Monad

**see** [[functional programming]]

```haskell
join m = m >>= id         -- join in terms of bind
m >>= f = join $ fmap f m -- bind in terms of join
```

--- <https://youtu.be/3ynPUN64eTA?t=8m5s>

## Free Monad

--- <https://stackoverflow.com/questions/13352205/what-are-free-monads>

**see** [[semigroup#free semigroup]], [[monoid#free monoid]]

> **resource** _Why free monads matter_, and a motivation for wanting a [[monad]] that doesn't compute --- [[Haskell for all_ Why free monads matter.pdf]] --- <https://www.haskellforall.com/2012/06/you-could-have-invented-free-monads.html>

> **resource** _Beyond Free Monads_ by John DeGoes at λC Winter Retreat 2017, with a focus on free [[monad]]s for I/O --- <https://youtu.be/A-lmrvsUi2Y>

> **resource** the `Free` and `Cofree` types in the PNLC prelude --- <https://github.com/Bricktech2000/PNLC/blob/master/prelude.pnlc>

[[monad#free monad]]s are a general way of turning [[functor]]s into [[monad]]s

_A Monad is something that "computes" when monadic context is collapsed by `join :: m (m a) -> m a` (recalling that `>>=` can be defined as `x >>= y = join (fmap y x)`). This is how Monads carry context through a sequential chain of computations: because at each point in the series, the context from the previous call is collapsed with the next. A **free monad** satisfies all the Monad laws, but does not do any collapsing (i.e., computation). It just builds up a nested series of contexts. The user who creates such a free monadic value is responsible for doing something with those nested contexts, so that the **meaning** of such a composition can be deferred until after the monadic value has been created._ --- <https://stackoverflow.com/questions/13352205/what-are-free-monads>

## Continuation Monad

**see** [[continuation]]

the [[monad#continuation monad]] is universal in the sense that all [[monad]]s can be embedded in it. after all, the right-hand side of `>>=` is a [[continuation]].

```haskell
import Control.Monad.Cont

embed x = cont (x >>=)
reify x = runCont x return

list = reify $ do
  x <- embed [0, 2]
  y <- embed [0, 1]
  return $ x + y
```

and thus _[...] given any language with a syntax for [[continuation]]s you have the possibility of reusing that notation for [[monad]]s. For example [[python]] has linear [[continuation]]s (via generators) so you can use this as a syntax for any of the 'linear' [[monad]]s (like `Identity`, `Maybe` and `Writer` I think)_ --- [[A Neighborhood of Infinity_ The Mother of all Monads.pdf]] --- <https://blog.sigfpe.com/2008/12/mother-of-all-monads.html>

--- me; and

--- _The essence of functional programming_ (Philip Wadler, 1992), $3.3 _Monads and CPS_ (have only read that section) --- [[143165.143169.pdf]] --- <https://dl.acm.org/doi/10.1145/143165.143169>

--- [[A Neighborhood of Infinity_ The Mother of all Monads.pdf]] --- <https://blog.sigfpe.com/2008/12/mother-of-all-monads.html>

## Kleisli Composition

**aka** _`>=>`_ in Haskell

```haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b             -- monadic bind
(>=>) :: Monad m => (a -> m b) -> (b -> m c) -> a -> m c -- kleisli composition
f >=> g = \x -> f x >>= g -- kleisli composition in terms of monadic bind
ma >>= f = (id >=> f) ma  -- monadic bind in terms of kleisli composition
```

a _Kleisli endomorphism_ is a [[function]] `:: Monad m => a -> m a`. Kleisli [[morphism#endomorphism]]s under [[monad#kleisli composition]] form a [[monoid]] with [[monoid#identity element]] `return :: a -> m a`

### as a category

--- <https://wiki.haskell.org/index.php?title=Monad_laws#Is_that_really_an_%22associative_law%22?>

a _Kleisli arrow_ is a [[function]] `:: Monad m => a -> m b`. Kleisli arrows under [[monad#kleisli composition]] form a [[category]] whose [[category#identity morphism]]s are `return`s

when stating the [[monad#monad laws]] using [[monad#kleisli composition]]s, we get exactly the [[category]] laws:

```haskell
return >=> h = h -- left identity
f >=> return = f -- right identity
(f >=> g) >=> h = f >=> (g >=> h) -- associativity
```

_Monad axioms: Kleisli composition forms a category._ --- <https://wiki.haskell.org/index.php?title=Monad_laws>

## Monad Transformer

monad transformer #todo <https://en.wikipedia.org/wiki/Monad_transformer> and <https://en.wikibooks.org/wiki/Haskell/Monad_transformers>

## Monad Laws

```haskell
return x >>= f = f x -- left identity
m >>= return = m -- right identity
(m >>= f) >>= g = m >>= (\x -> f x >>= g) -- associativity
```

--- <https://youtu.be/vhVG6sFeA58?t=3m50s>

--- <https://en.m.wikibooks.org/wiki/Haskell/Understanding_monads>
