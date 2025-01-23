# Conventional Math Notation

**see** [[math notation]]

**tradeoffs**

[[conventional math notation]] is full of _special-case the simplest use-case_; it is [[invent]]ed, not [[discover]]ed

[[conventional math notation]] is [[flawed but established]]

- $\sqrt{}$ is not the inverse of $^2$ as it only yields the principal root
- $ab = a \times b$, $fg(x) = f(g(x))$, $\sin x = \sin(x)$, $xy = x * y$ ([[group#operation]])
- division can be written as horizontal bar, but multiplication cannot
- $4^2$, $\sqrt{4}$, $\log_2 4$ are the same operation hidden behind obtuse syntax
- equalities return [[boolean]]s, except when they do not
- [[variable]]s are one letter in length, except when they are not
- [[conventional math notation]] is neither 1D nor 2D; it is some sort of a 1.5D
- $\sin^2 x = (\sin x)^2$ whereas $f^2(x) = f(f(x))$ and $\sin^{-1} x = \arcsin x$
- $a < b < c$ means $a < b \land b < c$ but $a < b \ge c$ doesn't mean anything
- [[exponent]]s are right-associative while most other [[operator]]s are left-associative
- indices start at $1$
- $a(b)$ represents both multiplication and [[function]] application
- $\sum_{i = 0}^{n} x_i$ and $\prod_{i = 0}^{n} x_i$ are shameful at best
- [[matrix]] indices are ambiguous when written as a juxtaposition
- $(a, b)$ is a GCD and a tuple and a [[euclidean vector]] and an [[interval]]
- $\begin{pmatrix} a \\\ b \end{pmatrix}$ is a [[matrix]] and a [[euclidean vector]] and a [[set#combination]]
- $f^{(n)}$ is repeated [[derivative#differentiation]] whereas $f^{n}$ is not
- $f'$ is both a separate [[variable]] name and a [[derivative]]
- $f(1, 2)$ is both $f(1.2)$ and $f(1; 2)$
- $4 \equiv 1 \mod 3$ is awful
- $\frac{10}{\frac 2 5}$ and $\frac{\frac{10}{2}}{5}$ look practically identical
- $|x|y|z|$ is both $\operatorname{abs}(x \times \operatorname{abs}(y) \times z)$ and $\operatorname{abs}(x) \times y \times \operatorname{abs}(z)$
- $\mathbb N$ might or might not contain $0$. the same is true for $\mathbb Z^+$
- $2x = 2 \times x$ whereas $2 \frac 2 3 = 2 + \frac 2 3$, and $-1 \frac 1 4$ might or might not equal $-\frac 5 4$
- there exists no [[operator]] for unary division
- there exists no [[operator]] for function application
- implied multiplication is often informally evaluated before multiplication and division

other notations used contextually include:

- $-$ is used for both subtraction and denoting ranges
- $+$ is used for both addition and concatenation
- $=$ is used for both equality and assignment
- $.$ is used for both decimals and version strings

--- <https://whystartat.xyz/wiki/Main_Page> --- Justin Veilleux

--- <https://youtu.be/4x-BcYCiKCk>

--- _The notational conventions I adopted, and why_, by Edsger W. Dijkstra --- <https://www.cs.utexas.edu/users/EWD/transcriptions/EWD13xx/EWD1300.html> --- Ben Burk

_mathematical notation is both awful, and it turns out ambiguous, and, to be perfectly honest, impressionistic_ --- <https://youtu.be/HB5TrK7A4pI?t=1058>. the purpose of notation is efficient communication---it's the minimal amount of information needed to get an idea across---and so it is only natural that the result be impressionistic scribbles, and that's okay
