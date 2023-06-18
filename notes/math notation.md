# Math Notation

**see** [[conventional math notation]]

this note describes my own [[math notation]], meant to solve inconsistencies in [[conventional math notation]]. it is not meant to be a fully formal system of [[mathematics]]; rather, it is built to be easy to understand and intuitive to use by mere humans

this [[math notation]] obviously cannot be used to communicate ideas to people who do not know it, but it has made my own experience of using [[mathematics]] much more enjoyable; it has become a [[tool]] for thought. being able to use a single relatively well-defined notation in various [[mathematics]] [[fields]] that conventially use their own made up notation has been invaluable

## principles

below is a non-exhaustive list of principles that guide the design of this [[math notation]]

- **simple** &mdash; build on simple foundations and eliminate superfluous concepts
- **expressive** &mdash; be expressive to the point that notations are their own definitions
- **opinionated** &mdash; embrace opinionated and controversial design choices
- **unambiguous** &mdash; stay clear of ambiguity and of abuse of notation

below are examples of a few design decisions following from these principles

- all equality [[operator]]s check for equality and return a [[boolean]], and it is implied that an [[expression]] on its own must evaluate to **`^^`**. this allows for [[boolean algebra#operators]] to be applied on equalities formally and not as an abuse of notation
- [[set]]s, [[vector]]s, [[matrix]]es, [[sequence]]s, [[multiset]]s, [[ordered pair]]s, [[graph]]s, [[interval]]s, and other objects are defined as [[function]]s. this has some nice consequences, such as:
  - [[set]] [[operator]]s such as unions and intersections are [[boolean algebra#operators]]
  - [[interval]]s are inequalities and [[interval]] [[operator]]s are [[boolean algebra#operators]]
  - [[graph]]s are their own [[graph#adjacency matrix]]es and their own [[graph#adjacency list]]s
  - the [[matrix#transpose]] of a [[graph]] yields its converse
  - [[markov chain]]s are their own transition matrix
- some [[operator]]s are identical but have different [[infix notation#precedence]]. this reduces the number of parentheses required in expressions, making them easier to visually parse
- [[rank polymorphism]] is supported over all [[operator]]s
- all indices start at **`0`**, as they always should have
- the [[circle]] constant is **`tt`**, and **`pp`** is to be avoided; see [[tau]]
- this [[math notation]] is 1D; it takes up constant vertical space and can wrap at the end of a line

## notation

also see [[trigonometric function]]s, [[hyperbolic function]]s and [[calculus notation]]

let:

- **`M`** represent a [[matrix]]
- **`V`** represent a [[vector]]
- **`P`** represent an [[ordered pair]]
- **`M_*`** represent a [[multiset]]
- **`G`** represent a [[graph]]
- **`E`** represent any [[expression]]
- **`x`** represent a [[variable]]
- **`f`** represent a [[function]]
- **`A`** represent a [[sequence]]
- **`B`** represent a [[series]]
- **`a, b`** represent any mathematical object
- **`A, B`** represent any mathematical object with rank greater than **`1`**
- **`n, i`** represent a [[natural]]
- **`b`** represent a [[boolean]]
- **`ww`** represent any [[number]]
- **`\*`** represent any [[operator]]

### numbers

- [[natural]]s are represented using the [[decimal]] [[positional numeral system]]
- [[integer]]s are represented using the unary **`.`** [[operator]] on [[natural]]s
- [[rational]]s are represented using the **`-`** [[operator]] on [[integer]]s
- [[real]]s are represented using other [[operator]]s and [[limit]]s
- [[p-adic]]s are currently represented using their own notation

> **note** both percentages and decimals are to be represented as [[rational]]s. the `%` [[character]] and the decimal `.` are to be avoided

> **note** to make [[number]]s easier to read, spaces may be introduced in where a decimal `.` would conventially be used. for example, the value of **`49 -- 25`** can be written as **`1 96-100`**

### characters

[[character]]s are to be written surrounded by `'`. for example, the [[character]] `&` is to be written **`''&''`**

### variables

[[variable]]s can be any lower-case latin letter (**`a`**), upper-case latin letter (**`A`**), calligraphic letter (**`BB`**), lower-case greek letter (**`gg`**), upper-case greek letter (**`GG`**)

> **note** constructs such as $\hat y$ and $y'$ and $\vec y$ are to be written using subscripts; by convention, **`y_*`** is used for both $\hat y$ and $y'$, and **`y`** is used for $\vec y$

### operators and constants

| notation                                                     | description                                                  | notes                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------------------------- |
| **`a : b`**                                                  | **`b`** added to **`a`**                                     |                                                 |
| **`a . b`**                                                  | **`b`** subtracted from **`a`**                              |                                                 |
| **`a'b`** <br /> **`a \| b`**                                | **`a`** multiplied by **`b`**                                |                                                 |
| **`a-b`** <br /> **`a -- b`**                                | **`a`** divided by **`b`**                                   |                                                 |
| **`[a]b`** <br /> **`a[b]`**                                 | **`a`** to the power of **`b`**                              |                                                 |
| **`\a/ b`**                                                  | the **`b`**th root of **`a`**                                |                                                 |
| **`/a\ b`**                                                  | the base-**`b`** [[logarithm]] of **`a`**                    |                                                 |
| **`x -> E`**                                                 | [[function]] abstraction                                     | **`f = x -> E == f <- x = E`**                  |
| **`f <- E`**                                                 | [[function]] application                                     | longhand discouraged                            |
| **`a = b`** <br /> **`a == b`**                              | whether **`a`** is equal to **`b`**                          | also serves as [[boolean algebra#equivalence]]  |
| **`a + b`** <br /> **`a >< b`**                              | whether **`a`** is not equal to **`b`**                      | also serves as [[boolean algebra#exclusive or]] |
| **`a -\| b`** <br /> **`a < b`**                             | whether **`a`** is at most **`b`**                           | identical to [[boolean algebra#implication]]    |
| **`a \|- b`** <br /> **`a > b`**                             | whether **`a`** is at least **`b`**                          | identical to [[boolean algebra#implication]]    |
| **`a __ b`** <br /> **`a /\ b`**                             | the minimum of **`a`** and **`b`**                           | identical to [[boolean algebra#conjunction]]    |
| **`a ^^ b`** <br /> **`a \/ b`**                             | the maximum of **`a`** and **`b`**                           | identical to [[boolean algebra#disjunction]]    |
| **`f {x -> a}`**                                             | the [[limit]] of **`f`** as **`x`** approaches **`a`**       |                                                 |
| **`dd y -- dd x`**                                           | the [[derivative]] of **`y`** with respect to **`x`**        | **`dd`** should be used instead of **`d`**      |
| **`$ y \| dd x`**                                            | the [[antiderivative]] of **`y`** with respect to **`x`**    | **`dd`** should be used instead of **`d`**      |
| **`x_"sub"`**                                                | the [[variable]] **`x`** with a subscript **`_"sub"`**       |                                                 |
| **`A^i`** <br /> **`B^i`** <br /> **`V^n`** <br /> **`P^b`** | **`A i`** <br /> **`B i`** <br /> **`V n`** <br /> **`P b`** | to be used for indices                          |
| **`M^i,j`** <br /> **`G^a,b`**                               | **`M i j`** <br /> **`G a b`**                               | to be used for indices                          |
| **`S a`** <br /> **`M_*  a`** <br /> **`G a`**               | **`S a`** <br /> **`M_*  a`** <br /> **`G a`**               | to be used for membership                       |
| **`{\*}`**                                                   | **`\*`** as a [[prefix notation]] [[operator]]               | works with any [[operator]]                     |
| **`@`**                                                      | _undefined_                                                  | see [[improved expression evaluation]]          |
| **`@@`**                                                     | _infinity_                                                   |                                                 |
| **`__`**                                                     | [[boolean]] _false_                                          |                                                 |
| **`^^`**                                                     | [[boolean]] _true_                                           |                                                 |
| **`tt`**                                                     | [[tau]], the [[circle]] constant                             |                                                 |
| **`ee`**                                                     | [[euler's constant]]                                         |                                                 |
| **`ii`**                                                     | the [[imaginary unit]]                                       | using **`i`** is discouraged                    |
| **`rr`**                                                     | **`f a b -> f b a`**                                         | see [[combinatory logic#c combinator]]          |
| **`PP`**                                                     | the [[pi function]]                                          | using **`"fact"`** is discouraged               |
| **`#`**                                                      | the number of "links" in a [[function]]                      | #todo define rigorously                         |
| **`yy`**                                                     | the [[psi function]]                                         |                                                 |

### shorthands

| notation                    | definition                                                         | notes                                                            |
| --------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **`:A`**                    | **`A`** reduced with **`:`**                                       | see [[reduce function]]                                          |
| **`.a`**                    | **`0 . a`**                                                        | addidive inverse                                                 |
| **`\|A`** <br /> **`'A`**   | **`A`** reduced with **`\|`** <br /> **`A`** reduced with **`'`**  | see [[reduce function]]                                          |
| **`--a`** <br /> **`-a`**   | **`1 -- a`** <br /> **`1-a`**                                      | multiplicative inverse                                           |
| **`ax`**                    | **`a'x`**                                                          |                                                                  |
| **`[a]`**                   | **`ee[a]`**                                                        | [[exponent]]ial                                                  |
| **`xww`**                   | **`[x]ww`**                                                        |                                                                  |
| **`\a/`**                   | **`\a/ 2`**                                                        | square root                                                      |
| **`/a\`**                   | **`/a\ ee`**                                                       | natural [[logarithm]]                                            |
| **`->E`**                   | **`* ->  E`**                                                      | see [[combinatory logic#k combinator]]                           |
| **`x y -> E`**              | **`x -> y -> E`**                                                  |                                                                  |
| **`f E`**                   | **`f <- E`**                                                       | shorthand preferred                                              |
| **`+a`** <br /> **`><a`**   | **`^^ + a`** <br /> **`^^ >< a`**                                  | [[boolean algebra#negation]]                                     |
| **`-\|A`** <br /> **`<A`**  | **`A`** sorted from least to greatest                              |                                                                  |
| **`\|-A`** <br />**`>A`**   | **`A`** sorted from greatest to least                              |                                                                  |
| **`__A`** <br /> **`/\A`**  | **`A`** reduced with **`__`** <br /> **`A`** reduced with **`/\`** | see [[reduce function]]                                          |
| **`^^A`** <br /> **`\/A`**  | **`A`** reduced with **`^^`** <br /> **`A`** reduced with **`\/`** | see [[reduce function]]                                          |
| **`a_0 \* a_1 \* ... a_n`** | with **`n = 3`**, **`a_0 \* a_1 \* a_2 \* a_3`**                   | step size is **`1`** or **`.1`** if **`a_1 \*`** is omitted      |
| **`a_0 ... a_n`**           | with **`n = 3`**, **`a_0, a_1, a_2, a_3`**                         | step size is **`1`** or **`.1`** if **`a_1`** is omitted         |
| **`f {a\*b}`**              | **`f a \* f b`**                                                   | see [[combinatory logic#psi combinator]]                         |
| **`a {--\*:} b`**           | **`(a -- b) \* (a : b)`**                                          | see [[combinatory logic#phi 1 combinator]]                       |
| **`f {a b}`**               | **`f {a <- b}`**                                                   |                                                                  |
| **`{f\*g} a`**              | **`(f a) \* (g a)`**                                               | see [[combinatory logic#phi combinator]]                         |
| **`{f g} a`**               | **`{f <- g} a`**                                                   | see [[combinatory logic#s combinator]]                           |
| **`E @@`**                  | **`E x {x -> @@}`**                                                |                                                                  |
| **`A \* B`**                | **`x -> A x \* B x`**                                              | see [[rank polymorphism]]                                        |
| **`A \* a`**                | **`x -> A x \* a`**                                                | see [[rank polymorphism]]                                        |
| **`f g *`**                 | **`x -> f (g x)`**                                                 | **`*`** is a "hole"                                              |
| **`{*}`**                   | **`x -> x`**                                                       | see [[combinatory logic#i combinator]], [[composition#identity]] |
| **`""math""`**              | **`(''m'', ''a'', ''t'', ''h'')`**                                 | see [[string]], [[list]]                                         |

### precedence and associativity

**see** [[infix notation#precedence]], [[infix notation#associativity]]

| operator                                | precedence | associativity |
| --------------------------------------- | ---------- | ------------- |
| **`( ) (( )) { } {{ }} [] [] 123 x_a`** | highest    |               |
| **`\./ [.] /.\ x^i`**                   | ...        | left          |
| **`' -`**                               | ...        | left          |
| **`dd "sin" # \* <-`**                  | ...        | left          |
| **`: .`**                               | ...        | left          |
| **`\| --`**                             | ...        | left          |
| **`$ { } ... -> "mod"`**                | ...        | right         |
| **`__ ^^`**                             | ...        | left          |
| **`= -\| \|- +`**                       | ...        | AND           |
| **`/\ \/`**                             | ...        | left          |
| **`== < > ><`**                         | ...        | AND           |
| **`,`**                                 | lowest     |               |

> **note** above,
>
> - **`123`** represents [[natural]] literals
> - **`x_a`** represents [[variable]]s and subscripts
> - **`x^i`** represents superscripts
> - **`<-`** represents [[function]] application
> - **`->`** represents [[function]] abstraction
> - **`"sin"`** represents any text [[operator]] in [[prefix notation]]
> - **`"mod"`** represents any text [[operator]] in [[infix notation]]

> **note** unary [[operator]]s have identical [[infix notation#precedence]] to their binary counterparts but are right associative

**definition** let **`\*`** be an [[operator]] with _AND associativity_. then, **`a \* b \* c \* ... == a \* b /\ b \* c /\ c \* ...`**

### comparison with conventional notation

| description                                 | in this [[math notation]]                  | in [[conventional math notation]]                                                                        |
| ------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| the [[quadratic formula]]                   | **`x = .b : \b2.4ac/ -- 2a`**              | $\displaystyle x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$                                            |
| definition of [[complex]] numbers           | **`CC x == x = a : bii /\ RR a /\ RR b`**  | $\displaystyle \mathbb C = \{a + bi : a, b \in \mathbb R\}$                                              |
| the [[gaussian function]]                   | **`G^ss p = -- ss \tt/ -- [:p2 -- 2ss2]`** | $\displaystyle G(x, y, \dots) = \frac{1}{\sqrt{2 \pi\sigma^2}} e^{-\frac{x^2 + y^2 + \dots}{2\sigma^2}}$ |
| [[limit]] form of a [[derivative]]          | **`f x . f a -- x . a {x -> a}`**          | $\displaystyle \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}$                                         |
| definition of factorials                    | **`"fact" n = 1 \| ... n`**                | $\displaystyle n! = \prod_{i = 1}^n i$                                                                   |
| the resonant [[frequency]] of an LC circuit | **`f = -- tt \"LC"/`**                     | $\displaystyle f = \frac{1}{2 \pi \sqrt{LC}}$                                                            |
| definition of the [[dot product]]           | **`:xy`**                                  | $\displaystyle x \cdot y  = \sum_{i=1}^n x_i y_i$                                                        |
| definition of the [[outer product]]         | **`x * \| y *`**                           | $\displaystyle (x \otimes y)_{i, j}  = x_i \times y_j$                                                   |
| definition of the [[cartesian product]]     | **`__ (X, Y) *`**                          | $\displaystyle X \times Y = \lbrace (x, y) \mid x \in X \text{ and } y \in Y \rbrace$                    |
| definition of [[vector in rn#magnitude]]    | **`\|\|v\|\| = \:v2/`**                    | $\displaystyle \vert v \vert = \sqrt{x^2 + y^2 + \dots}$ with $v = (x, y, \dots)$                        |
| definition of [[set]] difference            | **`A /\ +B`**                              | $\displaystyle A \setminus B = \{x : x \in A \text{ and } x \notin B\}$                                  |
| the [[p-adic#absolute value]]               | **`\|\|n\|\|^p = --p[yy n p]`**            | not really doable in a concise way without using plain English                                           |
| the **`n`**th column of a [[matrix]]        | **`rr M n`**                               | no standard notation; $(M^\intercal)_n$ or $\operatorname{col}_n(M)$ or $M_{\cdot j}$                    |
