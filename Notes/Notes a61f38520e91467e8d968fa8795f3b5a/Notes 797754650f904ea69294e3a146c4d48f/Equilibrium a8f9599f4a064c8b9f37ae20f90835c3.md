# Equilibrium

see [Classical Math Notation](../Tags%20b793d46ea133446daa88889450d15033/Classical%20Math%20Notation%20eb53679093ce497baa118d7bfde14d6c.md)

see [Stoichiometry](Stoichiometry%20a398038171b54bd2ab9fe08da84b4c32.md), [Concentration](Concentration%2042c423d2a69d40cb8b8bd2f84797bc3e.md), [Reaction Rate](Reaction%20Rate%2015b549be89df4681b668a5c52d129a36.md)s

all reactions have to be reversible for equilibrium to be reached

at equilibrium, $rate_{forward} = rate_{reverse}$. no net change is observed

$K = \frac{k_{fwd}}{k_{rev}}$ where $K$ is the equilibrium constant (or formally, the *thermodynamic equilibrium constant*)

## Le Châtelier's Principle

> A system at equilibrium will respond to external stress by minimizing the stress. — Rashmi
> 

## Formulas

### General Formula

let $aA + bB \Leftrightarrow cC + dD$

$Q = Q_c = \frac{[C]^c[D]^d}{[A]^a[B]^b}$ or $Q = Q_p = \frac{p_C^cp_D^d}{p_A^ap_B^b}$ for gaseous reactants or products

where $Q$ is the reaction quotient, $p$ are pressures in $bar$ and $[X]$ are molar [Concentration](Concentration%2042c423d2a69d40cb8b8bd2f84797bc3e.md)s

### Heterogeneous Equilibrium

*involving reactants or products in different phases*

> The expressions of $K$ and $Q$ include only species whose concentrations change as the reaction approaches equilibrium
> 

for example, with $CaCO_{3(s)} \Leftrightarrow CaO_{(s)} + CO_{2(g)}$, then $Q = Q_p = p_{CO_2}$

### Difference Between Pressures and Concentrations

> $PV = nRT \therefore P = \frac{n}{V}RT = [C]RT$ for all [Ideal Gas](Ideal%20Gas%205c4f3d38f82547718e4e6cf93752fb9f.md)es
> 
> 
> $Q_p = \frac{p^2_{NO_2}}{p^2_{NO}p_{O_2}} = \frac{([NO_2]RT)^2}{([NO]RT)^2([O_2]RT)} = \frac{[NO_2]^2}{[NO]^2[O_2]RT}$
> 
> $Q_c = \frac{[NO_2]^2}{[NO]^2[O_2]}$ ($\frac{}{RT}$ had to be ignored)
> 
> this means that $Q_p \propto Q_c$.
> therefore, for gases, $Q = Q_p$ and *not* $Q_c$
> 

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

*the sum of two or more individual reactions*

$Q_{overall} = Q_1 \times Q_2 \times Q_3 \dotsm Q_n$ (goes for both $Q$ and $K$)

### Multiplication by a Common Factor

*the multiplication of a whole reaction by a factor*

$Q' = Q^n = [\frac{[C]^c[D]^d}{[A]^a[B]^b}]^n$ (goes for both $Q$ and $K$)

since $Q_p \propto Q_c$, then

${Q_p}' = {Q_p}^n = [\frac{p_C^cp_D^d}{p_A^ap_B^b}]^n$ (goes for both $Q$ and $K$)

where $n$ is the common factor

*doubling a reaction squares its equilibrium constant*

### Reversion of Reactions

*switching the reactants and the products*

$Q_{fwd} = \frac{1}{Q_{rev}} \therefore Q_{rev} = \frac{1}{Q_{fwd}}$ (goes for both $Q$ and $K$)