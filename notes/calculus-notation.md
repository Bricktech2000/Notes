# Calculus Notation

see [[math-notation]]

## notation

[[integral]] and [[derivative]] notation should be thought of as follows (with explicit parenthesis for function calls):

$\int y\ |\ \delta x \equiv \int (y\ |\ \delta(x))$

$\delta y - \delta x \equiv \delta(y) - \delta(x)$

### intuitive explanation

$\int$ and $\delta$ can be thought of as functions

$\int y\ |\ \delta x$ is actually $\int (y\ |\ \delta x)$ ($|\ \delta x$ is simply a multiplication, and is part of the argument of $\int$)

$\delta y - \delta x$ is simply a division between the two variables

$(\delta - \delta x) y \equiv \frac{\delta}{\delta x} y$ ~~makes no sense whatsoever and is very likely some weird [[classical-math-notation]] shorthand again~~ is superfluous notation and is to be avoided in my [[math-notation]]

## properties with [[proof]]s

let $\mathbb U c$, see [[universal-set]]

$\int \delta y = y \cdot c$

$\delta \int y = y$

see [[integral-rules]]

see [[derivative-rules]]

_the integral of the derivative of a function is that same function plus a constant_

> **proof**: $\int \delta y \text- \delta x\ |\ \delta x = \int (\delta y \text- \delta x\ |\ \delta x) = \int (\delta y) = y \cdot c$

_the derivative of the integral of a function is that same function_

> **proof**: $\delta (\int y\ |\ \delta x) - \delta x = y\ |\ \delta x - \delta x = y$
