# Characteristic Table

for sequential [[logic circuit]]s. see [[excitation table]], [[truth table]]

_circuit inputs and previous state to next state. tells you how the control bits will modify the current state_

&mdash; <https://www.quora.com/What-is-the-difference-between-truth-table-and-characteristic-table-and-excitation-table>

> **example**
>
> | **`P`** | **`N`** | **`Qss t`** |
> | ------- | ------- | ----------- |
> | **`0`** | **`0`** | **`0`**     |
> | **`0`** | **`1`** | **`Q t`**   |
> | **`1`** | **`0`** | **`Q t`**   |
> | **`1`** | **`1`** | **`1`**     |

> **example**
>
> | **`P`** | **`N`** | **`Q t`** | **`Qss t`** |
> | ------- | ------- | --------- | ----------- |
> | **`0`** | **`0`** | **`0`**   | **`0`**     |
> | **`0`** | **`0`** | **`1`**   | **`0`**     |
> | **`0`** | **`1`** | **`0`**   | **`0`**     |
> | **`0`** | **`1`** | **`1`**   | **`1`**     |
> | **`1`** | **`0`** | **`0`**   | **`1`**     |
> | **`1`** | **`0`** | **`1`**   | **`0`**     |
> | **`1`** | **`1`** | **`0`**   | **`1`**     |
> | **`1`** | **`1`** | **`1`**   | **`1`**     |
