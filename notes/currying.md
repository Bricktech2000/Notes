# Currying

**see** [[function]], [[functional programming]]

**definition** _Currying_ is the process of transforming a [[function]] that takes multiple arguments into a set of nested [[function]]s that each take a single argument. &mdash; Github Copilot

**examples**

in [[conventional math notation]], we define [[function]]s as $f(x , y) = x + 2y$ and call them using $f(x, y)$

with [[currying]] in [[conventional math notation]], we define [[function]]s as $f = x \to y \to x + 2y$ and call them using $f(x)(y)$

in my [[math notation]], [[function]]s can optionally be defined using [[currying]]

**applications**

[[currying]] allows for extending [[functional programming]] patterns, which generally work on [[function]]s with only one input, to work on [[function]]s with multiple inputs.

[[currying]] allows for [[parital application]]
