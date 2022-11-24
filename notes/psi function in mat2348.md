# Psi Function in MAT2348

**definition**

$\psi\ n$ takes in a [[natural]] number $n$ and returns the [[multiset]] containing all [[natural]] prime [[factor]]s of $n$.

**properties**

$\mid\! \psi\ n = n$

$\psi\ n\ 0 = \psi\ n\ 1 = 0$

$\psi\ ab = \psi\ a : \psi\ b$

$a$ _divides_ $b$ if and only if $\psi\ a \le \psi\ b$

$n$ is a _square [[number]]_ if and only if $\mathbb E \psi\ n$

$n$ is a _prime [[number]]_ if and only if $\#\ \psi\ n = 1$, or $\psi\ n = ((n))$

$m$ and $n$ are _coprime_ if and only if $\psi\ m \land \psi\ n = (\ )$

$n = 1$ if and only if $\#\ \psi\ n = 0$, or $\psi\ n = (\ )$

the _greatest common divisor_ of $a$ and $b$ is $\mid\! (\psi\ a \land \psi\ b)$

the _least common multiple_ of $a$ and $b$ is $\mid\! (\psi\ a \lor \psi\ b)$

**equivalences**

> **equivalence** _the [[category]] $\mathbb N, \text{divides}$ and the [[category]] $\text{multiset of primes}, \text{multisubset}$_
>
> the [[psi function in mat2348]] is a [[functor]] from the [[category]] $\mathbb N, \text{divides}$ to the [[category]] $\text{multiset of primes}, \text{multisubset}$
>
> [[functor]]s [[map]] both [[category#morphism]]s and [[category#object]]s between [[category]]es. this means than:
>
> - [[category#product]]s in the first [[category]] represent the GCD of two [[natural]]s, and therefore [[category#product]]s in the second [[category]] represent the intersection of two [[multiset]]s
> - [[category#coproduct]]s in the first [[category]] represent the LCM of two [[natural]]s, and therefore [[category#coproduct]]s in the second [[category]] represent the union of two [[multiset]]s
> - the [[category#initial object]] in the first [[category]] represents the [[natural]] $1$, and therefore the [[category#initial object]] in the second [[category]] represents the empty [[multiset]] $(\ )$
> - the [[category#terminal object]] in the first [[category]] represents the [[natural]] $0$, and therefore the [[category#terminal object]] in the second [[category]] represents #think what does it represent? $e \rightarrow \infty$ maybe?
>
> it is also worth noting that this [[functor]] is a [[function#bijective function]] forming a [[category#isomorphism]], which means that the two [[category]]es are isomorphic
