# Programming Language

**see** [[statement]], [[expression]], [[null]], [[type system]], [[comment]]

**see** [[lexer]], [[parser]], [[syntax]]

**see** [[javascript]], [[c++]], [[python]], [[rust]], [[c]], [[iota language]], [[java]], [[go]], [[forth]], [[brainfuck]], [[apl]]

**see** _other types of languages_ [[json]], [[yaml]], [[markdown]], [[better markdown]], [[bash]]

> **resource** _Definitional Interpreters for Higher-Order Programming Languages_ (Reynolds, 1972) --- [[../references/800194.805852.pdf]] --- <https://dl.acm.org/doi/10.1145/800194.805852>
>
> - how to eliminate higher-order functions in a program (defunctionalization and closure conversion)
> - coined the term _meta-circular interpreter_. SICP's definition is different (as in, wrong?)
> - intuition for why [[continuation#continuation-passing style]] gives order-of-application independence
> - how to implement [[continuation]]s via `call/cc`, called `escape` in the paper

> **resource** _Implementing lazy functional languages on stock hardware: the Spineless Tagless G-machine_ (Peyton Jones, 1992) --- [[../references/spineless-tagless-gmachine.pdf]] --- <https://www.microsoft.com/en-us/research/wp-content/uploads/1992/04/spineless-tagless-gmachine.pdf>. covers lambda lifting. you can skim over $5 'Operational semantics of the STG language' at first, it'll make more sense when reading through $9 'Compiling the STG language to C'. same with Figure 5, the compilation example, it'll only make sense after reading through $9.
