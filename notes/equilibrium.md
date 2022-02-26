# Equilibrium

see [[classical-math-notation]]

see [[stoichiometry]], [[concentration]], [[reaction-rate]]s

all reactions have to be reversible for equilibrium to be reached

at equilibrium, $rate_{forward} = rate_{reverse}$. no net change is observed

$K = \frac{k_{fwd}}{k_{rev}}$ where $K$ is the equilibrium constant (or formally, the _thermodynamic equilibrium constant_)

## Le Châtelier's Principle

> A system at equilibrium will respond to external stress by minimizing the stress. — Rashmi

## Formulas

### General Formula

let $aA + bB \Leftrightarrow cC + dD$

$Q = Q_c = \frac{[C]^c[D]^d}{[A]^a[B]^b}$ or $Q = Q_p = \frac{p_C^cp_D^d}{p_A^ap_B^b}$ for gaseous reactants or products

where $Q$ is the reaction quotient, $p$ are pressures in $bar$ and $[X]$ are molar [[concentration]]s

### Heterogeneous Equilibrium

_involving reactants or products in different phases_

> The expressions of $K$ and $Q$ include only species whose concentrations change as the reaction approaches equilibrium

for example, with $CaCO_{3(s)} \Leftrightarrow CaO_{(s)} + CO_{2(g)}$, then $Q = Q_p = p_{CO_2}$

### Difference Between Pressures and Concentrations

> $PV = nRT \therefore P = \frac{n}{V}RT = [C]RT$ for all [[ideal-gas]]es
>
> $Q_p = \frac{p^2_{NO_2}}{p^2_{NO}p_{O_2}} = \frac{([NO_2]RT)^2}{([NO]RT)^2([O_2]RT)} = \frac{[NO_2]^2}{[NO]^2[O_2]RT}$
>
> $Q_c = \frac{[NO_2]^2}{[NO]^2[O_2]}$ ($\frac{}{RT}$ had to be ignored)
>
> this means that $Q_p \propto Q_c$.
> therefore, for gases, $Q = Q_p$ and _not_ $Q_c$

let $aA + bB \Leftrightarrow cC + dD$

$Q = Q_p = Q_c(RT)^{\Delta n_{gas}} = Q_c(RT)^{(c + d) - (a + b)}$ (goes for both $Q$ and $K$), where

$Q = Q_p$ is the actual reaction quotient using pressures in $bar$ (since we're working with gases) and $Q_c$ is the reaction quotient using concentrations

$\Delta n_{gas}$ is the change in the number of moles of gas in the reaction, assuming $A, B, C, D$ are gases

## $Q$ and $K$

### Difference between $Q$ and $K$

$Q$ is the reaction quotient. it holds at **any point in the reaction**

$K$ is the equilibrium constant. it is equal to $Q$ when the reaction is at **equilibrium**

$K$ is dependent on temperature

**example with** $N_2O_4 \Leftrightarrow NO_2$

$K = K_p = \frac{p^2_{NO_2}}{p^1_{N_2O_4}}$ where $p$ are the pressures of the gases in $bar$ at **equilibrium**

$K = Q_p = \frac{p^2_{NO_2}}{p^1_{N_2O_4}}$ where $p$ are the pressures of the gases in $bar$ at **any point in the reaction**

### Relationship between $Q$ and $K$

- if $Q < K$, the reactants must decrease and the products must increase
- if $Q > K$, the reactants must increase and the products must decrease
- if $Q = K$, the reaction is at equilibrium and no further net change takes place

where $Q$ is the reaction quotient and $K$ is the equilibrium constant of the reaction

## Properties

### Overall Reactions

_the sum of two or more individual reactions_

$Q_{overall} = Q_1 \times Q_2 \times Q_3 \dotsm Q_n$ (goes for both $Q$ and $K$)

### Multiplication by a Common Factor

_the multiplication of a whole reaction by a factor_

$Q' = Q^n = [\frac{[C]^c[D]^d}{[A]^a[B]^b}]^n$ (goes for both $Q$ and $K$)

since $Q_p \propto Q_c$, then

${Q_p}' = {Q_p}^n = [\frac{p_C^cp_D^d}{p_A^ap_B^b}]^n$ (goes for both $Q$ and $K$)

where $n$ is the common factor

_doubling a reaction squares its equilibrium constant_

### Reversion of Reactions

_switching the reactants and the products_

$Q_{fwd} = \frac{1}{Q_{rev}} \therefore Q_{rev} = \frac{1}{Q_{fwd}}$ (goes for both $Q$ and $K$)
