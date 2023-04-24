# Derivative Rules

**see** [[derivative]] notation, [[math notation]]

## power rule

**`\d x[n] -- \d x= nx[n . 1]`**

### derived shortcuts

**`\d c -- \d x = 0`**

**`\d x -- \d x = 1`**

## [[exponent]]ial rule

**`\d a[x] -- \d x = a[x] | /a\`**

> **proof**
>
> **`a[x] = [ \a[x]/ ] = [x /a\ ]`**
>
> **`\d a[x] -- \d x = [x /a\ ] | \d x /a\ -- \d x = [a]x | /a\`**
>
> &mdash; me

### derived shortcuts

**`\d [x] -- \d x = [x]`**

**`\d f x -- \d x = mf x == f x = [mx]`**

> **example** let **`g x = \ex2 : 2\e[x] : x\e2 : x[\e2]`**. then, **`\d g x -- \d x = 2\e x : 2\e[x] : \e2 : \e2 x[\e2.1]`**

## [[logarithm]] rule

**`\d /x\ b -- \d x = -- x /b\`**

### derived shortcuts

**`\d /x\ -- \d x = --x`**

> **proof** let **`y = /x\`**. then,
>
> **`x = [y]`**
>
> **`\d x = [y] | \d y`**
>
> **`\d y -- \d x = --[y]`**
>
> **`\d /x\ -- \d x = --x`**
>
> &mdash; <https://youtu.be/qb40J4N1fa4?t=762>

**`\d /||x||\ -- \d x = --x`**

> **proof** define as a [[function#piecewise function]] and compute both [[derivative]]s

**`\d ( /||x||\ : c x) -- \d x = --x`** and therefore

**`$ --x | \d x = /||x||\ : c x`** where **`c x = {c_0, c_1} (x -| 0)`**

> **proof** &mdash; <https://youtu.be/u4kex7hDC2o>

## constant multiple rule

if **`c`** is a [[real]] and **`f`** is differentiable, then

**`\d (cf x) -- \d x = c(\d f x -- \d x)`**

## sum rule

**`\d (f x : g x) -- \d x = (\d f x -- \d x) : (\d g x -- \d x)`**

## difference rule

**`\d (f x . g x) -- \d x = (\d f x -- \d x) . (\d g x -- \d x)`**

> **proof** derive from the sum rule, **`f x . g x = f x : (.1 | g\ x)`**

## product rule

**`\d (f x | g x) -- \d x = (f x | \d g x -- \d x) : (g x | \d f x -- \d x)`**

## quotient rule

**`\d (f x -- g x) -- \d x = (g x | \d f x -- \d x) . (f x | \d g x -- \d x) -- [g x]2`**

> **proof** derive from the product and power rules, **`f x -- g x = f x | [g x](.1)`**

### [[mnemonic]]

> lo d-hi, minus hi d-lo, over lo-lo

### derived reciprocal rule

**`\d (--f x) -- \d x = .\d f x -- \d x -- [f x]2`**

> **proof** derive from the power rule, **`--f x = [f x](.1)`**

## chain rule

**`\d f g x -- \d x = \d g x -- \d x | \d f g x -- \d g x`**

> **proof** **`(\d g x) -- \d x | \d f g x -- (\d g x) = \d f g x -- \d x`**
