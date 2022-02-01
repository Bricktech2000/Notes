# Boxing

see [Java](Java%200b5b700f7a384fc394698ce8490689cb.md), [Java Wrapper](Java%20Wrapper%2092b0e3e490b04780a1b5aa8e6239602d.md)

> **boxing** is the automatic conversion from a [Java Primitive](Java%20Primitive%20e7dbc1581ea5487ca06a33ec3344b3e7.md) to a [Java Reference](Java%20Reference%2041431c6e5e0749a7bc68d4bc851b15ce.md)
> 

> **unboxing** is the automatic conversion from a [Java Reference](Java%20Reference%2041431c6e5e0749a7bc68d4bc851b15ce.md) to a [Java Primitive](Java%20Primitive%20e7dbc1581ea5487ca06a33ec3344b3e7.md)
> 

### examples

```java
Integer i = 1; // valid in Java 5 and up
Integer i = Integer.valueOf(1); // transforms into this (called boxing)

Integer i = new Integer(1); // this syntax is deprecated since Java 9
```

```java
Integer i = 1;
i = i + 5;
//gets turned into
i = Integer.valueOf(
	i.intValue() + 5 // unboxing and adding to another primitive
); // re-boxing the value again
```

## performance

*using [Java Primitive](Java%20Primitive%20e7dbc1581ea5487ca06a33ec3344b3e7.md)s is almost always faster*

![Untitled](Boxing%2090a1ff7bca9a416eb76c72efd638cef7/Untitled.png)