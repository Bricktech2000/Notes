# Euclidean Vector

**aka** _geometric vector_, _spatial vector_, _vector_

**equiv** _[[list]] of [[number]]s_

**see** [[math notation]], [[math notation]], [[vector]]

**definition** _formally in my [[math notation]]_ a [[vector]] is a [[set theory]]etical [[function]] that takes a [[natural]] index and returns the element at that index

**notation** _in my [[math notation]]_ **`(1, 2)`**

## Vector Space

**see** [[vector]], [[vector space]]

**properties**

_zero [[euclidean vector]]_ **`O`** such that **`/\ O * = 0`**

_[[euclidean vector]] addition_ **`(a, b) : (c, d) == (a : c, b : d)`**

_multiplication by a [[scalar]]_ **`c(a, b) == (ca, cb) > RR c`**

## Magnitude

**see** [[dot product]]

**definition** **`\:V2/`**

### Unit Vector

**definition**

a _unit vector_ is a [[euclidean vector]] **`V`** such that **`"abs" V = 1`**

a [[euclidean vector]] can be _normalized_ (scaled into into a [[euclidean vector#unit vector]]) through **`{*--"abs"+`** #todo id

## Angle

_angle between two [[euclidean vector]]s_

**definition**

**`"cos" aa = :ab -- \:a2/ \:b2/`**, see [[dot product]] #magic

> **note** use **`"cos" aa = "abs" :ab -- \:a2/ \:b2/`** to always get the acute angle solution

**definition**

**`"sin" aa = (a "cross" b) -- \:a2/ \:b2/`**, see [[cross product]] #magic

### Orthogonal Euclidean Vectors

_a pair of vectors offset by **`-4tt"rad"`**_

**definition** **`u`** and **`v`** are _orthogonal_ if and only if **`:uv = 0`**, see [[dot product]]

**definition** a [[set]] of [[vector]]s is _orthogonal_ if and only if it does not contain the zero [[vector]] and all [[vector]]s in the [[set]] are orthogonal to all other [[vector]]s

**theorem** any orthogonal [[set]] of [[vector]]s in **`RR^n`** contains at most **`n`** [[vector]]s

**theorem** any orthogonal [[set]] of **`n`** [[vector]]s in **`RR^n`** is a [[basis#orthogonal basis]] of **`RR^n`**

**theorem** a [[set]] of [[vector]]s being orthogonal implies they are [[vector#linearly independent vector]]s, but not conversely

**theorem** suppose **`w`** is a [[basis#orthogonal basis]] for a [[vector space#subspace]] **`W`** of **`RR^n`**. then, **`w = :i. w i | (:w(w i) -- :(w i)2)`**, see [[dot product]]

### Colinear Euclidean Vectors

_a pair of parallel vectors_

**definition** **`u`** and **`v`** are _colinear_ if and only if **`:uv = "abs" {uv}**, see [[dot product]]

**definition** **`u`** and **`v`** are _colinear_ if and only if there exsits a [[scalar]] **`k`** such that **`u = kv`**

**properties**

**`u`** and **`v`** are colinear if **`u`** is a [[linear combination]] of the [[set]] **`{{v}}`**

## Projection

_the scalar projection is equal to the [[euclidean vector#magnitude]] of the [[euclidean vector#projection]]_ --- Wikipedia

**see** [[dot product]]

[[euclidean vector#projection]]s are [[linear map]]s, and therefore can be turned into [[matrix#multiplication]]

**definition** _projection onto another [[vector]]_

**`"abs" ("proj"^b a) = "abs" a | "cos" aa = :ab_*`**, and

**`"proj"^b a = "abs" a | "cos" aa | b_* = :ab_* | b_* = :ab -- :b2 | b`** (see [[dot product]]), where

- **`"proj"^b a`** is the _vector projection of **`a`** on **`b`**_
- **`"abs" ("proj"^b a)`** is the _scalar projection of **`a`** on **`b`**_
- **`b_*`** is the [[euclidean vector#unit vector]] in the direction of **`b`**, **`{*--"abs"} b`**

**definition** _projection onto a [[vector space]]_

**`"proj"^W v = :i. (:v(w i) -- :(w i)2)`**, where

- **`"proj"^W v`** is the projection of **`v`** on the [[vector space]] **`W`**
- **`W = "span" {{w_0 ... w_n}}`** and **`(w_0 ... w_n)`** is a [[basis#orthogonal basis]] for **`W`**

**properties**

**`"proj"^b a`** is parallel to **`b`**

**`a .. "proj"^b a`** is orthogonal to **`b`**

**`W ("proj"^W v)`**

**`v .. "proj"^W v`** is orthogonal to every [[vector]] in **`W`**

the [[vector]] **`"proj"^W v`** is the only [[vector]] in **`RR^n`** that satisfies the two properties above

**`"proj"^W v`** is the "best approximation" to **`v`** by [[vector]]s in **`W`**
