# Programming Language

**see** [[statement]], [[expression]], [[null]], [[lexer]], [[parser]], [[type]], [[comment]]

**see** [[javascript]], [[c++]], [[python]], [[rust]], [[c]], [[iota language]], [[java]], [[go]], [[solidity]], [[forth]]

**see** _other types of languages_ [[json]], [[yaml]], [[markdown]], [[better markdown]], [[bash]]

## building a language

**see** [[backus-naur form]], [[syntax tree]], [[lexer]], [[parser]]

**representation**

```mermaid
graph TD
  src(**Source Code**<br />`print 5`)
  tok(**Tokens**<br />`ID: print, NUMBER: 5`)
  ast(**Syntax Tree**<br />`CALL: NAME: print, ARGS: 5`)
  out(**Output**<br />`5`)

  src --**Tokenizer**<br />_Lexical Analysis_--> tok --**Parser**<br />_Syntactic Analysis_--> ast --**Interpreter** or<br />**Code Generator**<br />_Semantic Analysis_--> out
```
