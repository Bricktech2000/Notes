# Category Theory

see [[category]]

> "[[category-theory]] is to programming what chemistry is to baking" &mdash; <https://youtu.be/SmXB2K_5lcA?t=414>

there appears to be a standard way to build contexts in which we do [[mathematics]]. [[category-theory]] is all about formalizing this observation

> **examples** _mathematical contexts_
>
> - [[linear-algebra]]
> - [[group-theory]]
> - [[category-theory]]
> - [[set-theory]]
> - [[topology]]
> - [[type-theory]]
> - [[lambda-calculus]]
> - [[logic]]

---

the _curry howard lambek isomorphism_ states that [[logic]], [[type-theory]] and some subset of [[category-theory]] are all equivalent &mdash; <https://youtu.be/I8LbkfSSR58?t=1681>

[[function]]s and [[type]]s can be viewed as morphisms and objects in a [[category-theory]] context

the [[empty]] [[set]] corresponds to the [[type]] `Void` in Haskell, which corresponds to $\bot$ in [[logic]] from a [[category-theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. $\bot$ cannot be proven, similarly to how a [[function]] that takes `Void` as a parameter cannot be called

the singleton [[set]] corresponds to the [[type]] `()` (or `Unit`) in Haskell, which corresponds to $\top$ in [[logic]] from a [[category-theory]] perspective. when looking at propositions as types, [[function]]s are [[proof]]s. $\top$ can be proven, similarly to how a [[function]] that takes `Unit` as a parameter can be called

a [[relation]] being reflexive is equivalent to the presence of identity morphisms in [[category-theory]]

a [[category]] with exactly one object is a [[monoid]] (yes, that [[monoid]] from [[functional-programming]])

the [[category]] of [[type]]s is equivalent to a strongly typed [[programming-language]], as [[function]]s in such a language are only composable if their [[type]]s match

---

#todo to learn:

bottom types in haskell &mdash; <https://youtu.be/p54Hd7AmVFU>

pre order, partial order, total order, and how epi + mono != iso &mdash; <https://youtu.be/aZjhqkD6k6w>

Kleisli category <https://youtu.be/i9CU4CuHADQ>
