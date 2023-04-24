# Gradient

_returns a [[vector in rn]] representing the direction of steepest ascent of a [[function]] at a given point_

**see** [[calculus]], [[derivative#partial derivative]]s

**notation** _in [[conventional math notation]]_ the [[gradient]] of **`f`** is denoted $\nabla f(\dots)$

**definition** let **`f`** be a [[function]] differentiable at **`p = (x ...)`**. then, the _gradient_ of **`f`** at **`p`** is defined to be **`\d f p -- \d p`**

## Descent

[[gradient#descent]] is an [[optimization]] [[algorithm]] that uses [[gradient]]s to find a local [[function#extremum]] through [[iteration]]

[[gradient#descent]] is based on the observation that a differentiable [[function]] **`f`** decreases fastest in the direction of its negative [[gradient]] **`.\d f p -- \d p`**

> **procedure** _[[gradient#descent]]_
>
> given a guess **`a^0`** for a local [[function#extremum]] of a [[function]] **`f`** and a _learning rate_ **`\a^n |- 0`** with **`\a^n + 0`**, we have
>
> **`a^n:1 = a^n . \a^n (\d f a^n -- \d a^n)`**
>
> for a small enough **`\a^n`**, the [[sequence]] **`a`** is a (monotonically) [[sequence#decreasing sequence]] and therefore converges to a local [[function#extremum]] of **`f`**
>
> &mdash; <https://en.wikipedia.org/wiki/Gradient_descent>
