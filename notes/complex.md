# Complex

_the [[set]] of [[complex]] numbers_

**see** [[math notation]], [[imaginary unit]]

**definition**

**`CC x == x = a : bii /\ RR a /\ RR b`**

**notations**

_cartesian form_ **`z = a : bii`**

_polar form_ **`z = ||z||"cos" "arg" z : ||z||ii"sin" "arg" z = ||z||"cis" "arg" z = ||z|| ' [ii"arg" z]`**, where **`"cis" = "cos" : ii"sin" = aa -> [iiaa]`**

**aka** _Euler's formula notation_

**applications**

[[complex]] numbers are often intimately related to [[discrete mathematics]] &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

**properties**

**`CC < UU`**, see [[universal]]

_equality_ **`a : bii = c : dii == a = c /\ b = d`**

_addition_ **`(a : bii) : (c : dii) = (a : c) : (b : d)ii`**

_subtraction_ **`(a : bii) . (c : dii) = (a . c) : (b . d)ii`**

_multiplication in cartesian form_ **`a : bii | c : dii = ac : adii : bii c : bdii2 = (ac . bd) : (ad : bc)ii`**

_multiplication in polar form_ **`z | w = ||z|| ' [ii"arg" z] | ||w|| ' [ii"arg" w] = ||zw|| ' [ii | "arg" z : "arg" w]`**

_product of two [[complex#conjugate]]s are product of [[complex#modulus]]es_ **`a : bii | a . bii = a2 : b2 = ||a : bii|| | ||a . bii||`** &mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

**theorem** _De Moivre's Theorem_ **`["cis" aa]n = "cis" naa > ZZ n > RR aa`** &mdash; <https://en.wikipedia.org/wiki/De_Moivre%27s_formula>

> **proof** **`"cis" aa = [iiaa]`**. since **`[ [iiaa] ]n = [niiaa]`**, it must be that **`["cis" aa]n = "cis" naa`** &mdash; me

## Real Part

## Imaginary Part

let **`z = a : bii`**

**definitions**

_real part of a complex number_ **`z^re = a`**

_imaginary part of a complex number_ **`z^im = b`**

therefore, **`z = z^re : iiz^im`**

## Conjugate

_[[complex#conjugate]]_

**definition**

let **`z = a : bii`**

then, **`"conj" z = a . bii = z^re . iiz^im`** is the _complex conjugate_ of **`z`**

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

## Modulus

**aka** _magnitude, absolute value_

**definition** **`||z|| = \z^re 2 : z^im 2/`** where **`||z||`** is the _absolute value_ of **`z`**.

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

**definition** **`z = ||z|| ' [ii"arg" z]`** where **`"arg" z`** is the _argument_ of **`z`**

## Multiplication

geometrically, multiplying a [[complex]] number **`z`** by a [[complex]] number **`w`** is equivalent to rotating **`z`** by the [[angle]] **`"arg" w`** and then scaling it by a factor of **`||w||`**. this makes [[complex]] numbers useful for computing [[vector in rn]] rotations by choosing a **`w`** where **`||w|| = 1`** &mdash; <https://youtu.be/4KlvI_uK9zs?t=398>

> **proof** see properties

## square root of **`ii`**

**`\ii/ = { 1 : ii -- \2/ \/ 1 : ii -- . \2/ }`**

> **proof** &mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

[[complex#multiplication]] by **`ii`** is equivalent to a rotation by **`"arg" ii`**, or **`-4tt "rad"`**. the square root of **`ii`** is a number **`x`** such that **`x | x = ii`**, which can be thought of as a rotation by either **`-8tt "rad"`** or **`5-8tt "rad"`**, which are equivalent to **`1 : ii -- \2/`** or **`1 : ii -- . \2/`** respectively. this is because a right-angle triangle with hypotenuse **`1`** and angles **`-8tt "rad"`** has side lengths **`\2/`** &mdash; me
