# Join

_turns a nested [[effect-type]] into a normal [[effect-type]]_

> **AKA**: #todo

see [[functional-programming]]

## definition

[[join]] converts a nested "double-level" [[effect-type]] into a "single-level" [[effect-type]]

`join :: M (M a) -> M a`, where

`a` is a value

`M` is an [[effect-type]] constructor

## applications

see [[monad]], [[bind]]

[[join]] can be used to define [[bind]], as follows:

let a [[function]] `f :: a -> M a`. then,

`bind :: (a -> M a) => M a -> b`

`bind f m = join (fmap f m)`, where

`m` is a [[monad]] constructor

`f` is a "world-crossing" [[function]]

`join` is the [[join]] [[function]]

`bind` is the [[bind]] [[function]]

`fmap` is the [[map]] [[function]]

&mdash; Simon
