# Math Notation

see [[conventional math notation]]

this note describes my custom [[math notation]], meant to solve inconsistencies in [[conventional math notation]]. it is not meant to be a fully formal system of [[mathematics]]; rather, it is built to be easy to understand and intuitive to use by mere humans.

## principles

- all equality [[operator]]s check for equality and return a [[boolean]], and it is implied that an [[expression]] on its own must evaluate to $\top$. this allows for [[boolean logic]] [[operator]]s to be applied on equalities explicitly as opposed informally
- [[set]]s are [[function]]s that return a [[boolean]] ([[set]]s are [[predicate]]s). this way, [[boolean logic]] [[operator]]s and [[set]] [[operator]]s are one and the same. other [[data structure]]s that work similarly include [[vector]]s, [[matrix]]es, [[sequence]]s, [[multiset]]s, [[ordered pair]]s...
- some [[operator]]s are identical but have different precedence as "more brackets means more explicit, but less brackets means less complex and less confusing"
- $\lfloor a \rfloor$ returns both positive and negative square roots ($\lfloor q2 \rfloor \equiv\ \because q$). the same is true for other reciprocals
- superscripts are modifiers (subscripts with special meanings). this distinction is extremely useful when working with [[forward propagation]] and [[backpropagation]] in [[neural network]]s, for example
- [[derivative]]s are not to be written as $y'$, but rather as their complete form $\delta y - \delta x$. this makes [[calculus notation]] way more intuitive
- all indices start at $0$, as they always should have
- [[rank polymorphism]] is supported over all [[operator]]s

## notation

also see [[trigonometric function]]s and [[calculus notation]]

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
- $\circ$ be any [[operator]]

### operator descriptions

| notation                             | description                                       | notes                                                 |
| ------------------------------------ | ------------------------------------------------- | ----------------------------------------------------- |
| $a : b$                              | addition or disjoint union                        |                                                       |
| $a \cdot b$                          | subtraction                                       |                                                       |
| $\because$ and $\therefore$          | $\pm$ and $\mp$                                   |                                                       |
| $a \smash\shortmid b$ and $a \mid b$ | multiplication                                    |                                                       |
| $a \text- b$ and $a - b$             | division                                          |                                                       |
| $[a]b$                               | exponentiation                                    | represents a power by convention                      |
| $a[b]$                               | exponentiation                                    | represents an exponential by convention               |
| $\lfloor a \rfloor b$                | $b$ th root of $a$                                | $b = 2$ if $b$ is omitted                             |
| $\lceil a \rceil b$                  | base-$b$ [[logarithm]] of $a$                     | $b = e$ if $b$ is omitted                             |
| $x \rightarrow E$                    | [[function]] literal                              | $f = x \rightarrow E \equiv f \smash\leftarrow x = E$ |
| $f \smash\leftarrow E$               | [[function]] application                          | uncommon, shorthand preferred                         |
| $a = b$                              | equality                                          | numerical equality by convention                      |
| $a < b$ and $a > b$                  | strict inequality                                 |                                                       |
| $a \le b$ and $a \ge b$              | non-strict inequality                             |                                                       |
| $a \land b$                          | logical AND or $\min$ function                    |                                                       |
| $a \lor b$                           | logical OR or $\max$ function                     |                                                       |
| $a\ /\ b$                            | logical difference                                | $a \land b = \bot$                                    |
| $a \equiv b$                         | equality                                          | logical equality by convention                        |
| $a \times b$                         | nonequality                                       | also serves as logical XOR                            |
| $a \vdash b$                         | implication, subset                               | $a$ implies $b$, $b$ for all $a$                      |
| $a \dashv b$                         | reverse implication, superset                     | $a$ for all $b$, $b$ implies $a$                      |
| $a_0 \circ a_1 \circ \dots a_n$      | with $n = 3$, $a_0 \circ a_1 \circ a_2 \circ a_3$ | step size is $\because 1$ if $a_1 \circ$ is omitted   |
| $a_0 \dots a_n$                      | with $n = 3$, $a_0, a_1, a_2, a_3$                | step size is $\because 1$ if $a_1$ is omitted         |
| $a \circ \dots$                      | the [[reduce function]] of $\circ$ on $a$         |                                                       |
| $f\ \ \vdots\ \ a \circ\dots b$      | $f\ (a \dots b) \circ\dots$                       |                                                       |
| $f\ \ \vdots\ \ x \rightarrow a$     | the [[limit]] of $f$ as $x$ approaches $a$        |                                                       |
| $x_{sub}$                            | the [[variable]] $x$ with a subscript $_{sub}$    |                                                       |
| $V^n$                                | the $n$ th component of $V$                       |                                                       |
| $A^i$                                | the $i$ th element of $A$                         |                                                       |
| $B^i$                                | the $i$ th element of $B$                         |                                                       |
| $M^{\braket{i, j}}$                  | the $i, j$ th element of $M$                      | uncommon, shorthand preferred                         |
| $M^\intercal$                        | the transpose [[matrix]] of $M$                   |                                                       |
| $\text-M$                            | the multiplicative inverse of $M$                 |                                                       |
| $P^b$                                | the $b$ th element of $P$                         |                                                       |
| $S\ a$                               | whether $a$ is element of $S$                     |                                                       |
| $M'\ a$                              | the number of elements $a$ in $M'$                |                                                       |
| $G\ a$                               | whether vertex $a$ is in $G$                      |                                                       |
| $G^{\braket{a, b}}$                  | the number of edges from $a$ to $b$ in $G$        | uncommon, shorthand preferred                         |

