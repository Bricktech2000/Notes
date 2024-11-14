# Trigonometric Function

**see** [[math notation]], [[function]], [[hyperbolic function]]

**definition** _geometrically_

let **`(x, y)`** be a point on the unit [[circle]] and let **`aa`** be the [[angle]] from the positive x-axis counterclockwise to that point. then,

- **`x = "cos" aa`**
- **`y = "sin" aa`**
- **`"tan" aa = "sin" aa -- "cos" aa`**

> **note** _[[mnemonic]]_ SOHCAHTOA

**definition** _in terms of [[euler's constant]]_ &mdash; <https://math.stackexchange.com/questions/2853279/the-interconnection-between-hyperbolic-functions-and-eulers-formula>

- **`"cos" aa = [iiaa] : [.iiaa] -- 2`**
- **`"sin" aa = [iiaa] . [.iiaa] -- 2`**
- **`"tan" aa = "sin" aa -- "cos" aa`**

**definition** _in terms of [[hyperbolic function]]s_

the following follow from [[euler's formula]]: &mdash; <https://youtu.be/HnHnEnkZpJA?t=14m3s>

- **`"cos" aa = "cosh" iiaa`**
- **`"sin" aa = .ii"sinh" iiaa`**
- **`"tan" aa = .ii"tanh" iiaa`**

**properties**

_[[function#periodic function]]_ **`"sin" (aa : tt) = "sin" aa`**

_[[function#periodic function]]_ **`"cos" (aa : tt) = "cos" aa`**

_[[function#periodic function]]_ **`"tan" (aa : -2tt) = "tan" aa`**

_[[function#even function]]_ **`"cos" .aa = "cos" aa`**

_[[function#odd function]]_ **`"sin" .aa = ."sin" aa`**

_[[function#odd function]]_ **`"tan" .aa = ."tan" aa`**

**theorems**

**theorem** _sine law_ let a triangle with sides **`a, b, c`** and [[angle]]s **`A, B, C`** where an [[angle]] is opposite the side whose [[variable]] is the same letter. then, **`"sin" A -- a = "sin" B -- b = "sin" C -- c`**

**theorem** _cosine law_ let a triangle with sides **`a, b, c`** and [[angle]]s **`A, B, C`** where an [[angle]] is opposite the side whose [[variable]] is the same letter. then, **`c2 = a2 : b2 . 2ab"cos" C`**

**theorem** _harmonic addition theorem_ **`a"cos" : b"sin"`** can always be rewritten into the form **`c"cos"(aa:)`**, where **`c2 = a2 : b2`** and **`"tan" aa = .b-a`** &mdash; <https://mathworld.wolfram.com/HarmonicAdditionTheorem.html> &mdash; <https://youtu.be/bn38o3u0lDc?t=72>

## inverses

**definitions**

**`y = "sin" x == x = {"asin" y \/ ."asin" y : -2tt} : ttn /\ ZZ n`**

**`y = "cos" x == x = {"acos" y \/ ."acos" y} : ttn /\ ZZ n`**

**`y = "tan" x == x = "atan" y : -2ttn /\ ZZ n`**

**properties**

[[improved expression evaluation]] superposition #xxx

_[[function#multivalued function]]_ **`"asin" x = "asin" x : tt = ."asin" .x`**

_[[function#multivalued function]]_ **`"acos" x = "acos" x : tt = ."acos" x`**

_[[function#multivalued function]]_ **`"atan" x = "atan" x : -2tt = ."atan" x`**

## reciprocals

_cosecant_ **`-"sin" aa`**

_secant_ **`-"cos" aa`**

_cotangent_ **`-"tan" aa`**

_cosecant_ **`-"asin" x`**

_secant_ **`-"acos" x`**

_cotangent_ **`-"atan" x`**

## identities

&mdash; <https://youtu.be/7gigNsz4Oe8?t=4383>

also see [[euler's formula]]

### pythagorean identities

**`["sin" aa]2 : ["cos" aa]2 = 1`**

**`1 : ["tan" aa]2 = [-"cos" aa]2`** &mdash; derived by dividing by **`"cos" aa`**

**`[-"tan" aa]2 : 1 = [-"sin" aa]2`** &mdash; derived by dividing by **`"sin" aa`**

### angle sum identities

**`"sin" (x : y) = ("sin" x | "cos" y) : ("cos" x | "sin" y)`**

**`"cos" (x : y) = ("cos" x | "cos" y) . ("sin" x | "sin" y)`**

difference identities can be computed using the sum identities above

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=5103>

### double- and half-angle identities

**`"sin" 2x = 2 | "sin" x | "cos" x`** &mdash; derived from angle sum identities

**`"cos" 2x = ["cos" x]2 .["sin" x]2`** &mdash; derived from angle sum identities

**`"cos" 2x = 1 .2["sin" x]2`** &mdash; derived by substituting by the pythagorean identity

**`"cos" 2x = 2["cos" x]2 . 1`** &mdash; derived by substituting by the pythagorean identity

**`["sin" x]2 = 1 . "cos" 2x -- 2`** &mdash; derived by solving for **`["sin" x]2`**

**`["cos" x]2 = 1 : "cos" 2x -- 2`** &mdash; derived by solving for **`["cos" x]2`**

## derivatives

**see** [[derivative]]

**`dd "sin" x -- dd x = "cos" x`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21115>

**`dd "cos" x -- dd x = ."sin" x`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21193>

**`dd "tan" x -- dd x = [-"cos" x]2`**

**`dd -"sin" x -- dd x = . | -"sin" x | -"tan" x`**

**`dd -"cos" x -- dd x = -"cos" x | "tan" x`**

**`dd -"tan" x -- dd x = .[-"sin" x]2`**

**`dd "asin" x -- dd x = -- \1.x2/`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29016>

**`dd "acos" x -- dd x = . -- \1.x2/`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29111>

**`dd "atan" x -- dd x = -- 1 : x2`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29233>
