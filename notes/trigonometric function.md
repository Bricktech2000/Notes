# Trigonometric Function

**see** [[math notation]], [[function]], [[hyperbolic function]]

**definition**

let **`(x, y)`** be a point on the unit [[circle]] and let **`\q`** be the [[angle]] from the positive x-axis counterclockwise to that point. then,

**`x = "cos" \q /\ y = "sin" \q`**, and **`"tan" \q = "sin" \q -- "cos" \q`**

> **[[mnemonic]]** SOHCAHTOA

**properties**

_[[function#periodic function]]_ **`"sin" (\q : \t) = "sin" \q`**

_[[function#periodic function]]_ **`"cos" (\q : \t) = "cos" \q`**

_[[function#periodic function]]_ **`"tan" (\q : -2\t) = "tan" \q`**

_[[function#even function]]_ **`"cos" (.\q) = "cos" \q`**

_[[function#odd function]]_ **`"sin" (.\q) = ."sin" \q`**

_[[function#odd function]]_ **`"tan" (.\q) = ."tan" \q`**

## inverse functions

**see** [[function#inverse]]

**definitions**

**`y = "sin" x == x = "asin" y : \tn /\ ZZ n`**

**`y = "cos" x == x = "acos" y : \tn /\ ZZ n`**

**`y = "tan" x == x = "atan" y : -2\tn /\ ZZ n`**

## reciprocal functions

**see** [[function#reciprocal]]

**`-"sin" \q`**

**`-"cos" \q`**

**`-"tan" \q`**

**`-"asin" x`**

**`-"acos" x`**

**`-"atan" x`**

## identities

&mdash; <https://youtu.be/7gigNsz4Oe8?t=4383>

### pythagorean identities

**`["sin" \q]2 : ["cos" \q]2 = 1`**

**`["tan" \q]2 : 1 = [-"cos" \q]2`** &mdash; derived by dividing by **`"cos" \q`**

**`[-"tan" \q]2 : 1 = [-"sin" \q]2`** &mdash; derived by dividing by **`"sin" \q`**

### angle sum identities

**`"sin" (x : y) = ("sin" x | "cos" y) : ("cos" x | "sin" y)`**

**`"cos" (x : y) = ("cos" x | "cos" y) .("sin" x | "sin" y)`**

difference identities can be computed using the sum identities above

> **proof** &mdash; <https://youtu.be/7gigNsz4Oe8?t=5103>

### double- and half-angle identities

**`"sin" 2x = 2 | "sin" x | "cos" x`** &mdash; derived from angle sum identities

**`"cos" 2x = ["cos" x]2 .["sin" x]2`** &mdash; derived from angle sum identities

**`"cos" 2x = 1 .2["sin" x]2`** &mdash; derived by substituting by the pythagorean identity

**`"cos" 2x = 2["cos" x]2 . 1`** &mdash; derived by substituting by the pythagorean identity

**`["sin" x]2 = 1 . "cos" 2x -- 2`** &mdash; derived by solving for **`["sin" x]2`**

**`["cos" x]2 = 1 : "cos" 2x -- 2`** &mdash; derived by solving for **`["cos" x]2`**

## cosine and sine "law"s

**theorem** _sine law_ let a triangle with sides **`A, B, C`** and [[angle]]s **`a, b, c`** where an [[angle]] is opposite the side whose [[variable]] is the same letter. then, **`"sin" a -- A = "sin" b -- B = "sin" c -- C`**

**theorem** _cosine law_ let a triangle with sides **`A, B, C`** and [[angle]]s **`a, b, c`** where an [[angle]] is opposite the side whose [[variable]] is the same letter. then, **`a2 = b2 : c2 . 2bc"cos" A`**

## Derivatives

**see** [[derivative]]

**`\d "sin" x -- \d x = "cos" x`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21115>

**`\d "cos" x -- \d x = ."sin" x`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=21193>

**`\d "tan" x -- \d x = [-"cos" x]2`**

**`\d -"sin" x -- \d x = . | -"sin" x | -"tan" x`**

**`\d -"cos" x -- \d x = -"cos" x | "tan" x`**

**`\d -"tan" x -- \d x = .[-"sin" x]2`**

**`\d "asin" x -- \d x = -- \1.x2/`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29016>

**`\d "acos" x -- \d x = . -- \1.x2/`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29111>

**`\d "atan" x -- \d x = -- 1 : x2`** &mdash; [[proof]] <https://youtu.be/HfACrKJ_Y2w?t=29233>
