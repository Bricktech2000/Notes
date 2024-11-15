# Currying

**see** [[function]], [[functional programming]]

**definition** _currying_ is the process of transforming a [[function]] that takes multiple arguments into a set of nested [[function]]s that each take a single argument --- GitHub Copilot

**examples**

with [[type#product type]]s in [[conventional math notation]], we define [[function]]s with $f(x , y) = x + 2y$ and call them with $f(x, y)$

with [[currying]] in [[conventional math notation]], we define [[function]]s with $f = x \mapsto y \mapsto x + 2y$ and call them with $f(x)(y)$

**tradeoffs**

[[currying]] allows for extending [[functional programming]] patterns, which generally work on **`1`**-ary [[function]]s, to work on **`n`**-ary [[function]]s

from [[currying]] one may [[discover]] and not [[invent]] [[partial application]]
