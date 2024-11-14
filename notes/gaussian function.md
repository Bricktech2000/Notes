# Gaussian Function

&mdash; <https://en.wikipedia.org/wiki/Gaussian_blur>

**aka** _bell curve_

**definition**

**`G^ss p = --ss\tt/ -- [:p2 -- 2ss2]`**, where

- **`G^ss`** is the [[gaussian function]] with [[standard deviation]] **`ss`**
- **`p = (x ...)`** is a point

> **note** **`:p2 == :["abs" p]2`** and therefore **`G^ss (x ...) == G^ss ("abs" x)`**

> **note**
>
> the [[gaussian function]] above can be broken down as follows:
>
> **`x. --[x2]`** is the basic shape of the [[gaussian function]]
>
> **`x. --[x2 -- 2ss2]`** stretches the [[gaussian function]] horizontally so it has a [[standard deviation]] **`ss`**
>
> **`x. --ss\tt/ -- [x2 -- 2ss2]`** stretches the [[gaussian function]] vertically so it integrates to **`1`**, making it a [[probability density function]]
>
> **`p. --ss\tt/ -- [:p2 -- 2ss2]`** extends the [[gaussian function]] to take [[euclidean vector]]s as input while still returning a [[real]] number
>
> &mdash; me and <https://youtu.be/cy8r7WSuT1I?t=130>
