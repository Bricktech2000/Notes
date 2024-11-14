# Improved Expression Evaluation

_restrictions and holes are annoying so let's get rid of them_

**see** [[math notation]]

## overview

Would there be any disadvantage to having every mathematical expression be implicitly evaluated using [[limit]]s? Is there any situation in which an undefined value would be required? This would allow for any algebraic manipulation on expressions without having to worry about restrictions.

this [[improved expression evaluation]] proposes that any algebraic manipulation that can be done inside a conventional [[limit]] expression can also be done without a [[limit]] expression. this also means that if the result of an expression is _undefined_, then the expression must be rearranged first in order to avoid the undefined value, resulting in a meaningful result.

## applications

- conventionally, **`x = 0 < "atan" y-x = @`**. however, by substituting **`y-x`** in the definition of the **`"atan"`** [[function]] directly and by using [[limit rules]] to simplify it, the right answer **`-4tt`** is obtained.

- conventionally, the graph of a [[function]] such as **`f x = -- -- x . 2`** has a hole at **`x = 2`**. however, by simplifying the [[function]] using [[limit rules]] before graphing it, the function **`f x = x . 2`** is obtained; the hole is avoided.

- many algebraic rules contain an arbitrary restriction such as **`... > x + 0`** given a [[variable]] **`x`**. however, none of them break (have broken yet) when removing the restriction and using this [[improved expression evaluation]]. see backlinks for real-world examples

## analogy with [[complex]] numbers and [[fraction]]s

ignoring the existence of [[complex]] numbers, the square root of a negative [[number]] can be thought of as _invalid_. however, instead of trying to compute the square root straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being squared, which makes it "valid" again. it turns out that doing so never results in an erroneous answer.

in a [[positional numeral system]] that only supports [[integer]]s, a [[fraction]]al [[number]] such as **`2-5`** can be thought of as _invalid_. however, instead of trying to compute the division straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expresion could end up being multiplied by an [[integer]] multiple of its denominator such as **`10`**, which makes it "valid" again: **`2-5 | 10 = 4`**. it turns out that doing so never results in an erroneous answer.

similarly, dividing by a [[variable]] equal to zero can be thought of as _invalid_, or as _undefined_ in conventional [[mathematics]]. however, instead of trying to compute the division straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being multiplied by its denominator, which makes it "valid" again. for this [[improved expression evaluation]] to be valid, doing so must never results in an erroneous answer.

## attempting to break the system

### attempt with contradiction from division by zero

&mdash; <https://youtu.be/hI9CaQD7P6I>

the video above does _not_ break the principle stated above. the following rule would solve the issue outlined in the video above:

> **rule** when solving an equation by applying operations on both sides of an equality, the resulting equality must be equivalent to the original equality.

below are some applications of the rule above

- **`a = b == (ax = bx > x + 0) == (a -- x = b -- x > x + 0)`** (when multiplying or dividing an equality by an expression, said equality is only equivalent to the previous equality when the expression is non-zero)
- **`a = b == a2 = b2 > a + .b`**

this has the added benifit of preventing the introduction of incorrect solutions when increasing the degree of an expression. see examples below

### attempt with multiplication by zero

**`a = b`**

multiplying by **`a`** on both sides and adding the restriction,

**`a2 = ab > a + 0`**

