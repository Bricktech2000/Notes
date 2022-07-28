# Java Auto Boxing

see [[java]], [[java-wrapper]]

> **definition**: _auto boxing_ is the automatic conversion from a [[java-primitive]] to a [[java-reference]]

> **definition**: _auto unboxing_ is the automatic conversion from a [[java-reference]] to a [[java-primitive]]

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

_using [[java-primitive]]s is almost always faster than using [[java-reference]]s_

![[2022-02-26-01-14-04.png]]
