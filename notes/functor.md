# Functor

**see** [[functional programming]], [[return function]], [[map function]]

**definition**

a [[functor]]:

- is an [[effect type]]
- has a [[return function]]
- has a [[map function]]
- must have a sensible implementation following the [[functor#laws]]

**equiv** _[[category#functor]]_ the [[return function]] is the map for [[category#object]]s, the [[map function]] is the map for [[category#morphism]]s, the identity [[functor#law]] preserves the [[category#identity law]] and the composition [[functor#law]] preserves [[category#composition]]

**applications** **see** [[map function]]

**properties**

[[monad]]s generalize [[functor]]s

[[applicative]]s generalize [[functor]]s

# Laws

```haskell
fmap id = id -- identity
fmap (f . g) = fmap f . fmap g -- composition
```

> **note** an intuitive reason for why the second law exists is to allow the [[functor]] to work without having to "look inside" the [[category#object]]s it is mapping over --- Justin Veilleux
