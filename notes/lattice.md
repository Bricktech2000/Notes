# Lattice

**see** [[algebraic structure]], [[semilattice]]

--- Wikipedia

**definition** a _lattice_ is a [[partial order]]ed [[set]] in which every pair of elements has a unqiue [[supremum]] and [[infimum]]

**definition** a _lattice_ is a [[partial order]]ed [[set]] that is both a _join-[[semilattice]]_ and a _meet-[[semilattice]]_

**definition** a _lattice_ is a [[set]] of elements equipped with two closed, commutative, associative binary [[operator]]s $\vee$ _join_ and $\wedge$ _meet_ that satisfy $a \vee (b \wedge a) = a \wedge (b \vee a) = a$ for all elements $a, b$

**definition** a _lattice_ is a [[set]] $L$ equipped with two binary [[operator]]s $\vee$ _join_ and $\wedge$ _meet_ that satisfy the following [[axiom]]s for all $a, b, c \in L$:

_associativity_ $(a \vee b) \vee c = a \vee (b \vee c)$; $(a \wedge b) \wedge c = a \wedge (b \wedge c)$

_commutativity_ $a \vee b = b \vee a$; $a \wedge b = b \wedge a$

_absorption_ $a \vee (b \wedge a) = a$; $a \wedge (b \vee a) = a$

_closure_ $a \vee b \in L$; $a \wedge b \in L$

**properties** _follow from the [[axiom]]s_

_idempotence_ $a \vee a = a$; $a \wedge a = a$

## Distributive Lattice

--- <https://en.wikipedia.org/wiki/Lattice_(order)#Distributivity>

--- <https://en.wikipedia.org/wiki/Distributive_lattice>

**definition** a _distributive lattice_ is a [[lattice]] whose _join_ and _meet_ distribute over eachother

**definition** a _distributive lattice_ is a [[lattice]] that satisfies $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$---or, equivalently, $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$---for all elements $a, b, c$

## Bounded Lattice

--- <https://en.wikipedia.org/wiki/Lattice_(order)#Bounded_lattice>

**definition** a [[lattice]] is called _bounded_ if it has a _maximum_ (_greatest element_, _top element_) $\top$ and a _minimum_ (_least element_, _bottom element_) $\bot$

**definition** a [[lattice]] is called _bounded_ if it has two _identity elements_ $\top$ and $\bot$ that satisfy $\bot \leq a \leq \top$ for all elements $a$

**definition** a [[lattice]] is called _bounded_ if it has two _identity elements_ $\top$ and $\bot$ that satisfy $a \vee \bot = a \wedge \top = a$ for all elements $a$

every [[lattice]] can be bounded by adding a greatest and least element

every non-empty finite [[lattice]] $L$ is bounded because $\top = \vee L$ and $\bot = \wedge L$

### Complemented Lattice

--- <https://en.wikipedia.org/wiki/Complemented_lattice>

**definition** a [[lattice#bounded lattice]] is called _complemented_ if every element $a$ has a _complement_ $\neg a$ that satisfies $a \vee \neg a = \top$ and $a \wedge \neg a = \bot$
