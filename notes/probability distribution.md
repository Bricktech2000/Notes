# Probability Distribution

_a mathematical description of the [[probability]]es of events_

&mdash; <https://en.wikipedia.org/wiki/Probability_distribution>

## Normal Distribution

**aka** _gaussian distribution_

&mdash; <https://en.wikipedia.org/wiki/Normal_distribution>

**definition** the [[probability distribution#probability density function]] of a normal distribution is $x \rightarrow G^\sigma\ (x \cdot \mu)$, where

- $x$ is an _example_ in a [[sample]] $X$
- $\mu$ is the [[mean]] of $X$
- $\sigma$ is the [[standard deviation]] of $X$
- $G^\sigma$ is the [[gaussian function]] with [[standard deviation]] $\sigma$ and [[mean]] $0$

**representation**

![[Pasted image 20221127185202.png]]

**properties**

> partly due to the [[central limit theorem]], [...] physical quantities that are expected to be the sum of many independent processes, such as measurement errors, often have [[probability distribution]]s that are nearly normal &mdash; Wikipedia

as a rule of thumb, in a [[probability distribution#normal distribution]],

- $68\text-100$ of the values are within $1 \sigma$ of the [[mean]]
- $95\text-100$ of the values are within $2 \sigma$ of the [[mean]]
- $99\ 7\text-1000$ of the values are within $3 \sigma$ of the [[mean]]

> **proof**
>
> let $G^\sigma$ be the [[gaussian function]] with [[standard deviation]] $\sigma$ and [[mean]] $0$. then,
>
> - $\int G^1\ x \mid \delta x\ \braket{1 \cdot \cdot 1}$ is approximately $68\text-100$
> - $\int G^1\ x \mid \delta x\ \braket{2 \cdot \cdot 2}$ is approximately $95\text-100$
> - $\int G^1\ x \mid \delta x\ \braket{3 \cdot \cdot 3}$ is approximately $99\ 7\text-1000$

### Standard Normal Distribution

**definition** the [[probability distribution#probability density function]] of a standard normal distribution is $G^1$, where

- $G^1$ is the [[gaussian function]] with [[standard deviation]] $1$

**definition** the standard normal distribution is the normal distribution with $\mu = 0$ and $\sigma = 1$

## Continuous Uniform Distribution

&mdash; <https://en.wikipedia.org/wiki/Continuous_uniform_distribution>

**definition** the [[probability distribution#probability density function]] of a continuous uniform distribution is $x \rightarrow \braket{0, - b \cdot a}\ (a \dashv x \dashv b)$, where

- $x$ is an _example_ in a [[sample]] $X$
- $a$ is the minimum of $X$
- $b$ is the maximum of $X$

**representation**

![[Pasted image 20221127184826.png]]

## Skew

_a measure of the asymmetry of a [[probability distribution]]_

---

# Representation

there are different ways of representing [[probability distribution]]s, outlined below

## Probability Mass Function

**definition** a _probability mass function_ is a [[function]] $f$ that [[map]]s an event to its [[probability]] of occurrence such that $\,: f = 1$

> **example** the probability mass function of a fair dice roll is $x \rightarrow -6$

**applications**

probability mass functions are used to describe discrete random variables

## Probability Density Function

**aka** _PDF_

**see** [[integral]]

**definition** a _probability density function_ is a [[function]] $f$ such that $\int f\ x \mid \delta x\ \braket{b \cdot a}$ is the [[probability]] of an _example_ being in the interval $a \dashv \circ \dashv b$

**applications**

probability density functions are used to describe continuous random variables

## Cumulative Distribution Function

**aka** _CDF_

**see** [[integral]]

**definition** a _cumulative distribution function_ is a [[function]] $F$ such that $F\ a$ is the [[probability]] of an _example_ being in the interval $\cdot \infty \dashv \circ \dashv a$

**definition** $\int f\ x \mid \delta x\ \braket{x \cdot \cdot \infty}$ where $f$ is a [[probability distribution#probability density function]]

**applications**

cumulative distribution functions are used to describe continuous random variables
