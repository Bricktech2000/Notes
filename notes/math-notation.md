# Math Notation

see [[conventional-math-notation]]

this note describes my custom [[math-notation]], meant to solve inconsistencies in [[conventional-math-notation]]. it is not meant to be a fully formal system of [[mathematics]]; rather, it is built to be easy to understand and intuitive to use by mere humans.

## principles

- all equality [[operator]]s check for equality and return a [[boolean]], and it is implied that an [[expression]] on its own must evaluate to $\top$. this allows for [[boolean-logic]] [[operator]]s to be applied on equalities explicitly as opposed informally
- [[set]]s are [[function]]s that return a [[boolean]] ([[set]]s are [[predicate]]s). this way, [[boolean-logic]] [[operator]]s and [[set]] [[operator]]s are one and the same. other [[data-structure]]s that work similarly include [[vector]]s, [[matrix]]es, [[sequence]]s, [[multiset]]s, [[ordered-pair]]s...
- some [[operator]]s are identical but have different precedence as "more brackets means more explicit, but less brackets means less complex and less confusing"
- $\lfloor a \rfloor$ returns both positive and negative square roots ($\lfloor q2 \rfloor \equiv\ \because q$). the same is true for other reciprocals
- superscripts are modifiers (subscripts with special meanings). this distinction is especially useful when working with [[forward-propagation]] and [[backpropagation]] in [[neural-network]]s, for example
- [[derivative]]s are not to be written as $y'$, but rather as their complete form $\delta y - \delta x$. this makes [[calculus-notation]] way more intuitive
- all indices start at $0$, as they always should have

## notation

also see [[trigonometric-function]]s and [[calculus-notation]]

### operator descriptions

| notation                                                       | description                                    | notes                                                 |
| -------------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| $a : b$                                                        | addition                                       |                                                       |
| $a \cdot b$                                                    | subtraction                                    |                                                       |
| $\because$ and $\therefore$                                    | $\pm$ and $\mp$                                |                                                       |
| $a \smash\shortmid b$ and $a \mid b$                           | multiplication                                 |                                                       |
| $a \text- b$ and $a - b$                                       | division                                       |                                                       |
| $[a]b$                                                         | exponentiation                                 | represents a power by convention                      |
| $a[b]$                                                         | exponentiation                                 | represents an exponential by convention               |
| $\lfloor a \rfloor b$                                          | $b$ th root of $a$                             | $b = 2$ if $b$ is omitted                             |
| $\lceil a \rceil b$                                            | base-$b$ [[logarithm]] of $a$                  | $b = e$ if $b$ is omitted                             |
| $x \rightarrow E$ where $E$ is an [[expression]]               | [[function]] literal                           | $f = x \rightarrow E \equiv f \smash\leftarrow x = E$ |
| $f \smash\leftarrow E$ where $E$ is an [[expression]]          | [[function]] application                       | uncommon, shorthand preferred                         |
| $a = b$                                                        | equality                                       | numerical equality by convention                      |
| $a < b$ and $a > b$                                            | strict inequality                              |                                                       |
| $a \le b$ and $a \ge b$                                        | non-strict inequality                          |                                                       |
| $a \land b$                                                    | logical AND                                    |                                                       |
| $a \lor b$                                                     | logical OR                                     |                                                       |
| $a\ /\ b$                                                      | logical difference                             | $a \land b = \bot$                                    |
| $a \equiv b$                                                   | equality                                       | logical equality by convention                        |
| $a \times b$                                                   | nonequality                                    | also serves as logical XOR                            |
| $a \vdash b$                                                   | implication, subset                            | $a$ implies $b$, $b$ for all $a$                      |
| $a \dashv b$                                                   | reverse implication, superset                  | $a$ for all $b$, $b$ implies $a$                      |
| $x_0 \mid x_1 \mid \dots x_n$ where $\mid$ is any [[operator]] | with $n = 3$, $x_0 \mid x_1 \mid x_2 \mid x_3$ | step size is $\because 1$ if $x_1 \mid$ is omitted    |
| $x_0 \dots x_n$                                                | with $n = 3$, $x_0, x_1, x_2, x_3$             | step size is $\because 1$ if $x_1$ is omitted         |
| $x_{sub}$                                                      | the [[variable]] $x$ with a subscript $_{sub}$ |                                                       |
| $V^n$ where $V$ is a [[vector]]                                | the $n$ th component of $V$                    |                                                       |
| $a^i$ where $a$ is a [[sequence]]                              | the $i$ th element of $a$                      |                                                       |
| $b^i$ where $b$ is a [[series]]                                | the $i$ th element of $b$                      |                                                       |
| $M^{\braket{i, j}}$ where $M$ is a [[matrix]]                  | the $i, j$ th element of $M$                   | uncommon, shorthand preferred                         |
| $M^\intercal$ where $M$ is a [[matrix]]                        | the transpose of $A$                           |                                                       |
| $M^-$ where $M$ is a [[matrix]]                                | the multiplicative inverse of $A$              |                                                       |
| $P^b$ where $P$ is an [[ordered-pair]]                         | the $b$ th element of $P$                      |                                                       |
| $S\ a$ where $S$ is a [[set]]                                  | whether $a$ is element of $S$                  |                                                       |
| $M\ a$ where $M$ is a [[multiset]]                             | the number of elements $a$ in $M$              |                                                       |
| $G\ v$ where $G$ is a [[graph]]                                | whether vertex $v$ is in $G$                   |                                                       |
| $G^{\braket{v, w}}$ where $G$ is a [[graph]]                   | the number of edges from $v$ to $w$ in $G$     | uncommon, shorthand preferred                         |

