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

**equiv** _[[linear transformation]]_

**see** [[dot product]], [[euclidean vector]]

**definition**

**`AB = :(A *)(rr B *)`**, see [[dot product]]

intuitively, matrix multiplication is the [[dot product]] of **every row** of the first [[matrix]] by **every column** of the second [[matrix]]

**properties**

**`AB + @ == MM^m,n A /\ MM^n,p B /\ MM^m,p AB`** (**`AB`** is defined if the number of columns in **`A`** is equal to the number of rows in **`B`**. their product will be an **`m`** by **`p`** [[matrix]])

_not commutative_ **`><(MM A /\ MM B < AB = BA)`**

**`><(AB = 0 < A = 0 \/ B = 0)`** (it can happen that **`AB = 0`**, but **`A + 0`** and **`B + 0`**) (**`AB`** being equal to **`0`** does not imply that **`A = 0`** or that **`B = 0`**) ([[matrix]]es have _zero divisors_ --- <https://youtu.be/V7Pl4Jdiuac?t=6m6s>)

**`><(AC = BC /\ C + 0 < A = B)`** (**`AC = BC`** and **`C + 0`** does not imply that **`A = B`**)

_associative_ **`(AB)C = A(BC)`**

_distributive_ **`A(B : C) = AB : AC`**

_distributive_ **`(B : C)A = BA : CA`**

_associative with [[scalar]]s_ **`k(AB) = (kA)B = A(kB)`**

**applications**

[[matrix#multiplication]] can be used to represent a [[linear system]] of [[linear equation]]s. matrix-vector products can be seen as yielding a [[linear combination]] of the columns of the [[matrix]]:

**`[]1 & 2 & 3 && 4 & 5 & 6[][]x && y && z[] = x[]1 && 4[] : y[] 2 && 5[] : z[]3 && 6[]`**

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

_null space_ **`NN A`**

_column space_ **`CC A`**

_row space_ **`RR A`**

**definitions**

_kernel_ **`(NN A) x == Ax = O /\ MM^m,n A /\ MM^n,1 x`**

_column space_ **`CC A = "span" {{A^*,0 , A^*,1 , ...}}`**

_row space_ **`RR A = "span" {{A^0,* , A^1,* , ...}}`**

**procedure** _computing the null space of a [[matrix]]_ use [[row reduction]]

**theorems**

the [[matrix#null space]], [[matrix#row space]] and [[matrix#column space]] of a [[matrix]] are always [[vector space]]s

**`"number of free variables in" A : "number of pivots in" A = "number of columns in" A`**

**`"dim" NN A = "number of free variables in" A`**

**`"rank" A = "number of pivots in" A`**

the nonzero rows in any [[linear system#row echelon form]] of a [[matrix]] **`A`** forms a [[basis]] for **`RR A`**. therefore, **`"dim" RR A = "rank" A`**, see [[matrix#rank]]

if **`A`** and **`B`** are row-equivalent, then **`RR A = RR B`**, see [[linear system]]

the [[span]]ning [[set]] of **`NN A`** obtained from applying [[row reduction]] on the system **`Ax = O`** is a [[basis]] for **`NN A`**

**`RR A`** does not change when applying [[linear system#elementary operation]]s on the rows of **`A`**

**properties**

**`CC A = RR (rr A) /\ RR A = CC (rr A)`**, see [[matrix#transpose]]

**applications**

[[matrix#row space]]s can be used to find a [[basis]] for a [[span]]ning [[set]] of [[vector]]s through [[row reduction]]

the [[basis]] for a [[matrix#row space]] can be found by applying [[row reduction]] and [[span]]ning the **row-reduced columns** in the [[linear system#row echelon form]] of the [[matrix]]

the [[basis]] for a [[matrix#column space]] of a [[matrix]] can be found by applying [[row reduction]] and [[span]]ning the **original columns** that became pivots in the [[linear system#row echelon form]] of the [[matrix]]

the same can be said for **`CC A`**

> **example** _transforming a [[vector space]] into the [[matrix#null space]] of a certain [[matrix]]_
>
> let **`W = "span" {{ (1, 0, 0, 1), (1, 1, 1, 0), (2, 1, .1, 1) }}`**
>
> after solving the [[linear system]], we get **`W (x, y, z, w) == .x : y : w = 0`**. therefore, **`W`** is the [[matrix#null space]] of **`A = [].1 & 1 & 0 & 1[]`**

## Diagonal

_the diagonal of a [[matrix]]_

**definition** the _diagonal_ of a square [[matrix]] goes from its top left element to its bottom right element

## Trace

**definition** the _trace_ of a square [[matrix]] is the sum of its [[matrix#diagonal]] entries

**definition** **`:{A *}`**, see [[combinator#w combinator]]

**notation** **`:{A *}`**, see [[combinator#w combinator]]

**properties**

**`:{(A:B) *} = :{A *} : :{B *}`**

## Transpose

_flips a [[matrix]] around its [[matrix#diagonal]]_

**equiv** _[[combinator#c combinator]]_

**notation** **`rr A`**

**definition** **`rr A`**

**properties**

_[[function#self-inverse function]]_ **`rr rr A = A`**

**`rr AB = rr B | rr A`** #todo mm

## Conjugate Transpose

_the [[complex#conjugate]] of every entry of the [[matrix#transpose]] of a [[matrix]]_

**aka** _Hermitian transpose_, _adjoint matrix, transjugate_

**definition**

**`"conj" rr A`**, where

- **`A`** is the [[matrix]] to find the [[matrix#conjugate transpose]] of
- **`"conj"`** is the [[complex#conjugate]] [[function]]
- **`rr`** is the [[matrix#transpose]] [[operator]]

**properties**

let a [[matrix]] of [[real]]s **`A`**. then, **`"conj" rr A = rr A`**

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
> **`Ix = x = B [].1 && 1[]`**

## Triangular Matrix

**definition** a [[matrix]] **`A`** is said to be _triangular_ if every entry below its [[matrix#diagonal]] **or** above its [[matrix#diagonal]] is **`0`**

## Diagonal Matrix

**definition** a [[matrix]] **`A`** is said to be _diagonal_ if every entry below its [[matrix#diagonal]] **and** above its [[matrix#diagonal]] is **`0`**; that is, **`m + n < A m n = 0`**

**properties**

**`[D]x`** can be computed by raising every entry of **`D`** to the power **`x`** #todo mm

## Diagonalizable Matrix

**see** [[eigen#vector]]

**definition** an **`n`** by **`n`** [[matrix]] **`A`** is said to be _diagonalizable over the reals_ if there exists a [[basis]] of **`RR^n`** consisting entirely of [[eigen#vector]]s of **`A`**

a [[matrix]] is _diagonalizable_ if and only if the geometic [[eigen#multiplicity]] of an [[eigen#value]] is equal to the algebraic [[eigen#multiplicity]] of said [[eigen#value]], for every [[eigen#value]] of the [[matrix]]

> **note** a [[matrix]] may also be diagonalizable over other [[field]]s such as the [[set]] of [[complex]] numbers **`CC`**

> **note** some [[matrix]]es do not have "enough" real [[eigen#value]]s or "enough" [[eigen#vector]]s to be diagonalizable

> **example** the [[matrix]] **`A = []1 & 2 && 2 & 1[]`** is diagonalizable over the reals as **`{{ (1, 1), (1, .1) }}`** is a [[basis]] of **`RR^2`** consisting entirely of [[eigen#vector]]s of **`A`**

> **example** the [[matrix]] **`A = []1 & 1 && 1 & 1[]`** is not diagonalizable over the reals as it does not have any real [[eigen#value]]s

> **example** the [[matrix]] **`A = []3 & 1 && 0 & 3[]`** is not diagonalizable over the reals as it only has one [[eigen#value]], and therefore only one set of [[vector#linearly dependent vector]] [[eigen#vector]]s

> **example** the [[matrix]] **`A = []1 & 0 && 0 & 1[]`** is diagonalizable over the reals as, even though **`A`** has a single [[eigen#value]] **`ll = 1`**, its [[eigen#space]] [[span]]s **`RR^2`**. this is the case for both **`A = I /\ ll = 1`** and **`A = O /\ ll = 0`**
>
> > **proof** let **`A = I /\ ll = 1 /\ E_1 = x`**. we then have **`O = A . llI | x = I . 1I | E_1 = O | E_1`**. therefore, **`E_1 = RR^2`**. see [[eigen]]

> **example** let **`MM^n,n A /\ NN n`** and suppose **`A`** has **`n`** distinct [[eigen#value]]s. deduce that **`A`** is diagonalizable over the reals
>
> > **proof** **`A`** has at most **`n`** [[eigen#value]]s -> the algebraic [[eigen#multiplicity]] of every [[eigen#value]] of **`A`** is **`1`** as they are all distinct and must be greater than **`1`** -> the geometric [[eigen#multiplicity]] of every [[eigen#value]] of **`A`** is **`1`** as it must be greater than **`1`** and less than its algebraic [[eigen#multiplicity]] -> all algebraic [[eigen#multiplicity]]es and geometric [[eigen#multiplicity]]es are equal -> **`A`** is diagonalizable. see [[eigen]]

## theorems

**see** [[linear system]]

**theorem**

let **`MM^m,n A`**. the following statements are equivalent:

- every [[variable]] is a leading [[variable]]
- there is a leading **`1`** in every column of the [[linear system#reduced row echelon form]] of **`A`**
- the system **`Ax = O`** has a unique solution
- the columns of **`A`** are [[vector#linearly independent vector]]s
- **`NN A = {{O}}`**
- **`"dim" NN A = 0`**
- **`"rank" A = n`**

> **proof** each statement in the cycle implies the next:
>
> - each column represents a [[variable]]. every [[variable]] is a leading variable -> there is a leading **`1`** in each column of the [[linear system#reduced row echelon form]] of **`A`**
> - **`Ax = O`** is homogeneous -> the [[linear system]] is consistent. no free [[variable]]s -> there cannot be infinitely many solutions -> it must have a single solution
> - **`Ax = O`** has a unique solution -> **`x = O`** -> **`A^*,j x^j : ... A^*,j x^j = O`** has a unique solution (all coefficients are **`0`**) -> the columns of **`A`** are [[vector#linearly independent vector]]s
> - the columns of **`A`** are [[vector#linearly independent vector]]s -> **`Ax = O`** has a unique solution (**`x = O`**) -> the [[matrix#null space]] of **`A`** is the [[set]] containing the zero [[vector]]
> - the [[matrix#null space]] of **`A`** is the zero space -> the [[vector space#dimension]] of the zero space is **`0`**
> - **`"dim" NN A : "rank" A = "number of columns in" A`** (see [[matrix]]) -> as **`"dim" NN A = 0`**, **`"rank" A = "number of columns in" A = n`**
> - the [[matrix#rank]] of a [[matrix]] is the number leading [[variable]]s in the matrix. **`"rank" A = n`** and **`A`** has **`n`** columns -> every [[variable]] is a leading variable

**see** [[linear system theorem proof]]

**theorem**

let **`MM^n,n A`**. the following statements are equivalent:

> **note** all statements below are valid for both **`A`** and **`rr A`**, see [[matrix#transpose]]

> **note** thinking of [[matrix]]es as [[linear transformation]]s makes the following statements extremely intuitive

- **`"rank" A = n`**
- every [[linear system]] of the form **`Ax = b`** has a unique solution
- the [[linear system#reduced row echelon form]] of **`A`** is the [[matrix#identity matrix]]
- **`NN A = {{O}}`**
- **`CC A = RR^n`**
- **`RR A = RR^n`**
- the columns of **`A`** are [[vector#linearly independent vector]]s
- the rows of **`A`** are [[vector#linearly independent vector]]s
- the columns of **`A`** form a [[basis]] for **`RR^n`**
- the rows of **`A`** form a [[basis]] for **`RR^n`**
- **`A`** is an invertible [[matrix]]
- **`"det" A + 0`**, see [[determinant]]
