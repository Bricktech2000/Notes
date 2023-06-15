# Iota Language

&mdash; <https://en.wikipedia.org/wiki/Iota_and_Jot#Iota>

**see** [[math notation]], [[combinatory logic]]

the [[iota language]] is a minimalist [[programming language]] based on the [[combinatory logic#iota combinator]]. it is designed to be even simpler than other more popular alternatives, such as [[lambda calculus]] and **`S, K, I`** [[combinatory logic]]

## Syntax

**see** [[backus-naur form]]

```bnf
<iota> ::= "1"                 ; iota combinator
         | "0" <iota> <iota>   ; application
```

> **example**
>
> `0011011` denodes **`((ii ii) (ii ii))`**
>
> **representation** _as a [[tree#binary tree]]_
>
> ```mermaid
> graph TD
>   A(**`1`**)
>   B(**`1`**)
>   C(**`1`**)
>   D(**`1`**)
>   E(**`0`**)
>   F(**`0`**)
>   G(**`0`**)
>   E --> F
>   E --> G
>   F --> A
>   F --> B
>   G --> C
>   G --> D
> ```

> **example**
>
> `0101011` denodes **`(ii (ii (ii ii)))`**
>
> **representation** _as a [[tree#binary tree]]_
>
> ```mermaid
> graph TD
>   A(**`1`**)
>   B(**`1`**)
>   C(**`1`**)
>   D(**`1`**)
>   E(**`0`**)
>   F(**`0`**)
>   G(**`0`**)
>   E --> A
>   E --> F
>   F --> B
>   F --> G
>   G --> C
>   G --> D
> ```
