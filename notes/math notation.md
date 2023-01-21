# Math Notation

**see** [[conventional math notation]]

this note describes my own [[math notation]], meant to solve inconsistencies in [[conventional math notation]]. it is not meant to be a fully formal system of [[mathematics]]; rather, it is built to be easy to understand and intuitive to use by mere humans.

this [[math notation]] obviously cannot be used to communicate ideas to people who do not know it, but it has made my own experience of using [[mathematics]] much more enjoyable; it has become a tool for thought. being able to use a single relatively well-defined notation in various [[mathematics]] [[fields]] that conventially use their own made up notation has been invaluable

## principles

- all equality [[operator]]s check for equality and return a [[boolean]], and it is implied that an [[expression]] on its own must evaluate to $\top$. this allows for [[boolean algebra#operators]] to be applied on equalities explicitly as opposed informally
- [[set]]s are [[function]]s that return a [[boolean]] ([[set]]s are [[predicate]]s). this way, [[boolean algebra#operators]] and [[set]] [[operator]]s are one and the same. other [[data structure]]s that work similarly include [[vector]]s, [[matrix]]es, [[sequence]]s, [[multiset]]s, [[ordered pair]]s...
- some [[operator]]s are identical but have different precedence as "more brackets means more explicit, but less brackets means less complex and less confusing"
- $\lfloor a \rfloor$ returns both positive and negative square roots ($\lfloor q2 \rfloor =\!=\ \because q$). the same is true for other reciprocals
- superscripts are modifiers (subscripts with special meanings). this distinction is extremely useful when working with [[forward propagation]] and [[backpropagation]] in [[neural network]]s, for example
- [[derivative]]s are not to be written as $y'$, but rather as their complete form $\delta y - \delta x$. this makes [[calculus notation]] way more intuitive
- all indices start at $0$, as they always should have
- [[rank polymorphism]] is supported over all [[operator]]s

## Notation

also see [[trigonometric function]]s, [[hyperbolic function]]s and [[calculus notation]]

let:

- $M$ be a [[matrix]]
- $V$ be a [[vector]]
- $P$ be an [[ordered pair]]
- $M'$ be a [[multiset]]
- $G$ be a [[graph]]
- $E$ be an [[expression]]
- $x$ be a [[variable]]
- $f$ be a [[function]]
- $A$ be a [[sequence]]
- $B$ be a [[series]]
- $a, b$ be any mathematical objects
- $A, B$ be any mathematical objects with rank greater than $1$
- $n, i$ be [[natural]] numbers
- $b$ be a [[boolean]]
- $\omega$ be any [[number]]
- $*$ be any [[operator]]

### numbers

- [[natural]]s are represented using the [[decimal]] [[positional numeral system]]
- [[integer]]s are represented using the unary $\cdot$ [[operator]] on [[natural]]s
- [[rational]]s are represented using the $\text-$ [[operator]] on [[integer]]s
- [[real]]s are represented using other [[operator]]s and [[limit]]s
- [[p-adic]]s are currently represented using their own notation

> **note** both percentages and decimals are to be represented as [[rational]]s. the $\%$ sign and the decimal $.$ are to be avoided

> **note** to make [[number]]s easier to read, spaces may be introduced in where a decimal $.$ would conventially be used. for example, the value of $49 - 25$ can be written as $1\ 96\text-100$

### operator descriptions

| $\LaTeX$                               | `ASCII`                                | description                                       | notes                                               |
| -------------------------------------- | -------------------------------------- | ------------------------------------------------- | --------------------------------------------------- |
| $a : b$                                | `a : b`                                | $b$ added to $a$                                  |                                                     |
| $a \cdot b$                            | `a . b`                                | $b$ subtracted from $a$                           |                                                     |
| $\because$ <br> $\therefore$           |                                        | $\pm$ <br> $\mp$                                  |                                                     |
| $a \smash\shortmid b$ <br> $a \mid b$  | `a'b` <br> <code>a \| b</code>         | $a$ multiplied by $b$                             |                                                     |
| $a \text- b$ <br> $a - b$              | `a-b` <br> `a -- b`                    | $a$ divided by $b$                                |                                                     |
| $[a]b$ <br> $a[b]$                     | `[a]b` <br> `a[b]`                     | $a$ to the power of $b$                           | $a = e$ if $a$ is omitted                           |
| $\lfloor a \rfloor b$                  | `\a/b`                                 | the $b$th root of $a$                             | $b = 2$ if $b$ is omitted                           |
| $\lceil a \rceil b$                    | `/a\b`                                 | the base-$b$ [[logarithm]] of $a$                 | $b = e$ if $b$ is omitted                           |
| $x \rightarrow E$                      | `x -> E`                               | [[function]] literal                              | $f = x \rightarrow E =\!= f \leftarrow x = E$       |
| $f \leftarrow E$                       | `f <- E`                               | [[function]] application                          | uncommon, shorthand preferred                       |
| $a = b$ <br> $a =\!= b$                | `a = b` <br> `a == b`                  | $a$ is equal to $b$                               | also serves as [[boolean algebra#xnor]]             |
| $a + b$ <br> $a \times b$              | `a + b` <br> `a >< b`                  | $a$ is not equal to $b$                           | also serves as [[boolean algebra#xor]]              |
| $a \dashv b$ <br> $a < b$              | <code>a -\| b</code> <br> `a < b`      | $a$ is at most $b$                                | identical to [[boolean algebra#implication]]        |
| $a \vdash b$ <br> $a > b$              | <code>a \|- b</code> <br> `a > b`      | $a$ is at least $b$                               | identical to [[boolean algebra#implication]]        |
| $a\ \bot\ b$ <br> $a \land b$          | `a F b ` <br> `a /\ b`                 | the minimum of $a$ and $b$                        | identical to [[boolean algebra#and]]                |
| $a\ \top\ b$ <br> $a \lor b$           | `a T b` <br> `a \/ b`                  | the maximum of $a$ and $b$                        | identical to [[boolean algebra#or]]                 |
| $a_0 * a_1 * \cdots a_n$               | `a_0 * a_1 * ... a_n`                  | with $n = 3$, $a_0 * a_1 * a_2 * a_3$             | step size is $1$ or $\cdot 1$ if $a_1 *$ is omitted |
| $a_0 \cdots a_n$                       | `a_0 ... a_n`                          | with $n = 3$, $a_0, a_1, a_2, a_3$                | step size is $1$ or $\cdot 1$ if $a_1$ is omitted   |
| $f\ \braket{a * b}$                    | `f {a * b}`                            | $f\ a * f\ b$                                     |                                                     |
| $f\ \braket{x \rightarrow a}$          | `f {x -> a}`                           | the [[limit]] of $f$ as $x$ approaches $a$        |                                                     |
| $A * B$                                | `A * B`                                | $x \rightarrow A\ x * B\ x$                       | see [[rank polymorphism]]                           |
| $A * a$                                | `A * a`                                | $x \rightarrow A\ x * a$                          | see [[rank polymorphism]]                           |
| $a\ (\mid * :)\ b$                     | <code>a (\|\*:) b</code>               | $(a \mid b) * (a : b)$                            | works with any binary [[operator]]                  |
| $(\# * f)\ a$                          | `(#*f) a`                              | $(\#\ a) * (f\ a)$                                | works with any unary [[operator]]                   |
| $\,* A$                                | `* A`                                  | the [[reduce function]] of $A$ with $*$           |                                                     |
| $\delta y - \delta x$                  | `dy -- dx`                             | the [[derivative]] of $y$ with respect to $x$     | $\delta$ should be used instead of $d$              |
| $\int y \mid \delta x$                 | <code>S y \| dx</code>                 | the [[antiderivative]] of $y$ with respect to $x$ | $\delta$ should be used instead of $d$              |
| $x_{sub}$                              | `x_sub`                                | the [[variable]] $x$ with a subscript $_{sub}$    |                                                     |
| $A^i$ <br> $B^i$ <br> $V^n$ <br> $P^b$ | `A^i` <br> `B^i` <br> `V^n` <br> `P^b` | $A\ i$ <br> $B\ i$ <br> $V\ n$ <br> $P\ b$        | to be used for indices                              |
| $M^{i,j}$ <br> $G^{a, b}$              | `M^i,j` <br> `G^a, b`                  | $M\ i\ j$ <br> $G\ a\ b$                          | to be used for indices                              |
| $S\ a$ <br> $M'\ a$ <br> $G\ a$        | `S a` <br> `M' a` <br> `G a`           | $S\ a$ <br> $M\ a$ <br> $G\ a$                    | to be used for membership                           |

### constants

| $\LaTeX$      | `ASCII` | definition                                                   | notes                                       |
| ------------- | ------- | ------------------------------------------------------------ | ------------------------------------------- |
| $\varnothing$ |         | _undefined_                                                  | see [[improved expression evaluation]]      |
| $\top$        | `T`     | [[boolean]] _true_                                           |                                             |
| $\bot$        | `F`     | [[boolean]] _false_                                          |                                             |
| $\circ$       | `*`     | [[function]] [[composition#identity]]                        |                                             |
| $\tau$        | `t`     | the ratio of the circumference of a [[circle]] to its radius | using $\pi$ is discouraged                  |
| $e$           | `e`     | [[euler's constant]]                                         |                                             |
| $\iota$       | `i`     | $\lfloor \cdot 1 \rfloor$                                    | see [[imaginary]]. using $i$ is discouraged |
| $\rho$        | `p`     | $f\ a\ b \rightarrow f\ b\ a$                                | see [[matrix#transpose]]                    |
| $\Pi$         | `II`    | the [[pi function]]                                          | using $\operatorname{fact}$ is discouraged  |
| $\#$          | `#`     | the number of "links" in a [[function]]                      | #todo define rigorously                     |
| $\psi$        |         | the [[multiset]] of prime factors of a [[natural]]           | see [[psi function in mat2348]]             |

### operator properties

_in order of high to low precedence_

| operator                                      | associativity | unary identity | unary description       |
| --------------------------------------------- | ------------- | -------------- | ----------------------- |
| $()\ \braket{}\ \Big[ \Big]\ \ x\ x_a^i\ 123$ |               |                |                         |
| $[]\ \lfloor\rfloor\ \lceil\rceil$            |               |                |                         |
| $\shortmid \text-$                            | left          | $1$            | multiplicative inverse  |
| $\delta\ \sin\ \#\ \circ\ \leftarrow$         | left-ish      |                |                         |
| $\, :\ \cdot\ \because\ \ \therefore$         | left          | $0$            | negation                |
| $\mid -$                                      | left          | $1$            | multiplicative inverse  |
| $\int\ \braket{}\ \cdots\ \rightarrow\ \bmod$ | left-ish      |                |                         |
| $\bot\ \top$                                  | left          |                |                         |
| $=\ \dashv\ \vdash\ +$                        | AND           | $\top$         | [[boolean algebra#not]] |
| $\land\ \lor$                                 | left          |                |                         |
| $=\!=\ <\ >\ \times$                          | AND           | $\top$         | [[boolean algebra#not]] |
| $,$                                           |               |                |                         |

> **note** above,
>
> - $x$ represents [[variable]]s
> - $x_a^i$ represents subscripts and superscripts
> - $123$ represents [[number]] literals
> - $\leftarrow$ represents [[function]] application
> - $\rightarrow$ represents [[function]] literals
> - $\Big[ \Big]$ represents [[matrix]] literals

> **note** unary [[operator]]s have identical precedence to their binary counterparts, but are right associative

**definition** let $*$ be an [[operator]] with _AND associativity_. then, $a * b * c * \cdots =\!= a * b \land b * c \land c * \cdots$

### shorthands

| shorthand                             | definition                          | notes                        |
| ------------------------------------- | ----------------------------------- | ---------------------------- |
| $x\omega$                             | $[x]\omega$                         |                              |
| $ax$                                  | $a \smash\shortmid x$               |                              |
| $f\ E$                                | $f \leftarrow E$                    | common, longhand discouraged |
| $x\ y \rightarrow E$                  | $x \rightarrow y \rightarrow E$     |                              |
| $\braket{\ }$                         | $\braket{\braket{\ }}$              | see [[empty]] [[set]]        |
| $(\ )$                                | $((\ ))$                            | see [[multiset]]             |
| $V^x, V^y, V^z$                       | $V^0, V^1, V^2$                     |                              |
| $M^{i, j}$                            | $M^{\braket{i, j}}$                 | common, longhand discouraged |
| $x \rightarrow (a \dashv x \dashv b)$ | the closed interval from $a$ to $b$ |                              |
| $f\ g\ \circ$                         | $x \rightarrow f\ (g\ x)$           | $\circ$ is a "hole"          |

## variable scope

[[variable]] [[scope]] is currently entirely context dependent. this is know to cause occasional issues, such as with [[derivative]]s: $\delta\ f\ x - \delta x$ could represent both the [[derivative]] of $f$ with respect to $x$ in the general sense, or the [[derivative]] of $f$ with respect to $x$ **at the point** $x$

## examples

### comparison with conventional notation

| description                                 | in this [[math notation]]                                             | in [[conventional math notation]]                                                                        |
| ------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| the [[quadratic formula]]                   | $x = \cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$                     | $\displaystyle x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$                                            |
| definition of [[complex]] numbers           | $\mathbb C x =\!= x = a : b\iota \land \mathbb R a \land \mathbb R b$ | $\displaystyle \mathbb C = \{a + bi : a, b \in \mathbb R\}$                                              |
| the [[gaussian function]]                   | $G^\sigma\ p = -\lfloor \tau \sigma2 \rfloor - [\,: p2 - 2\sigma2]$   | $\displaystyle G(x, y, \dots) = \frac{1}{\sqrt{2 \pi\sigma^2}} e^{-\frac{x^2 + y^2 + \dots}{2\sigma^2}}$ |
| [[limit]] form of a [[derivative]]          | $f\ x \cdot f\ a - x \cdot a\ \braket{x \rightarrow a}$               | $\displaystyle \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}$                                         |
| definition of factorials                    | $\operatorname{fact} n = 1 \mid \cdots n$                             | $\displaystyle n! = \prod_{i = 1}^n i$                                                                   |
| the resonant [[frequency]] of an LC circuit | $f = -\tau \lfloor LC \rfloor$                                        | $\displaystyle f = \frac{1}{2 \pi \sqrt{LC}}$                                                            |
| definition of the [[dot product]]           | $\,: xy$                                                              | $\displaystyle x \cdot y  = \sum_{i=1}^n x_i y_i$                                                        |
| definition of the [[outer product]]         | $x\ \circ \mid\ y\ \circ$                                             | $\displaystyle (x \otimes y)_{i, j}  = x_i \times y_j$                                                   |
| definition of the [[cartesian product]]     | $\bot\ (x, y)\ \circ$                                                 | $\displaystyle x \times y = \lbrace (x, y) \mid x \in X \text{ and } y \in Y \rbrace$                    |
| definition of [[vector in rn#magnitude]]    | $\vert v \vert = \lfloor \,: v2 \rfloor$                              | $\displaystyle \vert v \vert = \sqrt{x^2 + y^2 + \dots}$ with $v = (x, y, \dots)$                        |
| definition of [[set]] difference            | $A \land +B$                                                          | $\displaystyle A \setminus B = \{x \in A : x \notin B\}$                                                 |
| the [[p-adic#absolute value]]               | $\vert n \vert^p = -p[\psi\ n\ p]$                                    | not really doable in a concise way without using plain English                                           |

definition of the [[boolean algebra#implication]] / [[set#subset]] / [[set#superset]] / [[quantifier#universal quantifier]] in this [[math notation]]: $a \dashv b =\!= +a \lor b$ and $a \vdash b =\!= a \lor +b$

in [[set theory]], if $U$ is a [[set#subset]] of $V$ and $V$ is a [[set#subset]] of $U$, then $V$ is $U$. in this [[math notation]]: $U \vdash V \land U \dashv V =\!= U = V$

the negation of a [[boolean algebra#implication]] in this [[math notation]]: $B \dashv C \times B \land +C$

in [[conventional math notation]]: $\lnot (B \to C) = B \land \lnot C$ or $(a \in B \to a \in C) \iff a \notin B \backslash C$ or $B \subset C \iff \forall a \in C, a \notin B$

definition of the $n$th column of a [[matrix]]: $\rho\ M\ n$ or $M \circ n$

### comparison between LaTeX and ASCII

| $\LaTeX$                                                              | `ASCII`                         |
| --------------------------------------------------------------------- | ------------------------------- |
| $x = \cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$                     | `x = .b : \b2.4ac/ -- 2a`       |
| $[\iota\tau] = 1$                                                     | `[it] = 1`                      |
| $\lceil e \rceil = 1$                                                 | `/e\ = 1`                       |
| $\iota = \lfloor \cdot 1 \rfloor$                                     | `i = \.1/`                      |
| $\int f\ x \mid \delta x$                                             | <code>S f x \| dx</code>        |
| $\mathbb C x =\!= x = a : b\iota \land \mathbb R a \land \mathbb R b$ | `C x == x = a : bi /\ Ra /\ Rb` |
| $B \dashv C \times B \land +C$                                        | <code>B -\| C >< B /\ +C</code> |
| $S \rightarrow \,\land\ \circ \dashv S$                               | <code>S -> /\ \* -\| S</code>   |
