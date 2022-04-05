# Math Notation

see [[classical-math-notation]]

### notation

[[todo]]: new square root notation

$a \cdot b$ is addition

$a \circ b$ is subtraction

$\dot \circ$ and $\mathring \cdot$ are $\pm$ and $\mp$ respectively

$a \text- b$ is division

$a - b$ is low-precedence division

$ab$ is high-precedence multiplication

$a ' b$ is multiplication

$a\ |\ b$ is low-precedence multiplication

$[a] b$ is $a$ to the power of $b$

$\lfloor a \rfloor b$ is the $b$ th root of $a$

$\lceil a \rceil b$ is the base-$b$ logarithm of $a$

$a\ b$ is shorthand for $[a] b$ only if $b$ is a number and $a$ is a variable

$\N a$ checks whether $a$ is part of the set $\N$

$a = b$ checks whether two expressions are equal

$a \ne b$ chechs whether two expressions are different

~~$a : b$ is high-precedence equality check~~

$a \land b$ is logical and (`and`)

$a \lor b$ is logical or (`or`)

$\neg a$ is logical not (`not`)

$a \times b$ is logical xor (`a ^ b`) (equivalent to $\ne$ but different precedence)

$\top$ is logical true (`true`)

$\bot$ is logical false (`false`)

$a \vdash b$ means _a implies b_ or _a is a subset of b_ or _b is true for every a_

$a \dashv b$ is the inverse of above

$a \equiv b$ is logical equality check (equivalent to $=$ but different precedence)

~~$a \to b$ is lambda notation (`(a) => b`)~~

$\varnothing$ is undefined

$V^i$ is the $i$ th element of the vector $V$

$M^{i, j}$ is the $i, j$ th element of the matrix $M$

$M^{i,}$ is the $i$ th row of the matrix $M$

$M^{, j}$ is the $j$ th column of the matrix $M$

trig identities: $sin$, $asin$, $cos$, $acos$, $tan$, $atan$...

### operator precedence

_high to low_

