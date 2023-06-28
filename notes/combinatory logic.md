# Combinatory Logic

**see** [[lambda calculus]], [[math notation]], [[combinator]]

**properties**

the [[combinator#s combinator]] and the [[combinator#k combinator]] can be composed to produce [[combinator]]s that are extentionally equal to any [[lambda calculus]] term. consequently, **`S, K`** [[combinatory logic]] is Turing complete, see [[turing machine]]

#todo this is an applicative ([[apply]]?) in [[category theory]] &mdash; <https://youtu.be/Y0KKPYkeOTA?t=501>

## Booleans

> **equivalence** _[[combinatory logic#booleans]] and [[boolean algebra]]_

[[boolean]] values and [[boolean algebra#operators]] can be defined as follows, see [[lambda calculus]]:

- **`"true" = x y -> x = K`**
- **`"false" = x y -> y = K I`**

we can then define:

- **`"not" = p -> p "false" "true" = C (T "false") "true"`**

## Pairs

> **equivalence** _[[combinatory logic#pairs]] and [[ordered pair]]_

[[ordered pair]]s can be defined as follows:

- **`"pair" = x y z -> z x y = B C T`**
- **`"fst" = p -> p "true" = T "true"`**
- **`"snd" = p -> p "false" = T "false"`**

## Naturals

> **equivalence** _[[combinatory logic#naturals]] and [[natural]] number_

[[natural]] numbers can be defined as follows, see [[lambda calculus]]:

- **`0 = "pair" "true" "false"`** (equivalent to **`I`**)
- **`"succ" = n -> "pair" "false" n = "pair" "false"`**

we can then define:

- **`"pred" = n -> "snd" n = "snd"`**
- **`"iszero" = n -> "fst" n = "fst"`**

## &mdash;

&mdash; <https://youtu.be/gnrSedVucXs>
