# Linear Transformation

**see** [[math notation]]

**definition**

let **`U`** and **`V`** be two [[vector space]]s with **`"dim" U = u`** and **`"dim" V = v`**. a [[linear transformation]] **`T`** from **`U`** to **`V`** is a [[matrix#multiplication]] **`T u = A | u`** with **`MM^v,u A`** #todo mm

**definition**

let **`U`** and **`V`** be two [[vector space]]s. a [[linear transformation]] **`T`** from **`U`** to **`V`** is a [[function]] from **`U`** to **`V`** that satisfies the following properties:

- **`T (u_1 : u_2) = T u_1 : T u_2 > U u_1 /\ U u_2`**
- **`T cu = c | T u > U u /| RR c`**

**notation** **`TT T`** if and only if **`T`** is a [[linear transformation]]

**theorem** **`TT T < T O = O`**

**properties**

**`TT < FF`**, see [[function#vector space]]

## Standard Matrix

#todo mm

**theorem** **`TT T`** if and only if there exists a [[matrix]] **`A`** such that **`T u = A | u > RR^n u`**

**theorem** given a **`TT T`** with **`T u == A | u`**, **`A = \r (T I *)`**

> **proof**
>
> **`A | u = AI | u = T I | u`**. it is worth noting that **`T I`** is not a valid [[linear transformation]] because **`I`** is a [[matrix]]. however, since **`I`** is the [[matrix#identity matrix]], **`T I`** is equivalent to **`\r (T (\r I) *)`**, which is equivalent to **`\r (T I *)`**. we therefore conclude that **`A = \r (T I *)`**, which is to be read as:
>
> > **`A`** is a [[matrix]] (**`A =`**) whose columns (**`\r`**) are the rows of the [[matrix#identity matrix]] (**`I *`**) transformed by **`T`** (**`T`**)
>
> &mdash; me

> **equivalence** _[[matrix#multiplication]] and [[linear transformation]]s_

> **example** _computing a [[linear transformation#standard matrix]]_
>
> let **`TT T /\ T (x, y, z) = (x : 5y : z, x . 3z, y, y : 2z)`**
>
> compute **`T (1, 0, 0) = (1, 1, 0, 0)`** and **`T (0, 1, 0) = (5, 0, 1, 1)`** and **`T (0, 0, 1) = (1, .3, 0, 2)`**
>
> then, the [[linear transformation#standard matrix]] of **`T`** **`A`** is defined as follows:
>
> **`A = []|| & || & || && T (1, 0, 0) & T (0, 1, 0) & T (0, 0, 1) && || & || & ||[] = []1 & 5 & 1 && 1 & 0 & .3 && 0 & 1 & 0 && 0 & 1 & 2[]`**

> **example** _turning a [[vector in rn#projection]] into [[matrix#multiplication]]_
>
> let **`W = "span" {{ (1, 0, 1), (0, 1, 0) }}`** and **`T u = "proj"_W u /\ RR^3 u`**
>
> as the [[basis]] we are given is a [[basis#orthogonal basis]], we define the [[vector in rn#projection]] as:
>
> **`"proj"_W u = (u^0 : u^2 -- 2 | (1, 0, 1)) : (u^1 -- 1 | (0, 1, 0)) = (u^0 : u^2 -- 2, u^1, u^0 : u^2 -- 2)`**, see [[vector in rn#projection]]
>
> #todo mm
>
> rearranging, we get **`"proj"_W u = u^0 (--2, 0, --2) : u^0 (0, 1, 0) : u^0 (--2, 0, --2) = []--2 & 0 & -2 && 0 & 1 & 0 && --2 & 0 & --2[][]u^0 && u^1 && u^2[] = []--2 & 0 & --2 && 0 & 1 & 0 && --2 & 0 & --2[] | u`**, which is [[matrix#multiplication]]
>
> alternatively, we can use the following, see #magic:
>
> **`B = []|| & & || && b_0 & ... & b_n && || & & ||[]`** where **`{{b_0 ... b_n}}`** is a [[basis]] for **`W`** that does **not** have to be a [[basis#orthogonal basis]]. in this case, **`b_0 = (1, 0, 1)`** and **`b_1 = (0, 1, 0)`**
>
> #todo mm
>
> then, **`"proj"_W u = A | u`** with **`A = B -- (\r B | B) | \r B = []--2 & 0 & --2 && 0 & 1 & 0 && --2 & 0 & --2[]`**, see #magic. **`A`** is the [[linear transformation#standard matrix]] of **`T`**

> **example** _computing the 2D Rotation Matrix_
>
> let a [[vector in rn#unit vector]] on the **`x`** axis **`i`** and let a [[vector in rn#unit vector]] on the **`y`** axis **`j`**
>
> let a [[vector in rn#unit vector]] on the **`x_*`** axis **`i_* = ("cos" \a, "sin" \a)`** and let a [[vector in rn#unit vector]] on the **`y_*`** axis **`j_* = (."sin" \a, "cos" \a)`**
>
> let **`(c, f c) = ic : jf c`** be a point on a [[function]] **`f`**. replacing **`i, j`** by **`i_* , j_*`**, we get the point **`i_* c : j_* f c = ("cos" \a, "sin" \a)c : (."sin" \a, "cos" \a)f c = (c("cos" \a) : (f c)(."sin" \a), c("sin" \a) : (f c)("cos" \a))`**.
>
> with **`(c, f c) = (x, y)`**, we get the point **`(x"cos" \a . y"sin" \a, x"sin" \a : y"cos" \a)`**, which can be graphed as **`x"sin" \a : y"cos" \a = f (x"cos" \a . y"sin" \a)`**
>
> computing the [[linear transformation#standard matrix]]:
>
> #todo mm
>
> with **`(c, f c) = (x, y)`**, we get the [[linear transformation]] **`T (x, y) = (x"cos" \a . y"sin" \a, x"sin" \a : y"cos" \a)`**. its [[linear transformation#standard matrix]] is **`[]|| & || && T (1, 0) & T (0, 1) && || & ||[] = []"cos" \a & ."sin" \a && "sin" \a & "cos" \a[]`**. defining **`T`** using [[matrix#multiplication]], we get **`T (x, y) = []"cos" \a & ."sin" \a && "sin" \a & "cos" \a[][]x && y[] = []x"cos" \a . y"sin" \a && x"sin" \a : y"cos" \a[]`**, which can also be graphed as **`x"sin" \a : y"cos" \a = f (x"cos" \a . y"sin" \a)`**
>
> &mdash; me

## Kernel

## Image

**notation**

**`kk T`**

**`"Im" T`**

**definition** _kernel_

**`(kk T) x == T x = 0 /\ TT T`**

**definition** _image_

**`("Im" T) x == T u = x /\ TT T`**

**theorem**

#todo fix below

let **`MM^m,n A`** be the [[linear transformation#standard matrix]] of **`T`**. then,

**`kk T = nn A`**, see [[matrix#null space]]

**`"Im" T = cc A`**, see [[matrix#column space]]

**theorem** **`"dim" kk T : "dim" "Im" T = "dim" nn A : "dim" cc A = n`**, where **`n`** is the dimension of the [[function#domain]] of **`T`**
