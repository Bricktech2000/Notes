# Gaussian Function

&mdash; <https://en.wikipedia.org/wiki/Gaussian_blur>

**aka** _bell curve_

**definition**

**`G^\s p = -- \s \\t/ -- [:p2 -- 2\s2]`**, where

- **`G^\s`** is the [[gaussian function]] with [[standard deviation]] **`\s`**
- **`p = (x ...)`** is a point

> **note** **`:p2 == ||p||2`** and therefore **`G^\s (x ...) == G^\s ||(x ...)||`**

> **note**
>
> the [[gaussian function]] above can be broken down as follows:
>
> **`x -> -- [x2]`** is the basic shape of the [[gaussian function]]
>
> **`x -> -- [x2 -- 2\s2]`** stretches the [[gaussian function]] horizontally so it has a [[standard deviation]] **`\s`**
>
> **`x -> -- \s \\t/ -- [x2 -- 2\s2]`** stretches the [[gaussian function]] vertically so it integrates to **`1`**, making it a [[probability distribution#probability density function]]
>
> **`p -> -- \s \\t/ -- [:p2 -- 2\s2]`** extends the [[gaussian function]] to take [[vector in rn]]s as input while still returning a [[real]] number
>
> &mdash; me and <https://youtu.be/cy8r7WSuT1I?t=130>
