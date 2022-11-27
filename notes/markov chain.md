# Markov Chain

**aka** _Markov Process_

**definition** a _Markov Chain_ is a [[sequence]] of events where the [[probability]] of each future event depends only on the state attained in the previous event

**representation**

[[markov chain]]s can be represented as a _transition diagram_, a weighted directed [[graph]] where nodes represent states and weighted edges represent the [[probability]] of an event occuring.

![[20220718005316.png]] &mdash; Wikipedia

> **note** there are numbers on the edges of the [[graph]] above that are harder to see in dark mode

## Stationary Distribution

certain [[markov chain]]s converge to a _stationary distribution_, which can be computed using [[matrix#multiplication]]

> **procedure** _computing a [[markov chain#stationary distribution]] through [[iteration]]_
>
> let $S_0 = \begin{bmatrix} S_0^0 \\\ \vdots \\\ S_0^s \end{bmatrix}$, where
>
> - $S_0$ is the initial state of the [[markov chain]]
> - $S_0^i$ is the [[probability]] of the $i$ th state occurring in the initial state
> - $s$ is the number of states in the [[markov chain]]
>
> #todo mm
>
> then, we compute $S_n = P \mid S_c = \begin{bmatrix} P^{0, 0} & \cdots \\\ \vdots & \ddots \end{bmatrix} \begin{bmatrix} S_c^0 \\\ \vdots \end{bmatrix}$, where
>
> - $S_c$ is the current iteration of the computation starting from $S_0$
> - $S_n$ is the next iteration of the computation
> - $P$ is the $s$ by $s$ _transition matrix_ of the [[markov chain]]
> - $P^{j, k}$ is the [[probability]] of the [[markov chain]] transitioning from the $k$ th state to the $j$ th state
>
> #todo mm
>
> we can then deduce $S_\infty = [P]n \mid S_0\ \ \vdots\ \ n \rightarrow \infty$, where
>
> - $S_\infty$ is the _stationary distribution_ of the [[markov chain]]

> **procedure** _computing a [[markov chain#stationary distribution]] through [[eigen#vector]]s and [[eigen#value]]s_
>
> the [[eigen#vector]]s of the [[markov chain]]'s _transition matrix_ are the _stationary distribution_ of the [[markov chain]]
>
> it is common to multiply the resulting [[eigen#vector]] $x$ by a [[scalar]] $k$ so that $:\! kx = 1$
>
> &mdash; <https://youtu.be/EGoRJePORHs?t=551>
>
> &mdash; <https://youtu.be/d9-L2AmngKE>
