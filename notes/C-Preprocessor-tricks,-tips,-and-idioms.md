# Basic
## Pattern Matching
The `##` operator is used to concatenate two tokens into one token. This is provides a very powerful way to do pattern matching. Say we want to write a `IIF` macro, we could write it like this:
```c
#define IIF(cond) IIF_ ## cond
#define IIF_0(t, f) f
#define IIF_1(t, f) t
```
However there is one problem with this approach. A subtle side effect of the `##` operator is that it inhibits expansion. Heres an example:
```c
#define A() 1
//This correctly expands to true
IIF(1)(true, false) 
// This will however expand to IIF_A()(true, false)
// This is because A() doesn't expand to 1,
// because its inhibited by the ## operator
IIF(A())(true, false) 
```
The way to work around this is to use another indirection. Since this is commonly done we can write a macro called `CAT` that will concatenate without inhibition.
```c
#define CAT(a, ...) PRIMITIVE_CAT(a, __VA_ARGS__)
#define PRIMITIVE_CAT(a, ...) a ## __VA_ARGS__
```
So now we can write the `IIF` macro(its called `IIF` right now, later we will show how to define a more generalized way of defining an `IF` macro):
```c
#define IIF(c) PRIMITIVE_CAT(IIF_, c)
#define IIF_0(t, ...) __VA_ARGS__
#define IIF_1(t, ...) t

#define A() 1
//This correctly expands to true
IIF(1)(true, false) 
// And this will also now correctly expand to true
IIF(A())(true, false) 
```
With pattern matching we can define other operations, such as `COMPL` which takes the complement:
```c
#define COMPL(b) PRIMITIVE_CAT(COMPL_, b)
#define COMPL_0 1
#define COMPL_1 0
```
or `BITAND`:
```c
#define BITAND(x) PRIMITIVE_CAT(BITAND_, x)
#define BITAND_0(y) 0
#define BITAND_1(y) y
```
We can define increment and decrement operators as macros:
```c
#define INC(x) PRIMITIVE_CAT(INC_, x)
#define INC_0 1
#define INC_1 2
#define INC_2 3
#define INC_3 4
#define INC_4 5
#define INC_5 6
#define INC_6 7
#define INC_7 8
#define INC_8 9
#define INC_9 9

#define DEC(x) PRIMITIVE_CAT(DEC_, x)
#define DEC_0 0
#define DEC_1 0
#define DEC_2 1
#define DEC_3 2
#define DEC_4 3
#define DEC_5 4
#define DEC_6 5
#define DEC_7 6
#define DEC_8 7
#define DEC_9 8
```
## Detection
Detection techniques can be used to detect if the parameter is a certain value or if it is parenthesis. It relies on vardiac arguments expanding to different number of parameters. At the core of detection is a `CHECK` macro with a `PROBE` macro like this:
```c
#define CHECK_N(x, n, ...) n
#define CHECK(...) CHECK_N(__VA_ARGS__, 0,)
#define PROBE(x) x, 1,
```
This is very simple. When the probe is given to the `CHECK` macro like this:
```c
CHECK(PROBE(~)) // Expands to 1
```
But if we give it a single token:
```c
CHECK(xxx) // Expands to 0
```
So with this, we can create some detection macros. For instance, if we want to detect for parenthesis:
```c
#define IS_PAREN(x) CHECK(IS_PAREN_PROBE x)
#define IS_PAREN_PROBE(...) PROBE(~)
IS_PAREN(()) // Expands to 1
IS_PAREN(xxx) // Expands to 0
```
Now, say we want to write a generalized `IF` macro that picks false if its 0 otherwise it would pick true. We can use these detection techniques to do that. First, we start by writing a `NOT` operator which is just like an `IS_0` macro:
```c
#define NOT(x) CHECK(PRIMITIVE_CAT(NOT_, x))
#define NOT_0 PROBE(~)
```
Next we use the `COMPL` macro that we wrote to inverse this result, and then call `IIF`:
```c
#define BOOL(x) COMPL(NOT(x))
#define IF(c) IIF(BOOL(c))
```
We can also create a `WHEN` macro, that only expands whats next, if the condition is true, otherwise it will expand to nothing:
```c
#define EAT(...)
#define EXPAND(...) __VA_ARGS__
#define WHEN(c) IF(c)(EXPAND, EAT)
```
# Recursion
Unfortunately, macros can't expand recursively. When a macro expands, it can become painted blue, which prevents it from expanding anymore. First, there are ways to work around this to prevent macros from being painted blue. Secondly, we can detect if a macro is painted blue(because it wont expand) and use this state to expand to a different macro.
## Deferred expression
A deferred expression is an expression that requires more scans to fully expand. Heres an example:
```c
#define EMPTY()
#define DEFER(id) id EMPTY()
#define OBSTRUCT(...) __VA_ARGS__ DEFER(EMPTY)()
#define EXPAND(...) __VA_ARGS__

#define A() 123
A() // Expands to 123
DEFER(A)() // Expands to A () because it requires one more scan to fully expand
EXPAND(DEFER(A)()) // Expands to 123, because the EXPAND macro forces another scan
```
Why is this important? Well when a macro is scanned and expanding, it creates a disabling context. This disabling context will cause a token, that refers to the currently expanding macro, to be painted blue. Thus, once its painted blue, the macro will no longer expand. This is why macros don't expand recursively. However, a disabling context only exists during one scan, so by deferring an expansion we can prevent our macros from becoming painted blue. We will just need to apply more scans to the expression. We can do that using this `EVAL` macro:
```c
#define EVAL(...)  EVAL1(EVAL1(EVAL1(__VA_ARGS__)))
#define EVAL1(...) EVAL2(EVAL2(EVAL2(__VA_ARGS__)))
#define EVAL2(...) EVAL3(EVAL3(EVAL3(__VA_ARGS__)))
#define EVAL3(...) EVAL4(EVAL4(EVAL4(__VA_ARGS__)))
#define EVAL4(...) EVAL5(EVAL5(EVAL5(__VA_ARGS__)))
#define EVAL5(...) __VA_ARGS__
```
We use a `REPEAT_INDIRECT` macro to refer back to itself recursively. This prevents the macro from being painted blue, since it will expand on a different scan(and using a different disabling context). We use `OBSTRUCT` here, which will defer the expansion twice. This is necessary because the conditional `WHEN` applies one scan already.
```c
#define REPEAT(count, macro, ...) \
    WHEN(count) \
    ( \
        OBSTRUCT(REPEAT_INDIRECT) () \
        ( \
            DEC(count), macro, __VA_ARGS__ \
        ) \
        OBSTRUCT(macro) \
        ( \
            DEC(count), __VA_ARGS__ \
        ) \
    )
#define REPEAT_INDIRECT() REPEAT

//An example of using this macro
#define M(i, _) i
EVAL(REPEAT(8, M, ~)) // 0 1 2 3 4 5 6 7

```
Also we can build a `WHILE` macro that takes a user defined predicate, like so:
```c
#define WHILE(pred, op, ...) \
    IF(pred(__VA_ARGS__)) \
    ( \
        OBSTRUCT(WHILE_INDIRECT) () \
        ( \
            pred, op, op(__VA_ARGS__) \
        ), \
        __VA_ARGS__ \
    )
#define WHILE_INDIRECT() WHILE
```
This will keep on applying the `op` macro until the `pred` returns true.
## Comparison
In order to compare two tokens, we can take advantage of the fact that tokens get painted blue. We can put the macro inside of the another macro, and then detect if it expands or not. If the two macros are not the same then it won't fully expand. So if we want to compare two tokens `foo` and `bar`, we can define two corresponding marcos:
```c
#define COMPARE_foo(x) x
#define COMPARE_bar(x) x
```
And we can put them together to create a primitive compare macro:
```c
#define PRIMITIVE_COMPARE(x, y) IS_PAREN \
( \
COMPARE_ ## x ( COMPARE_ ## y) (())  \
)
```
Parenthesis is passed to the compare macros, and then it uses the `IS_PAREN` to detect if the macro fully expands(which it won't expand to parenthesis if it was painted blue). So this can be used to see if two tokens are not equal, like this:
```c
PRIMITIVE_COMPARE(foo, bar) // Expands to 1
PRIMITIVE_COMPARE(foo, foo) // Expands to 0
```
So this almost works, but only for tokens that have a corresponding `COMPARE_` macro defined:
```c
PRIMITIVE_COMPARE(foo, unfoo) // Should expand to 1, but it expands to 0
```
So we add an extra level of detection, to detect whether both of the tokens are comparable, and then calling our `PRIMITIVE_COMPARE` macro:
```c
#define IS_COMPARABLE(x) IS_PAREN( CAT(COMPARE_, x) (()) )

#define NOT_EQUAL(x, y) \
IIF(BITAND(IS_COMPARABLE(x))(IS_COMPARABLE(y)) ) \
( \
   PRIMITIVE_COMPARE, \
   1 EAT \
)(x, y)
```
And now we can create a corresponding `EQUAL` macro by using our previous `COMPL` macro:
```c
#define EQUAL(x, y) COMPL(NOT_EQUAL(x, y))
```

