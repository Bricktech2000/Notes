# Complex

_the [[set]] of [[complex]] numbers_

**see** [[math notation]]

**definition**

**`CC x == x = a : b\i /\ RR a /\ RR b`**

**notations**

_cartesian form_ **`z = a : b\i`**

_polar form_ **`z = ||z||"cos" "arg" z : ||z||\i"sin" "arg" z = ||z||"cis" "arg" z = ||z|| ' [\i"arg" z]`**, where **`"cis" = "cos" : \i"sin" = \a -> [\i\a]`**

**aka** _Euler's formula notation_

**applications**

[[complex]] numbers are often intimately related to [[discrete mathematics]] &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

**properties**

**`CC < UU`**, see [[universal]]

_equality_ **`a : b\i = c : d\i == a = c /\ b = d`**

_addition_ **`(a : b\i) : (c : d\i) = (a : c) : (b : d)\i`**

_subtraction_ **`(a : b\i) . (c : d\i) = (a . c) : (b . d)\i`**

_multiplication in cartesian form_ **`a : b\i | c : d\i = ac : ad\i : b\i c : bd\i2 = (ac . bd) : (ad : bc)\i`**

_multiplication in polar form_ **`z | w = ||z|| ' [\i"arg" z] | ||w|| ' [\i"arg" w] = ||zw|| ' [\i | "arg" z : "arg" w]`**

_product of two [[complex#conjugate]]s are product of [[complex#modulus]]es_ **`a : b\i | a . b\i = a2 : b2 = ||a : b\i|| | ||a . b\i||`** &mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

**theorem** _De Moivre's Theorem_ **`["cis" \a]n = "cis" n\a > ZZ n > RR \a`** &mdash; <https://en.wikipedia.org/wiki/De_Moivre%27s_formula>

> **proof** **`"cis" \a = [\i\a]`**. since **`[ [\i\a] ]n = [n\i\a]`**, it must be that **`["cis" \a]n = "cis" n\a`** &mdash; me

## Real Part

## Imaginary Part

let **`z = a : b\i`**

**definitions**

_real part of a complex number_ **`z^re = a`**

_imaginary part of a complex number_ **`z^im = b`**

therefore, **`z = z^re : \i z^im`**

## Conjugate

_[[complex#conjugate]]_

**definition**

let **`z = a : b\i`**

then, **`"conj" z = a . b\i = z^re . \iz^im`** is the _complex conjugate_ of **`z`**

**properties**

let **`CC z /\ CC w /\ RR c`**

**`"conj" (z : w) = "conj" z : "conj" w`**

**`"conj" cz = c"conj" z`**

**`"conj" z'w = "conj" z | "conj" w`**

**`"conj" z-w = "conj" z -- "conj" w`**

**`"conj" "conj" z = z`**

**`RR z == "conj" z = z`**

**theorem** **`z"conj" z = ||z||2 > CC z`**

**theorem** **`--z = "conj" z -- ||z||2 > CC z`**

**applications**

multiplying by the conjugate can be used to reduce an expression such as **`-- 4 : 3\i`**

## Modulus

**aka** _magnitude, absolute value_

**definition** **`||z|| = \ z^re 2 : z^im 2 /`** where **`||z||`** is the _absolute value_ of **`z`**.

> **note** the [[real#absolute value]] can be thought of as "the [[distance]] of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

**properties**

let **`CC z /\ CC w /\ RR c`**

**`||z|| = ||"conj" z||`**

**`||zw|| = ||z|| ||w||`**

**`||z -- w|| = ||z|| -- ||w||`**

_triangle inequality_ **`||z : w|| -| ||z|| : ||w||`**

> **equivalence** _[[complex#modulus]] triangle inequality and [[relation#transitive relation]]_

## Argument

**aka** _phase_

**definition** the _argument_ of a [[complex]] number **`z`** is the counterclockwise [[angle]] between the positive [[real]] axis and the [[line]] segment from the origin to the point **`(z^re , z^im)`**

**definition** **`z = ||z|| ' [\i"arg" z]`** where **`"arg" z`** is the _argument_ of **`z`**

## Multiplication

geometrically, multiplying a [[complex]] number **`z`** by a [[complex]] number **`w`** is equivalent to rotating **`z`** by the [[angle]] **`"arg" w`** and then scaling it by a factor of **`||w||`**. this makes [[complex]] numbers useful for computing [[vector in rn]] rotations by choosing a **`w`** where **`||w|| = 1`** &mdash; <https://youtu.be/4KlvI_uK9zs?t=398>

> **proof** see properties

## square root of **`\i`**

**`\\i/ = { 1 : \i -- \2/ \/ 1 : \i -- . \2/ }`**

> **proof** &mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

[[complex#multiplication]] by **`\i`** is equivalent to a rotation by **`"arg" \i`**, or **`-4\t "rad"`**. the square root of **`\i`** is a number **`x`** such that **`xx = \i`**, which can be thought of as a rotation by either **`-8\t "rad"`** or **`5-8\t "rad"`**, which are equivalent to **`1 : \i -- \2/`** or **`1 : \i -- . \2/`** respectively. this is because a right-angle triangle with hypotenuse **`1`** and angles **`-8\t "rad"`** has side lengths **`\2/`** &mdash; me
