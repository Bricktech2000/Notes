# Taylor Series

_allows for the approximation of a [[function]] near a point by a [[polynomial]]_

**see** [[calculus]], [[series]]

> **note** [[taylor series]] don't necessarily have an infinite radius of convergence, see [[series#power series]]
>
> as an example, the [[taylor series]] of the [[function]] **`/x\`** at **`a = 1`** has a radius of convergence of **`1`**, meaning the [[taylor series]] only converges to the [[function]] on the [[interval]] **`0 {-|/\+} * -| 2`**
>
> &mdash; <https://youtu.be/X0razs3zR94>

> **note** a [[taylor series]] with a nonzero radius of convergence does **not** necessarily converge to the [[function]] it approximates. for this to be the case, the [[function]] must be a [[function#analytic function]] &mdash; <https://youtu.be/X0razs3zR94> and <https://youtu.be/7gigNsz4Oe8?t=21781>
>
> [[taylor series#remainder]]s can be used to determine whether a [[taylor series]] converges to its underlying [[function]] or not.

**definition**

let **`f`** be a [[function]] and let **`T f`** such that **`T f a = f a /\ dd T f a = dd f a /\ dd dd T f a = dd dd f a /\ ...`**, where **`(a, f a)`** is the point of interest on **`f`** and **`T f`** is a [[polynomial]] function

we then derive the following definition:

**`: T f = (T f)^0 : (T f)^1 : (T f)^2 : ...`**, where

**`(T f)^n x = (d^n f) a -- PP n | [x.a]n`**, where

**`d^n f = d^n.1 (x -> dd f x -- dd x) /\ d^0 f = f`**, see [[derivative]]

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=17431>

intuitive explanation: <https://youtu.be/3d6DsjIBzJ4?t=383>

> **note** the definition above assumes **`x0 = 1 > RR x`** and **`PP 0 = 1`**, see [[improved expression evaluation]]

**properties**

[[taylor series]] are [[series#power series]]

## taylor polynomial

**definition**

**`S_Tf^n x = (T f)^0 : ... (T f)^n`**, where

- **`S_Tf^n`** is the **`n`**th partial sum of the [[taylor series]] **`T f`**
- **`n`** is a finite [[number]]

## Remainder

**definition**

**`R_Tf^n x = f x . S_Tf^n x`**, where

- **`S_Tf`** is the Taylor polynomial (the [[series#sequence of partial sums]]) of the [[taylor series]] **`T f`**
- **`f x`** is the [[function]] the [[taylor series]] **`T f`** approximates
- **`R_Tf^n`** is the _remainder_ of the [[taylor series]] **`T f`** after **`n`** terms

> **note** the definition of the [[taylor series#remainder]] is different from the usual [[series#remainder]] as **`S_Tf^@@ x`** is not necessarily equal to **`f x`**. as we want [[taylor series]] to converge to their underlying [[function]], we use **`f x`** instead of **`S_Tf^@@ x`** to define the [[taylor series#remainder]]

**theorem** the [[taylor series]] **`T f x`** converges to **`f x`** in an [[interval]] **`I`** if and only if **`R_Tf^@@ x = 0 > I x`**

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=22042>

**theorem** _Taylor's Inequality #magic_ **`||(d^n f) x|| -| M /\ RR M /\ NN n > ||x.a|| -| d /\ RR a /\ RR d < (||R_Tf^n.1 x|| -| M -- PP n | [||x.a||]n > ||x.a|| -| d)`**

**theorem** _Practical Convergence Condition_ **`||(d^n f) x|| -| M /\ RR M > NN n > ||x.a|| -| d /\ RR a /\ R d < (R_Tf^@@ x = 0 > ||x.a|| -| d)`**

> **proof** <https://youtu.be/7gigNsz4Oe8?t=22288>

this practical convergence criterion is a good way to show that a [[taylor series]] converges to its underlying [[function]] on a given [[interval]]. however, if the inequality does not hold, no conclusion can be drawn; the [[taylor series]] may or may not converge to the underlying [[function]] on the [[interval]].
