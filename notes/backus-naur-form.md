# Backus-Naur form

_a notation to describe the syntax and grammar of a [[programming-language]]_

_extended Backus-Naur form_

&mdash; <https://youtu.be/4m7ubrdbWQU?t=365>

## example

```ebnf
Program
  : StatementList
  ;

Statement
  : BlockStatement
  | IfStatement
  | FunctionDeclaration
  ;

FunctionDecleration
  : def Identifier ( Arguments ) BlockStatement
  ;
```
