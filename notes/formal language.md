# Formal Language

**see** [[finite acceptor]], [[regular expression]], [[math notation]], [[conventional math notation]]

**definition** a _formal language_ is a [[set]] $L$ of finite [[string]]s (_words_) over a finite [[set]] (_alphabet_) of [[character]]s (_symbols_)

**notation** _alphabet_ typically one of $\Sigma$, $\Gamma$

**notation** _language_ typically one of $L$, $M$, $N$

**notation** _word_ typically one of $w$, $u$, $v$

**definition** the _Kleene closure_ $L^*$ of a [[formal language]] $L$ is the [[monoid#free monoid]] on $L$

**definition** the _Kleene plus_ $L^+$ of a [[formal language]] $L$ is the [[semigroup#free semigroup]] on $L$

the complement of a [[formal language]] is with respect to the Kleene closure of its alphabet; that is, $\overline L = \Sigma^* \setminus L$. the union of two [[formal language]]s is a [[set#union]], their intersection is a [[set#intersection]], their difference is a [[set#difference]], and their concatenation is their [[string#concatenation]]-[[outer product]]s

**definition** the _empty word_ is the word $w$ with $|w| = 0$

**notation** _empty word_ typically one of $e$, $\epsilon$, $\lambda$, $\Lambda$

**notation** _word length_ $|w|$, see [[string#length]]

**notation** _concatenation_ typically one of $uv$, $u \cdot v$, $u \circ v$, see [[string#concatenation]]

**notation** _alternation_ typically one of $u \mid v$, $u + v$, $u \cup v$, see [[set#union]]

**notation** _repeated concatenation_ $w^n$

## Regular Formal Language

**definition** a [[formal language]] is _regular_ if and only if it can be described by a [[finite acceptor]]

the [[set]] of regular languages is closed under Kleene closure, Kleene plus, [[set#complementation]], [[set#union]], [[set#intersection]], [[set#difference]], concatenation and reversal

**theorem** _Kleene's theorem_ [[finite acceptor]]s, [[regular expression]]s and [[formal language#regular grammar]]s have the same expression power

> **procedure** _conversions for Kleene's theorem_
>
> ![[lec27-overview.svg]] --- <https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec27-kleene.html>

**theorem** any finite language is regular

> **proof** a finite language can be described by a [[regular expression]] as the alternation of all its words

**theorem** _pumping lemma for regular languages_ **`/\ "regular" -| L. \/ p. /\ w. (L w /\ #w ee |- p < \/ x. \/ y. \/ z. (w = xyz /\ #xy ee -| p /\ #y ee + 0 /\ /\ NN -| n. L x{y}nz))`** #xxx in my [[math notation]], would have to define a [[formal language]] as a [[set]] of [[function]]s so [[composition]] corresponds to [[string#concatenation]]

**theorem** _pumping lemma for regular languages_ for any regular language $L$, there exists a $p$ such that any word $w \in L$ with $|w| \geq p$ can be split into three parts $w = xyz$ such that $|xy| \leq p$ and $|y| \ne 0$ and $xy^nz \in L$ for all $n \in \mathbb N$

> **note** intuitively, the pumping lemma states that all sufficiently long words of a regular language may be "pumped" (there exists a [[substring]] that, when repeated any number of times, produces another word in the language)

> **example** the [[set]] of all [[string]]s of [[prime]] [[string#length]] is not a [[formal language#regular formal language]] --- me
>
> > **proof** by the pumping lemma, the [[string#length]] of pumped words is a [[sequence#arithmetic sequence]] **`n. #w{y}n ee = n. (#w ee) : n(#y ee)`**, which, since **`#y ee + 0`**, will always hit a non-[[prime]], namely, at **`n = #w ee`** --- me

## Non-Regular Language

**definition** a [[formal language]] is _non-regular_ if and only if it cannot be described by a [[finite acceptor]]

#todo complete #xxx not actually a thing --- <https://en.wikipedia.org/wiki/Theory_of_computation#Automata_theory>

## Regular Grammar

#todo complete #xxx create `formal grammar` note instead?

---

a [[formal language]] may be described inductively by a _formal grammar_ (a collection of production rules) over an alphabet

---

#todo

> Just like the automata, a grammar is a formalism used for specifying languages. Each grammar corresponds to a type of machine or automaton:
>
> - Regular grammars ≡ finite state automata
> - Context-free grammars ≡ pushdown automata
> - Grammars without restrictions ≡ Turing machines

#todo currently on 2.4 Grammars

#todo currently on Chapter 12:

> The resultant tree is called the total language tree of the CFG.

> A CFG is called ambiguous if for at least one word in the language that it
> generates, there are two possible derivations of the word that correspond
> to different syntax trees. If a CFG is not ambiguous, it is called
> unambiguous.

link with [[prefix notation]], [[postfix notation]], [[syntax tree]]

#xxx useful table <https://en.wikipedia.org/wiki/Theory_of_computation#Automata_theory>

"meta-rules" for regular/context-free/context-sensitive grammars: <https://youtu.be/ENKT0Z3gldE?t=408>

## ---

--- <https://en.wikipedia.org/wiki/Kleene_star>

--- <https://en.wikipedia.org/wiki/Formal_language>

--- [[automata-and-formal-languages-cheatsheet.pdf]]

--- <https://en.wikipedia.org/wiki/Deterministic_finite_automaton>

--- [[CSI3104A_Introduction_to_Formal_Languages_LEC_20241_-_3152024_-_502_PM_1.zip]]
