# Probability

**see** [[math notation]], [[boolean algebra]]

**definition** a _sample space_ **`S`** is a [[set]] of elements

**definition** an _event_ **`E`** is a [[set#subset]] of a _sample space_ **`S`**

**definition** the _probability_ that _event_ **`E`** occurs in a space **`S`** is denoted **`P {E, S}`**, see [[ordered pair]]

if all events are equally likely to occur in the space, then **`P {E, S} = # E -- # S`**

**see** [[set#cardinality]]

## multiplicative rule

_for independent events_

**definition**

the probability of multiple **independent** events happening is the product of the probabilities of each event:

**`P {E_1 /\ E_2 , S} = P {E_1 , S} | P {E_2 , S}`**

## permutative rule

_without repetition, order matters_

**see** [[set]] permutation

## combinatory rule

_without repetition, order does not matter_

**see** [[set]] combination

## given "rule"

**definition**

**`P {A, B} = P {A /\ B, S} -- P {B, S}`**, where

- **`P {A /\ B, S}`** is the probability of both **`A`** and **`B`** occuring in the sample space **`S`**
- **`P {B, S}`** is the probability **`B`** occuring in the sample space **`S`**
- **`P {A, B}`** is the probability of **`A`** occurring _given that_ **`B`** has occurred

## bayes' theorem

**theorem** _Bayes' Theorem_

**`P {A, B} = P {A, S} -- P {B, S} | P {B, A}`**

> **proof**
>
> from the given "rule", we know **`P {A, B} = P {A /\ B, S} -- P {B, S}`** and that **`P {B, A} = P {B /\ A, S} -- P {A, S}`**
>
> solving for **`P {B /\ A, S}`** and substituting into the first equation, we get **`P {A, B} = P {A, S} -- P {B, S} | P {B, A}`**

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
> **`P {R, S} = 5-12`**
>
> **`P {B_1 , S} = 1-2`**
>
> **`P {R, B_1} = 1-2`**
>
> using Bayes' theorem, we get **`P {B_1 , R} = P {B_1 , S} - P {R, S} | P {R, B_1}`**
>
> and therefore **`P {B_1 , R} = 1-2 - 5-12 | 1-22 = 3-5`**
