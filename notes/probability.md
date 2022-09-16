# Probability

see [[math-notation]], [[boolean-logic]]

**definition** a _sample space_ $S$ is a [[set]] of elements

**definition** an _event_ $E$ is a sub[[set]] of a _sample space_ $S$

**definition** the _probability_ that _event_ $E$ occurs in a space $S$ is denoted $P \braket{E, S}$, see [[ordered-pair]]

if all events are equally likely to occur in the space, then $P \braket{E, S} = \#\ E - \#\ S$

see [[set]] cardinality

## Multiplicative Rule

_for independent events_

**definition**

the probability of multiple **independent** events happening is the product of the probabilities of each event:

$P \braket{E_1 \land E_2, S} = P \braket{E_1, S} \mid P \braket{E_2, S}$

## Permutative Rule

_without repetition, order matters_

**see** [[set]] permutation

## Combinatory Rule

_without repetition, order does not matter_

**see** [[set]] combination

## Given "Rule"

**definition**

$P \braket{A, B} = P \braket{A \land B, S} - P \braket{B, S}$, where

- $P \braket{A \land B, S}$ is the probability of both $A$ and $B$ occuring in the sample space $S$
- $P \braket{B, S}$ is the probability $B$ occuring in the sample space $S$
- $P \braket{A, B}$ is the probability of $A$ occurring _given that_ $B$ has occurred

## Bayes' Theorem

> **theorem** _Bayes' Theorem_
>
> $P \braket{A, B} = P \braket{A, S} - P \braket{B, S} \mid P \braket{B, A}$

> **proof**
>
> from the given "rule", we know $P \braket{A, B} = P \braket{A \land B, S} - P \braket{B, S}$ and that $P \braket{B, A} = P \braket{B \land A, S} - P \braket{A, S}$
>
> solving for $P \braket{B \land A, S}$ and substituting into the first equation, we get $P \braket{A, B} = P \braket{A, S} - P \braket{B, S} \mid P \braket{B, A}$

> **example**
>
> let $B_1$ be a bucket with 3 red balls and 3 yellow balls
>
> let $B_2$ be a bucket with 2 red balls and 4 yellow balls
>
> what is the probability of a randomly drawn red ball $R$ being from bucket $B_1$ in this space $S$?
>
> defining some events,
>
> $P \braket{R, S} = 5 \text- 12$
>
> $P \braket{B_1, S} = 1 \text- 2$
>
> $P \braket{R, B_1} = 1 \text- 2$
>
> using Bayes' theorem, we get $P \braket{B_1, R} = P \braket{B_1, S} - P \braket{R, S} \mid P \braket{R, B_1}$
>
> and therefore $P \braket{B_1, R} = 1 \text- 2 - 5 \text- 12 \mid 1 \text- 2 = 3 \text- 5$
