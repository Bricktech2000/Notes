# Function

**see** [[math notation]]

**definition**

a [[function]] **`HH`** between [[set]]s **`A`** and **`B`** is a [[relation]] between **`A`** and **`B`** such that:

1. **`HH {a, b} /\ B b > A a`** or alternatively **`B h a > A a`** &mdash; there exists some output for every input
2. **`HH {a, b_1} /\ HH {a, b_2} < b_1 = b_2`** or alternatively **`a_1 = a_2 < h a_1 = h a_2`** &mdash; there exists exactly one output for any input

one can use the _horizontal [[line]] test_ to determine whether the graph of a [[curve]] is the graph of a [[function]]

**types**

[[boolean]] [[function]]

[[trigonometric function]]

[[hyperbolic function]]

[[sigmoid function]]

[[predicate]]

**applications**

[[functional programming]]

[[function#vector space]]

[[loss function]] in [[neural network]]s

[[verifiable random function]] in [[cryptocurrency]]es

## Vector Space

**see** [[vector]], [[vector space]]

**definition** **`HH f`** if and only if the [[function]] **`f`** is defined on its whole [[function#domain]]

#think if and only if it is a [[set theory]]etical [[function]]?

**properties**

_zero [[function]]_ **`O x = 0`**

_[[function]] addition_ **`(f : g) x = f x : g x`**

_multiplication by a [[scalar]]_ **`(cf) x = c | f x`**

## Domain

## Codomain

## Range

## Root

**definition** the _domain_ of a [[function]] is the set of arguments for which it will produce an output

**definition** the _codomain_ of a [[function]] is the set of all **possible** outputs

**definition** the _range_ of a [[function]] is the set of all outputs it can produce

**definition** the _roots_ of a [[function]] **`f`** are the values of **`x`** such that **`f x = 0`**

this asymmetry between the "input" and the "output" of a [[function]] is what distinguishes it from a [[relation]] &mdash; <https://youtu.be/O2lZkr-aAqk?t=724>

**properties**

_codomain_ **`D x < C f x`**

_range_ **`D x == R f x`**

**`D x > A f x`**

## Function Parity

### Even Function

_an even function is symmetrical about the y axis_

**definition** **`f x = f (.x) > RR x`**

### Odd Function

_an odd function is symmetrical about the y axis, but also flipped about the x axis_

**definition** **`.f x = f (.x) > RR x`**

## Periodic Function

**definition** **`f x = f (x : p) /\ RR p > RR x`**

**definition** above, **`p`** is said to be the _period_ of **`f`**

## Multivalued Function

**definition** a [[function]] is _multivalued_ if it maps a single input to multiple outputs

#todo link with [[improved expression evaluation]] suporpositions

## Increasing Function

## Decreasing Function

**see** [[calculus notation]]

**definition** a [[function]] **`f`** is _increasing_ on an [[interval]] **`a -| * -| b`** if **`x_1 -| x_2 < f x_1 -| f x_2`**, or **`dd f x -- dd x |- 0`** on that [[interval]]

**definition** a [[function]] **`f`** is _decreasing_ on an [[interval]] **`a -| * -| b`** if **`x_1 |- x_2 < f x_1 |- f x_2`**, or **`dd f x -- dd x -| 0`** on that [[interval]]

## Concavity

**see** [[calculus notation]]

**definition** a [[function]] **`f x`** is _concave up_ at **`x`** if **`dd (dd f x -- dd x) -- dd x |- 0`**, it _bends upwards_

**definition** a [[function]] **`f x`** is _concave down_ at **`x`** if **`dd (dd f x -- dd x) -- dd x -| 0`**, it _bends downwards_

a point where [[function#concavity]] changes (from up to down or down to up) is a [[function#inflection point]]

## Extremum

**see** [[function#inflection point]], [[derivative]]

> extrema are the largest and smallest value of the function, either within a given range (the local or relative extrema), or on the entire [[function#domain]] (the global or absolute extrema). &mdash; Wikipedia

**definition**

the _global extrema_ **`x`** of a [[function]] **`f`** with [[function#domain]] **`D`** are defined as

**`f x |- f y > D y`** and **`f x -| f y > D y`**

**definition** the _global extrema_ of a [[function]] are the absolute highest and lowest points of the function

**definition** the _local extrema_ of a [[function]] are the highest and lowest points of the function within a given range

**theorem** if **`f`** has a local [[function#extremum]] at **`c`**, the point **`(c, f c)`** is a [[function#critical point]] of **`f`**, but not conversely

### First Derivative Test

let **`f`** be a [[function#continuous function]] near **`x = c`** and **`c`** be a critical number of **`f`**. then, **`f`** has a local [[function#extremum]] at **`c`** if **`dd f c -- dd c`** changes sign at **`c`**

### Second Derivative Test

let **`f`** be a [[function#continuous function]] near **`x = c`** and **`c`** be a critical number of **`f`** where **`dd f c -- dd c = 0`**. then, **`f`** has

- a local maximum at **`c`** if **`dd (dd f x -- dd x) -- dd x -| 0`**
- a local minimum at **`c`** if **`dd (dd f x -- dd x) -- dd x |- 0`**

> **note** the test is inconclusive if **`dd (dd f x -- dd x) -- dd x = 0`** or if it does not exist

## Inflection Point

**see** [[function#extremum]]

**definition** An _inflection point_ [...] is a point on a smooth plane [[curve]] at which the [[function#curvature]] changes sign &mdash; Wikipedia

**definition** a [[function]] **`f`** has an _inflection point_ at **`c`** if it is continuous at **`c`** and its [[function#concavity]] changes sign at **`c`**

> **note** a [[function]] having its second [[derivative]] equal to zero at **`c`** does not imply **`c`** is a [[function#inflection point]]. as an example, **`f x = x4`** does not have a [[function#inflection point]] at **`(x, f x) = (0, 0)`**

## Critical Point

**see** [[function]], [[math notation]]

**definition** _function of one variable_ a point **`(c, f c)`** is a _critical point_ of the [[function]] **`f`** if **`dd f c -- dd c = 0`** or it does not exist

**definition** _function of multiple variables_ a point **`(c, f c)`** is a _critical point_ of the [[function]] **`f`** if all components of **`dd f c -- dd c`** either are zero or do not exist

**definition** above, **`c`** would be said to be a _critical number_ of **`f`**

## [[mean value theorem]]

## [[intermediate value theorem]]

## Continuous Function

**see** [[math notation]]

**definition** a [[function]] **`f x`** is _continuous at **`x = a`**_ if **`f x {x -> a} = f a`**

> **note** above, **`f x {x -> a}`** must exist and **`f x`** must be defined at **`x = a`**

**definition** a [[function]] is _continuous from the left_ at **`a`** when **`f x {x -> a "from the left"} = f a`** and both other conditions are met

**definition** a [[function]] is _continuous from the right_ at **`a`** when **`f x {x -> a "from the right"} = f a`** and both other conditions are met

**definition** a [[function]] is _continuous on an [[interval]] **`a -| * -| b`**_ if it is continuous on every point from **`a`** to **`b`** exclusively, and continuous from the right at **`a`** and from the left at **`b`**

**definition** a [[function]] is _continuous_ (_globally continuous_) if it is continuous on every point of its [[function#domain]]

**theorem**

if **`f x`** and **`g x`** are continuous at **`a`**, then the following [[function]]s are also continuous at **`a`**:

- **`f : g`**
- **`f . g`**
- **`f | g`**
- **`cf`** where **`c`** is a [[scalar]]
- **`f -- g`** if **`g a + 0`** (restriction not necessary, see [[improved expression evaluation]])

## Reciprocal

_multiplicative inverse_

let **`f x`** be a function

**definition** if **`y = f x /\ y = --F x`**, then **`F`** is the _reciprocal_ of **`f`**

## Inverse

_switching input and output_

let **`f x`** be a function

**definition** if **`y = f x /\ x = F y`**, then **`F`** is the _inverse_ of **`f`**

> **note** the inverse of a [[function]] exists only if it is a [[function#injective function]]

**properties**

**`f F x = x`**

**`F f x = x`**

the graphs of **`(x, f x)`** and **`(x, F x)`** are symmetric about the [[line]] **`(x, x)`**

## Slope

**definition** **`x -> dd f x -- dd x`**

### Tangent Line

_used to represent [[function#slope]] at a point_

a tangent [[line]] has the same [[function#slope]] as a given [[function]] at a point

**definition**

**`L x = f a : (x . a | dd f a -- dd a)`**, where

- **`L`** is the [[line]] tangent to **`f`** at **`a`**

**applications**

the tangent of a [[function]] **`f`** approximates **`f (x ...)`** near a point **`(x ...)`**

[[function#tangent line]]s are used in [[newton's method]]

## Curvature

**definition** **`x -> dd (dd f x -- dd x) -- dd x`**

### Osculating Circle

_used to represent [[function#curvature]] at a point_

&mdash; <https://youtu.be/jvPPXbo87ds?t=1847>

an osculating [[circle]] has the same [[function#slope]] and the same [[function#curvature]] as a given [[function]] at a point

## Average

**see** [[integral]]

**definition**

**`f_"ave" = F b . F a -- b . a`**, where

- **`F`** is an [[antiderivative]] of **`f x`** with respect to **`x`**, **`$ f x | dd x`**
- **`f_"ave"`** is the _average_ of the [[function]] **`f x`** on the [[interval]] **`a -| * -| b`**

&mdash; <https://youtu.be/7gigNsz4Oe8?t=3093>

&mdash; <https://youtu.be/FnJqaIESC2s>

## Arclength

**see** [[integral]]

**definition** **`f_"arc" = $ \:(dd f t -- dd t)2/ | dd t`** where **`f t = (x, f x ...)`** &mdash; <https://tutorial.math.lamar.edu/classes/calciii/vectorarclength.aspx>

**definition** **`f_"arc" = $ \1 : [dd f x -- dd x]2/ | dd x`**

> **proof**
>
> the euclidean [[distance]] between two points is defined as **`d = \[DDx]2 : [DDf x]2/`**
>
> turning the [[distance]] [[function]] into an [[integral]], **`f_"arc" = $ \[dd x]2 : [dd f x]2/`**
>
> rearranging, **`f_"arc" = $ \[dd x]2 : [dd f x]2 -- [dd x]2/ | dd x`**
>
> and we get **`f_"arc" = $ \1 : [dd f x -- dd x]2/ | dd x`**
>
> &mdash; me

## Injective Function

_are multiple inputs collapsed into single outputs?_

**aka** _one-to-one function_

**definition** a [[function]] **`f`** is said to be _injective_ if **`f x_1 = f x_2 < x_1 = x_2`**, see [[set#universal set]]. _for every output value there exists at most one input mapping to it_

given the graph of a [[function]], one can use the _horizontal [[line]] test_ to determine whether it is injective or not

a [[function]] can be proven to be injective by proving that two output values being equal implies that the corresponding input values are equal

## Surjective Function

**aka** _onto function_

**definition** a [[function]] **`f`** with [[function#codomain]] **`C`** is said to be _surjective_ if **`C y < f x = y`**, see [[set#universal set]]. _for every output value there exists at least one input mapping to it_

a [[function]] can be proven to be surjective by proving one can construct an input value for the function given an arbitrary output value

> **example** _proving a function is surjective_
>
> let **`y = f m n = m : n`**. then, suppose **`m = 0`**. solving for **`n`**, we get **`n = y`**. therefore, the [[function]] is surjective

> **example** _proving a function is not surjective_
>
> let **`y = f m n = m2 : n2`**. **`y = .1`** would cause a [[contradiction]] as the square of an [[integer]] is always a positive [[integer]] and the sum of two positive [[integer]]s is always a positive [[integer]]. therefore, the [[function]] is not surjective

> **example** _proving a function is surjective_
>
> let **`y = f m n = m`**. then, we get **`m = y`** and therefore the [[function]] is surjective

> **example** _proving a function is not surjective_
>
> let **`y = f m n = "abs" n`**. **`y = .1`** would cause a [[contradiction]] as the [[real#absolute value]] of an [[integer]] is always a positive [[integer]]. therefore, the [[function]] is not surjective

> **example** _proving a function is surjective_
>
> let **`y = f m n = m . n`**. then, suppose **`n = 0`**. solving for **`m`**, we get **`m = y`**. therefore, the [[function]] is surjective

## Bijective Function

**definition** a [[function]] **`f`** is said to be _bijective_ if it is both injective and surjective. _for every output value there exists exactly one input mapping to it_

a [[function]] can be proven to be bijective by proving it is both injective and surjective

## Analytic Function

**see** [[derivative]]

**definition** an _analytic function_ is a [[function]] that is locally given by a [[series#convergent series]] [[series#power series]] &mdash; Wikipedia

**properties**

a [[function#analytic function]] is infinitely differentiable, but an infinitely differentiable [[function]] is not necessarily analytic &mdash; <https://youtu.be/X0razs3zR94?t=598>

analytic continuation of a [[function#analytic function]] is uniquely determined &mdash; <https://youtu.be/YuIIjLr6vUA?t=1746>

## Piecewise Function

**definition** in [[mathematics]], a _piecewise-defined function_ is a [[function]] defined by multiple sub-[[function]]s, where each sub-[[function]] applies to a different [[interval]] in the [[function#domain]] &mdash; Wikipedia

## Rational Function

_a function defined as a [[polynomial]] divided by another [[polynomial]]_

## Pure Function

**definition** a _pure function_ is a [[function]] that has no side effects and that does not depend on external state

of course, any [[function]] can be thought of as having side effects. for example, running a [[function#pure function]] on a CPU still consumes a measurable amount of [[energy]], modifying the entropy of the universe &mdash; <https://youtu.be/APUCMSPiNh4?t=2594>. practically, however, this definition remains useful

**properties**

pure [[function]]s can be memoized using a [[map]]

## Total Function

_a [[function]] that doesn't "lie" in its [[type]] signature_

a [[function#total function]] maps every element of its [[function#domain]] to an element of its [[function#codomain]]

> **example**
>
> let the following [[function]]:
>
> ```rust
> fn twelveOver(x: f64) -> f64 {
>   12 / x
> }
> ```
>
> even though the [[type]] signature of the [[function]] is `fn(f64) -> f64`, it won't be able to return a value if the input is `0`. most developers would add an `if` check and throw an [[exception]] if that were the case, which makes the [[type]] signature a "lie". however, in [[functional programming]], one of the following strategies should be used instead:
>
> - restrict the input of the [[function]] (`nonZeroF64` is an example)
> - extend the output of the [[function]] (`Option<f64>` is an example)

## Higher-Order Function

_[[function]]s as [[type]]s_

**definition** a _higher-order function_ is a [[function]] that takes a [[function]] as an argument or returns a [[function]]

**definition** a _first-order function_ is a [[function]] whose arguments and return values are not [[function]]s

## Parametrically Polymorphic Function

**definition** a [[function]] is said to be _parametrically polymorphic_ if it is possible to replace the [[type]] of its input with a different [[type]] without having any effect on its behavior. such [[function]]s can be implemented with the same "formula" for any [[type]]. &mdash; <https://youtu.be/aIOMRqiwziM?t=540>

## Idempotent Function

&mdash; <https://en.wikipedia.org/wiki/Idempotence>

&mdash; <https://youtu.be/VvUdvte1V3s?t=1261>

**definition** _[[procedural programming]]_ a [[function]] with side effects is said to be _idempotent_ if calling it multiple times results in the same system state as calling it once

> **example** HTTP `GET`, `PUT` and `DELETE` are all idempotent

**definition** _[[functional programming]] and [[mathematics]]_ an element **`x`** of a [[set]] **`S`** equiped with an [[operator]] **`*`** is said to be _idempotent under **`*`**_ if **`x * x = x`**

**definition** _[[functional programming]] and [[mathematics]]_ a [[function]] **`f`** is said to be _idempotent_ if **`f x = f (f x)`** for all **`x`** and, equivalently, an [[operator]] **`*`** on a set **`S`** is said to be _idempotent_ if **`x * x = x`** for all **`S x`**

> **example** in the [[monoid]] **`{NN, {|}}`**, only **`0`** and **`1`** are idempotent

> **example** in a [[group]] **`{GG, {:}}`**, only **`O`** (the identity element) is idempotent

> **example** **`"abs"`** is a [[function#idempotent function]] because **`"abs" x = "abs" "abs" x`** for all **`x`**
