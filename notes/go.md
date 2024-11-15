# Go

_it's not bad; it's just not good_ --- <https://yager.io/programming/go.html>

> **resource** _[[go]] at Google: Language Design in the Service of [[software engineering]]_ --- <https://go.dev/talks/2012/splash.article>

> **resource** _why [[go]] is not good_, comparing design decisions in [[go]] to Haskell and [[rust]] --- <https://yager.io/programming/go.html>

[[go]] contains a myriad of contradictory design decisions; examples include:

- [[go]] calls itself a _systems language_ yet requires a garbage collector
- [[go]] has the imperativity and verbosity of [[c]] but the built-in dynamic [[array]]s of [[python]]
- [[go]] is a modern language designed from the ground up yet still uses [[null]]s for failure conditions and [[c]]-style valueless statements for control flow
- [[go]] is a statically typed language yet has a [[type#top type]] in the form of the _empty [[interface]]_, which completely defeats the purpose of [[type system]]s

most of this can be explained by the fact that [[go]] is the result of _language design in the service of [[software engineering]]_:

- _Go's purpose is therefore not to do research into programming language design; it is to improve the working environment for its designers and their coworkers. Go is more about software engineering than programming language research. Or to rephrase, it is about language design in the service of software engineering._ --- Rob Pike --- <https://go.dev/talks/2012/splash.article>
- _The key point here is our programmers are Googlers, they're not researchers. They're typically fairly young, fresh out of school, probably learned Java, maybe learned C or C++, probably learned Python. They're not capable of understanding a brilliant language but we want to use them to build good software. So, the language that we give them has to be easy for them to understand and easy to adopt._ --- Rob Pike --- <https://news.ycombinator.com/item?id=16143918>
- _It must be familiar, roughly C-like. Programmers working at Google are early in their careers and are most familiar with procedural languages, particularly from the C family. The need to get programmers productive quickly in a new language means that the language cannot be too radical._ --- Rob Pike --- <https://go.dev/talks/2012/splash.article>

a large portion of the [[go]] language was [[invent]]ed rather than [[discover]]ed; examples include:

- `append`, `clear`, `delete`, `min`, `max`, and `new` are all [[go]] built-ins --- <https://go.dev/ref/spec#Built-in_functions>
- `range` and `map` are hard-coded into the [[go]] syntax --- <https://go.dev/ref/spec#For_range> and <https://go.dev/ref/spec#Map_types>
- [[function]]s returning multiple values is a hard-coded feature; tuples don't exist in [[go]] --- <https://go.dev/ref/spec#Return_statements>
- `range` and `make` are hard-coded [[go]] built-ins. they only work on primitives and cannot be extended --- <https://yager.io/programming/go.html>

and the rest of [[go]] is half-baked at best; examples include:

- [[go]] uses "zero values" to avoid uninitialized variables, which is a band-aid solution to a problem that should be solved at the [[type system]] level
- [[go]] has [[interface]]s, which are a poor man's [[trait]]s. and [[go]] [[interface]]s are duck-typed, which is another shady decision
- [[go]] dares to list [[type]] inference as a feature, but all its [[type]] inference engine does is guess the [[type]] of a [[variable]] based on the value it's assigned
- [[go]] proudly uses [[ordered pair]]s over special syntax for error handling, except that using [[type#product type]]s for error handling is a half-baked solution anyway

for the sake of [[confirmation bias]], let's end with a few cherry-picked quotes:

- _the [[go]] way is to half-ass things. the [[go]] way is to patch things up until they sorta kinda work, in the name of simplicity_ --- <https://fasterthanli.me/articles/i-want-off-mr-golangs-wild-ride>
- _[...] it becomes extremely hard to follow what any program is doing at a high level, because everywhere you look, you get bogged down in imperative code doing trivial data manipulation or error propagation_ --- <https://fasterthanli.me/articles/lies-we-tell-ourselves-to-keep-using-golang>
- _the closest thing to a flexible iterator keyword is building a wrapper around your data structure that returns a `chan` and then iterate over the `chan`, but that is slow, complicated, and bug-prone_ --- <https://yager.io/programming/go.html>
