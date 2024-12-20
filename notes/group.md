# Group

## Operation

## Identity Element

## Inverse Element

**see** [[math notation]], [[algebraic structure]]

--- <https://youtu.be/KufsL2VgELo>

--- <https://youtu.be/mvmuCPvRoWQ>

_a [[monoid]] where every element also has an inverse_

**definition** a [[group]] is a finite or infinite [[set]] of invertible elements equipped with a closed associative binary operation and an identity element --- Wikipedia and me

**definition**

let a binary [[operator]] **`{:}`** on a [[set]] **`G`**. for them to form a [[group]], the following [[axiom]]s must be satisfied for all **`G {a /\ b /\ c}`**:

_associativity_ **`(a : b) : c = a : (b : c) > G {a /\ b /\ c}`**

_identity element_ **`a : O = a /\ G O > G a`**

_closure_ **`G (a : b) > G {a /\ b}`**

_inverse element_ **`a : .a = O > G a`**

**notation**

_in my [[math notation]]_

the _inverse_ of **`a`** is denoted **`.a`**

the _identity_ element is denoted **`O`**

**`a : a`** is denoted **`2a`**

_in [[conventional math notation]]_

the _inverse_ of **`a`** is denoted $a^{-1}$

the _identity_ element is denoted $e$

**`a * a`** is denoted $a^2$

**properties** _follow from the [[axiom]]s_

a [[group]] contains exactly one identity element

every element of a [[group]] has exactly one inverse

> **note** consequently, **`.a : .a`** is identical to **`.(2a)`** which is identical to **`2(.a)`**, all of which can be denoted **`.2a`**. this is true for any coefficient

**`a : O = a > G a`** implies **`O : a = a > G a`**

**`a : .a = O > G a`** implies **`.a : a = O > G a`**

**`..a = a`**

**examples**

> **example** the following mathematical objects and binary [[operator]]s are examples of [[group]]s:
>
> - [[integer]]s and addition
> - [[rational]]s excluding **`0`** and multiplication
> - [[integer]]s modulo **`n`** and addition
> - invertible square [[matrix]]es and [[matrix#multiplication]]

## Order

**definition** the _order_ of a [[group]] **`G`** is the number of elements in the [[group]]

**notation** _in my [[math notation]]_ **`# G`**

## Subgroup

**theorem** _Lagrange's Theorem_ let **`G`** be a [[group]] and **`H`** be a [[group#subgroup]] of **`G`**. then, **`# H`** divides **`# G`**

**theorem** _Cauchy's Theorem_ if **`G`** is a finite [[group]] and **`p`** is a [[prime]] that divides **`# G`** then **`G`** has a [[group#subgroup]] **`H`** with **`# H = p`**

## Homomorphism

**see** [[morphism#homomorphism]]

**definition** a _group homomorphism_ from a [[group]] **`G`** to a [[group]] **`H`** is a [[function]] **`f`** such that **`f (a : b) = f a : f b > G {a /\ b}`**

## Trivial Group

**definition** the _trivial group_ is a [[group]] with exactly one element, the [[group#identity element]]
