# Vector in Rn

**equiv** _[[list]] of **`RR`**_

**see** [[math notation]], [[math notation]], [[vector]] properties

**definition** a _vector in **`RR^n`**_ is an ordered collection of elements that do not have to be unique

**definition** _formally in my [[math notation]]_ a [[vector]] is a [[set theory]]etical [[function]] that takes a [[natural]] index and returns the element at that index

**notation** _in my [[math notation]]_

**`(1, 2)`**

## Vector Space

**see** [[vector]], [[vector space]]

**properties**

_zero [[vector in rn]]_ **`O`** such that **`/\ O * = 0`**

_[[vector in rn]] addition_ **`(a, b) : (c, d) == (a : c, b : d)`**

_multiplication by a [[scalar]]_ **`c(a, b) == (ca, cb) > RR c`**

## Magnitude

**see** [[dot product]]

**definition** **`\:V2/`**

### Unit Vector

**definition**

a _unit vector_ is a [[vector in rn]] **`V`** such that **`\:V2/ = 1`**

a [[vector in rn]] can be _normalized_ (scaled into into a [[vector in rn#unit vector]]) through **`{*--\:*2/}`**

## Angle

_angle between two [[vector in rn]]s_

**definition**

**`"cos" aa = :ab -- \:a2/ \:b2/`**, see [[dot product]] #magic

> **note** use **`"cos" aa = "abs" :ab -- \:a2/ \:b2/`** to always get the acute angle solution

**definition**

**`"sin" aa = (a "cross" b) -- \:a2/ \:b2/`**, see [[cross product]] #magic

### Orthogonal Vectors

_a pair of vectors offset by **`-4tt "rad"`**_

**definition** **`u`** and **`v`** are _orthogonal_ if and only if **`:uv = 0`**, see [[dot product]]

**definition** a [[set]] of [[vector]]s is _orthogonal_ if and only if it does not contain the zero [[vector]] and all [[vector]]s in the [[set]] are orthogonal to all other [[vector]]s

**theorem** any orthogonal [[set]] of [[vector]]s in **`RR^n`** contains at most **`n`** [[vector]]s

**theorem** any orthogonal [[set]] of **`n`** [[vector]]s in **`RR^n`** is a [[basis#orthogonal basis]] of **`RR^n`**

**theorem** a [[set]] of [[vector]]s being orthogonal implies they are [[vector#linearly independent vector]]s, but not conversely

**theorem** suppose **`(w_0 ... w_m)`** is a [[basis#orthogonal basis]] for a [[vector space#subspace]] **`W`** of **`RR^n`**. then, **`w = w_0 (:w w_0 -- :w_0 w_0) : ... w_m (:w w_m -- :w_m w_m)`**, see [[dot product]]

### Colinear Vectors

_a pair of parallel vectors_

**definition** **`u`** and **`v`** are _colinear_ if and only if **`:uv = \:u2/ \:v2/`**, see [[dot product]]

**definition** **`u`** and **`v`** are _colinear_ if and only if **`u = kv`** given a [[scalar]] **`k`**

**properties**

**`u`** and **`v`** are colinear if **`u`** is a [[linear combination]] of the [[set]] **`{{v}}`**

## Projection

_The scalar projection is equal to the [[vector in rn#magnitude]] of the [[vector in rn#projection]]_ &mdash; Wikipedia

**see** [[dot product]]

[[vector in rn#projection]]s are [[linear transformation]]s, and therefore can be turned into [[matrix#multiplication]]

**definition** _projection onto another [[vector]]_

**`\:("proj"^b a)2/ = \:a2/ "cos" aa`**, and

**`"proj"^b a = \:a2/ "cos" aa | b_* = :ab_* | b_* = :ab -- :b2 | b`** (see [[dot product]]), where

- **`"proj"^b a`** is the _vector projection of **`a`** on **`b`**_
- **`\:("proj"^b a)2/`** is the _scalar projection of **`a`** on **`b`**_
- **`b_*`** is the [[vector in rn#unit vector]] in the direction of **`b`**, **`{*--||||} b`**

**definition** _projection onto a [[vector space]]_

**`"proj"^W v = (:vw_0 -- :w_0 w_0) : ... (:vw_n -- :w_n w_n)`**, where

- **`"proj"^W v`** is the projection of **`v`** on the [[vector space]] **`W`**
- **`W = "span" {{w_0 ... w_n}}`** and **`(w_0 ... w_n)`** is a [[basis#orthogonal basis]] for **`W`**

**properties**

**`"proj"^b a`** is parallel to **`b`**

**`a . "proj"^b a`** is orthogonal to **`b`**

**`W ("proj"^W v)`**

**`v . "proj"^W v`** is orthogonal to every [[vector]] in **`W`**

the [[vector]] **`"proj"^W v`** is the only [[vector]] in **`RR^n`** that satisfies the two properties above

**`"proj"^W v`** is the "best approximation" to **`v`** by [[vector]]s in **`W`**
