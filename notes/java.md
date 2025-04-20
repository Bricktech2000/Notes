# Java

_everything that seemed like a good idea 20 years ago_

**see** [[object-oriented programming]], [[math notation]]

## hello world

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World");
  }
}
```

compilation and execution:

```sh
java HelloWorld.java
```

## a painful language

[[java#auto boxing]] is a band-aid and [[java#wrapper]]s are a duct-tape solution

[[java]] does **not** support operator overloading. [[java]] does **not** have [[first-class function]]s

[[java]] does **not** allow the creation of generic [[array]]s `E[] a = new E[capacity]` where `E` is the generic [[type]]. `E[] = (E[]) Object[capacity]` is to be used instead, which will generate a compile-time a warning, which may be suppressed using the decorator `@SuppressWarnings("unchecked")` --- <https://stackoverflow.com/questions/529085/how-to-create-a-generic-array-in-java>

[[java]] has simplistic [[type inference]], through the `var` keyword --- <https://www.geeksforgeeks.org/var-keyword-in-java/>

[[java]] [[array]]s are indexed by [[integer]]s, meaning no [[java]] [[array]] can hold more than **`2[31]`** elements

[[java]] `import` best practices are basically cargo cult programming --- <https://youtu.be/FyCYva9DhsI?t=1673>

[[java]] has [[null]]s and [[exception]]s

also see <https://en.m.wikipedia.org/wiki/Criticism_of_Java>

### overriding `equals`

**see** [[polymorphism]]

overriding `Object.equals` in [[java]] should ideally follow the pattern below --- ITI1121 Introduction to Computing II

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

### `==` on references

using the `==` [[operator]] on [[java#reference]]s compares memory locations, which can be influenced by compiler [[optimization]]

> **example**
>
> ```java
> public class References {
>   public static void main(String[] args) {
>     String a = "asdf";
>     String b = "asdf";
>     String c = "a" + "sdf";
>     String first = "a";
>     String d = first + "sdf";
>
>     System.out.println(a == b); // true
>     System.out.println(a == c); // true
>     System.out.println(a == d); // false
>   }
> }
> ```

### auto boxing

_auto boxing_ is the automatic conversion from a [[java#primitive]] to a [[java#reference]]; _auto unboxing_ is the automatic conversion from a [[java#reference]] to a [[java#primitive]]

> **example**
>
> ```java
> Integer i = 1; // valid in Java 5 and up
> Integer i = Integer.valueOf(1); // transforms into this (called boxing)
>
> Integer i = new Integer(1); // this syntax is deprecated since Java 9
> ```

> **example**
>
> ```java
> Integer i = 1;
> i = i + 5;
>
> //gets turned into
>
> i = Integer.valueOf(
>   i.intValue() + 5 // unboxing and adding to another primitive
> ); // re-boxing the value again
> ```

## type "system"

### Generic

**see** [[generic]]

[[java#generic]]s are basically compile-time-checked type casts to [[java]]'s [[type#top type]] `Object`, a process known as _type erasure_ --- <https://stackoverflow.com/questions/48438160/how-do-java-generic-methods-work-under-the-hood>. consequently, collections may not contain [[java#primitive]]s --- <https://stackoverflow.com/questions/4594529/java-collections-why-no-primitive-types>

### Primitive

[[java#primitive]]s are stored on the [[stack]]

[[java#primitive]]s are passed by value and can be passed by reference through [[java#wrapper]]s

> **examples**
>
> ```java
> byte
> short
> int
> long
> float
> double
> boolean
> char
> ```

### Reference

[[java#reference]] types are stored on the heap; pointers to [[java#reference]] types are stored on the [[stack]]

despite [[java]] being a managed language, memory leaks can still occur if references to [[object]]s are not explicitly deleted

[[java#reference]]s are passed by reference. [[java#reference]]s inherit from `Object`, which allows them to be used in [[java#generic]]s. all user-defined [[class]]es are [[java#reference]]s

> **note** declaring a [[java]] [[class]] `class MyClass` is shorthand for `class MyClass extents Object` as `Object` is the [[type#top type]] in [[java]]

> **examples**
>
> ```java
> String
> Integer
> Object
> ```

### Wrapper

every [[java#primitive]] has a corresponding [[java#wrapper]], which are [[java#reference]]s

> **example** `Integer` is a wrapper for `int`
