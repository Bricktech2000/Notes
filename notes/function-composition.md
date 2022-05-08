# Function Composition

## notation

in my [[math-notation]]: $C\ x = f\ g\ x$, where

$f$ and $g$ are the original functions

$C$ is the resulting function

$x$ is the parameter to be passed to $f$ and $g$

## applications

[[function-composition]] is very useful in [[functional-programming]] as it allows for building larger [[function]]s from smaller ones. it also allows for [[abstraction]]

## example

suppose we have two functions: $A \to B$ and $B \to C$. after composing them, we get $A \to C$. there is no way to differentiate this function from any other function, and the intermediate value $B$ is not exposed to the outside world anymore.
