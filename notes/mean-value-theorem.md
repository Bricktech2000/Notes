# Mean Value Theorem

see [[math-notation]]

## for Functions

_Mean Value Theorem for Functions_

> [...] For a given planar arc between two endpoints, there is at least one point at which the tangent to the arc is parallel to the secant through its endpoints. &mdash; Wikipedia

> **theorem**: let $f\ x$ be a [[function]] defined on $x \rarr (a \le x \le b)$ such that $f\ x$ is continuous on $x \rarr (a \le x \le b)$ and that $f\ x$ is differentiable on $x \rarr (a < x < b)$. then, there is a number $c$ in $c \rarr (a \le c \le b)$ such that the average rate of change of $f\ x$ on $x \rarr (a \le x \le b)$ is equal to the [[derivative]] of $f\ x$ with respect to $x$ at $c$, or $f\ b \cdot f\ a - b \cdot a = (x \rarr \delta\ f\ x - \delta x)\ c$

> **note**: the number $c$ above is not necessarily unique

## Rolle's Theorem

> Rolle's theorem or Rolle's lemma essentially states that any real-valued differentiable function that attains equal values at two distinct points must have at least one stationary point somewhere between them -- that is, a point where the first derivative is zero. &mdash; Wikipedia

> **theorem**: let $f\ x$ be a [[function]] defined on $x \rarr (a \le x \le b)$ such that $f\ x$ is continuous on $x \rarr (a \le x \le b)$, that $f\ x$ is differentiable on $x \rarr (a < x < b)$ **and** that $f\ a = f\ b$. then, there is a number $c$ in $c \rarr (a \le c \le b)$ such that the [[derivative]] of $f\ x$ with respect to $x$ at $c$ is zero, or $(x \rarr \delta f\ x - \delta x)\ c = 0$

## for Integrals

_Mean Value Theorem for Integrals_

> **theorem**: let $f\ x$ be a continuous [[function]] defined on $x \rarr (a \le x \le b)$. then, there is a [[number]] $c$ in $c \rarr (a \le c \le b)$ such that $f\ c = (x \rarr \int f\ x \mid \delta x)\ b \cdot (x \rarr \int f\ x \mid \delta x)\ a - b \cdot a$ &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=33143> (somewhat gross, #think)

> **note**: the [[mean-value-theorem]] for [[integral]]s is the same as the [[mean-value-theorem]] for [[function]]s, with the [[function]] being the [[integral]] $\int f\ x \mid \delta x$. substituting it into the [[mean-value-theorem]] for [[function]]s, we get the [[mean-value-theorem]] for [[integral]]s.

definite [[integral]]s [[math-notation]] #todo

## Corollary of Mean Value Theorem

> **theorem**: if $\delta\ f\ x = \delta\ g\ x$ on an open interval $x \rarr (a < x < b)$, then $f\ x = g\ x : c \land \mathbb R c$ on the same interval. &mdash; <https://youtu.be/u4kex7hDC2o?t=433>
