# Probability

&mdash; <https://courses.lumenlearning.com/introstats1/chapter/two-basic-rules-of-probability/>

&mdash; <https://youtu.be/BCiZc0n6COY?t=1884>

**see** [[outcome]], [[event]], [[sample space]]

**see** [[math notation]], [[boolean algebra]]

**definition** the _probability_ that [[event]] **`E`** occurs in a [[sample space]] **`S`** is denoted **`P S E`**

if all [[event]]s are equally likely to occur in the [[sample space]], then **`P S E = # E -- # S`**, see [[set#cardinality]]

## Sum Rule

**theorem** _sum rule_ **`P S (A \/ B) = P S A : P S B . P S (A /\ B)`**

> **note** if **`A`** and **`B`** are _mutually exclusive_ in **`S`**, then **`P S (A /\ B) = 0`**

## Product Rule

**theorem** _product rule_ **`P S (A /\ B) = P S A | P (S /\ A) B = P S B | P (S /\ B) A`**

the above can also be written as **`P (S /\ B) A = P S (A /\ B) -- P S B`**

> **note** if **`A`** and **`B`** are _independent_ in **`S`**, then **`P (S /\ B) A = P S A`** and **`P (S /\ A) B = P S B`**

### Bayes' Theorem

**theorem** _Bayes' Theorem_ **`P (S /\ B) A = P S A -- P S B | P (S /\ A) B`**

> **proof** isolate **`P (S /\ B) A`** from the [[probability#product rule]]

> **example**
>
> let **`B_1`** be a bucket with 3 red balls and 3 yellow balls
>
> let **`B_2`** be a bucket with 2 red balls and 4 yellow balls
>
> what is the probability of a randomly drawn red ball **`R`** being from bucket **`B_1`** in this space **`S`**?
>
> defining some events,
>
> **`P S R = 5-12`**
>
> **`P S B_1 = 1-2`**
>
> **`P (S /\ B_1) R = 1-2`**
>
> using Bayes' theorem, we get **`P (S /\ R) B_1 = P S B_1 -- P S R | P (S /\ B_1) R`**
>
> and therefore **`P (S /\ R) B_1 = 1-2 -- 5-12 | 1-22 = 3-5`**
