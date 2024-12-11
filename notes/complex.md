# Complex

_the [[set]] of [[complex]] numbers_

**see** [[math notation]], [[imaginary unit]]

**definition**

**`CC x == x = a : bii /\ RR {a /\ b}`**

**notations**

_cartesian form_ **`z = a : bii`**

_polar form, [[euler's formula]] notation_ **`z = "abs" z | ("cos" : ii"sin") "arg" z = "abs" z | [ii"arg" z]`**

**applications**

[[complex]] numbers are often intimately related to [[discrete mathematics]] --- 3B1B <https://youtu.be/bOXCLR3Wric>

**properties**

**`CC < UU`**, see [[set#universal set]]

_equality_ **`a : bii = c : dii == a = c /\ b = d`**

_addition_ **`(a : bii) : (c : dii) = (a : c) : (b : d)ii`**

_subtraction_ **`(a : bii) .. (c : dii) = (a .. c) : (b .. d)ii`**

_multiplication in cartesian form_ **`a : bii | c : dii = ac : adii : bii c : bdii2 = (ac .. bd) : (ad : bc)ii`**

_multiplication in polar form_ **`z | w = "abs" z | [ii"arg" z] | "abs" w | [ii"arg" w] = "abs" zw | [ii | "arg" z : "arg" w]`**

_product of two [[complex#conjugate]]s are product of [[complex#modulus]]es_ **`a : bii | a .. bii = a2 : b2 = "abs" (a : bii) | "abs" (a .. bii)`** --- <https://youtu.be/bOXCLR3Wric?t=1522>

**theorem** _De Moivre's Theorem_ **`["cis" aa]n = "cis" naa > ZZ n > RR aa`** --- <https://en.wikipedia.org/wiki/De_Moivre%27s_formula>

> **proof** **`"cis" aa = [iiaa]`**. since **`[ [iiaa] ]n = [niiaa]`**, it must be that **`["cis" aa]n = "cis" naa`** --- me

## Real Part

## Imaginary Part

let **`z = a : bii`**

**definitions**

_real part of a complex number_ **`"re" z = a`**

_imaginary part of a complex number_ **`"im" z = b`**

therefore, **`z = ("re" : ii"im") z`**

## Conjugate

_[[complex#conjugate]]_

**definition**

**`"conj" z == ("re..ii"im")`** is the _complex conjugate_ of **`z`**

**properties**

let **`CC {z /\ w} /\ RR c`**

**`"conj" (z : w) = "conj" z : "conj" w`**

**`"conj" cz = c"conj" z`**

**`"conj" z'w = "conj" z | "conj" w`**

**`"conj" z-w = "conj" z -- "conj" w`**

_[[function#self-inverse function]]_ **`"conj"2 z = z`**

**`RR z == "conj" z = z`**

**theorem** **`z"conj" z = ["abs" z]2 > CC z`**

**theorem** **`--z = "conj" z -- ["abs" z]2 > CC z`**

## Modulus

**aka** _magnitude, absolute value_

**definition** **`"abs" z = "abs" ("re" z, "im" z)`** where **`"abs" z`** is the _absolute value_ of **`z`**.

> **note** the [[real#absolute value]] can be thought of as "the [[distance]] of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

**properties**

let **`CC {z /\ w} /\ RR c`**

**`"abs" z = "abs""conj" z`**

**`"abs" zw = "abs" z | "abs" w`**

**`"abs" z-w = "abs" z -- "abs" w`**

_triangle inequality_ **`"abs" (z : w) -| "abs" {z : w}`**

**equiv** _triangle inequality with [[relation#transitive relation]]_

## Argument

**aka** _phase_

**definition** the _argument_ of a [[complex]] number **`z`** is the counterclockwise [[angle]] between the positive [[real]] axis and the [[line]] segment from the origin to the point **`("re" z, "im" z)`**

**definition** **`z = "abs" z | [ii"arg" z]`** where **`"arg" z`** is the _argument_ of **`z`**

## Multiplication

geometrically, multiplying a [[complex]] number **`z`** by a [[complex]] number **`w`** is equivalent to rotating **`z`** by the [[angle]] **`"arg" w`** and then scaling it by a factor of **`"abs" w`**. this makes [[complex]] numbers useful for computing [[euclidean vector]] rotations by choosing a **`w`** where **`"abs" w = 1`** --- <https://youtu.be/4KlvI_uK9zs?t=398>

> **proof** see properties

## square root of **`ii`**

**`\ii/ = { 1 : ii -- \2/ \/ 1 : ii -- .. \2/ }`**

> **proof** --- <https://www.youtube.com/watch?v=Z49hXoN4KWg>

[[complex#multiplication]] by **`ii`** is equivalent to a rotation by **`"arg" ii`**, or **`-4tt"rad"`**. the square root of **`ii`** is a number **`x`** such that **`x | x = ii`**, which can be thought of as a rotation by either **`-8tt"rad"`** or **`5-8tt"rad"`**, which are equivalent to **`1 : ii -- \2/`** or **`1 : ii -- .. \2/`** respectively. this is because a right-angle triangle with hypotenuse **`1`** and angles **`-8tt"rad"`** has side lengths **`--\2/`** --- me
