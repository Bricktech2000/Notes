# Basis

_[[vector space]] basis_

**see** [[vector]], [[vector space]]

**definition**

a [[set]] of [[vector]]s is the [[basis]] of a [[vector space]] if both:

- the [[set]] is [[linearly independent]]
- the [[set]] [[span]]s the [[vector space]]

**properties**

all [[basis]]es of a [[vector space]] have the same size

**theorems**

**theorem** let **`B`** be a [[basis]] of a [[vector space]] **`V`**. then, each [[vector]] **`v`** in **`V`** can be represented by a **unique** [[linear combination]] of the [[vector]]s in the [[basis]] **`B`**

> **procedure** _finding a [[basis]] for a [[span]]_
>
> to find a basis for a [[vector space]] **`W = "span" {{v_0 ... v_m}}`**
>
> 1. write the [[matrix]] **`A`** whose rows are the [[vector]]s **`v_0 ... v_m`**. if the [[vector]]s are not [[vector in rn]]s, translate them into coordinate vectors first
> 2. use [[row reduction]] to get **`A`** to its [[linear system#row echelon form]]
> 3. use the nonzero rows of the [[linear system#row echelon form]] of **`A`** as a [[basis]] for **`W`**

## Ordered Basis

**see** [[math notation]]

_a [[basis]] containing [[vector]]s in a specific order_

> **example**
>
> **`( (1, 0), (0, 1) )`** and **`( (0, 1), (1, 0) )`** are the same [[basis]] but different [[basis#ordered basis]]es

**definition** suppose **`B = (v_0 ... v_n)`** is a [[basis#ordered basis]] for a [[vector space]] **`V`**. suppose **`u = :av`**. then, the vector **`(a_0 ... a_n)`** is said to be the _coordinate vector_ of **`u`** relative to the ordered [[basis]] **`B`**

## Orthogonal Basis

_a [[basis]] built from a [[set]] of [[vector in rn#orthogonal vectors]]_

> **example**
>
> the [[set]] **`{{ (1, 0), (0, 1) }}`** is a [[basis#orthogonal basis]] for **`"span" {{ (1, 0), (0, 1) }}`**, but **`{{ (1, 1), (0, 1) }}`** is not

## Standard Basis

**aka** _canonical basis, natural basis_

_a [[basis]] built from a [[set]] of [[vector in rn]]s whole components are all zero except for one, which is one_

> **example**
>
> the [[set]] **`{{ (1, 0), (0, 1) }}`** is a [[basis#standard basis]] for **`"span" {{ (1, 0), (0, 1) }}`**, but **`{{ (2, 0), (0, 2) }}`** is not
