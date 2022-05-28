# Math Notation

see [[classical-math-notation]]

this note describes my custom [[math-notation]], meant to solve inconsistencies in [[classical-math-notation]]. it is not meant to be a fully formal mathematical system; rather, it is built to be easy and intuitive to use by mere humans.

## notation

### basic operators

$a \cdot b$ is addition

$a \circ b$ is subtraction

$\dot \circ$ and $\mathring \cdot$ are $\pm$ and $\mp$ respectively

$a \text- b$ is division

$a - b$ is low-precedence division

$ab$ is high-precedence multiplication

$a \smash\shortmid b$ is multiplication

$a \mid b$ is low-precedence multiplication

$[a] b$ is $a$ to the power of $b$

$\lfloor a \rfloor b$ is the $b$ th root of $a$ ($b = 2$ if $b$ is omitted)

$\lceil a \rceil b$ is the base-$b$ [[logarithm]] of $a$ ($b = e$ if $b$ is omitted)

$a\ b$ is shorthand for $[a] b$ only if $b$ is a [[number]] and $a$ is a variable

### [[set]]s and [[function]]s

$\mathbb N a$ checks whether $a$ is part of the [[set]] $\mathbb N$

~~$a \to b$ is lambda notation (`(a) => b`)~~

$f\ x$ is the application of the [[function]] $f$ to $x$

$S = \{a \dots b\}$ is shorthand for $S\ x \equiv x = a \lor \dots x = b$

### [[boolean-operator]]s

$a = b$ checks whether two expressions are equal

$a \ne b$ checks whether two expressions are different

$a < b$ checks whether $a$ is less than $b$

$a > b$ checks whether $a$ is greater than $b$

$a \le b$ checks whether $a$ is less than or equal to $b$

$a \gt b$ checks whether $a$ is greater than or equal to $b$

$a \land b$ is logical and (`and`)

$a \lor b$ is logical or (`or`)

$\neg a$ is logical not (`not`)

$a \times b$ is logical xor (`a ^ b`) (equivalent to $\ne$ but different precedence)

$\top$ is logical true (`true`)

$\bot$ is logical false (`false`)

$a \vdash b$ means _a implies b_ or _a is a sub[[set]] of b_ or _b is true for every a_

$a \dashv b$ is the inverse of above

$a \not \vdash b$ and $a \not \dashv b$ are negations of the above

$a \equiv b$ is logical equality check; equivalent to $=$ but with different precedence

### subscripts and superscripts

_superscripts are modifiers (subscripts with special meanings)_

$X_{subscript}$ is the variable $X$ with a subscript $_{subscript}$

$V^y$ is the $y$ (second) component of the [[vector]] $V$

$V^\omega$ where $\omega$ is a [[number]] is the $\omega$ th component of the [[vector]] $V$

$M^{i, j}$ is the $i, j$ th element of the [[matrix]] $M$

$M^{i,}$ is the $i$ th row of the [[matrix]] $M$

$M^{, j}$ is the $j$ th column of the [[matrix]] $M$

$A^\intercal$ is the transpose [[matrix]] of $A$

$A^-$ is the multiplicative inverse of the [[matrix]] $A$

$f^\times$ is the reciprocal (switching input and output) of the function $f$ (might not be necessary, [[think]])

### [[trigonometric-function]]s

### [[calculus-notation]]

$\delta y - \delta x$ is the derivative of $y$ with respect to $x$

$\int y \mid \delta x$ is the integral of $y$ with respect to $x$

> **note**: $\delta$ (greek letter _delta_) should be used instead of $d$ (latin letter _d_)

### other

$\varnothing$ is _undefined_

$x_0 \mid \dots x_n$ with $n = 3$ means $x_0 \mid x_1 \mid x_2 \mid x_3$ (this works with any operator)

$x_0 \dots x_n$ with $n = 3$ means $x_0, x_1, x_2, x_3$

## operator precedence

_high to low_

- $() [] \lfloor\rfloor \lceil\rceil$
- $\shortmid \text-$
- $\delta f$
- $\cdot \circ$
- $\mid -$
- $\int \lim$
- $=\ne\gt\ge\lt\le$
- $\lnot$
- $\land$
- $\lor$
- $\dashv\ \vdash$
- $\equiv \times$

## principles

- $=$ **checks** for equality and returns a boolean
- it is implied that an expression on its own must evaluate to $\top$ (`true`)
- [[set]]s are [[function]]s that return a [[boolean]] ($\mathbb R a$ instead of $a \in \mathbb R$)
- $\lfloor a \rfloor$ (or $\lfloor a \rfloor 2$) returns both positive and negative square roots ($\lfloor q2 \rfloor \equiv \dot \circ q$)
- $\lfloor 4 \rfloor = 2$ is valid, but $\lfloor 4 \rfloor \equiv 2$ is invalid
- ~~functions support [[currying]] to take multiple arguments~~
- all indices start at $0$

## examples

- [[quadratic-formula]]: $\circ b \cdot \lfloor b2 \circ 4ac \rfloor - 2a$
- definition of the [[set]] of [[complex]] numbers: $\mathbb C x \equiv x = a \cdot b\lfloor \circ 1 \rfloor \land \mathbb R a \land \mathbb R b$
- definition of the implication / sub[[set]] / super[[set]] / “for all” symbol:
  - $a \vdash b = \lnot a \lor b$
  - $a \dashv b = a \lor \lnot b$
- in [[set]] theory, if $U$ is a sub[[set]] of $V$ and $V$ is a sub[[set]] of $U$, then $V$ is $U$. in this math notation: $U \vdash V \land V \vdash U \equiv U = V$

## [[random-math-notation-formulas]]

## &mdash;

<https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols>

<https://www.google.com/search?q=latex+sideways+t&oq=latex+sideways+t&aqs=edge..69i57j0i512l5j0i22i30l3.4773j0j1&sourceid=chrome&ie=UTF-8>

<https://tex.stackexchange.com/questions/100941/how-do-i-get-the-single-turnstile-symbol>

<https://www.google.com/search?q=math+sideways+t&oq=math+sideways+t&aqs=edge..69i57j0i22i30l2.5762j0j1&sourceid=chrome&ie=UTF-8>

<https://tex.stackexchange.com/questions/114364/what-command-to-use-for-reversed-vdash>
