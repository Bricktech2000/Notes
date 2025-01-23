# Basis

_[[vector space]] basis_

when represented in a chosen [[basis]], [[vector]]s become isomorphic to [[euclidean vector]]s aka tuples of [[scalar]]s --- <https://youtu.be/KbyYTjfgZJI?t=28m55s>

**see** [[vector]], [[vector space]]

**definition**

a [[set]] of [[vector]]s is a [[basis]] of a [[vector space]] if both:

- the [[set]] is of [[vector#linearly independent vector]]s
- the [[set]] [[span]]s the [[vector space]]

**properties**

all [[basis]]es of a [[vector space]] have identical [[set#cardinality]]

**theorems**

**theorem** let **`B`** be a [[basis]] of a [[vector space]] **`V`**. then, each [[vector]] **`v`** in **`V`** can be represented by a **unique** [[linear combination]] of the [[vector]]s in the [[basis]] **`B`**

> **procedure** _finding a [[basis]] for a [[span]]_
>
> to find a basis for a [[vector space]] **`W = "span" V`**
>
> 1. write the [[matrix]] **`A`** whose rows are the [[vector]]s **`V`**. if the [[vector]]s are not [[euclidean vector]]s, translate them into coordinate vectors first
> 2. use [[row reduction]] to get **`A`** to its [[linear system#row echelon form]]
> 3. use the nonzero rows of the [[linear system#row echelon form]] of **`A`** as a [[basis]] for **`W`**

## Ordered Basis

**see** [[math notation]]

_a [[basis]] containing [[vector]]s in a specific order_

> **example**
>
> **`( (1, 0), (0, 1) )`** and **`( (0, 1), (1, 0) )`** are the same [[basis]] but different [[basis#ordered basis]]es

**definition** suppose **`B`** is a [[basis#ordered basis]] for a [[vector space]] **`V`**. suppose **`u = :aB`**. then, the vector **`a`** is said to be the _coordinate vector_ of **`u`** relative to the ordered [[basis]] **`B`**

## Orthogonal Basis

_a [[basis]] built from a [[set]] of [[euclidean vector#orthogonal euclidean vectors]]_

> **example**
>
> the [[set]] **`{{ (1, 0), (0, 1) }}`** is a [[basis#orthogonal basis]] for **`"span" {{ (1, 0), (0, 1) }}`**, but **`{{ (1, 1), (0, 1) }}`** is not

## Standard Basis

**aka** _canonical basis_, _natural basis_

_a [[basis]] built from a [[set]] of [[euclidean vector]]s whole components are all zero except for one, which is one_

> **example**
>
> the [[set]] **`{{ (1, 0), (0, 1) }}`** is a [[basis#standard basis]] for **`"span" {{ (1, 0), (0, 1) }}`**, but **`{{ (2, 0), (0, 2) }}`** is not
