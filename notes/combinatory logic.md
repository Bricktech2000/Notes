# Combinatory Logic

**see** [[lambda calculus]]

&mdash; <https://en.wikipedia.org/wiki/B,_C,_K,_W_system>

## Y Combinator

_allows for [[lambda calculus#recursion]]_

_used to formally define recursive [[function]]s in a [[functional programming]] language that does not support [[recursion]]_

**definition**

_in [[lambda calculus]]_ $Y = \lambda f.\ (\lambda x.\ f\ (x\ x)) (\lambda x.\ f\ (x\ x))$

_in my [[math notation]]_ $Y = f \rightarrow (x \rightarrow f\ (x\ x))\ (x \rightarrow f\ (x\ x))$

> "it's not recursive but it encodes [[recursion]]" &mdash; <https://youtu.be/9T8A89jgeTI?t=678>

&mdash; <https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator>

## B Combinator

_the [[composition]] of its arguments_

> **aka** `(.)` in Haskell, "bluebird"

**definition**

_in [[lambda calculus]]_ $B = \lambda fgx.\ f\ (g\ x)$

_in my [[math notation]]_ $B = f\ g\ x \rightarrow f\ (g\ x)$

&mdash; <https://youtu.be/SmXB2K_5lcA?t=612>

## C Combinator

_swaps the arguments to a function_

**definition**

_in my [[math notation]]_ $C = f\ x\ y \rightarrow f\ y\ x$

## K Combinator

_discards the second argument_

**definition**

_in my [[math notation]]_ $K = f\ x\ y \rightarrow f\ x$

## W Combinator

_duplicates the second argument_

> **aka** 'commute' or 'self' in APL

**definition**

_in my [[math notation]]_ $W = f\ x\ \rightarrow f\ x\ x$
