# Derivative Rules

**see** [[derivative]] notation, [[math notation]]

## power rule

**`dd x[n] -- dd x= nx[n . 1]`**

### derived shortcuts

**`dd c -- dd x = 0`**

**`dd x -- dd x = 1`**

## [[exponent]]ial rule

**`dd a[x] -- dd x = a[x] | /a\`**

> **proof**
>
> **`a[x] = [ \a[x]/ ] = [x /a\ ]`**
>
> **`dd a[x] -- dd x = [x /a\ ] | dd x /a\ -- dd x = [a]x | /a\`**
>
> &mdash; me

### derived shortcuts

**`dd [x] -- dd x = [x]`**

**`dd f x -- dd x = mf x == f x = [mx]`**

> **example** let **`g x = eex2 : 2ee[x] : xee2 : x[ee2]`**. then, **`dd g x -- dd x = 2ee x : 2ee[x] : ee2 : ee2 x[ee2.1]`**

## [[logarithm]] rule

**`dd /x\ b -- dd x = -- x /b\`**

### derived shortcuts

**`dd /x\ -- dd x = --x`**

> **proof** let **`y = /x\`**. then,
>
> **`x = [y]`**
>
> **`dd x = [y] | dd y`**
>
> **`dd y -- dd x = --[y]`**
>
> **`dd /x\ -- dd x = --x`**
>
> &mdash; <https://youtu.be/qb40J4N1fa4?t=762>

**`dd /||x||\ -- dd x = --x`**

> **proof** define as a [[function#piecewise function]] and compute both [[derivative]]s

**`dd ( /||x||\ : c x) -- dd x = --x`** and therefore

**`$ --x | dd x = /||x||\ : c x`** where **`c x = {c_0, c_1} (x -| 0)`**

> **proof** &mdash; <https://youtu.be/u4kex7hDC2o>

## constant multiple rule

if **`c`** is a [[real]] and **`f`** is differentiable, then

**`dd (cf x) -- dd x = c(dd f x -- dd x)`**

## sum rule

**`dd (f x : g x) -- dd x = (dd f x -- dd x) : (dd g x -- dd x)`**

## difference rule

**`dd (f x . g x) -- dd x = (dd f x -- dd x) . (dd g x -- dd x)`**

> **proof** derive from the sum rule, **`f x . g x = f x : (.1 | g x)`**

## product rule

**`dd (f x | g x) -- dd x = (f x | dd g x -- dd x) : (g x | dd f x -- dd x)`**

## quotient rule

**`dd (f x -- g x) -- dd x = (g x | dd f x -- dd x) . (f x | dd g x -- dd x) -- [g x]2`**

> **proof** derive from the product and power rules, **`f x -- g x = f x | [g x](.1)`**

### [[mnemonic]]

> lo d-hi, minus hi d-lo, over lo-lo

### derived reciprocal rule

**`dd (--f x) -- dd x = .dd f x -- dd x -- [f x]2`**

> **proof** derive from the power rule, **`--f x = [f x](.1)`**

## chain rule

**`dd f g x -- dd x = dd g x -- dd x | dd f g x -- dd g x`**

> **proof** **`(dd g x) -- dd x | dd f g x -- (dd g x) = dd f g x -- dd x`**
