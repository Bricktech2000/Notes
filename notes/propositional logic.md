# Propositional Logic

**aka** _propositional calculus_, _zeroth-order logic_

**see** [[inference rule]], [[first-order logic]]

--- <https://www.youtube.com/watch?v=oM5LUGPO7Zk&list=PLh7QmcIRQB-uiOS4GMlBbq0jkvtqhqtq0&index=2> and <https://youtu.be/xL0kNw5TudI> and <https://youtu.be/_Iz83hfkFds&t=552> until 40:03

**definition** a _formula_ $\varphi$ is _propositional symbols_ ($\mathrm{Alice}$) joined by _logical connectives_ ([[boolean#operators]])

**definition** a _model_ $\mathcal M\ f$ of a formula $f$ is a mapping of _propositional symbols_ to _truth values_ ([[boolean]]s)

**definition** a _knowledge base_ $\Gamma$ is [[set]] of formulas taken to be true, onto which [[inference rule]]s operate

## knowledge bases

when combining a formula with a knowledge base, one of three things happens. under one interpretation we can "tell" the knowledge base new things and under another we can "ask" it things:

|                                                                                             | "tell"                | "ask"           |
| ------------------------------------------------------------------------------------------- | --------------------- | --------------- |
| **entailement** $\Gamma \vDash f$ (formula already follows form knowledge base)             | already knew it       | yes that's true |
| **contradiction** $\Gamma \vDash \lnot f$ (negation of formula follows from knowledge base) | don't believe it      | no that's false |
| **contingency** (knowledge base and formula have non-trivial intersection)                  | learned something new | don't know      |

a knowledge base is _satisfiable_ if there exists a model that makes all its formulas true. entailement/contradiction/contingency can be reduced to satisfiability; we can derive them by using a pair of calls to satisfiability:

|                           | $\Gamma, \lnot f$ unsatisfiable | $\Gamma, \lnot f$ satisfiable |
| ------------------------- | ------------------------------- | ----------------------------- |
| $\Gamma, f$ unsatisfiable | ($\Gamma$ unsatisfiable)        | contradiction                 |
| $\Gamma, f$ satisfiable   | entailment                      | contingency                   |

> **note** this is nothing more than a dance of [[quantifier]]s:
>
> |                                  | $\lnot \exists (\Gamma \land \lnot f)$            | $\exists (\Gamma \land \lnot f)$                                        |
> | -------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------- |
> | $\lnot \exists (\Gamma \land f)$ | $\forall \lnot \Gamma$ aka $\lnot \exists \Gamma$ | $\forall (\Gamma \to \lnot f)$                                          |
> | $\exists (\Gamma \land f)$       | $\forall (\Gamma \to f)$                          | $\lnot \forall (\Gamma \to f) \land \lnot \forall (\Gamma \to \lnot f)$ |

## Modus Ponens

the _modus ponens_ [[inference rule]] for [[propositional logic]] $\displaystyle \frac{p \quad p \to q}{q}$---or, more generally, $\displaystyle\frac{p_0 \quad \cdots p_k \quad p_0 \land \cdots p_k \to q}{q}$---is _sound_ (because $p \land (p \to q) \to q$ is a tautology) but is not _complete_ (because given $\Gamma = \{X, X \lor Y \to Z\}$ one may not derive $Z$ even though it is entailed by the knowledge base) --- <https://youtu.be/RIk67yGMVv4?t=1232> and <https://youtu.be/xL0kNw5TudI?t=3751>

> **note** [[propositional logic#modus ponens]] can be made complete by restricting our formulas to _Horn clauses_ --- <https://youtu.be/6bj4z2mt1KE?t=247> and <https://youtu.be/xL0kNw5TudI?t=4318>

## Resolution

the _resolution_ [[inference rule]] for [[propositional logic]] $\displaystyle \frac{p \lor f \quad \lnot p \lor g}{f \lor g}$---or, more generally, $\displaystyle\frac{p \lor f_0 \lor \cdots f_k \quad \lnot p \lor g_0 \lor \cdots g_k}{f_0 \lor \cdots f_k \lor g_0 \lor \cdots g_k}$---is both _sound_ and _complete_ --- <https://youtu.be/egLAF4dFdBo?t=476> and <https://youtu.be/_Iz83hfkFds?t=1232>

> **procedure** _resolution-based inference for [[propositional logic]]_ --- <https://youtu.be/egLAF4dFdBo?t=920> and <https://youtu.be/_Iz83hfkFds?t=1899>
>
> 1. add the [[boolean#negation]] of the conclusion into the knowledge base
> 2. convert all formulas to [[conjunctive normal form]]
> 3. collect the disjunctive terms into a new knowledge base
> 4. repeatedly apply [[propositional logic#resolution]]:
>    - if the empty clause $\bot$ is derived, return entailment
>    - otherwise, if resolution has converged, return non-entailment
>    - otherwise, continue

> **note** we know $\Gamma \vDash f$ if and only if $\Gamma, \lnot f$ is unsatisfiable---a sort of "[[proof]] by contradiction". thinking in [[quantifier]]s, $\forall (\Gamma \to f) = \lnot \exists (\Gamma \land \lnot f)$. the above procedure works because, since since resolution is sound and complete, derivability and entailment coincide
