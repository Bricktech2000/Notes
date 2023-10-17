# Linear Dependence

**see** [[vector]], [[vector space]], [[linear combination]]

**definition**

let **`V`** be a [[vector space]] and let **`V v *`** be a [[list]] of [[vector]]s in **`V`**

then, **`v`** are [[vector#linearly independent vector]]s if and only if **`:av = O == a = O`**

**procedures**

> **procedure** _determining if vectors are linearly independent_
>
> to check for [[linear dependence]], one can use a homogeneous [[linear system]] and solve it using [[row reduction]]. the following can be concluded (think of this intuitively):
>
> - no solutions: not possible, as the [[linear system]] is homogeneous
> - one solution: the vectors are [[vector#linearly independent vector]]s
> - infinitely many solutions: the vectors are [[vector#linearly dependent vector]]s

**properties**

any [[set#superset]] of a [[set]] of [[vector#linearly dependent vector]]s is also a [[set]] of [[vector#linearly dependent vector]]s

any [[set#subset]] of a [[set]] of [[vector#linearly independent vector]]s is also a [[set]] of [[vector#linearly independent vector]]s

any [[set]] containing the **`O`** [[vector]] is a [[set]] of [[vector#linearly dependent vector]]s

**theorems**

**theorem** a [[set]] is a [[set]] of [[vector#linearly dependent vector]]s if and only if at least one of its [[vector]]s can be represented as a [[linear combination]] of the others

**theorem** **`W = "span" {{v_0, v_1 ... v_m}} /\ "span" {{v_1 ... v_m}} v_0 < W = "span" {{v_1 ... v_m}}`** see [[span]]

**theorem** if a [[vector space]] **`V`** can be spanned by **`n`** [[vector]]s, then any [[set]] of [[vector#linearly independent vector]]s in **`V`** contains at most **`n`** [[vector]]s

**theorem** if a [[vector space]] **`V`** has a [[set#subset]] of **`m`** [[vector#linearly independent vector]]s, then any [[span]]ning [[set]] contains at least **`m`** [[vector]]s

**theorem** any [[set]] of [[vector#linearly independent vectorc]]s in a [[vector space]] has [[set#cardinality]] no more than the [[set#cardinality]] of a [[span]]ing [[set]] of the [[vector space]]

**theorem** the [[set#cardinality]] of any [[set]] of [[vector#linearly independent vector]]s in **`V`** is no more than **`"dim" V`** which is no more than the [[set#cardinality]] of any [[span]]ning [[set]] in **`V`**
