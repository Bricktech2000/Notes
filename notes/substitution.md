# Substitution

**see** [[unification]]

--- [[read6-unification.pdf]] --- <https://www.csd.uwo.ca/~mmorenom/cs2209_moreno/read/read6-unification.pdf>

a [[substitution]] replaces variables **simultaneously**

**notation** _replace $x$ by $N$ in $M$_ $M[N/x]$

**notation** _apply substution $\theta = \{\dots\}$ to $P$_ $P\theta$

**notation** _substitution literals_ $\{5/x, \mathrm{F}/y\}$, $\{x \mapsto 5, y \mapsto \mathrm{F}\}$

**notation** _empty substitution_ $\{\}$, $\varepsilon$

**notation** _composition of substitutions_ $\theta \circ \lambda$

**properties** _for all substitutions $\theta, \lambda, \mu$_

_associativity of composition_ $(\theta \circ \lambda) \circ \mu = \theta \circ (\lambda \circ \mu)$

_identity of composition_ $\varepsilon \circ \theta = \theta = \theta \circ \varepsilon$
