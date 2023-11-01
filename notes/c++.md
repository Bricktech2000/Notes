# C++

_bloated [[c]] &mdash; but with [[class]]es!_

**see** [[c]], [[object-oriented programming]], [[math notation]]

## an improper superset

&mdash; <https://en.wikipedia.org/wiki/Compatibility_of_C_and_C++> &mdash; <https://stackoverflow.com/questions/3777031/what-prevents-c-from-being-a-strict-superset-of-c>

[[c++]] is not a [[set#superset]] of [[c]]; that is, **`>< /\ "C++" |- "C"`**

> **examples** _valid [[c]] but invalid [[c++]]; that is, elements of **`"C" /\ +"C++"`**_
>
> ```c
> // implicit conversion from `void*`
> void *p;
> int *i = p;
>
> // multiple tentative definitions of a single global variable
> int N;
> int N = 10;
>
> // declaring a type with the same name as an existing tag
> enum BOOL {FALSE, TRUE};
> typedef int BOOL;
>
> // designated initializers
> char s[20] = { [0] = 'a', [8] = 'g' };
>
> // using any reserved C++ keyword as an identifier
> int new = 0;
> ```

## duck typing

[[c++]] `template`s are a form of [[type system#duck typing]]

> **example**
>
> ```cpp
> // to be compiled with `g++ -std=c++20`
>
> #include<string>
> #include<iostream>
> #include<filesystem>
>
> using namespace std::filesystem;
>
> template<typename T>
> T divide(T a, T b) {
>   return a / b;
> }
>
> int main() {
>   double division = divide(1.0, 2.0); // 0.5
>   path concatenation = divide(path("foo"), path("bar")); // "foo/bar"
> }
> ```

&mdash; <https://en.wikipedia.org/wiki/Duck_typing#Templates_or_generic_types> &mdash; <https://stackoverflow.com/questions/6923299/whats-the-relationship-between-c-template-and-duck-typing>

&mdash; <https://www.reddit.com/r/cpp/comments/139c2v1/whats_the_most_hilarious_use_of_operator/>

## undecidability of grammar

parsing the [[c++]] grammar is undecidable

> **resource** [[proof]] sketch of [[turing complete]]ness of [[c++]] templates &mdash; <https://port70.net/~nsz/c/c%2B%2B/turing.pdf>

> **proof**
>
> &mdash; <https://blog.reverberate.org/2013/08/parsing-c-is-literally-undecidable.html>
>
> consider the following [[c++]] program:
>
> ```cpp
> struct SomeType {};
>
> template <...> struct TuringMachine {
>   // Insert implementation of a Turing machine here, which we know
>   // is possible from previous proofs.
> };
>
> template <typename T> struct S {
>   static int name;
> };
>
> template<> struct S<SomeType> {
>   typedef int name;
> };
>
> int x;
> int main() {
>   S<TuringMachine<...>::output>::name * x;
> }
> ```
>
> - if `TuringMachine<...>::output` is `SomeType` then `::name` is an [[integer]] and the [[abstract syntax tree]] is the multiplication of two [[integer]]s
> - if `TuringMachine<...>::output` is not `SomeType` then `::name` is a `typedef` for the [[integer]] [[type]] and the [[abstract syntax tree]] is the declaration of the pointer-to-int `x`
>
> _These two are completely different parse trees, and the difference between them cannot be delayed to further stages of the compiler. The parse tree **itself** depends on arbitrary template instantiation, and is therefore the parsing step is undecidable_ &mdash; <https://blog.reverberate.org/2013/08/parsing-c-is-literally-undecidable.html>
