# Flip-Flop

**see** [[latch]], [[logic circuit]]

[[flip-flop]]s are _edge-triggered_ whereas gated [[latch]]es are _level-triggered_

all [[latch#types]] can be turned into [[flip-flop]]s and all [[flip-flop#types]] can be turned into [[latch]]es

---

# Types

--- <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>

## SR Flip-Flip

_set-reset flip-flop_

**representation** _[[truth table]]_

| $\mathrm{CLK}$ | $S$ | $R$ | $Q$ | comment   |
| -------------- | --- | --- | --- | --------- |
| rising         | $0$ | $0$ | $Q$ | no change |
| rising         | $0$ | $1$ | $0$ | reset     |
| rising         | $1$ | $0$ | $1$ | set       |
| rising         | $1$ | $1$ | --- | undefined |
| not rising     | --- | --- | $Q$ | no change |

## D Flip-Flop

_data flip-flop_

**representation** _[[truth table]]_

| $\mathrm{CLK}$ | $D$ | $Q$ | comment   |
| -------------- | --- | --- | --------- |
| rising         | $0$ | $0$ | reset     |
| rising         | $1$ | $1$ | set       |
| not rising     | --- | $Q$ | no change |

## JK Flip-Flop

_same as SR flip-flop, but with undefined states removed_

**representation** _[[truth table]]_

| $\mathrm{CLK}$ | $J$ | $K$ | $Q$       | comment   |
| -------------- | --- | --- | --------- | --------- |
| rising         | $0$ | $0$ | $Q$       | no change |
| rising         | $0$ | $1$ | $0$       | reset     |
| rising         | $1$ | $0$ | $1$       | set       |
| rising         | $1$ | $1$ | $\lnot Q$ | toggle    |
| not rising     | --- | --- | $Q$       | no change |

## T Flip-Flop

_toggle flip-flop_

**representation** _[[truth table]]_

| $\mathrm{CLK}$ | $T$ | $Q$       | comment   |
| -------------- | --- | --------- | --------- |
| rising         | $0$ | $Q$       | no change |
| rising         | $1$ | $\lnot Q$ | toggle    |
| not rising     | --- | $Q$       | no change |
