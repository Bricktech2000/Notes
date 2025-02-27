# Composition

**see** [[math notation]], [[function]]

**equiv** _[[combinator#b combinator]]_

**definition** _composition in my [[math notation]]_

**``f`g = x. f (g x)``**, where

- **`f`** and **`g`** are the original [[function]]s
- **`` ` ``** is the [[composition]] [[operator]]
- **`x`** is the parameter to be passed to **`f`** and **`g`**

**definition** _[[composition]] in Haskell_

`(.) :: (b -> c) -> (a -> b) -> a -> c`

> **example** _[[composition]] in Haskell_
>
> let `f :: A -> B` and `g :: B -> C`. then, `g . f` has type signature `A -> C`

**properties**

_associativity_ **``h\\g`f == h`g\\f == h`g`f``** --- <https://youtu.be/SmXB2K_5lcA?t=662>

**applications**

[[function]] [[composition]] is useful in [[functional programming]] as it allows for building larger [[function]]s from smaller ones. it also allows for [[abstraction]] and [[encapsulation]].

> **example** suppose we have two [[function]]s: **`A -> B`** and **`B -> C`**. after composing them, we get **`A -> C`**. there is no way to differentiate this [[function]] from any other [[function]], and the intermediate value **`B`** is not exposed to the outside world anymore

## Identity

#todo id

**aka** _identity [[function]]_

**equiv** _[[combinator#i combinator]]_

**notation** **`(*)`**

**definition** **`(*)`**

**properties**

_[[composition#identity]]_ **`(*)f == f == f(*)`**

_[[function#idempotent function]]_ **`(*)2 == (*)`**

_[[function#self-inverse function]]_ **`(*)2 == (*)`**
