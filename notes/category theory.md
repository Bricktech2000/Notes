# Category Theory

**see** [[category]]

_[[category theory]] is to programming what chemistry is to baking_ &mdash; <https://youtu.be/SmXB2K_5lcA?t=414>

> **resource** [[category theory]] for programmers by Bartosz Milewski &mdash; <https://www.youtube.com/watch?v=I8LbkfSSR58&list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM> (not yet finished)

> **resource** _[[category theory]] for the working hacker_ &mdash; <https://www.youtube.com/watch?v=gui_SE8rJUM>

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

the [[set#empty set]] corresponds to the [[type]] `Void` in Haskell, which corresponds to **`O`** in [[logic]] from a [[category theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. **`O`** cannot be proven, similarly to how a [[function]] that takes `Void` as a parameter cannot be called

the [[set#singleton set]] corresponds to the [[type]] `()` (or `Unit`) in Haskell, which corresponds to **`I`** in [[logic]] from a [[category theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. **`I`** can be proven, similarly to how a [[function]] that takes `Unit` as a parameter can be called

a [[relation]] being a [[relation#reflexive relation]] is equivalent to the presence of identity morphisms in [[category theory]]

a [[category]] with exactly one object is a [[monoid]] (yes, that [[monoid]] from [[functional programming]]). elements in the underlying [[set]] of a [[monoid]] correspond to [[category#morphism]]s and the [[monoid#operation]] corresponds to the [[category#composition]]

the [[category]] of [[type]]s is equivalent to a strongly typed [[programming language]], as [[function]]s in such a language are only composable if their [[type]]s match

_co..._ refers to the same object in the opposite [[category]]. product & coproduct, monad & comonad, monoid & comonoid...

[[monoid]]s are one-object categories. [[group]]s are one-object categories where every [[category#morphism]] has an inverse. adding the _oid_ suffix to a one-object category represents the equivalent multi-object category. as a consequence [[category]]es are jokingly called _monoidoids_ &mdash; <https://grossack.site/2022/08/21/monoidal-monoidoidoids.html>

---

#todo to learn:

bottom types in haskell &mdash; <https://youtu.be/p54Hd7AmVFU>

pre order, partial order, total order, and how epi + mono != iso &mdash; <https://youtu.be/aZjhqkD6k6w>

Kleisli category <https://youtu.be/i9CU4CuHADQ>

thin / thick categories

absurd function

universal construction:

the _Curry-Howard-Lambek isomorphism_ states that [[logic]], [[type theory]] and some subset of [[category theory]] are all equivalent &mdash; <https://youtu.be/I8LbkfSSR58?t=1681>

**aka** _#todo Curry-Howard correspondence, propositions as types #xxx see <https://youtu.be/IOiZatlZtGU?t=1490>_

equalizers and coequalizers, limits and colimits &mdash; GitHub Copilot. #xxx I think that limits and colimits might simply be products and coproducts but with more objects &mdash; <https://youtu.be/oCNQhTpyMgE?t=4m21s>

a [[group]] where group elements are morophisms and composition is [[group]] multiplication is a [[category]] #todo

#xxx <https://youtu.be/IOiZatlZtGU?t=2334>

#xxx <https://youtu.be/gui_SE8rJUM?t=605> from timestamp to #todo

exponentials are functions &mdash; <https://youtu.be/gui_SE8rJUM?t=1950>

system F (polymorphism) and system F&omega; (constructor on types) &mdash; <https://youtu.be/gui_SE8rJUM?t=2074>

duals are De Morgan's laws in category theory &mdash; <https://youtu.be/gui_SE8rJUM?t=2176>

exponential laws in category theory &mdash; <https://youtu.be/gui_SE8rJUM?t=2379>

proper category and functor definitions &mdash; <https://youtu.be/H0Ek86IH-3Y>

[[currying]] arises from adjumctions; programming operates in _cartesian closed categories_ &mdash; <https://youtu.be/JH_Ou17_zyU>. also see <https://cs.stackexchange.com/questions/80837/is-smn-theorem-the-same-concept-as-currying>

---

total order: aRb or bRa for all a,b. ie. <= on RR, ZZ, NN. exactly one morphism between any two objects in the category

poset. at most one morphism between any two objects in the category

"category of total order does not have products". why?

> because the product of two objects in the category is the object that is both the greatest lower bound and the least upper bound of the two objects. but in the category of total order, the product of two objects is not unique. for example, the product of 2 and 3 is 6, but it is also 6 for 3 and 2. so the category of total order does not have products. &mdash; GitHub copilot

products are terminal objects in a category of morphisms from a single object to two objects, see commutative diagram in photos on 2024-02-14
