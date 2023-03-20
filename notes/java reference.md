# Java Reference

> **examples** _reference types_
>
> ```java
> String, Array
> ```
>
> all other user-defined classes are [[java reference]]s

> **note** in java, pointers to reference [[type]]s in the heap are stored on the [[stack]]

## the `==` operator on references

using the `==` [[operator]] on reference [[type]]s compares their location in memory, which can be influenced by compiler [[optimization]]. for example, to compare the content of [[string]]s, one must use `s1.equals(s2)`, and **not** `s1 == s2`. as an example,

```java
public class References {
 public static void main(String[] args) {
   String a = "asdf";
   String b = "asdf";
   String c = "a" + "sdf";
   String first = "a";
   String d = first + "sdf";

   System.out.println(a == b); // true
   System.out.println(a == c); // true
   System.out.println(a == d); // false
 }
}
```
