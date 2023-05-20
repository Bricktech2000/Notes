# Java Reference

in [[java]], all reference types are store on the heap; pointers to reference [[type]]s are stored on the [[stack]]

> **examples** _reference types_
>
> ```java
> String, Array
> ```
>
> all user-defined [[class]]es are [[java reference]]s

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
