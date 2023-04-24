# Fundamental Theorem of Calculus

**see** [[calculus notation]], [[math notation]]

**theorem** _Fundamental Theorem of Calculus, Part 1_ if **`f`** is continuous on **`a -| * -| b`**, then **`$ f t | \d t {x -> a}`** is continuous on **`a -| * -| b`** and differentiable on **`a {-|/\+} * {-|/\+} b`** and **`\d ($ f t | \d t {x . a}) -- \d x = f x`** (restrictions not necessary, see [[improved expression evaluation]])

> **proof**
>
> by definition, **`\d g x -- \d x = g (x : h) . g x -- h {h -> 0}`**
>
> with **`g x = F x = $ f x | \d x`**, we get **`F (x : h) . F a . (F x . F a) -- h {h -> 0} = F (x : h) . F x -- h {h -> 0}`**
>
> then,
>
> - as **`h -> 0`**, we approximate the definite [[integral]] with a rectangle and get **`(f x | h) -- h {h -> 0} = f x`**
> - more formally, let **`m`** be the minimum of **`f`** on **`x -| * -| x : h`** and **`M`** be the maximum of **`f`** on **`x -| * -| x : h`**. then, with the property **`m | h -| F (x : h) . F x -| M | h`** (can be seen graphically) we get **`m -| F (x : h) . F x -- h -| M`** for **`h -| 0`**. finally, by the [[intermediate value theorem]], we deduce that **`F (x : h) . F x -- h {h -> 0} = f c`** for some **`x -| c -| x : h`**, and therefore **`f c = f x`**
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=40945>

**theorem** _Fundamental Theorem of Calculus, Part 2_ if **`f`** is continuous on **`a -| * -| b`**, then **`$ f x | \d x {b . a} = F b . F a`** where **`F = $ f x | \d x`**, any [[antiderivative]] of **`f`**

> **proof**
>
> let **`F x = $ f t | \d t {x . a}`**. from the first part of the theorem, we get **`\d F x -- \d x = f x`**, meaning **`F x : c`** with **`RR c`** is the set of all [[antiderivative]]s of **`f`** by definition. then, **`(F b : c) . (F a : c) = F b . F a = ($ f t | \d t {b . a}) . ($ f t | \d t {a . a})`** by definition, and therefore **`F b . F a = $ f t | \d t {b . a}`**.
>
> &mdash; <https://youtu.be/HfACrKJ_Y2w?t=41225>

> **note** I do not understand why the [[fundamental theorem of calculus]] has to be so complicated. the two properties defined in the note _[[calculus notation]]_ are all that is needed to derive the [[fundamental theorem of calculus]]. see [[integral]] for more details
