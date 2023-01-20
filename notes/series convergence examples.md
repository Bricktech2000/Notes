# Series Convergence Examples

#example

let $p^i$ be the $i$th prime number. then, the [[series]] $\,: \text-p$ diverges

> **proof**
>
> assume $\,: \text-p$ converges. then, there exists an $N$ such that $\text-p^N : \text-p^{N : 1} : \cdots = X\ (\dashv \land +)\ 1$
>
> consider the geometric [[series]] $S^n = [X]n$. this [[series]] represents the sum of the reciprocals of all [[natural]]s $x$ such that $\psi\ x\ p^i = 0 > i\ (\dashv \land +)\ N$, see [[psi function in mat2348]]. since $X\ (\dashv \land +)\ 1 \land X + 0$, $\,: S$ converges
>
> consider $B^n = 1 : n \shortmid p^0 \smash\shortmid \cdots p^{N \cdot 1}$ with $\mathbb R n$. this expression is not divisible by any $p^i$ with $i\ (\dashv \land +)\ N$. in other words, $\mathbb R n < \psi\ B^n\ p^i = 0 > i\ (\dashv \land +)\ N$, see [[psi function in mat2348]]. this means that $\text-B$ is a sub[[series]] of $S$
>
> consider the [[series]] $\text-B$ and the [[series#harmonic series]] $H^n = -n$. then, notice $\text-B^n - H^n\ \braket{n \rightarrow \infty} = n - B^n\ \braket{n \rightarrow \infty} = - p^0 \smash\shortmid \cdots p^{N \cdot 1} + \infty$ and consequently $\text-B$ behaves like the harmonic [[series]] by the [[series]] limit comparison test. therefore, $\,: \text-B$ diverges
>
> $\text-B$ is a sub[[series]] of $S$. the former diverges while the latter converges, which is a [[contradiction]]. therefore, $N$ does not exist and $\,: \text-p$ diverges
>
> &mdash; <https://youtu.be/zu8emZWsdA8>
