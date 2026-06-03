# Functional Programming

**see** [[effect type]], [[functor]], [[applicative]], [[monad]], [[monoid]]

**see** [[pure]], [[currying]], [[type]], [[recursion#scheme]], [[combinatory logic]], [[lambda-calculus]], [[type-driven design]]

> **resource** _A sliding scale of power_, an intuition for `Functor a => Applicative a => Monad a` --- <https://en.wikibooks.org/wiki/Haskell/Applicative_functors#A_sliding_scale_of_power>
>
> ``` haskell
> (<$>) :: Functor     t =>   (a ->   b) -> (t a -> t b)
> (<*>) :: Applicative t => t (a ->   b) -> (t a -> t b)
> (=<<) :: Monad       t =>   (a -> t b) -> (t a -> t b)
> ```

> **resource** the _Typeclassopedia_, a introduction to the standard Haskell type classes --- <https://wiki.haskell.org/Typeclassopedia> and [[Typeclassopedia.pdf]] --- <https://wiki.haskell.org/wikiupload/e/e9/Typeclassopedia.pdf>

**properties**

[[functional programming]] is both _procedural_ and _functional_, see [[programming paradigm]]

## ---

--- <https://youtu.be/Nrp_LZ-XGsY>

--- <https://youtu.be/srQt1NAHYC0>

--- <https://youtu.be/c_F1o_so2MQ>

--- <https://youtu.be/oDdXep6yTOM> and <https://youtu.be/hDO3lpAcF2I>
