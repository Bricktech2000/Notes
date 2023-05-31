# C

_assembly with syntactic sugar_

&mdash; <https://youtu.be/A3AdN7U24iU>

&mdash; Effective C by Robert C. Seacord

**see** [[math notation]]

**tradeoffs**

- high performance (fast, very little overhead, very little resources)
- great portability (compilers support many different targets)
- great simplicity (language is simple, not much syntax to learn)
- great stability (code doesn't break or become obsolete)

- memory unsafety (use-after-free, double-free, memory leaks, buffer overreads and overwrites, [[null]] pointers, data races...)

## Array Indexing Quirk

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
> // file scope
> int x;
> ```

objects declared within a block can be made to have a static lifetime using the `static` storage-class specifier

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

objects stored in dynamically allocated memory have _allocated_ lifetimes, living from the time they are allocated to the time they are deallocated

> **example**
>
> ```c
> int *x = malloc(sizeof(int));
> free(x);
> ```

_thread_ lifetimes #todo

## data types

**see** [[type]]

```c
_Bool // boolean
void // void

// characters
char
wchar_t
char16_t // UTF-16
char32_t // UTF-32

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

> **example**
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

> **example**
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

until C23, `void f();` declares a function that takes any number of arguments of any type. `void f(void);` declares a function that takes no arguments. the former is to be avoided &mdash; <https://en.wikipedia.org/wiki/Compatibility_of_C_and_C++>

`stdbool.h` defines the following:

```c
#define bool _Bool
#define true 1
#define false 0
```

**definition** an _lvalue_ is an expression that refers to an object; it makes sense for it to be on the left (or right) side of an assignment

**definition** an _rvalue_ is an expression that does not refer to an object; it only makes sense for it to be on the right side of an assignment

## type qualifiers

**definition** _type qualifiers_ are keywords that modify the meaning of a type &mdash; GitHub Copilot

`const` is a type qualifier that specifies that an object's value cannot be modified after initialization. the compiler can place `const`-qualified objects in read-only memory, which makes modifying them _undefined behavior_

> **example**
>
> ```c
> const int x = 1;
> x = 2; // error
>
> int *p = (int *)&x;
> *p = 2; // undefined behavior
> ```

`volatile` is a type qualifier that specifies that an object's value could be modified by something beyond the control of the program, such as a hardware device. this prevents the compiler from optimizing away reads and writes to the object

> **example**
>
> ```c
> volatile int port;
> port = port; // will generate instructions to read and write to `port`
> ```

`restrict` is a type qualifier that specifies that a pointer is the only way to access the object it points to. this allows the compiler to perform additional [[optimization]]

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

## tags

tags are a special naming mechanism for `enum`, `struct`, and `union` types. they live in a seperate namespace than that of ordinary identifiers

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

## flexible array members

[[c]] allows the last member of a `struct` to be a _flexible array member_ &mdash; an array of unspecified length. calling `sizeof` on a `struct` with a _flexible array member_ will return the size of the `struct` disregarding the flexible array member

> **example**
>
> ```c
> struct s {
>   int x;
>   int y[];
> };
>
> struct s *p = malloc(sizeof(struct s) + 10 * sizeof(int));
> ```

## statements

[[c]] includes the following statements, most of which are self-explanatory:

```c
if (expression) statement

if (expression) statement else statement

while (expression) statement

do statement while (expression);

for (expression; expression; expression) statement

switch (expression) statement

goto label;

continue;

break;

return expression;
```

the type of the controlling expression to a `switch` statement must be an _integer type_. _integer promotions_ are performed on the controlling expression. the constant expression in each `case` label is converted to the type of the promoted controlling expression

returning no value from a non-`void` [[function]] (through `return;` or through control reaching the end of the [[function]] body) and subsequently using the returned value is _undefined behavior_ in [[c]]

## reserved identifiers

any identifier matching the [[regular expression]]s `/__.*/` or `/_[A-Z].*/` or `/int[0-9a-z_]*_t/` or `/uint[0-9a-z_]*_t/` is reserved and is not to be used

## order of evaluation

_the order of evaluation of the operands of any [[c]] [[operator]], including the order of evaluation of any subexpressions, is generally unspecified behavior_ &mdash; Effective C

> **example**
>
> ```c
> int f(void);
> int g(void);
> int sum = f() + g(); // order of evaluation is unspecified
> int max = max(f(), g()); // order of evaluation is unspecified
> ```

_if a side effect is unsequenced relative to either a different side effect on the same scalar of a value computation that uses the value of the same scalar object, the code has undefined behavior_ &mdash; Effective C

> **example**
>
> ```c
> int i = 5;
> printf("%d\n", i++ * i++); // undefined behavior
> printf("%d %d\n", i++, i); // undefined behavior
> ```

it is guaranteed that the `&&` and `||` [[operator]]s will evaluate their operands from left to right. the `&&` and `||` [[operator]]s "short-circuit" in [[c]]

it is guaranteed that the `? :` [[operator]] will evaluate its first operand before its second or third operand. only one of the second and third operands will be evaluated

## dynamic allocation

### heap allocation

`stdlib.h` defines various [[function]]s for dealing with dynamic memory allocation, including `malloc`, `calloc`, `realloc` and `free`. [[c]] memory allocation [[function]]s will ensure proper alignment so any [[type]] can be correctly stored in the allocated memory

> **note**
>
> in [[c]], a `void *` is implicitly converted to any other pointer type
>
> > **example**
> >
> > the following is valid [[c]]:
> >
> > ```c
> > int *pi = malloc(sizeof(int));
> > ```

> **note** reading uninitialized memory is not _undefined behavior_ in [[c]]. with that said, is is not a great idea to do so

`void *malloc(size_t size)` allocates `size` bytes of memory and returns a pointer to the allocated memory. the memory is not initialized. if `size == 0`, `malloc` returns either `NULL` or a unique pointer value that can later be passed to `free`. if `malloc` fails to allocate memory, it returns `NULL`

`void *calloc(size_t nmemb, size_t size)` allocates `nmemb * size` bytes of memory and returns a pointer to the allocated memory. the memory is initialized to all bits zero. if `nmemb == 0` or `size == 0`, `calloc` returns either `NULL` or a unique pointer value that can later be passed to `free`. if `nmemb * size` overflows, `calloc` returns `NULL`. if `calloc` fails to allocate memory, it returns `NULL`

`void *realloc(void *ptr, size_t size)` changes the size of the memory block pointed to by `ptr` to `size` bytes and returns a pointer to the reallocated memory. the contents of the memory block are preserved up to the lesser of the new and old sizes. if `ptr == NULL`, `realloc` behaves like `malloc`. if `size == 0`, `realloc` behaves like `free`. if `realloc` fails to allocate memory, it returns `NULL` and leaves the original memory block unchanged

> **example**
>
> the following leaks memory:
>
> ```c
> int *p = malloc(0x10);
> // ...
> if ((p = realloc(p, 0x20)) == NULL) return NULL;
> ```

`void free(void *ptr)` frees the memory block pointed to by `ptr`. if `ptr == NULL`, `free` does nothing. calling `free` on a pointer that was not returned by `malloc`, `calloc` or `realloc` is _undefined behavior_ in [[c]]. calling `free` on a pointer that has already been freed is _undefined behavior_ in [[c]]

> **note** to mitigate issues with dangling pointers and double-frees, it is considered good practice to set pointers to `NULL` after freeing them

### stack allocation

`void *alloca(size_t size)` is a [[function]] that allocates memory on the stack. it is not part of the [[c]] standard, but is supported by many [[c]] compilers. `alloca` is declared in `alloca.h`. using `alloca` is risky:

- `alloca` can very quickly cause a stack overflow if used incorrectly
- calling `free` on a pointer returned by `alloca` is _undefined behavior_ in [[c]]

_variable-length arrays_ (VLAs) are a [[c]] feature that allows for the declaration of [[array]]s with runtime-specified lengths in the current [[stack]] frame. calling `sizeof` on a VLA will be evaluated at runtime

> **example** _VLA in block scope_
>
> ```c
> void func(size_t size) {
>   int vla[size];
> }
> ```

> **example** _VLA in function prototype scope_
>
> the [[function]] below takes a 2D [[array]] of any size. to index into a multi-dimensional array, the compiler needs to know the sizes of its innermost dimensions, which, in this case, are unknown at compile time. this would be somewhat awkward to accomplish without VLAs
>
> ```c
> int matrix_sum(size_t rows, size_t cols, int matrix[rows][cols]) {
>   // ...
> }
> ```

## arithmetic

### arithmetic literals

&mdash; <https://en.cppreference.com/w/cpp/language/floating_literal>

```c
// literals
42 // decimal integer
0b101010 // binary integer
052 // octal integer
0x2a // hexadecimal integer
0x1e5 // hexadecimal integer with exponent
3.14 // decimal floating-point
314e-2 // decimal floating-point with exponent
0.0314E+2 // decimal floating-point with exponent
0x0.3p10 // hexadecimal floating-point with exponent

// suffixes
42L // long integer
42LL // long long integer
42U // unsigned integer
42UL // unsigned long integer
42ULL // unsigned long long integer
3.14f // float
3.14F // float
3.14 // double
3.14l // long double
3.14L // long double
```

### arithmetic types

each compiler implementation defines `char` as either `signed char` or `unsigned char`. regardless of the choice made, `char` is a different type from the other two and is incompatible with both. `char` is to be used for characters **only**, and `signed char` and `unsigned char` for small integer data

actual-width integers such as `uint32_t`, and widest integer types `uintmax_t` and `intmax_t`, are available in `stdint.h` and `inttypes.h`

the size of integer data types is _implementation-defined behavior_ and is available in `limits.h`:

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

_wraparound_ (which is specific to unsigned integers) is well-defined behavior in [[c]]. values are reduced modulo the number that is one greater than the largest value that can be represented by the resulting type. however, _overflow_ (which is specific to signed integers) is _undefined behavior_ in [[c]]

the representation of signed integers in [[c]] is _implementation-defined behavior_. historically, the C language has supported three representation schemes:

- two's [[complement]]
- one's [[complement]]
- [[sign-magnitude notation]]

implementation of [[floating point]] numbers is _implementation-defined behavior_

`math.h` defines the following macros to classify [[floating point]] numbers:

```c
int fpclassify(real-floating x);
int isfinite(real-floating x);
int isinf(real-floating x);
int isnan(real-floating x);
int isnormal(real-floating x);
int signbit(real-floating x);

// fpclassify returns one of the following:
FP_INFINITE
FP_NAN
FP_NORMAL
FP_SUBNORMAL
FP_ZERO
```

### arithmetic conversions

**definition** the _integer types_ in [[c]] are `char`, `short`, `int`, `long`, `long long` and `enum`. \_Bool is also treated as an integer type when it comes to type promotions

**definition** the _small integer types_ in [[c]] are _integer types_ whose _conversion rank_ is less than `int`: `_Bool`, `char` and `short`

explicit conversions are performed using the _cast [[operator]]_ `(type)expression`

> **example**
>
> ```c
> float x = 3.14;
> int y = (int)x; // y == 3
> ```

implicit conversions, also known as _coercions_, are performed as follows:

simplistically, whenever a _small integer type_ is used in an expression in [[c]], it is converted to a `signed int` regardless of its signedness, or to an `unsigned int` under specific conditions. this process is called the _integer promotions_. this has the side effect that almost no operation in [[c]] can be performed directly on _small integer types_; operations are always carried out on `int`s or larger types

whenever a binary [[operator]] is applied to two operands of different types, [[c]] enforces an implicit conversion of one of the operands to the type of the other operand. the rules for this process are called _the usual arithmetic conversions_. simplistically, if one of the arguments has a [[floating point]] type, then the other is converted to that [[floating point]] type; otherwise, the _integer promotions_ are performed on both operands. then, if both operands have identical signedness, the operand with lesser _conversion rank_ is converted to the type of the other; otherwise, things get complicated and unintuitive

&mdash; Effective C p. 49-55 and <https://stackoverflow.com/questions/46073295/implicit-type-promotion-rules>

### pointer arithmetic

adding or subtracting an _integer type_ to or from a pointer [[type]] in [[c]] returns a value whose [[type]] is that of the pointer operand. this partly explains the [[c#array indexing quirk]]. the difference between the [[array]] subscripts is the value of the [[integer]] operand

> **note** the [[c]] standard does not impose that the members of a `struct` be contiguous. therefore, when using pointer arithmetic on members of a [[c]] `struct`s, one should use the `offsetof` macro from `stddef.h` to determine the offset of the element from the beginning of the `struct`

the resulting pointer must point to an element of the same [[array]] as the original pointer, or to an element one past the end of the [[array]] for historical reasons (known as the "too-far" pointer). otherwise, the behavior is _undefined behavior_. note that [[scalar]]s are considered length-one [[array]]s

> **example**
>
> ```c
> int m[2] = {1, 2};
>
> int sub_m_elements(void) {
>   int sum = 0;
>   for (int *pi = &m[0]; pi < &m[2]; pi++) sum += *pi; // &m[2] is a "too-far" pointer
>   return sum;
> }
> ```

## operators

for historical reasons, the return [[type]] of the `!`, `==`, `!=`, `<`, `>`, `<=` and `>=` [[operator]]s is `int` and not `_Bool`

`a / b` with `b == 0` is _undefined behavior_ in [[c]]

the [[c]] language imelements _truncating division_; that is,

| quotient        | remainder        |
| --------------- | ---------------- |
| `10 / 3 == 3`   | `10 % 3 == 1`    |
| `10 / -3 == -3` | `10 % -3 == 1`   |
| `-10 / 3 == -3` | `-10 % 3 == -1`  |
| `-10 / -3 == 3` | `-10 % -3 == -1` |

left shifting a negative number is _undefined behavior_ in [[c]]. left shifting a signed positive number leading to an _overflow_ is _undefined behavior_ in [[c]]. right shifting a negative number is _implementation-defined behavior_ in [[c]]; either an arithmetic shift or a logical shift is performed

shifting by a negative number of bits or by a number of bits greater than or equal to the width of the _integer-promoted_ left operand is _undefined behavior_ in [[c]]

the _usual arithmetic conversions_ are **not** performed on the operands of the `<<` and `>>` [[operator]]s

type casts in [[c]] either reinterpret the bits of a value or perform a conversion

> **example**
>
> ```c
> float x = 1.2f;
> int y = *(int *)&x; // reinterpret the bits of x as an int
> int z = (int)x; // converts x to an int
> ```

using one of `<`, `<=`, `>` or `>=` on two pointers to different objects is _undefined behavior_ in [[c]]

> **example**
>
> ```c
> int x, y;
> &x < &y; // undefined behavior
> x == y; // well-defined behavior
> x != y; // well-defined behavior
> ```

the `,` [[operator]] evaluates its left operand, discards the result, then evaluates its right operand and returns that result

> **example**
>
> ```c
> f(a, (t=3, t+2), c);
> // is equivalent to
> t = 3;
> f(a, t+2, c);
> ```

## textual data

### character literals

**see** [[ascii]]

```c
'a' // int
L'a' // wchar_t
u'a' // char16_t
U'a' // char32_t
```

| escape sequence | description     |
| --------------- | --------------- |
| `'\'`           | Apostrophe      |
| `'\"'`          | Quotation Mark  |
| `'\?'`          | Question Mark   |
| `'\\'`          | Backslash       |
| `'\a'`          | Alert           |
| `'\b'`          | Backspace       |
| `'\f'`          | Form Feed       |
| `'\n'`          | Newline         |
| `'\r'`          | Carriage Return |
| `'\t'`          | Horizontal Tab  |
| `'\v'`          | Vertical Tab    |
| `'\0'`          | Null            |
| `'\xhh'`        | Hexadecimal     |
| `'\ooo'`        | Octal           |

for historical reasons, the [[type]] of a [[character]] literal in [[c]] is `int` and not `char`. this differs from [[c++]]

### string literals

**see** [[ascii]], [[utf-8]]

```c
"foo" // char[6]
L"foo" // wchar_t[6]
u8"foo" // UTF-8 char[6]
u"foo" // char16_t[6]
U"foo" // char32_t[6]
```

[[c]] [[string]] literals can be used to construct both null-terminated [[string]]s and [[character]] [[array]]s:

```c
char *s = "foo"; // null-terminated string
char s[] = "foo"; // null-terminated string
char s[4] = "foo"; // null-terminated string
char s[3] = "foo"; // character array
```

writing to a string literal is _undefined behavior_ in [[c]]

> **note** `sizeof (char[])"foo"` is the length of the [[string]] including the null terminator (`4`) whereas `sizeof (char*)"foo"` is the size of the pointer (`sizeof char*`). `strlen((char*)"foo")` is the length of the [[string]] (`3`) but may incur a runtime cost
>
> #todo currently on pages 136 .. 142