### shorthands

| shorthand                                                  | definition                                         | notes                                  |
| ---------------------------------------------------------- | -------------------------------------------------- | -------------------------------------- |
| $a \not\vdash b$, $a \ne b$, $a \not\le b$, $a \not< b$... | $/(a \vdash b)$, $/a = b$, $/a \le b$, $/a < b$... |                                        |
| $x\omega$                                                  | $[x]\omega$                                        |                                        |
| $ax$                                                       | $a \smash\shortmid x$                              |                                        |
| $f\ x$                                                     | $f \smash\leftarrow x$                             | common, longhand discouraged           |
| $x\ y \rightarrow E$                                       | $x \rightarrow y \rightarrow E$                    |                                        |
| $\braket{\ }$                                              | $\braket{\braket{\ }}$                             | see [[empty]] [[set]]                  |
| $(\ )$                                                     | $((\ ))$                                           | see [[multiset]]                       |
| $V^x, V^y, V^z$                                            | $V^0, V^1, V^2$                                    |                                        |
| $M^{i, j}$                                                 | $M^{\braket{i, j}}$                                | common, longhand discouraged           |
| $M^{i,}$                                                   | the $i$ th row of $M$                              |                                        |
| $M^{, j}$                                                  | the $j$ th column of $M$                           |                                        |
| $S = \braket{\braket{a \dots b}}$                          | $S\ x \equiv x = a \lor \dots x = b$               | see [[set]]                            |
| $P = \braket{f, t}$                                        | $P^\bot = f \land P^\top = t$                      | see [[ordered pair]]                   |
| $M = \begin{bmatrix} a & b \\\ c & d \end{bmatrix}$        | [[matrix]] literal                                 | see [[matrix]]                         |
| $M' = ((1, 2, 2, 2, 3, 3))$                                | [[multiset]] literal                               | see [[multiset]]                       |
| $x \rightarrow (a < x < b)$                                | the interval from $a$ to $b$                       |                                        |
| $A \circ B$                                                | $x \rightarrow A\ x \circ B\ x$                    | see [[rank polymorphism]]              |
| $A \circ B$                                                | $A\ x \circ B\ x$ for all $x$                      | $(\top \dots)$ is treated as $\top$    |
| $\delta y - \delta x$                                      | the [[derivative]] of $y$ with respect to $x$      | $\delta$ should be used instead of $d$ |
| $\int y \mid \delta x$                                     | the [[antiderivative]] of $y$ with respect to $x$  | $\delta$ should be used instead of $d$ |

### constants

