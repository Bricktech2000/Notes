# Psi Function in MAT2348

**definition**

$\psi\ n$ takes in a [[natural]] number $n$ and returns the [[multiset]] containing all [[natural]] prime [[factor]]s of $n$.

#think see [[category theory]]

this [[function]] is a [[functor]] from the [[category]] $\mathbb N, \text{divides}$ to the [[category]] $\text{multiset of primes}, \text{includes}$

[[functor]]s also map morphisms between [[category]]es. this means than:

- products in the first category represent the GCD of two numbers, and therefore products in the second category represent the union of two multisets
- coproducts in the first category represent the LCM of two numbers, and therefore coproducts in the second category represent the intersection of two multisets

it is also worth noting that this [[functor]] is a [[function#bijective function]], which means that the two [[category]]es are isomorphic

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
