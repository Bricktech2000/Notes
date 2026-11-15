# Regular Expression

_a finite [[string]] describing a [[formal language#regular formal language]]_

--- <https://en.wikipedia.org/wiki/Regular_expression#Formal_language_theory>

--- [[../references/automata-and-formal-languages-cheatsheet.pdf]]

**see** [[brzozowski derivative]]

> **resource** LTRE, my [[finite automaton]] [[regular expression]] engine and [[formal language]]s playground --- <https://github.com/Bricktech2000/LTRE>

> **resource** CPS-RE, my tiny backtracking [[regular expression]] engine in [[continuation#continuation-passing style]] --- <https://github.com/Bricktech2000/CPS-RE>

> **resource** _Regular Expression Matching Can Be Simple And Fast_ by Russ Cox, an intro to [[finite automaton]] [[regular expression]] engines and a manifesto on why there are no good excuses to use backtracking engines --- [[../references/regexp1.html]] --- <https://swtch.com/~rsc/regexp/regexp1.html>

> **resource** _Regular Expression Matching: the Virtual Machine Approach_ by Russ Cox, notably the discussions on submatch extraction --- [[../references/regexp2.html]] and [[../references/nfa-posix.y.c]] and [[../references/nfa-perl.y.c]] and [[../references/regexp-bytecode.c]] --- <https://swtch.com/~rsc/regexp/regexp2.html> and <https://swtch.com/~rsc/regexp/nfa-posix.y.txt> and <https://swtch.com/~rsc/regexp/nfa-perl.y.txt> and <https://swtch.com/~rsc/regexp/regexp-bytecode.c.txt>

> **resource** _Regular Expression Matching in the Wild_ by Russ Cox, practical tips on writing [[regular expression]] engines --- [[../references/regexp3.html]] and [[../references/dfa0.c]] and [[../references/dfa1.c]] and [[../references/nfa.c]] --- <https://swtch.com/~rsc/regexp/regexp3.html> and <https://swtch.com/~rsc/regexp/dfa0.c.txt> and <https://swtch.com/~rsc/regexp/dfa1.c.txt> and <https://swtch.com/~rsc/regexp/nfa.c.txt>

> **resource** Andrew Gallant's blog posts on `ripgrep`, more practical tips on writing [[regular expression]] engines --- [[../references/ripgrep is faster than {grep, ag, git grep, ucg, pt, sift} - Andrew Gallant's Blog.pdf]] and [[../references/Regex engine internals as a library - Andrew Gallant's Blog.pdf]] --- <https://blog.burntsushi.net/ripgrep/> and <https://blog.burntsushi.net/regex-internals/>

in [[formal language]] theory, [[regular expression]]s support alternation `r|s`, concatenation `rs`, Kleene star `r*` and grouping `(r)`; `?` and `+` are omitted since `r? = r|ε` and `r+ = rr*`. additionaly, `∅` denotes the [[set#empty set]], `ε` the [[set]] containing the empty word, and any other [[character]] the [[set]] containing the word formed by that [[character]]. in truth, grouping `(r)` is redundant and only needed because of [[infix notation]], and the empty [[string]] `ε` and empty [[set]] `∅` are redundant and only needed because the notation can't express the empty concatenation and empty alternation, respectively

[[regular expression]]s are **not** a "notation for describing patterns of text". they are a notation for describing the [[formal language#regular formal language]]s. so many get it wrong; see, for example, _A Regular Expression Matcher. Code by Rob Pike, Exegesis by Brian Kernighan_ --- [[../references/beautiful.html]] --- <https://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html>. as a rule of thumb, if a pragmatic [[regular expression]] engine doesn't support alternation or grouping or backtracking, chances are high it's not a [[regular expression]] engine. sure, it matches patterns of text, but that's not what it means to be a [[regular expression]] engine

there exist several [[algorithm]]s for the determinization of [[regular expression]]s, but they're all kind of the same. Thompson's construction (_Regular Expression Search Algorith_ by Thompson --- [[../references/Thompson-1968.pdf]]) and Aho's "followpos" algorithm (_Principles of Compiler Design_ by Aho and Ullman) both convert [[regular expression]]s to equivalent non-deterministic [[finite acceptor]] [[graph]] intermediate representations. and the powerset construction, the "lock-step" algorithm and the McNaughton--Yamada algorithm (_Regular Expressions and State Graphs for Automata_ by McNaughton and Yamada) are just different takes on computing [[brzozowski derivative]]s (_Derivatives of Regular Expressions_ by Janusz A. Brzozowski --- [[../references/321239.321249.pdf]]) on those non-deterministic intermediate representations. see also <https://youtu.be/tAw9-nTCuzI>, an overview of this all, by Kay Lack

**properties** (not exhaustive or canonical)

_commutitivity of alternation_ `r|s = s|r`

_[[idempotence]] of alternation_ `r|r = r`

_associativity of alternation_ `r|s|t = r|(s|t) = (r|s)|t`

_identity of alternation_ `r|∅ = r`

_annihilation of alternation_ `r|Σ* = Σ*`

_associativity of concatenation_ `rst = (rs)t = r(st)`

_identity of concatenation_ `rε = r`

_annihilation of concatenation_ `r∅ = ∅`

_left distributivity_ `r(s|t) = rs|rt`

_right distributivity_ `(s|t)r = sr|tr`

_[[idempotence]] of Kleene star_ `r* = r**`

_Kleene star of `∅` and `ε`_ `∅* = ε* = ε`

_Kleene star of `?` and `+`_ `(r|ε)* = (rr*)* = r*`

## Extended Regular Expression

the [[formal language#regular formal language]]s are closed under complementation, so it is only natural to extend [[regular expression]]s with a complementation [[operator]] `!r`. this is seldom done in practice, however---and that's a shame, because these [[regular expression#extended regular expression]]s are more natural and more concise, as argued in _Regular Expressions and State Graphs for Automata_ by McNaughton and Yamada (subsection _A Specification Language for Automata_) and in _Regular-expression derivatives reexamined_ by Owens, Reppy and Turon (section 5.1 _Extended Regular Expressions_) and in _RE#: High Performance Derivative-Based Regex Matching_ by Varatalu, Veanes and Ernits (section 2 _Motivating Examples_)

the introduction of complementation induces a set of dual [[operator]]s. the dual of alternation $R \mid S = w.\ w \in R \lor w \in S$ is _intersection_ $R \mathbin\& S = \overline{\overline R \mid \overline S} = w.\ w \in R \land w \in S$, the dual of concatenation $R \cdot S = w.\ \exists rs = w.\ r \in R \land s \in S$ is _dual concatenation_ $R \odot S = \overline{\overline R \cdot \overline S} = w.\ \forall rs = w.\ r \in R \lor s \in S$, and the dual of the Kleene star $R^* = w.\ \exists r_0 \dots r_n = w.\ \forall r_\circ \in R$ is the _dual Kleene star_ $R^\circledast = \overline{\overline R^*} = w.\ \forall r_0 \dots r_n = w.\ \exists r_\circ \in R$ --- _The dual of concatenation_ by Alexander Okhotin --- [[../references/doi_10.1016_j.tcs.2005.07.019.pdf]] --- <https://www.sciencedirect.com/science/article/pii/S0304397505004056>. the suggestive $R \cdot' S = w.\ \exists rs = w.\ r \in R \lor s \in S$ and its dual $\overline{\overline R \cdot' \overline S} = R \odot' S = w.\ \forall rs = w.\ r \in R \land s \in S$ turn out to be uninteresting because their [[quantifier]]s distribute so they simplify to $w.\ (\exists rs = w.\ r \in R) \lor (\exists rs = w.\ s \in S) = R \cdot \overline\varnothing \mid \overline\varnothing \cdot S$ and $w.\ (\forall rs = w.\ r \in R) \land (\forall rs = w.\ s \in S) = R \odot \varnothing \mathbin\& \varnothing \odot S$, respectively. similarly, the suggestive $R^{*'} = w.\ \exists r_0 \dots r_n = w.\ \exists r_\circ \in R$ and its dual $\overline{\overline R^{*'}} = R^{\circledast'} = w.\ \forall r_0 \dots r_n = w.\ \forall r_\circ \in R$ simplify to $w.\ \exists srs' = w.\ r \in R = \overline\varnothing \cdot R \cdot \overline\varnothing$ and $w.\ \forall srs' = w.\ r \in R = \varnothing \odot R \odot \varnothing$, respectively

> **note** an intuition for the dual [[operator]]s is that while concatenation and Kleene star encode "existential valitidy" _if you look at this word right, all of it will be valid_, dual concatenation and dual Kleene star encode "universal invalidity" _no matter how you look at this word, some of it will be invalid_
