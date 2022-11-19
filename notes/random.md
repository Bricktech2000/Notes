# Random

```mermaid
graph LR
  A---B
  B-->C(asdf)
  B-->D(asdf)
```

```mermaid
graph LR
  fa:fa-check-->fa:fa-coffee
```

$1 - 2$

$1 \text- 2$

## sum of `n` first squares

```python
sum(i ** 2 for i in range(n + 1))
```

$$
i^n = \prod_{i=0}^n i
$$

$$
\Sigma_{i + 1} = \Sigma_i + (i + 1)^2 \\
% \Sigma_{i + 2} = \Sigma_i + (i - 1)^2 + i^2 \\
% \Sigma_{i + 2} = \Sigma_i + 2i^2 - 2i + 1 \\
% \Sigma_{i + 3} = \Sigma_i + (i - 2)^2 + 2i^2 - 2i + 1 \\
% \Sigma_{i + 3} = \Sigma_i + 2i^2 - 4i + 4 + 2i^2 - 2i + 1 \\
% \Sigma_{i + 3} = \Sigma_i + 4i^2 - 6i + 5 \\
% \Sigma_{i + 4} = \Sigma_i + (i - 3) ^ 2 + 4i^2 - 6i + 5 \\
% \Sigma_{i + 4} = \Sigma_i + (i - 3) ^ 2 + 4i^2 - 6i + 5 \\
$$

$$
\Sigma_i = \Sigma_{i - 1} + i^2 \\
\Sigma_i = i * i^2 - 2 * sum(i - 1) * i + \Sigma_{i - 1} \\
\Sigma_i = i^3 - 2 * i * i(i + 1) / 2 + \Sigma_{i - 1} \\
i^3 - 2 * i^2(i + 1) / 2 = i^2 \\

% i^3 - i^2 - 2 * i(i + 1) / 2 = 0
$$

## school situation

```mermaid
graph LR

A([predicted improvement of classes])
B(enjoyment of classes)
C([status of accommodations])
D(busyness during summer)
E(choice of classes during summer)
F([result of job application])
G(decision on dual degree)
H(decision on data science option)

A --> B
C -.-> B --> G --> H

F --> D
D --> E --> D
G -.-> E
```

```
I(audit thing)
I -.-> A
E ==> I
```

$$
P\ = \delta f - \delta x \\
P\ x, y = (\delta f - \delta x)\ x, y \\
$$

$$
P\ x, y = \delta f - \delta x \\
P\ 1, 2 = (\delta f - \delta x)\ 1, 2
$$

[[book]]

$\sin \theta - \cos \theta = y \text- r - x \text- r = y - x = \tan \theta$

## operator tests

$\lfloor \cdot x \rfloor = \diamond y$

$a \mid b$

$a \mid b$

$a\ \tiny\square\normalsize\ b$

$5 \sigma x \underline 0 2$

$x \underline 0 : 1 - \underline 0$

$x \sigma : 1 - \sigma$

$x \theta : 1 - \theta$

$\stackrel \cdot : $
$\stackrel : \cdot$
$\stackrel ! =$
$\stackrel = !$

$\cdot \atop : $
$\ : \atop \cdot$

$a : b$

$a \boxdot b$

$a \Box b$

$a \odot b$

$a \cdotledcirc b$

$\underline : a$

$a \shortmid b$

$a \smash\shortmid b$

$a \mid b$

$\lim_{x \to 0}$

$\lim\limits_{x \to 0}$

$\cdotleddash$

$\cdotledcirc$

$\odot$

$a \text- b$

$a - b$

$a \text- b$

$a {\scriptstyle-} b$

$a \textrm- b$

## stuff

- when something clicks
- if you're doing something challenging that requires you to focus intensely
- hard to switch from being on the internet to focusing

this is some block $$\LaTeX$$ inlined in the source code

$\delta\ (\delta\ f\ x - \delta x) - \delta x$

$\delta\ \delta\ f\ x - (\delta x \mid \delta x)$

$\cdot b : \lfloor b2 : 4ac \rfloor - 2a$

```python
point_ratio = n_in_area / (n_total - 2)
size_ratio = height / (max_height - min_height)

score = point_ratio / size_ratio
```

