# Lambda Calculus

**aka** _$\lambda$-calculus_

**see** [[combinatory logic]], [[recursion]]

&mdash; <https://youtu.be/eis11j_iGMs>

used for backlinks

**properties**

[[lambda calculus]] and [[turing machine]]s are equivalent

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

#todo **equivacence** with [[boolean algebra]]

[[boolean]] values and [[boolean algebra#operators]] can be defined as follows:

$\text{true} = x\ y \rightarrow x$

$\text{false} = x\ y \rightarrow y$

&mdash; <https://youtu.be/eis11j_iGMs?t=413>

$\text{not} = p \rightarrow p\ \text{false}\ \text{true}$

$\text{and} = p\ q \rightarrow p\ q\ p$

$\text{or} = p\ q\ \rightarrow q\ p\ q$

&mdash; <https://youtu.be/eis11j_iGMs?t=484>

&mdash; <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

## Iteration

[[iteration]] is defined as $(x \rightarrow x\ x)\ (x \rightarrow x\ x)$ in my [[math notation]] or as $(\lambda x.\ x\ x) (\lambda x.\ x\ x)$ in [[conventional math notation]]. evaluating this [[function]] call once yields itself. this definition is equivalent to $\operatorname{rec}\ (x \rightarrow x)$ in my [[math notation]] or to $\operatorname{rec} \lambda x.\ x$ in [[conventional math notation]], see [[recursion#general recursion]] &mdash; <https://youtu.be/9T8A89jgeTI?t=544>

## Recursion

general [[recursion]] in [[lambda calculus]] can be defined using the [[combinatory logic#y combinator]]

$\operatorname{rec} f =\!= Y\ f$

&mdash; <https://youtu.be/9T8A89jgeTI?t=627>

## array representation

all [[lambda calculus]] expressions can be represented as one-dimensional [[array]]s using the following [[backus-naur form]] syntax &mdash; me:

```bnf
<expr> ::= <index>                                   ; De Bruijn index
         | "λ"* "(" (<expr> | "id") " " <expr> ")"   ; (abstraction of)* application
```

> **example**
>
> in my [[math notation]]: $z \rightarrow (y \rightarrow y\ (x \rightarrow x))\ (x \rightarrow z\ x)$
>
> using De Bruijn indices: $\lambda\ (\lambda\ 0\ (\lambda\ 0))\ (\lambda\ 1\ 0)$
>
> as a [[tree#binary tree]]:
>
> ```mermaid
> graph TD;
>   node8(0)
>   node5(λ A)
>   node6(0)
>   node7(λ A)
>   node1(λ A)
>   node2(1)
>   node3(0)
>   node9(λ A)
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
> in my [[math notation]]: $s\ z \rightarrow s\ (s\ (s\ z))$
>
> using De Bruijn indices: $\lambda\ (\lambda\ (1\ (1\ (1\ 0))))$
>
> as a [[tree#binary tree]]:
>
> ```mermaid
> graph TD;
>   node1(λ λ A)
>   node2(1)
>   node3(A)
>   node4(1)
>   node5(A)
>   node6(1)
>   node7(0)
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
