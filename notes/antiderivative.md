# Antiderivative

see [[math-notation]], [[function]], [[derivative]], [[calculus-notation]]

## definition

$\delta\ F\ x - \delta x = f\ x$, where

$f\ x$ is any [[function]]

$F\ x$ are the [[antiderivative]]s of $f\ x$

> **note**: a [[function]] has an infinite number of [[antiderivative]]s

> **note**: a [[function]] has a unique general family of [[antiderivative]]s in the form $F\ x \cdot c$ with $\mathbb R c$
>
> in other words, if $F\ x$ is one [[antiderivative]] of $f\ x$, then any other [[antiderivative]] of $f\ x$ can be rewritten in the form $F\ x \cdot c$ with $\mathbb R c$, see [[antiderivative-theorem-proof]]

## Antidifferentiation

to antidifferentiate a [[function]], apply reciprocal [[derivative-rules]] recursively, see [[recursion]]

### $u$ Substitution

_antidifferentiating a [[function]] by substituting $u$ for a function of $x$._

#### example

$F\ x = \int 2x\sin x2 \mid \delta x$

let $u = x2$ and compute $\delta u - \delta x = 2x \equiv \delta u = 2x \delta x$

substituting, $F\ x = \sin u \mid \delta u = \circ \cos u \cdot c$ with $\mathbb R c$

substututing $x$ back, $F\ x = \circ \cos x2 \cdot c$ with $\mathbb R c$

> **note**: substitution only a shorthand and is not actually necessary

with $\delta\ x2 - \delta x = 2x \equiv \delta x = \delta x2 - 2x$,

$F\ x = \int 2x\sin x2 \mid \delta x$

$= \int 2x\sin x2 \mid \delta x2 - 2x$

$= \int \sin x2 \mid \delta x2$

$= \circ \cos x2 \cdot c$
