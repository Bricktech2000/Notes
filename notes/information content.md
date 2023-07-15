# Information Content

**aka** _self-information_, _surprisal_, _Shannon information_

**definition** **`I S x = /--P S x\ b`**, where

- **`b`** is an arbitrary base for the [[logarithm]], with **`b {|-/\+} 1`**
- **`P S x`** is the [[probability]] of the [[event]] **`x`** occuring in the [[sample space]] **`S`**
- **`I S x`** is the [[information content]] of the [[event]] **`x`** occuring in the [[sample space]] **`S`**

> **note** with **`b = 2`**, [[information content]] is measured in [[shannon]]s; with **`b = ee`**, [[information content]] is measured in [[nat]]s

**properties**

let **`p = P S /\ i = I S`**. then,

- **`p x = 1 < i x = 0`** &mdash; an [[event]] that is certain to occur has zero [[information content]]
- **`p x -| p y < i x |- i y`** &mdash; an [[event]] that is less likely to occur has more [[information content]]
- **`p z = p x | p y < i z = i x : i y`** &mdash; the [[information content]] of two independent [[event]]s is the sum of the [[information content]] of both [[event]]s

> **note** it can be proven that the only [[function]]s satisfying these properties are of the form **`I S x = /--P S x\ b`** &mdash; <https://youtu.be/B3y0RsVCyrw?t=483>
