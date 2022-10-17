# Fundamental Theorem of Calculus

see [[calculus notation]], [[math notation]]

**theorem** _Part 1_ if $f\ x$ is continuous on $x \rightarrow (a \le x \le b)$, then $\int f\ t \mid \delta t\ \ \vdots\ \ x \cdot a$ is continuous on $x \rightarrow (a \le x \le b)$ and differentiable on $x \rightarrow (a < x < b)$ and $\delta\ (\int f\ t \mid \delta t\ \ \vdots\ \ x \cdot a) - \delta x = f\ x$ (restrictions not necessary, see [[improved expression evaluation]])

> **proof**
>
> by definition, $\delta\ g\ x - \delta x = g (x : h) \cdot g\ x - h\ \ \vdots\ \ h \rightarrow 0$
>
> with $g\ x = F\ x = \int f\ x \mid \delta x$, we get $F\ (x : h) \cdot F\ a \cdot (F\ x \cdot F\ a) - h\ \ \vdots\ \ h \rightarrow 0 = F\ (x : h) \cdot F\ x - h\ \ \vdots\ \ h \rightarrow 0$
>
> then,
>
> - as $h \to 0$, we approximate the definite [[integral]] and get $(f\ x \mid h) - h\ \ \vdots\ \ h \rightarrow 0 = f\ x$
> - more formally, let $m$ be the minimum of $f\ x$ on $x \le m \le x : h$ and $M$ be the maximum of $f\ x$ on $x \le M \le x : h$. then, with the property $m \mid h \le F\ (x : h) \cdot F\ x - h \le M \mid h$ (can be seen graphically) we get $m \le F\ (x : h) \cdot F\ x - h \le M$ for $h \ge 0$. finally, by the [[intermediate value theorem]], we deduce that $F\ (x : h) \cdot F\ x - h\ \ \vdots\ \ h \rightarrow 0 = f\ c$ for some $x \le c \le x : h$, and therefore $f\ c = f\ x$
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

**theorem** _Part 2_ if $f\ x$ is continuous on $x \rightarrow (a \le x \le b)$, then $\int f\ x \mid \delta x\ \ \vdots\ \ b \cdot a = F\ b \cdot F\ a$ where $F = \int f\ x \mid \delta x$, any [[antiderivative]] of $f\ x$

> **proof**
>
> let $F\ x = \int f\ t \mid \delta t\ \ \vdots\ \ x \cdot a$. from the first part of the theorem, we get $\delta\ F\ x - \delta x = f\ x$, meaning $F\ x : c$ with $\mathbb R c$ is the set of all [[antiderivative]]s of $f\ x$ by definition. then, $(F\ b : c) \cdot (F\ a : c) = F\ b \cdot F\ a = (\int f\ t \mid \delta t\ \ \vdots\ \ b \cdot a) \cdot (\int f\ t \mid \delta t\ \ \vdots\ \ a \cdot a)$ by definition, and therefore $F\ b \cdot F\ a = \int f\ t \mid \delta t\ \ \vdots\ \ b \cdot a$.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

definite [[integral]]s [[math notation]] #todo

> **note** I do not understand why the [[fundamental theorem of calculus]] has to be so complicated. the two properties defined in the note _[[calculus notation]]_ are all that is needed to derive the [[fundamental theorem of calculus]]. see [[integral]] for more details.
