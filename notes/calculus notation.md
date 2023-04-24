# Calculus Notation

**see** [[math notation]]

## notation

[[integral]] and [[derivative]] notation should be thought of as follows:

**`\d y -- \d x = (\d <- y) -- (\d <- x)`**

**`$ y | \d x = $ <- (y | (\d <- x))`**

> **note** when representing the [[derivative]] or [[integral]] of a [[function]], its parameter must be included. for example, **`\d f -- \d x`** is invalid whereas **`\d f x -- \d x`** is valid

> **note** by convention, a space is added when the parameter to a **`\d`** or a **`$`** is a [[function]]

derivatives and integrals at a point **`t`** can be written as follows:

**`(x -> \d y -- \d x) t`** or more concisely **`\d f t -- \d t`**

**`(x -> $ y | \d x) t`** or more concisely **`$ f t | \d t`**

### intuitive explanation

**`$`** and **`\d`** can be thought of as [[function]]s

**`$ y | \d x`** is actually **`$ (y | \d x)`** (**`| \d x`** is simply a multiplication, and is part of the argument to **`$`**)

**`\d y -- \d x`** is simply a division between the two values involved

**`(\d -- \d x) y`** alias $\frac{\delta}{\delta x} y$ ~~makes no sense whatsoever and is very likely some weird [[conventional math notation]] shorthand again~~ is superfluous notation and is to be avoided in my [[math notation]].

## properties with [[proof]]s

let **`UU c`**, see [[universal]], [[improved expression evaluation]]

**`$ \d y = y`**

**`\d $ y = y`**

**properties**

**see** [[integral]], [[derivative]], [[antiderivative]]

_the antiderivative of the derivative of a function is that same function_ (constant is not present, see [[improved expression evaluation]])

> **proof** **`$ (\d y -- \d x) | \d x = $ (\d y) = y`**

_the derivative of the antiderivative of a function is that same function_

> **proof** **`\d ($ y | \d x) -- \d x = y | \d x -- \d x = y`**
