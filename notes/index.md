# Index

files below are based on [[conceptual note-taking]], a system in which atomic notes are structured through links from and to other notes. see [[adt organization]] for more information

![[Pasted image 20221128125505.png]]

[[tags]]

[[conventions]]

## Launchpad

[[categories]]

[[fields]]

[[random]]

## Worth Reading

[[math notation]] and related notes

[[functional programming]] and related notes

[[conceptual note-taking]] and related notes

[[pure mathematics]] and related notes

[[productivity]] and related notes

---

#xxx logic

#xxx during rewatch, make sure to define what a model is

_models_ (assignment of truth values to symbols)
_resolution_ is an inference rule that is both sound and complete
a clause is a disjunction of a bunch of literals (literals are symbol and ¬symbol) --- <https://youtu.be/egLAF4dFdBo?t=326>

| formulas allowed                           | inference rule | soundness | completeness |
| ------------------------------------------ | -------------- | --------- | ------------ |
| propositional logic                        | modus ponens   | yes       | no           |
| propositional logic with only Horn clauses | modus ponens   | yes       | yes          |
| propositional logic                        | resolution     | yes       | yes          |

--- <https://youtu.be/egLAF4dFdBo?t=92>

#xxx src for unification and substitution (_how GHC's type inference engine actually works_ by Simon Peyton Jones): <https://youtu.be/-TJGhGa04F8>. probably want to cross-reference with `learn hindley-milner.md` in calendar and with <https://terramorpha.github.io/blog.Sequent.html>

---

[[propositional logic]]

#xxx [[first-order logic]]

[[inference rule]]

[[natural deduction]]
