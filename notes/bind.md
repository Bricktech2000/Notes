# Bind

_turns diagonal functions into horizontal functions_

> **AKA**: `>>=`, `flatMap`, `SelectMany`

see [[functional-programming]]

## applications

let a [[function]] `f` that takes as input [[type]] `T` and returns an [[effect-type]] `E<e>`. "connecting" the output of one of such functions to the input of another is an issue, as `f` has one input `T` but multiple outputs `E<e>` (`Some` and `None` with `Option<T>`, "Done" and "Not Done" with `Async`, etc.).

this often leads to deeply nested `if` checks with `null` values in languages like C or Java or deeply nested callbacks in languages like JavaScript.

[[bind]] fixes this issue by providing a way to connect the meaningful output of such [[function]]s to the input of the next one and to short-circuit the alternative output. it makes "world-crossing" [[function]]s composable by turning them into "effects-world"-only [[function]]s.

## examples

`let bindOpt = |f, opt| if opt.is_some() { f(opt.unwrap()) } else { None }`

`let bindAsync = |f, async| async.then(|res| f(res))`
