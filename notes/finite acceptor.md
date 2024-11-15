# Finite Acceptor

_a [[finite automaton]] which recognizes a [[formal language#regular formal language]]_

**aka** _finite automaton, FA_

**see** [[formal language]]

**definition** a _finite acceptor_ is a [[finite automaton]] equipped with an _initial state_ and a [[set]] of _final states_ which recognizes a [[formal language]]

**definition** a word is _recognized_ or _accepted_ by a finite acceptor if and only if there exists a path corresponding to the sequence of symbols forming the word from the _initial state_ to a _final state_; otherwise, the word is _rejected_

**definition** the _language recognized_ or _language accepted_ by a finite acceptor is the [[set]] of all words recognized by the acceptor

**notation** _the language recognized by a finite acceptor $M$_ $L(M)$

an _ε-NFA_ is a finite acceptor containing transitions which consume no input, termed _ε-transitions_. such finite acceptors are considered non-deterministic, even though their _ε-closure_ may be deterministic

a _generalized NFA_ or _GNFA_ is a finite acceptor whose transitions are labeled with [[regular expression]]s instead of symbols

**examples**

> **example**
>
> the following (deterministic) finite acceptor recognizes the language given by the [[regular expression]] `/1[10]*0/`
>
> ```mermaid
> graph LR
>  I( ) --> A --1--> B
>  C --> F( )
>  C & B --1--> B
>  B & C --0--> C
>  A --0--> D --1--> D --0--> D
> ```

**definition** a deterministic [[finite acceptor]] is called _minimal_ if it has the minimum number of states needed to recognize its language --- <https://en.wikipedia.org/wiki/DFA_minimization>

_minimization_ is performed by merging _indistinguishable_ states --- <https://www.youtube.com/watch?v=7W2lSrt8r-0>. a pair of states is indistinguishable if and only if they are either both or neither final and their transitions are equal up to target state indistinguishability. minimal deterministic finite acceptors are unique up to state renumbering
