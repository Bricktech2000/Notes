# Regular Expression

**aka** _RegEx_, _RegExp_

_a finite [[string]] denoting a [[formal language#regular formal language]]_

--- <https://en.wikipedia.org/wiki/Regular_expression#Formal_language_theory>

--- [[automata-and-formal-languages-cheatsheet.pdf]]

**see** [[brzozowski derivative]]

> **resource** LTRE, my [[finite automaton]] [[regular expression]] engine and [[formal language]]s playground --- <https://github.com/Bricktech2000/LTRE>

> **resource** CPS-RE, my tiny backtracking [[regular expression]] engine in continuation-passing style --- <https://github.com/Bricktech2000/CPS-RE>

> **resource** _Regular Expression Matching Can Be Simple And Fast_ by Russ Cox, an intro to [[finite automaton]] [[regular expression]] engines and a manifesto for why there are no good excuses to use backtracking engines --- <https://swtch.com/~rsc/regexp/regexp1.html>

> **resource** _Regular Expression Matching in the Wild_ by Russ Cox, practical tips for writing [[regular expression]] engines --- <https://swtch.com/~rsc/regexp/regexp3.html>

> **resource** Andrew Gallant's blog posts on `ripgrep`, more practical tips for writing [[regular expression]] engines --- <https://blog.burntsushi.net/ripgrep/> and <https://blog.burntsushi.net/regex-internals/>

in [[formal language]] theory, [[regular expression]]s support concatenation `rs`, alternation `r|s`, Kleene star `r*` and grouping `(r)`; `?` and `+` are omitted since `r? = r|ε` and `r+ = rr*`. additionaly, `ε` denotes the [[set]] containing the empty word, `∅` the empty [[set]], and any other [[character]] the [[set]] containing the word formed by that [[character]]. in truth, grouping `(r)` is redundant and only needed because of [[infix notation]], and the empty [[string]] `ε` and empty [[set]] `∅` are redundant and only needed because the notation can't express the empty concatenation and empty alternation, respectively

[[regular expression]]s are **not** a "notation for describing patterns of text". they are a notation for describing the [[formal language#regular formal language]]s. so many get it wrong; see, for example, _A Regular Expression Matcher. Code by Rob Pike, Exegesis by Brian Kernighan_ --- <https://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html>. as a rule of thumb, if a [[regular expression]] engine doesn't support alternation or grouping or backtracking, chances are high it's not a [[regular expression]] engine. sure, it matches patterns of text, but that's not what it means to be a [[regular expression]] engine

alternation `|` corresponds to [[set#union]] [[under]] accepted language, so it is only natural to extend [[regular expression]]s with intersection `&` and complementation `~`, which correspond to, respectively, [[set#intersection]] and [[set#complementation]] [[under]] accepted language. this is seldom done in practice, however---and that's a shame, because these extended [[regular expression]]s are more natural and more concise, as argued in _Regular Expressions and State Graphs for Automata_ by McNaughton and Yamada (subsection _A Specification Language for Automata_) and in _Regular-expression derivatives reexamined_ by Owens, Reppy and Turon (section 5.1 _Extended Regular Expressions_)

there exist several [[algorithm]]s for the determinization of [[regular expression]]s, but they're all kind of the same. Thompson's construction (_Regular Expression Search Algorith_ by Thompson) and Aho's "followpos" algorithm (_Principles of Compiler Design_ by Aho and Ullman) both convert [[regular expression]]s to equivalent non-deterministic [[finite acceptor]] [[graph]] intermediate representations. and the powerset construction, "lock-step" algorithm and McNaughton--Yamada algorithm (_Regular Expressions and State Graphs for Automata_ by McNaughton and Yamada) are just different takes on computing [[brzozowski derivative]]s (_Derivatives of Regular Expressions_ by Janusz A. Brzozowski) on those non-deterministic intermediate representations. see also <https://youtu.be/tAw9-nTCuzI>, an overview of this all, by Kay Lack

**properties** (not canonical)

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
