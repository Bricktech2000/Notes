# Programming Language

**see** [[statement]], [[expression]], [[null]], [[lexer]], [[parser]], [[type]]

**see** [[javascript]], [[c++]], [[python]], [[rust]], [[c]], [[iota language]], [[java]], [[go]], [[solidity]]

**see** _other types of languages_ [[json]], [[yaml]], [[markdown]], [[better markdown]], [[bash]]

## building a language

**see** [[backus-naur form]], [[abstract syntax tree]], [[lexer]], [[parser]]

**representation**

```mermaid
graph TD
  A(**Source Code**<br />`print 5`)
  B(**Tokens**<br />`ID: print, NUMBER: 5`)
  C(**Abstract Syntax Tree**<br />`CALL: NAME: print, ARGS: 5`)
  D(**Output**<br />`5`)

  A -- **Tokenizer**<br />_Lexical Analysis_ --> B -- **Parser**<br />_Syntactic Analysis_ --> C -- **Interpreter** or<br />**Code Generator**<br />_Semantic Analysis_ --> D
```
