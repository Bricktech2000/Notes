# Rust

_a language for the next 40 years_

&mdash; <https://youtu.be/A3AdN7U24iU>

&mdash; <https://youtu.be/PuMXWc0xrK0>

**tradeoffs**

- high performance (no garbage collector, zero-cost [[abstraction]]s)
- great portability (compiles to LLVM bytecode which is widely supported)
- great stability (very strong backwards compatibility)
- great memory safety (done through the borrow checker)

- relatively complex (more features and more syntax than languages like [[c]])
- lacking ecosystem features (no standard, no LTS releases, no private crate hosting)

## Type System

&mdash; <https://youtu.be/bnnacleqg6k>

&mdash; <https://youtu.be/s5S2Ed5T-dc>

the [[type#empty type]] `!`, pronounced _never_, is [[rust]]'s [[type#bottom type]]. it is the type of an expression that never returns, such as `panic!()` or `loop {}` &mdash; <https://doc.rust-lang.org/std/primitive.never.html>

`()` is [[rust]]'s [[type#unit type]]. it is the type of an expression that returns nothing, such as `println!()` or `let x = 1;`

`struct` is a [[type#product type]] and `enum` is a [[type#sum type]] of [[type#product type]]s

### Function Types

&mdash; <https://youtu.be/SqT5YglW3qU>

all [[function]] items and all closures of a [[rust]] program have a unique [[type]] internal to the compiler. as they only have a single inhabitant, their corresponding [[function]], these [[type]] are [[type#unit type]]s. consequently, the size of any inhabitant of theirs is zero. they are completely opaque; the only reason they are useful is because they implement one of the `Fn` [[trait]]s, which allows them to be called. _we don't know exactly what's inside the [[function]], but we can call it as long as we know how to set up everything according to the calling convention_ &mdash; <https://youtu.be/SqT5YglW3qU>

### Impl Traits

&mdash; <https://stackoverflow.com/questions/47514930/what-are-the-differences-between-an-impl-trait-argument-and-generic-function-par>

`impl Trait`s as [[function]] arguments or return types are syntactic sugar for anonymous [[type]] parameters

### Function Traits

&mdash; <https://www.eventhelix.com/rust/rust-to-assembly-return-impl-fn-vs-dyn-fn/>

[[rust]] defines the following [[function]] traits:

- `FnOnce` &mdash; takes ownership of its environment and can only be called once
- `FnMut` &mdash; takes mutable references to its environment and can be called multiple non-overlapping times
- `Fn` &mdash; takes immutable references to its environment and can be called multiple overlapping times

## Safety

[[rust]] borrows many features from [[functional programming]] and makes them easy to use. for instance, [[rust]] has `Option`s instead of [[null]] pointers, and it has `Result`s instead of `try catch` exceptions.

accessing out-of-bounds memory causes either a compile time error or a `panic!` at runtime instead of maybe or maybe not causing a segfault. the `#[no_panic]` attribute macro can be used to force the compiler to prove that a function will never panic. &mdash; <https://youtu.be/sbVxq7nNtgo?t=586>

the [[rust#type system]] checks thread safety at compile time as ownership rules apply across multiple threads

### Borrow Checker

[[rust#borrow checker]] rules are as follows:

- data can have either one mutable reference or any number of immutable references
- the lifetime of a reference may not exceed the lifetime of the owner

_in fixing memory safety, the Rust team accidentally fixed everything_ &mdash; <https://youtu.be/Q3AhzHq8ogs?t=113>

### Unsafe System

the [[rust#type system]] can be a bit restrictive for low-level programming. this is why [[rust]] has a way to bypass a few specific checks in the form of the `unsafe` keyword. consequently, [[rust]] code is safe by default

unsafe code can:

- dereference a raw pointer
- call an unsafe [[function]]
- implement unsafe traits
- mutate global [[variable]]s
- access fields of unions (see algebraic data [[type]]s)

_other languages say "here is the line; you may never cross it". [[rust]] says "cross here, if you know what you're doing"_ &mdash; <https://youtu.be/PuMXWc0xrK0?t=76>

most languages have a floor for [[abstraction]]s, such as builtin functions like `parseInt` in [[javascript]] or `sorted` in [[python]]. in [[rust]], the `unsafe` system allows access to lower-level functionality **without** sacrificing high-level orgonomics.

### Macro System

the [[rust#macro system]] is Turing complete, see [[turing machine]]. they allow for both [[abstraction]]s and new syntax

### Smart Pointers

- `Box` is for unique ownership
- `Rc` is for multiple ownership (reference counted)
- `Arc` is for multiple ownership across threads (atomic reference counted)
- `Mutex` is for interior mutability across threads (atomic not reference counted)

the following can be used for interior mutability:

- `Cell` &mdash; wrapped data cannot be borrowed but can be copied and mutated. has no overhead
- `RefCell` &mdash; wrapped data can be borrowed. borrow checks are done at runtime and therefore could panic. has small overhead
- `UnsafeCell` &mdash; no borrow checks and therefore unsafe. used internally by and made safe by `Cell` and `RefCell`

&mdash; <https://users.rust-lang.org/t/confused-between-box-rc-cell-arc/10946>

&mdash; <https://stackoverflow.com/questions/30275982/when-i-can-use-either-cell-or-refcell-which-should-i-choose>

&mdash; <https://doc.rust-lang.org/std/cell/struct.UnsafeCell.html>

## Sign Posts

Rust ensures "surprising" behavior is clearly sign-posted:

- macros are sign-posted with a `!`
- unsafe code is sign-posted with the `unsafe` keyword
- lazy exception handling is sign-posted with an `unwrap()` call
- anything that could cause a [[function]] to return early is sign-posted with the `!` or `?` operators

> **example**
>
> below, the [[rust]] solution is just as unsafe as the [[python]] solution, but that anything unsafe is clearly sign-posted with an `.unwrap()` call
>
> ```python
> int(items['ViewCount']['N'])
> ```
>
> ```rust
> i32::from_str_radix(
>   item.get("ViewCount").unwrap()
>       .get("N").unwrap(),
>   10
> ).unwrap()
> ```

## Edition System

&mdash; <https://youtu.be/A3AdN7U24iU?t=2009>

for breaking changes (such as adding an `async` keyword), [[rust]] uses an edition system (such as the 2015 and 2018 editions), where the [[rust]] compiler understands all editions simultaneously. this means that a project written in any edition of [[rust]] can depend on a library written for any other edition of [[rust]], preventing ecosystem splits

because of the way the compiler is currently built, maintenance to core [[rust]] functionality (such as borrow checking, [[optimization]], code generation) is not affected.

**representation**

```mermaid
graph TD
  A(2015 Edition<br />Source Code)
  B(2018 Edition<br />Source Code)
  A_HIR(High-Level IR)
  B_HIR(High-Level IR)
  MIR(Mid-Level IR<br />_core functionality_)
  LLVM_IR(LLVM IR)
  MACHINE_CODE(Machine Code)

  A --> A_HIR --> MIR
  B --> B_HIR --> MIR
  MIR --> LLVM_IR --> MACHINE_CODE
```
