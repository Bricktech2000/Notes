# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[muscle memory]], [[undo tree]]

> **resource** [[vim]] bindings cheat sheet --- [[YLInLlY.png]] --- <https://i.imgur.com/YLInLlY.png>

> **resource** `:h quickref`, specifically the key bindings --- <https://vimdoc.sourceforge.net/htmldoc/quickref.html>

> **resource** `:h registers`, good reference on registers --- <https://vimdoc.sourceforge.net/htmldoc/change.html#registers>

> **resource** `:h help-summary`, on using `:help` effectively --- <https://vimdoc.sourceforge.net/htmldoc/usr_02.html#help-summary>

some useful bindings not present in the quickref:

- `g+` - `g-` --- go to newer/older text state in the [[undo tree]]
- `:u!<cr>` --- undo one change and remove it from the [[undo tree]]
- `:undol<cr>` --- list all leafs in the [[undo tree]]
- `Q` --- replay last recorded macro (Neovim only)
- `q:` - `q/` --- open the command-line window
- `@:` --- repeat the last command-line
- `gi` --- resume **insert** at the position the last insert was stopped
- i`<c-e>` --- abort an autocompletion (see `:h ins-compl`)
- `gF` --- edit the **file** under the cursor at the line specified
- `<c-w>gF` --- edit in a new window the **file** under the cursor at the line specified
- `gx` --- open the file under the cursor in **external** program (requires netrw)
- `:cope<cr>` --- **open** the quickfix window
- `:ccl<cr>` --- **close** the quickfix window
- `:cr<cr>` --- **rewind** to the first quickfix item
- `:chi<cr>` --- display the quickfix list **history**
- `:col<cr>` --- go to an **older** quickfix list in the history
- `:cnew<cr>` --- go to a **newer** quickfix list in the history
- v`O` --- switch the parity of v`o` in a blockwise selection
- v`g<c-a>` - v`g<c-x>` --- incrementally increment/decrement numbers in selection
- v`P` --- put from register without overwriting the unnamed register
- c`<c-r><c-w>` --- insert the word under the cursor
- c`<c-r><c-a>` --- insert the WORD under the cursor
- c`<c-r><c-l>` --- insert the line under the cursor
- `gn` - `gN` --- select **next**/previous match, applying an operator if one is pending
- i`<c-x><c-e>` - i`<c-x><c-y>` --- scroll from within insert mode

useful shell bindings spread a little all over the quickref:

- `:!`_cmd_ --- run shell command _cmd_
- `:r!`_cmd_ --- **read in** output of shell command _cmd_
- v`:w !`_cmd_ --- **write out** selected lines to shell command _cmd_
- `!!`_cmd_ --- filter current line through shell command _cmd_
- `!`_motion_ _cmd_ --- filter motion _motion_ through shell command _cmd_
- v`!`_cmd_ --- filter selected lines through shell command _cmd_

some "compound" bindings to be treated as units for [[muscle memory]]:

- `ea` --- insert **after word**
- `Ea` --- insert **after WORD**
- `o<esc>` --- insert a blank line below
- `Jx` --- **join** lines, removing all leading whitespace
- `Jde` --- **join** lines, removing leading word (like `//` [[c]] comments and `-` [[markdown]] lists)
- `xp` --- swap a character with the next
- `ddp` --- swap a line with the next
- `r<cr>` --- split a line at the cursor position
- `m'` --- push current cursor position onto the jumplist (well kind of)
- `==` --- push current text state onto the [[undo tree]] (well kind of)
- `99g+` --- jump to the latest change in the [[undo tree]]
- `99<c-r>` --- jump to the latest change in the current [[undo tree]] branch
- `*N` --- highlight the word under the cursor
- `0D` --- clear out the current line without deleting it
- `VP` --- replace current line with contents of unnamed register
- `<cr>;` --- repeat last `f` or `t` search on next line down

some small tricks and workflows I use:

- peek at occurences of a pattern---without clobbering the last search or cluttering up the jump list---with `/`_re_, then `<c-g>` and `<c-t>`, then `<esc>`
- quickly repeat a compound change by recording it with the usual `qq`_commands_`q` then mashing `Q` (Neovim only)
- perform an interactive substitution with `/`_re_, then `cgn`_replacement_`<esc>` or `dgn`, then skip with `n` and repeat with `.` --- more flexible than `:s/.../c<cr>`
- interactively append a suffix to the end of matches with `/`_re_`/e<cr>`, then `a`_suffix_`<esc>`, then skip with `n` and repeat with `.`
- keep or delete lines matching a pattern with `:g/`_re_`/d<cr>` and `:v/`_re_`/d<cr>`
- grep recursively from the working directory with `:vim/`_re_`/**`; matches are put in the quickfix list
  > **note** turn `:fin` into a fuzzy finder with `set wildmenu path+=**` --- <https://youtu.be/XA2WjJbmmoM?t=6m44s>
- when it exists, print the digraph for the character under the cursor using `ga`
  > **note** useful digraphs worth memorizing: `“”‘’…•‾–—   §¶ °′″‴ ×÷−±√≈≡≤≥≮≯≠∞ ∫∏∑∂∆∇αβγ ∃∀∧∨¬∈∋∅ ½⅔¾₀₁₂₊₋₍₎⁰¹²⁺⁻⁽⁾ⁿ`
- if `'noruler'` is set, query the cursor position with `<c-g>`
- query the word count for a selection and for an entire buffer with `g<c-g>`
- append a suffix to the end of a range of lines with `<c-v>`_selection_`$A`_suffix_`<esc>`
- edit the current command-line in normal mode with `<c-f>`
- move left and right, wrapping across lines, with `<bs>` and `<space>` --- by default, `<bs>` and `<space>` are in `'whichwrap'` while `h` and `l` are not
- jump to the first byte of a file with `go` --- `gg` won't go to the first byte when `'nostartofline'` is set
  > **resource** _Byte Positions Are Better Than Line Numbers_, by Casey Muratori --- <https://www.computerenhance.com/p/byte-positions-are-better-than-line>
- hold the shift key to temporarily disable the mouse
- view a searchable digraph table with `:h euro<cr>`
- jump to a URL or path on the current line with `f/` and `F/` --- slashes are uncommon and URLs and paths usually contain them
- use undos from within insert mode by marking undo points with `<c-g>u` and undoing with `<c-o>u`. delete all entered characters with `<c-u>`
