# Zipper

**see** [[functional programming]]

> **resource** _The Zipper_ (Gérard Huet, 1997) --- [[../references/The_Zipper.pdf]] --- <https://www.researchgate.net/publication/220676535_The_Zipper>

> **resource** _The Derivative of a Regular Type is its Type of One-Hole Contexts_ (Conor McBride, 2001) --- [[../references/diff.pdf]] --- <http://strictlypositive.org/diff.pdf>. ($3.2 'Examples of Derivatives' has a typo in the reduction of $\partial_x\ \mathbf{list}\ x$: on the third line the weakening shouldn't extend under $\times z$. $3.5 'Subterms and Derivatives' has a typo in **Theorem** (subtree): there should be a $t$ on the right-hand side of $u \leq_{\mu x{.}F}$)

**definition** the _derivative_ of a [[type]] is its [[type]] of one-hole contexts: the _derivative_ $\partial_xT$ of $T$ with respect to $x$ is the [[type]] of terms that look like terms of $T$ but have one hole somewhere an $x$ would normally go

and in particular we can always write a [[function]] $\partial_xT \times x \to T$ that plugs $\partial_xT$'s hole using an $x$. the construction is in Figure 5.

> **examples**
>
> - $\partial_x(x + x) = \mathbf 2$---whether the hole is in $\mathrm{inl}$ or $\mathrm{inr}$
> - $\partial_x(x \times x) = \mathbf 2 \times x$---whether the hole is in $\mathrm{fst}$ or $\mathrm{snd}$ along with the other component
> - $\partial_x(\mu y.\ \mathbf 1 + x \times y) = \partial_x\ \mathbf{list}\ x = \mathbf{list}\ x \times \mathbf{list}\ x$---the prefix and suffix
> - $\partial_x(\mu y.\ x + y \times y) = \partial_x\ \mathbf{tree}\ x = \mathbf{list}\ (\mathbf 2 \times \mathbf{tree}\ x)$---the path from the root equipped with the off-path subtrees

