# Currying

see [[function]], [[functional-programming]]

> **definition**: _Currying_ is the process of transforming a function that takes multiple arguments into a function that takes a single argument. &mdash; GitHub Copilot

## example

in [[math-notation]], we define [[function]]s as $f\ x, y = x \cdot 2y$ and call them using $f/ (x, y)$

with [[currying]], we define [[function]]s as $f = x \to y \to x \cdot 2y$ and call them using $f\ x\ y$

## applications

[[currying]] allows for extending [[functional-programming]] patterns, which generally work on [[function]]s with only one input, to work on [[function]]s with multiple inputs.

[[currying]] allows for [[partial-application]]
