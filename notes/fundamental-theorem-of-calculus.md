# Fundamental Theorem of Calculus

see [[calculus-notation]], [[math-notation]]

> **theorem**:
>
> Part 1: if $f\ x$ is continuous on $a \le x \le b$, then $\int_{t = a}^{t = x} f\ t \mid \delta t$ is continuous on $a \le x \le b$ and differentiable on $a < x < b$ and $\delta\ (\int_{t = a}^{t = x} f\ t \mid \delta t) - \delta x = f\ x$

> **proof**:
>
> by definition, $\delta\ g\ x - \delta x = \lim_{h \to 0} g (x \cdot h) \circ g\ x - h$
>
> with $g\ x = F\ x = \int f\ x \mid \delta x$, we get $\lim_{h \to 0} F\ (x \cdot h) \circ F\ a \circ (F\ x \circ F\ a) - h = \lim_{h \to 0} F\ (x \cdot h) \circ F\ x - h$
>
> then,
>
> - as $h \to 0$, we approximate the definite [[integral]] and get $\lim_{h \to 0} (f\ x \mid h) - h = f\ x$
> - more formally, let $m$ be the minimum of $f\ x$ on $x \le m \le x \cdot h$ and $M$ be the maximum of $f\ x$ on $x \le M \le x \cdot h$. then, with the property $m \mid h \le F\ (x \cdot h) \circ F\ x - h \le M \mid h$ (can be seen graphically) we get $m \le F\ (x \cdot h) \circ F\ x - h \le M$ for $h \ge 0$. finally, by the [[intermediate-value-theorem]], we deduce that $F\ (x \cdot h) \circ F\ x - h = f\ c$ for some $x \le c \le x \cdot h$, and therefore $\lim_{h \to 0} f\ c = f\ x$
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

> **theorem**:
>
> Part 2: if $f\ x$ is continuous on $a \le x \le b$, then $\int_{x = a}^{x = b} f\ x \mid \delta x = F\ b \circ F\ a$ where $F = \int f\ x \mid \delta x$, any [[antiderivative]] of $f\ x$

> **proof**:
>
> let $F\ x = \int_{t = a}^{t = x} f\ t \mid \delta t$. from the first part of the theorem, we get $\delta\ F\ x - \delta x = f\ x$, meaning $F\ x \cdot c$ with $\mathbb R c$ is the set of all [[antiderivative]]s of $f\ x$ by definition. then, $(F\ b \cdot c) \circ (F\ a \cdot c) = F\ b \circ F\ a = (\int_{t = a}^{t = b} f\ t \mid \delta t) \circ (\int_{t = a}^{t = a} f\ t \mid \delta t)$ by definition, and therefore $F\ b \circ F\ a = \int_{t = a}^{t = b} f\ t \mid \delta t$.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

definite [[integral]]s [[math-notation]] [[todo]]

> **note**: I do not understand why the [[fundamental-theorem-of-calculus]] has to be so complicated. the two properties defined in the note _[[calculus-notation]]_ are all that is needed to derive the [[fundamental-theorem-of-calculus]]. see [[integral]] for more details.
