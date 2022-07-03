# Math Notation

see [[classical-math-notation]]

this note describes my custom [[math-notation]], meant to solve inconsistencies in [[classical-math-notation]]. it is not meant to be a fully formal mathematical system; rather, it is built to be easy and intuitive to use by mere humans.

## principles

- all equality operators **check** for equality and returns a [[boolean]], and it is implied that an expression on its own must evaluate to $\top$. this allows for [[boolean-operator]]s to be applied on equalities explicitly as opposed informally
- [[set]]s are [[function]]s that return a [[boolean]] ($\mathbb R a$ instead of $a \in \mathbb R$). this way [[boolean-operator]]s and [[set]] operators are one and the same
- some operators have versions with a different precedence as "more brackets means more explicit, but less brackets means less complex and less confusing"
- $\lfloor a \rfloor$ returns both positive and negative square roots ($\lfloor q2 \rfloor \equiv\ \because q$). same applies for other reciprocals
- superscripts are modifiers (subscripts with special meanings). this distinction is especially useful when working with [[forward-propagation]] and [[backpropagation]] in neural networks
- [[derivative]]s are not to be written as $y'$, but rather as their complete form $\delta y - \delta x$. this makes [[calculus]] notation way more intuitive
- all indices start at $0$, as they should always have

## notation

also see [[trigonometric-function]], [[calculus-notation]]

### main operators

| notation                                                          | description                                      | notes                                     |
| ----------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------- |
| $a : b$                                                           | addition                                         |                                           |
| $a \cdot b$                                                       | subtraction                                      |                                           |
| $\because$ and $\therefore$                                       | $\pm$ and $\mp$                                  |                                           |
| $a \smash\shortmid b$ and $a \mid b$                              | multiplication                                   |                                           |
| $a \text- b$ and $a - b$                                          | division                                         |                                           |
| $[a]b$                                                            | exponentiation                                   | represents a power by convention          |
| $a[b]$                                                            | exponentiation                                   | represents an exponential by convention   |
| $\lfloor a \rfloor b$                                             | $b$ th root of $a$                               | $b = 2$ if $b$ is omitted                 |
| $\lceil a \rceil b$                                               | base-$b$ [[logarithm]] of $a$                    | $b = e$ if $b$ is omitted                 |
| $\lambda x\ \ E$ where $E$ is an expression                       | [[function]] definition                          | $f = \lambda x\ E \equiv f\ x = E$        |
| $f\ x$                                                            | [[function]] application                         |                                           |
| $a = b$                                                           | equality                                         | numerical equality by convention          |
| $a < b$ and $a > b$                                               | less than and greater than                       |                                           |
| $a \le b$ and $a \ge b$                                           | less than or greater than, or equal              |                                           |
| $a \land b$                                                       | logical and                                      | `a && b`                                  |
| $a \lor b$                                                        | logical or                                       | `a \|\| b`                                |
| $a\ /\ b$                                                         | logical difference                               | $a \land b = \bot$                        |
| $/a$                                                              | logical not                                      | `!a`                                      |
| $a \equiv b$                                                      | equality                                         | logical equality by convention            |
| $a \times b$                                                      | nonequality                                      | logical xor by convention                 |
| $a \vdash b$                                                      | implication, subset                              | $a$ implies $b$, $b$ for all $a$          |
| $a \dashv b$                                                      | reverse implication, superset                    | $a$ for all $b$, $b$ implies $a$          |
| $x_0 \mid x_1 \mid \dots x_n$ where $\mid$ is any operator        | with $n = 3$, $x_0 \mid x_1 \mid x_2 \mid x_3$   | step size is $1$ if $x_1 \mid$ is omitted |
| $x_0 \dots x_n$                                                   | with $n = 3$ $x_0, x_1, x_2, x_3$                | step size is $1$ if $x_1$ is omitted      |
| $X_{subscript}$                                                   | the variable $X$ with a subscript $_{subscript}$ |                                           |
| $V^y$ where $V$ is a [[vector]]                                   | the $y$ (second) component of $V$                |                                           |
| $V^\omega$ where $\omega$ is a [[number]] and $V$ is a [[vector]] | the $\omega$ th component of $V$                 |                                           |
| $a^i$ where $a$ is a [[sequence]]                                 | the $i$ th element of $a$                        |                                           |
| $b^i$ where $b$ is a [[series]]                                   | the $i$ th element of $b$                        |                                           |
| $M^{i, j}$ where $M$ is a [[matrix]]                              | the $i, j$ th element of $M$                     |                                           |
| $M^{i,}$ where $M$ is a [[matrix]]                                | the $i$ th row of $M$                            |                                           |
| $M^{, j}$ where $M$ is a [[matrix]]                               | the $j$ th column of $M$                         |                                           |
| $M^\intercal$ where $M$ is a [[matrix]]                           | the transpose of $A$                             |                                           |
| $M^-$ where $M$ is a [[matrix]]                                   | the multiplicative inverse of the $A$            |                                           |

