# Functor

**see** [[functional programming]]

## Functor Laws

```haskell
fmap id = id -- identity
fmap (f . g) = fmap f . fmap g -- composition
```

## Base Functor

**see** [[recursion#recursion scheme]], [[monad#free monad]]

**aka** _pattern functor_, _signature functor_

```haskell
data List  a   = Cons a (List a) | Nil -- a recursive type
data ListF a r = Cons a r        | Nil -- its base functor
```

`Fix (ListF a) ~= List a`---the [[fixed point]] of the [[functor#base functor]] is isomorphic to the recursive [[type]]
