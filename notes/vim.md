# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[procedural memory]], [[undo tree]]

> **resource** [[vim]] bindings cheat sheet --- [[YLInLlY.png]] --- <https://i.imgur.com/YLInLlY.png>

> **resource** `:h quickref`, specifically the key bindings --- <https://vimdoc.sourceforge.net/htmldoc/quickref.html>

> **resource** `:h registers`, good reference on registers --- <https://vimdoc.sourceforge.net/htmldoc/change.html#registers>

> **resource** `:h help-summary`, on using `:help` effectively --- <https://vimdoc.sourceforge.net/htmldoc/usr_02.html#help-summary>

[[vim]] bindings are susceptible to [[fossilization]]

some useful bindings not present in the quickref:

- `g+` - `g-` --- go to newer/older text state in the [[undo tree]]
- `:u!<cr>` --- undo one change and remove it from the [[undo tree]]
- `:undol<cr>` --- list all leafs in the [[undo tree]]
- `Q` --- replay last recorded macro (Neovim only)
- `q:` - `q/` - c`<c-f>` --- open command-line window
- `@:` --- repeat the last command-line
- `gi` --- resume insert at the position the last insert was stopped
- i`<c-e>` --- abort an autocompletion (see `|ins-compl|` and `|popupmenu|`)
- i`<c-y>` --- accept an autocompletion (see `|ins-compl|` and `|popupmenu|`)
- `gF` --- edit the file under the cursor at the line specified
- `<c-w>F` --- `gF` but in new window
- `gx` --- _netrw_ open the file under the cursor in external program
- `:cr<cr>` --- rewind to the first quickfix item
- `:cope<cr>` - `:ccl<cr>` --- open/cloe the quickfix window
- `:cpf<cr>` - `:cnf<cr>` --- `:cn<cr>`/`:cp<cr>` until a new file is hit
- `:chi<cr>` --- display the quickfix list history
- `:col<cr>` - `:cnew<cr>` --- go to an older/newer quickfix list in the history
- v`O` --- switch the parity of v`o` in a blockwise selection
- v`g<c-a>` - v`g<c-x>` --- incrementally increment/decrement numbers in selection
- v`P` --- put from register without overwriting the unnamed register
- c`<c-r><c-w>` --- insert the word under the cursor
- c`<c-r><c-a>` --- insert the WORD under the cursor
- c`<c-r><c-l>` --- insert the line under the cursor
- `gn` - `gN` --- select next/previous match, applying an operator if one is pending
- o`v` - o`V` - o`<c-v>` --- force the operator to work charwise/linewise/blockwise
- o`v` --- when motion is charwise, toggle inclusive/exclusive
- o`2i'` - o`2i"` --- o`a'`/o`a"` but without surrounding whitespace
- i`<c-x><c-e>` - i`<c-x><c-y>` --- scroll from within insert mode
- i`<c-x><c-l>` --- autocomplete the entire line, ignoring indent
- i`<c-x><c-l>` --- after `<c-x><c-l>`, autocomplete subsequent lines
- i`<c-x><c-f>` --- autocomplete from filenames in working directory
- i`<c-x><c-n>` - i`<c-x><c-p>` --- after `<c-n>`/`<c-p>`, autocomplete subsequent words
- i`<c-x><c-i>` - i`<c-x><c-d>` --- autocomplete from occurrences/definitions across includes
- `[i` - `[d` --- display first occurrence/definition of word under cursor across includes
- `[I` - `[D` --- display all occurrences/definitions of word under cursor across includes
- `[<c-i>` - `[<c-d>` --- go to first occurrence/definition of word under cursor across includes
- `]<c-i>` - `]<c-d>` --- go to next ccurrence/definition of word under cursor across includes
- `<c-w>i` - `<c-w>d` --- `[<c-i>`/`[<c-d>` but in new window
- `1gd` - `1gD` --- `gd`/`gD` but ignore `{}` blocks before the cursor
- v`zy` - `zp` --- yank/paste a block, removing trailing spaces
- c`<c-n>` - c`<c-p>` --- recall next/previous command line
- `:mes<cr>` --- view message history
- i`<c-g>k` - i`<c-g>j` --- go to the column where insert was started, one line up/down
- `[%` - `]%` --- _matchit.vim_ jump to beginning/end of `%`able group
- `g%` --- _matchit.vim_ cycle backward through `%`able groups
- `zs` - `ze` - scroll so the cursor is on the left/right of the window
- `N <c-w>q` --- quit Nth window
- `:tabs<cr>` --- list open tabpages
- `:tabe<cr>` --- open new blank tabpage
- `<c-w>T` --- move current window to new tabpage
- `<c-w>gf` - `<c-w>gF` --- `gf`/`gF` but in new tabpage
- `:tabe FILE<cr>` - `:tabf FILE<cr>` --- `:e FILE<cr>`/`:fin FILE<cr>` but in new tabpage
- `:tab CMD<cr>` --- run `CMD` but open tabpages instead of windows
- `:tabc<cr>` --- close the current tabpage
- `:tabo<cr>` --- close all tabpages but the current one
- `gt` - `gT` - `N gt` --- go to next/previous/Nth tabpage
- `g<tab>` - `<c-w>g<tab>` --- toggle between two most recent tabpages
- `:diffs FILE<cr>` --- open `FILE` in new window and enable diff mode
- `:diffp PATCH<cr>` --- apply `PATCH` in new window and enable diff mode
- `:difft<cr>` - `:diffo<cr>` --- add/remove current window to/from the diff windows
- `:diffo!<cr>` --- switch off diff mode for all windows of current tabpage
- `[c` - `]c` --- jump to previous/next diff change
- `N do` - `N dp` --- obtain/put a diff change from/to buffer number N

