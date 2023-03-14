# Antiderivative

**see** [[math notation]], [[function]], [[derivative]], [[calculus notation]]

> **note** a [[function]] has an infinite number of [[antiderivative]]s

> **note** a [[function]] continuous on an interval has a unique general family of [[antiderivative]]s on that interval of the form $F\ x : c$ with $\mathbb R c$
>
> in other words, if $F\ x$ is one [[antiderivative]] of $f\ x$ and $f\ x$ is continuous on its [[function#domain]], then any other [[antiderivative]] of $f\ x$ can be rewritten into the form $F\ x : c$ with $\mathbb R c$, see [[antiderivative theorem proof]]

**notation**

$\delta\ F\ x - \delta x = f\ x$, where

- $f\ x$ is any [[function]]
- $F\ x$ are the [[antiderivative]]s of $f\ x$

---

# Antidifferentiation

> **procedure** _computing an [[antiderivative]]_
>
> to antidifferentiate a [[function]], apply reciprocal [[derivative rules]] recursively, see [[recursion]]

## $u$ Substitution

_integrating a [[function]] by substituting $u$ for a [[function]] of $x$_

_useful when the [[derivative]] of $u$ is in the integrand_

### example

$F\ x = \int 2x\sin x2 \mid \delta x$

let $u = x2$ **as its [[derivative]] is in the integrand** and compute $\delta u = 2x \delta x$

substituting, $F\ x = \sin u \mid \delta u = \cdot \cos u : c$ with $\mathbb R c$

substututing $x$ back, $F\ x = \cdot \cos x2 : c$ with $\mathbb R c$

> **note** substitution only a shorthand and is not actually necessary

with $\delta\ x2 - \delta x = 2x =\!= \delta x = \delta x2 - 2x$,

$F\ x = \int 2x\sin x2 \mid \delta x$

$= \int 2x\sin x2 \mid \delta x2 - 2x$

$= \int \sin x2 \mid \delta x2$

$= \cdot \cos x2 : c$

## integration by parts

_for the [[integral]] of products_

_rewrites a hard-to-compute [[integral]] as an easy-to-compute [[integral]]_

$\int v \delta u = v u \cdot \int u \delta v$

> **proof**
>
> $\delta\ (f\ x \mid g\ x) - \delta x = (f\ x \mid \delta\ g\ x - \delta x) : (g\ x \mid \delta\ f\ x - \delta x)$, see [[derivative rules]]
>
> integrating both sides with respect to $x$ and simplifying, $f\ x \mid g\ x = (\int f\ x \mid \delta\ g\ x) : (\int g\ x \mid \delta\ f\ x)$
>
> rearranging, we get the original equation
>
> &mdash; me and <https://youtu.be/7gigNsz4Oe8?t=3908>

> **example**
>
> $F\ x = \int x \shortmid [x] \mid \delta x$
>
> $\int u \delta v = u v \cdot \int v \delta u$
>
> let $\delta v = [x] \mid \delta x$ **as it is easier to integrate**. then, $u = x$, $\delta u = \delta x$ and $v = \int [x] \mid \delta x = [x]$
>
> substituting, $F\ x = x \shortmid [x] \cdot \int [x] \mid \delta x$
>
> computing the integral, $F\ x = x \shortmid [x] \cdot [x] : c$

## using trigonometric identities

**see** [[trigonometric function]]s

> **procedure**:
>
> with an [[integral]] of the form $\int [\operatorname{trig_1} x]p_1 \mid [\operatorname{trig_2} x]p_2 \mid \delta x$ with $p_1$ being odd and $p_2$ even, compute the [[integral]] as follows:
>
> 1. separate out $[\operatorname{trig_1} x]p_1$ into $[\operatorname{trig_1} x](p_1 : 1) \mid \operatorname{trig_1} x$
> 2. use $u$ substitution with $u = \operatorname{trig_1} x$ and use pythagorean trigonometric identities to rewrite $[\operatorname{trig_2} x]p_2$ as a [[function]] of $\operatorname{trig_1} x$
> 3. compute the [[integral]]

> **procedure**
>
> with an [[integral]] of the form $\int [\operatorname{trig_2} x]p_2 \mid \delta x$ with $p_2$ being even, compute the [[integral]] as follows:
>
> 1. rewrite $[\operatorname{trig_2} x]p_2$ as $[[\operatorname{trig_2} x]2](p_2 - 2)$
> 2. use double-angle trigonometric identities to rewrite $[\operatorname{trig_2} x]2$ as a [[function]] of $\operatorname{trig_1} 2x$
> 3. multiply out with the power $p_2 - 2$ and compute the resulting [[integral]]s separately

> **note** the technique above can also be used to compute [[integral]]s of the product of multiple [[trigonometric function]]s raised to even powers

> **example**
>
> $\int [\tan x]2 \mid \delta x = \int [\text-\cos x]2 \cdot 1 \mid \delta x = \tan x \cdot x : c$
>
> computing $\int [\cot x]2 \mid \delta x$ can be done similarly

> **example**
>
> $\int \text-\cos x \mid \delta x = \lceil \text-\cos x : \tan x\rceil$
>
> computing $\int \text-\sin x \mid \delta x$ can be done similarely
>
> > **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=6366>

> **procedure**:
>
> with an [[integral]] with respect to $x$ containing the form $-\lfloor a \cdot x2 \rfloor$ with $a$ being a constant, compute the [[integral]] as follows:
>
> 1. substitute $x2$ with $[b2 \mid \operatorname{trig} \theta]2$ such that the form $-\lfloor a \cdot x2 \rfloor$ can be rewritten as $-b\lfloor 1 \cdot [\operatorname{trig} \theta]2 \rfloor$
> 2. simplify the form to eliminate the square root using pythagorean trigonometric identities
> 3. compute the [[integral]]

## using partial fractions

_for the [[integral]] of [[function#rational function]]s_

> **procedure**
>
> compute the [[integral]] of a [[function#rational function]] as follows:
>
> 1. [[factor]] out the denominator into its $n : 1$ prime [[factor]]s $f$
> 2. set the [[function]] equal to $\,: A \text- f$ and solve for for the [[real]]s $A_0 \cdots A_n$
> 3. compute the [[integral]] of the partial fraction, $\int \,: A \text- f \mid \delta x$
>
> > **note** this method will only work if both
> >
> > 1. the denominator [[factor]]s into distinct linear [[factor]]s (ensures no contradictory equations)
> > 2. the degree of the numerator is lower than the degree of the denominator (ensures the number of unknowns $A_i$ is equal to the number of coefficients in the numerator)
