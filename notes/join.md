# Join

_turns a nested [[effect-type]] into a normal [[effect-type]]_

> **AKA**: `flatten` in Rust

see [[functional-programming]]

## definition

[[join]] converts a nested "double-level" [[effect-type]] into a "single-level" [[effect-type]]

`join :: M (M a) -> M a`, where

`a` is a value

`M` is an [[effect-type]] constructor

## applications

[[join]] can be used to define [[bind]]
