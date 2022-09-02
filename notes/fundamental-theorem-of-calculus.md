# Fundamental Theorem of Calculus

see [[calculus-notation]], [[math-notation]]

**theorem** _Part 1_ if $f\ x$ is continuous on $x \rightarrow (a \le x \le b)$, then $\int_{t = a}^{t = x} f\ t \mid \delta t$ is continuous on $x \rightarrow (a \le x \le b)$ and differentiable on $x \rightarrow (a < x < b)$ and $\delta\ (\int_{t = a}^{t = x} f\ t \mid \delta t) - \delta x = f\ x$

> **proof**
>
> by definition, $\delta\ g\ x - \delta x = \lim_{h \to 0} g (x : h) \cdot g\ x - h$
>
> with $g\ x = F\ x = \int f\ x \mid \delta x$, we get $\lim_{h \to 0} F\ (x : h) \cdot F\ a \cdot (F\ x \cdot F\ a) - h = \lim_{h \to 0} F\ (x : h) \cdot F\ x - h$
>
> then,
>
> - as $h \to 0$, we approximate the definite [[integral]] and get $\lim_{h \to 0} (f\ x \mid h) - h = f\ x$
> - more formally, let $m$ be the minimum of $f\ x$ on $x \le m \le x : h$ and $M$ be the maximum of $f\ x$ on $x \le M \le x : h$. then, with the property $m \mid h \le F\ (x : h) \cdot F\ x - h \le M \mid h$ (can be seen graphically) we get $m \le F\ (x : h) \cdot F\ x - h \le M$ for $h \ge 0$. finally, by the [[intermediate-value-theorem]], we deduce that $F\ (x : h) \cdot F\ x - h = f\ c$ for some $x \le c \le x : h$, and therefore $\lim_{h \to 0} f\ c = f\ x$
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

**theorem** _Part 2_ if $f\ x$ is continuous on $x \rightarrow (a \le x \le b)$, then $\int_{x = a}^{x = b} f\ x \mid \delta x = F\ b \cdot F\ a$ where $F = \int f\ x \mid \delta x$, any [[antiderivative]] of $f\ x$

> **proof**
>
> let $F\ x = \int_{t = a}^{t = x} f\ t \mid \delta t$. from the first part of the theorem, we get $\delta\ F\ x - \delta x = f\ x$, meaning $F\ x : c$ with $\mathbb R c$ is the set of all [[antiderivative]]s of $f\ x$ by definition. then, $(F\ b : c) \cdot (F\ a : c) = F\ b \cdot F\ a = (\int_{t = a}^{t = b} f\ t \mid \delta t) \cdot (\int_{t = a}^{t = a} f\ t \mid \delta t)$ by definition, and therefore $F\ b \cdot F\ a = \int_{t = a}^{t = b} f\ t \mid \delta t$.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

definite [[integral]]s [[math-notation]] #todo

> **note** I do not understand why the [[fundamental-theorem-of-calculus]] has to be so complicated. the two properties defined in the note _[[calculus-notation]]_ are all that is needed to derive the [[fundamental-theorem-of-calculus]]. see [[integral]] for more details.
