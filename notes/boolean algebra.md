# Boolean Algebra

**see** [[boolean]], [[algebraic structure]]

**see** [[disjunctive normal form]], [[conjunctive normal form]], [[quantifier]]

**see** [[karnaugh map]], [[truth table]]

**definition** a _boolean algebra_ is a [[lattice#complemented lattice]] [[lattice#distributive lattice]] --- Wikipedia

**definition** --- Wikipedia and me

a _boolean algebra_ is a [[set]] $A$ equipped with two binary [[operator]]s $\vee$ _join_ and $\wedge$ _meet_, one unary [[operator]] $\neg$ _not_, and two _identity elements_ $\top$ _true_ and $\bot$ _false_, that satisfy the following [[axiom]]s for all $a, b, c \in A$:

_associativity_ $(a \vee b) \vee c = a \vee (b \vee c)$; $(a \wedge b) \wedge c = a \wedge (b \wedge c)$

_commutativity_ $a \vee b = b \vee a$; $a \wedge b = b \wedge a$

_absorption_ $a \vee (b \wedge a) = a$; $a \wedge (b \vee a) = a$

_identity_ $a \vee \bot = a$; $a \wedge \top = a$

_distributivity_ $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$; $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$

_excluded middle_ $a \vee \neg a = \top$; $a \wedge \neg a = \bot$

_closure_ $a \vee b \in A$; $a \wedge b \in A$; $\neg a \in A$

the simplest non-trivial [[boolean algebra]] has only two elements, $\bot$ and $\top$; its underlying [[set]] is the [[boolean]] numbers. its underlying [[partial order]] is the one given by the [[relation]] $\to$, the [[boolean#implication]]. in [[computer science]] and [[formal logic]], the _two-element boolean algebra_ is simply referred to as _boolean algebra_ --- me.
