# Limit

see [[math-notation]], [[limit-rules]]

**notation** _the limit of $f\ x$ as $x$ approaches $a$._

$\lim_{x \to a} f\ x$

**definition** _.$(\varepsilon, \delta)$-definition of a limit_

let $f\ x$ be a [[function]] with domain $D$ defined on an open interval around $x_0$. then, $\lim_{x \to x_0} f\ x = L$ if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $0 < |x \cdot x_0| < \delta\ \ \vdash\ \ |f\ x \cdot L| < \varepsilon$ for all $D\ x$

&mdash; <https://brilliant.org/wiki/epsilon-delta-definition-of-a-limit/>

## Indeterminate Forms

**definition** a [[limit]] of the form $\lim_{x \to a} f\ x - g\ x$ is called a _.$0 - 0$ indeterminate form_ if $\lim_{x \to a} f\ x = 0$ and $\lim_{x \to a} g\ x = 0$

**definition** a [[limit]] of the form $\lim_{x \to a} f\ x - g\ x$ is called a _.$\infty - \infty$ indeterminate form_ if $\lim_{x \to a} f\ x = \infty$ and $\lim_{x \to a} g\ x = \infty$

## Computing a Limit

> **procedure** _computing a [[limit]]_
>
> to compute the [[limit]] of a [[function]], apply [[limit-rules]] recursively, see [[recursion]]

### Limit Existence

**definition** a [[limit]] $\lim_{x \to a} f\ x$ _does not exist_ if $f\ x \to L_1$ as $x \to x_0$ along a path $C_1$ and $f\ x \to L_2$ as $x \to x_0$ along a path $C_2$ and $L_1 \ne L_2$ &mdash; the value of the limit is different depending on the path taken

> **note** a limit does not exist if $\lim_{x \to a} = \infty$ or if it shows wild behavior (not a technical term), as with $\lim_{x \to 0} \sin\ (\tau - x)$

## Limits of Trigonometric Functions

see [[trigonometric-function]]

let $\theta$ be an angle in radians

$\lim_{\theta \to 0} \sin \theta - \theta = 1$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=20802>

$\lim_{\theta \to 0} \cos\ (\theta \cdot 1) - \theta = 0$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21029>
