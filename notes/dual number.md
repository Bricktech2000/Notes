# Dual Number

--- <https://en.wikipedia.org/wiki/Dual_number>

#stub

**definition** the _dual numbers_ are a [[number]] system with numbers of the form $a + b\varepsilon$ with $a, b \in \mathbb R$ and $\varepsilon^2 = 0 \land \varepsilon \neq 0$

**properties**

> **note** note the similarity with [[derivative rules]]

$(a + b\varepsilon) + (c + d\varepsilon) = (a + b) + (c + d)\varepsilon$

$(a + b\varepsilon) \cdot (c + d\varepsilon) = ab + (ad + bc)\varepsilon$

$\frac{a + b\varepsilon}{c + d\varepsilon} = \frac a b + \frac{bc - ad}{c^2}\varepsilon$

$(a + b\varepsilon)^n = a^n + n(a + b\varepsilon)^{n - 1}\varepsilon$

$f\ (a + b\varepsilon) = f\ a + (f'\ a)b\varepsilon$ for any [[function#analytic function]] $f$

> **proof** the [[taylor series]] of $f\ (a + b\varepsilon) = \sum_{n = 0}^\infty\ \frac{f^{(n)}\ a}{n!} (b\varepsilon)^n = f\ a + (f'\ a)b\varepsilon$ because all terms involving $\varepsilon^n, n \geq 2$ are trivially $0$ --- Wikipedia

## matrix representation

$a + b\varepsilon.\ \begin{bmatrix}a & b \\ 0 & a\end{bmatrix}$ is a [[morphism#homomorphism]] from [[dual number]]s under addition and multiplication to [[matrix]]es under [[matrix#addition]] and [[matrix#multiplication]]
