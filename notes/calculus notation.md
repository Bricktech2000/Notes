# Calculus Notation

**see** [[math notation]]

## notation

[[integral]] and [[derivative]] notation should be thought of as follows:

**`dd y -- dd x = (dd <- y) -- (dd <- x)`**

**`$ y | dd x = $ <- (y | (dd <- x))`**

> **note** when representing the [[derivative]] or [[integral]] of a [[function]], its parameter must be included. for example, **`dd f -- dd x`** is invalid whereas **`dd f x -- dd x`** is valid

> **note** by convention, a space is added when the parameter to a **`dd`** or a **`$`** is a [[function]]

derivatives and integrals at a point **`t`** can be written as follows:

**`(x -> dd y -- dd x) t`** or more concisely **`dd f t -- dd t`**

**`(x -> $ y | dd x) t`** or more concisely **`$ f t | dd t`**

### intuitive explanation

**`$`** and **`dd`** can be thought of as [[function]]s

**`$ y | dd x`** is actually **`$ (y | dd x)`** (**`| dd x`** is simply a multiplication, and is part of the argument to **`$`**)

**`dd y -- dd x`** is simply a division between the two values involved

**`(dd -- dd x) y`** alias $\frac{\delta}{\delta x} y$ ~~makes no sense whatsoever and is very likely some weird [[conventional math notation]] shorthand again~~ is superfluous notation and is to be avoided in my [[math notation]]

## properties with [[proof]]s

let **`UU c`**, see [[set#universal set]], [[improved expression evaluation]]

**`$ dd y = y`**

**`dd $ y = y`**

**properties**

**see** [[integral]], [[derivative]], [[antiderivative]]

_the antiderivative of the derivative of a function is that same function_ (constant is not present, see [[improved expression evaluation]])

> **proof** **`$ (dd y -- dd x) | dd x = $ (dd y) = y`**

_the derivative of the antiderivative of a function is that same function_

> **proof** **`dd ($ y | dd x) -- dd x = y | dd x -- dd x = y`**
