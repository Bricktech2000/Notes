# Math Notation

**see** [[conventional math notation]]

this note describes my own [[math notation]], meant to solve inconsistencies in [[conventional math notation]]. it is not meant to be a fully formal system of [[mathematics]]; rather, it is built to be easy to understand and intuitive to use by mere humans.

this [[math notation]] obviously cannot be used to communicate ideas to people who do not know it, but it has made my own experience of using [[mathematics]] much more enjoyable; it has become a tool for thought. being able to use a single relatively well-defined notation in various [[mathematics]] [[fields]] that conventially use their own made up notation has been invaluable

## principles

- all equality [[operator]]s check for equality and return a [[boolean]], and it is implied that an [[expression]] on its own must evaluate to **`^^`**. this allows for [[boolean algebra#operators]] to be applied on equalities explicitly as opposed informally
- [[set]]s are [[function]]s that return a [[boolean]] ([[set]]s are [[predicate]]s). this way, [[boolean algebra#operators]] and [[set]] [[operator]]s are one and the same. other [[data structure]]s that work similarly include [[vector]]s, [[matrix]]es, [[sequence]]s, [[multiset]]s, [[ordered pair]]s...
- some [[operator]]s are identical but have different [[infix notation#precedence]] as "more brackets means more explicit, but less brackets means less complex and less confusing"
- [[operator]]s return what they should actually return to match their inverse. for example, **`\ a /`** returns both positive and negative square roots
- superscripts are modifiers (subscripts with special meanings). this distinction is extremely useful when working with [[forward propagation]] and [[backpropagation]] in [[neural network]]s, for example
- [[derivative]]s are not to be written as **`y_*`**, but rather as their complete form **`\d y -- \d x`**. this makes [[calculus notation]] way more intuitive
- all indices start at **`0`**, as they always should have
- [[rank polymorphism]] is supported over all [[operator]]s

## Notation

also see [[trigonometric function]]s, [[hyperbolic function]]s and [[calculus notation]]

let:

- **`M`** be a [[matrix]]
- **`V`** be a [[vector]]
- **`P`** be an [[ordered pair]]
- **`M_*`** be a [[multiset]]
- **`G`** be a [[graph]]
- **`E`** be an [[expression]]
- **`x`** be a [[variable]]
- **`f`** be a [[function]]
- **`A`** be a [[sequence]]
- **`B`** be a [[series]]
- **`a, b`** be any mathematical objects
- **`A, B`** be any mathematical objects with rank greater than **`1`**
- **`n, i`** be [[natural]] numbers
- **`b`** be a [[boolean]]
- **`\w`** be any [[number]]
- **`\*`** be any [[operator]]

### numbers

- [[natural]]s are represented using the [[decimal]] [[positional numeral system]]
- [[integer]]s are represented using the unary **`.`** [[operator]] on [[natural]]s
- [[rational]]s are represented using the **`-`** [[operator]] on [[integer]]s
- [[real]]s are represented using other [[operator]]s and [[limit]]s
- [[p-adic]]s are currently represented using their own notation

> **note** both percentages and decimals are to be represented as [[rational]]s. the `%` [[character]] and the decimal `.` are to be avoided

> **note** to make [[number]]s easier to read, spaces may be introduced in where a decimal `.` would conventially be used. for example, the value of **`49 -- 25`** can be written as **`1 96-100`**

### characters

[[character]]s are to be written surrounded by `'`. for example, the [[character]] `&` is to be written **`''\&''`**

### variables

[[variable]]s can be any latin letter (**`a`**), greek letter (**`\a`**), calligraphic letter (**`aa`**), or double-struck letter (**`AA`**). constructs such as $\hat y$ and $y'$ and $\vec y$ are to be written using subscripts; by convention, **`y_*`** is used for both $\hat y$ and $y'$, and **`y`** is used for $\vec y$

### operators and constants

| notation                                                     | description                                                  | notes                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **`a : b`**                                                  | **`b`** added to **`a`**                                     |                                                              |
| **`a . b`**                                                  | **`b`** subtracted from **`a`**                              |                                                              |
| **`a'b`** <br /> **`a \| b`**                                | **`a`** multiplied by **`b`**                                |                                                              |
| **`a-b`** <br /> **`a -- b`**                                | **`a`** divided by **`b`**                                   |                                                              |
| **`[a]b`** <br /> **`a[b]`**                                 | **`a`** to the power of **`b`**                              |                                                              |
| **`\ a / b`**                                                | the **`b`**th root of **`a`**                                |                                                              |
| **`/a\ b`**                                                  | the base-**`b`** [[logarithm]] of **`a`**                    |                                                              |
| **`x -> E`**                                                 | [[function]] literal                                         | **`f = x -> E == f <- x = E`**                               |
| **`f <- E`**                                                 | [[function]] application                                     | uncommon, shorthand preferred                                |
| **`a = b`** <br /> **`a == b`**                              | **`a`** is equal to **`b`**                                  | also serves as [[boolean algebra#equivalence]]               |
| **`a + b`** <br /> **`a >< b`**                              | **`a`** is not equal to **`b`**                              | also serves as [[boolean algebra#exclusive or]]              |
| **`a -\| b`** <br /> **`a < b`**                             | **`a`** is at most **`b`**                                   | identical to [[boolean algebra#implication]]                 |
| **`a \|- b`** <br /> **`a > b`**                             | **`a`** is at least **`b`**                                  | identical to [[boolean algebra#implication]]                 |
| **`a __ b`** <br /> **`a /\ b`**                             | the minimum of **`a`** and **`b`**                           | identical to [[boolean algebra#conjunction]]                 |
| **`a ^^ b`** <br /> **`a \/ b`**                             | the maximum of **`a`** and **`b`**                           | identical to [[boolean algebra#disjunction]]                 |
| **`f {x -> a}`**                                             | the [[limit]] of **`f`** as **`x`** approaches **`a`**       |                                                              |
| **`\d y -- \d x`**                                           | the [[derivative]] of **`y`** with respect to **`x`**        | **`\d`** should be used instead of **`d`**                   |
| **`$ y \| \d x`**                                            | the [[antiderivative]] of **`y`** with respect to **`x`**    | **`\d`** should be used instead of **`d`**                   |
| **`x_"sub"`**                                                | the [[variable]] **`x`** with a subscript **`_"sub"`**       |                                                              |
| **`A^i`** <br /> **`B^i`** <br /> **`V^n`** <br /> **`P^b`** | **`A i`** <br /> **`B i`** <br /> **`V n`** <br /> **`P b`** | to be used for indices                                       |
| **`M^i,j`** <br /> **`G^a,b`**                               | **`M i j`** <br /> **`G a b`**                               | to be used for indices                                       |
| **`S a`** <br /> **`M_*  a`** <br /> **`G a`**               | **`S a`** <br /> **`M_*  a`** <br /> **`G a`**               | to be used for membership                                    |
| **`{\*}`**                                                   | **`\*`** as a [[prefix notation]] [[operator]]               | works with any [[operator]]                                  |
| **`@`**                                                      | _undefined_                                                  | see [[improved expression evaluation]]                       |
| **`@@`**                                                     | _infinity_                                                   |                                                              |
| **`__`**                                                     | [[boolean]] _false_                                          |                                                              |
| **`^^`**                                                     | [[boolean]] _true_                                           |                                                              |
| **`\t`**                                                     | the [[circle]] constant                                      | see [[tau]]                                                  |
| **`\e`**                                                     | [[euler's constant]]                                         |                                                              |
| **`\i`**                                                     | **`\.1/`**                                                   | see [[imaginary]]. using **`i`** is discouraged              |
| **`\r`**                                                     | **`f a b -> f b a`**                                         | see [[matrix#transpose]], [[combinatory logic#c combinator]] |
| **`\P`**                                                     | the [[pi function]]                                          | using **`"fact"`** is discouraged                            |
| **`#`**                                                      | the number of "links" in a [[function]]                      | #todo define rigorously                                      |
| **`\y`**                                                     | the [[multiset]] of [[prime]] factors of a [[natural]]       | see [[psi function]]                                         |

### shorthands

| notation                    | definition                                                         | notes                                                       |
| --------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| **`:A`**                    | **`A`** reduced with **`:`**                                       | see [[reduce function]]                                     |
| **`.a`**                    | **`0 . a`**                                                        | addidive inverse                                            |
| **`\|A`** <br /> **`'A`**   | **`A`** reduced with **`\|`** <br /> **`A`** reduced with **`'`**  | see [[reduce function]]                                     |
| **`--a`** <br /> **`-a`**   | **`1 -- a`** <br /> **`1-a`**                                      | multiplicative inverse                                      |
| **`ax`**                    | **`a'x`**                                                          |                                                             |
| **`[a]\w`**                 | **`\e[a]`**                                                        | [[exponent]]ial                                             |
| **`x\w`**                   | **`[x]\w`**                                                        |                                                             |
| **`\ a /`**                 | **`\ a / 2`**                                                      | square root                                                 |
| **`/a\`**                   | **`/a\ \e`**                                                       | natural [[logarithm]]                                       |
| **`->E`**                   | **`* ->  E`**                                                      | [[combinatory logic#k combinator]]                          |
| **`x y -> E`**              | **`x -> y -> E`**                                                  |                                                             |
| **`f E`**                   | **`f <- E`**                                                       | common, longhand discouraged                                |
| **`+a`** <br /> **`><a`**   | **`^^ + a`** <br /> **`^^ >< a`**                                  | [[boolean algebra#negation]]                                |
| **`-\|A`** <br /> **`<A`**  | **`A`** sorted from least to greatest                              |                                                             |
| **`\|-A`** <br />**`>A`**   | **`A`** sorted from greatest to least                              |                                                             |
| **`__A`** <br /> **`/\A`**  | **`A`** reduced with **`__`** <br /> **`A`** reduced with **`/\`** | see [[reduce function]]                                     |
| **`^^A`** <br /> **`\/A`**  | **`A`** reduced with **`^^`** <br /> **`A`** reduced with **`\/`** | see [[reduce function]]                                     |
| **`a_0 \* a_1 \* ... a_n`** | with **`n = 3`**, **`a_0 \* a_1 \* a_2 \* a_3`**                   | step size is **`1`** or **`.1`** if **`a_1 \*`** is omitted |
| **`a_0 ... a_n`**           | with **`n = 3`**, **`a_0, a_1, a_2, a_3`**                         | step size is **`1`** or **`.1`** if **`a_1`** is omitted    |
| **`f {a\*b}`**              | **`f a \* f b`**                                                   | [[combinatory logic#psi combinator]]                        |
| **`a {--\*:} b`**           | **`(a -- b) \* (a : b)`**                                          | [[combinatory logic#phi 1 combinator]]                      |
| **`f {a b}`**               | **`f {a <- b}`**                                                   |                                                             |
| **`{f\*g} a`**              | **`(f a) \* (g a)`**                                               | [[combinatory logic#phi combinator]]                        |
| **`{f g} a`**               | **`{f <- g} a`**                                                   |                                                             |
| **`E @@`**                  | **`E x {x -> @@}`**                                                |                                                             |
| **`A \* B`**                | **`x -> A x \* B x`**                                              | see [[rank polymorphism]]                                   |
| **`A \* a`**                | **`x -> A x \* a`**                                                | see [[rank polymorphism]]                                   |
| **`f g *`**                 | **`x -> f (g x)`**                                                 | **`*`** is a "hole"                                         |
| **`{*}`**                   | **`x -> x`**                                                       | see [[function]] [[composition#identity]]                   |
| **`""math""`**              | **`(''m'', ''a'', ''t'', ''h'')`**                                 | see [[string]], [[list]]                                    |

### precedence and associativity

_in order of high to low precedence_

**see** [[infix notation#precedence]], [[infix notation#associativity]]

| operator                                | associativity |
| --------------------------------------- | ------------- |
| **`( ) (( )) { } {{ }} [] [] 123 x_a`** |               |
| **`x^i`**                               |               |
| **`\./ [.] /.\`**                       | left          |
| **`' -`**                               | left          |
| **`\d "sin" # \* <-`**                  | left          |
| **`: .`**                               | left          |
| **`\| --`**                             | left          |
| **`$ { } ... -> "mod"`**                | right         |
| **`__ ^^`**                             | left          |
| **`= -\| \|- +`**                       | AND           |
| **`/\ \/`**                             | left          |
| **`== < > ><`**                         | AND           |
| **`,`**                                 |               |

> **note** above,
>
> - **`123`** represents [[natural]] literals
> - **`x_a`** represents [[variable]]s and subscripts
> - **`x^i`** represents superscripts
> - **`<-`** represents [[function]] application
> - **`->`** represents [[function]] abstraction
> - **`"sin"`** represents any text [[operator]] in [[prefix notation]]
> - **`"mod"`** represents any text [[operator]] in [[infix notation]]

> **note** unary [[operator]]s have identical [[infix notation#precedence]] to their binary counterparts, but are right associative

**definition** let **`\*`** be an [[operator]] with _AND associativity_. then, **`a \* b \* c \* ... == a \* b /\ b \* c /\ c \* ...`**

## examples

### comparison with conventional notation

| description                                 | in this [[math notation]]                  | in [[conventional math notation]]                                                                        |
| ------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| the [[quadratic formula]]                   | **`x = .b : \ b2.4ac / -- 2a`**            | $\displaystyle x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$                                            |
| definition of [[complex]] numbers           | **`CC x == x = a : b\i /\ RR a /\ RR b`**  | $\displaystyle \mathbb C = \{a + bi : a, b \in \mathbb R\}$                                              |
| the [[gaussian function]]                   | **`G^\s p = -- \s \\t/ -- [:p2 -- 2\s2]`** | $\displaystyle G(x, y, \dots) = \frac{1}{\sqrt{2 \pi\sigma^2}} e^{-\frac{x^2 + y^2 + \dots}{2\sigma^2}}$ |
| [[limit]] form of a [[derivative]]          | **`f x . f a -- x . a {x -> a}`**          | $\displaystyle \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h}$                                         |
| definition of factorials                    | **`"fact" n = 1 \| ... n`**                | $\displaystyle n! = \prod_{i = 1}^n i$                                                                   |
| the resonant [[frequency]] of an LC circuit | **`f = -- \t \"LC"/`**                     | $\displaystyle f = \frac{1}{2 \pi \sqrt{LC}}$                                                            |
| definition of the [[dot product]]           | **`:xy`**                                  | $\displaystyle x \cdot y  = \sum_{i=1}^n x_i y_i$                                                        |
| definition of the [[outer product]]         | **`x * \| y *`**                           | $\displaystyle (x \otimes y)_{i, j}  = x_i \times y_j$                                                   |
| definition of the [[cartesian product]]     | **`__ (X, Y) *`**                          | $\displaystyle X \times Y = \lbrace (x, y) \mid x \in X \text{ and } y \in Y \rbrace$                    |
| definition of [[vector in rn#magnitude]]    | **`\|\|v\|\| = \:v2/`**                    | $\displaystyle \vert v \vert = \sqrt{x^2 + y^2 + \dots}$ with $v = (x, y, \dots)$                        |
| definition of [[set]] difference            | **`A /\ +B`**                              | $\displaystyle A \setminus B = \{x \in A : x \notin B\}$                                                 |
| the [[p-adic#absolute value]]               | **`\|\|n\|\|^p = --p[\y n p]`**            | not really doable in a concise way without using plain English                                           |

definition of the [[boolean algebra#implication]] / [[set#subset]] / [[set#superset]] / [[quantifier#universal quantifier]] in this [[math notation]]: **`a -| b == +a \/ b`** and **`a |- b == a \/ +b`**

in [[set theory]], if **`U`** is a [[set#subset]] of **`V`** and **`V`** is a [[set#subset]] of **`U`**, then **`V`** is **`U`**. in this [[math notation]]: **`U |- V /\ U -| V == U = V`**

the negation of a [[boolean algebra#implication]] in this [[math notation]]: **`B -| C >< B /\ +C`**

in [[conventional math notation]]: $\lnot (B \to C) = B \land \lnot C$ or $(a \in B \to a \in C) \iff a \notin B \backslash C$ or $B \subset C \iff \forall a \in C, a \notin B$

definition of the **`n`**th column of a [[matrix]]: **`\r M n`** or **`M * n`**

the closed interval from **`a`** to **`b`**: **`a -| * -| b`**
