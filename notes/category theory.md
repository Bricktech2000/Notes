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

**applications**

[[category theory]] is a [[tool]] that can be used for studying [[algebraic structure]]s &mdash; <https://en.wikipedia.org/wiki/Algebraic_structure>

---

[[function]]s and [[type]]s can be viewed as morphisms and objects in a [[category theory]] context

the [[set#empty set]] corresponds to the [[type]] `Void` in Haskell, which corresponds to **`__`** in [[logic]] from a [[category theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. **`__`** cannot be proven, similarly to how a [[function]] that takes `Void` as a parameter cannot be called

the [[set#singleton set]] corresponds to the [[type]] `()` (or `Unit`) in Haskell, which corresponds to **`^^`** in [[logic]] from a [[category theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. **`^^`** can be proven, similarly to how a [[function]] that takes `Unit` as a parameter can be called

a [[relation]] being a [[relation#reflexive relation]] is equivalent to the presence of identity morphisms in [[category theory]]

a [[category]] with exactly one object is a [[monoid]] (yes, that [[monoid]] from [[functional programming]])

the [[category]] of [[type]]s is equivalent to a strongly typed [[programming language]], as [[function]]s in such a language are only composable if their [[type]]s match

the terminal object of a [[category]] corresponds to the [[set#singleton set]] and the initial object of a [[category]] corresponds to the [[set#empty set]]

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

the _curry-howard-lambek isomorphism_ states that [[logic]], [[type theory]] and some subset of [[category theory]] are all equivalent &mdash; <https://youtu.be/I8LbkfSSR58?t=1681>

**aka** _#todo curry-howard correspondence, propositions as types #todo #think see <https://youtu.be/IOiZatlZtGU?t=1490>_

[[category#product]]s in the [[category]] of [[set]]s are [[cartesian product]]s &mdash; Justin Veilleux

[[category#coproduct]]s in the [[category]] of [[set]]s are [[set#disjoint union]]s &mdash; Justin Veilleux

[[category#product]]s in the [[category]] **`RR, -|`** are the minimum of two numbers &mdash; Justin Veilleux

[[category#coproduct]]s in the [[category]] **`RR, -|`** are the maximum of two numbers &mdash; Justin Veilleux

[[category#product]]s in the [[category]] **`NN, "divides"`** are the GCD of two numbers, see [[psi function]] &mdash; Justin Veilleux

[[category#coproduct]]s in the [[category]] **`NN, "divides"`** are the LCM of two numbers, see [[psi function]] &mdash; Justin Veilleux

[[category#product]]s in the [[category]] **`{{ }}, a b -> /\ a -| b`** are the intersection of two sets &mdash; Justin Veilleux

[[category#coproduct]]s in the [[category]] **`{{ }}, a b -> /\ a -| b`** are the union of two sets &mdash; Justin Veilleux

a category of ([[vector space]]s, linear maps) is a thing. #todo look up linear maps

a category of (topological spaces, continuous maps) is a thing. #todo look up continuous maps and topological spaces

a category of ([[group]]s, [[group]] homomorphisms) is a thing. #todo look up group homomorphisms

(bijective function, function composition) forms a [[group]] #todo

a [[group]] where group elements are morophisms and composition is [[group]] multiplication is a [[category]] #todo

#think <https://youtu.be/IOiZatlZtGU?t=2334>

#think <https://youtu.be/gui_SE8rJUM?t=605> from timestamp to #todo

exponintials are functions &mdash; <https://youtu.be/gui_SE8rJUM?t=1950>

system F (polymorphism) and system F&omega; (constructor on types) &mdash; <https://youtu.be/gui_SE8rJUM?t=2074>

duals are DeMorgan's laws in category theory &mdash; <https://youtu.be/gui_SE8rJUM?t=2176>

exponential laws in category theory &mdash; <https://youtu.be/gui_SE8rJUM?t=2379>

proper category and functor definitions &mdash; <https://youtu.be/H0Ek86IH-3Y>
