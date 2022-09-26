# Binary Decoder

_a [[logic circuit]] (or [[boolean]] [[function]]) that converts an $n$-bit binary number to a set of $2[n]$ outputs_

see [[math notation]], [[binary]]

**representation**

as an example, a _3-to-8 binary decoder_ can be represented by the following [[truth table]]:

| Input | Output  |
| ----- | ------- |
| 0     | 0000000 |
| 1     | 0000001 |
| 2     | 0000010 |
| 3     | 0000100 |
| 4     | 0001000 |
| 5     | 0010000 |
| 6     | 0100000 |
| 7     | 1000000 |

or more formally:

| $I_0$ | $I_1$ | $I_2$ | $O_0$ | $O_1$ | $O_2$ | $O_3$ | $O_4$ | $O_5$ | $O_6$ | $O_7$ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| 0     | 0     | 1     | 0     | 1     | 0     | 0     | 0     | 0     | 0     | 0     |
| 0     | 1     | 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     | 0     |
| 0     | 1     | 1     | 0     | 0     | 0     | 1     | 0     | 0     | 0     | 0     |
| 1     | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 0     | 0     | 0     |
| 1     | 0     | 1     | 0     | 0     | 0     | 0     | 0     | 1     | 0     | 0     |
| 1     | 1     | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 0     |
| 1     | 1     | 1     | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 1     |

and by the following [[logic circuit]]:

![[20220427192937.png]]
