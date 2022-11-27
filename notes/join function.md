# Join Function

_turns a nested [[effect type]] into a normal [[effect type]]_

**aka** _`flatten` in Rust_

**see** [[functional programming]]

**definition** the [[join function]] converts a nested "double-level" [[effect type]] into a "single-level" [[effect type]]

**definition**

`join :: M (M a) -> M a`, where

- `a` is a value
- `M` is an [[effect type]] constructor

**applications**

the [[join function]] can be used to define the [[bind function]]
