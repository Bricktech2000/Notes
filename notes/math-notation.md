# Math Notation

see [[classical-math-notation]]

## notation

### basic operators

$a \cdot b$ is addition

$a \circ b$ is subtraction

$\dot \circ$ and $\mathring \cdot$ are $\pm$ and $\mp$ respectively

$a \text- b$ is division

$a - b$ is low-precedence division

$ab$ is high-precedence multiplication

$a ' b$ is multiplication

$a\ |\ b$ is low-precedence multiplication

$[a] b$ is $a$ to the power of $b$

$\lfloor a \rfloor b$ is the $b$ th root of $a$ ($b = 2$ if $b$ is omitted)

$\lceil a \rceil b$ is the base-$b$ logarithm of $a$ ($b = e$ if $b$ is omitted)

$a\ b$ is shorthand for $[a] b$ only if $b$ is a number and $a$ is a variable

### [[set]]s and [[function]]s

$\mathbb N a$ checks whether $a$ is part of the [[set]] $\mathbb N$

~~$a \to b$ is lambda notation (`(a) => b`)~~

$f\ x$ is the application of the [[function]] $f$ to $x$

$S = \{a \dots b\}$ is shorthand for $S\ x = (x = a) \lor \dots (x = b)$

### [[boolean-operator]]s

$a = b$ checks whether two expressions are equal

$a \ne b$ chechs whether two expressions are different

~~$a : b$ is high-precedence equality check~~

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

$V^\omega$ where $\omega$ is a number is the $\omega$ th component of the [[vector]] $V$

$M^{i, j}$ is the $i, j$ th element of the [[matrix]] $M$

$M^{i,}$ is the $i$ th row of the [[matrix]] $M$

$M^{, j}$ is the $j$ th column of the [[matrix]] $M$

$X^-$ is the multiplicative inverse of $X$, where $X$ can be a [[function]], a [[matrix]], a [[vector]], a [[set]]...

$f^\times$ is the reciprocal (switching input and output) of the function $f$

$A^\intercal$ is the transpose [[matrix]] of $A$

$f^\times$ is the reciprocal of the [[function]] $f$

$f^-$ is the inverse of the [[function]] $f$

### [[trigonometric-identity]]es

$\sin = \sin \land \cos = \cos \land \tan = \tan$

$\sin^\times = \text{asin } \land \cos^\times = \text{acos } \land \tan^\times = \text{atan }$

$\sin^- = 1 - \sin \land \cos^- = 1 - \cos \land \tan^- = 1 - \tan$

### [[calculus-notation]]

$\delta y - \delta x$ is the derivative of $y$ with respect to $x$

$\int y\ |\ \delta x$ is the integral of $y$ with respect to $x$

> **note**: $\delta$ (greek letter _delta_) should be used instead of $d$ (latin letter _d_)

### other

$\varnothing$ is _undefined_

## operator precedence

_high to low_

- $() [] \lfloor\rfloor \lceil\rceil$
- $' \text-$
- $\delta f$
- $\cdot \circ$
- $| -$
- $\int \lim$
- $=\ne\gt\ge\lt\le$
- $\lnot$
- $\land$
- $\lor$
- $\dashv\ \vdash$
- $\equiv \times$

~~composition distributes over implication. this allows for notation such as $\mathbb N \vdash \mathbb R$~~

## principles

- $=$ **checks** for equality and returns a boolean
- it is implied that an expression on its own must evaluate to $\top$ (`true`)
- [[set]]s are [[function]]s that return a boolean ($\mathbb R a$ instead of $a \in \mathbb R$)
- $\lfloor a \rfloor$ (or $\lfloor a \rfloor 2$) returns both positive and negative square roots ($\lfloor q2 \rfloor \equiv \dot \circ q$)
- $\lfloor 4 \rfloor = 2$ is valid, but $\lfloor 4 \rfloor \equiv 2$ is invalid
- ~~functions support currying to take multiple arguments~~

## examples

- [[quadratic-formula]]: $\circ b \cdot \lfloor b2 \circ 4ac \rfloor - 2a$
- definition of the [[set]] of [[complex-number]]s: $\mathbb C x \equiv x = a \cdot b\lfloor \circ 1 \rfloor \land \mathbb R a \land \mathbb R b$
- definition of multiplication of a boolean by a scalar:
  - $\mathbb B b = (b \equiv \top) \lor (b \equiv \bot)$
  - $(ab = b \dashv a \ne 0 \land \mathbb Bb) \vdash 2\top = \top$
  - $(ab = \varnothing \dashv a = 0 \land \mathbb Bb) \vdash 0\top = \varnothing$
- definition of the implication / sub[[set]] / super[[set]] / “for all” symbol:
  - $a \vdash b = \lnot a \lor b$
  - $a \dashv b = a \lor \lnot b$
- in [[set]] theory, if $U$ is a sub[[set]] of $V$ and $V$ is a sub[[set]] of $U$, then $V$ is $U$. in this math notation: $U \vdash V \land V \vdash U \equiv U = V$

## [[random-math-notation-formulas]]

## srcs

<https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols>

<https://www.google.com/search?q=latex+sideways+t&oq=latex+sideways+t&aqs=edge..69i57j0i512l5j0i22i30l3.4773j0j1&sourceid=chrome&ie=UTF-8>

<https://tex.stackexchange.com/questions/100941/how-do-i-get-the-single-turnstile-symbol>

<https://www.google.com/search?q=math+sideways+t&oq=math+sideways+t&aqs=edge..69i57j0i22i30l2.5762j0j1&sourceid=chrome&ie=UTF-8>

<https://tex.stackexchange.com/questions/114364/what-command-to-use-for-reversed-vdash>
