# Applicative

**see** [[functional programming]], [[return function]], [[apply function]]

**definition**

an [[applicative]]:

- is an [[effect type]]
- has a [[return function]], often called `of` or `pure`
- has an [[apply function]], often called `ap` or `<*>`
- must have a sensible implementation following the [[applicative#laws]]

**applications** **see** [[apply function]]

**properties**

[[applicative]]s are [[functor]]s because the [[map function]] can be defined in terms of the [[apply function]] and [[return function]]

[[monad]]s generalize [[applicative]]s

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
