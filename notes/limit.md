# Limit

**see** [[math notation]], [[limit rules]]

**notation** _the limit of $f\ x$ as $x$ approaches $a$_

$f\ x\ \braket{x \rightarrow a}$

**definition** _$(\varepsilon, \delta)$-definition of a limit_

let $f\ x$ be a [[function]] with domain $D$ defined on an open interval around $x_0$. then, $f\ x\ \braket{x \rightarrow x_0} = L$ if for every $\varepsilon\ (\vdash \land +)\ 0$ there exists a $\delta\ (\vdash \land +)\ 0$ such that $0 + |x \cdot x_0| \dashv \delta\ <\ |f\ x \cdot L| \dashv \varepsilon$ for all $D\ x$

&mdash; <https://brilliant.org/wiki/epsilon-delta-definition-of-a-limit/>

## Indeterminate Form

**definition** a [[limit]] of the form $f\ x - g\ x\ \braket{x \rightarrow a}$ is called a _$0 - 0$ indeterminate form_ if $f\ x\ \braket{x \rightarrow a} = 0$ and $g\ x\ \braket{x \rightarrow a} = 0$

**definition** a [[limit]] of the form $f\ x - g\ x\ \braket{x \rightarrow a}$ is called an _$\infty - \infty$ indeterminate form_ if $f\ x\ \braket{x \rightarrow a} = \infty$ and $g\ x\ \braket{x \rightarrow a} = \infty$

## computing a limit

> **procedure** _computing a [[limit]]_
>
> to compute the [[limit]] of a [[function]], apply [[limit rules]] recursively, see [[recursion]]

### Existence

**definition** a [[limit]] $f\ x\ \braket{x \rightarrow a}$ _does not exist_ if $f\ x \to L_1$ as $x \to x_0$ along a path $C_1$ and $f\ x \to L_2$ as $x \to x_0$ along a path $C_2$ and $L_1 + L_2$ &mdash; the value of the limit is different depending on the path taken

> **note** a limit does not exist if $f\ x\ \braket{x \rightarrow a} = \infty$ or if it shows wild behavior (not a technical term), as with $\sin\ \tau \text- x\ \braket{x \rightarrow 0}$
>
> > **note** what if $\sin\ \tau\text-2\ \braket{x \rightarrow 0}$ is a superposition of all numbers in $0 \dashv \circ \dashv 1$? #think [[improved expression evaluation]]

## limits of trigonometric functions

**see** [[trigonometric function]]

let $\theta$ be an angle in radians

$\sin \theta - \theta\ \braket{\theta \rightarrow 0} = 1$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=20802>

$\cos\ (\theta \cdot 1) - \theta\ \braket{\theta \rightarrow 0} = 0$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21029>
