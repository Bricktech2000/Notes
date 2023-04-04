# C++

_[[c]] with OOP_

**see** [[c]], [[object-oriented programming]], [[math notation]]

## an improper superset

&mdash; <https://en.wikipedia.org/wiki/Compatibility_of_C_and_C++> &mdash; <https://stackoverflow.com/questions/3777031/what-prevents-c-from-being-a-strict-superset-of-c>

[[c++]] is not a [[set#superset]] of [[c]]; that is, $\times \,\land \text{C++} \vdash \text{C}$

> **examples** _valid [[c]] but invalid [[c++]]; that is, elements of $\text{C} \vdash \text{C++}$_
>
> ```C
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
