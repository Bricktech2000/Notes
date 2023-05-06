# Java Auto Boxing

**see** [[java]], [[java wrapper]]

**definition** _auto boxing_ is the automatic conversion from a [[java primitive]] to a [[java reference]]

**definition** _auto unboxing_ is the automatic conversion from a [[java reference]] to a [[java primitive]]

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
> //gets turned into
> i = Integer.valueOf(
>   i.intValue() + 5 // unboxing and adding to another primitive
> ); // re-boxing the value again
> ```

## Performance Impacts

using [[java primitive]]s is almost always faster than using [[java reference]]s

> **example**
>
> ```java
> // the following executes in 40ms
> long sum = (long) 0;
> for (int i = 0; i < 100000000; i++) {
>   sum += sum + (long) 1;
> }
>
> // the following executes in 477ms
> Long sum = (long) 0;
> for (int i = 0; i < 100000000; i++) {
>   sum += sum + (long) 1;
> }
> ```
