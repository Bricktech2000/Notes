# C

_assembly with syntactic sugar_

&mdash; <https://youtu.be/A3AdN7U24iU>

&mdash; Effective C by Robert C. Seacord

**see** [[math notation]]

**pros**

- performance (fast, very little overhead, very little resources)
- portability (compilers support many different targets)
- simplicity (language is simple, not much syntax to learn)
- stability (code doesn't break or become obsolete)

**cons**

- memory unsafety (use-after-free, double-free, memory leaks, buffer overreads and overwrites, [[null]] pointers, data races...)

## array indexing quirk

```c
#include <stdio.h>

int main(void) {
  short a[4] = {1, 2, 3, 4};

  printf("%d", a[3]); // 4
  printf("%d", 3[a]); // 4
  prinf("%d", *(a + 3)); // 4
  printf("%d", *(3 + a)); // 4
}
```

## portability

&mdash; <https://www.reddit.com/r/rust/comments/jf66eu/why_are_there_no_increment_and_decrement/>

### implementation-defined behavior

**definition** _implementation-defined behavior_ is program behavior that is not specified by the [[c]] standard and that may offer different results among implementations [...]. &mdash; Effective C

> **example** the number of bits in a byte

a compiler must choose a single behavior, document it, and implement it consistently

### unspecified behavior

**definition** _unspecified behavior_ is program behavior for which the standard provides two or more options and imposes no requirements on which option is chosen at any instance &mdash; Effective C

> **example** function parameter storage layout

a compiler must compile the program meaningfully but may choose a different behavior each time it encounters a construct

### undefined behavior

**definition** _undefined behavior_ is behavior that implicitly or explicitly isn't defined by the [[c]] standard &mdash; Effective C

> **example** signed integer overflow, dereferencing an invalid pointer value

> **note** classifying behavior as _undefined_ is **intentional** and **considered**; it isn't an error or omission in the [[c]] standard

a compiler may:

- ignore undefined behavior completely, giving unpredictable results
- behave in a documented manner characteristic of the environment (with or without issuing a diagnostic)
- terminate a translation or execution (with issuing a diagnostic)
- produce arbitrary output (anything from a corrupted binary to a program that formats the hard drive)

undefined behavior is a tool for the compiler to optimize programs even further

> **example** since division by zero is undefined behavior, the compiler can assume the [[variable]] `a` in an expresion such as `1 / a` will never be zero. it can then build onto that assumption for further optimization

## lifetimes

objects declared within a block or within a function parameter have _automatic_ lifetimes, living from the start to the end of the block

> **example**
>
> ```c
> {
>   int x;
> }
> ```

objects declared in file scope have _static_ lifetimes, living throughout the execution of the program

> **example**
>
> ```c
> int x;
> ```

objects declared within a block can be made to have a static lifetime using the `static` keyword

> **example**
>
> the program below outputs `1 2 3 4 5 `
>
> ```c
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

```c
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
> ```c
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
> ```c
> #define bool _Bool
> #define true 1
> #define false 0
> ```

> **note** until C23, `void f();` declares a function that takes any number of arguments of any type. `void f(void);` declares a function that takes no arguments. the former is to be avoided &mdash; <https://en.wikipedia.org/wiki/Compatibility_of_C_and_C++>

> **note**
>
> ```c
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
> ```c
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

### arithmetic types

each compiler implementation defines `char` as either `signed char` or `unsigned char`. regardless of the choice made, `char` is a different type from the other two and is incompatible with both. `char` is to be used for characters **only**, and `signed char` and `unsigned char` for small integer data

actual-width integers such as `uint32_t`, and widest integer types `uintmax_t` and `intmax_t`, are available in `stdint.h` and `inttypes.h`

the size of integer data types is implementation-defined behavior and is available in `limits.h`:

| `limits.h` constant expression | type                 | standard-imposed minimum magnitude |
| ------------------------------ | -------------------- | ---------------------------------- |
| `UCHAR_MAX`                    | `unsigned char`      | **`2[8] . 1`**                     |
| `USHRT_MAX`                    | `unsigned short`     | **`2[16] . 1`**                    |
| `UINT_MAX`                     | `unsigned int`       | **`2[16] . 1`**                    |
| `ULONG_MAX`                    | `unsigned long`      | **`2[32] . 1`**                    |
| `ULLONG_MAX`                   | `unsigned long long` | **`2[64] . 1`**                    |
| `SCHAR_MIN`                    | `signed char`        | **`.(2[7] . 1)`**                  |
| `SCHAR_MAX`                    | `signed char`        | **`2[7] . 1`**                     |
| `SHRT_MIN`                     | `signed short`       | **`.(2[15] . 1)`**                 |
| `SHRT_MAX`                     | `signed short`       | **`2[15] . 1`**                    |
| `INT_MIN`                      | `signed int`         | **`.(2[15] . 1)`**                 |
| `INT_MAX`                      | `signed int`         | **`2[15] . 1`**                    |
| `LONG_MIN`                     | `signed long`        | **`.(2[31] . 1)`**                 |
| `LONG_MAX`                     | `signed long`        | **`2[31] . 1`**                    |
| `LLONG_MIN`                    | `signed long long`   | **`.(2[63] . 1)`**                 |
| `LLONG_MAX`                    | `signed long long`   | **`2[63] . 1`**                    |

_wraparound_ (which is specific to unsigned integers) is well-defined behavior in [[c]]. values are reduced modulo the number that is one greater than the largest value that can be represented by the resulting type. however, _overflow_ (which is specific to signed integers) is undefined behavior in [[c]]

the representation of signed integers in [[c]] is implementation-defined behavior. historically, the C language has supported three representation schemes:

- two's [[complement]]
- one's [[complement]]
- [[sign-magnitude notation]]

implementation of [[floating point]] numbers is implementation-defined behavior

#todo currently on page 45

## tags

tags are a special naming mechanism for `enum`, `struct`, and `union` types. they live in a seperate namespace from ordinary identifiers

> **note**
>
> the snippets below are valid
>
> ```c
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

## type qualifiers

**definition** _type qualifiers_ are keywords that modify the meaning of a type &mdash; GitHub Copilot

### `const`

`const` is a type qualifier that specifies that an object's value cannot be modified after initialization. the compiler can place `const`-qualified objects in read-only memory, which makes modifying them undefined behavior

> **example**
>
> ```c
> const int x = 1;
> x = 2; // error
>
> int *p = (int *)&x;
> *p = 2; // undefined behavior
> ```

### `volatile`

`volatile` is a type qualifier that specifies that an object's value could be modified by something beyond the control of the program, such as a hardware device. this prevents the compiler from optimizing away reads and writes to the object

> **example**
>
> ```c
> volatile int port;
> port = port; // will generate instructions to read and write to `port`
> ```

### `restrict`

`restrict` is a type qualifier that specifies that a pointer is the only way to access the object it points to. this allows the compiler to perform additional optimizations

> **example**
>
> ```c
> // `restrict` promises to the compiler that `s1` and `s2` do not overlap
> void copy(char *restrict s1, const char *restrict s2) {
>   while ((*s1++ = *s2++));
> }
>
> char s[10];
> copy(s, s + 1); // undefined behavior
> ```

## reserved identifiers

any identifier matching the [[regular expression]]s `/__.*/` or `/_[A-Z].*/` or `/int[0-9a-z_]*_t/` or `/uint[0-9a-z_]*_t/` is reserved and is not to be used
