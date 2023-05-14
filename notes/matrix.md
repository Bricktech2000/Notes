# Matrix

**see** [[math notation]], [[eigen]]

**definition** _formally in my [[math notation]]_ a [[matrix]] is a [[set theory]]etical [[function]] that takes two [[natural]] indices and returns the element at that index

**notation**

**`[]a & b && c & d[]`**

## Vector Space

**notation** _in my [[math notation]]_ **`MM^m,n`**

**notation** _in [[conventional math notation]]_ $M_{m\ n}(\mathbb R)$

### Multiplication by Scalar

**see** [[vector]], [[vector space]]

**definition**

**`kA`**

**properties**

_commutativity with [[scalar]]s_ **`kA = Ak`**

### Addition

**see** [[vector]], [[vector space]]

**definition**

**`A : B`**

## Multiplication

#todo mm

**see** [[dot product]], [[vector in rn]]

**definition**

**`AB = :(A *)(\r B *)`**, see [[dot product]]

intuitively, matrix multiplication is the [[dot product]] of **every row** of the first [[matrix]] by **every column** of the second [[matrix]]

**properties**

**`AB + @ == MM^m,n A /\ MM^n,p B /\ MM^m,p AB`** (**`AB`** is defined if the number of columns in **`A`** is equal to the number of rows in **`B`**. their product will be an **`m`** by **`p`** [[matrix]])

_not commutative_ **`><(MM A /\ MM B < AB = BA)`**

**`><(AB = 0 < A = 0 \/ B = 0)`** (it can happen that **`AB = 0`**, but **`A + 0`** and **`B + 0`**) (**`AB`** being equal to **`0`** does not imply that **`A = 0`** or that **`B = 0`**)

**`><(AC = BC /\ C + 0 < A = B)`** (**`AC = BC`** and **`C + 0`** does not imply that **`A = B`**)

_associative_ **`(AB)C = A(BC)`**

_distributive_ **`A(B : C) = AB : AC`**

_distributive_ **`(B : C)A = BA : CA`**

_associative with [[scalar]]s_ **`k(AB) = (kA)B = A(kB)`**

**applications**

