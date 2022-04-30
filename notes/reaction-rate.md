# Reaction Rate

see [[classical-math-notation]]

> The reaction rate or rate of reaction is the speed at which a chemical reaction takes place, defined as proportional to the increase in the concentration of a product per unit time and to the decrease in the concentration of a reactant per unit time. Reaction rates can vary dramatically. &mdash; Wikipedia

_only questions on **first-order reactions** will be asked in [[chm1301-principles-of-chemistry]]_

## Formulas

### The Rate Law

in a reaction $aA + bB \rightarrow cC + dD$,

$Rate = k[A]^m[B]^n$, where

$k$ is the _rate constant_. it is specific for a reaction at a single temperature and doesn't change as the reaction proceeds

$m$ and $n$ are the _reaction orders_

> **note**: the [[stoichiometry]]c coefficients $a$ and $b$ are not necessarily related to the reaction orders (partial orders) $m$ and $n$, see [[reaction-mechanism]]s

> **note**: $Rate$, $m$ , $n$ and $k$ must be found by experiment and cannot be determined mathematically

### other formula

$Rate = -\frac{\Delta [A]}{a\Delta t} = \frac{\Delta [B]}{b\Delta t} = +\frac{\Delta [C]}{c\Delta t} = +\frac{\Delta [D]}{d\Delta t}$, where

$[X]$ is the molar [[concentration]] of a reactant or product

$x$ is the [[stoichiometry]]c coefficient of reactant or product $X$

$t$ is the amount of time elapsed

## Orders

A reaction has an _individual order_ "in respect to" or "in" each reactant, and an _overall order_

$\text{Overall Order} = \sum \text{Individual Order}_i$

## Determining Orders by Changing Reactant Concentrations

$\frac{Rate_2}{Rate_1} = \frac{k[A]_2^m[B]_2^m}{k[A]_1^m[B]_1^m}$

cancel out the constants $k$ and the concentrations that don't happen to change (for instance, $[B]_2$ with $[B]_1$). then, substitute the rates and remaining concentrations to determine $m$ and $n$

## Integrating Over Time

_relationship between elapsed time and concentration_

for a general **first-order** reaction,

$Rate = -\frac{\Delta[A]}{\Delta t} = k[A]$

after integrating over time, we get

$\ln \frac{[A]_t}{[A]_0} = -kt$, where

$t$ is the time representing the progress of the reaction

$k$ is the [[reaction-rate]] constant, expressed in $t^{-1}$

$[A]$ is the concentration of a reactant

for a **zero-order** reaction,

$Rate = -\frac{\Delta[A]}{\Delta t} = k$

after integrating over time, we get

$[A]_t - [A]_0 = -kt$

for calculating **half-lives of second-order** reactions,

by definition, we know that $t = t_{1/2}$ and $[A]_t = \frac{1}{2}[A]_0$

after solving for $t_{1/2}$, we get

$k t_{1/2} = \ln 2$, where

$t_{1/2}$ is the half-life of the reaction

$k$ is the rate constant, expressed in $t^{-1}$

the **half-life of a first-order** reaction is constant

## Rates over Temperature

_finding $k$ at one temperature given $k$ at another temperature_

using the Arrhenius equation, we can derive the Van't Hoff equation

$k = Ae^{-\frac{E_a}{RT}} \\\  \ln k = \ln A - \frac{E_a}{RT} \\\  \ln k = -\frac{E_a}{R} \times \frac{1}{T} + \ln A \\\  y = m x + b \\\  \ln \frac{k_2}{k_1} = -\frac{E_a}{R}(\frac{1}{T_2} - \frac{1}{T_1})$, where

$k$ is the [[reaction-rate]] constant, expressed in $t^{-1}$

$A$ is the pre-exponential factor / the frequency factor. it does have a slight dependence on temperature, but we will assume it changes negligibly in respect to temperature.

$E_a$ is the activation energy, or $\Delta_rH^0$

$R$ is the [[ideal-gas]] constant, $8.314\frac{J}{mol K}$

$T$ is the absolute temperature, in $K$

$e$ is Euler's constant [[e]]
