# Normal Distribution

**see** [[math notation]], [[probability distribution]]

**aka** _gaussian distribution_

--- <https://en.wikipedia.org/wiki/Normal_distribution>

**definition** the [[probability density function]] of a normal distribution is **`x -> G^ss (x . mm)`**, where

- **`x`** is an _example_ in a [[sample]] **`X`**
- **`mm`** is the [[mean]] of **`X`**
- **`ss`** is the [[standard deviation]] of **`X`**
- **`G^ss`** is the [[gaussian function]] with [[standard deviation]] **`ss`** and [[mean]] **`0`**

**representation**

![[Pasted image 20221127185202.png]]

**properties**

_partly due to the [[central limit theorem]], [...] physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have [[probability distribution]]s that are nearly normal_ --- Wikipedia

as a rule of thumb, in a [[normal distribution]],

- **`68-100`** of the values are within **`1 ss`** of the [[mean]]
- **`95-100`** of the values are within **`2 ss`** of the [[mean]]
- **`99 7-1000`** of the values are within **`3 ss`** of the [[mean]]

> **proof**
>
> let **`G^ss`** be the [[gaussian function]] with [[standard deviation]] **`ss`** and [[mean]] **`0`**. then,
>
> - **`$ G^1 x | dd x {1 . .1} ~ 68-100`**
> - **`$ G^1 x | dd x {2 . .2} ~ 95-100`**
> - **`$ G^1 x | dd x {3 . .3} ~ 99 7-1000`**

offsetting a [[normal distribution]] upward or downward may not have much of an effect in the middle of the distribution but can have a huge impact at the tails of the distribution --- <https://youtu.be/h02w5E7FGlY?t=948>

> **example**
>
> let two [[normal distribution]]s **`A = G^ss /\ B = G^ss : 4-11ss`**. then, given [[outcome]]s **`a`** from **`A`** and **`b`** from **`B`**, the [[probability]] that **`a |- b`** is **`6-10`**, which is relatively close to fifty-fifty. however, the [[probability]] that **`a |- 2ss`** is **`5-2`** times higher than the [[probability]] that **`b |- 2ss`**, which is way larger of a difference
>
> > **proof**
> >
> > ```python
> > import numpy as np
> >
> > trails = 1000000
> > matches = (np.random.normal(0, 1, trails) < np.random.normal(4/11, 1, trails)).sum()
> >
> > print(matches / trails) # prints approximately 0.6
> > ```
>
> > **proof** **`($ G^1 x | dd x {@@ . 2}) -- ($ G^1 x : 4-11 | dd x {@@ . 2}) ~ 5-2`**

### Standard Normal Distribution

**see** [[standard normal table]]

**definition** the [[probability density function]] of a standard normal distribution is **`G^1`**, where

- **`G^1`** is the [[gaussian function]] with [[standard deviation]] **`1`** and [[mean]] **`0`**

**definition** the standard normal distribution is the normal distribution with **`mm = 0`** and **`ss = 1`**