without the additional restriction, the second equality would have solutions that are not present in the first, such as **`a = 0 /\ UU b`**, see [[set#universal set]]

### attempt with division by zero

&mdash; <https://youtu.be/hI9CaQD7P6I?t=70>

at the [[time]]stamp included in the URL above, the teacher divided both sides of the equality by the value **`a . b`** without adding the restriction required by the rule above. if he had added the restriction **`a . b + 0`**, it would've been a [[contradiction]] with the equality **`a = b`**

> **note** by using the symbol **`>`**, the [[quantifier#universal quantifier]], to denote the restriction, there is technically no contradiction. the right way to think of the equation is the following: as we know the restriction is always **`__`**, the equation on the left is true _for all **`__`**_, meaning it is never true. this is crucially different form a [[contradiction]], as that would mean all other equations in the same context are rendered invalid.

### second attempt with multiplication by zero

let **`x = 0`**

**`a = b`**

multiplying both sides by **`x`** and adding the restriction,

**`ax = bx > x + 0`**

> **note** the equality above is always true even if **`a + b`**, which is not equivalent to the original equality. however, the restriction states that the equality is valid only if **`x + 0`**. as **`x = 0`**, we deduce that the equation is never valid, which means it _is_ equivalent to the first equality. note that in this explanation, a "valid" equation is an equation whose truthness can be determined

dividing both sides by **`x`**, adding the restriction and simplifying using [[limit rules]],

**`(a = b > x + 0) > x + 0 == (a = b > x + 0) == a = b`**

as the multiplications by zero have been cancelled out, the restrictions are no longer necessary. the equality above is always true.

### attempts with **`0[0]`**

define **`0[0] = 1`** and let **`x = 0`**

trying to break the definition above,

**`1 = 0[0] = x[1 . 1] = x -- x = 1`**

**`0 = 0[1] = x[2 . 1] = x2 - x = x | 1 = 0`**

**`@ = 0[.1] = 1 -- 0 = @`**

**`1 = 0[0] = x[2 | 0] = [x2]0 = [x | x]0 = x0 | x0 = 1`**

**`[[0]0]0 = [1]0 = 1`** and **`[[0]0]0 = 0[0 | 0] = 0[0] = 1`**

### additional examples

**`0[n:1] = 0 > NN n`**

**`0[.n.1] = @ > NN n`**

**`0 -- 0 = @`**

infinities do not exist

**`-- 0 = @ + @@`**

in order to avoid breaking **`0[0] = 1`** (see Wikipedia article), we must define:

**`1[.--0] = @ + 0`**

### attempt with [[integral]]s and [[logarithm]]s

using the [[logarithm]] [[antiderivative]] rule, **`$ 1 -- x | dd x = /"abs" x\ : c x`**. then, using the power [[antiderivative]] rule, **`$ 1 -- x | dd x = $ x[.1] | dd x = x[qq]-q : c`**. with **`c = .1 -- qq`**, we get **`/x\ = x[qq] . 1 -- qq`**

### exponents and square roots

define **`\x2/ = x`**, but **`\4/ = {2 \/ .2}`** &mdash; Kiera

**`x = \x2/ = \[.x]2/ = .x`**

using the property **`[x]2 = [.x]2 > RR x`**, just as we could use the property **`0x = 0 > RRx`** for division by zero

breakthrough (I think): in the case of division by zero, it's not about the zeros being the same; it's about not using the _information-tampering_ property that any [[real]] multiplied by zero returns zero. the same is true with the exponent-root pair.

we define **`qq -> 0`**

**`[3]2 -> 9`** and **`[.3]2 -> 9`** (which loses information) just as **`qq x -> 0`** (which loses information)

**`\[3]2/ = 3`** (through cancellation) just as **`qq x -- qq = x`** (through cancellation)

**`\9/ = @`** (can be thought of as **`{{3, .3}}`**) just as **`0 -- 0 = @`** (can be thought of as "any [[real]] number")

## conclusion

I could not break this [[improved expression evaluation]]. it would be very hard to prove this system right using [[mathematics]], as it was built from the ground up on a slightly different kind of [[mathematics]]. with that said, a counterexample would be a simple way to prove this system wrong. none has been found yet.

### current rules

#xxx might be incomplete or erroneous

**`qq -> 0`**

**`0x = 0 /\ qq x + qq`**

**`qq -- qq = 1`** but **`0 -- 0 -> @ /\ qq - 0 -> @ /\ 0 - qq -> 0`**

**`-- -- qq = qq`** but **`-- -- 0 -> @`**

**`-- 0 -> @ /\ --qq -> @`**

**`x[qq] = 1`**

**`qq[0] -> 1 /\ qq[0] -> @ /\ 0[0] -> @ /\ qq[qq] -> @`**

**`/x2\ = x`**

**`/x\ -> @`**

**`[x]2 -> "square of x" /\ [.x]2 -> "square of x"`**

**`(>< [.x]2 -> [x]2) /\ (>< "square of x" -> [x]2)`**

**`x[qq] = 1`**

**`$ dd y = dd $ y = y`**

**`$ f -> @`**

in a [[proof]], equalities must be linked together through the intended [[boolean#implication]]s. this means that multiplying or dividing an equality by an expresion that could be **`0`** or raising it to some power could require additional restrictions.

if the result of an expression is _undefined_, then the expression must be rearranged first in order to avoid the undefined value. note that some expressions (such as **`--0`**) cannot be computed without proper context, leaving them undefined.

## &mdash;

&mdash; <https://en.wikipedia.org/wiki/Indeterminate_form>

&mdash; <https://www.youtube.com/watch?v=jNhjB4UfR9A>

&mdash; <https://www.wolframalpha.com/input?i=derivative+x%5E%28n+%2B+1%29+%2F+%28n+%2B+1%29%2C+n+%3D+-1>

&mdash; <https://www.wolframalpha.com/input?i=derivative+ln+x>

&mdash; <https://www.wolframalpha.com/input?i=lim+as+n+-%3E+0+%28x%5En+%2F+n+-+1+%2F+n%29>

&mdash; <https://en.wikipedia.org/wiki/Natural_logarithm#Properties>

[[trigonometric function]] period #xxx

#todo is <https://ncatlab.org/nlab/show/wheel> related here? &mdash; <https://whystartat.xyz/wiki/Unary_division> &mdash; Justin Veilleux
