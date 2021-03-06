# Rust

_a language for the next 40 years_

&mdash; <https://youtu.be/A3AdN7U24iU>

&mdash; <https://youtu.be/PuMXWc0xrK0>

## safety features

[[rust]] borrows many features from [[functional-programming]] and makes them easy to use. for instance, [[rust]] has `Option`s instead of `null` pointers, and it has `Result`s instead of `try catch` exceptions.

accessing out-of-bounds memory causes either a compile time error or a `panic!` at runtime instead of maybe or maybe not causing a segfault

[[rust]]'s [[type]] system checks thread safety at compile time as ownership rules apply across multiple threads

### borrow checker

_ownership and borrowing_

- data can have either one mutable reference or multiple immutable references
- #todo

> _in fixing memory safety, the Rust team accidentally fixed everything_ &mdash; <https://youtu.be/Q3AhzHq8ogs?t=113>

### unsafe system

[[rust]]'s type system can be a bit restrictive for low-level programming. this is why [[rust]] has a way to bypass a few specific checks in the form of the `unsafe` keyword. consequently, [[rust]] code is safe by default

unsafe code can:

- dereference a raw pointer
- call an unsafe [[function]]
- implement unsafe traits
- mutate global variables
- access fields of unions (see algebraic data [[type]]s)

> other languages say _here is the line; you may never cross it_. [[rust]] says _cross here if you know what you're doing_ &mdash; <https://youtu.be/PuMXWc0xrK0?t=76>

most languages have a floor for [[abstraction]]s, such as builtin functions like `parseInt` in [[javascript]] or `sorted` in [[python]]. in [[rust]], the `unsafe` system allows access to lower-level functionality **without** sacrificing high-level orgonomics.

the unsafe code is for framework authors, meaning framework users don't have to worry about it. (duplicate)

### macro system

[[rust]]'s macro system is Turing complete, see [[turing-machine]]. they allow for both [[abstraction]]s and new syntax.

[[rust]] macros are for framework authors, meaning framework users don't have to worry about them. (duplicate)

## sign posts

Rust ensures "surprising" behavior is clearly sign-posted:

- macros are sign-posted with a `!`
- unsafe code is sign-posted with the `unsafe` keyword
- lazy exception handling is sign-posted with an `unwrap()` call
- anything that could cause a [[function]] to return early is sign-posted with the `!` or `?` operators

### example

below, the [[rust]] solution is just as unsafe as the [[python]] solution, but that anything unsafe is clearly sign-posted with an `.unwrap()` call

```python
int(items['ViewCount']['N'])
```

```rust
i32::from_str_radix(
  item.get("ViewCount").unwrap()
      .get("N").unwrap(),
  10
).unwrap()
```

## edition system

for breaking changes (such as adding an `async` keyword), [[rust]] uses an edition system (such as the 2015 and 2018 editions), where the [[rust]] compiler understands all editions simultaneously. this means that a project written in any edition of [[rust]] can depend on a library written for any other edition of [[rust]], preventing ecosystem splits

because of the way the compiler is currently built, maintenance to core [[rust]] functionality (such as borrow checking, optimization, code generation) is not affected:

```mermaid
graph LR;

A(2015 Edition<br>Source Code)
B(2018 Edition<br>Source Code)
A_HIR(High-Level IR)
B_HIR(High-Level IR)
MIR(Mid-Level IR<br><em>core functionality</em>)
LLVM_IR(LLVM IR)
MACHINE_CODE(Machine Code)

A --> A_HIR --> MIR
B --> B_HIR --> MIR
MIR --> LLVM_IR --> MACHINE_CODE
```

&mdash; <https://youtu.be/A3AdN7U24iU?t=2009>

## pros & cons

pros:

- performance (no garbage collector, zero-cost [[abstraction]]s)
- portability (compiles to LLVM bytecode which is widely supported)
- stability (very strong backwards compatibility)
- memory safety (done through the ownership and borrowing system)

cons:

- simplicity (more features and more syntax than languages like [[c]])
- ecosystem features (no standard, no LTS releases, no private crate hosting)
