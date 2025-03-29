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
