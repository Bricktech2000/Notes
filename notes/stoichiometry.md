# Stoichiometry

see [[conventional-math-notation]]

> Stoichiometry refers to the relationship between the quantities of reactants and products before, during, and following chemical reactions &mdash; Wikipedia

_use units to figure out what equations to use_

## example problem 1

![[2022-02-26-01-24-45.png]]

$Q_{water} = m_{water} \rho_{water} c (T_f - T_i)$

_derived from $Q = mc \Delta T$_

![[2022-02-26-01-24-57.png]]

![[2022-02-26-01-25-08.png]]

$m_{iridium} = -Q_{water} / (c (T_f - T_i))$

_derived from $Q = mc \Delta T$_

![[2022-02-26-01-25-19.png]]

![[2022-02-26-01-25-27.png]]

$V = m_{iridium} / \rho_{iridium} / 100$

_the [[volume]] of a [[sphere]] is its [[mass]] divided by its [[density]], divided by 100 [[sphere]]s_

![[2022-02-26-01-25-36.png]]

![[2022-02-26-01-25-43.png]]

$V_{sphere} = \frac{2 \pi (d/2)^3}{3}$

_solve for diameter_

![[2022-02-26-01-25-51.png]]

![[2022-02-26-01-26-00.png]]

$d_{sphere} = 8.45121mm \approx 8.5mm$

## example problem 2

![[2022-02-26-01-26-08.png]]

enthalpy change of a reaction: $\Delta_rH^0$

> pronounced _delta R, H nought_

- find out what reactions to use to go from $CIF_{(g)} + 2F_2$ to $CIF_3$
- multiply reactions by constants to balance everything. note that when multiplying a reaction, $\Delta_rH^0$ also gets multiplied. fractional coefficients are allowed.
- reactions are allowed to be flipped, but doing so also flips the sign of $\Delta_rH^0$
- when done, cancel out molecules that are both in the reactants and in the products. note that the states and coefficients have to match, not only the molecules
  ![[2022-02-26-01-26-21.png]]
- add up all $\Delta_rH^0$ to find the enthalpy change of the original reaction. in this case $\Delta_rH^0 = -135.0 \frac{kJ}{mol}$

## example problem 3

![[2022-02-26-01-26-32.png]]

enthalpy of formation: $\Delta_fH^0$

### find the limiting reagent

- find $n$ for $H_{2(g)}$ and $CO_{(g)}$ using $PV = nRT$
- figure out what is the limiting reagent. in this case, $n_{H_2} = 0.634$ and $n_{CO} = 0.564$, meaning $H_2$ is the limiting reagent

$\begin{matrix}1mol_{CO} &:& 2mol_{H_2} \\\  0.564mol_{CO} &:& n \end{matrix} \therefore n = 1.128mol_{H_2}$ needed, which we do not have

### calculate $\Delta_rH^0$ using enthalpies of formation

- get the equation for $\Delta_rH^0$
  $\Delta_rH^0 = [(1)\Delta_fH^0_{CH_3OH_{(l)}}] - [(1)\Delta_fH^0_{CO_{(g)}} + (2)\Delta_fH^0_{H_{2(g)}}]$
- look up enthalpies of formation of the reactants and products
  $\Delta_fH^0_{H_{2(g)}} = 0 \frac{kJ}{mol}$
  $\Delta_fH^0_{CH_3OH_{(l)}} = -238.6 \frac{kJ}{mol}$
  $\Delta_fH^0_{CO{(g)}} = -110.5 \frac{kJ}{mol}$
- calculate $\Delta_r H^0$
  $\Delta_rH^0 = [-238.6 \frac{kJ}{mol}] - [-110.5 \frac{kJ}{mol}] = -128.1 \frac{kJ}{mol}$
  a negative $\Delta_r H^0$ means the reaction is exothermic

### calculate the amount of energy released

- we know $H_{2(g)}$ is the limiting reagent
- calculate the amount of energy released

$\begin{matrix} 2mol_{H_2} &:& -128.1 \frac{kJ}{mol} \\\  0.634mol_{H_2} &:& Q\end{matrix} \therefore Q = -40.6kJ$

a negative $Q$ means the reaction is exothermic, hence $40.6kJ$ of heat are released

## example problem 4

![[2022-02-26-01-26-59.png]]

## write down the reaction

$H_2SO_{4(aq)} + 2KOH_{(aq)} \to K_2SO_{4(aq)} + 2H_2O_{(l)}$

### find the limiting reagent

- find $n$ for $H_2SO_{4(aq)}$. in this case $25.0mL * 0.500 \frac{mol}{L} = 1.25 \times 10^{-2}mol$
- find $n$ for $KOH_{(aq)}$. in this case $25.0mL * 1.00 \frac{mol}{L} = 2.50 \times 10^{-2}mol$
- in this case, there is no limiting reagent

### find $Q_{reaction}$

$Q_{reaction} + Q_{contents} + Q_{calorimeter} = 0$

since there is no information about it, assume $Q_{calorimeter} = 0$

$Q_{reaction} = - Q_{contents}$

$Q_{reaction} = (mc\Delta T)_{contents}$

$Q_{reaction} = (2\frac{n_{H_2SO_{4(aq)}}}{MM_{H_2SO_{4(aq)}}} + 2\frac{n_{KOH{(aq)}}}{MM_{KOH{(aq)}}}) \times 4.184 \frac{J}{g^\cdot C} \times (T_f - T_i)$

$Q_{reaction} = (\frac{1.25 \times 10^{-2}mol}{2 \times 1.00784 \frac{g}{mol} + 1 \times 32.065 \frac{g}{mol} + 4 \times 15.999 \frac{g}{mol}} + 2 \frac{2.50 \times 10^{-2}mol}{1 \times 39.0983 \frac{g}{mol} + 1 \times 15.999 \frac{g}{mol} + 1 \times 1.00784 \frac{g}{mol}}) \times 4.184 \frac{J}{g^\cdot C} \times (30.17^\cdot C - 23.50^\cdot C)$

$Q_{reaction} = -1.40 \times 10^3J$ (I believe, see screenshots below)

## find enthalpy of neutralization

$\Delta H^0 = \frac{Q}{n_{H^+}} = \frac{-1.40 \times 10^3J}{2.5 \times 10^{-2}mol} = -55.8\frac{kJ}{mol_{H^+}}$

---

we will finish the question in the next DGD

![[2022-02-26-01-28-15.png]]

$Q_{reaction} = - Q_{contents} \\\  Q_{reaction} = (mc\Delta T)_{contents} \\\  Q_{reaction} = (\frac{n_{H_2SO_{4(aq)}}}{MM_{H_2SO_{4(aq)}}} + 2\frac{n_{KOH{(aq)}}}{MM_{KOH{(aq)}}}) \times 4.184 \frac{J}{g^\cdot C} \times (T_f - T_i) \\\  Q_{reaction} = (\frac{1.25 \times 10^{-2}mol}{2 \times 1.00784 \frac{g}{mol} + 1 \times 32.065 \frac{g}{mol} + 4 \times 15.999 \frac{g}{mol}} + 2 \frac{2.50 \times 10^{-2}mol}{1 \times 39.0983 \frac{g}{mol} + 1 \times 15.999 \frac{g}{mol} + 1 \times 1.00784 \frac{g}{mol}}) \times 4.184 \frac{J}{g^\cdot C} \times (30.17^\cdot C - 23.50^\cdot C)$

![[2022-02-26-01-28-28.png]]
