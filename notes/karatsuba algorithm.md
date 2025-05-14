# Karatsuba Algorithm

the [[karatsuba algorithm]] is a [[divide and conquer]] [[algorithm]] for multiplication that works by reducing an $n$-digit multiplication into three $\frac n 2$-digit multiplications

if $x = aB + b$ and $y = (cB + d)$ then $xy = z_2B^2 + z_1B + z_0$, where:

- $z_0 = bd$
- $z_2 = ac$
- $z_1 = ad + bc = (a + b)(c + d) - z_0 - z_2$

which can be computed with 3 multiplications instead of 4, at the cost of a few more additions and subtractions

an input of $n$ [[binary]] digits can be split in half $\log_2 n$ times, and at each split we recurse on ourselves $3$ times, which gives $3^{\log_2 n} = n^{\log_2 3}$ single-digit multiplications, and thus a time [[computational complexity]] of $O\ (n.\ n^{1.585})$

## ---

--- <https://youtu.be/KzT9I1d-LlQ?t=733>

--- <https://youtu.be/cCKOl5li6YM>

--- <https://en.wikipedia.org/wiki/Karatsuba_algorithm>
