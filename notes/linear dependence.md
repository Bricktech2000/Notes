# Linear Dependence

see [[linearly dependent]], [[linearly independent]], [[vector]], [[vector space]], [[linear combination]]

**definition**

let $V$ be a [[vector space]] and let $v_0 \dots v_i$ such that $V v_n \dashv \mathbb N n$

$v_0 \dots v_i$ are [[linearly independent]] if and only if $a_0v_0 : \dots a_iv_i = O\ \equiv\ a_n = O \dashv \mathbb N n$

**procedures**

> **procedure** _determining if vectors are linearly independent_
>
> to check for [[linear dependence]], one can use a homogeneous [[linear system]] and solve it using [[row reduction]]. the following can be concluded (think of this intuitively):
>
> - no solutions: not possible, as the [[linear system]] is homogeneous
> - one solution: the vectors are [[linearly independent]]
> - infinitely many solutions: the vectors are [[linearly dependent]]

**properties**

any super[[set]] of a [[linearly dependent]] [[set]] is also [[linearly dependent]]

any sub[[set]] of a [[linearly independent]] is also [[linearly independent]]

any [[set]] containing the $O$ [[vector]] is [[linearly dependent]]

**theorems**

**theorem** a set of [[vector]]s is [[linearly dependent]] if and only if at least one of its [[vector]]s can be represented as a [[linear combination]] of the others

**theorem** $W = \operatorname{span} \braket{\braket{v_0, v_1 \dots v_m}} \land \operatorname{span} \braket{\braket{v_1 \dots v_m}} \smash\leftarrow v_0 \vdash W = \operatorname{span} \braket{\braket{v_1 \dots v_m}}$ see [[span]]

**theorem** if a [[vector space]] $V$ can be spanned by $n$ [[vector]]s, then any [[linearly independent]] [[set]] in $V$ has at most $n$ [[vector]]s

**theorem** if a [[vector space]] $V$ has a sub[[set]] of $m$ [[linearly independent]] [[vector]]s, then any [[span]]ning [[set]] has at least $m$ [[vector]]s

**theorem** any [[linearly independent]] set in a [[vector space]] is smaller than or equal in length to a [[span]]ing [[set]] of the [[vector space]]

**theorem** size of any [[linearly independent]] [[set]] in $V$ $\le$ $\dim V$ $\le$ size of any [[span]]ning [[set]] in $V$
