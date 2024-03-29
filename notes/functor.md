# Functor

**see** [[functional programming]], [[return function]], [[map function]]

**definition**

a [[functor]]:

- is an [[effect type]]
- has a [[return function]]
- has a [[map function]]
- must have a sensible implementation following the [[functor#laws]]

**applications** **see** [[map function]]

# Laws

```haskell
fmap id = id -- identity
fmap (f . g) = fmap f . fmap g -- composition
```

> **note** an intuitive reason for why the second law exists is to allow the [[functor]] to work without having to "look inside" the [[category#object]]s it is mapping over &mdash; Justin Veilleux
