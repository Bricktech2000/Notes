# Disjunctive Normal Form

see [[conjunctive-normal-form]]

> **AKA**: DNF, SoP

## definition

a compound proposition is said to be in DNF if it is a disjunction of conjunctive clauses (see [[boolean-operator]]s)

## [[boolean]] expression to [[disjunctive-normal-form]]

1. build a [[truth-table]] using the [[boolean]] expression
2. write a conjunctive clause (see [[boolean-operator]]s) for each $\top$ row of the [[truth-table]]
3. join the conjunctive clauses (see [[boolean-operator]]s) using disjunctions (see [[boolean-operator]]s)

## Standard Sum of Products

[[iti1100-a-digital-systems-i]] equivalent of a [[disjunctive-normal-form]]. the conjunctive clauses are known as _Minterms_

Sums of Products can be used to easily convert a [[boolean]] expression to only NOR [[gate]]s by double-negating the [[boolean]] expression and distributing one of the negations. note that $\lnot A =\lnot (A \lor A)$, see [[boolean-operator]]s
