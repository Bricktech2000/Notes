# Group

_a [[set]] with extra structure_

&mdash; <https://youtu.be/KufsL2VgELo>

> a [[group]] is a [[monoid]] that also has an inverse &mdash; <https://youtu.be/p54Hd7AmVFU?t=1807>

**definition** a [[group]] is a finite or infinite [[set]] of invertible elements equipped with a closed associative binary operation and an identity element. &mdash; Wikipedia and me

**definition**

let a binary [[operator]] $:$ on a [[set]] $S$. for them to form a [[group]], the following [[axiom]]s must be satisfied:

_associativity_ $(a : b) : c = a : (b : c) \dashv S\ a \land S\ b \land S\ c$

_identity element_ $a : e = a \land S\ e \dashv S\ a$

_closure_ $S\ (a : b) \dashv S\ a \land S\ b$

_inverse element_ $a : \cdot a = e \dashv S\ a$

**definition** the _order_ of a [[group]] $G$ is the number of elements in the [[group]], denoted $\#\ G$

**notation**

_in my [[math notation]]_

the _inverse_ of $a$ is denoted $\cdot a$

the _identity_ element is denoted $e$

$a : a$ is denoted $2a$

_in [[conventional math notation]]_

the _inverse_ of $a$ is denoted $a^{-1}$

the _identity_ element is denoted $e$

$a \circ a$ is denoted $a^2$

**properties** _follow from the [[axiom]]s_

a [[group]] contains exactly one identity element

every element of a [[group]] has exactly one inverse

> **note** consequently, $\cdot a : \cdot a$ is identical to $\cdot (2a)$ which is identical to $2 (\cdot a)$, all of which can be denoted $\cdot 2a$. this is true for any coefficient

$a : e = a \dashv S\ a$ implies $e : a = a \dashv S\ a$

$a : \cdot a = e \dashv S\ a$ implies $\cdot a : a = e \dashv S\ a$

$\cdot \smash\cdot a = a$

**examples**

> **example** the following mathematical objects and binary [[operator]]s are examples of [[group]]s:
>
> - [[integer]]s and addition
> - [[real]]s excluding $0$ and multiplication
> - [[integer]]s modulo $n$ and addition

## Subgroup

#todo add subheading _subspace_ to [[vector space]]

**theorem** _Lagrange's Theorem_ let $G$ be a [[group]] and $H$ be a sub[[group]] of $G$. then, $\psi\ \#\ H \le \psi\ \#\ G$, see [[psi function in mat2348]]
