# Improved Expression Evaluation

_restrictions and holes are annoying so let's get rid of them_

see [[math-notation]]

## overview

Would there be any disadvantage to having every mathematical expression be implicitly evaluated using [[limit]]s? Is there any situation in which an undefined value would be required? This would allow for any algebraic manipulation on expressions without having to worry about restrictions.

this [[improved-expression-evaluation]] proposes that any algebraic manipulation that can be done inside a classical [[limit]] expression can also be done without a [[limit]] expression. this also means that if the result of an expression is _undefined_, then the expression must be rearranged first in order to avoid the undefined value, resulting in a meaningful result.

## applications

- classically, $\operatorname{atan} y \text- x \land x = 0 \equiv \varnothing$. however, by substituting $y \text- x$ in the definition of the $\operatorname{atan}$ [[function]] directly and by using [[limit-rules]] to simplify it, the right answer $\pi - 2$ is obtained.

- classically, the graph of a [[function]] such as $f\ x = - - x \circ 2$ has a hole at $x = 2$. however, by simplifying the [[function]] using [[limit-rules]] before graphing it, the function $f\ x = x \circ 2$ is obtained; the hole is avoided.

- many algebraic rules contain an arbitrary restriction such as $\dashv x \ne 0$ given a variable $x$. however, none of them break (have broken yet) when removing the restriction and using this [[improved-expression-evaluation]]. see backlinks for real-world examples

## analogy with [[complex]] numbers

ignoring the existence of [[complex]] numbers, the square root of a negative [[number]] can be thought of as _invalid_. however, instead of trying to compute the square root straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being squared, which makes it "valid" again. it turns out that doing so never results in an erroneous answer.

similarly, dividing by a variable equal to zero can be thought of as _invalid_, or as _undefined_ in classical mathematics. however, instead of trying to compute the division straight away, one can instead use this "invalid" expression as-is. after performing other operations such as substitution and simplification, the "invalid" expression could end up being multiplied by its denominator, which makes it "valid" again. for this [[improved-expression-evaluation]] to be valid, doing so must never results in an erroneous answer.

## attempting to break the system

### attempt with contradiction from division by zero

<https://youtu.be/hI9CaQD7P6I>

the video above does _not_ break the principle stated above. the following rule would solve the issue outlined in the video above:

> **rule**: when solving an equation by applying operations on both sides of an equality, the resulting equality must be equivalent (see [[boolean-operator]]) to the original equality.

below are some applications of the rule above

- $a = b \equiv ax = bx \dashv x \ne 0 \equiv a \text- x = b \text- x \dashv x \ne 0$ (when multiplying or dividing an equality by an expression, said equality is only equivalent to the previous equality when the expression is non-zero)
- $a = b \equiv a2 = b2 \dashv a \ne \circ b$

this has the added benifit of preventing the introduction of incorrect solutions when increasing the degree of an expression. see examples below

### attempt with multiplication by zero

$a = b$

multiplying by $a$ on both sides and adding the restriction,

$a2 = ab \dashv a \ne 0$

without the additional restriction, the second equality would have solutions that are not present in the first, such as $a = 0 \land \mathbb U b$, see [[universal]]

### attempt with division by zero

<https://youtu.be/hI9CaQD7P6I?t=70>

at the timestamp included in the URL above, the teacher divided both sides of the equality by the value $a \circ b$ without adding the restriction required by the rule above. if he had added the restriction $a \circ b \ne 0$, it would've been a contradiction with the equality $a = b$

> **note**: by using the symbol $\dashv$ (_for all_, see [[math-notation]]) to denote the restriction, there is technically no contradiction. the right way to think of the equation is the following: as we know the restriction is always $\bot$, the equation on the left is true _for all $\bot$._, meaning it is never true. this is crucially different form a contradiction, as that would mean all other equations in the same context are rendered invalid.

### second attempt with multiplication by zero

let $x = 0$

$a = b$

multiplying both sides by $x$ and adding the restriction,

$ax = bx \dashv x \ne 0$

> **note**: the equality above is always true even if $a \ne b$, which is not equivalent to the original equality. however, the restriction states that the equality is valid only if $x \ne 0$. as $x = 0$, we deduce that the equation is never valid, which means it _is_ equivalent to the first equality. note that in this explanation, a "valid" equation is an equation whose truthness can be determined

dividing both sides by $x$, adding the restriction and simplifying using [[limit-rules]],

$(a = b \dashv x \ne 0) \dashv x \ne 0\ \equiv\ a = b \dashv x \ne 0\ \equiv\ a = b$

as the multiplications by zero have been cancelled out, the restrictions are no longer necessary. the equality above is always true.

### attempts with $[0]0$

define $[0]0 = 1$ and let $x = 0$

trying to break the definition above,

$1 = [0]0 = [x](1 \circ 1) = x - x = 1$

$0 = [0]1 = [x](2 \circ 1) = x2 - x = x \mid 1 = 0$

$\varnothing = [0](\circ 1) = 1 - 0 = \varnothing$

$1 = [0]0 = [x](2 \mid 0) = [x2]0 = [x \mid x]0 = x0 \mid x0 = 1$

