# Apply Function

**aka** _`ap`, `<*>`_

_applies a [[function]] sitting in the effects world_

**definition** the [[apply function]] applies a [[function]] sitting in the effects world to a value in the effects world

**definition**

`apply :: T (a -> b) -> T a -> T b`, where

- `a` is a value
- `T` is an [[effect type]] constructor

**applications**

**examples**

> **example** `[f, g, h] <*> [1, 2, 3]` will return `[f 1, g 2, h 3]`

> **example** `return (+) <*> [1, 2, 3] <*> [4, 5, 6]` will return `[1 + 4, 2 + 5, 3 + 6]`
