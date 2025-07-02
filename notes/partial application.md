# Partial Application

**see** [[functional programming]], [[currying]], [[function#application]]

**definition** _partial application_ is the action of applying only part of a [[function]]'s arguments to produce a new [[function]] that takes the remaining arguments

> **example**
>
> ```fsharp
> let hello = printfn "Hello, %s"
> let names = ["John", "Jane", "Mary"]
>
> names
> |> List.map hello
> ```
