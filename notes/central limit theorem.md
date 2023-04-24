# Central Limit Theorem

&mdash; <https://youtu.be/zeJD6dqJ5lo>

**theorem** _central limit theorem_ given a sufficiently large [[set]] of sufficiently large [[sample]]s **independent from eathother** drawn from the **same [[probability distribution]]** with **finite [[variance]]**,

1. the [[sample]] [[mean]]s are approximately normally distributed, see [[probability distribution#normal distribution]]
2. the [[sample]] [[mean]]s have a [[mean]] approximately equal to the [[population]] [[mean]]
3. the [[sample]] [[mean]]s have a [[variance]] approximately equal to the [[population]] [[variance]] divided by the [[sample]] size

**properties**

by `2`, the [[sample]] [[mean]]s are unbiased estimators of the [[population]] [[mean]]

by `1.` and `3.`, the [[standard deviation]] of the [[sample]] [[mean]]s decreases as the [[sample]] size increases but remains stable as the number of [[sample]]s increases

by `3.`, the _standard error of the mean_, defined as **`\s - \n/`** where **`\s`** is the [[population]] [[standard deviation]] and **`n`** is the [[sample]] size, is approximately equal to the [[standard deviation]] of the [[sample]] [[mean]]s

generally, the [[standard deviation]] of a [[sample]] becomes a better estimation of the [[population]] [[standard deviation]] as the [[sample]] size increases and as the [[population]] [[probability distribution#skew]] decreases, but remains stable as the [[population]] size increases

> **note** the properties above can be used to create a [[confidence interval]] for the [[population]] [[mean]] given a single [[sample]]
>
> an estimate of the [[population]] [[probability distribution#skew]] can be used to determine an appropriate [[sample]] size. the [[standard deviation]] of that appropriately sized [[sample]] can be used to estimate the [[population]] [[standard deviation]]. the [[population]] [[standard deviation]] estimate along with the [[sample]] size can be used to estimate the [[standard deviation]] of [[sample]] [[mean]]s through the _standard error of the mean_. the original [[sample]] [[mean]] can be used to estimate the [[population]] [[mean]]. this estimated [[population]] [[mean]] along with the estimated [[standard deviation]] of [[sample]] [[mean]]s can be used to create a [[confidence interval]] on the [[population]] [[mean]]
