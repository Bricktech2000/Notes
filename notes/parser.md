# Parser

#stub

## Parser Combinator

> **resource** JSON parser in Haskell leveraging [[parser#parser combinator]]s, [[functor]]s, [[applicative]]s and [[monad]]s, by Tsoding --- <https://youtu.be/N9RUqGYuGfw>

> **resource** the [[parser#parser combinator]] library contained in the PNLC prelude --- <https://github.com/Bricktech2000/PNLC/blob/master/prelude.pnlc>

_[[parser#parser combinator]]s are a way to program a recursive descent parser_ --- Chandler Carruth --- <https://youtu.be/ZI198eFghJk?t=6m25s>

> **example**
>
> ```haskell
> type Parser a = String -> Maybe (a, String)
>
> -- a parser that parses a single character
> char :: Char -> Parser Char
> char c (x:xs) | c == x = Just (c, xs)
> char c _ = Nothing
>
> -- `many` is a parser combinator
> whitespaces :: Parser String
> whitespaces = many (char ' ')
> ```
