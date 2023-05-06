# Java is a Terrible Language

**see** [[java]]

![[2022-02-26-01-29-58.png]]

&mdash; Discord # general

![[2022-02-26-01-30-07.png]]

&mdash; Discord # general

![[2022-02-26-01-30-13.png]]

![[2022-02-26-01-34-54.png]]

&mdash; Discord # general

![[2022-02-26-01-35-03.png]]

&mdash; live lecture

![[20220410161358.png]]

&mdash; Aquarium Discord server

## java `.equals`

**see** [[java#overriding equals]]

## generic arrays

Java does _not_ allow the creation of generic arrays `E[] a = new E[capacity]` where `E` is the generic [[type]]. use `E[] = (E[]) Object[capacity]` instead.

however, this will throw a warning, which will have to be suppressed using the following decorator: `@SuppressWarnings("unchecked")`.

**see** <https://stackoverflow.com/questions/529085/how-to-create-a-generic-array-in-java>

## type inference

Java has simplistic [[type]] inference through the `var` keyword &mdash; <https://www.geeksforgeeks.org/var-keyword-in-java/>

## operator overloading

Java does **not** support [[operator]] overloading, because Java

## wrappers

[[java wrapper]]s are such a duct-tape solution

## other criticism of java

of course, there’s a Wikipedia article about Java criticism: <https://en.m.wikipedia.org/wiki/Criticism_of_Java>

## java imports

see <https://youtu.be/FyCYva9DhsI?t=1673>
