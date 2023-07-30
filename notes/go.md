# Go

_it's not bad; it's just not good_

&mdash; <https://yager.io/programming/go.html>

[[go]] contains a myriad of contradictory design decisions, including:

- it calls itself a _systems language_ yet requires a garbage collector
- it has the imperativity of [[c]] but the built-in dynamic [[array]]s of [[python]]
- it proudly uses [[ordered pair]]s over special syntax for error handling, but using [[type#product type]]s for error handling is a half-baked solution anyway
- it is a modern language designed from the ground up yet still uses [[null]]s for failure conditions and has [[c]]-style valueless statements for control flow
- it is a statically typed language yet has a [[type#top type]] in the form of the _empty [[interface]]_, which completely defeats the purpose of [[type system]]s

most of this can be explained by the fact that [[go]] is the result of _language design in the service of [[software engineering]]_:

- _Go's purpose is therefore not to do research into programming language design; it is to improve the working environment for its designers and their coworkers. Go is more about software engineering than programming language research. Or to rephrase, it is about language design in the service of software engineering._ &mdash; Rob Pike &mdash; <https://go.dev/talks/2012/splash.article>
- _The key point here is our programmers are Googlers, they’re not researchers. They’re typically, fairly young, fresh out of school, probably learned Java, maybe learned C or C++, probably learned Python. They’re not capable of understanding a brilliant language but we want to use them to build good software. So, the language that we give them has to be easy for them to understand and easy to adopt._ &mdash; Rob Pike &mdash; <https://news.ycombinator.com/item?id=16143918>
- _It must be familiar, roughly C-like. Programmers working at Google are early in their careers and are most familiar with procedural languages, particularly from the C family. The need to get programmers productive quickly in a new language means that the language cannot be too radical._ &mdash; Rob Pike &mdash; <https://go.dev/talks/2012/splash.article>