| constant      | definition                                                   | notes                                       |
| ------------- | ------------------------------------------------------------ | ------------------------------------------- |
| $\varnothing$ | _undefined_                                                  | see [[improved expression evaluation]]      |
| $\top$        | logical true                                                 |                                             |
| $\bot$        | logical false                                                |                                             |
| $\tau$        | the ratio of the circumference of a [[circle]] to its radius | using $\pi$ is discouraged                  |
| $e$           | Euler's constant                                             | see [[eulers constant]]                     |
| $\iota$       | $\lfloor \cdot 1 \rfloor$                                    | see [[imaginary]], using $i$ is discouraged |
| $\Pi$         | the [[pi function]]                                          | using $\operatorname{fact}$ is discouraged  |

### operator properties

_in order of high to low precedence_

| operator                                      | associativity | unary identity | unary description     |
| --------------------------------------------- | ------------- | -------------- | --------------------- |
| $()\ \braket{}\ \Big[\Big]\ \ x\ x_a^i$       |               |                |                       |
| $[]\ \lfloor\rfloor\ \lceil\rceil$            |               |                |                       |
| $\shortmid \text-$                            | left          | $1$            | inverse               |
| $\delta\ \sin\ \#\ \smash\leftarrow$          | right-ish     |                |                       |
| $\, :\ \cdot\ \because\ \ \therefore$         | left          | $0$            | negation              |
| $\mid -$                                      | left          | $1$            | inverse               |
| $\int\ \ \vdots\ \ \dots\ \rightarrow\ \bmod$ | right-ish     |                |                       |
| $=\ne > \ge < \le$                            | AND           | $0$            | is (not) $0$          |
| $/$                                           | left          | $\top$         | [[boolean logic]] NOT |
| $\land\ \lor$                                 | left          |                |                       |
| $\dashv\ \vdash$                              | left          |                |                       |
| $\equiv \times$                               | AND           | $\top$         | [[boolean logic]] NOT |
| $,$                                           |               |                |                       |

> **note**: above,
>
> - $x$ represents [[variable]]s
> - $x_a^i$ represents subscripts and superscripts
> - $\leftarrow$ represents [[function]] application
> - $\rightarrow$ represents [[function]] literals
> - $\Big[\Big]$ represents [[matrix]] literals

> **note**: unary [[operator]]s have identical precedence to their binary counterparts, but are right associative

**definition** let $\circ$ be an [[operator]] with _AND_ associativity. then, $a \circ b \circ c \circ \dots\ \ \equiv\ \ a \circ b \land b \circ c \land c \circ \dots$

## variable scope

[[variable]] [[scope]] is currently entirely context-dependent. this is know to cause occasional issues, such as with [[derivative]]s: $\delta\ f\ x - \delta x$ could represent both the [[derivative]] of $f$ with respect to $x$ in the general sense, or the [[derivative]] of $f$ with respect to $x$ **at the point** $x$

## examples

[[quadratic formula]] $\cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$

definition of the [[set]] of [[complex]] numbers: $\mathbb C x \equiv x = a : b\iota \land \mathbb R a \land \mathbb R b$

definition of the implication / sub[[set]] / super[[set]] / “for all” symbol: $a \vdash b \equiv /a \lor b$ and $a \dashv b \equiv a \lor /b$

in [[set theory]], if $U$ is a sub[[set]] of $V$ and $V$ is a sub[[set]] of $U$, then $V$ is $U$. in this math notation: $(U\ x \vdash V\ x) \land (U\ x \dashv V\ x) \equiv U = V$

the probability density of the normal distribution in [[conventional math notation]]: $\frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2}$

compared to in my [[math notation]]: $-\lfloor \tau \sigma2 \rfloor - e[\ [x \cdot \mu - \sigma]2 - 2\ ]$

definition of factorials: $\operatorname{fact} n = 1 \mid \dots n$

the negation of an implication in my [[math notation]]: $B \vdash C \times B\ /\ C$ (_B implying C equals not (B without C)_ or _implication is the negation of set difference_ or _the negation of "for all B, C" is "there exists a B such that not C"_)

compared to [[conventional math notation]]: $\lnot (B \to C) = B \land \lnot C$ or $(a \in B \to a \in C) \iff a \notin B \backslash C$ or $B \subset C \iff \forall a \in C, a \notin B$

the resonant frequency of an LC circuit in [[conventional math notation]]: $f = \frac{1}{2 \pi \sqrt{LC}}$

compared to in my [[math notation]]: $f = -\tau \lfloor LC \rfloor$

see [[random math notation formulas]] for more examples
