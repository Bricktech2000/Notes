# Markov Chain

**aka** _Markov Process_

**definition** a _Markov Chain_ is a [[sequence]] of events where the [[probability]] of each future event depends only on the state attained in the previous event

**representation**

[[markov chain]]s can be represented as a _transition diagram_, a weighted directed [[graph]] where nodes represent states and weighted edges represent the [[probability]] of an event occuring.

![[20220718005316.png]]

&mdash; Wikipedia

> **note** there are numbers on the edges of the [[graph]] above that are harder to see in dark mode

## Stationary Distribution

certain [[markov chain]]s converge to a _stationary distribution_, which can be computed using [[matrix#multiplication]]

> **procedure** _computing a [[markov chain#stationary distribution]] through [[iteration]]_
>
> let **`S`** be a column [[vector in rn]], where
>
> - **`S^0`** is the initial state of the [[markov chain]]
> - **`S^0,i`** is the [[probability]] of node **`i`** being present in the initial state
>
> #todo mm
>
> then, we compute **`S^n:1 = P | S^n`**, where
>
> - **`S^n`** is the current iteration of the computation starting from **`S^0`**
> - **`S^n:1`** is the next iteration of the computation
> - **`P`** is the **`# S`** by **`# S`** _transition matrix_ of the [[markov chain]]
> - **`P^j,k`** is the [[probability]] of a transition from node **`k`** to node **`j`**
>
> #todo mm
>
> we can then deduce **`S^@@ = [P]@@ | S^0`**, where
>
> - **`S^@@`** is the _stationary distribution_ of the [[markov chain]]

> **procedure** _computing a [[markov chain#stationary distribution]] through [[eigen#vector]]s and [[eigen#value]]s_
>
> the [[eigen#vector]]s of the [[markov chain]]'s _transition matrix_ are the _stationary distribution_ of the [[markov chain]]
>
> it is common to multiply the resulting [[eigen#vector]] **`x`** by a [[scalar]] **`k`** so that **`:kx = 1`**
>
> &mdash; <https://youtu.be/EGoRJePORHs?t=551>
>
> &mdash; <https://youtu.be/d9-L2AmngKE>
