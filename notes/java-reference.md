# Java Reference

### examples of reference [[type]]s

```java
String, Array
```

or all other user-defined classes

> **note**: in java, pointers to reference [[type]]s in the heap are stored on the [[stack]]

## the `==` operator on References

using the `==` [[operator]] on reference [[type]]s compares their location in memory, which can be influenced by compiler [[optimization]]. for example, to compare the content of strings, one must use `s1.equals(s2)`, and **not** `s1 == s2`. as an example,

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
