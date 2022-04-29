# Limit

see [[math-notation]], [[limit-rules]]

## Computing a Limit

to compute the limit of a [[function]], apply [[limit-rules]] recursively

### Limit Existence

$\lim_{x \to a}$ does not exist if any of the following is true:

- $\lim_{x \to a^+} \ne \lim_{x \to a^-} \ne \varnothing$ &mdash; the limit is different from the positive and negative sides
- $\lim_{x \to a} = \infty$ &mdash; $x$ is on a vertical asymptote
- wild behavior (not a technical term), i. e. $\lim_{x \to 0} \sin\ (\pi - x)$

if $g\ a = 0$, then $\lim_{x \to a} (f\ x - g\ x)$

- does not exist if $f\ a \ne 0$
- can exist if $f\ a = 0$. first simplify using the [[limit-rules]] and then study the limit

### tricks for computing a limit

for an $\infty - \infty$ indeterminate form (see [[rational-function]]):

- formal method: factor out the highest power in both the numerator and the denominator
- informal method: look at the highest degree of the numerator and of the denominator

for the addition or subtraction of fractions, try to use a common denominator

for subtraction of square roots, try to multiply by the conjugate