### shorthands

| shorthand                                                          | definition                                         | notes                                  |
| ------------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------- |
| $a \not\vdash b$, $a \ne b$, $a \not\le b$, $a \not< b$...         | $/(a \vdash b)$, $/a = b$, $/a \le b$, $/a < b$... |                                        |
| $x\omega$ where $x$ is a [[variable]] and $\omega$ is a [[number]] | $[x]\omega$                                        |                                        |
| $ax$ where $x$ is a [[variable]]                                   | $a \smash\shortmid x$                              |                                        |
| $f\ x$ where $f$ is a [[function]]                                 | $f \smash\leftarrow x$                             | common, longhand discouraged           |
| $x\ y \rightarrow E$ where $E$ is an [[expression]]                | $x \rightarrow y \rightarrow E$                    |                                        |
| $V^x$, $V^y$ and $V^z$ where $V$ is a [[vector]]                   | the $x$, $y$ and $z$ components of $V$             |                                        |
| $M^{i, j}$ where $M$ is a [[matrix]]                               | $M^{\braket{i, j}}$                                | common, longhand discouraged           |
| $M^{i,}$ where $M$ is a [[matrix]]                                 | the $i$ th row of $M$                              |                                        |
| $M^{, j}$ where $M$ is a [[matrix]]                                | the $j$ th column of $M$                           |                                        |
| $S = \braket{\braket{a \dots b}}$                                  | $S\ x \equiv x = a \lor \dots x = b$               | see [[set]]                            |
| $P = \braket{f, t}$                                                | $P^\bot = f \land P^\top = t$                      | see [[ordered-pair]]                   |
| $M = \begin{bmatrix} a & b \\\ c & d \end{bmatrix}$                | matrix literal                                     | see [[matrix]]                         |
| $x \rightarrow (a < x < b)$                                        | the closed interval from $a$ to $b$                | same can be used for open intervals    |
| $A \vdash B$ where $\vdash$ is any #think [[operator]]             | $A\ x \vdash B\ x$ for all $x$                     | commonly $\equiv \dashv \vdash$ #think |
| $A \cdot B$ where $\cdot$ is any #think [[operator]]               | $x \rightarrow A\ x \cdot B\ x$                    | commonly $: \cdot \mid -$ #think       |
| $\delta y - \delta x$                                              | the [[derivative]] of $y$ with respect to $x$      | $\delta$ should be used instead of $d$ |
| $\int y \mid \delta x$                                             | the [[antiderivative]] of $y$ with respect to $x$  | $\delta$ should be used instead of $d$ |

### constants

| constant      | definition                                                   | notes                                  |
| ------------- | ------------------------------------------------------------ | -------------------------------------- |
| $\varnothing$ | _undefined_                                                  | see [[improved-expression-evaluation]] |
| $\top$        | logical true                                                 |                                        |
| $\bot$        | logical false                                                |                                        |
| $\tau$        | the ratio of the circumference of a [[circle]] to its radius | using $\pi$ is discouraged             |
| $e$           | Euler's constant                                             | see [[eulers-constant]]                |
| $i$           | $\lfloor \cdot 1 \rfloor$                                    | see [[imaginary]]                      |

