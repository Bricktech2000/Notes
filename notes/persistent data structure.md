# Persistent Data Structure

**see** [[data structure]]

**definition** a _persistent data structure_ is a [[data structure]] that always preserves the previous version of itself when it is modified. such [[data structure]]s are **effectively** immutable [...] --- Wikipedia

[[persistent data structure]]s use _structural sharing_ to improve performance

> **examples** [[git]] and [[blockchain]]s are [[persistent data structure]]s

> **example**
>
> a [[stack]] [[persistent data structure]] can be written using a [[linked list]] with a shared tail
>
> ```rust
> use std::rc::Rc;
>
> enum Stack<T> {
>   Empty,
>   Node(T, Rc<Stack<T>>),
> }
>
> impl<T: Clone> Stack<T> {
>   fn push(self: Rc<Self>, val: T) -> Rc<Self> {
>     Rc::new(Stack::Node(val, self))
>   }
>
>   fn pop(self: Rc<Self>) -> Option<(T, Rc<Self>)> {
>     match self.as_ref() {
>       Stack::Empty => None,
>       Stack::Node(val, next) => Some((val.clone(), Rc::clone(next))),
>     }
>   }
> }
> ```
>
> --- me
>
> ![[20220520161901.png]]
>
> --- <https://youtu.be/APUCMSPiNh4?t=2830>
