# Antiderivative

**see** [[math notation]], [[function]], [[derivative]], [[calculus notation]]

> **note** a [[function]] has an infinite number of [[antiderivative]]s

> **note** a [[function]] continuous on an [[interval]] has a unique general family of [[antiderivative]]s on that [[interval]] of the form **`F x : c`** with **`RR c`**
>
> in other words, if **`F x`** is one [[antiderivative]] of **`f x`** and **`f x`** is continuous on its [[function#domain]], then any other [[antiderivative]] of **`f x`** can be rewritten into the form **`F x : c`** with **`RR c`**, see [[antiderivative theorem proof]]

**notation**

**`dd F = f`**, where #todo inv

- **`f`** is any [[function]]
- **`F`** are the [[antiderivative]]s of **`f x`**

---

# Antidifferentiation

**procedure** _computing an [[antiderivative]]_ reciprocal [[derivative rules]] recursively

## **`u`** substitution

_integrating a [[function]] by substituting **`u`** for a [[function]] of **`x`**_

_useful when the [[derivative]] of **`u`** is in the integrand_

**``$ f = $ (f -- dd u \\ `u) \\ u``** #todo inv &mdash; me

> **proof** #todo inv
>
> **``$ f = $dd ($ f \\ `u) \\ u``** by [[composition]] identities
>
> **``= $ (f \\ `u | dd `u) \\ u``** by the chain [[derivative rules]]
>
> **``= $ (f \\ `u -- (dd u \\ `u)) \\ u``** by the inverse [[derivative rules]]
>
> **``= $ (f -- dd u \\ `u) \\ u``** since **``f`h -- g`h = f-g \\ h``**
>
> &mdash; me

> **example**
>
> **`F = $ x. 2x"sin" x2`**
>
> let **`u = x. x2`** **as its [[derivative]] is in the integrand** and compute **`dd u = x. 2x`**
>
> substituting, **`F = $ ((x. 2x"sin" x2) -- (x. 2x) \\ (x2. x)) \\ (x. x2)`**
>
> computing the integral, **`F = $ (x. "sin" x) \\ (x. x2) = x. c.."cos" x2`** with **`RR c`**

## integration by parts

_for the [[integral]] of products_

_rewrites a hard-to-compute [[integral]] as an easy-to-compute [[integral]]_

**`$ v'dd u = u'v .. $ u'dd v`**

> **proof** integrate both sides of the product [[derivative rules]] &mdash; me and <https://youtu.be/7gigNsz4Oe8?t=3908>

> **example**
>
> **`F = $ x. x'[x]`**
>
> let **`dd v = x. [x]`** **as it is easier to integrate**. then, **`u = x. x`**, **`dd u = x. 1`** and **`v = $ x. [x] = x. [x]`**
>
> substituting, **`F = (x. x)(x. [x]) .. $ (x. [x])(x. 1)`**
>
> computing the integral, **`F = x. x'[x] .. [x] : c`** with **`RR c`**

## using trigonometric identities

**see** [[trigonometric function]]s

> **procedure**
>
> with an [[integral]] of the form **`$ x. ["trig1" x]p_1 | ["trig2" x]p_2`** with **`p_1`** being odd and **`p_2`** even, compute the [[integral]] as follows:
>
> 1. separate out **`["trig1" x]p_1`** into **`["trig1" x](p_1 : 1) | "trig1" x`**
> 2. use **`u`** substitution with **`u = "trig1" x`** and use pythagorean trigonometric identities to rewrite **`["trig2" x]p_2`** as a [[function]] of **`"trig1" x`**
> 3. compute the [[integral]]

> **procedure**
>
> with an [[integral]] of the form **`$ x. ["trig2" x]p_2`** with **`p_2`** being even, compute the [[integral]] as follows:
>
> 1. rewrite **`["trig2" x]p_2`** as **`[["trig2" x]2](p_2 -- 2)`**
> 2. use double-angle trigonometric identities to rewrite **`["trig2" x]2`** as a [[function]] of **`"trig1" 2x`**
> 3. multiply out with the power **`p_2 -- 2`** and compute the resulting [[integral]]s separately

> **note** the technique above can also be used to compute [[integral]]s of the product of multiple [[trigonometric function]]s raised to even powers

> **example**
>
> **`$ "tan"2 = $ -"cos"2 .. 1 = x. "tan" x .. x : c`**
>
> computing **`$ "cot"2`** can be done similarly

> **example**
>
> **`$ -"cos" = /-"cos" : "tan"\`**
>
> computing **`$ -"sin"`** can be done similarely
>
> > **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=6366>

> **procedure**
>
> with an [[integral]] with respect to **`x`** containing the form **`-- \a .. x2/`** with **`a`** being a constant, compute the [[integral]] as follows:
>
> 1. substitute **`x2`** with **`[b2 | "trig" aa]2`** such that the form **`-- \a .. x2/`** can be rewritten as **`-- b \1 .. ["trig" aa]2/`**
> 2. simplify the form to eliminate the square root using pythagorean trigonometric identities
> 3. compute the [[integral]]

## using partial fractions

_for the [[integral]] of rational [[function]]s_

> **procedure**
>
> compute the [[integral]] of a rational [[function]] as follows:
>
> 1. [[factor]] out the denominator into its [[list]] of **`n : 1`** [[prime]] [[factor]]s **`f`**
> 2. set the [[function]] equal to **`:A-f`** and solve for for the [[list]] of [[real]]s **`A`**
> 3. compute the [[integral]] of the partial fraction, **`$ :A-f`**
>
> > **note** this method will only work if both
> >
> > 1. the denominator [[factor]]s into distinct linear [[factor]]s (ensures no contradictory equations)
> > 2. the degree of the numerator is lower than the degree of the denominator (ensures the number of unknowns is equal to the number of coefficients in the numerator)
