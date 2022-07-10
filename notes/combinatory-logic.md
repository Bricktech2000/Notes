# Combinatory Logic

see [[lambda-calculus]]

&mdash; <https://en.wikipedia.org/wiki/B,_C,_K,_W_system>

## Y Combinator

_allows for [[recursion]] in [[lambda-calculus]]_

_used to formally define recursive [[function]]s in a [[functional-programming]] language that does not support [[recursion]]_

in [[lambda-calculus]]: $Y = \lambda f.\ (\lambda x.\ f\ (x\ x)) (\lambda x.\ f\ (x\ x))$

in my [[math-notation]]: $Y = f \rightarrow (x \rightarrow f\ (x\ x))\ (x \rightarrow f\ (x\ x))$

> "it's not recursive but it encodes [[recursion]]" &mdash; <https://youtu.be/9T8A89jgeTI?t=678>

&mdash; <https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator>

## B Combinator

_the [[composition]] of its arguments_

> **AKA**: `(.)` in Haskell, "bluebird"

in [[lambda-calculus]] notation: $B = \lambda fgx.\ f\ (g\ x)$

in my [[math-notation]]: $B = f\ g\ x \rightarrow f\ (g\ x)$

&mdash; <https://youtu.be/SmXB2K_5lcA?t=612>

## C Combinator

_swaps the arguments to a function_

in my [[math-notation]]: $C = f\ x\ y \rightarrow f\ y\ x$

## K Combinator

_discards the second argument_

in my [[math-notation]]: $K = f\ x\ y \rightarrow f\ x$

## W Combinator

_duplicates the second argument_

in my [[math-notation]]: $W = f\ x\ y \rightarrow f\ x\ y\ y$
