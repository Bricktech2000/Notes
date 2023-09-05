# Parser

_used to build a [[programming language]]_

## Recursive Descent Parser

_starts from the top symbol and builds an [[abstract syntax tree]] through [[recursion]]_

## Combinator

_a [[function#higher-order function]]s that combines [[parser]]s_

> **example**
>
> ```haskell
> type Error = String
> type Parser a = String -> Either Error (a, String)
>
> -- a parser that matches a single character
> char :: Char -> Parser Char
> char c (x:xs) | c == x = Right (c, xs)
> char c _ = Left "no match"
>
> -- ...
>
> -- `many` is a parser combinator
> whitespaces :: Parser String
> whitespaces = many (char ' ')
> ```
