# Bind

_turns a diagonal [[function]] into horizontal [[function]] in the effects world_

> **AKA**: `>>=`, `flatMap`, `SelectMany`, Sequential Composition, `and_then` in Rust

see [[functional-programming]]

## definition

[[bind]] converts a "diagonal" function ("world-crossing", that goes from "normal" world to "effects" world) into a "horizontal" function (in the "effects" world only)

`bind :: (a -> M b) -> M a -> M b`, where

`a` is a value

`M` is an [[effect-type]] constructor

[[join]] can be used to define [[bind]]

## applications

let a [[function]] `f` that takes as input [[type]] `T` and returns an [[effect-type]] `E<e>`. "connecting" the output of one of such functions to the input of another is an issue, as `f` has one input `T` but multiple outputs `E<e>` (`Some` and `None` with `Option<T>`, "Done" and "Not Done" with `Async`, etc.).

this often leads to deeply nested `if` checks with [[null]] values in languages like C or Java or deeply nested callbacks in languages like JavaScript.

[[bind]] fixes this issue by providing a way to connect the meaningful output of such [[function]]s to the input of the next one and to short-circuit the alternative output. it makes "world-crossing" [[function]]s composable by turning them into "effects-world"-only [[function]]s.

## examples

`let bindOpt = |f, opt| if opt.is_some() { f(opt.unwrap()) } else { None }`

`let bindAsync = |f, async| async.then(|res| f(res))`
