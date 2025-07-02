# Semilattice

**see** [[algebraic structure]], [[lattice]]

--- Wikipedia

**definition** a _join-semilattice_ or _upper semilattice_ is a [[partial order]]ed [[set]] in which any pair of elements has a unique [[supremum]]

**definition** a _join-semilattice_ is a [[set]] $L$ equipped with a binary [[operator]] $\vee$ _join_ that satisfies the following [[axiom]]s for all $a, b, c \in L$:

_associativity_ $(a \vee b) \vee c = a \vee (b \vee c)$

_commutativity_ $a \vee b = b \vee a$

_[[idempotence]]_ $a \vee a = a$

_[[closure]]_ $a \vee b \in L$

**definition** a _meet-semilattice_ or _lower semilattice_ is a [[partial order]]ed [[set]] in which any pair of elements has a unique [[infimum]]

**definition** a _meet-semilattice_ is a [[set]] $L$ equipped with a binary [[operator]] $\wedge$ _meet_ that satisfies the following [[axiom]]s for all $a, b, c \in L$:

_associativity_ $(a \wedge b) \wedge c = a \wedge (b \wedge c)$

_commutativity_ $a \wedge b = b \wedge a$

_[[idempotence]]_ $a \wedge a = a$

_closure_ $a \wedge b \in L$

## Bounded Semilattice

**definition** a join-[[semilattice]] is called _bounded_ if it has an identity element $\bot$ _bottom_ that satisfies $a \vee \bot = a$ for all elements $a$

**definition** a meet-[[semilattice]] is called _bounded_ if it has an identity element $\top$ _top_ that satisfies $a \wedge \top = a$ for all elements $a$

### Complemented Semilattice

--- me and [[lattice#complemented lattice]]

**definition** a join-[[semilattice#bounded semilattice]] is called _complemented_ if every element $a$ has a _complement_ $\neg a$ that satisfies $a \vee \neg a = \top$

**definition** a meet-[[semilattice#bounded semilattice]] is called _complemented_ if every element $a$ has a _complement_ $\neg a$ that satisfies $a \wedge \neg a = \bot$
