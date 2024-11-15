# Integral

**see** [[math notation]], [[function]], [[antiderivative]], [[calculus notation]]

**notation** _in [[conventional math notation]]_

with **`dd F x -- dd x = f`**,

$F\ x\ \bigr|_{a}^{b} \dots = F\ b \cdot F\ a$

**definition** a _definite integral_ has its two endpoints present

**definition** an _indefinite integral_ has its two endpoints missing

**definition** the _integrand_ is the [[function]] being integrated. it would be **`f x`** in the [[integral]] **`$ f x | dd x`**

---

# Integration

## [[antiderivative#antidifferentiation]]

**see** [[antiderivative#antidifferentiation]]

## Improper Integration

### type I

_an [[integral]] with at least one endpoint being infinite_

**theorem** **`$ f x | dd x {@@ . a} == $ f x | dd x {t . a} {t -> @@}`**

**theorem** **`$ f x | dd x {b . .@@} == $ f x | dd x {b . t} {t -> .@@}`**

a Type I improper [[integral]] is said to:

- converge if the [[limit]] exis, see [[limit#existence]]
- diverge if the [[limit]] does not exist, see [[limit#existence]]

### type II

_an [[integral]] whose integrand has a [[function]] discontinuity on the integration [[interval]]_

**theorem** if **`f x {x -> b "from the left"} = {@@ \/ .@@}`** #xxx [[improved expression evaluation]], then **`$ f x | dd x {b . a} == $ f x | dd x {t . a} {t -> b "from the left"}`**

**theorem** if **`f x {x -> a "from the right"} = {@@ \/ .@@}`** #xxx [[improved expression evaluation]], **`$ f x | dd x {b . a} == $ f x | dd x {b . t} {t -> a "from the right"}`**

### comparison test

**theorem** _Comparison Test_

let **`0 -| g x -| f x`** on an [[interval]] **`a {-|/\+} * {-|/\+} b`**, where **`a`** and **`b`** are not necessarily finite. then,

- if **`$ f x | dd x {b . a}`** converges, so does **`$ g x | dd x {b . a}`**, but not conversely
- if **`$ g x | dd x {b . a}`** diverges, so does **`$ f x | dd x {b . a}`**, but not conversely

### p-test

--- <https://youtu.be/TKIdC847K3k>

**theorem** _P-Test_

the [[integral]] **`$ --[x]p | dd x {@@ . 1}`**:

- converges if **`p {|-/\+} 1`**
- diverges if **`p -| 1`**

## Numerical Integration

the definite [[integral]] of a [[function]] can be estimated by the [[monte carlo method]] by generating a finite number of random points and calculating the ratio between the number of points under the [[function]] and the total number of points --- <https://youtu.be/rUxP7TM8-wo?t=2925>. the accuracy of such an [[algorithm]] can be measured through [[inferential statistics]]
