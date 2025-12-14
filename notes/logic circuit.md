# Logic Circuit

**see** [[digital system]], [[boolean algebra]]

**see** [[truth table]], [[characteristic table]], [[excitation table]], [[karnaugh map]]

**see** [[latch]], [[flip-flop]]

**definition** _combinational logic circuits_ are [[pure]]. they can be represented by [[truth table]]s and [[karnaugh map]]s

**definition** _sequential logic circuits_ are im[[pure]]. they can be represented by [[characteristic table]]s and [[excitation table]]s

sequential [[logic circuit]]s can be modeled as combinational [[logic circuit]]s with feedback:

![[3-s2.0-B9780340645703500071-f05-01-9780340645703.gif]] --- <https://www.sciencedirect.com/topics/engineering/combinatorial-circuits>

memory is typically only a handful of bits. deterministic [[finite automaton]]a (Mealy machines, Moore machines) can be compiled to sequential circuits via _state assignment_: each [[finite automaton]] state is mapped onto a state of memory. the combinational logic tends to simplify better when [[finite automaton]] states that have similar outputs and similar transitions are mapped onto _close_ states of memory---_close_ as measured by Hamming distance, that is, states of memory that form valid minterm rectangles in a [[karnaugh map]]

#todo CEG 3155 (lecs 14--15) : the "memory" in an asynchronous circuit is just a wire; in a synchronous logic circuit it is [[flip-flop]]s: ![[3-s2.0-B9780340645703500071-f05-03-9780340645703.gif]] --- ibid.

#xxx also need to avoid two outputs changing at the same time, in case we end up feeding the outputs to another async circuit

#xxx may need "ready" signals / handshaking. if one async circuit transitions 01->00->10 at gate delay speed, may cause issues downstream if something takes a few gate delays to process its new input

#xxx state reduction is different from [[finite acceptor]]s because we have don't cares.
