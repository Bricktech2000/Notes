# Functional Programming

**see** [[functor]], [[applicative]], [[monad]]

**see** [[pure]], [[currying]], [[type]], [[recursion#recursion scheme]], [[continuation]], [[combinatory logic]], [[lambda-calculus]], [[type-driven design]]

> **resource** _A sliding scale of power_, an intuition for `Functor a => Applicative a => Monad a` --- [[../references/Haskell_Applicative functors - Wikibooks.pdf]] --- <https://en.wikibooks.org/wiki/Haskell/Applicative_functors#A_sliding_scale_of_power>
>
> ``` haskell
> (<$>) :: Functor     t =>   (a ->   b) -> (t a -> t b)
> (<*>) :: Applicative t => t (a ->   b) -> (t a -> t b)
> (=<<) :: Monad       t =>   (a -> t b) -> (t a -> t b)
> ```

> **resource** the _Typeclassopedia_, a introduction to the standard Haskell type classes --- <https://wiki.haskell.org/Typeclassopedia> and [[../references/Typeclassopedia.pdf]] --- <https://wiki.haskell.org/wikiupload/e/e9/Typeclassopedia.pdf>

**properties**

[[functional programming]] is both _procedural_ and _functional_, see [[programming paradigm]]

## ---

--- <https://youtu.be/Nrp_LZ-XGsY>

--- <https://youtu.be/srQt1NAHYC0>
