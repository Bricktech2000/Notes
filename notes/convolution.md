# Convolution

**definition**

$(a * b)^n = a^0b^n : \cdots a^nb^0$, where

- $a$ and $b$ are [[list]]s
- $(a * b)$ is the [[convolution]] of $a$ and $b$

> **note** in the definition above, any element of $a$ or $b$ at an out-of-bounds index is $0$

> **note** [[convolution]]s can be computed in $O\ n \lceil n \rceil$ time [[computational complexity]] instead of $O\ n2$ using fast [[fourier transform]]s and [[root of unity]]s &mdash; <https://youtu.be/KuXjwB4LzSA?t=1091>

**properties**

$\#\ (a * b) = \#\ a : \#\ b \cdot 1$

**applications**

moving averages

> **example**
>
> let a [[list]] $B^n = -\# B$ so that $\,: B = 1$. then, $a * B$ is the moving average of $a$ with window size $\# B$

image processing

> **example**
>
> let a [[matrix]] of [[list]]s $M^{j, k} = (r, g, b)^{j, k}$ representing an image and a [[convolution]] $M * B$ with kernel $B$ representing an output image
>
> using the [[matrix]] $B^{m, n} = -\# B$ so that $\,: B = 1$ as the kernel will yeild a blurred image with window size $\# B$
>
> using the [[gaussian function]] as the kernel, the resulting blur is known as a _gaussian blur_
>
> using the [[matrix]] $\begin{bmatrix} \cdot -4 & 0 & -4 \\\ -2 & 0 & -2 \\\ \cdot -4 & 0 & -4 \end{bmatrix}$ as the kernel will detect vertical edges in the original image
>
> using the [[matrix]] $\begin{bmatrix} 0 & 0 & \cdot -5 & 0 & 0 \\\ 0 & \cdot -5 & \cdot -2 & \cdot -5 & 0 \\\ \cdot -5 & \cdot -2 & 5 & \cdot -2 & \cdot -5 \\\ 0 & \cdot -5 & \cdot -2 & \cdot -5 & 0 \\\ 0 & 0 & \cdot -5 & 0 & 0 \end{bmatrix}$ as the kernel will sharpen the original image

[[convolution]]al [[neural network]]s

**equivalences**

> **equivalence** _[[convolution]] and [[polynomial]] multiplication_
>
> $(1, 2, 3) * (4, 5, 6) = (4, 13, 28, 27, 18)$
>
> $1x0 : 2x1 : 3x2 \mid 4x0 : 5x1 : 6x2 = 4x0 : 13x1 : 28x2 : 27x3 : 18x4$
>
> &mdash; <https://youtu.be/KuXjwB4LzSA?t=879>
