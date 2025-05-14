# First-Order Logic

**aka** _predicate logic_, _predicate calculus_

**see** [[inference rule]], [[propositional logic]], [[unification]], [[substitution]]

--- <https://www.youtube.com/watch?v=Z-O0Q3_oTJM&list=PLh7QmcIRQB-uiOS4GMlBbq0jkvtqhqtq0&index=7> and <https://youtu.be/_Iz83hfkFds?t=2403>

first-order logic is [[propositional logic]] extended with [[quantifier]]s, [[function]]s and [[predicate]]s

**definition** a _formula_ $\varphi$ is _predicate symbols_ ($\mathrm{Likes}(\dots)$, $\mathrm{Equals}(\dots)$) applied to _terms_---consisting of _constant symbols_ ($\mathrm{Alice}$, $3$), _variables_ ($x$, $y$) and _function symbols_ on terms ($\mathrm{FatherOf}(\dots)$, $\mathrm{Sum}(\dots)$)---connected by _logical connectives_ ([[boolean#operators]]) and bound by _quantifiers_ ($\forall x.$, $\exists y.$)

**definition** a _model_ $\mathcal M\ f$ of a formula $f$ consists of: --- [[6806f437-8a00-8008-9e60-d2402c0fbcd8]]

- a _domain_ or _universe_ $D$ that serves as the range of quantification for the variables
- a mapping of _constant symbols_ to elements of $D$
- a mapping of $n$-ary _function symbols_ to elements of $D^n \to D$ ($n$-ary [[function]]s on $D$)
- a mapping of $n$-ary _predicate symbols_ to elements of $\mathcal P\ D^n$ ($n$-ary [[relation]]s on $D$)

**definition** a _knowledge base_ $\Gamma$ is [[set]] of formulas taken to be true, onto which [[inference rule]]s operate

## Decidability

--- <https://youtu.be/mndzhfBpyUw?t=818> and <https://youtu.be/_Iz83hfkFds?t=4022>

[[first-order logic]], even when restricted to Horn clauses, is _semi-decideable_: if $\Gamma \vDash f$, forward inference will prove $f$ in finite time, but if $\Gamma \not \vDash f$, in general, no algorithm can show this in finite time

## Propositionalization

--- <https://youtu.be/Z-O0Q3_oTJM?t=1328> and <https://youtu.be/_Iz83hfkFds?t=3197> (they say _constant symbol <=> object_ but I'm pretty sure they mean _term <=> object_)

if we can come up with a one-to-one mapping between the _terms_ of a [[first-order logic]] language and elements of a _domain_ $D$, then the [[first-order logic]] language reduces to a [[propositional logic]] language, by the process of _propositionalization_

> **example** --- <https://youtu.be/Z-O0Q3_oTJM?t=1530> and <https://youtu.be/_Iz83hfkFds?t=3312>
>
> the [[first-order logic]] knowledge base:
>
> - $\mathrm{Student}(\mathrm{Alice}) \land \mathrm{Student}(\mathrm{Bob})$
> - $\forall x.\ \mathrm{Student}(x) \to \mathrm{Person}(x)$
> - $\exists x.\ \mathrm{Student}(x) \land \mathrm{Creative}(x)$
>
> reduces to the [[propositional logic]] knowledge base:
>
> - $\mathrm{StudentAlice} \land \mathrm{StudentBob}$
> - $(\mathrm{StudentAlice} \to \mathrm{PersonAlice}) \land (\mathrm{StudentBob} \to \mathrm{PersonBob})$
> - $(\mathrm{StudentAlice} \land \mathrm{CreativeAlice}) \lor (\mathrm{StudentBob} \land \mathrm{CreativeBob})$

## Modus Ponens

_a generalization of [[propositional logic#modus ponens]]_

the _modus ponens_ [[inference rule]] for [[first-order logic]] $\displaystyle \frac{p' \quad p \to q}{q\theta}$ where $\theta$ is the [[unification]] of $p'$ with $p$---or, more generally, $\displaystyle\frac{p'_0 \quad \cdots p'_k \quad p_0 \land \cdots p_k \to q}{q\theta}$ where $\theta$ is the [[unification]] of $p'_0 \land \cdots p'_k$ with $p_0 \land \cdots p_k$---, and where all variables are implicitly universally quantified, is _sound_ but is not _complete_ --- <https://youtu.be/mndzhfBpyUw?t=631> and <https://youtu.be/_Iz83hfkFds?t=3784>

> **note** [[first-order logic#modus ponens]] can be made complete by restricting our formulas to _Horn clauses_

> **note** repeatedly applying [[first-order logic#modus ponens]] may never converge, because of [[first-order logic#decidability]]

## Resolution

_a generalization of [[propositional logic#resolution]]_

the _resolution_ [[inference rule]] for [[first-order logic]] $\displaystyle \frac{p' \lor f \quad \lnot p \lor g}{(f \lor g)\theta}$ where $\theta$ is the [[unification]] of $p'$ with $p$---or, more generally, $\displaystyle\frac{p' \lor f_0 \lor \cdots f_k \quad \lnot p \lor g_0 \lor \cdots g_k}{(f_0 \lor \cdots f_k \lor g_0 \lor \cdots g_k)\theta}$ where $\theta$ is the [[unification]] of $p'$ with $p$---, and where all variables are implicitly universally quantified, is both _sound_ and _complete_ --- <https://youtu.be/iG_tz7ZjZAI?t=494> and <https://youtu.be/_Iz83hfkFds?t=4547>

> **procedure** _resolution-based inference for [[first-order logic]]_ --- <https://youtu.be/iG_tz7ZjZAI?t=25> and <https://youtu.be/_Iz83hfkFds?t=4165> and
>
> 1. add the [[boolean#negation]] of the conclusion into the knowledge base
> 2. rename bound variables so no two [[quantifier]]s within a formula bind the same name (_standardization_)
> 3. move [[quantifier]]s to the front of all formulas (conversion to _prenex normal form_)
> 4. replace existentially-quantified variables by functions of their universally-quantified dependencies, dropping the existential [[quantifier]]s (_skolemization_)
> 5. drop universal [[quantifier]]s; free variables are now implicitly universally quantified
> 6. convert all formulas to [[conjunctive normal form]]
> 7. collect the disjunctive terms into a new knowledge base
> 8. repeatedly apply [[first-order logic#resolution]]:
>    - if the empty clause $\bot$ is derived, return entailment
>    - otherwise, if resolution has converged, return non-entailment
>    - otherwise, continue
>
> _skolemization_ is a noteworthy step. it eliminates existential [[quantifier]]s by introducing _skolem functions_ and _skolem constants_ ($0$-ary skolem functions). it doesn't preserve _logical equivalence_---just because it changes the form of formulas and thus models aren't directly compatible---but it does preserve _satisfiability_---because it moves all existential [[quantifier]]s outwards using the [[second-order logic]] equivalence $\forall x.\ \exists y.\ R\ x\ y \iff \exists Y.\ \forall x.\ R\ x\ (Y\ x)$, and satisfiability is implicitly existentially quantified over models and thus over functions --- me and <https://en.wikipedia.org/wiki/Skolem_normal_form#How_Skolemization_works> and [[680fd401-c864-8008-adf4-f8d950bf01d9]]

> **example** _resolution-based inference for [[first-order logic]]_ --- [[cs188_sp93_f_sol.pdf]], problem 2 --- <https://hkn.eecs.berkeley.edu/examfiles/cs188_sp93_f_sol.pdf>

> **note** repeatedly applying [[first-order logic#resolution]] may never converge, because of [[first-order logic#decidability]]
