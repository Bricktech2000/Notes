# First-Order Logic

**aka** _predicate logic_, _predicate calculus_

**see** [[inference rule]], [[propositional logic]]

--- <https://www.youtube.com/watch?v=Z-O0Q3_oTJM&list=PLh7QmcIRQB-uiOS4GMlBbq0jkvtqhqtq0&index=7>

first-order logic is [[propositional logic]] extended with [[quantifier]]s and [[predicate]]s

**definition** a _formula_ is _terms_---formed of _constants_ ($\mathrm{Alice}$), _variables_ ($x$) and _predicates_ ($\operatorname{Sum}(Alice, x)$)---connected by _logical connectives_ ([[boolean#operators]]) and bound by _quantifiers_ ($\forall x.$ $\exists y.$)

**definition** a _model_ ($w$) is an assignment of _truth values_ ([[boolean]]s) to _propositional symbols_

**definition** a _knowledge base_ ($\Gamma$) is [[set]] of formulas taken to be true

## Modus Ponens

#todo

## Resolution

#todo

#xxx good resource for resolution-based inference in FOL <https://hkn.eecs.berkeley.edu/examfiles/cs188_sp93_f_sol.pdf> (problem 2)

---

#todo

#xxx rewatch <https://youtu.be/Z-O0Q3_oTJM?si=He16JogYWyh2XqSf> (especially propositionalization, turning fol into prop logic. fol is syntax sugar. propositionalization cannot be done on all formulas --- <https://youtu.be/LYsOjtmLpPo?t=512>. resolution is sound and complete in fol --- <https://youtu.be/LYsOjtmLpPo?t=578>)

#xxx rewatch <https://youtu.be/mndzhfBpyUw?si=dPsUtLn1IaUg4LFJ> (unification takes formulas and returns a substitution. more specifically, the _most general unifier_. fol modus ponens)

#xxx rewatch <https://youtu.be/iG_tz7ZjZAI?si=nP0355Crjv59wqoS> (skolem functions are how we deal with exist (she capts them). when in CNF, all vars are forall and we drop foralls)

#xxx defn of resolution at <https://youtu.be/iG_tz7ZjZAI?t=494>
