# Propositional Logic

**aka** _propositional calculus_, _zeroth-order logic_

**see** [[inference rule]], [[first-order logic]]

--- <https://www.youtube.com/watch?v=oM5LUGPO7Zk&list=PLh7QmcIRQB-uiOS4GMlBbq0jkvtqhqtq0&index=2>

**definition** a _formula_ is _propositional symbols_ joined by _logical connectives_

**definition** a _knowledge base_ is set of formulas taken to be true

when combining a formula with a knowledge base, one of three things happens. under one interpretation we can "tell" the knowledge base new things and under another we can "ask" it things:

|                                                                            | "tell"                | "ask"           |
| -------------------------------------------------------------------------- | --------------------- | --------------- |
| **entailement** (formula already follows form knowledge base)              | already knew it       | yes that's true |
| **contradiction** (negation of formula follows from knowledge base)        | don't believe it      | no that's false |
| **contingency** (knowledge base and formula have non-trivial intersection) | learned something new | don't know      |

## satisfiability

a knowledge base is _satisfiable_ if there exists an assignment of truth values to propositional symbols that makes all its formulas true. entailement/contradiction/contingency can be reduced to satisfiability; we can derive them by using a pair of calls to satisfiability:

|                                   | $\Gamma \cup \{\lnot f\}$ unsatisfiable | $\Gamma \cup \{\lnot f\}$ satisfiable |
| --------------------------------- | --------------------------------------- | ------------------------------------- |
| $\Gamma \cup \{f\}$ unsatisfiable |                                         | contradiction                         |
| $\Gamma \cup \{f\}$ satisfiable   | entailment                              | contingency                           |

> **note** this is nothing more than a dance of [[quantifier]]s:
>
> |                                  | $\lnot \exists (\Gamma \land \lnot f)$            | $\exists (\Gamma \land \lnot f)$                                        |
> | -------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------- |
> | $\lnot \exists (\Gamma \land f)$ | $\forall \lnot \Gamma$ aka $\lnot \exists \Gamma$ | $\forall (\Gamma \to \lnot f)$                                          |
> | $\exists (\Gamma \land f)$       | $\forall (\Gamma \to f)$                          | $\lnot \forall (\Gamma \to f) \land \lnot \forall (\Gamma \to \lnot f)$ |

## Modus Ponens

the _modus ponens_ [[inference rule]] $\displaystyle \frac{p \quad p \to q}{q}$---or, more generally, $\displaystyle\frac{p_0 \quad \cdots p_k \quad p_0 \land \cdots p_k \to q}{q}$---is _sound_ (because $p \land (p \to q) \to q$ is a [[tautology]]) but is not _complete_ (because given $\Gamma = \{X, X \lor Y \to Z\}$ one may not derive $Z$ even though it is entailed by the knowledge base) --- <https://youtu.be/RIk67yGMVv4?t=1232>

> **note** modus ponens can be made complete by restricting our formulas to _Horn clauses_ --- <https://youtu.be/6bj4z2mt1KE?t=247>

## Resolution

the _resolution_ [[inference rule]] $\displaystyle \frac{p \lor f \quad \lnot p \lor g}{f \lor g}$---or, more generally, $\displaystyle\frac{p \lor f_0 \lor \cdots f_k \quad \lnot p \lor g_0 \lor \cdots g_k}{f_0 \lor \cdots f_k \lor g_0 \lor \cdots g_k}$--- is both _sound_ and _complete_ --- <https://youtu.be/egLAF4dFdBo?t=476>.

> **procedure** _resolution-based inference_ --- <https://youtu.be/egLAF4dFdBo?t=920>
>
> 1. add $\lnot f$ into $\Gamma$
> 2. convert all formulas to [[conjunctive normal form]]
> 3. repeatedly apply resolution until convergence
> 4. return entailment if and only if we derived the empty clause

> **note** we know a knowledge base $\Gamma$ entails a formula $f$ if and only if $\Gamma \cup \{\lnot f\}$ is unsatisfiable---a sort of "[[proof]] by [[contradiction]]". thinking in [[quantifier]]s, $\forall (\Gamma \to f) \leftrightarrow \lnot \exists (\Gamma \land \lnot f)$. the above procedure works because, since since resolution is sound and complete, derivability and entailment coincide
