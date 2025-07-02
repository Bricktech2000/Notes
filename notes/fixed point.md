# Fixed Point

**see** [[involution]], [[idempotence]]

**see** [[fibonacci sequence]]

**aka** _fixpoint_, _invariant point_

**definition** a value $x$ is a _fixed point_ of a [[function]] $f$ if and only if $f\ x = x$

we have `fix :: (a -> a) -> a`. by the Curry--Howard correspondence, this is saying _give me a proof that `a` implies `a` and I give you a proof of `a`_, so `fix` cannot be a [[function#total function]]. in practice, `fix` may not terminate

> **example** the [[combinator#y combinator]] and [[combinator#theta combinator]] return the [[fixed point]] of a [[lambda-calculus]] term

> **example** _functions on [[type]]s_ $\mathrm{fix}\ (x.\ x + 1) = 1 + 1 + 1 + \dots$, the [[natural]] numbers; $\mathrm{fix}\ (x.\ 1 + \mathrm{Nat} \cdot x) = 1 + \mathrm{Nat} + \mathrm{Nat}^2 + \mathrm{Nat}^3 + \dots$, the [[list]]s of $\mathrm{Nat}$s --- Justin Veilleux
