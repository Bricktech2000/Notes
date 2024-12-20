# Refactoring to Immutability

--- <https://youtu.be/APUCMSPiNh4>

## replace `set` with `with`

_what would you be if I were to [operation with side effects]?_

this replaces setters (which have side effects) with the creation of a new object (which has no side effects)

> **example**
>
> ```python
> class Counter:
>   def __init__(self):
>     self.value = 0
>
>   def increment(self):
>     self.value += 1
>
>   def reset(self):
>     self.value = 0
> ```
>
> can be refactored as:
>
> ```python
> class Counter:
>   def __init__(self, value):
>     self.value = value
>
>   def with_increment(self):
>     return Counter(self.value + 1)
>
>   def with_reset(self):
>     return Counter(0)
> ```

## use persistent data structures

**see** [[persistent data structure]]
