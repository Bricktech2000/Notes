# Disjunctive Normal Form

**see** [[conjunctive normal form]]

**aka** _DNF_, _SoP_, _sum of products_

**definition** a compound proposition is said to be in _DNF_ if it is a _disjunction of conjunctive clauses_, see [[boolean algebra]]

> **procedure** _converting a [[boolean]] expression to [[disjunctive normal form]]_
>
> **see** [[boolean algebra]]
>
> 1. build a [[truth table]] using the [[boolean]] expression
> 2. write a conjunctive clause for each **`^^`** row of the [[truth table]]
> 3. join the conjunctive clauses using disjunctions

the [[disjunctive normal form]] can be used to convert a [[boolean]] expression to exclusively NOR [[logic gate]]s by double-negating the [[boolean]] expression and distributing one of the negations. note that **`>< A == >< A \/ A`**, see [[boolean algebra]]
