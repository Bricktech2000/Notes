# Fundamental Theorem of Calculus

**see** [[calculus notation]], [[math notation]]

**theorem** _Fundamental Theorem of Calculus, Part 1_ if **`f`** is continuous on **`a -| * -| b`**, then **`$ f {x..a}`** is continuous on **`a -| * -| b`** and differentiable on **`a {-|/\+} * {-|/\+} b`** and **`dd x. $ f {x..a} = f`** (restrictions not necessary, see [[improved expression evaluation]])

> **proof**
>
> by definition, **`dd g x = g {x:h..x} -- h {h -> 0}`** #todo lim
>
> with **`g x = $ f {x..a}`**, we get **`dd g x = $ f {x:h..a} .. $ f {x..a} -- h {h -> 0} = $ f {x:h..x} -- h {h -> 0}`** #todo lim
>
> then, either
>
> - as **`h -> 0`**, we approximate the definite [[integral]] with a rectangle and get **`(f x | h) -- h {h -> 0} = f x`** #todo lim
> - more formally, let **`m`** be the minimum of **`f`** on **`x -| * -| x : h`** and **`M`** be the maximum of **`f`** on **`x -| * -| x : h`**. then, with the property **`m | h -| $ f {x:h..x} -| M | h`** (can be seen graphically) we get **`m -| $ f {x:h..x} -- h -| M`** for **`h -| 0`**. finally, by the [[intermediate value theorem]], we deduce that **`F {x:h..x} -- h {h -> 0} = f c`** #todo lim for some **`x -| c -| x : h`**, and therefore **`f c = f x`**
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

**theorem** _Fundamental Theorem of Calculus, Part 2_ if **`f`** is continuous on **`a -| * -| b`**, then **`$ f {b .. a} = $ f b .. $ f a`** where **`$ f`**, is any [[antiderivative]] of **`f`**

> **proof**
>
> let **`F x = $ f {x..a}`**. from the first part of the theorem, we get **`dd F = f`**, meaning **`F x : c`** with **`RR c`** is the set of all [[antiderivative]]s of **`f`** by definition. then, **`(F b : c) .. (F a : c) = F b .. F a = $ f {b..a} .. $ f {a..a}`** by definition, and therefore **`$ f b .. $ f a = $ f {b..a}`**.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

> **note** I do not understand why the [[fundamental theorem of calculus]] has to be so complicated. the two properties defined in the note _[[calculus notation]]_ are all that is needed to derive the [[fundamental theorem of calculus]]. see [[integral]] for more details

> **note**
>
> _integrating_ refers to calculating the are under a [[function]], **not** computing the [[antiderivative]] and plugging stuff in. this is why indefinite [[integral]]s must include that **`... : c`** whereas [[antiderivative]]s do not
>
> _[[antiderivative]]s can be used to **compute** [[area]]s ([[integral]]s) and [[area]]s ([[integral]]s) can be used to **define** [[antiderivative]]s._ this is the essence of the [[fundamental theorem of calculus]]
>
> I was taught [[integral]]s went hand-in-hand with [[derivative]]s, but I now see that [[integral]]s as we are taught them are a mere side effect of [[antiderivative]]s. what a mess!
>
> &mdash; me and <https://www.quora.com/Is-there-any-difference-whatsoever-between-an-indefinite-integral-and-an-antiderivative> and <https://socratic.org/questions/what-is-the-difference-between-an-antiderivative-and-an-integral>
