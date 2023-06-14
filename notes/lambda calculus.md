# Lambda Calculus

**aka** _&lambda;-calculus_

**see** [[combinatory logic]], [[recursion]]

&mdash; <https://youtu.be/eis11j_iGMs>

used for backlinks

**properties**

[[function]]s in [[lambda calculus]] are [[function#pure function]]s

[[lambda calculus]] is Turing complete, see [[turing machine]]

[[lambda calculus]] is the basis for most [[functional programming]] languages

## Syntax

**see** [[backus-naur form]]

&mdash; <https://youtu.be/IOiZatlZtGU?t=292>

&mdash; <https://opendsa-server.cs.vt.edu/OpenDSA/Books/PL/html/Syntax.html>

**definition**

_in [[conventional math notation]]_

```bnf
<expr> ::= <var>                       ; variable
         | "λ" <var> "." <expr>        ; abstraction
         | "(" <expr> " " <expr> ")"   ; application
```

_in my [[math notation]]_

```bnf
<expr> ::= <var>               ; variable
         | <var> "->" <expr>   ; abstraction
         | <expr> " " <expr>   ; application
         | "(" <expr> ")"      ; grouping
```

## Church Booleans

> **equivalence** _[[lambda calculus#church booleans]] and [[boolean algebra]]_

[[boolean]] values and [[boolean algebra#operators]] can be defined as follows:

- **`"true" = x y -> x`**
- **`"false" = x y -> y`**

&mdash; <https://youtu.be/eis11j_iGMs?t=413>

we can then define:

- **`"not" = p -> p "false" "true"`**
- **`"and" = p q -> p q p`**
- **`"or" = p q -> q p q`**

&mdash; <https://youtu.be/eis11j_iGMs?t=484>

&mdash; <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

## Pairs

> **equivalence** _[[lambda calculus#pairs]] and [[ordered pair]]_

[[ordered pair]]s can be defined as follows:

- **`"pair" = x y z -> z x y`**
- **`"fst" = p -> p "true"`**
- **`"snd" = p -> p "false"`**

## Church Encoding

> **equivalence** _[[lambda calculus#church encoding]] and [[natural]] numbers_

[[natural]] numbers can be defined as follows:

- **`0 = f x -> x`**
- **`"succ" = n f x -> f (n f x)`**

we can then define:

- **`"iszero" = n -> n (-> "false") "true"`**

## Iteration

[[iteration]] is defined as **`(x -> x x) (x -> x x)`** in my [[math notation]] or as $(\lambda x.\ x\ x) (\lambda x.\ x\ x)$ in [[conventional math notation]]. evaluating this [[function]] call once yields itself. this definition is equivalent to **`"rec" {*}`** in my [[math notation]] or to $\operatorname{rec} \lambda x.\ x$ in [[conventional math notation]], see [[recursion#general recursion]] &mdash; <https://youtu.be/9T8A89jgeTI?t=544>

## Recursion

general [[recursion]] in [[lambda calculus]] can be defined using the [[combinatory logic#y combinator]]

**`"rec" f == Y f`**

&mdash; <https://youtu.be/9T8A89jgeTI?t=627>

## array representation

all [[lambda calculus]] expressions can be represented as one-dimensional [[array]]s using the following [[backus-naur form]] syntax &mdash; me:

```bnf
<expr> ::= <index>                                   ; De Bruijn index
         | "λ"* "(" (<expr> | "id") " " <expr> ")"   ; (abstraction of)* application
```

> **example**
>
> in my [[math notation]]: **`z -> (y -> y (x -> x)) (x -> z x)`**
>
> using De Bruijn indices: **`ll (ll 0 (ll 0)) (ll 1 0)`**
>
> as a [[tree#binary tree]]:
>
> ```mermaid
> graph TD
>   node8(**`0`**)
>   node5(**`ll A`**)
>   node6(**`0`**)
>   node7(**`ll A`**)
>   node1(**`ll A`**)
>   node2(**`1`**)
>   node3(**`0`**)
>   node9(**`ll A`**)
>
>   node1 --> node3
>   node1 --> node2
>
>   node5 --> node6
>
>   node7 --> node8
>   node7 --> node5
>
>   node9 --> node7
>   node9 --> node1
> ```
>
> as an [[array]]: `0x01010100010100XXXXXX00XXXXXXXX`

> **example**
>
> in my [[math notation]]: **`s z -> s (s (s z))`**
>
> using De Bruijn indices: **`ll (ll (1 (1 (1 0))))`**
>
> as a [[tree#binary tree]]:
>
> ```mermaid
> graph TD
>   node1(**`ll ll A`**)
>   node2(**`1`**)
>   node3(**`A`**)
>   node4(**`1`**)
>   node5(**`A`**)
>   node6(**`1`**)
>   node7(**`0`**)
>
>   node1 --> node2
>   node1 --> node3
>
>   node3 --> node4
>   node3 --> node5
>
>   node5 --> node6
>   node5 --> node7
> ```
>
> as an [[array]]: `0x020100XXXX0100XXXXXXXXXXXX0100`