$$
S\ x \equiv x = 1 \lor x = 2 \lor x = 3\\\

S = \lbrace 1, 2, 3 \rbrace
$$

$$
S = \lambda x\ x2\\\

S = \lambda^x 2\\\

\lambda x\ (\delta\ f\ x - \delta x)\ 5\\\

f = x \to x2\\\

x \to \delta\ f\ x - \delta x \circ 5\\\

f = \lambda x \lambda y\ x : y
$$

integral of $\lceil x \rceil$

$\int \lceil x \rceil \mid \delta x$

$= \int (\int -x \mid \delta x) \mid \delta x$

$= \int ([x]\theta - \theta) : c \mid \delta x$

$= ([x]\theta \mid x - \theta - \theta : 1) : cx : c$

$= (\lceil x \rceil \mid x - \theta : 1) : cx : c$

$= (\lceil x \rceil \mid x) : cx : c$

$= (x \mid \lceil x \rceil : c) : c$

---

integral of $\lceil x \rceil$ using $\delta\ \lceil x \rceil - \delta x = \text-x \cdot (\delta\ \text-\theta - \delta x)$

$\int \lceil x \rceil \mid \delta x$

$= \int (\int (\text-x) \cdot (\delta\ \text-\theta - \delta x) \mid \delta x) \mid \delta x$

$= \int ([x]\theta - \theta) \cdot (\text-\theta) \mid \delta x$

<!-- $= ([x]\theta \mid x - \theta) \cdot x\text-\theta : c$ -->

<!-- $= ([x]\theta \mid x - \theta - \theta : 1) \cdot x\text-\theta : c$ -->

<!-- $= ([x]\theta - \theta : 1 \mid x - \theta) \cdot x\text-\theta : c$ -->

$= ([x]\theta \mid x - \theta - \theta : 1) \cdot x\text-\theta : c$

<!-- $= x\lceil x \rceil \cdot x\text-\theta : c$ -->

$= ([x]\theta \cdot 1 \cdot \theta \mid x - \theta - \theta : 1) : c$

$= (\lceil x \rceil \cdot 1 \mid x - \theta : 1) : c$

$= x \lceil x \rceil \cdot x : c$

<!-- $(x \mid [x]\theta \cdot 1 - \theta) \cdot x$ -->

<!-- $\theta : 1 \not \to 1$ -->

conclusion:

> "you can only replace all $\theta$ by $0$ at the end". as $\theta$ represents a number very close but not quite equal to $0$, all $\theta$ must be completely isolated from one another when replacing them by $0$

<!-- $(-\theta : 1) : 1$

$= (-1) : 1$

$= 2$

$(-\theta : 1) : 1$

$(1 : \theta : 1 - \theta : 1)$ -->

$-\lfloor \tau \sigma2 \rfloor - [e]([x \cdot \mu]2 - 2\sigma2)$

&mdash; <http://mirrors.ibiblio.org/CTAN/info/undergradmath/undergradmath.pdf>

$(x : 2][x \cdot 5)$

$(x : 2]2$

$2[x : 2)$

$e \langle x \cdot mu)$

$10[5]$

$[10]5$

$5 \shortmid x[1 \text- 3]$

```
[^\[!\$ ]\[[^\[]

[^\[]\[[^\[]
```

$-\lfloor \tau \sigma2 \rfloor - e[[x \cdot \mu]2 - 2\sigma2]$

$\omicron o$

$\Mu M$

let $S\ x \equiv x = 0$. then,

$(S' = \mathbb U\ /\ S) \equiv (S' = /S) \equiv (S'\ x \equiv /x = 0) \equiv (S'\ x \equiv x \ne 0)$

---

let $I = \lambda x\ \int -x \mid \delta x = \lceil x \rceil \cdot c'$. then,

$$
\begin{align*}
  & \lim_{x \to \infty} I\ x \text- 2 \cdot I\ x \\\
= & \lim_{x \to \infty} \lceil x \text- 2 \rceil \cdot \lceil x \rceil \\\
= & \lim_{x \to \infty} \lceil x \text- 2 - x \rceil \\\
= & \lim_{x \to \infty} \lceil 2 \rceil \\\
= & \lceil 2 \rceil \\\
\end{align*}
$$

