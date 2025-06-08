# Finite Automaton

**aka** _finite state machine_, _FSM_, _finite state automaton_, _FSA_

**see** [[math notation]]

**definition** a _non-deterministic finite automaton_ is a finite [[graph]] whose edges are [[set]]s of _symbols_ representing non-deterministic _state transitions_

an NFA $M$ may be described by a _transition function_ $\delta$ that maps a _current state_ and a _symbol_ to a [[set]] of reachable _next states_

**definition** a _deterministic finite automaton_ is a finite [[graph]] whose edges are single _symbols_ representing deterministic _state transitions_

a DFA $M$ may be described by a _transition function_ $\delta$ that maps a _current state_ and a _symbol_ to a single _next state_

NFAs and NFAs have the same expression power; a DFA can be converted to an NFA trivially, and an NFA can be converted to a DFA using the _powerset construction_, which converts "superpositions" of reachable states in the NFA into single states in the DFA
