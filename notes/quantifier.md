# Quantifier

**see** [[predicate]]

## Universal Quantifier

**equiv** _[[boolean#conjunction]]-reduce_

**definition** $\forall P = \land\ P$

> **note** $\forall S\ x.\ P\ x$ means $\land\ (S \to P)$

## Existential Quantifier

**equiv** _[[boolean#disjunction]]-reduce_

**definition** $\exists P = \lor\ P$

> **note** $\exists S\ x.\ P\ x$ means $\lor\ (S \land P)$

## Uniqueness Quantifier

**definition** $\exists! P = \exists P\ x.\ \forall P\ y.\ x = y$

> **note** the [[quantifier#universal quantifier]] and [[quantifier#existential quantifier]] are fundamental and work well together because they're duals. the [[quantifier#uniqueness quantifier]], on the other hand, is a whole different thing because it either assumes or defines a [[relation#equivalence relation]]. it can be a useful shorthand, but it's in no way fundamental
