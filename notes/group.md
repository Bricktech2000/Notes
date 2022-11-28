# Group

**see** [[math notation]]

&mdash; <https://youtu.be/KufsL2VgELo>

&mdash; <https://youtu.be/mvmuCPvRoWQ>

> a [[group]] is a [[monoid]] where every element also has an inverse &mdash; <https://youtu.be/p54Hd7AmVFU?t=1807>

**definition** a [[group]] is a finite or infinite [[set]] of invertible elements equipped with a closed associative binary operation and an identity element. &mdash; Wikipedia and me

**definition**

let a binary [[operator]] $:$ on a [[set]] $G$. for them to form a [[group]], the following [[axiom]]s must be satisfied:

_associativity_ $(a : b) : c = a : (b : c) \dashv G\ a \land G\ b \land G\ c$

_identity element_ $a : O = a \land G\ O \dashv G\ a$

_closure_ $G\ (a : b) \dashv G\ a \land G\ b$

_inverse element_ $a : \cdot a = O \dashv G\ a$

**notation**

_in my [[math notation]]_

the _inverse_ of $a$ is denoted $\cdot a$

the _identity_ element is denoted $O$

$a : a$ is denoted $2a$

_in [[conventional math notation]]_

the _inverse_ of $a$ is denoted $a^{-1}$

the _identity_ element is denoted $e$

$a \circ a$ is denoted $a^2$

**properties** _follow from the [[axiom]]s_

a [[group]] contains exactly one identity element

every element of a [[group]] has exactly one inverse

> **note** consequently, $\cdot a : \cdot a$ is identical to $\cdot (2a)$ which is identical to $2 (\cdot a)$, all of which can be denoted $\cdot 2a$. this is true for any coefficient

$a : O = a \dashv G\ a$ implies $O : a = a \dashv G\ a$

$a : \cdot a = O \dashv G\ a$ implies $\cdot a : a = O \dashv G\ a$

$\cdot \smash\cdot a = a$

**examples**

> **example** the following mathematical objects and binary [[operator]]s are examples of [[group]]s:
>
> - [[integer]]s and addition
> - [[rational]]s excluding $0$ and multiplication
> - [[integer]]s modulo $n$ and addition
> - invertible square [[matrix]]es and [[matrix#multiplication]]

## Order

**definition** the _order_ of a [[group]] $G$ is the number of elements in the [[group]]

**notation** _in my [[math notation]]_ $\# G$

## Subgroup

**theorem** _Lagrange's Theorem_ let $G$ be a [[group]] and $H$ be a [[group#subgroup]] of $G$. then, $\psi\ \#\ H \le \psi\ \#\ G$ or equivanently $\psi\ \#\ \ \vdots\ \ H \le G$, see [[psi function in mat2348]]

## Abelian Group

**aka** _commutative [[group]]_

&mdash; <https://en.wikipedia.org/wiki/Abelian_group>

**definition** a [[group]] $G$ is an _abelian group_ if and only if $a : b = b : a \dashv G\ a \land G\ b$
