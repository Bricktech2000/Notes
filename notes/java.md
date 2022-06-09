# Java

_just a terrible programming language_

[[java-is-a-terrible-language]]

[[object-oriented-programming]], [[object]], [[class]]

[[java-hello-world]], [[overriding-java-equals]]

[[java-primitive]], [[java-reference]], [[java-wrapper]], [[java-auto-boxing]]

[[java-scopes]]

[[java-garbage-collector]]

[[java-abstract-data-type]]

### definitions

> **definition**: _collections_ are data [[type]]s containing multiple elements. they cannot contain [[java-primitive]]s &mdash; <https://stackoverflow.com/questions/4594529/java-collections-why-no-primitive-types>. see [[java-is-a-terrible-language]]

> **definition**: in Java, an _abstract method_ is used to have a definition but no implementation. abstract methods must be implemented by sub[[class]]es.

> **definition**: in Java, an _abstract class_ is used to prevent its instantiation. it must be used when a [[class]] contains abstract methods

> **definition**: in Java, _generics_ are almost identical to `template`s in C++. behind the scenes, they seem to replace all instances of the generic [[type]] by `Object`, but they still allow for compile-time [[type]] checks to avoid runtime errors &mdash; <https://stackoverflow.com/questions/48438160/how-do-java-generic-methods-work-under-the-hood>. see [[java-is-a-terrible-language]]

Java does **not** support operator overloading, because Java

Java does **not** support [[first-class-function]]s, because Java

in Java, declaring a [[class]] `class MyClass` is shorthand for `class MyClass extents Object`
