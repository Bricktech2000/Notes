# Vim

<?
see [[public speaking]]

prep:
- open new VSCode window
- turn on screen cast mode
- open MosaicLarge in window
- open [[vim talk demo]] in window
- zoom in 3x
?>

---

# Background

<?
a set of key bindings?
efficient
?>

---

# Modes

<br />

<?
I and ESC
?>

```mermaid
graph TD

N(Normal)

I(Insert)
C(Command)
V(Visual)

N --- I
N --- V
N --- C
```

---

## Normal Mode

---

## Normal Mode

#### Motion Commands

<br />

|                        |              |
| ---------------------- | ------------ |
| _h_ _j_ _k_ _l_ &emsp; | (arrow keys) |
| _w_                    | word         |
| \_                     | line         |

<?
USE NUMBERS
?>

---

## Normal Mode

#### Verb Commands

<br />

|              |             |
| ------------ | ----------- |
| **d** &emsp; | delete      |
| **y**        | yank (copy) |
| **p**        | paste       |

<?
nothing happened...
?>

---

## Normal Mode

#### Phrases

<br />

|                  |                  |
| ---------------- | ---------------- |
| **d**_w_         | delete word      |
| **y**2*w* &emsp; | yank two words   |
| **y**\_          | yank line        |
| **d**2\_         | delete two lines |
| &hellip;         | &hellip;         |

<?
easy to remember, switch keyboard layouts
?>

---

# Demo

---

<?
learn Vim!
disadvantage: frustrating
?>
