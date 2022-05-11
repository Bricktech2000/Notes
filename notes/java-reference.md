# Java Reference

### examples of reference [[type]]s

```java
String, Array
```

or all other user-defined classes

> **note**: in java, pointers to reference [[type]]s in the heap are stored on the stack

## the `==` operator on References

using the `==` operator on reference [[type]]s compares their memory address. for example, to compare the content of strings, one must use `s1.equals(s2)`, and **not** `s1 == s2`. as an example,

```java
s1 = "String";
s2 = "String";
// s1 == s2 returns True
// s1.equals(s2) returns True
s1 = "String";
s2 = s1 + "1";
s1 = s1 + "1";
// s1 == s2 returns False
// s1.equals(s2) returns True
```
