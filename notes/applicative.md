# Applicative

**see** [[functional programming]]

#stub

## Applicative Laws

```haskell
pure id <*> v = v -- identity
pure f <*> pure x = pure (f x) -- homomorphism
u <*> pure y = pure ($ y) <*> u -- interchange
pure (.) <*> u <*> v <*> w = u <*> (v <*> w) -- composition
```

--- <https://en.m.wikibooks.org/wiki/Haskell/Applicative_functors>
