# Return

_lifts a value to the effects world_

**aka** _`pure`_, _`unit`_

**equiv** _map between [[category#object]]s_

**see** [[effect type]], [[functional programming]]

**definition** the [[return function]] lifts a value to the effects world. can be thought of as the constructor to an [[effect type]] or as wrapping a value into an [[effect type]]

**definition**

`return :: a -> T a`, where

- `a` is a value
- `T` is an [[effect type]] constructor

**examples**

`Some(1)` to create an `Option<T>` [[effect type]]

`1` to create a `Vec<T>` [[effect type]]
