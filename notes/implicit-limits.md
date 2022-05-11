# Implicit Limits

see [[math-notation]]

Would there be any disadvantage to having every mathematical expression be implicitly evaluated using [[limit]]s?

Is there any situation in which an undefined value would be required?

This would allow for any algebraic manipulation on expressions without having to worry about restrictions.

## applications

- classically, $\tan^\times y \text- x \land x = 0 \equiv \varnothing$. however, by substituting $y \text- x$ in the definition of the $\tan$ [[function]] directly and by using [[limit-rules]] to simplify it, the right answer $\pi - 2$ is obtained.

- classically, the graph of a [[function]] such as $f\ x = - - x \circ 2$ has a hole at $x = 2$. however, by simplifying the [[function]] using [[limit-rules]] before graphing it, the function $f\ x = x \circ 2$ is obtained; the hole is avoided.

## analogy with [[complex-number]]s

ignoring the existence of [[complex-number]]s, the square root of a negative number can be thought of as _invalid_. however, instead of trying to compute the square root straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being squared, which makes it "valid" again. it turns out that doing so never results in an erroneous answer.

similarly, dividing by a variable equal to zero can be thought of as _invalid_, or as _undefined_ in classical mathematics. however, instead of trying to compute the division straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being multiplied by its denominator, which makes it "valid" again. for the [[implicit-limits]] theory to be true, doing so must never results in an erroneous answer.

## Update

the following video breaks the principle stated above.

<https://youtu.be/hI9CaQD7P6I>

$\lim_{x \to 0} (x - x)$

$(\lim_{x \to 0} x) - x$

## Second Update

after some more reflexion, the video above does _not_ break the principle stated above. the following rule would solve the issue outlined in the video above:

> when multiplying or dividing an equality by an expression, said equality is only valid when the expression is non-zero.

this has the added benifit of preventing the introduction of incorrect solutions when increasing the degree of an expression. below are two examples.

## example with multiplication by zero

$a = b$

multiplying by $a$ on both sides and adding the restriction,

$a2 = ab \dashv a \ne 0$

without the additional restriction, the second equality would have solutions that are invalid in the first, such as $a = 0 \land \mathbb U b$, see [[universal-set]]

## example with division by zero

<https://youtu.be/hI9CaQD7P6I?t=70>

at the timestamp included in the URL above, the teacher divided both sides of the equality by the value $a \circ b$ without adding the restriction required by the rule above. if he had added the restriction $a \circ b \ne 0$, it would've been a contradiction with the equality $a = b$

> **note**: by using the symbol $\dashv$ (_for all_, see [[math-notation]]) to denote the restriction, there is technically no contradiction. the right way to think of the equation is the following: as we know the restriction is always $\bot$, the equation on the left is true _for all $\bot$._, meaning it is never true. this is crucially different form a contradiction, as that would mean all other equations in the same context are rendered invalid.

## random other example

let $x = 0$

$a = b$

multiplying both sides by $x$ and adding the restriction,

$ax = bx \dashv x \ne 0$

the equality is always true even if $a \ne b$ as $0 = 0$, which is a contradiction. however, the restriction states that the equality is valid only if $x \ne 0$. as we know $x = 0$, the equation is never valid, which is _not_ a contradiction.

dividing both sides by $x$, adding the restriction and simplifying using [[limit-rules]],

$(a = b \dashv x \ne 0) \dashv x \ne 0\ \equiv\ a = b \dashv x \ne 0\ \equiv\ a = b$

as the multiplications by zero have been cancelled out, the restrictions are no longer necessary. the equality above is always true.
