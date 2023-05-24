# C++

_[[c]] with OOP_

**see** [[c]], [[object-oriented programming]], [[math notation]]

## an improper superset

&mdash; <https://en.wikipedia.org/wiki/Compatibility_of_C_and_C++> &mdash; <https://stackoverflow.com/questions/3777031/what-prevents-c-from-being-a-strict-superset-of-c>

[[c++]] is not a [[set#superset]] of [[c]]; that is, **`>< /\ "C++" |- "C"`**

> **examples** _valid [[c]] but invalid [[c++]]; that is, elements of **`"C" /\ +"C++"`** _
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
