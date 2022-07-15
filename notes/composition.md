# Composition

see [[math-notation]], [[function]]

## definition

in my [[math-notation]]: $C\ f\ g = x \rarr f\ g\ x$, where

$f$ and $g$ are the original [[function]]s

$C$ is the [[composition]] [[function]]

$x$ is the parameter to be passed to $f$ and $g$

in Haskell, let `f :: A -> B` and `g :: B -> C`. then, `g . f` has type signature `A -> C`, see [[composition]]

in Haskell, `(.) :: (b -> c) -> (a -> b) -> a -> c`

## properties

let $\circ$ be the [[composition]] [[operator]]. then,

$h \circ (g \circ f) \equiv (h \circ g) \circ f \equiv h \circ g \circ f$ &mdash; associative

&mdash; <https://youtu.be/SmXB2K_5lcA?t=662>

## applications

[[function]] [[composition]] is very useful in [[functional-programming]] as it allows for building larger [[function]]s from smaller ones. it also allows for [[abstraction]] and [[encapsulation]].

### example

suppose we have two [[function]]s: $A \to B$ and $B \to C$. after composing them, we get $A \to C$. there is no way to differentiate this [[function]] from any other [[function]], and the intermediate value $B$ is not exposed to the outside world anymore.
