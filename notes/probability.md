# Probability

see [[math-notation]], [[boolean-logic]]

> **definition**: a _sample space_ $S$ is a [[set]] of elements

> **definition**: an _event_ $E$ is a sub[[set]] of a _sample space_ $S$

> **definition**: the _probability_ that _event_ $E$ occurs in a space $S$ is denoted $P\ (E, S)$

if all events are equally likely to occur in the space, then $P\ (E, S) = E^\# - S^\#$

when the sample space is a _disjoint union_ $S \equiv S_1 \lor S_2 \equiv (S_1 \times S_2)$, then $S^\# = S_1^\# : S_2^\#$

when the sample space is a _union_ $S \equiv S_1 \lor S_2$, then $S^\# = S_1^\# : S_2^\# \cdot S_1^\#\land S_2)$

## multiplicative rule

_for independent events_

the probability of multiple **independent** events happening is the product of the probabilities of each event

$P\ (E_1 \land E_2, S) = P\ (E_1, S) \mid P\ (E_2, S)$

## permutative rule

see [[classical-math-notation]]

_without repetition, order matters_

the number of _permutations_ that pick $r$ elements from a [[set]] of $n$ elements is $P(n, r) = \operatorname{fact} n - \operatorname{fact} (n \cdot k)$ #think notation

## combinatory rule

see [[classical-math-notation]]

_without repetition, order does not matter_

the number of _combinations_ that choose $r$ elements from a [[set]] of $n$ elements is $C(n, r) = \begin{pmatrix} n \\\ r \end{pmatrix} = P(n, r) - \operatorname{fact} r$ #think notation

## given "rule"

$P\ (A, B) = P\ (A \land B, S) - P\ (B, S)$, where

$P\ (A \land B, S)$ is the probability of both $A$ and $B$ occuring in the sample space $S$

$P\ (B, S)$ is the probability $B$ occuring in the sample space $S$

$P\ (A, B)$ is the probability of $A$ occurring _given that_ $B$ has occurred

## Bayes' Theorem

> **theorem**: _Bayes' Theorem_
>
> $P\ (A, B) = P\ (A, S) - P\ (B, S) \mid P\ (B, A)$

> **proof**:
>
> from the given "rule", we know $P\ (A, B) = P\ (A \land B, s) - P\ (B, S)$ and that $P\ (B, A) = P\ (B \land A, S) - P\ (A, S)$
>
> solving for $P\ (B, A)$ and substituting into the first equation, we get $P\ (A, B) = P\ (A, S) - P\ (B, S) \mid P\ (B, A)$

### example

#example

let $B_1$ be a bucket with 3 red balls and 3 yellow balls

let $B_2$ be a bucket with 2 red balls and 4 yellow balls

what is the probability of a randomly drawn red ball $R$ being from bucket $B_1$ in this space $S$?

defining some events,

$P\ (R, S) = 5 \text- 12$

$P\ (B_1, S) = 1 \text- 2$

$P\ (R, B_1) = 1 \text- 2$

using Bayes' theorem, we get $P\ (B_1, R) = P\ (B_1, S) - P\ (R, S) \mid P\ (R, B_1)$

and therefore $P\ (B_1, R) = 1 \text- 2 - 5 \text- 12 \mid 1 \text- 2 = 3 \text- 5$

## see

[[neural-network]]s