### operator properties

_in order of high to low precedence_

| operator                                | associativity | unary identity | unary description |
| --------------------------------------- | ------------- | -------------- | ----------------- |
| $()\ \braket{}\ \Big[\Big]\ \ x\ x_a^i$ |               |                |                   |
| $[ ]\ \lfloor\rfloor\ \lceil\rceil$     |               |                |                   |
| $\shortmid \text-$                      | left          | $1$            | inverse           |
| $\delta\ \sin\ \smash\leftarrow$        | right-ish     |                |                   |
| $\ :\ \cdot\ \because\ \ \therefore$    | left          | $0$            | negation          |
| $\mid -$                                | left          | $1$            | inverse           |
| $\int \lim\ \dots\ \rightarrow$         | right         |                |                   |
| $=\ne\gt\ge\lt\le$                      | AND           | $0$            | is (not) $0$      |
| $/$                                     | left          | $\top$         | logical NOT       |
| $\land\ \lor$                           | left          |                |                   |
| $\dashv\ \vdash$                        | left          |                |                   |
| $\equiv \times$                         | AND           | $\top$         | logical NOT       |
| $,$                                     |               |                |                   |

> **note**: above,
>
> - $x$ represents [[variable]]s
> - $x_a^i$ represents subscripts and superscripts
> - $\leftarrow$ represents [[function]] application
> - $\rightarrow$ represents [[function]] literals
> - $\Big[\Big]$ represents [[matrix]] literals

> **note**: unary [[operator]]s have identical precedence to their binary counterparts, but are right associative

> **definition**: let $=$ be an [[operator]] with _AND_ associativity. then, $a = b = c = \dots\ \ \equiv\ \ a = b \land b = c \land c = \dots$

## variable scope

[[variable]] scope is currently entirely context-dependent. this is know to cause occasional issues, such as with [[derivative]]s: $\delta\ f\ x - \delta x$ could represent both the [[derivative]] of $f$ with respect to $x$ in the general sense, or the [[derivative]] of $f$ with respect to $x$ **at the point** $x$ as $(x \rightarrow \delta\ f\ x - \delta x)\ x \equiv \delta\ f\ x - \delta x$.

## examples

[[quadratic-formula]]: $\cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$

definition of the [[set]] of [[complex]] numbers: $\mathbb C x \equiv x = a : b \lfloor \cdot 1 \rfloor \land \mathbb R a \land \mathbb R b$

definition of the implication / sub[[set]] / super[[set]] / “for all” symbol: $a \vdash b \equiv /a \lor b$ and $a \dashv b \equiv a \lor /b$

in [[set-theory]], if $U$ is a sub[[set]] of $V$ and $V$ is a sub[[set]] of $U$, then $V$ is $U$. in this math notation: $(U\ x \vdash V\ x) \land (U\ x \dashv V\ x) \equiv U = V$

the probability density of the normal distribution in [[conventional-math-notation]]: $\frac{1}{\sqrt{2 \sigma^2 \pi}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}$

compared to in my [[math-notation]]: $-\lfloor \tau \sigma2 \rfloor - e[\ [x \cdot \mu]2 - 2\sigma2\ ]$

definition of factorials: $\operatorname{fact} n = 1 \mid \dots n$

the negation of an implication in my [[math-notation]]: $B \vdash C \times B\ /\ C$ (_B implying C equals not (B without C)_ or _implication is the negation of set difference_ or _the negation of "for all B, C" is "there exists a B such that not C"_)

compared to [[conventional-math-notation]]: $\lnot (B \to C) = B \land \lnot C$ or $(a \in B \to a \in C) \iff a \notin B \backslash C$ or $B \subset C \iff \forall a \in C, a \notin B$

the resonant frequency of an LC circuit in [[conventional-math-notation]]: $f = \frac{1}{2 \pi \sqrt{LC}}$

compared to in my [[math-notation]]: $f = -\tau \lfloor LC \rfloor$

see [[random-math-notation-formulas]] for more examples

<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
