# Limit

see [[math-notation]], [[limit-rules]]

## notation

the _limit of $f\ x$ as $x$ approaches $a$ ._ is denoted as follows:

$\lim_{x \to a} f\ x$

## Indeterminate Forms

> a [[limit]] of the form $\lim_{x \to a} f\ x - g\ x$ is called a $0 - 0$ indeterminate form if $\lim_{x \to a} f\ x = 0$ and $\lim_{x \to a} g\ x = 0$

> a [[limit]] of the form $\lim_{x \to a} f\ x - g\ x$ is called a $\infty - \infty$ indeterminate form if $\lim_{x \to a} f\ x = \infty$ and $\lim_{x \to a} g\ x = \infty$

## Computing a Limit

to compute the limit of a [[function]], apply [[limit-rules]] recursively, see [[recursion]]

### Limit Existence

$\lim_{x \to a}$ does not exist if any of the following is true:

- $\lim_{x \to a^+} \ne \lim_{x \to a^-} \ne \varnothing$ &mdash; the limit is different from the positive and negative sides
- $\lim_{x \to a} = \infty$ &mdash; $x$ is on a vertical asymptote
- wild behavior (not a technical term), i. e. $\lim_{x \to 0} \sin\ (\pi - x)$

if $g\ a = 0$, then $\lim_{x \to a} (f\ x - g\ x)$

- does not exist if $f\ a \ne 0$ (including $\dot \circ \infty$)
- can exist if $f\ a = 0$. first simplify using the [[limit-rules]] and then study the limit

## special limits

see [[trigonometric-function]]

let $\theta$ be an angle in radians

$\lim_{\theta \to 0} \sin \theta - \theta = 1$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=20802>

$\lim_{\theta \to 0} \cos\ (\theta \circ 1) - \theta = 0$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21029>
