# Programming Language

used for backlinks

**see**

[[statement]]

[[expression]]

[[null]]

[[parser]]

[[type]]

## building a language

**see** [[backus-naur form]], [[abstract syntax tree]], [[parser]]

**representation**

```mermaid
graph TD
  A(**Source Code**<br />`print 5`)
  B(**Tokens**<br />`ID: print, NUMBER: 5`)
  C(**Abstract Syntax Tree**<br />`CALL: NAME: print, ARGS: 5`)
  D(**Output**<br />`5`)

  A -- **Tokenizer**<br />_Lexical Analysis_ --> B -- **Parser**<br />_Syntactic Analysis_ --> C -- **Interpreter** or<br />**Code Generator**<br />_Semantic Analysis_ --> D
```

**examples** _languages in the rough order I learned them_

1. Visual Basic Script (and Batch)
2. [[javascript]] (and HTML and CSS)
3. [[c++]]
4. [[python]]
5. [[rust]]
6. [[java]] (forced in university)
7. [[solidity]] (familiar)
8. [[c]]

[[esoteric programming language idea]]

[[the worst programming language ever]]

[[markup language idea]]

[[iota language]]

**examples** _other types of languages_

[[json]]

[[yaml]]

[[markdown]]