useful shell bindings spread a little all over the quickref:

- `:!`_cmd_ --- run shell command _cmd_
- `:r!`_cmd_ --- read in output of shell command _cmd_
- v`:w !`_cmd_ --- write out selected lines to shell command _cmd_
- `!!`_cmd_ --- filter current line through shell command _cmd_
- `!`_motion_ _cmd_ --- filter motion _motion_ through shell command _cmd_
- v`!`_cmd_ --- filter selected lines through shell command _cmd_

some "compound" bindings to be treated as units for [[procedural memory]]:

- `ea` --- insert after word
- `Ea` --- insert after WORD
- `o<esc>` - `O<esc>` --- insert a blank line below/above
- `Jx` --- join lines, removing all leading whitespace
- `Jde` --- join lines, removing leading word (like `//` [[c]] comments and `-` [[markdown]] lists)
- `xp` --- swap a character with the next
- `ddp` --- swap a line with the next
- `r<cr>` --- split a line at the cursor position
- `m'` --- push current cursor position onto the jumplist (well kind of)
- `==` --- push current text state onto the [[undo tree]] (well kind of)
- `99g+` --- jump to the latest change in the [[undo tree]]
- `99<c-r>` --- jump to the latest change in the current [[undo tree]] branch
- `*N` --- highlight the word under the cursor
- `0D` --- clear out the current line without deleting it
- `VP` --- replace the current line with the contents of the unnamed register
- `<cr>;` - `-;` --- repeat last `f`/`t` search on the next/previous line
- `gon` - `GN` --- repeat last `/`/`?` search from the start/end of the buffer
- `<c-^><c-w>^` --- reopen just-opened buffer in new window instead
- `<space><bs>` - `<bs><space>` --- set curswant to the current column number

some small tricks and workflows I use:

- peek at occurrences of a pattern---without clobbering the last search or cluttering up the jumplist---with `/`_re_, then `<c-g>` and `<c-t>`, then `<esc>`
- quickly repeat a compound change by recording it with the usual `qq`_commands_`q` then mashing `Q` (Neovim only)
- perform an interactive substitution with `/`_re_, then `cgn`_replacement_`<esc>` or `dgn`, then skip with `n` and repeat with `.` --- more flexible than `:s/.../c<cr>`
- interactively append a suffix to the end of matches with `/`_re_`/e<cr>`, then `a`_suffix_`<esc>`, then skip with `n` and repeat with `.`
- keep or delete lines matching a pattern with `:g/`_re_`/d<cr>` and `:v/`_re_`/d<cr>`
- grep recursively from the working directory with `:vim/`_re_`/**<cr>`; matches are put in the quickfix list
  > **note** turn `:fin` into a fuzzy finder with `set wildmenu path+=**` --- <https://youtu.be/XA2WjJbmmoM?t=6m44s>
- when it exists, print the digraph for the character under the cursor using `ga`
  > **note** useful digraphs worth memorizing: `“”‘’…•‾–—   §¶ °′″‴ ×÷−±√≈≡≤≥≮≯≠∞∝ ∫∏∑∂∆∇αβγ ∃∀∧∨¬∈∋∅ ½⅔¾₀₁₂₊₋₍₎⁰¹²⁺⁻⁽⁾ⁿ`
- if `'noruler'` is set, query the cursor position with `<c-g>`
- query the word count for a selection and for an entire buffer with `g<c-g>`
- append a suffix to the end of a range of lines with `<c-v>`_selection_`$A`_suffix_`<esc>`
- edit the current command-line in normal mode with `<c-f>`
- move left and right, wrapping across lines, with `<bs>` and `<space>` --- by default, `<bs>` and `<space>` are in `'whichwrap'` while `h` and `l` are not
- jump to the first byte of a file with `go` --- `gg` won't go to the first byte when `'nostartofline'` is set
  > **resource** _Byte Positions Are Better Than Line Numbers_, by Casey Muratori --- [[Byte Positions Are Better Than Line Numbers.pdf]] --- <https://www.computerenhance.com/p/byte-positions-are-better-than-line>
- hold the shift key to temporarily disable the mouse
- view a searchable digraph table with `:h euro<cr>`
- jump to a URL or path on the current line with `f/` and `F/` --- slashes are uncommon and URLs and paths usually contain them
- use undos from within insert mode by marking undo points with `<c-g>u` and undoing with `<c-o>u`. delete all entered characters with `<c-u>`
- temporarily isolate a window with `<c-w>|`/`<c-w>_` then revert to equal window size with `<c-w>=`
- insert something of the form _first second first third_ using `i`_first_`<esc>a`_second_`<c-a>`_third_
- repeat a change with a different motion using `c`_motion_ _replacement_ then `c`_motion_`<c-a>`
- fill out one cell of a plaintext table with `gR`_cell contents_ then move to the next cell up/down with `<c-g>k`/`<c-g>j`
- perform a `*` without clobbering the last search with `]<tab>` aka `]<c-i>`
- set curswant to the current column number by hitting `<space>` and `<bs>` simultaneously
- delete the current buffer without closing the window by editing another buffer with say `<c-^>` then running `:bd#<cr>`
- delete an entire `if/for/while (...) { ... }` construct with `dVaB`

Vim patterns support a `\&` [[operator]] that may look like [[regular expression]] intersection, but unfortunately it's just a lookahead because the subpattern matches are not required to end at the same positions. what a shame
