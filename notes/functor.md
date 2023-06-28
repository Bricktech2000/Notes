# Functor

**see** [[functional programming]], [[return function]], [[map function]]

**definition**

a [[functor]]:

- is an [[effect type]]
- has a [[return function]]
- has a [[map function]]
- must have a sensible implementation following the [[functor#laws]]

> **equivalence** _[[functor]] [[return function]] and map between [[category#object]]s_

> **equivalence** _[[functor]] [[map function]] and map between [[category#morphism]]s_

see [[map function]] for applications

# Laws

```haskell
fmap id = id
fmap (f . g) = fmap f . fmap g
```

> **note** an intuitive reason for why the second law exists is that is allows the [[functor]] to work without having to "look inside" the [[category#object]]s it is mapping over &mdash; Justin Veilleux
