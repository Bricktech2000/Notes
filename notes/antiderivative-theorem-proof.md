# Antiderivative Theorem Proof

&mdash; <https://youtu.be/HfACrKJ_Y2w?t=38531>

#example, see backlink

> **theorem**: if $\delta\ g\ x - \delta x = 0$ on $x \rightarrow (a < x < b)$, then $g\ x = c$ with $\mathbb R c$

> **proof**:
>
> using the [[mean-value-theorem]], for any $x_1$ and $x_2$ in $x \rightarrow (a < x < b)$,
>
> $g\ x_2 \cdot g\ x_1 - x_2 \cdot x_1 = \delta\ g\ x_3 - \delta x_3$
>
> as $\delta\ g\ x - \delta x = 0$, $g\ x_2 \cdot g\ x_1 = 0$
>
> therefore, $g\ x_1 = g\ x_2 = c$, meaning $g\ x$ is a constant [[function]]

> **theorem**: if $g_1\ x$ and $g_2\ x$ are two [[function]]s defined on $x \rightarrow (a < x < b)$ and $\delta\ g_1\ x - \delta x = \delta\ g_2\ x - \delta x$ on $x \rightarrow (a < x < b)$, then $g_1\ x = g_2\ x : c$ with $\mathbb R c$

> **proof**:
>
> $\delta\ g_1\ x - \delta x = \delta\ g_2\ x - \delta x$
>
> $\equiv\ (\delta\ g_1\ x - \delta x) \cdot (\delta\ g_2\ x - \delta x) = 0$
>
> $\equiv\ \delta\ (g_1\ x \cdot g_2\ x) - \delta x = \delta\ 0 - \delta x = 0$
>
> using the first theorem, we deduce $g_1\ x \cdot g_2\ x = c$ with $\mathbb R c$
>
> therefore, $g_1\ x = g_2\ x : c$ with $\mathbb R c$
