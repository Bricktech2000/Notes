# Flip-Flop

**see** [[logic gate]], [[latch]], [[logic circuit]], [[math notation]]

[[flip-flop]]s are _edge-triggered_ whereas gated [[latch]]es are _level-triggered_

all [[latch#types]] can be turned into [[flip-flop]]s and all [[flip-flop#types]] can be turned into [[latch]]es

---

# Types

&mdash; <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>

## SR Flip-Flip

_set-reset flip-flop_

not used as it has an undefined state

## D Flip-Flop

_data flip-flop_

**representation** _[[truth table]]_

| $CLK$          | $D$      | $Q$ | comment    |
| -------------- | -------- | --- | ---------- |
| $\uparrow$     | 0        | 0   | data reset |
| $\uparrow$     | 1        | 1   | data set   |
| not $\uparrow$ | $\times$ | $Q$ | no change  |

## JK Flip-Flop

_same as SR flip-flop, but with undefined states removed_

**representation** _[[truth table]]_

| $CLK$          | $J$      | $K$      | $Q$  | comment   |
| -------------- | -------- | -------- | ---- | --------- |
| $\uparrow$     | 0        | 0        | $Q$  | no change |
| $\uparrow$     | 0        | 1        | 0    | reset     |
| $\uparrow$     | 1        | 0        | 1    | set       |
| $\uparrow$     | 1        | 1        | $+Q$ | toggle    |
| not $\uparrow$ | $\times$ | $\times$ | $Q$  | no change |

## T Flip-Flop

_toggle flip-flop_

**representation** _[[truth table]]_

| $CLK$          | $T$      | $Q$  | comment   |
| -------------- | -------- | ---- | --------- |
| $\uparrow$     | 0        | $Q$  | no change |
| $\uparrow$     | 1        | $+Q$ | toggle    |
| not $\uparrow$ | $\times$ | 0    | no change |
