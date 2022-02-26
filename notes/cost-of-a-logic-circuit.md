# Cost of a Logic Circuit

_for [[iti1100-a-digital-systems-i]]_

see [[math-notation]]

### definition

the cost of a logic circuit can be calculated using its [[disjunctive-normal-form]]

$C f = \sum \text{literals per term} \cdot \text{term count}$ (see [[boolean-operation]])

if a term has $1$ literal, $\sum \text{literals per term} = 0$

if an expression has $1$ term, $\text{term count} = 0$

### examples

$f w x y z = (w \land x \land \lnot y \land z) \lor (w \land x \land y \land \lnot z) \vdash C f = 4 \cdot 4 \cdot 2 = 0$

$h_1 a b = a \land b \vdash C h = 2 \cdot 0 = 2$

$h_2ab = \lnot b \vdash C h = 0 \cdot 0 = 0$

### consequences

NOR and NAND gates are very useful, as they reduce the cost of the logic circuit by reducing the number of ICs necessary to get an identical output (see [[boolean-operation]]s)