---

$(x \rightarrow \delta\ f\ x - \delta x)\ 5$

$\lambda x\ (\delta\ f\ x - \delta x)\ 5$

$f\ x = 5x$

$f = \lambda x\ 5x$

$3 \mid x = 5$

$3 = 5 - x$

---

$y$ axis is the line $y = \cdot x - \tan \alpha$

$x$ axis is the line $y = x \mid \tan \alpha$

---

$y$ axis is the line $\cdot x \cos \theta = y \sin \theta$

$x$ axis is the line $x \sin \theta = y \cos \theta$

---

$a \tiny\leftarrow\normalsize b$

$\leftarrow \lessdot$

---

$e = \lim_{n \to \infty} [1 : -n]n = \lim_{n \to \infty} n - \lfloor \operatorname{fact} n \rfloor n$

$e = 1 \text- \operatorname{fact} 0 : 1 \text- \operatorname{fact} 1 : \dots$

---

$M\ o = n \dashv V^n = o$

$V^n = o \dashv M\ o = n$

---

$A \vdash B$ is not the same as $/A \lor B$

$A \vdash B$ has an implied "the operator yields _false_ if and only if there is a possibility the truth table yields _false_"

$/A \lor B$ has an implied "the operator yields _true_ if and only if there is a possibility the truth table yields _true_"

---

# todo

p indented

cite tags

https://example.com/

---

[[the worst programming language ever]]

[[carbon language talk]]

---

$X\ x = 1 \dashv X\ x > 0$ and $\lnot X\ x > 1$

$X\ x = X^\#$ (or) $X^\# = 1$

$\lnot X\ x > 1 \lor X^\# = 1$

---

$y = r \land \delta x = r\ \delta a$

---

