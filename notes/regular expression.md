# Regular Expression

**aka** _RegEx_, _RegExp_

_a finite [[string]] denoting a [[formal language#regular formal language]]_

&mdash; <https://en.wikipedia.org/wiki/Regular_expression#Formal_language_theory>

&mdash; [[automata-and-formal-languages-cheatsheet.pdf]]

> **resource** LTRE, my [[finite automaton]] [[regular expression]] engine and [[formal language]]s playground &mdash; <https://github.com/Bricktech2000/LTRE>

> **resource** _Regular Expression Matching Can Be Simple And Fast_, an intro to [[finite automaton]] [[regular expression]] engines and a manifesto for why there are no good excuses to use backtracking engines &mdash; <https://swtch.com/~rsc/regexp/regexp1.html>

in [[formal language]] theory, [[regular expression]]s support grouping `(r)`, concatenation `rs`, alternation `r|s` and Kleene closure `r*`; `?` and `+` are omitted since `r? = r|ε` and `r+ = rr*`. additionaly, `ε` denotes the [[set]] containing the empty word, `∅` the empty [[set]], and any other [[character]] the [[set]] containing the word formed by that [[character]]

alternation `|` corresponds to [[set#union]] [[under]] accepted language, so it is only natural to extend [[regular expression]]s with intersection `&` and complementation `~`, which correspond to, respectively, [[set#intersection]] and [[set#complementation]] [[under]] accepted language. this is seldom done in practice, however. one reason may be that alternations are trivial to implement whereas intersections and complements take more work. poor [[generalism]] could also be a contributing factor

**properties** (not exhaustive)

_commutitivity of alternation_ `r|s = s|r`

_associativity of alternation_ `r|s|t = r|(s|t) = (r|s)|t`

_associativity of concatenation_ `rst = (rs)t = r(st)`

_distributivity of concatenation over alternation_ `r(s|t) = rs|rt` and `(s|t)r = sr|tr`

_idempotence of Kleene closure_ `r* = r**`

_Kleene closure of `∅` and `ε`_ `∅* = ε* = ε`

_Kleene closure of `?` and `+`_ `(r|ε)* = (rr*)* = r*`

_Kleene closure of concatenation_ `(r*s*)* = (r|s)*`
