# Eigen

## Space

## Vector

## Value

**definition**

let **`MM^n,n A /\ NN n /\ RR ll /\ RR^n x /\ x + O`**

if **`:Ax = llx`**, then **`x`** is an [[eigen#vector]] of **`A`** and **`ll`** is its corresponding [[eigen#value]]

**theorems**

let **`MM^n,n A /\ NN n`**

**theorem** there are infinitely many [[eigen#vector]]s for each [[eigen#value]]

**theorem** all [[eigen#vector]]s together with the zero [[vector]] form a [[vector space]]

**theorem** the [[characteristic polynomial]] **`"det" (A . llI)`** is a [[polynomial]] of degree **`n`**, meaning it has at most **`n`** distinct [[function#root]]s by the [[fundamental theorem of algebra]]

**theorem** **`A`** has at most **`n`** distinct [[eigen#value]]s

**theorem** each [[eigen#value]] of **`A`** gives an [[eigen#space]] of [[vector space#dimension]] greater than **`0`**

**theorem** [[eigen#vector]]s of **`A`** corresponding to **distinct [[eigen#value]]s** are [[vector#linearly independent vector]]s

**procedures**

> **procedure** _finding [[eigen#value]]s_
>
> **`:Ax = llx`**
>
> **`O = :Ax . llx = :Ax . :(llI)x = :(A . llI)x = O`**
>
> the equation above is a homogeneous [[linear system]] where **`A . llI`** is the _coefficient matrix_
>
> recall that a homogeneous [[linear system]] can have either a unique solution (with **`x = O`**, which is not a valid [[eigen#vector]] as per the definition) or an infinite number of solutions (which we can achieve by picking the right values for **`ll`**). for a homogeneous [[linear system]] to have an infinite number of solutions, the [[determinant]] of its coefficient matrix must be equal to **`0`** (see [[matrix#theorems]])
>
> **`"det" (A . llI) = 0`** (this [[polynomial]] is known as the _[[characteristic polynomial]] of **`A`**_)
>
> solving...
>
> _using **`A = []1 & 2 && 2 & 1[]`** as an example_
>
> **`A . llI = []1 & 2 && 2 & 1[] . ll[]1 & 0 && 0 & 1[] = []1 .ll & 2 && 2 & 1 . ll[]`**
>
> **`"det" (A . llI) = 0 = [1 . ll]2 . 4 = 1 . ll : 2 | 1 . ll . 2 = 3 . ll | . 1 . ll = 0`**
>
> **`ll = {3 \/ .1}`** are the [[eigen#value]]s of **`A`**

> **procedure** _finding [[eigen#vector]]s_
>
> as **`:(A . llI)x = O`**, we get the following (see [[matrix#null space]]):
>
> **`E_ll = NN (A.llI)`**, where
>
> **`E_ll`** is the _[[eigen#space]]_ of **`A`** corresponding to the [[eigen#value]] **`ll`** (this [[vector space]] is called the &lambda;-[[eigen#space]] of **`A`**)
>
> the [[eigen#vector]]s of **`A`** associated with the [[eigen#value]] **`ll`** are all the nonzero [[vector]]s in **`E_ll`**. therefore, instead of finding the [[eigen#vector]]s corresponding to the known [[eigen#value]], we will find a basis for the [[eigen#space]]
>
> for **`ll = 3`**:
>
> **`:(A . 3I)x = O`**
>
> **`:(A . 3I)x = :([]1 & 2 && 2 & 1[] . []3 & 0 && 0 & 3[])x = :[].2 & 2 && 2 & .2[]x = 0`**
>
> therefore, we can solve the following [[linear system]] using [[row reduction]]
>
> **`[].2 & 2 & || & 0 && 2 & .2 & || & 0[]`**
>
> and we get:
>
> **`x = c(1, 1) > RR c`**
>
> **`{{ (1, 1) }}`** is then a [[basis]] for the [[eigen#space]] **`E_3`** of **`A`**
>
> > **note** the general solution of the homogenous [[linear system]] will always be a [[basis]] as the resulting [[vector]]s will always be [[vector#linearly independent vector]]s, see [[matrix#null space]] for more information
>
> for **`ll = .1`**, we get the [[basis]] **`{{ (1, .1) }}`** for the [[eigen#space]] **`E_.1`** of **`A`**

**application**

#todo mm

_raising a matrix to a large power efficiently_

let **`MM^n,n A /\ NN n`** be a [[matrix#diagonalizable matrix]]

1.  construct a matrix **`P = []|| & || & || && x_0 & x_1 & x_2 && || & || & ||[] = []x_0^0 & x_1^0 & x_2^0 && x_0^1 & x_1^1 & x_2^1 && x_0^2 & x_1^2 & x_2^2[]`** whose columns are the **`n`** [[vector#linearly independent vector]] [[eigen#vector]]s **`x`** of **`A`**
2.  construct a matrix **`D = []ll_0 & 0 & 0 && 0 & ll_1 & 0 && 0 & 0 & ll_2[]`** whose [[matrix#diagonal]] entries are the [[eigen#value]]s of **`A`** and all other entries equal to **`0`**, in the same order as the columns of **`P`**

then, **`AP = PD`**. as the columns of **`P`** are [[vector#linearly independent vector]]s, we know **`P`** is an invertible [[matrix]]. therefore, **`A = PDP^-`** and **`P^- AP = D`**

> **proof** the **`n`**th column of **`AP`** is **`AP^*,n = Ax_n`**. since **`x_n`** is an [[eigen#vector]] of **`A`**, we use its corresponding [[eigen#value]] to get **`AP^*,n = Ax_n = ll_n x_n`** by definition, see [[eigen]]. the **`n`**th column of **`PD`** is **`PD^*,n`**. when multiplying out, we get **`PD^*,n = x_n D^n,n = x_n ll_n`**. as **`AP^*,n = PD^*,n -| NN n`**, we conclude **`AP = PD`**

now, compute **`[A]p /\ NN p`** with **`p`** being a very large integer

with **`A = PDP^-`**, we get **`[A]p = [PDP^-]p = P | [D]p | P^-`**

as **`D`** is a [[matrix#diagonal matrix]], we get **`[D]p = [] [ll_0]p & 0 & 0 && 0 & [ll_1]p & 0 && 0 & 0 & [ll_2]p []`**

computing **`[A]p = P[][ll_0]p & 0 & 0 && 0 & [ll_1]p & 0 && 0 & 0 & [ll_2]p[]P^-`** is now way less computationally expensive than computing **`[A]p`** directly

**application**

[[eigen#vector]]s and [[eigen#value]] can be useful in [[markov chain]]s &mdash; <https://www.youtube.com/watch?v=JGQe4kiPnrU>

### Multiplicity

**see** [[multiplicity]]

**definition** the _algebraic multiplicity_ of a [[function#root]] **`ll`** of the [[characteristic polynomial]] of **`A`** is its [[multiplicity]]

**definition** the _geometric multiplicity_ of a [[function#root]] **`ll`** of the [[characteristic polynomial]] of **`A`** is the [[vector space#dimension]] of the [[eigen#space]] **`E_ll`** of **`A`** corresponding to the [[eigen#value]] **`ll`**

**theorem** let **`ll`** be an [[eigen#value]] of **`A`**. then, **`1 -| "geometric multiplicity of" ll -| "algebraic multiplicity of" ll`**

> **example** the [[characteristic polynomial]] of **`[]2 & 4 & .3 && 0 & 3 & 5 && 0 & 0 & 3[]`** is **`2 . ll | [3 . ll]2`**. its [[eigen#value]]s are **`ll = 2`** and **`ll = 3`**. the algebraic [[eigen#multiplicity]] of **`ll = 2`** is **`1`** and the algebraic [[eigen#multiplicity]] of **`ll = 3`** is **`2`**.

**applications**

[[eigen#multiplicity]] can be used to determine whether a [[matrix]] is a [[matrix#diagonalizable matrix]]
