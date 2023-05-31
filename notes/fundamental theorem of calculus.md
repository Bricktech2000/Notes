# Fundamental Theorem of Calculus

**see** [[calculus notation]], [[math notation]]

**theorem** _Fundamental Theorem of Calculus, Part 1_ if **`f`** is continuous on **`a -| * -| b`**, then **`$ f t | dd t {x -> a}`** is continuous on **`a -| * -| b`** and differentiable on **`a {-|/\+} * {-|/\+} b`** and **`dd ($ f t | dd t {x . a}) -- dd x = f x`** (restrictions not necessary, see [[improved expression evaluation]])

> **proof**
>
> by definition, **`dd g x -- dd x = g (x : h) . g x -- h {h -> 0}`**
>
> with **`g x = F x = $ f x | dd x`**, we get **`F (x : h) . F a . (F x . F a) -- h {h -> 0} = F (x : h) . F x -- h {h -> 0}`**
>
> then,
>
> - as **`h -> 0`**, we approximate the definite [[integral]] with a rectangle and get **`(f x | h) -- h {h -> 0} = f x`**
> - more formally, let **`m`** be the minimum of **`f`** on **`x -| * -| x : h`** and **`M`** be the maximum of **`f`** on **`x -| * -| x : h`**. then, with the property **`m | h -| F (x : h) . F x -| M | h`** (can be seen graphically) we get **`m -| F (x : h) . F x -- h -| M`** for **`h -| 0`**. finally, by the [[intermediate value theorem]], we deduce that **`F (x : h) . F x -- h {h -> 0} = f c`** for some **`x -| c -| x : h`**, and therefore **`f c = f x`**
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

**theorem** _Fundamental Theorem of Calculus, Part 2_ if **`f`** is continuous on **`a -| * -| b`**, then **`$ f x | dd x {b . a} = F b . F a`** where **`F = $ f x | dd x`**, any [[antiderivative]] of **`f`**

> **proof**
>
> let **`F x = $ f t | dd t {x . a}`**. from the first part of the theorem, we get **`dd F x -- dd x = f x`**, meaning **`F x : c`** with **`RR c`** is the set of all [[antiderivative]]s of **`f`** by definition. then, **`(F b : c) . (F a : c) = F b . F a = ($ f t | dd t {b . a}) . ($ f t | dd t {a . a})`** by definition, and therefore **`F b . F a = $ f t | dd t {b . a}`**.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

> **note** I do not understand why the [[fundamental theorem of calculus]] has to be so complicated. the two properties defined in the note _[[calculus notation]]_ are all that is needed to derive the [[fundamental theorem of calculus]]. see [[integral]] for more details

> **note**
>
> _integrating_ refers to calculating the are under a [[function]], **not** computing the [[antiderivative]] and plugging stuff in. this is why indefinite [[integral]]s must include that **`... : c`** whereas [[antiderivative]]s don't have to
>
> _[[antiderivative]]s can be used to **find** [[area]]s ([[integral]]s) and [[area]]s ([[integral]]s) can be used to **define** [[antiderivative]]s._ this is the essence of the [[fundamental theorem of calculus]]
>
> I was taught [[integral]]s went hand-in-hand with [[derivative]]s, but I now see that [[integral]]s as we are taught them are a mere side effect of [[antiderivative]]s. what a mess!
>
> &mdash; me and <https://www.quora.com/Is-there-any-difference-whatsoever-between-an-indefinite-integral-and-an-antiderivative> and <https://socratic.org/questions/what-is-the-difference-between-an-antiderivative-and-an-integral>
