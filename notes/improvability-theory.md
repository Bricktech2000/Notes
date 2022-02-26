# Improvability Theory

see [[classical-math-notation]]

The Improvability Theory states that:

> No formal proof for a theorem is valid as its set of assumptions is never comprehensive.

## explanation

_no proof for a theorem is valid as the theorem could always be proven more formally_

this statement implies that every theorem believed to be true has some edge cases, even if they are negligible in practice.

to clarify some assumptions made in the original theorem &mdash; as any proof is based on a set of assumptions, it should be rephrased as “no proof for a theorem is valid as its list of assumption can never be considered complete.” to clarify some assumptions made in the second version of the theorem, it should be rephrased as...

that’s meta.

## note

This theory was formulated while eating nachos with Kiera. See $Fig.\ 1$.

TODO:
![20211219_215504.jpg](Improvabil%2002414/20211219_215504.jpg)

$Fig.\ 1$: Eating nachos with Kiera.

## examples

> _anything_ squared is a positive number: $x^2 \ge 0$

the statement above used to be true, except on rare cases where $x$ happens to be an imaginary number. it is right for most practical use cases, but it is in fact “almost always right”.

> $(a^b)^c = a^{b \times c}$

the equation above is thought of as always being true. however, it can break when working with negative values and fractional exponents. for example, $(a^2)^{\frac{1}{2}}  \ne (a^{\frac{1}{2}})^2$ when $a < 0$.

> $x \times 0 = 0$

ignoring the existence of vectors, the equation above seems to always be true, as an implicit assumption is made that $x$ is limited to complex numbers. then, let theorem $A'$ be derived from the expression above. as theorem $A'$ relies on the implicit assumption that $x$ is limited to complex numbers, it would break with $x = (2, 3)$, for example. $x \times 0 = (0, 0) \therefore x \times 0 \ne 0$ as vector multiplication by a scalar does not return a scalar, but a vector.
