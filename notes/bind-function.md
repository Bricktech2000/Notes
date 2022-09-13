# Bind Function

_turns a diagonal [[function]] into horizontal [[function]] in the effects world_

> **AKA** `>>=`, `flatMap`, `SelectMany`, Sequential Composition, `and_then` in Rust

see [[functional-programming]]

> **note** the name `flatMap` comes from the fact that `bind` can be defined as calling the [[map-function]] then calling the [[join-function]] (flattening in the case of [[list]]s), see definition below &mdash; <https://youtu.be/C2w45qRc3aU?t=808>

**definition** the [[bind-function]] converts a "diagonal" function ("world-crossing", that goes from "normal" world to "effects" world) into a "horizontal" function (in the "effects" world only)

**definition** _conventional definition of [[bind-function]]_

`bind :: (a -> M b) -> M a -> M b`, where

- `a` is a value
- `M` is an [[effect-type]] constructor

**definition** _defining the [[bind-function]] using the [[join-function]]_

let a [[function]] `f :: a -> M b`. then,

`bind :: (a -> M b) -> M a -> b`

`bind f ma = join (fmap f ma)`, where

- `ma` is a [[monad]]
- `f` is a "world-crossing" [[function]]
- `join` is the [[join-function]]
- `bind` is the [[bind-function]]
- `fmap` is the [[map-function]]

&mdash; Simon

**examples**

> **example** `let bindOpt = |f, opt| if opt.is_some() { f(opt.unwrap()) } else { None }`

> **example** `let bindAsync = |f, async| async.then(|res| f(res))`

**applications**

let a [[function]] `f` that takes as input [[type]] `T` and returns an [[effect-type]] `E<e>`. "connecting" the output of one of such functions to the input of another is an issue, as `f` has one input `T` but multiple outputs `E<e>` (`Some` and `None` with `Option<T>`, "Done" and "Not Done" with `Async`, etc.).

this often leads to deeply nested `if` checks with [[null]] values in languages like C or Java or deeply nested callbacks in languages like JavaScript.

the [[bind-function]] fixes this issue by providing a way to connect the meaningful output of such [[function]]s to the input of the next one and to short-circuit the alternative output. it makes "world-crossing" [[function]]s composable by turning them into "effects-world"-only [[function]]s.
