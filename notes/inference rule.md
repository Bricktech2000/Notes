# Inference Rule

**see** [[axiom]]

--- <https://en.wikipedia.org/wiki/Natural_deduction#Notation>

**notation** _entailment (semantic consequence)_ $\Gamma \vDash f$

**notation** _derivability (syntactic consequence)_ $\Gamma \vdash f$

the _inference line_ $\displaystyle \frac \quad \quad$, separating the _premises_ and the _conclusion_, also denotes syntactic consequence

a key idea is that [[inference rule]]s operate solely on syntax, with no concern to semantics --- <https://youtu.be/RIk67yGMVv4?t=349> and <https://youtu.be/xL0kNw5TudI?t=3161>. _soundness_ and _completeness_ are what anchors [[inference rule]]s in semantics --- <https://youtu.be/_Iz83hfkFds?t=696>:

**definition** a set of [[inference rule]]s is _sound_ "nothing but the truth" if and only if any formula _derivable_ using the [[inference rule]]s is _entailed_ by a knowledge base: $\forall \Gamma.\ \forall f.\ (\Gamma \vDash f) \gets (\Gamma \vdash f)$ --- <https://youtu.be/RIk67yGMVv4?t=838> and <https://youtu.be/xL0kNw5TudI?t=3514>

**definition** a set of [[inference rule]]s is _complete_ "the whole truth" if and only if any formula _entailed_ by a knowledge base is _derivable_ using the [[inference rule]]s: $\forall \Gamma.\ \forall f.\ (\Gamma \vDash f) \to (\Gamma \vdash f)$ --- <https://youtu.be/RIk67yGMVv4?t=909> and <https://youtu.be/xL0kNw5TudI?t=3539>

> **example** _some inference rules of classical logic_ --- <https://terramorpha.github.io/blog.Sequent.html>
>
> _hypothesis_ $\displaystyle \frac{\Gamma \ni P}{\Gamma \vdash P}$
>
> _$\top$-introduction_ $\displaystyle \frac{}{\Gamma \vdash \top}$
>
> _$\bot$-elimination_ $\displaystyle \frac{\Gamma \vdash \bot}{\Gamma \vdash P}$
>
> _$\lor$-introduction_ $\displaystyle \frac{\Gamma \vdash P}{\Gamma \vdash P \lor Q} \quad \frac{\Gamma \vdash Q}{\Gamma \vdash P \lor Q}$
>
> _$\lor$-elimination_ $\displaystyle \frac{\Gamma \vdash P \lor Q \quad \Gamma, P \vdash R \quad \Gamma, Q \vdash R}{\Gamma \vdash R}$
>
> _$\land$-introduction_ $\displaystyle \frac{\Gamma \vdash P \quad \Gamma \vdash Q}{\Gamma \vdash P \land Q}$
>
> _$\land$-elimination_ $\displaystyle \frac{\Gamma \vdash P \land Q \quad \Gamma, P, Q \vdash R}{\Gamma \vdash R}$
>
> _explosion_ $\displaystyle \frac{\Gamma \vdash P \quad \Gamma \vdash \lnot P}{\Gamma \vdash \bot}$
>
> _excluded middle_ $\displaystyle \frac{}{\Gamma \vdash P \lor \lnot P}$
