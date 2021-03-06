## Map

_lifts a horizontal [[function]] to the effects world_

> **AKA**: `lift`, `select`, `fmap`

## definition

[[map]] "lifts" a [[function]] to the effects world

`map :: (a -> b) -> T a -> T b`, where

`a` is a value

`T` is an [[effect-type]] constructor

## applications

[[map]]s unwrap the inputs to a [[function]] before wrapping them back after execution, see [[effect-type]]

let a [[function]] `let inc = |x| x + 1` and a [[effect-type]] `Option<T>`

`inc 1` works fine, but `inc Some(1)` will fail. it would be possible to work around this issue by defining a custom [[function]] to unwrap the optional [[type]], increment it, and wrap it back into an optional [[type]]. however, this is an antipattern in [[functional-programming]].

ideally, we would want to stay in the "optional" world while using a value and unwrap it only after being done all operations. this is what [[map]]s are for.

## examples

`(Some 1).map(inc)` will return `Some 2`

`[1, 2, 3].map(inc)` will return `[2, 3, 4]`