[[matrix#multiplication]] can be used to represent a [[linear system]] of [[linear equation]]s. matrix-vector products can be seen as yielding a [[linear combination]] of the columns of the [[matrix]]:

**`[]1 & 2 & 3 && 4 & 5 & 6[][]x && y && z[] = x[]1 && 4[] : y[] 2 && 5[] : z[]3 && 6[]`**

> **equivalence** _[[matrix#multiplication]] and [[linear transformation]]s_

## Identity Matrix

**definition**

**`I = i j -> (i = j)`**

**properties**

**`AI = A /\ IA = A`**

## Zero Matrix

**see** [[vector]], [[vector space]]

**definition**

**`O = i j -> 0`**

**properties**

**`A_m,n O_n,p = O_m,p > MM^n,p O_n,p /\ MM^m,p O_m,p /\ MM^m,n A_m,n`**

**`O_q,m A_m,n = O_q,n > MM^q,m O_q,m /\ MM^q,n O_q,n /\ MM^m,n A_m,n`**

## Rank

_the number of pivots in any [[linear system#row echelon form]] of the [[matrix]]_

**notation** **`"rank" A`**

## Element Count

**notation** **`# M`**

**definition** the _element count_ of a [[matrix]] is the total number of elements in the [[matrix]]

> **example** let **`M = []1 & 2 & 3 && 4 & 5 & 6[]`**. then, **`MM^2,3 M /\ # M = 2 | 3 = 6`**

## Null Space

## Column Space

## Row Space

**notations**

_null space_ **`nn A`**

_column space_ **`cc A`**

_row space_ **`rr A`**

**definitions**

_kernel_ **`(nn A) x == Ax = O /\ MM^m,n A /\ MM^n,1 x`**

_column space_ **`cc A = "span" {{A^*,0 , A^*,1 , ...}}`**

_row space_ **`rr A = "span" {{A^0,* , A^1,* , ...}}`**

**procedure** _computing the null space of a [[matrix]]_ use [[row reduction]]

**theorems**

the [[matrix#null space]], [[matrix#row space]] and [[matrix#column space]] of a [[matrix]] are always [[vector space]]s

**`"number of free variables in" A : "number of pivots in" A = "number of columns in" A`**

**`"dim" nn A = "number of free variables in" A`**

**`"rank" A = "number of pivots in" A`**

the nonzero rows in any [[linear system#row echelon form]] of a [[matrix]] **`A`** forms a [[basis]] for **`rr A`**. therefore, **`"dim" rr A = "rank" A`**, see [[matrix#rank]]

if **`A`** and **`B`** are row-equivalent, then **`rr A = rr B`**, see [[linear system]]

the [[span]]ning [[set]] of **`nn A`** obtained from applying [[row reduction]] on the system **`Ax = O`** is a [[basis]] for **`nn A`**

**`rr A`** does not change when applying [[linear system#elementary operation]]s on the rows of **`A`**

**properties**

**`cc A = rr (\r A) /\ rr A = cc (\r A)`**, see [[matrix#transpose]]

**applications**

[[matrix#row space]]s can be used to find a [[basis]] for a [[span]]ning [[set]] of [[vector]]s through [[row reduction]]

the [[basis]] for a [[matrix#row space]] can be found by applying [[row reduction]] and [[span]]ning the **row-reduced columns** in the [[linear system#row echelon form]] of the [[matrix]]

the [[basis]] for a [[matrix#column space]] of a [[matrix]] can be found by applying [[row reduction]] and [[span]]ning the **original columns** that became pivots in the [[linear system#row echelon form]] of the [[matrix]]

the same can be said for **`cc A`**

> **example** _transforming a [[vector space]] into the [[matrix#null space]] of a certain [[matrix]]_
>
> let **`W = "span" {{ (1, 0, 0, 1), (1, 1, 1, 0), (2, 1, .1, 1) }}`**
>
> after solving the [[linear system]], we get **`W (x, y, z, w) == .x : y : w = 0`**. therefore, **`W`** is the [[matrix#null space]] of **`A = [].1 & 1 & 0 & 1[]`**

## Diagonal

_the diagonal of a [[matrix]]_

**definition** the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element

## Transpose

_the transpose of a [[matrix]]_

_flips a [[matrix]] around its [[matrix#diagonal]]_

**notation** **`\r A`**

**definition** **`\r A`**

**properties**

**`\r \r A = A`**

**`\r AB = \r B | \r A`** #todo mm

## Conjugate Transpose

_the [[complex#conjugate]] of every entry of the [[matrix#transpose]] of a [[matrix]]_

**aka** _Hermitian transpose, adjoint matrix, transjugate_

**definition**

**`"conj" \r A`**, where

- **`A`** is the [[matrix]] to find the [[matrix#conjugate transpose]] of
- **`"conj"`** is the [[complex#conjugate]] [[function]]
- **`\r`** is the [[matrix#transpose]] [[operator]]

**properties**

let a [[matrix]] of [[real]]s **`A`**. then, **`"conj" \r A = \r A`**

## Inverse

#todo mm

_the inverse of a [[matrix]]_

**definition**

**`AA^- = A^- A = I > MM A`**, where

- **`A`** is a square [[matrix]]
- **`A^-`** is the _inverse matrix_ of **`A`**

### Invertability

**definition** an _invertible matrix_ has a corresponding [[matrix#inverse]]

**see** theorems below for invertability criteria

**properties**

let **`A`** and **`C`** be invertible [[matrix]]es, let **`ZZ p`** and let **`RR k /\ k + 0`**. then,

**`AA^- = A^- A = I`**

**`(A^-)^- = A`**

**`(A^p)^- = (A^-)^p`**

**`(kA)^- = -k | A^-`** (see [[improved expression evaluation]])

**`(AC)^- = C^- A^-`**

> **note** in the equation above, the order of the [[matrix]]es has changed. this is significant as [[matrix#multiplication]] is not commutative

if **`AC`** is invertible, then **`A`** is invertible and **`C`** is invertible

> **procedure** _computing the [[matrix#inverse]] of a [[matrix]]_
>
> let **`MM^n,n A`**
>
> solve the system **`AA^- = I`** by extending the [[matrix]] with the [[matrix#identity matrix]] and solve the [[linear system]] up to [[linear system#reduced row echelon form]] using [[row reduction]]. **`[]A & || & I[]`** [...] **`[]I & || & A^-[]`**

> **procedure** _computing the [[matrix#inverse]] of a **`2`** by **`2`** [[matrix]]_
>
> **see** [[determinant]]
>
> let **`A = []a & x && c & d[]`**
>
> **`A`** is invertible if and only if **`"det" A + 0`**
>
> **`A^- = -- "det" A | []d & .b && .c & a[]`**

**applications**

> **example** _using a [[matrix#inverse]] to solve a [[linear system]]_
>
> let **`A = []1 & 1 && 2 & 3[]`**
>
> then, calculate **`B`** such that **`B = A^-`**
>
> this can be used to solve a [[linear system]] such as:
>
> **`Ax = [].1 && 1[]`**
>
> **`BAx = B [].1 && 1[]`**
>
> **`Ix = x = B [].1 && 1[]`\***

## Triangular Matrix

**definition** a [[matrix]] is said to be _triangular_ if every entry below its [[matrix#diagonal]] **or** above its [[matrix#diagonal]] is **`0`**

## Diagonal Matrix

**definition** a [[matrix]] is said to be _diagonal_ if every entry below its [[matrix#diagonal]] **and** above its [[matrix#diagonal]] is **`0`**

**applications**

**`[D]x`** can be calculated by raising every entry of **`D`** to the power **`x`** #todo mm

## Diagonalizable Matrix

**see** [[eigen#vector]]

**definition** an **`n`** by **`n`** [[matrix]] **`A`** is said to be _diagonalizable over the reals_ if there exists a [[basis]] of **`RR^n`** consisting entirely of [[eigen#vector]]s of **`A`**

a [[matrix]] is _diagonalizable_ if and only if the geometic [[eigen#multiplicity]] of an [[eigen#value]] is equal to the algebraic [[eigen#multiplicity]] of said [[eigen#value]], for every [[eigen#value]] of the [[matrix]]

> **note** a [[matrix]] may also be diagonalizable over other [[field]]s such as the [[set]] of [[complex]] numbers **`CC`**

> **note** some [[matrix]]es do not have "enough" real [[eigen#value]]s or "enough" [[eigen#vector]]s to be diagonalizable

> **example** the [[matrix]] **`A = []1 & 2 && 2 & 1[]`** is diagonalizable over the reals as **`{{ (1, 1), (1, .1) }}`** is a [[basis]] of **`RR^2`** consisting entirely of [[eigen#vector]]s of **`A`**

> **example** the [[matrix]] **`A = []1 & 1 && 1 & 1[]`** is not diagonalizable over the reals as it does not have any real [[eigen#value]]s

> **example** the [[matrix]] **`A = []3 & 1 && 0 & 3[]`** is not diagonalizable over the reals as it only has one [[eigen#value]], and therefore only one set of [[linearly dependent]] [[eigen#vector]]s

> **example** the [[matrix]] **`A = []1 & 0 && 0 & 1[]`** is diagonalizable over the reals as, even though **`A`** has a single [[eigen#value]] **`\l = 1`**, its [[eigen#space]] [[span]]s **`RR^2`**. this is the case for both **`A = I /\ \l = 1`** and **`A = O /\ \l = 0`**
>
> > **proof** let **`A = I /\ \l = 1 /\ E_1 = x`**. we then have **`O = A . \lI | x = I . 1I | E_1 = O | E_1`**. therefore, **`E_1 = RR^2`**. see [[eigen]]

> **example** let **`MM^n,n A /\ NN n`** and suppose **`A`** has **`n`** distinct [[eigen#value]]s. deduce that **`A`** is diagonalizable over the reals
>
> > **proof** **`A`** has at most **`n`** [[eigen#value]]s &rarr; the algebraic [[eigen#multiplicity]] of every [[eigen#value]] of **`A`** is **`1`** as they are all distinct and must be greater than **`1`** &rarr; the geometric [[eigen#multiplicity]] of every [[eigen#value]] of **`A`** is **`1`** as it must be greater than **`1`** and less than its algebraic [[eigen#multiplicity]] &rarr; all algebraic [[eigen#multiplicity]]es and geometric [[eigen#multiplicity]]es are equal &rarr; **`A`** is diagonalizable. see [[eigen]]

## theorems

**see** [[linear system]]

**theorem**

let **`MM^m,n A`**. the following [[logic statement]]s are equivalent:

- every [[variable]] is a leading [[variable]]
- there is a leading [[variable]] in every column of the [[linear system#reduced row echelon form]] of **`A`**
- the system **`Ax = O`** has a unique solution
- the columns of **`A`** are [[linearly independent]]
- **`nn A = {{O}}`**
- **`"dim" nn A = 0`**
- **`"rank" A = n`**

**see** [[linear system theorem proof]]

**theorem**

let **`MM^n,n A`** (see [[matrix]]). the following [[logic statement]]s are equivalent:

> **note** all [[logic statement]]s below are valid for both **`A`** and **`\r A`**, see [[matrix#transpose]]

> **note** thinking of [[matrix]]es as [[linear transformation]]s makes the following [[logic statement]]s easier to understand intuitively

- **`"rank" A = n`**
- every [[linear system]] of the form **`Ax = b`** has a unique solution
- the [[linear system#reduced row echelon form]] of **`A`** is the [[matrix#identity matrix]]
- **`nn A = {{O}}`**
- **`cc A = RR^n`**
- **`rr A = RR^n`**
- the columns of **`A`** are [[linearly independent]]
- the rows of **`A`** are [[linearly independent]]
- the columns of **`A`** form a [[basis]] for **`RR^n`**
- the rows of **`A`** form a [[basis]] for **`RR^n`**
- **`A`** is an invertible [[matrix]]
- **`"det" A + 0`**, see [[determinant]]
