# Disjunctive Normal Form

### acronym

DNF

### definition

a compound proposition is said to be in DNF if it is a disjunction of conjunctive clauses (see [[boolean-operation]]s)

### [[boolean-expression]] to [[disjunctive-normal-form]]

1. build a [[truth-table]] using the [[boolean-expression]]
2. write a conjunctive clause (see [[boolean-operation]]s) for each $\top$ row of the [[truth-table]]
3. join the conjunctive clauses (see [[boolean-operation]]s) using disjunctions (see [[boolean-operation]]s)

## Standard Sum of Products

[[iti1100-a-digital-systems-i]] equivalent of a [[disjunctive-normal-form]]. the conjunctive clauses are known as _Minterms_

Sums of Products can be used to easily convert a boolean expression to only NOR gates by double-negating the expression and distributing one of the negations. note that $\lnot A =\lnot (A \lor A)$, see [[boolean-operation]]s

## Standard Product of Sums

[[iti1100-a-digital-systems-i]] equivalent of a [[disjunctive-normal-form]], but is a conjunction of disjunctive clauses instead of a disjunction of conjunctive clauses (see [[boolean-operation]]s). the disjunctive clauses are know as _Maxterms_

Products of Sums can be used to easily convert a boolean expression to only NAND gates by double-negating the expression and distributing one of the negations. note that $\lnot A =\lnot (A \land A)$, see [[boolean-operation]]s
