## Binomial Distribution

**see** [[math notation]], [[probability distribution]]

&mdash; <https://en.wikipedia.org/wiki/Binomial_distribution>

**definition** the [[probability mass function]] of a binomial distribution is **`k -> C n k | [p]k | [1.p](n.k)`**, where

- **`C`** is a [[set#combination]]
- **`p`** is the [[probability]] of success of a [[bernoulli trial]]
- **`n`** is the number of [[bernoulli trial]]s in a [[sample]] **`X`**
- **`k`** is the number of successes in a [[sample]] **`X`**

the [[probability mass function]] of a [[binomial distribution]] represents the [[probability]] of exactly **`k`** successes in **`n`** independent [[bernoulli trial]]s with [[probability]] **`p`** of success

> **note** the definition above can be understood as follows. the [[probability]] of **`k`** successes is **`[p]k`** and the [[probability]] of **`n.k`** failures is **`[1.p](n.k)`**. the [[probability]] of **`k`** successes followed by **`n.k`** failures is **`[p]k | [1.p](n.k)`** by the [[probability#prduct rule]]. however, the number of ways to arrange **`k`** successes and **`n.k`** failures is **`C n k`**. therefore, the probability of **`k`** successes occuring **anywhere** in **`n`** [[bernoulli trial]]s is **`C n k | [p]k | [1.p](n.k)`** &mdash; me

**representation**

![[Pasted image 20230710113541.png]]
