# C

_the OG with UB_

&mdash; <https://youtu.be/A3AdN7U24iU>

&mdash; Effective C by Robert C. Seacord

**pros**

- performance (fast, very little overhead, very little resources)
- portability (compilers support many different targets)
- simplicity (language is simple, not much syntax to learn)
- stability (code doesn't break or become obsolete)

**cons**

- memory unsafety (use after free, double free, memory leaks, buffer overreads and overwrites, [[null]] pointers, data races...)

## array indexing quirk

```Cpp
#include <iostream>

int main(void) {
 short a[4] = {1, 2, 3, 4};

 std::cout << a[3] << std::endl; // 4
 std::cout << 3 [a] << std::endl; // 4
 std::cout << *(a + 3) << std::endl; // 4
 std::cout << *(3 + a) << std::endl; // 4
}
```

## portability

### implementation-defined behavior

**definition** _implementation-defined behavior_ is program behavior that is not specified by the [[c]] standard and that may offer different results among implementations [...]. &mdash; Effective C

> **example** the number of bits in a byte

### unspecified behavior

**definition** _unspecified behavior_ is program behavior for which the standard provides two or more options and imposes no requirements on which option is chosen at any instance &mdash; Effective C

> **example** function parameter storage layout

### undefined behavior

**definition** _undefined behavior_ is behavior that implicitly or explicitly isn't defined by the [[c]] standard &mdash; Effective C

> **example** signed integer overflow, dereferencing an invalid pointer value

> **note** classifying behavior as _undefined_ is **intentional** and **considered**; it isn't an error or omission in the [[c]] standard

upon encountering undefined behavior, a compiler may:

- ignore undefined behavior completely, giving unpredictable results
- behave in a documented manner characteristic of the environment (with or without issuing a diagnostic)
- terminate a translation or execution (with issuing a diagnostic)

undefined behavior is a tool for the compiler to optimize programs even further

> **example** since division by zero is undefined behavior, the compiler can assume the [[variable]] `a` in an expresion such as `1 / a` will never be zero. it can then build onto that assumption for further optimization

## lifetimes

objects declared within a block or within a function parameter have _automatic_ lifetimes, living from the start to the end of the block

> **example**
>
> ```C
> {
>   int x;
> }
> ```

objects declared in file scope have _static_ lifetimes, living throughout the execution of the program

> **example**
>
> ```C
> int x;
> ```

objects declared within a block can be made to have a static lifetime using the `static` keyword

> **example**
>
> the program below outputs `1 2 3 4 5 `
>
> ```C
> void increment(void) {
>   static unsigned int counter = 0;
>   counter++;
>   printf("%d ", counter);
> }
>
> int main(void) {
>   for (int i = 0; i < 5; i++) {
>     increment();
>   }
> }
> return 0;
> ```

_thread_ lifetimes #todo

_allocated_ lifetimes #todo

## data types

**see** [[type]]

```C
_Bool // boolean
char // character
void // void

// signed integer data
signed char
short int // aka `short`
int
long int // aka `long`
long long int // aka `long long`

// unsigned integer data
unsigned signed char
unsigned short int // aka `unsigned short`
unsigned int
unsigned long int // aka `unsigned long`
unsigned long long int // aka `unsigned long long`

// floating-point data
float
double
long double

// user-defined types
enum, struct, union, typedef
```

> **examples**
>
> ```C
> enum day { sun, mon, tue, wed, thu, fri, sat };
> enum month { jan = 1, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec };
>
> struct {
>   int x;
>   int y;
> } point;
>
> union {
>   float f;
>   char c;
> } u;
>
> char *str;
> int arr[10];
> int f(void);
>
> typedef unsigned int uint_type;
> ```

> **note** `stdbool.h` defines the following:
>
> ```C
> #define bool _Bool
> #define true 1
> #define false 0
> ```

> **note** `void f();` declares a function that takes any number of arguments or any type. `void f(void);` declares a function that takes no arguments. the former is to be avoided

> **note**
>
> ```C
> char *src, c;
> int x, y[5];
> // is equivalent to
> char *src;
> char c;
> int x;
> int y[5];
> ```

> **note**
>
> ```C
> typedef signed char schar_type, *schar_p, (*fp)(void);
> // is equivalent to
> typedef signed char schar_type;
> typedef signed char *schar_p;
> typedef signed char (*fp)(void);
> ```
>
> - `schar_type` is an alias to `signed char`
> - `schar_p` is a pointer to `signed char *`
> - `fp` is an alias to `char(*)(void)`

each compiler implementation defines `char` as either `signed char` or `unsigned char`. regardless of the choice made, `char` is a different type from the other two and is incompatible with both. `char` is to be used for characters **only**, and `signed char` and `unsigned char` for small integer data

the size of integer data types is implementation-defined behavior and is available in `limits.h`

actual width integers such as `uint32_t`, and widest integer types `uintmax_t` and `intmax_t`, are available in `stdint.h` and `inttypes.h`

floating-point implementations are implementation-defined behavior

## tags

tags are a special naming mechanism for `enum`, `struct`, and `union` types. they live in a seperate namespace from ordinary identifiers

> **note**
>
> the snippets below are valid
>
> ```C
> struct s { };
> struct s s; // an object `s` of type `struct s`
>
> enum status { ok, fail };
> enum status status(void); // a function `status` that returns an `enum status`
>
> // the name of the type and of the tag can be the same
> typedef struct tnode {
>   struct tnode *left;
>   struct tnode *right;
> } tnode;
> ```

#todo currently on page 31

## reserved identifiers

any identifier matching the [[regular expression]]s `/__.*/` or `/_[A-Z].*/` or `/int[0-9a-z_]*_t/` or `/uint[0-9a-z_]*_t/` is reserved and is not to be used
