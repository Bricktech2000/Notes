# Latch

**see** [[flip-flop]], [[logic circuit]]

all [[latch#types]] can be turned into [[flip-flop]]s and all [[flip-flop#types]] can be turned into [[latch]]es

## Gated Latch

gated [[latch]]es are _level-triggered_ whereas [[flip-flop]]s are _edge-triggered_

all [[latch]]es can be converted to gated [[latch]]es with an _enable_ input

---

# Types

--- <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>

[[logic circuit]] diagrams --- <https://www.javatpoint.com/latches-in-digital-electronics>

## SR Latch

_set-reset latch_

**representation** _[[truth table]]_

| $S$ | $R$ | $Q$ | comment   |
| --- | --- | --- | --------- |
| $0$ | $0$ | $Q$ | no change |
| $0$ | $1$ | $0$ | reset     |
| $1$ | $0$ | $1$ | set       |
| $1$ | $1$ | --- | undefined |

## D Latch

_data latch, gated by default_

**representation** _[[truth table]]_

| $E$ | $D$ | $Q$ | comment    |
| --- | --- | --- | ---------- |
| $0$ | --- | $Q$ | no change  |
| $1$ | $0$ | $0$ | data reset |
| $1$ | $1$ | $1$ | data set   |

## JK Latch

_same as SR latch, but with undefined states removed_

**representation** _[[truth table]]_

| $J$ | $K$ | $Q$       | comment   |
| --- | --- | --------- | --------- |
| $0$ | $0$ | $Q$       | no change |
| $0$ | $1$ | $0$       | reset     |
| $1$ | $0$ | $1$       | set       |
| $1$ | $1$ | $\lnot Q$ | toggle    |

## T Latch

_toggle latch_

not used as its only state would be undefined
