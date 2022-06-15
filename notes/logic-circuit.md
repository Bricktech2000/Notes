# Logic Circuit

see [[digital-system]]

see [[truth-table]], [[characteristic-table]], [[excitation-table]], [[characteristic-equation]], [[karnaugh-map]], [[state-table]], [[state-diagram]]

[[logic-circuit]]s are made of logic [[gate]]s.

## types

### Combinational Logic Circuit

_no feedback loops, no clocks_

see [[truth-table]], [[karnaugh-map]]

the outputs of a combinational logic circuit are a [[function]] the inputs, without side effects

### Sequential Logic Circuit

see [[excitation-table]], [[characteristic-table]]

the outputs of a sequential logic circuit can be based on previous inputs and can have side effects on future inputs

## examples

[[latch]]

[[flip-flop]]

[[binary-decoder]]

[[multiplexer]]

## cost of a logic circuit

_for [[iti1100-a-digital-systems-i]]_

see [[math-notation]]

### definition

the cost of a logic circuit can be calculated using its [[disjunctive-normal-form]]

$C f = \sum \text{literals per term} : \text{term count}$ (see [[boolean-operator]])

if a term has $1$ literal, $\sum \text{literals per term} = 0$

if an expression has $1$ term, $\text{term count} = 0$

### examples

$f w x y z = (w \land x \land \lnot y \land z) \lor (w \land x \land y \land \lnot z) \vdash C f = 4 : 4 : 2 = 0$

$h_1 a b = a \land b \vdash C h = 2 : 0 = 2$

$h_2ab = \lnot b \vdash C h = 0 : 0 = 0$

### consequences

NOR and NAND gates are very useful, as they reduce the cost of the logic circuit by reducing the number of ICs necessary to get an identical output (see [[boolean-operator]]s)
