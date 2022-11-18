# Category Theory

**see** [[category]]

> "[[category theory]] is to programming what chemistry is to baking" &mdash; <https://youtu.be/SmXB2K_5lcA?t=414>

there appears to be a standard way to build contexts in which we do [[mathematics]]. [[category theory]] is all about formalizing this observation

> **examples** _mathematical contexts_
>
> - [[linear algebra]]
> - [[group theory]]
> - [[category theory]]
> - [[set theory]]
> - [[topology]]
> - [[type theory]]
> - [[lambda calculus]]
> - [[logic]]

---

[[function]]s and [[type]]s can be viewed as morphisms and objects in a [[category theory]] context

the [[empty]] [[set]] corresponds to the [[type]] `Void` in Haskell, which corresponds to $\bot$ in [[logic]] from a [[category theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. $\bot$ cannot be proven, similarly to how a [[function]] that takes `Void` as a parameter cannot be called

the singleton [[set]] corresponds to the [[type]] `()` (or `Unit`) in Haskell, which corresponds to $\top$ in [[logic]] from a [[category theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. $\top$ can be proven, similarly to how a [[function]] that takes `Unit` as a parameter can be called

a [[relation]] being reflexive is equivalent to the presence of identity morphisms in [[category theory]]

a [[category]] with exactly one object is a [[monoid]] (yes, that [[monoid]] from [[functional programming]])

the [[category]] of [[type]]s is equivalent to a strongly typed [[programming language]], as [[function]]s in such a language are only composable if their [[type]]s match

the terminal object of a [[category]] corresponds to the singleton [[set]] and the initial object of a [[category]] corresponds to the [[empty]] [[set]]

_co..._ refers to the same object in the opposite [[category]]. product & coproduct, monad & comonad, monoid & comonoid...

---

#todo to learn:

bottom types in haskell &mdash; <https://youtu.be/p54Hd7AmVFU>

pre order, partial order, total order, and how epi + mono != iso &mdash; <https://youtu.be/aZjhqkD6k6w>

Kleisli category <https://youtu.be/i9CU4CuHADQ>

thin / thick categories

absurd function

universal construction:

> A _product_ of two objects $a$ and $b$ is the object $c$ equipped with two projections such that for any other object $c'$ equipped with two projections there is a unique morphism $m$ from $c'$ to $c$ that factorizes those projections.

&mdash; <https://miklos-martin.github.io/learn/fp/category-theory/2018/02/01/adventures-in-category-theory-the-algebra-of-types.html>

factorizes &mdash; <https://youtu.be/Bsdl_NKbNnU?t=1011>

the _curry-howard-lambek isomorphism_ states that [[logic]], [[type theory]] and some subset of [[category theory]] are all equivalent &mdash; <https://youtu.be/I8LbkfSSR58?t=1681>

> **AKA** #todo curry-howard correspondence, propositions as types #todo #think see <https://youtu.be/IOiZatlZtGU?t=1490>

products in the category of [[set]]s are [[cartesian product]]s &mdash; Terramorpha

coproducts in the category of [[set]]s are disjoint unions &mdash; Terramorpha

products in the category of $\mathbb R, \le$ are the minimum of two numbers &mdash; Terramorpha

coproducts in the category of $\mathbb R, \le$ are the maximum of two numbers &mdash; Terramorpha

products in the category of $\mathbb N, \text{divides}$ are the GCD of two numbers, see [[psi function in mat2348]] &mdash; Terramorpha

coproducts in the category of $\mathbb N, \text{divides}$ are the LCM of two numbers, see [[psi function in mat2348]] &mdash; Terramorpha

products in the category of $\braket{\ }, \vdash$ are the intersection of two sets &mdash; Terramorpha

coproducts in the category of $\braket{\ }, \vdash$ are the union of two sets &mdash; Terramorpha

#think <https://youtu.be/IOiZatlZtGU?t=2334>

#think <https://youtu.be/gui_SE8rJUM?t=605> from timestamp to #todo

exponintials are functions &mdash; <https://youtu.be/gui_SE8rJUM?t=1950>

system F (polymorphism) and system Fω (constructor on types) &mdash; <https://youtu.be/gui_SE8rJUM?t=2074>

duals are DeMorgan's laws in category theory &mdash; <https://youtu.be/gui_SE8rJUM?t=2176>

exponential laws in category theory &mdash; <https://youtu.be/gui_SE8rJUM?t=2379>

proper category and functor definitions &mdash; <https://youtu.be/H0Ek86IH-3Y>
