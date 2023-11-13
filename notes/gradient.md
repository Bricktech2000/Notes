# Gradient

_returns a [[euclidean vector]] representing the direction of steepest ascent of a [[function]] at a given point_

**equiv** _[[jacobian#matrix]]_

**see** [[math notation]], [[calculus]], [[derivative#partial derivative]], [[jacobian]]

**notation** _in [[conventional math notation]]_ the [[gradient]] of **`f`** is denoted $\nabla f(\dots)$

**definition** let **`f`** be a [[function]] differentiable at **`p = (x ...)`**. then, the _gradient_ of **`f`** at **`p`** is defined to be **`dd f p -- dd p *`**, or equivalently **`dd f p -- dd p`**

## Descent

[[gradient#descent]] is an [[optimization]] [[algorithm]] that uses [[gradient]]s to find a local [[function#extremum]] through [[iteration]]

[[gradient#descent]] is based on the observation that a differentiable [[function]] **`f`** decreases fastest in the direction of its negative [[gradient]] **`.dd f p -- dd p`**

> **procedure** _[[gradient#descent]]_
>
> given a guess **`a^0`** for a local [[function#extremum]] of a [[function]] **`f`** and a _learning rate_ **`aa^n |- 0`** with **`aa^n + 0`**, we have
>
> **`a^n:1 = a^n . aa^n (dd f a^n -- dd a^n)`**
>
> for a small enough **`aa^n`**, the [[sequence]] **`a`** is a (monotonically) [[sequence#decreasing sequence]] and therefore converges to a local [[function#extremum]] of **`f`**
>
> &mdash; <https://en.wikipedia.org/wiki/Gradient_descent>
