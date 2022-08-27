# Basis

_[[vector-space]] Basis_

see [[vector]], [[vector-space]]

### definition

a [[set]] of [[vector]]s is the [[basis]] of a [[vector-space]] if both:

- the [[set]] is [[linearly-independent]]
- the [[set]] [[span]]s the [[vector-space]]

### properties

all [[basis]]es of a [[vector-space]] have the same size

> **theorem**: let $B$ be a [[basis]] of a [[vector-space]] $V$. then, each [[vector]] $v$ in $V$ can be represented by a **unique** [[linear-combination]] of the [[vector]]s in the [[basis]] $B$

### procedure

_finding a [[basis]] for a [[span]]_

to find a basis for a vector space $W = \operatorname{span} \braket{\braket{v_0 \dots v_m}}$

1. write the [[matrix]] $A$ whose rows are the [[vector]]s $v_0 \dots v_m$. if the [[vector]]s are not [[vector-in-rn]]s, translate them into [[basis|coordinate-vector]]s first
2. [[row-reduction|row-reduce]] $A$ to [[REF]] form
3. use the nonzero rows of the [[REF]] form of $A$ as a [[basis]] for $W$

## Ordered Basis

see [[math-notation]]

_a [[basis]] containing [[vector]]s in a specific order_

### example

$(\ (1, 0), (0, 1)\ )$ and $(\ (0, 1), (1, 0)\ )$ are the same [[basis]] but different ordered bases

> **definition**: suppose $B = v_0 \dots v_n$ is an ordered [[basis]] for a [[vector-space]] $V$. suppose $v = a_0v_0 : \dots a_nv_n$. then, the vector $[a_0 \dots a_n]$ is the _coordinate vector_ of $V$ relative to the ordered [[basis]] $B$

## Orthogonal Basis

_a [[basis]] built from a [[set]] of orthogonal [[vector-in-rn]]s_

### example

the [[set]] $\braket{\braket{\ (1, 0), (0, 1)\ }}$ is an orthogonal [[basis]] for $\operatorname{span} \braket{\braket{\ (1, 0), (0, 1)\ }}$, but $\braket{\braket{\ (1, 1), (0, 1)\ }}$ is not
