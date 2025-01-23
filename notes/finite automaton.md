# Finite Automaton

**aka** _finite state machine_, _FSM_, _finite state automaton_, _FSA_

**see** [[math notation]], [[state table]], [[state diagram]]

**definition** a _finite automaton_ is a finite [[graph]] whose edges are [[set]]s of _symbols_ representing possible _state transitions_. **`M S T s`** represents whether automaton **`M`** can transition from state **`S`** to state **`T`** given symbol **`s`**

[[finite automaton#deterministic finite automaton]]s and [[finite automaton#non-deterministic finite automaton]]a have the same expression power; a DFA can be converted to an NFA trivially and an NFA can be converted to a DFA using the _powerset construction_, which converts "superpositions" of reachable states in the NFA into single states in the DFA

## Deterministic Finite Automaton

**aka** _DFA_, _DFSM_

**definition** a _deterministic finite automaton_ is a [[finite automaton]] **`M`** such that **`/\ S. /\ s. (# T. M S T s = 1)`**

a DFA **`M`** may be described by a _transition function_ **`dd S s = T == M S T s`**

## Non-Deterministic Finite Automaton

**aka** _NFA_, _NFSM_

**definition** a _non-deterministic finite automaton_ is a [[finite automaton]] **`M`** such that **`\/ S. \/ s. (# T. M S T s + 1)`**

an NFA **`M`** may be described by a _transition function_ **`dd S s == T. M S T s`**; we find that **`dd == rrM`**
