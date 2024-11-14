# Apply Function

_applies a [[function]] sitting in the effects world_

**aka** _`ap`, `<*>`_

**see** [[functional programming]]

**definition** the [[apply function]] applies a [[function]] sitting in the effects world to a value in the effects world

**definition**

`apply :: T (a -> b) -> T a -> T b`, where

- `a` is a value
- `T` is an [[effect type]] constructor

**definition** _in terms of the [[bind function]]_

let a [[function]] `f :: T (a -> b)`. then,

`apply :: T (a -> b) -> T a -> T b`

`apply f ma = f >>= \f -> (ma >>= \ma -> (return f m))`, where

- `ma` is a [[monad]]
- `return` is the [[return function]]
- `>>=` is the [[bind function]]

&mdash; <https://youtu.be/caSOTjr1z18?t=21m12s>

**applications**

> **example** `[f, g] <*> [1, 2]` will return `[f 1, f 2, g 1, g 2]`

> **example** `return (+) <*> [1, 2, 3] <*> [4, 5, 6]` will return `[1 + 4, 1 + 5, 1 + 6, 2 + 4, 2 + 5, 2 + 6, 3 + 4, 3 + 5, 3 + 6]`