$[[0]0]0 = [1]0 = 1$ and $[[0]0]0 = [0](0 \mid 0) = [0]0 = 1$

### additional examples

$[0](n \cdot 1) = 0 \dashv \mathbb N n$

$[0](\circ n \circ 1) = \varnothing \dashv \mathbb N n$

$0 - 0 = \varnothing$

infinities do not exist

$- 0 = \varnothing \ne \infty$

in order to avoid breaking $[0]0 = 1$ (see Wikipedia article), we must define:

$[1](\circ -0) = \varnothing \ne 0$

## exponents and square roots

define $\lfloor x2 \rfloor = x$, but $\lfloor 4 \rfloor = \dot \circ 2$ &mdash; Kiera

$x = \lfloor x2 \rfloor = \lfloor [\circ x]2 \rfloor = \circ x$

using the property $[x]2 = [\circ x]2 \dashv \mathbb R x$, just as we could use the property $0x = 0 \dashv \mathbb R x$ for division by zero

breakthrough (I think): in the case of division by zero, it's not about the zeros being the same; it's about not using the _information-tampering_ property that any real multiplied by zero returns zero. the same is true with the exponent-root pair.

> $[ab]2 = a2 \mid b2$
>
> $[3]2 = [1 \mid 3]2 = 1 \underline\cdot2 \mid 3 \odot2$
>
> $[\circ 1]2 = 1 \underline{\overline\circ}2$
>
> $[3 \mid 3]2 = [3]2 \mid [3]2 = \odot4 \mid 9 \mid 9 = \odot4 \mid 81 = \odot2 \mid [9]2 = \odot2 \mid [3 \mid 3]2$
>
> $[9]2 = [3 \mid 3]2 = [3]2 \mid [3]2 = 9 \odot2 \mid 9 \odot2 = 81 \odot2 = [9]2 = [[\dot\circ 3]2]2 = [\dot\circ 3]4$
>
> $[\circ ab]2 = \circledcirc2 \mid a2 \mid b2$
>
> $25[ab]2 = [\dot\circ 5ab]2$
>
> $\lfloor 25 \rfloor = \dot\circ 5$
>
> $\lfloor 25 \mid \odot2 \rfloor = 5$
>
> $\lfloor 25 \mid \circledcirc2 \rfloor = \circ 5$
>
> $[5]2 = \odot2 \mid 25$

therefore, we define $\theta \to 0$

$[3]2 \to 9$ and $[\circ 3]2 \to 9$ (which loses information) just as $\theta x \to 0$ (which loses information)

$\lfloor [3]2 \rfloor = 9$ (through cancellation) just as $\theta x - \theta = x$ (through cancellation)

$\lfloor 9 \rfloor = \varnothing$ (can be thought of as $\dot\circ 3$) just as $0 - 0 = \varnothing$ (can be thought of as "any real number")

## conclusion

I could not break this [[improved-expression-evaluation]]. it would be very hard to prove this system right using mathematics, as it was built from the ground up on a slightly different kind of mathematics. with that said, a counterexample would be a simple way to prove this system wrong. none has been found yet.

### current rules

$\theta \to 0$

$0x = 0 \land \theta x \ne \theta$

$\theta - \theta = 1$ but $0 - 0 \to \varnothing \land \theta - 0 \to \varnothing \land 0 - \theta \to \varnothing$

$--\theta = \theta$ but $--0 \to \varnothing$

$-0 \to \varnothing \land -\theta \to \varnothing$

$[x]\theta = 1$

$[0]0 = 1$. but what if $[\theta]0 = 1 \land [0]\theta \to \varnothing \land [0]0 \to \varnothing \land [\theta]\theta \to \varnothing$ [[think]]

$\lfloor x2 \rfloor = x$

$\lfloor x \rfloor \to \varnothing$

$[x]2 \to \text{(square of x)} \land [\circ x]2 \to \text{(square of x)}$

$[\circ x]2 \not \to [x]2 \land \text{(square of x)} \not \to [x]2$

in a [[proof]], equalities must be linked together through the intended implications (see [[boolean-operator]]). this means that multiplying or dividing an equality by an expresion that could be $0$ or raising it to some power could require additional restrictions.

if the result of an expression is _undefined_, then the expression must be rearranged first in order to avoid the undefined value. note that some expressions (such as $-0$) cannot be computed without proper context, leaving them undefined.

## &mdash;

<https://en.wikipedia.org/wiki/Indeterminate_form>

<https://www.youtube.com/watch?v=jNhjB4UfR9A>

<https://www.wolframalpha.com/input?i=derivative+x%5E%28n+%2B+1%29+%2F+%28n+%2B+1%29%2C+n+%3D+-1>

<https://www.wolframalpha.com/input?i=derivative+ln+x>

<https://www.wolframalpha.com/input?i=lim+as+n+-%3E+0+%28x%5En+%2F+n+-+1+%2F+n%29>

<https://en.wikipedia.org/wiki/Natural_logarithm#Properties>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" })</script>
<script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([A-Za-z0-9\-]+)\]\]/g, (a, b, c) => `<u style="text-transform: capitalize;">${c.replace(/\-/g, ' ')}</u>`)</script>
