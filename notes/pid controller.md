# PID Controller

**aka** _proportional-integral-derivative controller_

**see** [[math notation]], [[integral]], [[derivative]]

**definition**

**`r = :K(rr {dd}C e)`**, where

- **`r t`** is the controller _response_ at [[time]] **`t`**
- **`e t`** is the _error_ at [[time]] **`t`**
- **`K`** are the controller _gains_ **`(K_I, K_P, K_D)`**
- **`C`** are the [[integral]]-proportional-[[derivative]] constants **`(.1, 0, 1)`**
- **`dd`** is the [[derivative]] operator #todo derivative [[operator]] in my [[math notation]]
- **`{dd}C`** composes the [[function]] **`dd`** with itself **`C`** times #todo repeated [[function#composition]] in my [[math notation]]
