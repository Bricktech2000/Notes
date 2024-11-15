# Map Function

_lifts a horizontal [[function]] to the effects world_

**aka** _`lift`, `select`, `fmap`, `<$>`_

**equiv** _map between [[category#morphism]]s_

**definition** the [[map function]] "lifts" a [[function]] to the effects world

**definition**

`map :: (a -> b) -> T a -> T b`, where

- `a` is a value
- `T` is an [[effect type]] constructor

**definition** _in terms of the [[apply function]]_

let a [[function]] `f :: a -> b`. then,

`fmap :: (a -> b) -> T a -> T b`

`fmap f aa = pure f <*> aa`, where

- `aa` is an [[applicative]]
- `fmap` is the [[map function]]
- `pure` is the [[return function]]
- `<*>` is the [[apply function]]

--- <https://github.com/fantasyland/static-land/blob/master/docs/spec.md#applicative>

--- <https://en.wikipedia.org/wiki/Applicative_functor>

**definition** _in terms of the [[bind function]]_

let a [[function]] `f :: a -> T b`. then,

`fmap :: (a -> b) -> T a -> T b`

`fmap f ma = (return . f) =<< ma`, where

- `ma` is a [[monad]]
- `fmap` is the [[map function]]
- `return` is the [[return function]]
- `=<<` is the [[bind function]]

--- me, Simon Discord DM

**applications**

[[map function]]s unwrap the inputs to a [[function]] before wrapping them back after execution, see [[effect type]]. let a [[function]] `let inc = |x| x + 1` and a [[effect type]] `Option<T>`. `inc 1` works fine, but `inc Some(1)` will fail. it would be possible to work around this issue by defining a custom [[function]] to unwrap the optional [[type]], increment it, and wrap it back into an optional [[type]]. however, this is an antipattern in [[functional programming]]. ideally, we would want to stay in the "optional" world while using a value and unwrap it only after being done all operations. this is what [[map function]]s are for.

**examples**

> **example** `(Some 1).map(inc)` will return `Some 2`

> **example** `[1, 2, 3].map(inc)` will return `[2, 3, 4]`
