# Join Function

_turns a nested [[effect type]] into a normal [[effect type]]_

**aka** _`flatten`_ in Rust, string _`concat`_

**see** [[functional programming]]

**definition** the [[join function]] converts a nested "double-level" [[effect type]] into a "single-level" [[effect type]]

**definition**

`join :: M (M a) -> M a`, where

- `a` is a value
- `M` is an [[effect type]] constructor

**definition** _in terms of the [[bind function]]_

`join :: M (M a) -> M a`

`join a = bind id a`, where

- `a` is a value
- `join` is the [[join function]]
- `bind` is the [[bind function]]
- `id` is the [[composition#identity]]

**applications**

the [[join function]] can be used to define the [[bind function]]