$(()[]\lfloor\rfloor\lceil\rceil)('\text-)(\cdot \circ) (|-) (=\ne\gt\ge\lt\le) \lnot \land \lor (\dashv\ \vdash\ \equiv \times)$

### associativity

[[todo]]

### distributivity

[[todo]]

composition distributes over implication. this allows for notation such as $\N \vdash \R$

### principles

- $=$ **checks** for equality and returns a boolean
- it is implied that an expression on its own must evaluate to $\top$ (`true`)
- sets are [[function]]s that return a boolean ($\R a$ instead of $a \in \R$)
- $\lfloor a \rfloor = \lfloor a \rfloor 2$ returns both positive and negative square roots ($\lfloor q2 \rfloor = \dot \circ q$)
- $\lfloor 4 \rfloor = 2$ is invalid, but $\lfloor 4 \rfloor \dashv 2$ is valid
- ~~functions support currying to take multiple arguments~~

### examples

- [[quadratic-formula]]: $\circ b \cdot \lfloor b2 \circ 4ac \rfloor - 2a$
- definition of the set of [[complex-number]]s: $\mathbb{C} x \equiv x = a \cdot b\lfloor \circ 1 \rfloor \land \R a \land \R b$
- definition of multiplication of a boolean by a scalar:
  - $\mathbb{B} b = (b \equiv \top) \lor (b \equiv \bot)$
  - $(ab = b \dashv a \ne 0 \land \mathbb{B}b) \vdash 2\top = \top$
  - $(ab = \varnothing \dashv a = 0 \land \mathbb{B}b) \vdash 0\top = \varnothing$
- definition of the implication / subset / superset / “for all” symbol:
  - $a \vdash b = \lnot a \lor b$
  - $a \dashv b = a \lor \lnot b$
- in set theory, if $U$ is a subset of $V$ and $V$ is a subset of $U$, then $V$ is $U$. in this math notation: $U \vdash V \land V \vdash U \equiv U = V$

### random formulas

$df\text-dx = \lim_{h \to 0} f (x \cdot h) \circ f (x) - h$

$[a \cdot b] 2 = a2 \cdot b2 \cdot 2ab$

$V = b \cdot B\ |\ h - 2$

$\int_a^b(df\text- dx)\ x\ dx = f\ b \circ f\ a$

$d\text- dx\int_a^x(f\ t)\ dt = f x$

$a2 \circ b2 = a \circ b\ |\ a \cdot b$

$a2 \cdot b2 = c2$

$y = \lfloor r2 \circ x2 \rfloor$

$x2 + y2 + z2 = r2$

$[e] i\pi = \circ 1$

$\N \vdash \R$

$\R^nU_1 \land \R^nO \dashv aO = O \dashv \R a$

$^\perp = U \to v \to \R^nv \land u \cdot v = 0 \dashv U u$

$dist\ A, B = dist\ A \cdot x, B \cdot x \dashv \R x$

$dist\ A, B \cdot dist\ B, C \ge dist\ A, C$

$\lnot\ a \cdot b = c\ |\ d$

$3' x = y \dashv \Z x$

_there exists an [[integer]] $x$ such that $1 + x = 3$_

[[classical-math-notation]]: $\exist x \in \Z \text{\ \ \ s. t.\ \ \ } 1 + x = 3$

my [[math-notation]]: $1 \cdot x = 3 \land \Z x$

**while on call with Kiera**

$a2$

$2a$

$1 \div 3 (1 + 2)$

$1 - 3(1 \cdot 2)$

$1 - 3\ |\ 1 \cdot 2$

$[a] 2 \cdot b$

$[b2 \circ 4ac] 2\text-3$

$\circ b \cdot \lfloor b2 \circ 4ac \rfloor - 2a$

$1 - 0 = \varnothing$

$a \vdash b = \lnot a \lor b$

$a \dashv b = a \lor \lnot b$

$P = (x, y, z)$

$P = (P^0, P^1, P^2) \dashv \R^3 P$

**oh god I think Kiera is right**

$A \vdash B \equiv \lnot A \lor B$ ($A$ implies $B$ or $B$ for all $A$)

~~the inverse of that would be $B \vdash A$ ($B$ implies $A$ or there exists a $A$ such that $B$)~~

| A   | B   | A implies B |
| --- | --- | ----------- |
| 0   | 0   | ?           |
| 0   | 1   | ?           |
| 1   | 0   | 0           |
| 1   | 1   | ?           |

| A   | B   | B for all A |
| --- | --- | ----------- |
| 0   | 0   | ?           |
| 0   | 1   | ?           |
| 1   | 0   | 0           |
| 1   | 1   | ?           |

| A   | B   | -(A implies B) |
| --- | --- | -------------- |
| 0   | 0   | ?              |
| 0   | 1   | ?              |
| 1   | 0   | 1              |
| 1   | 1   | ?              |

| A   | B   | E A s.t. -B |
| --- | --- | ----------- |
| 0   | 0   | ?           |
| 0   | 1   | ?           |
| 1   | 0   | 1           |
| 1   | 1   | ?           |

$\lnot A \lor B \equiv A \vdash B$, which means “$B$ for all $A$”. therefore,

$\lnot (A \vdash B) \equiv A \land \lnot B$, which means “there exists an $A$ such that $\lnot B$”

the negation of $A \vdash B$ is **not** $A \dashv B$ (duh)

### srcs

<https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols>

<https://www.google.com/search?q=latex+sideways+t&oq=latex+sideways+t&aqs=edge..69i57j0i512l5j0i22i30l3.4773j0j1&sourceid=chrome&ie=UTF-8>

<https://tex.stackexchange.com/questions/100941/how-do-i-get-the-single-turnstile-symbol>

<https://www.google.com/search?q=math+sideways+t&oq=math+sideways+t&aqs=edge..69i57j0i22i30l2.5762j0j1&sourceid=chrome&ie=UTF-8>

<https://tex.stackexchange.com/questions/114364/what-command-to-use-for-reversed-vdash>
