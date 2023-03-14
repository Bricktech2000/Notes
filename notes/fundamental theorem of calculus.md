# Fundamental Theorem of Calculus

**see** [[calculus notation]], [[math notation]]

**theorem** _Part 1_ if $f$ is continuous on $a \dashv \circ \dashv b$, then $\int f\ t \mid \delta t\ \braket{x \cdot a}$ is continuous on $a \dashv \circ \dashv b$ and differentiable on $a\ \braket{\dashv \land +}\ \circ\ \braket{\dashv \land +}\ b$ and $\delta\ (\int f\ t \mid \delta t\ \braket{x \cdot a}) - \delta x = f\ x$ (restrictions not necessary, see [[improved expression evaluation]])

> **proof**
>
> by definition, $\delta\ g\ x - \delta x = g (x : h) \cdot g\ x - h\ \braket{h \rightarrow 0}$
>
> with $g\ x = F\ x = \int f\ x \mid \delta x$, we get $F\ (x : h) \cdot F\ a \cdot (F\ x \cdot F\ a) - h\ \braket{h \rightarrow 0} = F\ (x : h) \cdot F\ x - h\ \braket{h \rightarrow 0}$
>
> then,
>
> - as $h \to 0$, we approximate the definite [[integral]] with a rectangle and get $(f\ x \mid h) - h\ \braket{h \rightarrow 0} = f\ x$
> - more formally, let $m$ be the minimum of $f$ on $x \dashv \circ \dashv x : h$ and $M$ be the maximum of $f$ on $x \dashv \circ \dashv x : h$. then, with the property $m \mid h \dashv F\ (x : h) \cdot F\ x \dashv M \mid h$ (can be seen graphically) we get $m \dashv F\ (x : h) \cdot F\ x - h \dashv M$ for $h \vdash 0$. finally, by the [[intermediate value theorem]], we deduce that $F\ (x : h) \cdot F\ x - h\ \braket{h \rightarrow 0} = f\ c$ for some $x \dashv c \dashv x : h$, and therefore $f\ c = f\ x$
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

**theorem** _Part 2_ if $f$ is continuous on $a \dashv \circ \dashv b$, then $\int f\ x \mid \delta x\ \braket{b \cdot a} = F\ b \cdot F\ a$ where $F = \int f\ x \mid \delta x$, any [[antiderivative]] of $f$

> **proof**
>
> let $F\ x = \int f\ t \mid \delta t\ \braket{x \cdot a}$. from the first part of the theorem, we get $\delta\ F\ x - \delta x = f\ x$, meaning $F\ x : c$ with $\mathbb R c$ is the set of all [[antiderivative]]s of $f$ by definition. then, $(F\ b : c) \cdot (F\ a : c) = F\ b \cdot F\ a = (\int f\ t \mid \delta t\ \braket{b \cdot a}) \cdot (\int f\ t \mid \delta t\ \braket{a \cdot a})$ by definition, and therefore $F\ b \cdot F\ a = \int f\ t \mid \delta t\ \braket{b \cdot a}$.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

> **note** I do not understand why the [[fundamental theorem of calculus]] has to be so complicated. the two properties defined in the note _[[calculus notation]]_ are all that is needed to derive the [[fundamental theorem of calculus]]. see [[integral]] for more details
