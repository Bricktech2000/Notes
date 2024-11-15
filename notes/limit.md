# Limit

**see** [[math notation]], [[limit rules]]

**notation** _the limit of **`f x`** as **`x`** approaches **`a`**_

**`f x {x -> a}`**

**definition** _**`(ee, dd)`** definition of a limit_

let **`f x`** be a [[function]] with [[function#domain]] **`D`** defined on an open [[interval]] around **`x_0`**. then, **`f x {x -> x_0} = L`** if for every **`ee {|-/\+} 0`** there exists a **`dd {|-/\+} 0`** such that **`0 + |x . x_0| -| dd < |f x . L| -| ee`** for all **`D x`**

--- <https://brilliant.org/wiki/epsilon-delta-definition-of-a-limit/>

## Indeterminate Form

**definition** a [[limit]] of the form **`f x -- g x {x -> a}`** is called a _**`0 -- 0`** indeterminate form_ if **`f x {x -> a} = 0`** and **`g x {x -> a} = 0`**

**definition** a [[limit]] of the form **`f x -- g x {x -> a}`** is called an _**`@@ -- @@`** indeterminate form_ if **`f x {x -> a} = @@`** and **`g x {x -> a} = @@`**

## computing a limit

> **procedure** _computing a [[limit]]_
>
> to compute the [[limit]] of a [[function]], apply [[limit rules]] recursively, see [[recursion]]

### Existence

**definition** a [[limit]] **`f x {x -> a}`** _does not exist_ if **`f x -> L_1`** as **`x -> x_0`** along a path **`C_1`** and **`f x -> L_2`** as **`x -> x_0`** along a path **`C_2`** and **`L_1 + L_2`** --- the value of the limit is different depending on the path taken

> **note** a limit does not exist if **`f x {x -> a} = @@`** or if it shows wild behavior (not a technical term), as with **`"sin" tt-x {x -> 0}`**
>
> > **note** what if **`"sin" tt-x {x -> 0}`** is a superposition of all numbers in **`0 -| * -| 1`**? #xxx [[improved expression evaluation]]

## limits of trigonometric functions

**see** [[trigonometric function]]

let **`aa`** be an angle in radians

**`"sin" aa -- aa {aa -> 0} = 1`**

> **proof** --- <https://youtu.be/HfACrKJ_Y2w?t=20802>

**`"cos" (aa . 1) -- aa {aa -> 0} = 0`**

> **proof** --- <https://youtu.be/HfACrKJ_Y2w?t=21029>
