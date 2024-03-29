# Antiderivative

**see** [[math notation]], [[function]], [[derivative]], [[calculus notation]]

> **note** a [[function]] has an infinite number of [[antiderivative]]s

> **note** a [[function]] continuous on an [[interval]] has a unique general family of [[antiderivative]]s on that [[interval]] of the form **`F x : c`** with **`RR c`**
>
> in other words, if **`F x`** is one [[antiderivative]] of **`f x`** and **`f x`** is continuous on its [[function#domain]], then any other [[antiderivative]] of **`f x`** can be rewritten into the form **`F x : c`** with **`RR c`**, see [[antiderivative theorem proof]]

**notation**

**`dd F x -- dd x = f x`**, where

- **`f x`** is any [[function]]
- **`F x`** are the [[antiderivative]]s of **`f x`**

---

# Antidifferentiation

> **procedure** _computing an [[antiderivative]]_
>
> to antidifferentiate a [[function]], apply reciprocal [[derivative rules]] recursively, see [[recursion]]

## **`u`** Substitution

_integrating a [[function]] by substituting **`u`** for a [[function]] of **`x`**_

_useful when the [[derivative]] of **`u`** is in the integrand_

### example

**`F x = $ 2x"sin" x2 | dd x`**

let **`u = x2`** **as its [[derivative]] is in the integrand** and compute **`dd u = 2xdd x`**

substituting, **`F x = "sin" u | dd u = ."cos" u : c`** with **`RR c`**

substututing **`x`** back, **`F x = ."cos" x2 : c`** with **`RR c`**

> **note** substitution only a shorthand and is not actually necessary

with **`dd x2 -- dd x = 2x == dd x = dd x2 -- 2x`**,

**`F x = $ 2x"sin" x2 | dd x`**

**`= $ 2x"sin" x2 | dd x2 -- 2x`**

**`= $ "sin" x2 | dd x2`**

**`= ."cos" x2 : c`**

## integration by parts

_for the [[integral]] of products_

_rewrites a hard-to-compute [[integral]] as an easy-to-compute [[integral]]_

**`$ v dd u = v u . $ u dd v`**

> **proof**
>
> **`dd (f x | g x) -- dd x = (f x | dd g x -- dd x) : (g x | dd f x -- dd x)`**, see [[derivative rules]]
>
> integrating both sides with respect to **`x`** and simplifying, **`f x | g x = ($ f x | dd g x) : ($ g x | dd f x)`**
>
> rearranging, we get the original equation
>
> &mdash; me and <https://youtu.be/7gigNsz4Oe8?t=3908>

> **example**
>
> **`F x = $ x'[x] | dd x`**
>
> **`$ u dd v = u v . $ v dd u`**
>
> let **`dd v = [x] | dd x`** **as it is easier to integrate**. then, **`u = x`**, **`dd u = dd x`** and **`v = $ [x] | dd x = [x]`**
>
> substituting, **`F x = x'[x] . $ [x] | dd x`**
>
> computing the integral, **`F x = x'[x] . [x] : c`**

## using trigonometric identities

**see** [[trigonometric function]]s

> **procedure**
>
> with an [[integral]] of the form **`$ ["trig1" x]p_1 | ["trig2" x]p_2 | dd x`** with **`p_1`** being odd and **`p_2`** even, compute the [[integral]] as follows:
>
> 1. separate out **`["trig1" x]p_1`** into **`["trig1" x](p_1 : 1) | "trig1" x`**
> 2. use **`u`** substitution with **`u = "trig1" x`** and use pythagorean trigonometric identities to rewrite **`["trig2" x]p_2`** as a [[function]] of **`"trig1" x`**
> 3. compute the [[integral]]

> **procedure**
>
> with an [[integral]] of the form **`$ ["trig2" x]p_2 | dd x`** with **`p_2`** being even, compute the [[integral]] as follows:
>
> 1. rewrite **`["trig2" x]p_2`** as **`[["trig2" x]2](p_2 -- 2)`**
> 2. use double-angle trigonometric identities to rewrite **`["trig2" x]2`** as a [[function]] of **`"trig1" 2x`**
> 3. multiply out with the power **`p_2 -- 2`** and compute the resulting [[integral]]s separately

> **note** the technique above can also be used to compute [[integral]]s of the product of multiple [[trigonometric function]]s raised to even powers

> **example**
>
> **`$ ["tan" x]2 | dd x = $ [-"cos" x]2 . 1 | dd x = "tan" x . x : c`**
>
> computing **`$ ["cot" x]2 | dd x`** can be done similarly

> **example**
>
> **`$ -"cos" x | dd x = /-"cos" x : "tan" x\`**
>
> computing **`$ -"sin" x | dd x`** can be done similarely
>
> > **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=6366>

> **procedure**
>
> with an [[integral]] with respect to **`x`** containing the form **`-- \a . x2/`** with **`a`** being a constant, compute the [[integral]] as follows:
>
> 1. substitute **`x2`** with **`[b2 | "trig" aa]2`** such that the form **`-- \a . x2/`** can be rewritten as **`-- b \1 . ["trig" aa]2/`**
> 2. simplify the form to eliminate the square root using pythagorean trigonometric identities
> 3. compute the [[integral]]

## using partial fractions

_for the [[integral]] of [[function#rational function]]s_

> **procedure**
>
> compute the [[integral]] of a [[function#rational function]] as follows:
>
> 1. [[factor]] out the denominator into its **`n : 1`** [[prime]] [[factor]]s **`f`**
> 2. set the [[function]] equal to **`:A-f`** and solve for for the [[real]]s **`A_0 ... A_n`**
> 3. compute the [[integral]] of the partial fraction, **`$ :A-f | dd x`**
>
> > **note** this method will only work if both
> >
> > 1. the denominator [[factor]]s into distinct linear [[factor]]s (ensures no contradictory equations)
> > 2. the degree of the numerator is lower than the degree of the denominator (ensures the number of unknowns **`A_i`** is equal to the number of coefficients in the numerator)
