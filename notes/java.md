# Java

_just a terrible programming language_

**see** [[java is a terrible language]]

**see** [[object-oriented programming]], [[object]], [[class]]

**see** [[java primitive]], [[java reference]], [[java wrapper]], [[java auto boxing]]

## Java Hello World

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World");
  }
}
```

compilation and execution:

```bash
java HelloWorld.java
```

## Scopes

**see** [[scope]]

Java [[scope]]s are defined using `{ /*...*/ }`

> **example**
>
> ```java
> {
>   int k = 0;
> }
> k++; // throws an error
> ```

## Overriding Equals

**see** [[polymorphism]], [[java is a terrible language]]

overriding the `Object.equals` in Java must follow the pattern below &mdash; [[iti1121 c introductionto computing ii]]

```java
public class Account {
	private int id;
	private String name;
	// ...
	public boolean equals(Object o) {
		if (o == null) return false;
		if (getClass() != o.getClass()) return false;
		// if (!(o instanceof Account)) return false; // alternative

		Account other = (Account) o;
		if (id != other.id) return false;
		if (name == null && other.name != null) return false;
		if (name != null && !name.equals(other.name)) return false;

		return true;
  }
}
```

## Garbage Collector

in [[java]], memory is freed by the Garbage Collector when all references to an object are deleted. this means that memory leaks are still possible when references are not explicitly deleted.

## Java Abstract Data Type

[[abstract data type]]s include:

- [[stack]]s
- [[queue]]s
- lists

abstract data [[type]]s can be implemented through [[interface]]s

## Classes

**see** [[class]]

in a [[java]] [[class]], a _final variable_ can only be initialized once

in a [[java]] [[class]], the order in which properties and methods are defined is irrelevant

## Interfaces

**see** [[interface]]s

**definition** in [[java]], an _interface_ is an abstract [[type]] that is used to specify what behavior a [[class]] should implement. [[interface]]s may only contain abstract method signatures and constant declarations.

## Generics

**see** [[generic]]s

**definition** in [[java]], _generics_ are almost identical to `template`s in C++. behind the scenes, they seem to replace all instances of the generic [[type]] by `Object`, but they still allow for compile-time [[type]] checks to avoid runtime errors &mdash; <https://stackoverflow.com/questions/48438160/how-do-java-generic-methods-work-under-the-hood>. see [[java is a terrible language]]

## other definitions and properties

**definition** _collections_ are data [[type]]s containing multiple elements. they cannot contain [[java primitive]]s &mdash; <https://stackoverflow.com/questions/4594529/java-collections-why-no-primitive-types>. see [[java is a terrible language]]

**definition** in Java, an _abstract method_ is used to have a definition but no implementation. abstract methods must be implemented by sub[[class]]es.

**definition** in Java, an _abstract class_ is used to prevent its instantiation. it must be used when a [[class]] contains abstract methods

**properties**

in Java, declaring a [[class]] `class MyClass` is shorthand for `class MyClass extents Object`

Java does **not** support operator overloading, because Java

Java does **not** support [[first-class function]]s, because Java
