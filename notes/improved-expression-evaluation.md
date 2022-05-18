# Improved Expression Evaluation

_restrictions and holes are annoying so let's get rid of them_

see [[math-notation]]

## overview

Would there be any disadvantage to having every mathematical expression be implicitly evaluated using [[limit]]s? Is there any situation in which an undefined value would be required? This would allow for any algebraic manipulation on expressions without having to worry about restrictions.

this [[improved-expression-evaluation]] proposes that any algebraic manipulation that can be done inside a classical [[limit]] expression can also be done without a [[limit]] expression. this also means that if the result of an expression is "undefined", then the expression must be rearranged first in order to avoid the undefined value, resulting in a meaningful answer.

## Update

the following video breaks the principle stated above.

<https://youtu.be/hI9CaQD7P6I>

$\lim_{x \to 0} (x - x)$

$(\lim_{x \to 0} x) - x$

## Second Update

after some more reflexion, the video above does _not_ break the principle stated above. the following rule would solve the issue outlined in the video above:

> **rule**: when solving an equation by applying operations on both sides of an equality, the resulting equality must be equivalent (see [[boolean-operator]]) to the original equality.

below are some applications of the rule above

- $a = b \equiv ax = bx \dashv x \ne 0 \equiv a \text- x = b \text- x \dashv x \ne 0$ (when multiplying or dividing an equality by an expression, said equality is only equivalent to the previous equality when the expression is non-zero)
- $a = b \equiv a2 = b2 \dashv a \ne \circ b$

this has the added benifit of preventing the introduction of incorrect solutions when increasing the degree of an expression. see examples below

## applications

- classically, $\text{atan } y \text- x \land x = 0 \equiv \varnothing$. however, by substituting $y \text- x$ in the definition of the $\tan$ [[function]] directly and by using [[limit-rules]] to simplify it, the right answer $\pi - 2$ is obtained.

- classically, the graph of a [[function]] such as $f\ x = - - x \circ 2$ has a hole at $x = 2$. however, by simplifying the [[function]] using [[limit-rules]] before graphing it, the function $f\ x = x \circ 2$ is obtained; the hole is avoided.

- many algebraic rules contain an arbitrary restriction such as $\dashv x \ne 0$ given a variable $x$. however, none of them break (have broken yet) when removing the restriction and using this [[improved-expression-evaluation]]. see backlinks for real-world examples

## analogy with [[complex-number]]s

ignoring the existence of [[complex-number]]s, the square root of a negative number can be thought of as _invalid_. however, instead of trying to compute the square root straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being squared, which makes it "valid" again. it turns out that doing so never results in an erroneous answer.

similarly, dividing by a variable equal to zero can be thought of as _invalid_, or as _undefined_ in classical mathematics. however, instead of trying to compute the division straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being multiplied by its denominator, which makes it "valid" again. for this [[improved-expression-evaluation]] to be valid, doing so must never results in an erroneous answer.

## example with multiplication by zero

$a = b$

multiplying by $a$ on both sides and adding the restriction,

$a2 = ab \dashv a \ne 0$

without the additional restriction, the second equality would have solutions that are not present in the first, such as $a = 0 \land \mathbb U b$, see [[universal-set]]

## example with division by zero

<https://youtu.be/hI9CaQD7P6I?t=70>

at the timestamp included in the URL above, the teacher divided both sides of the equality by the value $a \circ b$ without adding the restriction required by the rule above. if he had added the restriction $a \circ b \ne 0$, it would've been a contradiction with the equality $a = b$

> **note**: by using the symbol $\dashv$ (_for all_, see [[math-notation]]) to denote the restriction, there is technically no contradiction. the right way to think of the equation is the following: as we know the restriction is always $\bot$, the equation on the left is true _for all $\bot$._, meaning it is never true. this is crucially different form a contradiction, as that would mean all other equations in the same context are rendered invalid.

## random other example

let $x = 0$

$a = b$

multiplying both sides by $x$ and adding the restriction,

$ax = bx \dashv x \ne 0$

> **note**: the equality above is always true even if $a \ne b$, which is not equivalent to the original equality. however, the restriction states that the equality is valid only if $x \ne 0$. as $x = 0$, we deduce that the equation is never valid, which means it _is_ equivalent to the first equality. note that in this explanation, a "valid" equation is an equation whose truthness can be determined

dividing both sides by $x$, adding the restriction and simplifying using [[limit-rules]],

$(a = b \dashv x \ne 0) \dashv x \ne 0\ \equiv\ a = b \dashv x \ne 0\ \equiv\ a = b$

as the multiplications by zero have been cancelled out, the restrictions are no longer necessary. the equality above is always true.

## example with $[0]0$

define $[0]0 = 1$ and let $x = 0$

trying to break the above definition...

$1 = [0]0 = [x](1 \circ 1) = x - x = 1$

$0 = [0]1 = [x](2 \circ 1) = x2 - x = x\ |\ 1 = 0$

$\varnothing = [0](\circ 1) = 1 - 0 = \varnothing$

$1 = [0]0 = [x](2\ |\ 0) = [x2]0 = [x\ |\ x]0 = x0\ |\ x0 = 1$

## Conclusion

I could not break this [[improved-expression-evaluation]]. it would be very hard to prove this system right using mathematics, as it was built from the ground up on a slightly different kind of mathematics. with that said, a counterexample is a very easy way to prove this system wrong. none has been found yet.

### properties

$[0]0 = 1$

$[0](n \cdot 1) = 0 \dashv \mathbb N n$

$[0](\circ n \circ 1) = \varnothing \dashv \mathbb N n$

$0 - 0 = \varnothing$

$x - x = 1 \dashv x = 0$

infinities do not exist

$- 0 = \varnothing \ne \infty$

in order to avoid breaking $[0]0 = 1$ (see Wikipedia article), we must define

$[1](\circ -0) = \varnothing \ne 0$