$0 = (\#\ x \to x = 3)$

$\braket{\braket{3}}^\#$

$0 = \#\ x \to \times\ \mathbb N x \vdash \mathbb R x$

$x \to \top = x \to \mathbb N x \vdash \mathbb R x$

$\mathbb N x \vDash \mathbb R x$

$0\ \#\ /f$

$x \to \mathbb N x \vdash \mathbb R x$

---

- feedback that is a function of the inputs

&nbsp;

- effort to learn (deliberate practice, "active learning")
- many repetitions
- timely feedback

large dataset

adjusting weights

---

$y = 2x$ and therefore $\delta y - \delta x = 2$

$f\ (x, y) = x : y$

$\delta\ f\ (x, y) - \delta x = 1 : (\delta y - \delta x) = 1 : 2 = 3$

$\delta\ f\ (x', y) - \delta x' = 1 : (\delta y - \delta x') =$

$\delta\ (x \rightarrow f\ (x, y)) - \delta x$

---

$a \dots \lor$

$a \stackrel \lor \dots$

$a {\lor \atop \dots}$

$1 : 2 : \dots 5$

$a \dots \lor$

$a^0 \lor a^1 \lor \dots a^5$

$a \lor \dots$

$a : \dots$

$x = 5 \lor \dots$

```lua
S ((+) map.) reduce. A ==
```

---

[[sequence]]s starting with an [[even number]] $4 \mid 10 \mid 5 = 200$

[[sequence]]s starting with an [[odd number]] $5 \mid 10 \mid 5 = 250$

total number of [[sequence]]s: $200 : 250 = 450$

---

even-even-even: $4 \mid 4 \mid 3 = 48$

even-odd-even: $4 \mid 5 \mid 4 = 80$

odd-even-even: $5 \mid 5 \mid 4 = 100$

odd-odd-even: $5 \mid 4 \mid 5 = 100$

total: $48 : 80 : 100 : 100 = 328$

---

$(101 \cdot 10 \lfloor 93 \rfloor)a2\ :\ (139 \cdot 13 \lfloor 93 \rfloor)a\ \cdot\ 76\ -\ 108$

---

- first digit is not divisible by $5$
- second digit is not divisible by $3$
- third digit is divisible by $2$

```
12346789
124578
02468
```

---

$[a : b]n = (C\ n\ 0) \shortmid a[n] b0 : \cdots (C\ n\ n) \shortmid a0 b[n]$

---

$\psi\ \#\ \ \vdots\ \ G \le H$

$\int f\ x \mid \delta x\ \ \vdots\ \ a \cdot b$

$(\psi\ \ \vdots\ \ m \land n) = (\ )$

$\#\ \ \vdots\ \ a = b$

$: \cdots\ \ \vdots\ \ i : i'$

$\bmod\ 5\ \ \vdots\ \ 1 = 6$

$|x| \equiv \lfloor x2 \rfloor$

$|x| \equiv \lfloor [x] \rfloor$

---

```lua
x (1 min.) map.

0 5 range. dup. (+) outer.

1 one:
one one +
```

---

for all $n \ge 1$ and $c = 66$,

$f(n) = 60n^2 + 5n + 1 \le 60n^2 + 5n^2 + 1n^2 = 66n^2 \le c\ n^2 \le c\ g(n)$

and therefore $f(n) \le c\ g(n)$ and, by definition, $f \in O(n^2)$

---

let $f(n) = \log_a(n)$ and $g(n) = \log_b(n)$

$$
f(n) = \frac{\log(n)}{\log(a)}
$$

$$
g(n) = \frac{\log(n)}{\log(b)}
$$

$$
f(n) = g(n) \frac{\log(b)}{\log(a)} = g(n) \log_a(b)
$$

therefore, $f(n) \le c\ g(n)$ with $c = \log_a(b)$ for all $n$

---

$p = (1, 2, 3)$

$q$ is the goal

$(x, y, z)(1, \cdot 1, 1) = 4$

$p_0 = (4, 0, 0)$

$p_1 = (0, \cdot 4, 0)$

$p_2 = (0, 0, 4)$

> $p_0 \cdot p_1\ \check\mid\ p_2 \cdot p_1$

$p \cdot q \mid p_0 \cdot p_1 = 0 \land p \cdot q \mid p_2 \cdot p_1 = 0$

$(1, 2, 3) \cdot q \mid (4, 4, 0) = 0 \land (1, 2, 3) \cdot q \mid (0, 4, 4) = 0$

$\cdot 4q_0 : \cdot 8q_1 : 0 q_2 = 0 \land 0q_0 : \cdot 8q_1 : \cdot 12q_2 = 0$

$\cdot q_0 - 2 = q_1 \land q_1 = \cdot q_2 \mid 4 - 3$

$5 / 3, 4 / 3, \text{corresponding z}$

---

### Notion

- Social
- Personal
- Learning
- Hobbies
- Work
- House
- School
- Productivity
- Organization

### Notes

- tags
- conventions
- classes
- thinking
- learning
- fields
- other
- outdated

### Sync

- Random
- Projects
  - Programming
  - Other
  - RC
  - Thinking
  - 3D Printing
  - Arduino
  - TI84
  - Microbit
  - LEGO
- Howto
- Nonpublic
- Education

### ???

**see** [[why-how-what]]

- Organization
- movies and readings read?
- think about fix for notifications efficiency?
- talk / socialize?
- github field day trip?
- answer wealthsimple agent finance?

## Notion Changes

order in table

visibility in pages

properties shown in 4 views

color columns: no

---

$\int\ (\int f\ (x, y) \mid \delta x\ \ \vdots\ \ x_1 \cdot x_0) \mid \delta y\ \ \vdots\ \ y_1 \cdot y_0$

$\int\ (\int f\ (x, y) \mid \delta x) \mid \delta y$

$\bra{A}$

$\int$

$\mathbb{A}$

function $f$ is continuous on $[a, b]$

$$
\begin{test}

\emptyset
$$

$\varnothing$

$$
\varnothing
$$

---

$\sin x$

energy-momentum relation: $E2 = [pc]2 : [m_0 c2]2$

---

the number of nodes in a full binary tree is $n = 2^{h + 1} - 1$ (simple proof), and therefore the number of nodes in a complete binary tree is $n' = 2^{h + 1} - 1 - m$ where $m$ is the number of nodes missing on the last level of the tree. making the **huge** assumption that $k$ is an integer **and** that the criteria must hold for **all** integer values of $k$ with $k \ge 3$, we get $h = k - 1 + i$ for any natural $i$ and $m = 2$. the number of leaf nodes in a full binary tree is $l = 2^h$ (simple proof), and therefore the number of leaf nodes in the complete binary tree is $l' = 2^h - m = 2^{k - 1 + i} - 2$ for any natural $i$

answer: $f$ with $f(k) = 2^{k - 1 + i} - 2$ for any natural $i$

the number of nodes in a full binary tree is $n = 2^{h + 1} - 1$ (simple proof), and therefore the number of nodes in a complete binary tree is $n' = 2^{h + 1} - 1 - m$ where $m$ is the number of nodes missing on the last level of the tree. making the huge assumption that $k$ is an integer, we get $h = k - 1$ and $m = 2$. the number of leaf nodes in a full binary tree is $2^h$ (simple proof), and therefore the number of nodes in the last layer of the complete binary tree is $2^h - m = 2^{k - 1} - 2$. the two nodes missing on the last layer have a common parent node that is a leaf, and so the number of leaf nodes of the complete binary tree is $2^{k - 1} - 1$

answer: $f$ with $f(k) = 2^{k - 1} - 1$

if the number of nodes of a complete binary tree is $2^k - 3$, then the number of nodes in the full binary tree excluding its last layer is $2^{k - 1} - 1$. computing the difference, we get $2^{k - 1} - 2$ nodes on the last layer of the tree. given that the number of leaf nodes in the full binary tree of the same height as the complete binary tree is $2^{k - 1}$, we deduce that there are two nodes missing on the last layer of the complete binary tree. the two nodes missing on the last layer have a common parent node that is a leaf, and so the number of leaf nodes of the complete binary tree is $2^{k - 1} - 1$

---

$r \rightarrow [\cdot 1]r (C\ m\ r) [m \cdot r]n\ \ \vdots\ \ 0 : \cdots m$

$r \rightarrow [\cdot 1]r (C\ s\ r)\ \ \vdots\ \ 0 : \cdots r$

$$
Z = \frac{X - \mu}{\sigma}
$$

---

- interactivity, way better than book club
- learned the new `println` syntax
- apology about technical explanations

---

important:

- communication & teamwork

concerns:

- rejection of the state of the art
- worried about reinventing the wheel
- motivation for tedious tasks

---

let $a = (a^0, 13 - 5, 79 - 25, 367 - 125, 1891 - 625, 9343 - 3125, 46939 - 12625, \cdots)$

then, $a^n = [\cdot 2]n : 3[5]n - [5]n$

---

$\land \lor \lnot$

you've probably seen how in some classes we do boolean algebra with `+ - '` and in others we do boolean algebra with `∧ ∨ ¬`

---

$M \rightarrow \#\ M = \#\ M^\intercal \land \det M \ne 0$

$^i ^j$

$x^2$

$a \cdots b$ $a \ldots b$

$1 + \cdots 2$ $1 + \ldots 2$

$1 + \cdots + 2$ $1 + \ldots + 2$

$\mod 3\ \ \vdots\ \ 1 = 4$

$0.5 = -2 = \text-2$

$\sin x \mid \sin x = [\sin x]2$

$\operatorname{asin} x = y \equiv \sin y = x$

$f\ 2\text-3$

$f\ 2 - 3$

$x : 1 \mid x \cdot 1 \mid x2 \cdot 2$

$x \rightarrow c \le x \le d \land x \ne 5$

---

[[set#subset]]

---

$f\ x = x : 1 \mid x \cdot 2 - x : 1$

$f\ x = x \cdot 2$

$f(x) = \displaystyle \frac{(x + 1)(x - 2)}{x + 1}$

$a \theta b - \theta = ab$

$[a : b\epsilon]2 = a2 : 2ab\epsilon : b2\epsilon2$

let $b = \delta a - \delta X$. then, $\delta a2 - \delta X = 2ab$

$ab = 2b$

$ab2 = 2b2$

$F((a -> b) \cdot (b -> c)) = F(a -> b) \cdot F(b -> c)$
