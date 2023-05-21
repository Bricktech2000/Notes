# Derivative

**see** [[math notation]], [[derivative rules]], [[function]], [[calculus notation]]

**definition** _in my [[math notation]]_

**`dd f x -- dd x = f (x : h) . f x -- h {h -> 0} = f x . f a -- x . a {x -> a}`**

**definition** _with a multivariable [[function]] in my [[math notation]]_

let **`p = (x ...)`**

**`dd f p -- dd p = (dd f p -- dd p^0 , dd f p -- dd p^1 , ...)`**

**notations**

_[[conventional math notation]] Lagrange's notation_

$f'(x)$, $f''(x)$, $f'''(x)$

$f^{(n)}(x)$

_[[conventional math notation]] Leibniz's Notation_

$\frac{d}{dx}f(x) = \frac{df}{dx}$

$\frac{d^n}{dx^n} = \frac{d^nf}{dx^n}$

_in my [[math notation]]_

**`dd f x -- dd x`**, see [[calculus notation]]

**`d^n f = d^n.1 (x -> dd f x -- dd x) /\ d^0 f = f`**

**`d^n f`** would then be the **`n`**th [[derivative]] of **`f x`** with respect to **`x`**

## Directional Derivative

**see** [[gradient]]

**definition**

let **`f`** be a [[function]] differentiable at **`p = (x ...)`** and let **`v`** be a **[[vector in rn#unit vector]]**. then,

**`D^v f p = :v(dd f p -- dd p)`**, where

- **`D^v f p`** is the [[derivative]] of **`f`** in direction **`v`** at **`p`**
- **`dd f p -- dd p`** is the [[gradient]] of **`f`** at **`p`**
- **`v`** is the direction [[vector in rn]], see [[dot product]]

> **examples**
>
> **`D^1,0 f (x, y) = dd f (x, y) -- dd x`**
>
> **`D^0,1 f (x, y) = dd f (x, y) -- dd y`**

## Partial Derivative

> **note** partial differentiation is not a thing. unless I'm missing something major, all it means is:
>
> > differentiate this [[function]] with respect to this [[variable]], and please blindly assume the derivative of the [[variable]] with respect to any other parameter is **`0`**
>
> partial differentiation is equivalent to a [[derivative#directional derivative]] with direction **`(0 ... 0, 1, 0 ... 0)`**
>
> &mdash; <https://www.reddit.com/r/mathematics/comments/oxj88q/why_are_partial_derivatives_a_separate_thing_than/>

**notation**

_in [[conventional math notation]]_

in [[conventional math notation]], use the following abomination:

$f_x = f'_x = \partial_x f = D_x f = D_1 f = \frac{\partial}{\partial x}f = \frac{\partial f}{\partial x}$

$\frac{\partial^2 f}{\partial x^2} = f^n_{x x} = \partial_{x x} f = \partial^2_x f$ &mdash; Wikipedia

_in my [[math notation]]_

in my [[math notation]], it's just a [[derivative]]:

**`dd f x y -- dd x`**, see [[calculus notation]]

**definition**

the _partial derivative_ of **`f (x, y)`** with respect to **`x`** is defined as follows:

**`f (x : h, y) . f (x, y) -- h {h -> 0}`**

the same is true with any other parameter and with any number of parameters

---

# Differentiation

> **procedure** _computing a [[derivative]]_
>
> to differentiate a [[function]], apply [[derivative rules]] recursively, see [[recursion]]

## differentiability

**definition** a [[function]] **`f`** is _differentiable_ at **`a`** if **`dd f a -- dd x`** exists

**definition** a [[function]] is _differentiable_ on an interval **`a -| * -| b`** if it is differentiable on every point from **`a`** to **`b`**

**theorem** if **`f x`** is not continuous at **`x = a`**, then it is not differentiable at **`x = a`**

**theorem** if **`f x`** is differentiable at **`x = a`**, then it is continuous at **`x = a`**

**theorem** if **`f x`** is continuous at **`x = a`**, then it may or may not be differentiable at **`x = a`**

## Logarithmic Differentiation

_differentiating the [[logarithm]] of a [[function]] instead of the [[function]] itself_

**application**

useful for computing the [[derivative]] of an [[exponent]]ial [[function]]

**examples**

> **example** _logarithmic differentiation of **`x[ee[x]]`**_
>
> **`y = x[ee[x]]`**
>
> **`/y\ = /x[ee[x]]\ = /x\ ee[x]`**
>
> **`dd /y\ -- dd x = dd /x\ ee[x] -- dd x`**
>
> **`--y | dd y -- dd x = -xee[x] : /x\ ee[x]`**
>
> **`dd y -- dd x = x[ee[x]] | -xee[x] : /x\ ee[x]`**
>
> the alternative would be the following, by transforming and using the chain [[derivative rules]]:
>
> **`y = x[ee[x]]`**
>
> **`x[ee[x]] = ee[ /x[ee[x]]\ ] = ee[ /x\ ee[x]]`**
>
> **`dd y -- dd x = dd ee[ /x\ ee[x]] -- dd x`**
>
> **`dd y -- dd x = ee[ /x\ ee[x]] | dd /x\ ee[x] -- dd x`**
>
> **`dd y -- dd x = x[ee[x]] | -xee[x] : /x\ ee[x]`**

> **example** _logarithmic differentiation of **`[x]x`**_
>
> **`y = [x]x`**
>
> **`/y\ = x /x\`**
>
> **`dd /y\ -- dd x = dd x /x\ -- dd x`**
>
> **`--y | dd y -- dd x = 1 : /x\`**
>
> **`dd y -- dd x = y | 1 : /x\ = [x]x | 1 : /x\`**

## Implicit Differentiation

differentiation of an implicit equation (where the dependent [[variable]] is not isolated). works with both [[function]]s and [[relation]]s that aren't [[function]]s.

> **example**
>
> **`x2 : y2 = 2`**
>
> **`dd (x2 : y2) -- dd x = dd 2 -- dd x`**
>
> **`2x : 2y(dd y -- dd x) = 0`**
>
> **`dd y -- dd x = .x -- y`**
>
> or alternatively,
>
> **`x2 : y2 = 2`**
>
> **`dd x2 : dd y2 = dd 2`**
>
> **`2x dd x : 2y dd y = 0`**
>
> **`dd y -- dd x = .x -- y`**
>
> > **note** as both **`x`** and **`y`** are present in the equation, the [[derivative]] at **`.y`** will be different from the one at **`y`**
