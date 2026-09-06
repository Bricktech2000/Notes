# Recursion

**see** [[combinator#y combinator]]

#stub

## Recursion Scheme

> **resource** the PNLC prelude, makes use of [[recursion#recursion scheme]]s throughout --- <https://github.com/Bricktech2000/PNLC/blob/master/prelude.pnlc>

> **resource** _Recursion Schemes_ by Tim Williams at London Haskell, with implementations for everything and lots of real-world use-cases --- <https://youtu.be/Zw9KeP3OzpU> and [[../references/slides-final.pdf]] <http://www.timphilipwilliams.com/slides.html>

> **resource** _An Introduction to Recursion Schemes_ by Patrick Thomson
>
> 1. [[../references/adventures in uncertainty_ An Introduction to Recursion Schemes.pdf]] --- <https://blog.sumtypeofway.com/posts/introduction-to-recursion-schemes.html>
> 2. [[../references/adventures in uncertainty_ Recursion Schemes, Part II_ A Mob of Morphisms.pdf]] --- <https://blog.sumtypeofway.com/posts/recursion-schemes-part-2.html>
> 3. [[../references/adventures in uncertainty_ Recursion Schemes, Part III_ Folds in Context.pdf]] --- <https://blog.sumtypeofway.com/posts/recursion-schemes-part-3.html>
> 4. [[../references/adventures in uncertainty_ Recursion Schemes, Part IV_ Time is of the Essence.pdf]] --- <https://blog.sumtypeofway.com/posts/recursion-schemes-part-4.html>
> 5. [[../references/adventures in uncertainty_ Recursion Schemes, Part 4½_ Better Living Through Base Functors.pdf]] --- <https://blog.sumtypeofway.com/posts/recursion-schemes-part-4-point-5.html>
> 6. [[../references/adventures in uncertainty_ Recursion Schemes, Part V_ Hello, Hylomorphisms.pdf]] --- <https://blog.sumtypeofway.com/posts/recursion-schemes-part-5.html>

> **resource** _The Hitchhiker's Guide to Morphisms_ by Jonathan Brachthäuser, terse summaries of several construction and destruction morphisms --- [[../references/guide-to-morphisms.pdf]] --- <https://b-studios.de/assets/guide-to-morphisms.pdf>

> **resource** _Recursion Schemes for Mathematicians_ by Iago Leal de Freitas, an explanation of catamorphisms, anamorphisms and hylomorphisms with no prerequisite knowledge but a little [[category theory]] --- [[../references/Recursion Schemes for Mathematicians _ Iago Leal de Freitas.pdf]] --- <https://iagoleal.com/posts/recursion-schemes/>

> **resource** _F-Algebras_ by Bartosz Milewski, heavier on the [[category theory]] --- [[../references/F-Algebras _   Bartosz Milewski's Programming Cafe.pdf]] --- <https://bartoszmilewski.com/2017/02/28/f-algebras/>

[[recursion#recursion scheme]]s let you factor [[recursion]] out of recursive [[algorithm]]s. use a [[type#algebraic data type]] to specify how to recurse, write a single layer of the recursive [[algorithm]] without using [[recursion]], and out pops the recursive [[algorithm]]. the rigid structure of [[recursion#recursion scheme]]s makes it easier to reason about the resulting recursive [[algorithm]]

> **example** `foldr` is the _catamorphism_ for [[linked list]]s and `unfold` is their _anamorphism_, both [[recursion#recursion scheme]]s

> **example** the [[lambda-calculus#church encoding]] encodes [[type#algebraic data type]]s as their own _catamorphism_

> **example** [[divide and conquer]] algorithms lend themselves well to _hylomorphisms_ (an anamorphism followed by a catamorphism)

one might say that [[recursion#recursion scheme]]s are to direct [[recursion]] what structured control-flow is to [[goto]] --- <https://iagoleal.com/posts/recursion-schemes/> and <https://blog.sumtypeofway.com/posts/introduction-to-recursion-schemes.html>
