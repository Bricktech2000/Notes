# Probability Distribution

_a mathematical description of the [[probability]]es of events_

&mdash; <https://en.wikipedia.org/wiki/Probability_distribution>

## Normal Distribution

**aka** _gaussian distribution_

&mdash; <https://en.wikipedia.org/wiki/Normal_distribution>

**definition** the [[probability distribution#probability density function]] of a normal distribution is **`x -> G^\s (x . \m)`**, where

- **`x`** is an _example_ in a [[sample]] **`X`**
- **`\m`** is the [[mean]] of **`X`**
- **`\s`** is the [[standard deviation]] of **`X`**
- **`G^\s`** is the [[gaussian function]] with [[standard deviation]] **`\s`** and [[mean]] **`0`**

**representation**

![[Pasted image 20221127185202.png]]

**properties**

> partly due to the [[central limit theorem]], [...] physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have [[probability distribution]]s that are nearly normal &mdash; Wikipedia

as a rule of thumb, in a [[probability distribution#normal distribution]],

- **`68-100`** of the values are within **`1 \s`** of the [[mean]]
- **`95-100`** of the values are within **`2 \s`** of the [[mean]]
- **`99 7-1000`** of the values are within **`3 \s`** of the [[mean]]

> **proof**
>
> let **`G^\s`** be the [[gaussian function]] with [[standard deviation]] **`\s`** and [[mean]] **`0`**. then,
>
> - **`$ G^1 x | \d x {1 . .1}`** is approximately **`68-100`**
> - **`$ G^1 x | \d x {2 . .2}`** is approximately **`95-100`**
> - **`$ G^1 x | \d x {3 . .3}`** is approximately **`99 7-1000`**

[[standard normal table]]

### Standard Normal Distribution

**definition** the [[probability distribution#probability density function]] of a standard normal distribution is **`G^1`**, where

- **`G^1`** is the [[gaussian function]] with [[standard deviation]] **`1`** and [[mean]] **`0`**

**definition** the standard normal distribution is the normal distribution with **`\m = 0`** and **`\s = 1`**

## Continuous Uniform Distribution

&mdash; <https://en.wikipedia.org/wiki/Continuous_uniform_distribution>

**definition** the [[probability distribution#probability density function]] of a continuous uniform distribution is **`x -> {0, -- b . a} (a -| x -| b)`**, where

- **`x`** is an _example_ in a [[sample]] **`X`**
- **`a`** is the minimum of **`X`**
- **`b`** is the maximum of **`X`**

**representation**

![[Pasted image 20221127184826.png]]

## Skew

_a measure of the asymmetry of a [[probability distribution]]_

---

# Representation

there are different ways of representing [[probability distribution]]s, outlined below

## Probability Mass Function

**definition** a _probability mass function_ is a [[function]] **`f`** that [[map]]s an event to its [[probability]] of occurrence such that **`:f = 1`**

> **example** the probability mass function of a fair dice roll is **`x -> --6`**

**applications**

probability mass functions are used to describe discrete random variables

## Probability Density Function

**aka** _PDF_

**see** [[integral]]

**definition** a _probability density function_ is a [[function]] **`f`** such that **`$ f x | \d x {b . a}`** is the [[probability]] of an _example_ being in the interval **`a -| * -| b`**

**applications**

probability density functions are used to describe continuous random variables

**properties**

**`$ f x | \d x {@@ . .@@} = 1`** where **`f`** is a _probability density function_

## Cumulative Distribution Function

**aka** _CDF_

**see** [[integral]]

**definition** a _cumulative distribution function_ is a [[function]] **`F`** such that **`F a`** is the [[probability]] of an _example_ being in the interval **`.@@ -| * -| a`**

**definition** **`$ f x | \d x {x . .@@}`** where **`f`** is a [[probability distribution#probability density function]]

**applications**

cumulative distribution functions are used to describe continuous random variables

**properties**

**`F @@ = 1`** where **`F`** is a _cumulative distribution function_
