# Latch

see [[gate]], [[flip-flop]], [[logic-circuit]]

all [[latch]]es can be turned into [[flip-flop]]s and all [[flip-flop]]s can be turned into [[latch]]es

## Gated Latch

gated [[latch]]es are _level-triggered_ whereas [[flip-flop]]s are _edge-triggered_

all [[latch]]es can be converted to gated [[latch]]es with an _enable_ input

## types of latches

&mdash; <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>

circuit diagrams &mdash; <https://www.javatpoint.com/latches-in-digital-electronics>

### SR Latch

_set-reset latch_

| $S$ | $R$ | $Q$      | comment   |
| --- | --- | -------- | --------- |
| 0   | 0   | $Q$      | no change |
| 0   | 1   | 0        | reset     |
| 1   | 0   | 1        | set       |
| 1   | 1   | $\times$ | undefined |

![](20220427161726.png)

**note**: can also be built using NAND [[gate]]s

### D Latch

_data latch, gated by default_

| $E$ | $D$ | $Q$ | comment    |
| --- | --- | --- | ---------- |
| 0   | 0   | $Q$ | no change  |
| 0   | 1   | $Q$ | no change  |
| 1   | 0   | 0   | data reset |
| 1   | 1   | 1   | data set   |

![](20220427161914.png)

### JK Latch

_same as SR [[latch]], but with undefined states removed_

| $J$ | $K$ | $Q$       | comment   |
| --- | --- | --------- | --------- |
| 0   | 0   | $Q$       | no change |
| 0   | 1   | 0         | reset     |
| 1   | 0   | 1         | set       |
| 1   | 1   | $\lnot Q$ | toggle    |

![](20220427162006.png)

### T Latch

_toggle latch_

not used as its only state would be undefined
