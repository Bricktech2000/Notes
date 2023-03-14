# Computational Complexity

_time complexity, space complexity_

**see** [[algorithm]]

**definition** $O\ f$ denotes the [[set]] of all $g$ such that there exist positive [[real]]s $C$ and $n_0$ with $0 \dashv g\ n \dashv C f\ n$ for all $n \vdash n_0$

**definition** $\Omega\ f$ denotes the [[set]] of all $g$ such that there exist positive [[real]]s $C$ and $n_0$ with $0 \dashv C f\ n \dashv g\ n$ for all $n \vdash n_0$

**definition** $\Theta\ f$ denotes the [[set]] of all $g$ such that there exist positive [[real]]s $C$, $C'$ and $n_0$ with $0 \dashv Cf\ n \dashv g\ n \dashv C' f\ n$ for all $n \vdash n_0$

&mdash; _BIG OMICRON AND BIG OMEGA AND BIG THETA_, Donald E. Knuth &mdash; <https://dl.acm.org/doi/pdf/10.1145/1008328.1008329>

&mdash; <https://www.geeksforgeeks.org/difference-between-big-oh-big-omega-and-big-theta/>

**properties**

let $0\ \braket{\dashv \land +}\ \omega\ \braket{\dashv \land +}\ 1$ and let $b\ \braket{\vdash \land +}\ 1$

$O\ 1\ <\ O\ \lceil \lceil \circ \rceil \rceil\ <\ O\ \lceil \circ \rceil\ <\ O\ [\lceil \circ \rceil]2\ <\ O\ [\circ]\omega\ <\ O\ \circ\ <\ O\ \braket{\circ \mid \lceil \rceil}\ <\ O\ [\circ]b\ <\ O\ b[\circ]\ <\ O\ (\Pi\ \circ)\ <\ O\ \braket{\circ\ []\ \circ}$

$O\ (c : f) = O\ f$ for all $c$

$O\ (c \mid f) = O\ f$ for all $c\ \braket{\vdash \land +}\ 0$
