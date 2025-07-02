# Functor

**see** [[functional programming]]

**definition** a _functor_ is an [[effect type]] that has a [[functor#map]] that upholds the [[functor#laws]]

## Map

_lifts a horizontal [[function]] to the effects world_

**aka** _`lift`_, _`select`_, _`fmap`_, _`<$>`_

**definition** `fmap :: Functor f => (a -> b) -> f a -> f b`

**applications**

[[functor#map]]s unwrap the inputs to a [[function]] before wrapping them back after execution, see [[effect type]]. let a [[function]] `let inc = |x| x + 1;` and a [[effect type]] `Option<T>`. `inc(1)` works fine, but `inc(Some(1))` will fail. it would be possible to work around this issue by defining a custom [[function]] to unwrap the optional [[type]], increment it, and wrap it back into an optional [[type]]. however, this is an antipattern in [[functional programming]]. ideally, we would want to stay in the "optional" world while using a value and unwrap it only after being done all operations. this is what [[functor#map]]s are for.

## Laws

```haskell
fmap id = id -- identity
fmap (f . g) = fmap f . fmap g -- composition
```

> **note** an intuitive reason for why the second law exists is to allow the [[functor]] to work without having to "look inside" the [[category#object]]s it is mapping over --- Justin Veilleux
