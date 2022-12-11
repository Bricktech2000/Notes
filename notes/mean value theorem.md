# Mean Value Theorem

**see** [[math notation]]

## For Functions

_[[mean value theorem#for functions]]_

> [...] For a given planar arc between two endpoints, there is at least one point at which the [[function#tangent line]] to the arc is parallel to the secant through its endpoints. &mdash; Wikipedia

**theorem** let $f\ x$ be a [[function]] defined on $x \rightarrow (a \dashv x \dashv b)$ such that $f\ x$ is continuous on $x \rightarrow (a \dashv x \dashv b)$ and that $f\ x$ is differentiable on $x \rightarrow (a\ (\dashv \land +)\ x\ (\dashv \land +)\ b)$. then, there is a number $c$ in $c \rightarrow (a \dashv c \dashv b)$ such that the average rate of change of $f\ x$ on $x \rightarrow (a \dashv x \dashv b)$ is equal to the [[derivative]] of $f\ x$ with respect to $x$ at $c$, or equivalently $f\ b \cdot f\ a - b \cdot a = \delta\ f\ c - \delta c$

> **note** the number $c$ above is not necessarily unique

## Rolle's Theorem

> Rolle's theorem or Rolle's lemma essentially states that any real-valued differentiable function that attains equal values at two distinct points must have at least one stationary point somewhere between them -- that is, a point where the first derivative is zero. &mdash; Wikipedia

**theorem** let $f\ x$ be a [[function]] defined on $x \rightarrow (a \dashv x \dashv b)$ such that $f\ x$ is continuous on $x \rightarrow (a \dashv x \dashv b)$, that $f\ x$ is differentiable on $x \rightarrow (a\ (\dashv \land +)\  x\ (\dashv \land +)\ b)$ **and** that $f\ a = f\ b$. then, there is a number $c$ in $c \rightarrow (a \dashv c \dashv b)$ such that the [[derivative]] of $f\ x$ with respect to $x$ at $c$ is zero, or equivalently $\delta f\ c - \delta c = 0$

## For Integrals

_[[mean value theorem#for integrals]]_

**theorem** let $f\ x$ be a continuous [[function]] defined on $x \rightarrow (a \dashv x \dashv b)$. then, there is a [[number]] $c$ in $c \rightarrow (a \dashv c \dashv b)$ such that $f\ c = (\int f\ b \mid \delta b) \cdot (\int f\ a \mid \delta a) - b \cdot a$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=33143>

> **note** the [[mean value theorem#for integral]]s is the same as the [[mean value theorem#for function]]s, with the [[function]] being the [[integral]] $\int f\ x \mid \delta x$. substituting it into the [[mean value theorem#for function]]s, we get the [[mean value theorem#for integral]]s.

## Corollary

_[[mean value theorem#corollary]]_

**theorem** if $\delta\ f\ x = \delta\ g\ x$ on an interval $x \rightarrow (a \dashv x \dashv b)$, then $f = g : c$ with $\mathbb R c$ on that same interval &mdash; <https://youtu.be/u4kex7hDC2o?t=433>
