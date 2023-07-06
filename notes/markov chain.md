# Markov Chain

**aka** _Markov Process_

**definition** a _markov chain_ is a [[sequence]] of events where the [[probability]] of each future event depends only on the state attained in the previous event

**representation**

[[markov chain]]s can be represented as a _transition diagram_, a weighted directed [[graph]] where nodes represent states and weighted edges represent the [[probability]] of an event occuring

![[20220718005316.png]]

&mdash; Wikipedia

> **note** there are numbers on the edges of the [[graph]] above that are harder to see in dark mode

## Stationary Distribution

certain [[markov chain]]s converge to a _stationary distribution_, which can be computed through [[matrix#multiplication]]

**theorem** an _irreducible_ [[markov chain]] has a unique [[markov chain#stationary distribution]] &mdash; <https://youtu.be/JGQe4kiPnrU>

**theorem** _ergodic theorem_ an _irreducible_ and _aperiodic_ [[markov chain]] converges to its unique [[markov chain#stationary distribution]] regardless of the initial state &mdash; <https://youtu.be/JGQe4kiPnrU?t=784>

**proceduces**

> **procedure** _approximating a [[markov chain#stationary distribution]] through [[iteration]]_
>
> let **`S`** be a [[sequence]] of column [[vector in rn]]s, where
>
> - **`S^0`** is the initial state of the [[markov chain]]
> - **`S^0,i`** is the initial state of node **`i`**
>
> #todo mm
>
> then, we compute **`S^n:1 = PS^n`**, where
>
> - **`S^n`** is the current iteration of the computation starting from **`S^0`**
> - **`S^n:1`** is the next iteration of the computation
> - **`P`** is the _transition matrix_ of the [[markov chain]]
> - **`P^j,k`** is the [[probability]] of a transition from node **`k`** to node **`j`**
>
> #todo mm
>
> we can then deduce **`S^@@ = [P]@@S^0`**, where
>
> - **`S^@@`** is the _stationary distribution_ of the [[markov chain]]

> **procedure** _computing a [[markov chain#stationary distribution]] through [[eigen#vector]]s and [[eigen#value]]s_
>
> the [[eigen#vector]] corresponding to the [[eigen#value]] **`1`** of the [[markov chain]]'s _transition matrix_ is the _stationary distribution_ of the [[markov chain]]. any _irreducible_ [[markov chain]] has an [[eigen#value]] of **`1`** with a unique corresponding [[eigen#vector]]
>
> it is common to multiply the resulting [[eigen#vector]] **`x`** by a [[scalar]] **`k`** so that **`:kx = 1`**
>
> &mdash; <https://youtu.be/EGoRJePORHs?t=551>
>
> &mdash; <https://youtu.be/d9-L2AmngKE>
>
> &mdash; <https://youtu.be/JGQe4kiPnrU>
