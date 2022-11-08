# Psi Function in MAT2348

**definition**

$\psi\ n$ takes in a [[natural]] number $n$ and returns the [[multiset]] containing all [[natural]] prime factors of $n$.

**properties**

$\psi\ n \mid \cdots = n$

$\psi\ n\ 0 = \psi\ n\ 1 = 0$

$\psi\ ab = \psi\ a : \psi\ b$

$a$ _divides_ $b$ if and only if $\psi\ a \le \psi\ b$

$n$ is a _square [[number]]_ if and only if $\mathbb E \psi\ n$

$n$ is a _prime [[number]]_ if and only if $\#\ \psi\ n = 1$, or $\psi\ n = ((n))$

$m$ and $n$ are _coprime_ if and only if $\psi\ m \land \psi\ n = (\ )$

$n = 1$ if and only if $\#\ \psi\ n = 0$, or $\psi\ n = (\ )$

the _greatest common divisor_ of $a$ and $b$ is $(\psi\ a \land \psi\ b) \mid \cdots$

the _least common multiple_ of $a$ and $b$ is $(\psi\ a \lor \psi\ b) \mid \cdots$
