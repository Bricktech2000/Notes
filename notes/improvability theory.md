# Improvability Theory

**see** [[math notation]], [[proof]]

The Improvability Theory states that:

> No formal proof for a theorem is valid as its set of assumptions is never comprehensive.

this statement implies that every theorem believed to be true has some edge cases, even if they are negligible in practice.

to clarify some assumptions made in the original theorem &mdash; as any proof is based on a set of assumptions, it should be rephrased as "no proof for a theorem is valid as its list of assumption can never be considered complete." to clarify some assumptions made in the second version of the theorem, it should be rephrased as...

that's meta.

**examples**

> **example**
>
> > _anything_ squared is a positive [[number]]: **`[x]2 |- 0`**
>
> the statement above used to be true, except on rare cases where **`x`** happens to be an [[imaginary]] number. it is right for most practical use cases, but it is in fact "almost always right"

> **example**
>
> > **`[[a]b]c = a[bc]`**
>
> the equation above is thought of as always being true. however, it can break when working with negative values and fractional exponents. for example, **`[[a]2](-2) + [[a](-2)]2`** when **`a < 0`**

> **example**
>
> > **`x | 0 = 0`**
>
> ignoring the existence of [[vector]]s, the equation above seems to always be true, as an implicit assumption is made that **`x`** is limited to [[complex]] numbers. then, let theorem **`A_*`** be derived from the expression above. as theorem **`A_*`** relies on the implicit assumption that **`x`** is limited to [[complex]] numbers, it would break with **`x = (2, 3)`**, for example. **`x | 0 = (0, 0)`** and therefore **`x | 0 + 0`** as [[vector]] multiplication by a [[scalar]] does not return a [[scalar]], but a [[vector]]