### shorthands and constants

| constant      | definition                                                   | notes                                  |
| ------------- | ------------------------------------------------------------ | -------------------------------------- |
| $\varnothing$ | _undefined_                                                  | see [[improved-expression-evaluation]] |
| $\top$        | logical true                                                 | `true`                                 |
| $\bot$        | logical false                                                | `false`, $/\top$                       |
| $\tau$        | the ratio of the circumference of a [[circle]] to its radius | using $\pi$ is discouraged             |

| shorthand                                                      | definition                                            | notes                                  |
| -------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------- |
| $a \not\vdash b$, $a \ne b$, $a \not\le b$, $a \not< b$...     | $/(a \vdash b)$, $/a = b$, $/a \le b$, $/a < b$...    |                                        |
| $x\omega$ where $x$ is a variable and $\omega$ is a [[number]] | $[x]\omega$                                           |                                        |
| $ax$ where $x$ is a variable                                   | $a \smash\shortmid x$                                 |                                        |
| $S = \lbrace a \dots b \rbrace$                                | $S\ x \equiv x = a \lor \dots x = b$                  |                                        |
| $\mathbb N a$                                                  | checks whether $a$ is part of the [[set]] $\mathbb N$ |                                        |
| $\delta y - \delta x$                                          | the derivative of $y$ with respect to $x$             | $\delta$ should be used instead of $d$ |
| $\int y - \delta x$                                            | the integral of $y$ with respect to $x$               | $\delta$ should be used instead of $d$ |

### precedence, associativity, unary identity

| operator                         | precedence | associativity | unary identity |
| -------------------------------- | ---------- | ------------- | -------------- |
| $()\ x\ x_a^i$                   | highest    |               |                |
| $[] \lfloor\rfloor \lceil\rceil$ | .          |               |                |
| $\shortmid \text-$               | .          | left          | $1$            |
| $\delta\ \sin\ f$                | .          | right-ish     |                |
| $\ : \cdot$                      | .          | left          | $0$            |
| $\mid -$                         | .          | left          | $1$            |
| $,$                              | .          |               |                |
| $\int \lim\ \dots\ \lambda$      | .          | right         |                |
| $=\ne\gt\ge\lt\le$               | .          | AND           |                |
| $/$                              | .          | left          | $\top$         |
| $\land \lor$                     | .          | left          |                |
| $\dashv\ \vdash$                 | .          | left          |                |
| $\equiv \times$                  | lowest     | AND           |                |

> **note**: above,
>
> - $x$ represents variables
> - $f$ represents [[function]] application
> - $x_a^i$ represents subscripts and superscripts
> - $\lambda$ represents [[function]] definitions

> **note**: unary operators have identical precedence to their binary counterparts, but are right associative

> **definition**: let $=$ be an operator with _AND_ associativity. then, $a = b = c = \dots\ \ \equiv\ \ a = b \land b = c \land c = \dots$

## examples

[[quadratic-formula]]: $\cdot b : \lfloor b2 \cdot 4ac \rfloor - 2a$

definition of the [[set]] of [[complex]] numbers: $\mathbb C x \equiv x = a : b \lfloor \cdot 1 \rfloor \land \mathbb R a \land \mathbb R b$

definition of the implication / sub[[set]] / super[[set]] / “for all” symbol: $a \vdash b = /a \lor b$ and $a \dashv b = a \lor /b$

in [[set]] theory, if $U$ is a sub[[set]] of $V$ and $V$ is a sub[[set]] of $U$, then $V$ is $U$. in this math notation: $U \vdash V \land V \vdash U \equiv U = V$

the probability density of the normal distribution in [[classical-math-notation]]: $\frac{1}{\sqrt{2 \sigma^2 \pi}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}$

compared to in my [[math-notation]]: $-\lfloor \tau \sigma2 \rfloor - e[[x \cdot \mu]2 - 2\sigma2]$

## #think

~~$a \to b$ is lambda notation (`(a) => b`)~~

- ~~functions support [[currying]] to take multiple arguments~~

## [[random-math-notation-formulas]]
