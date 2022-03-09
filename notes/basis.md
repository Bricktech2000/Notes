# Basis

_[[vector-space]] Basis_

see [[vector-space]], [[vector]]

### definition

a set of [[vector]]s in a [[vector-space]] if both:

- the set is [[linearly-independent]]
- the set [[span]]s the [[vector-space]]

### properties

all [[basis]]es of a [[vector-space]] have the same size

> **theorem**: let $B$ be a [[basis]] of a [[vector-space]] $V$. then, each [[vector]] $v$ in $V$ can be represented by a **unique** [[linear-combination]] of the [[vector]]s in the [[basis]] $B$

### finding a basis for a [[span]]

to find a basis for a vector space $W = span\{v_0 \dots v_m\}$

1. write the [[matrix]] $A$ whose rows are the vectors $v_0 \dots v_m$
2. row-reduce (see [[linear-system]]) $A$ to REF form (see [[linear-system]])
3. use the nonzero rows of the REF form of $A$ as a [[basis]] for $W$

## Ordered Basis

see [[math-notation]]

_a basis containing vectors in a specific order_

### example

$(1, 0), (0, 1)$ and $ (0, 1), (1, 0)$ are the same [[basis]] but different ordered bases

> suppose $B = v_0 \dots v_n$ is an ordered [[basis]] for a [[vector-space]] $V$. suppose $v = a_0v_0 \cdot \dots a_nv_n$. then, the vector $(a_0 \dots a_n)$ is the **coordinate vector** of $V$ relative to the ordered [[basis]] $B$
