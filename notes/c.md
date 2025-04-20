# C

_assembly with syntactic sugar and undefined behavior_

--- <https://youtu.be/A3AdN7U24iU>

--- Effective C by Robert C. Seacord

> **resource** _Advanced [[c]]: The UB and optimizations that trick good programmers._ by Eskil Steenberg --- <https://youtu.be/w3_e9vZj7D8>

> **resource** _How I program [[c]]_ by Eskil Steenberg, good opinions on [[c]] and on [[software engineering]] --- <https://youtu.be/443UNeGrFoM>

> **resource** _"New" Features in C_ by Dan Saks, a firehose of modern C features --- <https://youtu.be/ieERUEhs910>

> **resource** ISO/IEC 9899:TC3, WG14/N1256 --- <https://www.open-std.org/JTC1/SC22/WG14/www/docs/n1256.pdf>

what makes [[c]] timeless is not its simplicity; it's its [[durability]]. most constructs in [[c]] map trivially into assembly, which, in turn, maps trivially into machine code. in other words, there is a strong correspondence between the features of [[c]] and the fundamental ideas governing the design of processors and instruction sets. for this reason, [[programming language]]s that proudly claim to have the simplicity of [[c]]---like [[go]] does---should raise red flags

**tradeoffs**

- high performance (fast, very little overhead, very little resources)
- great portability (compilers support many different targets)
- great simplicity (language is simple, not much syntax to learn)
- great stability (code doesn't break or become obsolete)
- memory unsafety (use-after-free, double-free, memory leaks, buffer overreads and overwrites, [[null]] pointers, data races...)

## types and literals

**see** [[type]], [[ascii]], [[utf-8]]

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
unsigned char
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
>
> char *src, c;
> int x, y[5];
> typedef signed char schar_type, *schar_p, (*fp)(void);
> // is equivalent to
> char *src;
> char c;
> int x;
> int y[5];
> typedef signed char schar_type;
> typedef signed char *schar_p;
> typedef signed char (*fp)(void);
> ```

```c
// number literals
42 // decimal integer
0b101010 // binary integer
052 // octal integer
0x2a // hexadecimal integer
0x1e5 // hexadecimal integer with exponent
3.14 // decimal floating-point
314e-2 // decimal floating-point with exponent
0.0314E+2 // decimal floating-point with exponent
0x0.3p10 // hexadecimal floating-point with exponent

// number suffixes
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

// character literals
'a' // int
L'a' // wchar_t
u'a' // char16_t
U'a' // char32_t

// string literals
"foo" // char[6]
L"foo" // wchar_t[6]
u8"foo" // UTF-8 char[6]
u"foo" // char16_t[6]
U"foo" // char32_t[6]

// escape sequences
'\'' // Apostrophe
'\"' // Quotation Mark
'\?' // Question Mark
'\\' // Backslash
'\a' // Alert
'\b' // Backspace
'\f' // Form Feed
'\n' // Newline
'\r' // Carriage Return
'\t' // Horizontal Tab
'\v' // Vertical Tab
'\xhh' // Hexadecimal
'\ooo' // Octal
```

--- <https://en.cppreference.com/w/cpp/language/floating_literal>

`'\0'` is an octal escape sequence

[[c]] allows the last member of a `struct` to be a _flexible array member_---an array of unspecified length. calling `sizeof` on a `struct` with a _flexible array member_ will yield the size of the `struct` _as if the flexible array member were omitted except that it may have more trailing padding than the omission would imply_ --- ISO/IEC 9899:TC3, $6.7.2.1, paragraph 16

> **example** `struct { int size; char data[]; } *p = malloc(sizeof(*p) + sizeof(char[m]);`

> **note** generally, prefer `struct s *p = malloc(sizeof(*p));` to `struct s *p = malloc(sizeof(struct s));` when using `sizeof` --- <https://www.kernel.org/doc/Documentation/process/coding-style.rst> "Linux kernel coding style", $14 'Allocating memory', and <https://youtu.be/443UNeGrFoM?t=1h3m57s>
>
> > **note** `size_t zero(int a[10]) { return memset(a, 0, sizeof(a)); }` won't work, but `size_t zero(int (*a)[10]) { return memset(a, 0, sizeof(*a)); }` will

`sizeof char` is `1`, and the size of the other integer data types is implementation defined and is available in `limits.h`. each has a standard-imposed minimum magnitude; see ISO/IEC 9899:TC3, Annex E, paragraph 1. actual-width integers such as `uint32_t` and widest integer types `uintmax_t` and `intmax_t` are available in `stdint.h` and `inttypes.h`

_wraparound_ (which is specific to unsigned integers) has well-defined behavior in [[c]]. values are reduced modulo the number that is one greater than the largest value that can be represented by the resulting type. however, _overflow_ (which is specific to signed integers) has [[c#undefined behavior]]

the representation of signed integers in [[c]] is implementation defined. historically, the [[c]] language has supported three representation schemes: two's [[complement]], one's [[complement]] and [[sign--magnitude notation]]. the implementation of [[float]]ing-point numbers is implementation defined

each compiler implementation defines `char` as either `signed char` or `unsigned char`. regardless of the choice made, `char` is a different type from the other two and is incompatible with both. `char` is to be used for characters **only**, and `signed char` and `unsigned char` for small integer data

for historical reasons, the [[type]] of a [[character]] literal in [[c]] is `int` and not `char`. this differs from [[c++]]

writing to a string literal has [[c#undefined behavior]]; [[c]] [[string]] literals can be used to construct both null-terminated [[string]]s and [[character]] [[array]]s:

```c
char *s = "foo"; // null-terminated string
char s[] = "foo"; // null-terminated string
char s[4] = "foo"; // null-terminated string
char s[3] = "foo"; // character array
```

`sizeof (char[])"foo"` is the length of the [[string]] including the null terminator (`4`) whereas `sizeof (char*)"foo"` is the size of the pointer (`sizeof char*`). `strlen((char*)"foo")` is the length of the [[string]] (`3`) but may incur a runtime cost

`stdbool.h` defines `bool`, `true`, and `false`

`math.h` defines the various functions for classifying [[float]]ing-point numbers, such as `fpclassify`, `isfinite`, `isinf`, `isnan`, `isnormal` and `signbit`, along with various macros, such as `FP_INFINITE`, `FP_NAN`, `FP_NORMAL`, `FP_SUBNORMAL` and `FP_ZERO`

until C23, `void f();` declares a function that takes any number of arguments of any type. `void f(void);` declares a function that takes no arguments. the former is to be avoided --- <https://en.wikipedia.org/wiki/Compatibility_of_C_and_C++>

returning no value from a non-`void` [[function]] (through `return;` or through control reaching the end of the [[function]] body) and subsequently using the returned value has [[c#undefined behavior]]

### tags

tags are a special naming mechanism for `enum`, `struct`, and `union` types. they live in a separate namespace than that of ordinary identifiers

> **example** `struct s { }; struct s s;` is an object `s` of type `struct s`

> **example** `enum status { ok, fail }; enum status status(void);` is a function named `status` that returns an `enum status`

> **example** in `typedef struct tnode { struct tnode *left; struct tnode *right; } tnode;`, the type name and tag name are the same

### incomplete types

--- Effective C and <https://learn.microsoft.com/en-us/cpp/c-language/incomplete-types>

**definition** an _incomplete type_ is a type that describes an object but lacks information needed to determine its size

> **example** `struct s; enum e; int a[];` are all incomplete types

incomplete types can be completed by specifying the missing information. `void` is an incomplete type that cannot be completed

## declarations

reordering of declaration specifiers has no effect in [[c]] --- <https://youtu.be/zGWj7Qo_POY?t=21m28s>

> **example** `int typedef const a;` is equivalent to `typedef const int a;`, and `long unsigned static long b;` is equivalent to `static unsigned long long b;`

`*` is part of the _declarator_ and not of the _declaration specifier_, which is why `int* a;` is considered bad style

as a rule of thumb, read declarators from the inside out, at each level moving right then moving left

> **example** `float (*(*b(void))[])(void);` --- `b` is a function that returns a pointer to an array of pointers to functions returning `float`s --- <https://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations>

> **example** `void *(*c)(char, int (*)(void));` --- `c` is a pointer to a function that takes a `char` and {a pointer to a function that returns an `int`} and returns a pointer to `void` --- <https://www.codeproject.com/Articles/7042/How-to-interpret-complex-C-C-declarations>

> **example** in `const char *foo;` the pointer is constant while in `char *const foo` the pointee is constant

## initialization

--- <https://youtu.be/lLv1s7rKeCM?t=19m55s>

objects of pretty much any [[type]] can be initialized using _initializer lists_ in [[c]]

> **example** `int x = {5};` is valid [[c]]

initializer lists are brace-enclosed sequences of _positional initializers_ (which do not include a _designation_) and _designated initializers_ (which do include a _designation_). any subobjects not explicitly initialized are zeroed. initializers initialize subobjects in order according to the type of object being initialized, and designations cause the following initializers to continue initialization starting at the subobject designated --- ISO/IEC 9899:TC3, $6.7.8, paragraph 17

> **example** `struct { int a[10]; float f; } s = {.a = {2, 3, [8] = 7, 9, [1] = 5}, .f = 5.5, .a[9] = 8, 6.6};`

_empty initialization_ (informally also known as _zero initialization_ and _default initialization_), written `{0}`, zeroes out an object's memory. starting in C23, it can also be written `{}`

## compound literals

a _compound literal_, written _`(` type-name `)` `{` initializer-list `,`? `}`_, creates an unnamed lvalue (!!) of the specified type. compound literals used in _block scope_ have _automatic storage duration_ and live for the entire duration of the block; compound literals may be used in _file scope_, in which case they have _static storage duration_ --- ISO/IEC 9899:TC3, $6.5.2.5, paragraph 6

> **example** `struct vec2 zero(void) { return (struct vec2){0.0, 0.0}; }`

> **example** constructs such as `f(&(int){5});` can be used to pass a literal to a function expecting a pointer --- me

> **example** `(int){3} = 5;` is valid [[c]] --- me

> **example** `(char []){"/tmp/fileXXXXXX"}` is essentially a modifiable string literal --- ISO/IEC 9899:TC3, $6.5.2.5, paragraph 13

> **example** `*p = (struct p){0};` can be used to zero out a structure, say before returning from a destructuor --- <https://youtu.be/lLv1s7rKeCM?t=56m32s>

## lvalues and rvalues

**definition** an _lvalue_ is an expression that refers to an object; it makes sense for it to be on the left side of an assignment [[expression]]

**definition** an _rvalue_ is an expression that does not refer to an object; it only makes sense for it to be on the right side of an assignment [[expression]]

## pointer arithmetic

adding or subtracting an _integer type_ to or from a pointer [[type]] in [[c]] returns a value whose [[type]] is that of the pointer operand. the difference between the [[array]] subscripts is the value of the [[integer]] operand

> **example**
>
> ```c
> short a[4] = {1, 2, 3, 4};
> printf("%d", a[3]); // 4
> printf("%d", 3[a]); // 4
> prinf("%d", *(a + 3)); // 4
> printf("%d", *(3 + a)); // 4
> //*
> ```

the resulting pointer must point to an element of the same [[array]] as the original pointer, or to an element one past the end of the [[array]] (known as the "too-far" pointer). otherwise, the behavior is [[c#undefined behavior]]. scalars are treated as length-one [[array]]s

> **example** in `int m[2] = {1, 2}; for (int *p = &m[0]; p < &m[2]; p++);`, `&m[2]` is a "too-far" pointer

the [[c]] standard does not impose that the members of a `struct` be contiguous. therefore, when using pointer arithmetic on members of a [[c]] `struct`s, one should use the `offsetof` macro from `stddef.h` to determine the offset of the element from the beginning of the `struct`

in [[c]], a `void *` is implicitly converted to any other pointer type

> **example** `int *pi = malloc(sizeof(int));` is valid [[c]] but not valid [[c++]]

the _strict aliasing rule_ allows the compiler to assume that pointers to different types do not alias each other. therefore, apart from a few exceptions, referring to the same memory simultaneously through pointers of different types has [[c#undefined behavior]] --- <https://youtu.be/SmlLdd1Q2V8?t=5m46s>

> **example** `int x = 1; float *f = (float *)&x; *f = 2;` has [[c#undefined behavior]]

## type coercions

**definition** the _integer types_ in [[c]] are `char`, `short`, `int`, `long`, `long long` and `enum`. `_Bool` is also treated as an integer type when it comes to type promotions

**definition** the _small integer types_ in [[c]] are _integer types_ whose _conversion rank_ is less than `int`: `_Bool`, `char` and `short`

in [[c]], implicit type conversions, also known as _coercions_, are performed as follows:

simplistically, whenever a _small integer type_ is used in an expression in [[c]], it is converted to a `signed int` regardless of its signedness, or to an `unsigned int` under specific conditions. this process is called the _integer promotions_. this has the side effect that almost no operation in [[c]] can be performed directly on _small integer types_; operations are always carried out on `int`s or larger types

whenever a binary [[operator]] is applied to two operands of different types, [[c]] enforces an implicit conversion of one of the operands to the type of the other operand. the rules for this process are called _the usual arithmetic conversions_. simplistically, if one of the arguments has a [[float]]ing-point type, then the other is converted to that [[float]]ing-point type; otherwise, the _integer promotions_ are performed on both operands. then, if both operands have identical signedness, the operand with lesser _conversion rank_ is converted to the type of the other; otherwise, things get complicated and unintuitive

--- Effective C p. 49-55 and <https://stackoverflow.com/questions/46073295/implicit-type-promotion-rules>

## operators

for historical reasons, the return [[type]] of the `!`, `==`, `!=`, `<`, `>`, `<=` and `>=` [[operator]]s is `int` and not `_Bool`

`a / b` with `b == 0` has [[c#undefined behavior]]

the [[c]] language imelements _truncating division_; that is,

- `10 / 3 == 3` and `10 % 3 == 1`
- `10 / -3 == -3` and `10 % -3 == 1`
- `-10 / 3 == -3` and `-10 % 3 == -1`
- `-10 / -3 == 3` and `-10 % -3 == -1`

left shifting a negative number has [[c#undefined behavior]]. left shifting a signed positive number leading to an _overflow_ has [[c#undefined behavior]]. right shifting a negative number has [[c#implementation-defined behavior]]; either an arithmetic shift or a logical shift is performed

shifting by a negative number of bits or by a number of bits greater than or equal to the width of the _integer-promoted_ left operand has [[c#undefined behavior]]

the _usual arithmetic conversions_ are **not** performed on the operands of the `<<` and `>>` [[operator]]s

the _integer promotions_ are applied to the argument of the unary `+` and `-` [[operator]]s --- <https://youtu.be/zGWj7Qo_POY?t=1m37s>

> **example** `sizeof +(short)1` is equal to `sizeof(int)`

type casts in [[c]] can either reinterpret the bits of a value or perform a conversion

> **example** `int i = *(int *)&f;` reinterprets the bits of `float f` as an `int`

> **example** `int i = (int)f;` converts `float f` to an `int`

using one of `<`, `<=`, `>` or `>=` on two pointers to different objects has [[c#undefined behavior]]

> **example**
>
> ```c
> int x, y;
> &x < &y; // undefined behavior
> &x == &y; // well-defined behavior
> &x != &y; // well-defined behavior
> ```

the `,` [[operator]] evaluates its left operand, discards the result, then evaluates its right operand and returns that result

> **example** `f(a, (t=3, t+2), c);` is equivalent to `t = 3; f(a, t+2, c);`

the `&&` and `||` [[operator]]s "short-circuit" in [[c]]

exactly one of the second and third operands of the `? :` [[operator]] is evaluated

## order of evaluation

_the order of evaluation of the operands of any [[c]] [[operator]], including the order of evaluation of any subexpressions, generally has [[c#unspecified behavior]]_ --- Effective C

> **example** in `int sum = f() + g();`, the order of evaluation unspecified

> **example** in `int max = max(f(), g());`, the order of evaluation is unspecified

_if a side effect is unsequenced relative to either a different side effect on the same scalar or a value computation that uses the value of the same scalar object, the code has [[c#undefined behavior]]_ --- Effective C

> **example** `printf("%d\n", i++ * i++);` has [[c#undefined behavior]]

> **example** `printf("%d %d\n", i++, i);` has [[c#undefined behavior]]

> **example** `i = ++i;` has [[c#undefined behavior]] --- <https://stackoverflow.com/questions/78286568/in-standard-c-is-the-expression-i-i-1-1-well-defined>

there is a sequence point between the evaluations of the operands of the `&&`, `||` and `,` [[operator]]s

there is a sequence point between the evaluations of the first and second or third operands of the `? :` [[operator]], whichever is evaluated

there is **no** sequence point between evaluations of the operands of the `=` [[operator]], and the stored value may be updated any time between the previous and next sequence points --- ISO/IEC 9899:TC3, $6.5.16, paragraphs 3-4

## dynamic allocation

### heap allocation

`stdlib.h` defines various [[function]]s for dealing with dynamic memory allocation, including `malloc`, `calloc`, `realloc` and `free`. [[c]] memory allocation [[function]]s will ensure proper alignment so any [[type]] can be correctly stored in the allocated memory

`void *malloc(size_t size)` allocates `size` bytes of memory and returns a pointer to the allocated memory. the memory is not initialized. if `size == 0`, `malloc` returns either `NULL` or a unique pointer value that can later be passed to `free`. if `malloc` fails to allocate memory, it returns `NULL`

`void *calloc(size_t nmemb, size_t size)` allocates `nmemb * size` bytes of memory and returns a pointer to the allocated memory. the memory is initialized to all bits zero. if `nmemb == 0` or `size == 0`, `calloc` returns either `NULL` or a unique pointer value that can later be passed to `free`. if `nmemb * size` overflows, `calloc` returns `NULL`. if `calloc` fails to allocate memory, it returns `NULL`

`void *realloc(void *ptr, size_t size)` changes the size of the memory block pointed to by `ptr` to `size` bytes and returns a pointer to the reallocated memory. the contents of the memory block are preserved up to the lesser of the new and old sizes. if `ptr == NULL`, `realloc` behaves like `malloc`. if `size == 0`, `realloc` behaves like `free`. if `realloc` fails to allocate memory, it returns `NULL` and leaves the original memory block unchanged

`void free(void *ptr)` frees the memory block pointed to by `ptr`. if `ptr == NULL`, `free` does nothing. calling `free` on a pointer that was not returned by `malloc`, `calloc` or `realloc` has [[c#undefined behavior]]. calling `free` on a pointer that has already been freed has [[c#undefined behavior]]

### stack allocation

`void *alloca(size_t size)` is a [[function]] that allocates memory on the stack. it is not part of the [[c]] standard, but is supported by many [[c]] compilers. `alloca` is declared in `alloca.h`. using `alloca` is risky:

- `alloca` can very quickly cause a stack overflow if used incorrectly
- calling `free` on a pointer returned by `alloca` has [[c#undefined behavior]]

_variable-length arrays_ (VLAs) are a [[c]] feature that allows for the creation of [[array]]s with runtime-specified lengths on the stack (the [[c]] standard does not require VLAs to be placed on the stack, but most compilers do). `sizeof` on a VLA is evaluated at runtime

> **example** _VLA in block [[scope]]_ `void func(size_t size) { int vla[size]; }`

> **example** _VLA in function prototype [[scope]]_ `int matrix_sum(size_t rows, size_t cols, int matrix[rows][cols]);`

VLAs can be used to make indexing into dynamic multidimensional [[array]]s less cumbersome

> **example** `double *p = malloc(sizeof(*p) * rows * cols);` has to be indexed with `p[i * rows + j]` while `double (*p)[rows][cols] = malloc(sizeof(*p));` can be indexed with `(*p)[i][j]` and `double (*p)[rows] = malloc(sizeof(*p) * cols);` can be indexed with `p[i][j]`

## control flow

[[c]] includes the following control flow [[statement]]s, most of which are self-explanatory:

```c
if (expression) statement
if (expression) statement else statement
while (expression) statement
do statement while (expression)
for (expression; expression; expression) statement
switch (expression) statement
goto label
continue
break
return expression
```

the type of the controlling expression to a `switch` statement must be an _integer type_. _integer promotions_ are performed on the controlling expression. the constant expression in each `case` label is converted to the type of the promoted controlling expression

`else if` is not its own [[statement]] in [[c]]; rather, it is an `if-else` statement whose `else` clause contains another `if` statement

> **example** a common guideline is to always use braces to convert statements into compound statements inside of control flow statements. therefore, to be pedantic, `if (c) { ... } else if (d) { ... }` should be written as `if (c) { ... } else { if (d) { ... } }`. if `else-if`s are allowed, why aren't `else-switch`es? `if (!color) { alpha = 1; } else switch (*color) { ... }` --- <https://youtu.be/zGWj7Qo_POY?t=10m32s>

## reserved identifiers

--- ISO/IEC 9899:TC3, $7.1.3 'Reserved identifiers'

identifiers matching the [[regular expression]] `/_[_A-Z].*/` are reserved everywhere and those matching `/_.*/` are reserved at file scope including for tags. defining or declaring such an identifier or using such an identifier as a macro name has [[c#undefined behavior]]

## storage duration

objects declared within a block or within a function parameter and objects declared with the `auto` storage-class specifier have _automatic_ storage duration, living from the start to the end of the block. `auto` is a bit useless, because the only places it's allowed to be used, automatic storage duration is already the default --- <https://stackoverflow.com/questions/4688816/concept-of-auto-keyword-in-c>. starting in C23, `auto` provides [[c++]]-style "[[type inference]]" --- <https://youtu.be/lLv1s7rKeCM?t=11m45s>

> **example** `{ int x; }`

objects declared at file [[scope]] have _static_ storage duration, living throughout the execution of the program

> **example** `int x; // at file scope`

objects declared within a block can be made to have a static storage duration using the `static` storage-class specifier; not to be confused with `static` at file [[scope]]

> **example** `void increment(void) { static size_t counter = 0; return counter++; }`

objects stored in dynamically allocated memory have _allocated_ storage duration, living from the time they are allocated to the time they are deallocated

> **example** `int *x = malloc(sizeof(int)); free(x);`

objects declared with the `thread_local` storage-class specifier have _thread_ storage duration, living from thread startup to thread termination

> **example** `thread_local int x;`

## linkage

a declaration with _external linkage_ makes all its references refer to the same object throughout all translation units. objects declared at file [[scope]] have external linkage by default

> **example** `int x; int f(void); extern int x; extern int f(void); // at file scope`

`extern` at file scope has no effect on functions, but when used on variables it _doesn't instantiate the variable itself, i.e. doesn't allocate any memory_ --- <https://stackoverflow.com/questions/496448/how-to-correctly-use-the-extern-keyword-in-c>. `extern` should be used to declare global variables shared across translation units

block-scope objects can be made to have external linkage using the `extern` storage-class specifier

> **example** `{ extern int x; extern int f(void); }`

a declaration with _internal linkage_ makes all its references refer to the same object within the same translation unit. objects declared at file [[scope]] with the `static` storage-class specifier have internal linkage; not to be confused with `static` at block [[scope]]

> **example** `static int x; static int f(void); // at file scope`

> **example** `static` can be used to redefine a local version of some library function, say `static void *memchr(const void *s, int c, size_t n) { ... }`

> **note** it is good practice to mark file-scoped implementation details with `static` so as not to pollute the global namespace

a declaration with _no linkage_ makes all its references refer to the same object within the same block. identifiers with no linkage include function parameters, objects declared at block [[scope]] and enumeration constants

> **example** `{ int x; }` and parameter `x` at `int f(int x) { ... }`

## type qualifiers

`const` is a type qualifier that specifies that an object's value cannot be modified after initialization. the compiler can place `const`-qualified objects in read-only memory, which means modifying them has [[c#undefined behavior]]

> **example** `const int x = 1; x = 2;` produces an error

> **example** `int *p = (int *)&x; *p = 2;` has [[c#undefined behavior]]

`volatile` is a type qualifier that specifies that an object's value could be modified by something beyond the control of the program, such as a hardware device. this prevents the compiler from optimizing away reads and writes to the object

> **example** `volatile int port; port = port;` will generate instructions to read and write to `port`

`restrict` is a type qualifier that specifies that a pointer is the only way to access the object it points to. this allows the compiler to perform further optimization. using the `restrict` qualifier on two pointers that overlap has [[c#undefined behavior]]

> **example** `void copy(char *restrict s1, const char *restrict s2);`

## portability

--- <https://www.reddit.com/r/rust/comments/jf66eu/why_are_there_no_increment_and_decrement/>

### Implementation-Defined Behavior

**definition** _implementation-defined behavior_ is program behavior that is not specified by the [[c]] standard and that may offer different results among implementations [...] --- Effective C

a compiler must choose a single behavior, document it, and implement it consistently

### Unspecified Behavior

**definition** _unspecified behavior_ is program behavior for which the standard provides two or more options and imposes no requirements on which option is chosen at any instance --- Effective C

a compiler must compile the program meaningfully but may choose a different behavior each time it encounters a construct

### Undefined Behavior

**definition** _undefined behavior_ is behavior that implicitly or explicitly isn't defined by the [[c]] standard --- Effective C

classifying behavior as _undefined_ is **intentional** and **considered**; it isn't an error or omission in the [[c]] standard. [[c#undefined behavior]] is a tool the compiler can use to optimize programs; a compiler may assume programs never contain [[c#undefined behavior]]

a compiler may:

- ignore [[c#undefined behavior]] completely, giving unpredictable results
- behave in a documented manner characteristic of the environment (with or without issuing a diagnostic)
- terminate a translation or execution (with issuing a diagnostic)
- produce arbitrary output (anything from a corrupted binary to a program that formats the hard drive)

### indeterminate values

_trap representations_ are essentially a value in memory that cannot be represented by the [[type]] of an object. uninitialized memory contains _indeterminate values_, and it is implementation defined whether or not these values can be _trap representations_

reading a _trap representation_ has [[c#undefined behavior]]; reading an _uninitialized value_ does not necessarily have [[c#undefined behavior]] in [[c]] but does in [[c++]]. using _indeterminate values_ in arithmetic operations has [[c#undefined behavior]]

--- Effective C and <https://stackoverflow.com/questions/13423673/what-is-indeterminate-value>

## Preprocessor

--- Effective C

--- <https://cplusplus.com/doc/tutorial/preprocessor/>

> **resource** _Metaprogramming custom control structures in C_ by Simon Tatham --- [[Metaprogramming custom control structures in C.html]] and [[mp.h]] and [[mptest.c]] --- <https://www.chiark.greenend.org.uk/%7Esgtatham/mp/> and <https://www.chiark.greenend.org.uk/%7Esgtatham/mp/mp.h> and <https://www.chiark.greenend.org.uk/%7Esgtatham/mp/mptest.c>

> **resource** _Coroutines in C_ by Simon Tatham --- [[Coroutines in C.html]] and [[coroutine.h]] --- <https://www.chiark.greenend.org.uk/%7Esgtatham/coroutines.html> and <https://www.chiark.greenend.org.uk/%7Esgtatham/coroutine.h>

### directives

the [[c#preprocessor]] includes the following directives:

```c
#include
#define #undef
#ifdef #ifndef #if #elif #else #endif
#error
#line
#pragma
#
```

whitespace may added between the beginning of a line and a `#` character or between a `#` character and a directive name to indent directives

`#include` inserts the contents of a file into the current file. the file is searched for in an implementation-defined manner. if the file is not found, the behavior is [[c#implementation-defined behavior]]. if the file is found, the contents of the file are inserted into the current file at the point of the `#include` directive. the difference between quoted include strings (`#include "filename"`) and angle-bracketed include strings (`#include <filename>`) is implementation defined. typically, the former is used for user-defined headers and the latter for system headers

`#define identifier replacement-list` defines an _object-like macro_ named `identifier`; `#define identifier(parameter-list) replacement-list` (with no whitespace between `identifier` and `(`) defines a _function-like macro_ named `identifier`. macro identifiers textually expand to `replacement-list`. `replacement-list` may be empty, in which case instances of `identifier` will simply be removed. `#undef identifier` undefines macro `identifier` and is safe regardless of whether `identifier` is defined. instances of the `##` preprocessing token within a replacement list are deleted, concatenating the preceeding token with the following token; this process is called _token pasting_. if the result is not a valid token, the behavior is [[c#undefined behavior]]. within a function-like macro replacement list, a parameter preceeded by a `#` is replaced with a string literal containing the text of the argument; this process is sometimes called _stringizing_. an unparenthesized `,` within a function-like macro invocation is always interpreted as a macro argument, meaning `LOG([1, 2, 3])` invokes `LOG` with arguments `[1`, `2` and `3]`

> **example** given `#define DOTS .##.##.`, expansion of `DOTS` has [[c#undefined behavior]], because, even though `...` is a valid token, `..` is not

> **resource** Dave Prosser's C Preprocessing Algorithm --- [[x3J11-86-196.pdf]] --- <https://www.spinellis.gr/blog/20060626/>

`#ifdef`, `#ifndef`, `#if`, `#elif`, `#else` and `#endif` are used for conditional compilation. `#ifdef identifier` is equivalent to `#if defined identifier` which is equivalent to `#if defined(identifier)`. `#ifndef identifier` is equivalent to `#if !defined identifier` which is equivalent to `#if !defined(identifier)`. `#if` evaluates its expression and if it is nonzero, the following group of lines is compiled

`#error message` issues a diagnostic message that includes `messsage` then terminates translation

`#line line-number` sets the current line number to `line-number`. `#line line-number "filename"` sets the current line number to `line-number` and the current filename to `filename`

`#pragma` is used to issue implementation-defined commands to the compiler. no diagnostic is issued for an unknown `#pragma` directive

`#` (the _null directive_) is a no-op

### predefined macros

_predefined macros_ are macros implicitly defined by the [[c#preprocessor]]. they include, non-exhaustively:

`__LINE__` expands to the current line number as an integer literal

`__FILE__` expands to the name of the current file as a string literal

`__DATE__` expands to the current date as a string literal in the form `Mmm dd yyyy`

`__TIME__` expands to the current time as a string literal in the form `hh:mm:ss`

`__STDC__` expands to `1` if the implementation conforms to the [[c]] standard

### macro coloring

what color is your macro? in [[c]], expressions are syntactically a [[set#subset]] of statements, yet expressions are more usable than statements while statements are more capable than expressions. "uphold $A > B$ while minimizing $A$ while maximizing $B$": that's the function coloring problem; see <https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/>. concretely, macros that expand to a statement "red macros" are more capable but can only be used within statements and not within expressions, while macros that expand to an expression "blue macros" are less capable but can be used both within statements and within expressions

### useful idioms

--- <https://stackoverflow.com/questions/1067226/c-multi-line-macro-do-while0-vs-scope-block>

--- <https://stackoverflow.com/questions/3136686/is-the-c99-preprocessor-turing-complete>

--- <https://www.chiark.greenend.org.uk/%7Esgtatham/mp/mp.h>

--- <https://gist.github.com/jdah/1ae0048faa2c627f7f5cb1b68f7a2c02>

--- <https://stackoverflow.com/questions/2308243/macro-returning-the-number-of-arguments-it-is-given-in-c>

--- <https://youtu.be/lLv1s7rKeCM?t=1h15m7s>

macro-expand then token-paste/stringize

```c
#define PASTE_INNER(LHS, RHS) LHS##RHS
#define PASTE(LHS, RHS) PASTE_INNER(LHS, RHS)
// #define MKLABEL(ID) PASTE_INNER(_label_##ID##_, __LINE__)
// MKLABEL(some_id) // _label_some_id___LINE__
// #define MKLABEL(ID) PASTE(_label_##ID##_, __LINE__)
// MKLABEL(some_id) // _label_some_id_4
#define STRINGIZE_INNER(...) #__VA_ARGS__
#define STRINGIZE(...) STRINGIZE_INNER(__VA_ARGS__)
// #define SOME_MACRO(...) __VA_ARGS__
// STRINGIZE_INNER(SOME_MACRO(5)) // SOME_MACRO(5)
// STRINGIZE(SOME_MACRO(5))       // 5
```

commas within macro arguments

```c
// #define SOME_MACRO(...) __VA_ARGS__
#define COMMA ,
// SOME_MACRO([1 COMMA 2 COMMA 3])
#define WRAP(...) __VA_ARGS__
// SOME_MACRO(WRAP([1, 2, 3]))
```

uniform compound statements

```c
#define RETURN(VAL) do { some_cleanup(); return VAL; } while (0)
// if (some_condition)
//   RETURN(5);
// else
//   RETURN(6);
```

inhibit/force macro expansion

```c
#define EMPTY
#define DEFER(ID) ID EMPTY
#define EXPAND(...) __VA_ARGS__
// #define ZERO() 0
// ZERO()                // 0
// DEFER(ZERO)()         // ZERO ()
// EXPAND(DEFER(ZERO)()) // 0
```

X macros and higher-order macros

```c
#define NAMES X(FOO) X(BAR) X(BAZ)
// #define X(NAME) NAME,
// enum names { NAMES };
// #define X(NAME) [NAME] = #NAME,
// char *names[] = {NAMES};
#define NAMES(F) F(FOO) F(BAR) F(BAZ)
// #define MKENUM(NAME) NAME,
// enum names { NAMES(MKENUM) };
// #define MKSTRS(NAME) [NAME] = #NAME,
// char *names[] = {NAMES(MKSTRS)};
```

> **resource** the `NODE_TYPES` X macro in my [[automatic differentiation]] library --- <https://github.com/Bricktech2000/Autodiff/blob/master/lib/autodiff.h> and <https://github.com/Bricktech2000/Autodiff/blob/master/lib/autodiff.c>

overload on/expand to argument count

```c
#define SOME_FUNC_N(_3, _2, _1 NAME, ...) NAME
#define SOME_FUNC(...)                                                         \
  FUNC_N(__VA_ARGS__, ternary, binary, unary, nullary)(__VA_ARGS__)
// SOME_FUNC()        // undefined behavior
// SOME_FUNC(x)       // unary(x)
// SOME_FUNC(x, y)    // binary(x, y)
// SOME_FUNC(x, y, z) // ternary(x, y, z)
#define PP_NARG_N(_3, _2, _1, N, ...) N
#define PP_NARG(...) PP_NARG_N(__VA_ARGS__, 3, 2, 1, 0)
// PP_NARG()        // undefined behavior
// PP_NARG(x)       // 1
// PP_NARG(x, y)    // 2
// PP_NARG(x, y, z) // 3
```

> **note** using dummy `nullary` and `0` because C99 requires at least one argument to `...` --- ISO/IEC 9899:TC3, $6.10.3, paragraph 4, and `gcc -Wpedantic -std=c99`
