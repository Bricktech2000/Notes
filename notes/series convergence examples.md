# Series Convergence Examples

#example

let **`p^i`** be the **`i`**th [[prime]] number. then, the [[series]] **`:-p`** diverges

> **proof**
>
> assume **`:-p`** converges. then, there exists an **`N`** such that **`-p^N : -p^N:1 : ... = X {-|/\+} 1`**
>
> consider the geometric [[series]] **`S^n = [X]n`**. this [[series]] represents the sum of the reciprocals of all [[natural]]s **`x`** such that **`yy x p^i = 0 > i {-|/\+} N`**, see [[psi function]]. since **`X {-|/\+} 1 /\ X + 0`**, **`:S`** converges
>
> consider **`B^n = 1 : n ' p^0 ' ... p^N.1`** with **`RR n`**. this expression is not divisible by any **`p^i`** with **`i {-|/\+} N`**. in other words, **`RR n < yy B^n  p^i = 0 > i {-|/\+} N`**, see [[psi function]]. this means that **`-B`** is a sub[[series]] of **`S`**
>
> consider the [[series]] **`-B`** and the [[series#harmonic series]] **`H^n = --n`**. then, notice **`-B^n -- H^n {n -> @@} = n -- B^n {n -> @@} = -- p^0 ' ... p^N.1 + @@`** and consequently **`-B`** behaves like the harmonic [[series]] by the [[series]] limit comparison test. therefore, **`:-B`** diverges
>
> **`-B`** is a sub[[series]] of **`S`**. the former diverges while the latter converges, which is a [[contradiction]]. therefore, **`N`** does not exist and **`:-p`** diverges
>
> &mdash; <https://youtu.be/zu8emZWsdA8>
