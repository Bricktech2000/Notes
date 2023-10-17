# Vector Space

**see** [[vector]], [[vector in rn]], [[matrix]], [[math notation]], [[basis]], [[algebraic structure]]

**types**

[[vector in rn#vector space]]

[[matrix#vector space]]

[[function#vector space]]

[[polynomial#vector space]]

[[ordered pair#vector space]]

[[eigen#space]]

**examples**

> **example**
>
> the following are [[vector space]]s:
>
> - **`RR^1`**, **`RR^2`**, **`RR^n /\ NN n`**
> - **`v -> (v = O)`**
> - any [[plane#plane in r3]] through the origin is a [[vector space#subspace]] of **`RR^3`**
> - any [[line#line in r3]] through the origin is a [[vector space#subspace]] of **`RR^3`** (same with **`RR^2`**)
> - any [[line#line in r3]] or [[plane#plane in r3]] that does _not_ go through the origin is not a [[vector space#subspace]] of **`RR^3`**
> - **`/\ RR^n -| RR^n > NN n`** (**`RR^n`** is a [[vector space#subspace]] of **`RR^n`**)
> - **`/\ v -> (v = (0 ... 0)) -| RR^n > NN n`** (**`(0 ... 0)`** is a [[vector space#subspace]] of **`RR^n`**)
> - **`RR^n.x`** is not a [[vector space#subspace]] of **`RR^n`**, as [[vector]]s in **`RR^n.x`** are not really comparable to [[vector]]s in **`RR^n`**

**definition**

let a [[vector space]] **`V`** be a [[set]] of [[vector]]s. all of the following [[axiom]]s must be satisfied for all **`V {u /\ v /\ w} /\ RR {c /\ d}`** for **`V`** to be a [[vector space]]:

_closure under addition_ **`V (u : v)`**

_closure under multiplication by a [[scalar]]_ **`V (c | u)`**

_zero vector_ **`V O /\ O : u = u`**

_inverse_ **`V (.u) /\ u : .u = O`**

_identity_ **`1u = u`**

_commutativity_ **`u : v = v : u`**

_associativity of addition_ **`u : (v : w) = (u : v) : w`**

_distributivity_ **`c | u : v = cu : cv`**

_distributivity_ **`c : d | v = cv : dv`**

_associativity of multiplication_ **`c | du = cd | u`**

## Subspace

**definition**

**`U`** is a _subspace_ of **`V`** if and only if **`/\ U -| V`** and **`U`** is a [[vector space]]

> **note** if **`/\ U -| V`**, many properties of **`U`** are inherited from **`V`** and therefore the only [[axiom]]s that need be rechecked are _closure under addition_, _closure under multiplication by a [[scalar]]_, and the _zero vector_

**propreties**

let **`V {{v_0 ... v_m}}`**. if **`U = "span" {{v_0 ... v_m}}`**, then **`/\ U -| V`**, see [[span]]

## Isomorphism

_Iso-Morphic &mdash; Same Shape_

**see** [[category]], [[category theory]]

> **example** **`RR^3`** and **`PP^2`** are isomorphic, as any vector in **`RR^3`** can be converted to a unique vector in **`PP^2`**, and vice-versa, see [[category]]

## Dimension

**notation** _in my [[math notation]]_

**`"dim" V`**

**definition**

the _dimension of a vector space_ is equal to the number of [[vector]]s in any [[basis]] of that vector space

> **example**
>
> below are the [[vector space#dimension]]s of a few common [[vector space]]s
>
> - **`"dim" RR^2 = 2`**
> - **`"dim" PP^2 = 3`**
> - **`"dim" HH = @@`**
> - **`"dim" MM^3,4 = 12`**
> - **`"dim" V = 2`** where **`V`** is a [[plane#plane in r3]]
> - **`"dim" V = 1`** where **`V`** is a [[line#line in r3]] or in **`RR^2`**
> - **`"dim" "span" {{O}} = 0`** (see [[span]], zero [[vector]])

## describing vector spaces

there are three major ways of describing [[vector space]]s

### [[vector]] with restrictions

**`V v == v = (x, y, z) /\ x . 2y : z = 0 > RR {x /\ y /\ z}`**

### [insert name here]

**`V v == v = (2y . z, y, z) > RR {y /\ z}`**

### as a [[linear combination]]

let **`V v == v = (x, y, z) /\ x . 2y : z = 0`**

yields the system **`[]1 & .2 & 1 & || & 0[] == x = 2y . z`**

the general solution to the [[linear system]] above will be the [[vector space]] represented as a [[linear combination]] of specific [[vector]]s:

**`(x, y, z) = (2y . z, y, z) = y(2, 1, 0) : z(.1, 0, 1)`**
