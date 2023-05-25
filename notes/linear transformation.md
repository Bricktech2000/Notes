# Linear Transformation

**see** [[math notation]]

**definition**

let **`U`** and **`V`** be two [[vector space]]s with **`"dim" U = u`** and **`"dim" V = v`**. a [[linear transformation]] **`T`** from **`U`** to **`V`** is a [[matrix#multiplication]] **`T u = A | u`** with **`MM^v,u A`** #todo mm

**definition**

let **`U`** and **`V`** be two [[vector space]]s. a [[linear transformation]] **`T`** from **`U`** to **`V`** is a [[function]] from **`U`** to **`V`** that satisfies the following properties:

- **`T (u_1 : u_2) = T u_1 : T u_2 > U u_1 /\ U u_2`**
- **`T cu = c | T u > U u /\ RR c`**

**notation** **`TT T`** if and only if **`T`** is a [[linear transformation]]

**theorem** **`TT T < T O = O`**

**properties**

**`TT < HH`**, see [[function#vector space]]

## Standard Matrix

#todo mm

**theorem** **`TT T`** if and only if there exists a [[matrix]] **`A`** such that **`T u = A | u > RR^n u`**

> **equivalence** _[[matrix#multiplication]] and [[linear transformation]]s_

**theorem** given a **`TT T`** with **`T u == A | u`**, **`A = rr (T I *)`**

> **proof**
>
> **`A | u = AI | u = T I | u`**. it is worth noting that **`T I`** is not a valid [[linear transformation]] because **`I`** is a [[matrix]]. however, since **`I`** is the [[matrix#identity matrix]], **`T I`** is equivalent to **`rr (T (rr I) *)`**, which is equivalent to **`rr (T I *)`**. we therefore conclude that **`A = rr (T I *)`**, which is to be read as:
>
> > **`A`** is a [[matrix]] (**`A =`**) whose columns (**`rr`**) are the rows of the [[matrix#identity matrix]] (**`I *`**) transformed by **`T`** (**`T`**)
>
> &mdash; me

> **note** by definition, applying a [[linear transformation]] on [[vector]]s of the [[function#domain]] [[vector space]] will yield the images of those [[vector]]s in the [[function#codomain]] [[vector space]]. since multiplying a [[matrix]] by a [[basis#standard basis]] [[vector]] yields one of the columns of the [[matrix]], the columns of a [[linear transformation#standard matrix]] corresponds to the images of the [[basis#standard basis]] [[vector]]s
>
> &mdash; me

> **example** _computing a [[linear transformation#standard matrix]]_
>
> let **`TT T /\ T (x, y, z) = (x : 5y : z, x . 3z, y, y : 2z)`**
>
> compute **`T (1, 0, 0) = (1, 1, 0, 0)`** and **`T (0, 1, 0) = (5, 0, 1, 1)`** and **`T (0, 0, 1) = (1, .3, 0, 2)`**
>
> then, the [[linear transformation#standard matrix]] of **`T`** **`A`** is defined as follows:
>
> **`A = []|| & || & || && T (1, 0, 0) & T (0, 1, 0) & T (0, 0, 1) && || & || & ||[] = []1 & 5 & 1 && 1 & 0 & .3 && 0 & 1 & 0 && 0 & 1 & 2[]`**

**properties**

`(A | B) | u = A | (B | u)` &mdash; [[matrix#multiplication]] on the [[linear transformation#standard matrix]]es of two [[linear transformation]]s gives the [[composition]] of the two [[linear transformation]]s

**examples**

> **example** _deriving the 2D Rotation Matrix_
>
> let a [[vector in rn#unit vector]] on the **`x`** axis **`i`** and let a [[vector in rn#unit vector]] on the **`y`** axis **`j`**
>
> let a [[vector in rn#unit vector]] on the **`x_*`** axis **`i_* = ("cos" aa, "sin" aa)`** and let a [[vector in rn#unit vector]] on the **`y_*`** axis **`j_* = (."sin" aa, "cos" aa)`**
>
> let **`(c, f c) = ic : jf c`** be a point on a [[function]] **`f`**. replacing **`i, j`** by **`i_* , j_*`**, we get the point **`i_* c : j_* f c = ("cos" aa, "sin" aa)c : (."sin" aa, "cos" aa)f c = (c("cos" aa) : (f c)(."sin" aa), c("sin" aa) : (f c)("cos" aa))`**.
>
> with **`(c, f c) = (x, y)`**, we get the point **`(x"cos" aa . y"sin" aa, x"sin" aa : y"cos" aa)`**, which can be graphed as **`x"sin" aa : y"cos" aa = f (x"cos" aa . y"sin" aa)`**
>
> computing the [[linear transformation#standard matrix]]:
>
> with **`(c, f c) = (x, y)`**, we get the [[linear transformation]] **`T (x, y) = (x"cos" aa . y"sin" aa, x"sin" aa : y"cos" aa)`**. its [[linear transformation#standard matrix]] is **`[]|| & || && T (1, 0) & T (0, 1) && || & ||[] = []"cos" aa & ."sin" aa && "sin" aa & "cos" aa[]`**. defining **`T`** using [[matrix#multiplication]], we get **`T (x, y) = []"cos" aa & ."sin" aa && "sin" aa & "cos" aa[][]x && y[] = []x"cos" aa . y"sin" aa && x"sin" aa : y"cos" aa[]`**, which can also be graphed as **`x"sin" aa : y"cos" aa = f (x"cos" aa . y"sin" aa)`**
>
> &mdash; me

> **example** _deriving the 2D Rotation Matrix, in a sane way_
>
> the columns of a [[linear transformation#standard matrix]] are the images of the [[basis#standard basis]] [[vector]]s. to rotate a [[plane]] by **`aa "rad"`**, we want **`(1, 0)`** to end up at **`("cos" aa, "sin" aa)`** and **`(0, 1)`** to end up at **`(."sin" aa, "cos" aa)`**. therefore, the [[linear transformation#standard matrix]] is **`[]"cos" aa & ."sin" aa && "sin" aa & "cos" aa[]`**
>
> &mdash; me

## Kernel

## Image

**notation**

**`KK T`**

**`"Im" T`**

**definition** _kernel_

**`(KK T) x == T x = 0 /\ TT T`**

**definition** _image_

**`("Im" T) x == T u = x /\ TT T`**

**theorem**

#todo fix below

let **`MM^m,n A`** be the [[linear transformation#standard matrix]] of **`T`**. then,

**`KK T = NN A`**, see [[matrix#null space]]

**`"Im" T = CC A`**, see [[matrix#column space]]

**theorem** **`"dim" KK T : "dim" "Im" T = "dim" NN A : "dim" CC A = n`**, where **`n`** is the dimension of the [[function#domain]] of **`T`**
