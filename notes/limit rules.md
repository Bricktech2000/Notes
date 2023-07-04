# Limit Rules

**see** [[math notation]]

let **`c`** be a constant and ensure **`f x {x -> a}`** and **`g x {x -> a}`** are [[limit]]s that exist, see [[limit#existence]]

## sum rule

**`f x : g x {x -> a} = (f x {x -> a}) : (g x {x -> a})`**

## difference rule

**`f x . g x {x -> a} = (f x {x -> a}) . (g x {x -> a})`**

## constant multiple rule

**`cf x {x -> a} = c(f x {x -> a})`**

## product rule

**`f x | g x {x -> a} = (f x {x -> a}) | (g x {x -> a})`**

## quotient rule

**`f x -- g x {x -> a} = (f x {x -> a}) -- (g x {x -> a}) > g x {x -> a} + 0`** (restriction not necessary, see [[improved expression evaluation]])

## power rule

**`[f x]n {x -> a} = [f x {x -> a}]n`**

### derived radical rule

**`\f x/ n {x -> a} = \f x {x -> a}/ n`**. when **`EE n`** (see [[even number]]), we assume that **`f x {x -> a} + 0`** (restriction might not be necessary, see [[improved expression evaluation]])

## composition rule

**`f g x {x -> a} = f (g x {x -> a})`** if **`f`** is a [[function#continuous function]] at **`a`**

## infinity rules

**`[x]r {x -> @@} = 0 > r {-|/\+} 0`**

**`--x {x -> 0} = {@@ \/ .@@}`** #think [[improved expression evaluation]]

## squeeze theorem

**theorem** _Squeeze Theorem_

let **`f x -| g x -| h x`** for **`x`** near a value **`a`**

if **`f x {x -> a} = h x {x -> a} = L`**, then **`g x {x -> a} = L`**

## l'Hopital's rule

**aka** _L'Hôpital's rule_

_used to compute [[limit]]s in [[limit#indeterminate form]]s using their [[derivative]]s_

**theorem**

let **`f x`** and **`g x`** be differentiable [[function]]s on an open [[interval]] **`I /\ +a`**. if **`dd g x -- dd x + 0 > (I /\ +a) x`** (restriction not necessary, see [[improved expression evaluation]]) and **`f x {x -> a} = g x {x -> a} = 0`** and **`dd f x -- dd g x {x -> a}`** is a [[limit]] that exists, then **`f x -- g x {x -> a} = dd f x -- dd g x {x -> a}`** &mdash; Wikipedia

intuitive explanation &mdash; <https://youtu.be/kfF40MiS7zA?t=734>

other [[limit#indeterminate form]]s can be rewritten to use L'Hopital's rule:

- **`@@ -- @@`**: **`(--@@) -- (--@@) -> 0 -- 0`**
- **`0 | @@`**: **`0 -- (--@@) -> 0 -- 0`** or **`(--0) -- @@ -> 0 -- 0`**
- **`[1]@@`**: **`/[1]@@\ -> @@ /1\ -> @@ | 0 -> 0 -- 0`**
- **`[@@]0`**: **`/[@@]0\ -> 0 /@@\ -> 0 | @@ -> 0 -- 0`**
- **`[0]0`**: **`/[0]0\ -> 0 /0\ -> 0 | .@@ -> 0 -- 0`**

**examples**

> **example** _[[limit]]s that can be computed using L'Hopital's rule_:
>
> **`x -- 3[x] {x -> @@}`**
>
> **`"sin" x . x -- ["sin" x]3 {x -> 0}`**
>
> **`"sin" x . x -- ["sin" x]3 {x -> 0}`**
>
> **`"sin" x /x\ {x -> 0 "from the right"}`**
>
> **`[1 : -x]x {x -> @@}`**
