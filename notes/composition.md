# Composition

**see** [[math notation]], [[function]]

**equiv** _[[combinator#b combinator]]_

**definition** _composition in my [[math notation]]_

**`C f g = x -> f (g x)`**, where

- **`f`** and **`g`** are the original [[function]]s
- **`C`** is the [[composition]] [[function]]
- **`x`** is the parameter to be passed to **`f`** and **`g`**

**definition** _[[composition]] in Haskell_

`(.) :: (b -> c) -> (a -> b) -> a -> c`

> **example** _[[composition]] in Haskell_
>
> let `f :: A -> B` and `g :: B -> C`. then, `g . f` has type signature `A -> C`

**properties**

_associativity_ **`h (g f *) * == (h g *) f * == h g f *`** &mdash; <https://youtu.be/SmXB2K_5lcA?t=662>

**applications**

[[function]] [[composition]] is very useful in [[functional programming]] as it allows for building larger [[function]]s from smaller ones. it also allows for [[abstraction]] and encapsulation.

> **example** suppose we have two [[function]]s: **`A -> B`** and **`B -> C`**. after composing them, we get **`A -> C`**. there is no way to differentiate this [[function]] from any other [[function]], and the intermediate value **`B`** is not exposed to the outside world anymore

## Identity

**aka** _identity [[function]]_

**equiv** _[[combinator#i combinator]]_

**notation** **`{*}`**

**definition** **`{*}`**

**properties** **`{*} x == x`**
