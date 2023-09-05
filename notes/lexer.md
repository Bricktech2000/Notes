# Lexer

_used to build a [[programming language]]_

> **note** I don't understand the point of [[lexer]]s. using the token as the basic unit of syntax is arbitrary; I would argue using the [[character]] is more natural. given a [[parser]] that operates on tokens, it is trivial to build a parser that operates on [[character]]s. consequently, the [[lexer]] is a strict [[set#subset]] of a [[parser]], except that it's even worse at lexical analysis than a [[parser]] is! a well-written [[parser]] that leverages [[parser#combinator]]s does everything a [[lexer]] promises, and heaps more. and it does it better, and more declaratively.
