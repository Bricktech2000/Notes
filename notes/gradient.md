# Gradient

_a [[euclidean vector]] pointing to the direction of steepest ascent_

**equiv** _[[jacobian#matrix]]_

**see** [[calculus]], [[derivative#partial derivative]], [[jacobian]]

## Descent

[[gradient#descent]] is an [[optimization]] [[algorithm]] that uses [[gradient]]s to find a local [[function#extremum]] through [[iteration]]

[[gradient#descent]] is based on the observation that a differentiable [[function]] $f$ decreases fastest in the direction of its negative [[gradient]] $-\nabla f$

> **procedure** _[[gradient#descent]]_
>
> given a guess $a_0$ for a local [[function#extremum]] of a [[function]] $f$ and a _learning rate_ $\forall n.\ \gamma_n > 0$, iterate $a_{n + 1} = a_n - \gamma_n \nabla f\ a_n$
>
> for a small enough $\gamma$s, the [[sequence]] $a$ is a (monotonically) [[sequence#decreasing sequence]] and therefore converges to a local [[function#extremum]] of $f$
>
> --- <https://en.wikipedia.org/wiki/Gradient_descent>
