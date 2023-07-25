# Convolution

&mdash; <https://youtu.be/IaSGqQa5O-M>

&mdash; <https://youtu.be/KuXjwB4LzSA>

**definition**

**`(CC a b)^n = a^0 b^n : ... a^n b^0 = :(x -> a x | b (n.x))`**, where

- **`a`** and **`b`** are [[list]]s
- **`CC a b`** is the [[convolution]] of **`a`** and **`b`**

> **note** in the definition above, any element of **`a`** or **`b`** at an out-of-bounds index is taken to be **`0`**

> **note** this can be thought of as "the [[convolution]] of **`a`** and **`b`** at **`n`** is the [[dot product]] of elements of **`a`** and **`b`** at indices that sum to **`n`**"

> **note** [[convolution]]s can be computed in **`O (| /.\)`** time [[computational complexity]] instead of **`O [*]2`** using fast [[fourier transform]]s and [[root of unity]]s &mdash; <https://youtu.be/KuXjwB4LzSA?t=1091>

**definition**

**`(CC a b) n = $ a x | b (n.x) | dd x {@@ . .@@}`**

- **`a`** and **`b`** are [[function]]s
- **`CC a b`** is the [[convolution]] of **`a`** and **`b`**

**properties**

_length_ **`# (CC a b) == # a : # b . 1`**

_commutativity_ **`CC a b == CC b a`** or equivalently **`CC == rr CC`**

_associativity_ **`CC (CC a b) c == CC a (CC b c)`**

**applications**

moving averages

> **example**
>
> let a [[list]] **`B^* = -- # B`** so that **`:B = 1`**. then, **`CC a B`** is the moving average of **`a`** with window size **`# B`**

image processing

> **example**
>
> let a [[matrix]] of [[colors]]s **`MM^j,k M`** representing an image and a [[convolution]] **`CC M B`** with kernel **`B`** representing an output image
>
> using the [[matrix]] **`B^*,* = -- # B`** so that **`::B = 1`** as the kernel will yeild a blurred image with window size **`# B`**
>
> using the [[gaussian function]] as the kernel, the resulting blur is known as a _gaussian blur_
>
> using the [[matrix]] **`[].--4 & 0 & --4 && --2 & 0 & --2 && .--4 & 0 & --4[]`** as the kernel will detect vertical edges in the original image
>
> using the [[matrix]] **`[]0 & 0 & .--5 & 0 & 0 && 0 & .--5 & .--2 & .--5 & 0 && .--5 & .--2 & 5 & .--2 & .--5 && 0 & .--5 & .--2 & .--5 & 0 && 0 & 0 & .--5 & 0 & 0[]`** as the kernel will sharpen the original image

[[convolution]]al [[neural network]]s

sums of [[probability distribution]]s

> **example**
>
> let a fair dice with [[probability distribution]] **`d = x -> {0, -6} {{1 ... 6}} x`**. the probability of rolling two such die such that the sum of their values is **`n`** is **`(CC d d) n`**

**equivalences**

> **equivalence** _[[convolution]] and [[polynomial]] multiplication_
>
> **`CC (1, 2, 3) (4, 5, 6) = (4, 13, 28, 27, 18)`**
>
> **`1x0 : 2x1 : 3x2 | 4x0 : 5x1 : 6x2 = 4x0 : 13x1 : 28x2 : 27x3 : 18x4`**
>
> &mdash; <https://youtu.be/KuXjwB4LzSA?t=879>
