# Derivative Rules

**see** [[derivative]] notation, [[math notation]]

## power rule

**`dd x. x[n] = x. nx[n..1]`**

### derived shortcuts

**`dd x. c = .0`**

**`dd x. x = .1`**

## [[exponent]]ial rule

**`dd x. a[x] = x. a[x]/a\`**

> **proof**
>
> **`a[x] = [/a[x]\] = [x/a\]`**
>
> **`dd x. a[x] = (x. [x/a\]) | dd x. x/a\ = x. a[x]/a\`**
>
> &mdash; me

### derived shortcuts

**`dd x. [x] = x. [x]`**

**`dd f = mf == f = x. [mx]`**

## [[logarithm]] rule

**`dd x. /x\b = x. --x/b\`**

### derived shortcuts

**`dd x. /x\ = x. --x`**

> **proof** &mdash; <https://youtu.be/qb40J4N1fa4?t=762>

**`dd x. /"abs" x\ = --x`**

> **proof** define as a piecewise [[function]] and compute both [[derivative]]s

**`dd (x. /"abs" x\ : c x) = --x`** and therefore

**`$ x. --x = /"abs" x\ : c x`** where **`c x = {c_0, c_1} (x -| 0)`**

> **proof** &mdash; <https://youtu.be/u4kex7hDC2o>

## constant multiple rule

if **`c`** is a scalar and **`f`** is differentiable, then

**`dd cf = cdd f`**

## sum rule

**`dd (f:g) = dd f : dd g`**

## difference rule

**`dd (f..g) = dd f .. dd g`**

> **proof** derive from the sum rule, **`f..g = f : (..1)g`**

## product rule

**`dd f'g = f'dd g : g'dd f`**

## quotient rule

**`dd f-g = g'dd f .. f'dd g -- g'g`**

> **proof** derive from the product and power rules, **`f-g = f | g[..1]`**

> **[[mnemonic]]** lo d-hi, minus hi d-lo, over lo-lo

### derived reciprocal rule

**`dd -f = ..dd f -- f'f`**

> **proof** derive from the power rule, **`-f = f[..1]`**

## chain rule

**``dd f`g = dd f \\ g | dd g``**

> **proof** **``dd f \\ g | dd g = (dd f`g -- dd g) | dd g = dd f`g``**

### derived inverse rule

**``dd `f = --(dd f \\ `f)``** #todo inv

> **proof** derive from the chain rule, **`dd f``f = dd (*) = .1`** #todo inv #todo id &mdash; me
