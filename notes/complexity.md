# Complexity

_time complexity, space complexity_

**see** [[algorithm]]

**definition** $\Omicron\ f\ n$ denotes the [[set]] of all $g\ n$ such that there exists positive [[real]]s $C$ and $n_0$ with $0 \le g\ n \le C f\ n$ for all $n \ge n_0$

**definition** $\Omega\ f\ n$ denotes the [[set]] of all $g\ n$ such that there exists positive [[real]]s $C$ and $n_0$ with $0 \le C f\ n \le g\ n$ for all $n \ge n_0$

**definition** $\Theta\ f\ n$ denotes the [[set]] of all $g\ n$ such that there exists positive [[real]]s $C$, $C'$ and $n_0$ with $0 \le Cf\ n \le g\ n \le C' f\ n$ for all $n \ge n_0$

&mdash; _BIG OMICRON AND BIG OMEGA AND BIG THETA_, Donald E. Knuth &mdash; <https://dl.acm.org/doi/pdf/10.1145/1008328.1008329>

&mdash; <https://www.geeksforgeeks.org/difference-between-big-oh-big-omega-and-big-theta/>

&mdash; #todo computerphile video

**properties**

let $0 < c < 1$

$\Omicron\ 1 \vdash \Omicron\ \lceil \lceil n \rceil \rceil \vdash \Omicron\ \lceil n \rceil \vdash \Omicron\ [n]c \vdash \Omicron\ n \vdash \Omicron\ n \lceil n \rceil \vdash \Omicron\ n2 \vdash \Omicron\ n3 \vdash \Omicron\ 2[n] \vdash \Omicron\ \operatorname{fact} n$
