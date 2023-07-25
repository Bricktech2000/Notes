# Type System

**see** [[type]], [[polymorphism]]

## Nominal Type System

**aka** _name-based type system, nominative type system_

**definition** a [[type system]] is a _nominal type system_ if [[type]] equivalence and compatibility are determined by explicit declarations and/or the name of the [[type]]s &mdash; Wikipedia

> **example**
>
> ```rust
> struct Foo;
>
> struct Bar;
>
> let x: Foo = Bar; // error: `Foo` and `Bar` are incompatible types
> ```

## Structural Type System

**aka** _property-based type system_

**definition** a [[type system]] is a _structural type system_ if [[type]] equivalence and compatibility are determined by the structure, content, or members of the [[type]]s &mdash; Wikipedia

> **example**
>
> ```typescript
> interface Foo {
>   foo: string;
> }
>
> interface Bar {
>   foo: string;
> }
>
> let x: Foo = Bar; // `Foo` and `Bar` are compatible types
> ```

## Duck Typing

_if it walks like a duck and it quacks like a duck, then it must be a duck_

**definition** in _duck typing_, [[type]] compatibility is determined by the part of the [[type]]'s structure that is used in a given context &mdash; Wikipedia

[[type system#duck type system]]s can be seen as a usage-based [[type system#structural type system]]

> **example**
>
> ```python
> class Foo:
>   def baz(self):
>     pass
>   def qux(self):
>
>
> class Bar:
>   def baz(self):
>     pass
>
> for x in [Foo(), Bar()]:
>   x.baz() # `Foo` and `Bar` are compatible types
>   x.qux() # until they are not
> ```

## Static Typing

_type safety is enforced at compile time_

## Dynamic Typing

_type compatibility is verified at runtime_

## Strong Typing

_memory-safe, invalid operations impossible, explicit type conversion_

## Weak Typing

_memory-unsafe, invalid operations possible, implicit type conversion_

## &mdash;

&mdash; <https://en.wikipedia.org/wiki/Type_system>

&mdash; <https://en.wikipedia.org/wiki/Duck_typing>

&mdash; <https://en.wikipedia.org/wiki/Structural_type_system>

&mdash; <https://en.wikipedia.org/wiki/Nominal_type_system>

&mdash; <https://en.wikipedia.org/wiki/Comparison_of_programming_languages_by_type_system>

&mdash; <https://youtu.be/QI-ktlf7qFU>
