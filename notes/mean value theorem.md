# Mean Value Theorem

**see** [[math notation]]

## For Functions

_[[mean value theorem#for functions]]_

> [...] For a given planar arc between two endpoints, there is at least one point at which the [[function#tangent line]] to the arc is parallel to the secant through its endpoints. &mdash; Wikipedia

**theorem** let $f\ x$ be a [[function]] defined on $x \rightarrow (a \le x \le b)$ such that $f\ x$ is continuous on $x \rightarrow (a \le x \le b)$ and that $f\ x$ is differentiable on $x \rightarrow (a < x < b)$. then, there is a number $c$ in $c \rightarrow (a \le c \le b)$ such that the average rate of change of $f\ x$ on $x \rightarrow (a \le x \le b)$ is equal to the [[derivative]] of $f\ x$ with respect to $x$ at $c$, or $f\ b \cdot f\ a - b \cdot a = (x \rightarrow \delta\ f\ x - \delta x)\ c$

> **note** the number $c$ above is not necessarily unique

## Rolle's Theorem

> Rolle's theorem or Rolle's lemma essentially states that any real-valued differentiable function that attains equal values at two distinct points must have at least one stationary point somewhere between them -- that is, a point where the first derivative is zero. &mdash; Wikipedia

**theorem** let $f\ x$ be a [[function]] defined on $x \rightarrow (a \le x \le b)$ such that $f\ x$ is continuous on $x \rightarrow (a \le x \le b)$, that $f\ x$ is differentiable on $x \rightarrow (a < x < b)$ **and** that $f\ a = f\ b$. then, there is a number $c$ in $c \rightarrow (a \le c \le b)$ such that the [[derivative]] of $f\ x$ with respect to $x$ at $c$ is zero, or $(x \rightarrow \delta f\ x - \delta x)\ c = 0$

## For Integrals

_[[mean value theorem#for integrals]]_

**theorem** let $f\ x$ be a continuous [[function]] defined on $x \rightarrow (a \le x \le b)$. then, there is a [[number]] $c$ in $c \rightarrow (a \le c \le b)$ such that $f\ c = (x \rightarrow \int f\ x \mid \delta x)\ b \cdot (x \rightarrow \int f\ x \mid \delta x)\ a - b \cdot a$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=33143> (somewhat gross, #think)

> **note** the [[mean value theorem]] for [[integral]]s is the same as the [[mean value theorem]] for [[function]]s, with the [[function]] being the [[integral]] $\int f\ x \mid \delta x$. substituting it into the [[mean value theorem]] for [[function]]s, we get the [[mean value theorem]] for [[integral]]s.

## Corollary

_[[mean value theorem#corollary]]_

**theorem** if $\delta\ f\ x = \delta\ g\ x$ on an open interval $x \rightarrow (a < x < b)$, then $f\ x = g\ x : c \land \mathbb R c$ on the same interval. &mdash; <https://youtu.be/u4kex7hDC2o?t=433>
