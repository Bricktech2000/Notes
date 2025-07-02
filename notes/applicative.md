# Applicative

**see** [[functional programming]]

**definition** an _applicative_ is an [[effect type]] that has an [[applicative#pure]] and an [[applicative#apply]] that uphold the [[applicative#laws]]

**properties**

[[applicative]]s are [[functor]]s because the [[functor#map]] can be defined in terms of the [[applicative#apply]] and [[applicative#pure]]: given [[function]] `f :: a -> b` and [[applicative]] `fa` we have `fmap f fa = pure f <*> fa`

--- <https://github.com/fantasyland/static-land/blob/master/docs/spec.md#applicative>

--- <https://en.wikipedia.org/wiki/Applicative_functor>

## Pure

_lifts a value to the effects world_

**aka** _`pure`_, _`unit`_, _`of`_

**definition** `pure :: Applicative f => a -> f a`

## Apply

_applies a [[function]] in the effects world to a value in the effects world_

**aka** _`ap`_, _`<*>`_

**definition** `(<*>) :: Applicative f => f (a -> b) -> f a -> f b`

**examples**

> **example** `[f, g] <*> [1, 2]` will return `[f 1, f 2, g 1, g 2]`

> **example** `pure (+) <*> [1, 2, 3] <*> [4, 5, 6]` will return `[1 + 4, 1 + 5, 1 + 6, 2 + 4, 2 + 5, 2 + 6, 3 + 4, 3 + 5, 3 + 6]`

> **example** `Pair <$> (ma :: Maybe a) <*> (mb :: Maybe b) :: Maybe (Pair a b)` is a common pattern

## Laws

--- <https://youtu.be/caSOTjr1z18?t=20m43s>

--- <https://en.m.wikibooks.org/wiki/Haskell/Applicative_functors>

```haskell
pure id <*> v = v -- identity
pure f <*> pure x = pure (f x) -- homomorphism
u <*> pure y = pure ($ y) <*> u -- interchange
pure (.) <*> u <*> v <*> w = u <*> (v <*> w) -- composition
```

## ---

--- <https://youtu.be/s5S2Ed5T-dc?t=571>

--- <https://thedet.wordpress.com/2012/04/28/functors-monads-applicatives-can-be-so-simple/>

--- <https://youtu.be/Y0KKPYkeOTA?t=501>
