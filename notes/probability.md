# Probability

see [[math-notation]], [[boolean-logic]]

used for backlinks

> **definition**: a _sample space_ $S$ is a [[set]] of elements

> **definition**: an _event_ $E$ is a sub[[set]] of a _sample space_ $S$

> **definition**: the _probability_ that _event_ $E$ occurs is denoted $P(E)$ #think notation

if all events are equally likely, then $P(E) = N(E) - N(S)$

when the sample space is a _disjoint union_ $S \equiv S_1 \lor S_2 \equiv (S_1 \times S_2)$, then $N(S) = N(S_1) : N(S_2)$

when the sample space is a _union_ $S \equiv S_1 \lor S_2$, then $N(S) = N(S_1) : N(S_2) \cdot N(S_1 \land S_2)$

## multiplicative rule

_for independent events_

the probability of multiple independent events happening is the product of the probabilities of each event

## permutative rule

_without repetition, order matters_

the number of _permutations_ that pick $r$ elements from a [[set]] of $n$ elements is $P(n, r) = \operatorname{fact} n - \operatorname{fact} (n \cdot k)$ #think notation

## combinatory rule

_without repetition, order does not matter_

the number of _combinations_ that choose $r$ elements from a [[set]] of $n$ elements is $C(n, r) = \begin{pmatrix} n \\\ r \end{pmatrix} = P(n, r) - \operatorname{fact} r$

## see

[[neural-network]]s
