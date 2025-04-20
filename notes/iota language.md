# Iota Language

--- <https://en.wikipedia.org/wiki/Iota_and_Jot#Iota>

**see** [[combinatory logic]]

the [[iota language]] is a minimalist [[programming language]] based on the [[combinator#iota combinator]]. it is designed to be even simpler than other more popular alternatives, such as the [[lambda-calculus]] and SKI [[combinatory logic]]

## Syntax

**see** [[backus--naur form]]

```bnf
<iota> ::= "1"                 ; iota combinator
         | "0" <iota> <iota>   ; application
```

> **example**
>
> `0011011` denodes $((\iota\ \iota)\ (\iota\ \iota))$
>
> **representation** _as a [[tree#binary tree]]_
>
> ```mermaid
> graph TD
>   A($$1$$)
>   B($$1$$)
>   C($$1$$)
>   D($$1$$)
>   E($$0$$)
>   F($$0$$)
>   G($$0$$)
>   E --> F --> A & B
>   E --> G --> C & D
> ```

> **example**
>
> `0101011` denodes $(\iota\ (\iota\ (\iota\ \iota)))$
>
> **representation** _as a [[tree#binary tree]]_
>
> ```mermaid
> graph TD
>   A($$1$$)
>   B($$1$$)
>   C($$1$$)
>   D($$1$$)
>   E($$0$$)
>   F($$0$$)
>   G($$0$$)
>   E --> A
>   E --> F --> B
>         F --> G --> C & D
> ```
