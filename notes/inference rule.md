# Inference Rule

**see** [[axiom]]

--- <https://en.wikipedia.org/wiki/Natural_deduction#Notation>

**notation** _entailment (semantic consequence)_ $\Gamma \vDash f$

**notation** _derivability (syntactic consequence)_ $\Gamma \vdash f$

the _inference line_ $\displaystyle \frac \quad \quad$ also denotes syntactic consequence

a key idea is that [[inference rule]]s operate solely on syntax, with no concern to semantics --- <https://youtu.be/RIk67yGMVv4?t=349> and <https://youtu.be/xL0kNw5TudI?t=3161>

**definition** a set of [[inference rule]]s is _sound_ "nothing but the truth" if and only if any formula _derivable_ using the [[inference rule]]s is _entailed_ by a knowledge base: $\Gamma.\ \forall f.\ (\Gamma \vDash f) \gets (\Gamma \vdash f)$ --- <https://youtu.be/RIk67yGMVv4?t=838> and <https://youtu.be/xL0kNw5TudI?t=3514>

**definition** a set of [[inference rule]]s is _complete_ "the whole truth" if and only if any formula _entailed_ by a knowledge base is _derivable_ using the [[inference rule]]s: $\Gamma.\ \forall f.\ (\Gamma \vDash f) \to (\Gamma \vdash f)$ --- <https://youtu.be/RIk67yGMVv4?t=909> and <https://youtu.be/xL0kNw5TudI?t=3539>
