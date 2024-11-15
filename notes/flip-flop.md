# Flip-Flop

**see** [[logic gate]], [[latch]], [[logic circuit]], [[math notation]]

[[flip-flop]]s are _edge-triggered_ whereas gated [[latch]]es are _level-triggered_

all [[latch#types]] can be turned into [[flip-flop]]s and all [[flip-flop#types]] can be turned into [[latch]]es

---

# Types

--- <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>

## SR Flip-Flip

_set-reset flip-flop_

**representation** _[[truth table]]_

| **`"CLK"`** | **`S`** | **`R`** | **`Q`** | comment   |
| ----------- | ------- | ------- | ------- | --------- |
| ↑           | **`0`** | **`0`** | **`Q`** | no change |
| ↑           | **`0`** | **`1`** | **`0`** | reset     |
| ↑           | **`1`** | **`0`** | **`1`** | set       |
| ↑           | **`1`** | **`1`** | ×       | undefined |
| not ↑       | ×       | ×       | **`Q`** | no change |

## D Flip-Flop

_data flip-flop_

**representation** _[[truth table]]_

| **`"CLK"`** | **`D`** | **`Q`** | comment   |
| ----------- | ------- | ------- | --------- |
| ↑           | **`0`** | **`0`** | reset     |
| ↑           | **`1`** | **`1`** | set       |
| not ↑       | ×       | **`Q`** | no change |

## JK Flip-Flop

_same as SR flip-flop, but with undefined states removed_

**representation** _[[truth table]]_

| **`"CLK"`** | **`J`** | **`K`** | **`Q`**  | comment   |
| ----------- | ------- | ------- | -------- | --------- |
| ↑           | **`0`** | **`0`** | **`Q`**  | no change |
| ↑           | **`0`** | **`1`** | **`0`**  | reset     |
| ↑           | **`1`** | **`0`** | **`1`**  | set       |
| ↑           | **`1`** | **`1`** | **`+Q`** | toggle    |
| not ↑       | ×       | ×       | **`Q`**  | no change |

## T Flip-Flop

_toggle flip-flop_

**representation** _[[truth table]]_

| **`"CLK"`** | **`T`** | **`Q`**  | comment   |
| ----------- | ------- | -------- | --------- |
| ↑           | **`0`** | **`Q`**  | no change |
| ↑           | **`1`** | **`+Q`** | toggle    |
| not ↑       | ×       | **`Q`**  | no change |
