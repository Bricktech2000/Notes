# Make

_POSIX `make`_

> **resource** `make`, POSIX.1-2017 --- [[make.html]] --- <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/make.html>

> **reosurce** _A Tutorial on Portable Makefiles_ by Chris Wellons, on adhering to POSIX [[make]] --- [[A Tutorial on Portable Makefiles.pdf]] --- <https://nullprogram.com/blog/2017/08/20/>

if the first non-comment line is not the _special target_ `.POSIX`, the behavior is unspecified. make has _built-in rules_, which can be disabled by supplying a rule for the _special target_ `.SUFFIXES` with no prerequisites. when there are no rules to build a target, the _special target_ `.DEFAULT` is invoked. targets names matching `\.[A-Z]+` are reserved.

`#` introduces a comment to the end of the line. not supported in _command lines_, but shells tend to use `#` comments so it might work anyway

target names consist of `[._0-9a-zA-Z]+`; notably, an implementation need not support target names containing `/` characters

newlines can be escaped with `\` and they get replaced `s/\\\n\s*/ /`, except in a _command line_, where they get replaced `s/\\\n\t?/\\\n/`

_command lines_ are indented with a tab, not spaces. each is executed in its own shell so a `cd` only applies to the current line. after the tab there can be any number of:

- `-` --- ignore any errors executing the commad, like `.IGNORE`
- `@` --- don't print the command before executing it, like `.SILENT`
- `+` --- also execute the command in dry runs

_`include` path_ behaves like [[c#c preprocessor]] `#include`. _path_ can't contain blanks

_name `=` value_ defines a macro: thereafter _`$(`name`)`_ and _`${`name`}`_ both expand to _value_, and _`$(`name`:`suffix`=`substitute`)`_ and _`${`name`:`suffix`=`substitute`}`_ both expand to _`s/`suffix`\b/`substitute`/g`_ on _value_. the parentheses or braces may be omitted when their contents have length one. the name of the macro being invoked cannot depend on other macro invocations. macro expansion is lazy: after `MACRO = 1` then `REF = $(MACRO)` then `MACRO = 2`, `$(REF)` expands to `2`. _The macro `$$` shall be replaced by the single charater '\$'_ and only God would know whether `$($)` and `${$}` expand to '\$' as well.

there are five _internal macros_, `$< $* $@ $? $%`, and two sets of alternative forms, `$(<F) $(*F) $(@F) $(?F) $(%F)` to extract the filename parts and `$(<D) $(*D) $(@D) $(?D) $(%D)` to extract the directory parts (plus the equivalent `${<F} ${*F} ${@F} ${?F} ${%F}` and `${<D} ${*D} ${@D} ${?D} ${%D}`). careful, some work in _inference rules_ but not in _target rules_, and some only work for _archive library targets_ `lib(member.o)`

an _inference rule_---not to be confused with an [[inference rule]]---is a rule whose target part is of the form _`.`o_ or _`.`c`.`o_, where _`.`c_ (if present) and _`.`o_ are included as prerequisites of the _special target_ `.SUFFIXES`. it describes how to build any file with extension _`.`o_ from a corresponding file with extension _`.`c_ (if present, else without extension) in the same directory

## whining

_Target rules are formatted as follows: `target [target...]: [prerequisite...][;command]<newline>[<tab>command<tab>command...]<newline>line that does not begin with <tab>`_. so a rule must contain either zero or at least two _command lines_, all of which must be on the same line

_There are two kinds of rules: inference rules and target rules. [...] If a rule is defined more than once, the value of the rule shall be that of the last one specified._ so later rules overwrite earlier rules. _A target that has prerequisites, but does not have any commands, can be used to add to the prerequisite list for that target. Only one target rule for any given target can contain commands._ so later rules don't actually overwrite earlier rules. _Inference rules can be redefined. A target that matches an existing inference rule shall overwrite the old inference rule._ so later rules do sometimes overwrite earlier rules. (the wording is confusing here, what they mean is that overwriting happens when the target parts of the inference rules are the same)

_The five internal macros are --- `$@`: The `$@` [macro] shall evaluate to the full target name of the current target, or the archive filename part of a library archive target. [...] `$%`: The `$%` macro shall be evaluated only when the current target is an archive library member [...]. `$?`: The `$?` macro shall evaluate to the list of prerequisites that are newer than the current target. [...] `$<`: In an inference rule, the `$<` macro shall evaluate to [...]. `$*`: The `$*` macro shall evaluate to the current target name with its suffix deleted. [...] Each of the internal macros has an alternative form. When an uppercase 'D' or 'F' is appended to any of the macros, the meaning shall be changed to the directory part for 'D' and filename part for 'F'._ if we're calling `$?` a macro, then appending `D` to the macro gives us `$?D`. turns out that's not what they meant, because later in that paragraph they talk about the macro `$(?D)`. so sloppy

_For the target `lib(member.o)` and the `s2.a` rule, the internal macros shall be defined as: `$<` = `member.s2`, `$*` = `member`, `$@` = `lib`, `$?` = `member.s2`, `$%` = `member.o`._ lmao, they meant to say _the `.s2.a` rule_. the rule `s2.a` wouldn't match `lib(member.o)`
