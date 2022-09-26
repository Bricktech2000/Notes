# Probing

**see** [[math notation]]

probing [[function]]s include:

- linear probing: $i\ k \rightarrow ai : b$
- quadratic probing: $i\ k \rightarrow ai2 : bi : c$
- double hashing: $i\ k \rightarrow i \mid H_2\ k$, where $H_2$ is a secondary [[hash]] [[function]]
- PRNG: $i\ k \rightarrow i \mid \operatorname{PRNG}\ (H\ k)\ i$, where $\operatorname{PRNG}$ is a PRNG with seed $H\ k$ and initial state $i$

> **note** double hashing reduces to linear probing at runtime when the value of $k$ is known

## Cycle Length

see [[set]]

**definition** the _cycle length_ of a [[probing]] [[function]] $P\ i\ k$ given a [[list]] length $n$ is the minimum number of iterations of $P\ i\ k \bmod n$ that must be performed before the sequence repeats.

the cycle length of a linear [[probing]] [[function]] $i \rightarrow ai : b$ modulo $n$ is $n$ if and only if $\psi\ a \land \psi\ n = (\ )$ , see [[psi function in mat2348]] &mdash; <https://youtu.be/RBSGKlAvoiM?t=17369>

the [[probing]] [[function]] $i \rightarrow i$ is popular because it has a cycle length of $n$ for any $n$

the cycle length of a quadratic [[probing]] [[function]] $i \rightarrow ai2 : bi : c$ modulo $n$ can be difficult to compute. a few examples of quadratic [[probing]] [[function]]s with cycle lengths of $n$ are: &mdash; <https://youtu.be/RBSGKlAvoiM?t=18191>

- $i \rightarrow i2$ with $n > 3\ \land\ \#\ \psi\ n = 1$ (cycle length is not $n$ and therefore it must be the case that $\alpha \le 1\text-2$, see [[hash table]])
- $i \rightarrow i2 : i - 2$ with $n = 2[k] \land \mathbb N k$
- $i \rightarrow [\cdot 1]x \mid x2$ with $\#\ \psi\ n = 1\ \land\ n \bmod 4 = 3$
