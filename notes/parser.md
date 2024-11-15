# Parser

_used to build a [[programming language]]_

## Recursive Descent Parser

recursive descent parsers start from the top symbol and build a [[syntax tree]] through [[recursion]]

### Combinator

_a higher-order [[function]] that combines [[parser]]s_

> **resource** JSON parser in Haskell leveraging [[parser#combinator]]s by Tsoding --- <https://youtu.be/N9RUqGYuGfw>

_[[parser#combinator]]s are a way to program a [[parser#recursive descent parser]]_ --- <https://youtu.be/ZI198eFghJk?t=6m25s>

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
> -- `many` is a parser combinator
> whitespaces :: Parser String
> whitespaces = many (char ' ')
> ```