**definition** the [[zipper]] _path_ for a recursive [[type]] is the derivative of the [[monad#free monad]] over its [[functor#base functor]] at zero, what's the problem?

> **proof** (refer to the differentiation rules in Figure 4)
>
> the derivative of `Free f a` with respect to `a` is:
>
> $$
> \begin{align}
>    &\partial_a(\mathbf{free}_x\ F\ a) \qquad \text{\(x\) is free in \(F\)} \\
> =\ &\partial_a(\mu x.\ a + \underline F_a) \\
> =\ &\mu z.\ \underline{\partial_a(a + \underline F_a)|x{=}(\mathbf{free}_x\ F\ a)}_z + \underline{\partial_x(a + \underline F_a)|x{=}(\mathbf{free}_x\ F\ a)}_z \times z \\
> =\ &\mu z.\ \underline{(\mathbf 1 + \mathbf 0)|x{=}(\mathbf{free}_x\ F\ a)}_z + \underline{(\mathbf 0 + \partial_x \underline F_a)|x{=}(\mathbf{free}_x\ F\ a)}_z \times z \\
> =\ &\mu z.\ \mathbf 1 + \underline{\partial_x \underline F_a|x{=}(\mathbf{free}_x\ F\ a)}_z \times z \\
> =\ &\mathbf{list}\ \partial_x \underline F_a|x{=}(\mathbf{free}_x\ F\ a) \\
> \end{align}
> $$
>
> taking the derivative at `a ~ Void`:
>
> $$
> \begin{align}
>    &\partial_a(\mathbf{free}_x\ F\ a)|a{=}\mathbf 0 \\
> =\ &\big(\mathbf{list}\ \partial_x \underline F_a|x{=}(\mathbf{free}_x\ F\ a)\big)|a{=}\mathbf 0 \\
> =\ &\mathbf{list}\ \partial_x F|x{=}(\mu x.\ \mathbf 0 + F) \\
> =\ &\mathbf{list}\ \partial_x F|x{=}\mu x{.}F \\
> =\ &\mathbf{sub}\ \mu x{.}F \qquad \text{the zipper path for \(\mu x{.}F\)} \\
> \end{align}
> $$
>
> so the [[zipper]] path for `Fix f` is the derivative of `Free f a` with respect to `a` at `a ~ Void`. this makes sense: the [[monad#free monad]] over `f` is a `Fix f` but with holes `a` where a subtree would normally go, so differentiating with respect to `a` distinguishes one of the holes, and setting `a ~ Void` plugs all other holes. the result is a `Fix f` but with a single hole of type `Fix f`---that's a [[zipper]] path

**definition** the _zipper_ for a recursive [[type]] is the derivative of the cofree co[[monad]] over its [[functor#base functor]] at one, what's the problem?

> **proof** (refer to the differentiation rules in Figure 4. for why $\partial \nu$ gives $\mu$ and for why the $\cong$ holds, see the end of $3.1 'Partial Differentiation')
>
> the derivative of `Cofree f a` with respect to `a` is:
>
> $$
> \begin{align}
>    &\partial_a(\mathbf{cofree}_x\ F\ a) \qquad \text{\(x\) is free in \(F\)} \\
> =\ &\partial_a(\nu x.\ a \times \underline F_a) \\
> =\ &\partial_a((a \times \underline F_a)|x{=}(\mathbf{cofree}_x\ F\ a)) \\
> =\ &\partial_a (a \times \underline F_a)|x{=}(\mathbf{cofree}_x\ F\ a)) + \partial_x (a \times \underline F_a)|x{=}(\mathbf{cofree}_x\ F\ a) \times \partial_a(\mathbf{cofree}_x\ F\ a) \\
> =\ &\mu z.\ \underline{\partial_a (a \times \underline F_a)|x{=}(\mathbf{cofree}_x\ F\ a))}_z + \underline{\partial_x (a \times \underline F_a)|x{=}(\mathbf{cofree}_x\ F\ a)}_z \times z \\
> =\ &\mu z.\ \underline{(\mathbf 1 \times \underline F_a + a \times \mathbf 0)|x{=}(\mathbf{cofree}_x\ F\ a)}_z + \underline{(\mathbf 0 \times \underline F_a + a \times \partial_x \underline F_a)|x{=}(\mathbf{cofree}_x\ F\ a)}_z \times z \\
> =\ &\mu z.\ \underline{\underline F_a|x{=}(\mathbf{cofree}_x\ F\ a)}_z + \underline{a \times \partial_x \underline F_a|x{=}(\mathbf{cofree}_x\ F\ a)}_z \times z \\
> \cong\ &\underline F_a|x{=}(\mathbf{cofree}_x\ F\ a) \times \mu z.\ \mathbf 1 + \underline{a \times \partial_x \underline F_a|x{=}(\mathbf{cofree}_x\ F\ a)}_z \times z \\
> =\ &\underline F_a|x{=}(\mathbf{cofree}_x\ F\ a) \times \mathbf{list}\ (a \times \partial_x \underline F_a|x{=}(\mathbf{cofree}_x\ F\ a)) \\
> \end{align}
> $$
>
> taking the derivative at `a ~ Unit`:
>
> $$
> \begin{align}
>    &\partial_a(\mathbf{cofree}_x\ F\ a)|a{=}\mathbf 1 \\
> =\ &\big(\underline F_a|x{=}(\mathbf{cofree}_x\ F\ a) \times \mathbf{list}\ (a \times \partial_x \underline F_a|x{=}(\mathbf{cofree}_x\ F\ a))\big)|a{=}\mathbf 1 \\
> =\ &F|x{=}(\nu x.\ \mathbf 1 \times F) \times \mathbf{list}\ (\mathbf 1 \times \partial_x F|x{=}(\nu x.\ \mathbf 1 \times F)) \\
> =\ &\nu x{.}F \times \mathbf{list}\ \partial_x F|x{=}\nu x{.}F \\
> =\ &\nu x{.}F \times \mathbf{sub}\ \nu x{.}F \qquad \text{the zipper for \(\nu x{.}F\)}\\
> \end{align}
> $$
>
> the same holds for $\mu$ in place of $\nu$. namely, $\partial_a(\mu x.\ a \times \underline F_a)|a{=}\mathbf 1\ =\ \mu x{.}F \times \mathbf{sub}\ \mu x{.}F$
>
> so the [[zipper]] for `Fix f` is the derivative of `Cofree f a` with respect to `a` at `a ~ Unit`. this makes sense: the cofree co[[monad]] over `f` is a `Fix f` but with annotations `a` on each subtree, so differentiating with respect to `a` distinguishes one of the annotations, and setting `a ~ Unit` plugs all other annotations. the result is a `Fix f` but with a focus on a subtree---that's a [[zipper]].

and in particular we can always write a [[function]] $\mathbf{sub}\ \mu x{.}F \times \mu x{.}F \to \mu x{.}F$ that plugs $\mathbf{sub}\ \mu x{.}F$'s hole using a $\mu x{.}F$. the construction is in $3.4 'Subtrees in Recursive Regular Types'.

## ---

--- [[../references/Semantic Domain_ Five (and a Half) Derivatives in Language Theory.pdf]] --- <https://semantic-domain.blogspot.com/2021/02/five-and-half-derivatives-in-language.html>

--- [[../references/ddc06107-b6ab-4f8d-b040-93235676c5e2.md]]
