# Linear Dependence

**see** [[linearly dependent]], [[linearly independent]], [[vector]], [[vector space]], [[linear combination]]

**definition**

let **`V`** be a [[vector space]] and let **`v = (v^0 ... v^i)`** such that **`V v *`**

then, **`v`** are [[linearly independent]] if and only if **`:av = O == a = O`**

**procedures**

> **procedure** _determining if vectors are linearly independent_
>
> to check for [[linear dependence]], one can use a homogeneous [[linear system]] and solve it using [[row reduction]]. the following can be concluded (think of this intuitively):
>
> - no solutions: not possible, as the [[linear system]] is homogeneous
> - one solution: the vectors are [[linearly independent]]
> - infinitely many solutions: the vectors are [[linearly dependent]]

**properties**

any [[set#superset]] of a [[linearly dependent]] [[set]] is also [[linearly dependent]]

any [[set#subset]] of a [[linearly independent]] [[set]] is also [[linearly independent]]

any [[set]] containing the **`O`** [[vector]] is [[linearly dependent]]

**theorems**

**theorem** a [[set]] of [[vector]]s is [[linearly dependent]] if and only if at least one of its [[vector]]s can be represented as a [[linear combination]] of the others

**theorem** **`W = "span" {{v_0, v_1 ... v_m}} /\ "span" {{v_1 ... v_m}} v_0 < W = "span" {{v_1 ... v_m}}`** see [[span]]

**theorem** if a [[vector space]] **`V`** can be spanned by **`n`** [[vector]]s, then any [[linearly independent]] [[set]] in **`V`** has at most **`n`** [[vector]]s

**theorem** if a [[vector space]] **`V`** has a [[set#subset]] of **`m`** [[linearly independent]] [[vector]]s, then any [[span]]ning [[set]] has at least **`m`** [[vector]]s

**theorem** any [[linearly independent]] [[set]] in a [[vector space]] is smaller than or equal in length to a [[span]]ing [[set]] of the [[vector space]]

**theorem** the size of any [[linearly independent]] [[set]] in **`V`** is no more than **`\dim V`** is no more than the size of any [[span]]ning [[set]] in **`V`**
