# Computational Complexity

_time complexity, space complexity_

**see** [[algorithm]]

**definition** $O\ f\ n$ denotes the [[set]] of all $g\ n$ such that there exists positive [[real]]s $C$ and $n_0$ with $0 \dashv g\ n \dashv C f\ n$ for all $n \vdash n_0$

**definition** $\Omega\ f\ n$ denotes the [[set]] of all $g\ n$ such that there exists positive [[real]]s $C$ and $n_0$ with $0 \dashv C f\ n \dashv g\ n$ for all $n \vdash n_0$

**definition** $\Theta\ f\ n$ denotes the [[set]] of all $g\ n$ such that there exists positive [[real]]s $C$, $C'$ and $n_0$ with $0 \dashv Cf\ n \dashv g\ n \dashv C' f\ n$ for all $n \vdash n_0$

&mdash; _BIG OMICRON AND BIG OMEGA AND BIG THETA_, Donald E. Knuth &mdash; <https://dl.acm.org/doi/pdf/10.1145/1008328.1008329>

&mdash; <https://www.geeksforgeeks.org/difference-between-big-oh-big-omega-and-big-theta/>

**properties**

let $0\ (\dashv \land +)\ \omega\ (\dashv \land +)\ 1$ and let $b\ (\vdash \land +)\ 1$

$O\ 1\ <\ O\ \lceil \lceil n \rceil \rceil\ <\ O\ \lceil n \rceil\ <\ O\ [\lceil n \rceil]2\ <\ O\ [n]\omega\ <\ O\ n\ <\ O\ n \lceil n \rceil\ <\ O\ [n]b\ <\ O\ b[n]\ <\ O\ \Pi\ n\ <\ O\ n[n]$

$O\ (c : f\ n) = O\ f\ n$ for all $c$

$O\ (cf\ n) = O\ f\ n$ for all $c > 0$
