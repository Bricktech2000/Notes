# Math Notation

**see** [[conventional math notation]]

this note describes my own [[math notation]], meant to solve inconsistencies in [[conventional math notation]]. it is not meant to be a fully formal system of [[mathematics]]; rather, it is built to be easy to understand and intuitive to use by mere humans.

this [[math notation]] obviously cannot be used to communicate ideas to people who do not know it, but it has made my own experience of using [[mathematics]] much more enjoyable. being able to use a single relatively well defined notation in various [[mathematics]] [[fields]] that conventially use their own made up notation has been invaluable

## principles

- all equality [[operator]]s check for equality and return a [[boolean]], and it is implied that an [[expression]] on its own must evaluate to $\top$. this allows for [[boolean algebra#operators]] to be applied on equalities explicitly as opposed informally
- [[set]]s are [[function]]s that return a [[boolean]] ([[set]]s are [[predicate]]s). this way, [[boolean algebra#operators]] and [[set]] [[operator]]s are one and the same. other [[data structure]]s that work similarly include [[vector]]s, [[matrix]]es, [[sequence]]s, [[multiset]]s, [[ordered pair]]s...
- some [[operator]]s are identical but have different precedence as "more brackets means more explicit, but less brackets means less complex and less confusing"
- $\lfloor a \rfloor$ returns both positive and negative square roots ($\lfloor q2 \rfloor \equiv\ \because q$). the same is true for other reciprocals
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
- $\circ$ be any [[operator]]

### numbers

- [[natural]]s are represented using the [[decimal]] [[positional numeral system]]
- [[integer]]s are represented using the unary $\cdot$ [[operator]] on [[natural]]s
- [[rational]]s are represented using the $\text-$ [[operator]] on [[integer]]s
- [[real]]s are represented using other [[operator]]s and [[limit]]s
- [[p-adic]]s are currently represented using their own notation

> **note** both percentages and decimals are to be represented as [[rational]]s. the $\%$ sign and the decimal $.$ are to be avoided

> **note** to make [[number]]s easier to read, spaces may be introduced in where a decimal $.$ would conventially be used. for example, the value of $49 - 25$ can be written as $1\ 96\text-100$

```
: . | -- - [] () / \ <> -> <- = < > <= >= / === |- -| ... /\ \/ o d S e i # II ; `

-=][)(*&^%$#@!`~_+|}{:"<>?/.,;'\

missing: \shortmid \vdots \times \top \bot \tau \psi \mathbb \lfloor \rfloor \lceil \rceil ^ \sigma
```

`x = .b : \b2.4ac/ -- 2a` $x = \cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$

`e[it] = 1` $e[\iota\tau] = 1$

`/e\ = 1` $\lceil e \rceil = 1$

`i = \.1/` $\iota = \lfloor \cdot 1 \rfloor$

`S f x | dx` $\int f\ x \mid \delta x$

`C x == x = a : bi /\ Ra /\ Rb` $\mathbb C x =\!= x = a : b\iota \land \mathbb R a \land \mathbb R b$

### operator descriptions

| notation                             | description                                       | notes                                               |
| ------------------------------------ | ------------------------------------------------- | --------------------------------------------------- |
| $a : b$                              | addition or disjoint union                        |                                                     |
| $a \cdot b$                          | subtraction                                       |                                                     |
| $\because$ and $\therefore$          | $\pm$ and $\mp$                                   |                                                     |
| $a \smash\shortmid b$ and $a \mid b$ | multiplication                                    |                                                     |
| $a \text- b$ and $a - b$             | division                                          |                                                     |
| $[a]b$                               | exponentiation                                    | represents a power by convention                    |
| $a[b]$                               | exponentiation                                    | represents an exponential by convention             |
| $\lfloor a \rfloor b$                | $b$ th root of $a$                                | $b = 2$ if $b$ is omitted                           |
| $\lceil a \rceil b$                  | base-$b$ [[logarithm]] of $a$                     | $b = e$ if $b$ is omitted                           |
| $x \rightarrow E$                    | [[function]] literal                              | $f = x \rightarrow E \equiv f \leftarrow x = E$     |
| $f \leftarrow E$                     | [[function]] application                          | uncommon, shorthand preferred                       |
| $a = b$                              | equality                                          | numerical equality by convention                    |
| $a < b$ and $a > b$                  | strict inequality                                 |                                                     |
| $a \le b$ and $a \ge b$              | non-strict inequality                             |                                                     |
| $a \land b$                          | logical AND or $\min$ function                    |                                                     |
| $a \lor b$                           | logical OR or $\max$ function                     |                                                     |
| $a\ /\ b$                            | logical difference                                | $a \land b = \bot$                                  |
| $a \equiv b$                         | equality                                          | logical equality by convention                      |
| $a \times b$                         | nonequality                                       | also serves as logical XOR                          |
| $a \vdash b$                         | implication, [[set#subset]]                       | $a$ implies $b$, $b$ for all $a$                    |
| $a \dashv b$                         | reverse implication, [[set#superset]]             | $a$ for all $b$, $b$ implies $a$                    |
| $a_0 \circ a_1 \circ \cdots a_n$     | with $n = 3$, $a_0 \circ a_1 \circ a_2 \circ a_3$ | step size is $\because 1$ if $a_1 \circ$ is omitted |
| $a_0 \cdots a_n$                     | with $n = 3$, $a_0, a_1, a_2, a_3$                | step size is $\because 1$ if $a_1$ is omitted       |
| $f\ \ \vdots\ \ a \circ b$           | $f\ a \circ f\ b$                                 |                                                     |
| $f\ \ \vdots\ \ x \rightarrow a$     | the [[limit]] of $f$ as $x$ approaches $a$        |                                                     |
| $x_{sub}$                            | the [[variable]] $x$ with a subscript $_{sub}$    |                                                     |
| $V^n$                                | the $n$ th component of $V$                       |                                                     |
| $A^i$                                | the $i$ th element of $A$                         |                                                     |
| $B^i$                                | the $i$ th element of $B$                         |                                                     |
| $M^{\braket{i, j}}$                  | the $i, j$ th element of $M$                      | uncommon, shorthand preferred                       |
| $P^b$                                | the $b$ th element of $P$                         |                                                     |
| $S\ a$                               | whether $a$ is element of $S$                     |                                                     |
| $M'\ a$                              | the number of elements $a$ in $M'$                |                                                     |
| $G\ a$                               | whether vertex $a$ is in $G$                      |                                                     |
| $G^{\braket{a, b}}$                  | the number of edges from $a$ to $b$ in $G$        | uncommon, shorthand preferred                       |

### shorthands

| shorthand                                                  | definition                                         | notes                                  |
| ---------------------------------------------------------- | -------------------------------------------------- | -------------------------------------- |
| $a \not\vdash b$, $a \ne b$, $a \not\le b$, $a \not< b$... | $/(a \vdash b)$, $/a = b$, $/a \le b$, $/a < b$... |                                        |
| $x\omega$                                                  | $[x]\omega$                                        |                                        |
| $ax$                                                       | $a \smash\shortmid x$                              |                                        |
| $f\ E$                                                     | $f \leftarrow E$                                   | common, longhand discouraged           |
| $x\ y \rightarrow E$                                       | $x \rightarrow y \rightarrow E$                    |                                        |
| $\braket{\ }$                                              | $\braket{\braket{\ }}$                             | see [[empty]] [[set]]                  |
| $(\ )$                                                     | $((\ ))$                                           | see [[multiset]]                       |
| $V^x, V^y, V^z$                                            | $V^0, V^1, V^2$                                    |                                        |
| $M^{i, j}$                                                 | $M^{\braket{i, j}}$                                | common, longhand discouraged           |
| $M^{i,}$                                                   | the $i$ th row of $M$                              |                                        |
| $M^{, j}$                                                  | the $j$ th column of $M$                           |                                        |
| $P = \braket{f, t}$                                        | $P^\bot = f \land P^\top = t$                      | see [[ordered pair]]                   |
| $S = \braket{\braket{a \cdots b}}$                         | $S\ x \equiv x = a \lor \cdots x = b$              | see [[set]]                            |
| $V = (a \cdots b)$                                         | $V^0 = a \land \cdots V^n = b$                     | see [[vector in rn]]                   |
| $M' = ((1, 2, 2, 2, 3, 3))$                                | [[multiset]] literal                               | see [[multiset]]                       |
| $M = \begin{bmatrix} a & b \\\ c & d \end{bmatrix}$        | [[matrix]] literal                                 | see [[matrix]]                         |
| $x \rightarrow (a < x < b)$                                | the interval from $a$ to $b$                       |                                        |
| $A \circ B$                                                | $x \rightarrow A\ x \circ B\ x$                    | see [[rank polymorphism]]              |
| $A \circ B$                                                | $A\ x \circ B\ x$ for all $x$                      | why not $\land A \circ B$ #think       |
| $\circ\!\ A$                                               | the [[reduce function]] of $A$ with $\circ$        |                                        |
| $A\ \dot\circ\ B$                                          | the [[outer product]] of $A$ and $B$ with $\circ$  |                                        |
| $\delta y - \delta x$                                      | the [[derivative]] of $y$ with respect to $x$      | $\delta$ should be used instead of $d$ |
| $\int y \mid \delta x$                                     | the [[antiderivative]] of $y$ with respect to $x$  | $\delta$ should be used instead of $d$ |

### constants

| constant      | definition                                                   | notes                                       |
| ------------- | ------------------------------------------------------------ | ------------------------------------------- |
| $\varnothing$ | _undefined_                                                  | see [[improved expression evaluation]]      |
| $\top$        | [[boolean]] _true_                                           |                                             |
| $\bot$        | [[boolean]] _false_                                          |                                             |
| $\circ$       | the identity over [[function]] [[composition]]               |                                             |
| $\tau$        | the ratio of the circumference of a [[circle]] to its radius | using $\pi$ is discouraged                  |
| $e$           | [[eulers constant]]                                          |                                             |
| $\iota$       | $\lfloor \cdot 1 \rfloor$                                    | see [[imaginary]], using $i$ is discouraged |
| $\Pi$         | the [[pi function]]                                          | using $\operatorname{fact}$ is discouraged  |
| $\#$          | the number of "links" in a [[function]]                      | #todo define rigorously                     |
| $\psi$        | the [[multiset]] of prime factors of a [[natural]]           | see [[psi function in mat2348]]             |

### operator properties

_in order of high to low precedence_

#todo fix asymmetry between $=\ne > \ge < \le$ and $\land\ \lor \dashv\ \vdash\ \equiv \times$

| operator                                       | associativity | unary identity | unary description       |
| ---------------------------------------------- | ------------- | -------------- | ----------------------- |
| $()\ \braket{}\ \Big[ \Big]\ \ x\ x_a^i\ 123$  |               |                |                         |
| $[]\ \lfloor\rfloor\ \lceil\rceil$             |               | $2$ or $e$     | see above               |
| $\shortmid \text-$                             | left          | $1$            | inverse                 |
| $\delta\ \sin\ \#\ \leftarrow$                 | left-ish      |                |                         |
| $\, :\ \cdot\ \because\ \ \therefore$          | left          | $0$            | negation                |
| $\mid -$                                       | left          | $1$            | inverse                 |
| $\int\ \ \vdots\ \ \cdots\ \rightarrow\ \bmod$ | left-ish      |                |                         |
| $=\ne > \ge < \le$                             | AND           | $0$            | is (not) $0$            |
| $/$                                            | left          | $\top$         | [[boolean algebra]] NOT |
| $\land\ \lor$                                  | left          |                |                         |
| $\dashv\ \vdash$                               | left          |                |                         |
| $\equiv \times$                                | AND           | $\top$         | [[boolean algebra]] NOT |
| $,$                                            |               |                |                         |

> **note** above,
>
> - $x$ represents [[variable]]s
> - $x_a^i$ represents subscripts and superscripts
> - $123$ represents [[number]] literals
> - $\leftarrow$ represents [[function]] application
> - $\rightarrow$ represents [[function]] literals
> - $\Big[ \Big]$ represents [[matrix]] literals

> **note** unary [[operator]]s have identical precedence to their binary counterparts, but are right associative

**definition** let $\circ$ be an [[operator]] with _AND associativity_. then, $a \circ b \circ c \circ \cdots\ \ \equiv\ \ a \circ b \land b \circ c \land c \circ \cdots$

## variable scope

[[variable]] [[scope]] is currently entirely context dependent. this is know to cause occasional issues, such as with [[derivative]]s: $\delta\ f\ x - \delta x$ could represent both the [[derivative]] of $f$ with respect to $x$ in the general sense, or the [[derivative]] of $f$ with respect to $x$ **at the point** $x$

## examples

| description                                 | in this [[math notation]]                                               | in [[conventional math notation]]                                                                        |
| ------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| the [[quadratic formula]]                   | $x = \cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$                       | $\displaystyle x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$                                            |
| definition of [[complex]] numbers           | $\mathbb C x \equiv x = a : b\iota \land \mathbb R a \land \mathbb R b$ | $\displaystyle \mathbb C = \{a + bi : a, b \in \mathbb R\}$                                              |
| the [[gaussian function]]                   | $G^\sigma\ p = -\lfloor \tau \sigma2 \rfloor - e[:\! p2 - 2\sigma2]$    | $\displaystyle G(x, y, \dots) = \frac{1}{\sqrt{2 \pi\sigma^2}} e^{-\frac{x^2 + y^2 + \dots}{2\sigma^2}}$ |
| [[limit]] form of a [[derivative]]          | $f\ x \cdot f\ a - x \cdot a\ \ \vdots\ \ x \rightarrow a$              | $\displaystyle \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}$                                         |
| definition of factorials                    | $\operatorname{fact} n = 1 \mid \cdots n$                               | $\displaystyle n! = \prod_{i = 1}^n i$                                                                   |
| the resonant [[frequency]] of an LC circuit | $f = -\tau \lfloor LC \rfloor$                                          | $\displaystyle f = \frac{1}{2 \pi \sqrt{LC}}$                                                            |
| definition of the [[dot product]]           | $:\! xy$                                                                | $\displaystyle x \cdot y  = \sum_{i=1}^n x_i y_i$                                                        |
| definition of the [[outer product]]         | $x\ \dot\mid\ y$                                                        | $\displaystyle (x \otimes y)_{i, j}  = x_i \times y_j$                                                   |
| definition of the [[cartesian product]]     | $x\ \dot,\ y$                                                           | $\displaystyle x \times y = \lbrace (x, y) \mid x \in X \text{ and } y \in Y \rbrace$                    |
| definition of [[vector in rn#magnitude]]    | $\lfloor :\! v2 \rfloor$                                                | $\displaystyle \vert v \vert = \sqrt{x^2 + y^2 + \dots}$ with $v = (x, y, \dots)$                        |
| definition of [[set]] difference            | $A / B \equiv A \land \times B$                                         | $\displaystyle A \setminus B = \{x \in A : x \notin B\}$                                                 |
| the [[p-adic#absolute value]]               | $\vert n \vert^p = -p[\psi\ n\ p]$                                      | not really doable in a concise way without using plain English                                           |

definition of the [[boolean algebra#implication]] / [[set#subset]] / [[set#superset]] / [[quantifier#universal quantifier]] in this [[math notation]]: $a \vdash b \equiv /a \lor b$ and $a \dashv b \equiv a \lor /b$

in [[set theory]], if $U$ is a [[set#subset]] of $V$ and $V$ is a [[set#subset]] of $U$, then $V$ is $U$. in this [[math notation]]: $(U\ x \vdash V\ x) \land (U\ x \dashv V\ x) \equiv U = V$

the negation of a [[boolean algebra#implication]] in this [[math notation]]: $B \vdash C \times B\ /\ C$

in [[conventional math notation]]: $\lnot (B \to C) = B \land \lnot C$ or $(a \in B \to a \in C) \iff a \notin B \backslash C$ or $B \subset C \iff \forall a \in C, a \notin B$
