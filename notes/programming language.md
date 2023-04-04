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
  A(<strong>Source Code</strong><br /><code>print 5</code>)
  B(<strong>Tokens</strong><br /><code>ID: print, NUMBER: 5</code>)
  C(<strong>Abstract Syntax Tree</strong><br /><code>CALL: NAME: print, ARGS: 5</code>)
  D(<strong>Output</strong><br /><code>5</code>)

  A -- <strong>Tokenizer</strong><br /><em>Lexical Analysis</em> --> B -- <strong>Parser</strong><br /><em>Syntactic Analysis</em> --> C -- <strong>Interpreter</strong> or<br /><strong>Code Generator</strong><br /><em>Semantic Analysis</em> --> D
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
