# Generalism

_striving to become a jack of all trades_

**see** [[encapsulation]], [[durability]], [[conceptual note-taking]], [[knowledge]]

_specialists_ may come off as clueless, ignorant, blind or unaware. specialism results in compartmentalization of [[knowledge]] and hinders serendipitous discovery. _generalists_, on the other hand, are living swiss army knives. [[generalism]] results in broader [[knowledge]] bases and encourages cross-disciplinary insight

[[generalism]] boils down to broad yet shallow just-in-case learning. _cutting a tree with a chain saw is more efficient than with a swiss army knife---but owning a swiss army knife helps you realize that cutting a tree is a thing you can actually do_

> **examples** _issue --- with rationale_
>
> - [[database]]s all have their own great way of storing and querying data, whether it'd be relational or graph or document or whatever. but most can't even represent [[type#sum type]]s without requiring contortions! --- [[database]]s are designed by [[software engineering]] people, not by [[mathematics]] people
> - HDLs probably shouldn't be DSLs. feels like everything is awkward in HDLs, **including** hardware description. why aren't HDLs just libraries? HDLs have crappy [[c#preprocessor]]-like templating syntax. why not use a neat general-purpose [[turing complete]] [[programming language]] for templating instead? feels like HDLs are reinventing the wheel. instead of starting from a general-purpose language and specializing it, people start from a domain-specific language and awkwardly attempt to extend it. that's how [[bash]] became [[bash]] and [[c++]] became [[c++]] --- it's likely [[computer engineering]] people and [[computer science]] people don't often collaborate
> - from what I understand [[economics]] people perform [[discounted cash flow]] analyses manually in huge tables. that's insane. the other day I realized [[discounted cash flow]] analyses could be modeled using [[calculus]]; some elementary algebra later, I was left with a trivial closed-form equation --- most [[economics]] people probably haven't received formal training in [[mathematics]]
> - _it was a very interesting conference: I'm still deeply ashamed by the presentation I gave, but I remember fondly the time an audience member asked the [[go]] team "why did you choose to ignore any research about [[type system]]s since the 1970s"? I didn't fully understand the implications at the time, but I sure do now._ --- <https://fasterthanli.me/articles/lies-we-tell-ourselves-to-keep-using-golang#the-author-is-a-platypus>
> - YARA strings are [[regular expression]]s under a load of cruft that doesn't even affect expression power, and YARA conditions are [[boolean algebra]] under a load of cruft that tries to make trivial use-cases nicer --- cybersecurity people probably don't have a strong background in [[mathematics]]. --- <https://yara.readthedocs.io/en/latest/writingrules.html#strings> and <https://yara.readthedocs.io/en/latest/writingrules.html#conditions>
