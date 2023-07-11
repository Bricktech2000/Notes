# Probability

&mdash; <https://courses.lumenlearning.com/introstats1/chapter/two-basic-rules-of-probability/>

&mdash; <https://youtu.be/BCiZc0n6COY?t=1884>

**see** [[math notation]], [[boolean algebra]]

**definition** a _sample space_ **`S`** is a [[set]] of elements

**definition** an _event_ **`E`** is a [[set#subset]] of a _sample space_ **`S`**

**definition** the _probability_ that _event_ **`E`** occurs in a space **`S`** is denoted **`P {E, S}`**, see [[ordered pair]]

if all events are equally likely to occur in the space, then **`P {E, S} = # E -- # S`**, see [[set#cardinality]]

## Sum Rule

**theorem** _sum rule_ **`P {A \/ B, S} = P {A, S} : P {B, S} . P {A /\ B, S}`**

> **note** if **`A`** and **`B`** are _mutually exclusive_ in **`S`** (**`A /\ B /\ S = { }`**), then **`P {A /\ B, S} = 0`**

## Product Rule

**theorem** _product rule_ **`P {A /\ B, S} = P {A, S} | P {B, A /\ S} = P {B, S} | P {A, B /\ S}`**

the above can also be written as **`P {A, B /\ S} = P {A /\ B, S} -- P {B, S}`**

> **note** if **`A`** and **`B`** are _independent_ in **`S`**, then **`P {A, B /\ S} = P {A, S}`** and **`P {B, A /\ S} = P {B, S}`**

### Bayes' Theorem

**theorem** _Bayes' Theorem_ **`P {A, B /\ S} = P {A, S} -- P {B, S} | P {B, A /\ S}`**

> **proof** isolate **`P {A, B /\ S}`** from the [[probability#product rule]]

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
> **`P {R, B_1 /\ S} = 1-2`**
>
> using Bayes' theorem, we get **`P {B_1 , R /\ S} = P {B_1 , S} - P {R, S} | P {R, B_1 /| S}`**
>
> and therefore **`P {B_1 , R /\ S} = 1-2 - 5-12 | 1-22 = 3-5`**
