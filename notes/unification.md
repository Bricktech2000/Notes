# Unification

**see** [[substitution]]

--- <https://youtu.be/mndzhfBpyUw?t=412> and <https://youtu.be/_Iz83hfkFds?t=3625>

--- [[read6-unification.pdf]] --- <https://www.csd.uwo.ca/~mmorenom/cs2209_moreno/read/read6-unification.pdf>

[[unification]] is an [[algorithm]] that returns a _most general unifier_ for some [[set]] of expressions $E$, if it exists; it gives a most general [[substitution]] that makes the expressions in $E$ syntactically identical, so [[inference rule]]s may be applied

**definition** a [[substitution]] $\theta$ is called a _unifier_ for a [[set]] of expressions $E$ if $= E\theta$; a [[set]] of expressions is _unifiable_ if and only if there exists a unifier for it

**definition** a unifier $\theta$ is a _most general unifier_ for a [[set]] of expressions $E$ if and only if $\forall (= E\lambda).\ \exists \mu.\ \lambda = \theta \circ \mu$; that is, for all unifiers $\lambda$ for $E$ there exists a [[substitution]] $\mu$ such that $\lambda = \theta \circ \mu$; that is, any unifier $\lambda$ for $E$ is achievable by applying some [[substitution]] $\mu$ before applying a _most general unifier_ $\theta$
