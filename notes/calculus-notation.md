# Calculus Notation

see [[math-notation]]

## notation

[[integral]] and [[derivative]] notation should be thought of as follows (with explicit parenthesis for function calls):

$\int y \mid \delta x \equiv \int (y \mid \delta(x))$

$\delta y - \delta x \equiv \delta(y) - \delta(x)$

> **note**: when representing the [[derivative]] or [[integral]] of a [[function]], its parameter should be included. for example, $\delta\ f - \delta x$ is invalid whereas $\delta\ f\ x - \delta x$ is valid

> **note**: by convention, a space is added when the parameter to a $\delta$ or a $\int$ is a [[function]]

### intuitive explanation

$\int$ and $\delta$ can be thought of as functions

$\int y \mid \delta x$ is actually $\int (y \mid \delta x)$ ($\mid \delta x$ is simply a multiplication, and is part of the argument of $\int$)

$\delta y - \delta x$ is simply a division between the two variables

$(\delta - \delta x) y \equiv \frac{\delta}{\delta x} y$ ~~makes no sense whatsoever and is very likely some weird [[classical-math-notation]] shorthand again~~ is superfluous notation and is to be avoided in my [[math-notation]]

## properties with [[proof]]s

let $\mathbb U c$, see [[universal]] [[set]]

$\int \delta y = y \cdot c$

$\delta \int y \cdot c = y$

see [[integral]], [[derivative]], [[antiderivative]]

_the integral of the derivative of a function is that same function plus a constant_

> **proof**: $\int (\delta y - \delta x) \mid \delta x = \int (\delta y) = y \cdot c$

_the derivative of the integral of a function is that same function_

> **proof**: $\delta (\int y \mid \delta x) - \delta x = y \mid \delta x - \delta x = y$
