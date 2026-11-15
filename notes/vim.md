# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[procedural memory]], [[undo tree]]

> **resource** [[vim]] bindings cheat sheet --- [[../references/YLInLlY.png]] --- <https://i.imgur.com/YLInLlY.png>

> **resource** `:h quickref`, specifically the key bindings --- <https://vimdoc.sourceforge.net/htmldoc/quickref.html>

> **resource** `:h registers`, good reference on registers --- <https://vimdoc.sourceforge.net/htmldoc/change.html#registers>

> **resource** `:h help-summary`, on using `:help` effectively --- <https://vimdoc.sourceforge.net/htmldoc/usr_02.html#help-summary>

[[vim]] bindings are susceptible to [[fossilization]]

some useful bindings not present in the quickref:

- `g+` - `g-` --- go to newer/older text state in the [[undo tree]]
- `:u!<CR>` --- undo one change and remove it from the [[undo tree]] (Neovim only)
- `:undol<CR>` --- list all leafs in the [[undo tree]]
- `Q` --- replay last recorded macro (Neovim only)
- `q:` - `q/` - c`<C-F>` --- open command-line window
- `@:` --- repeat the last command-line
- `gi` --- resume insert at the position the last insert was stopped
- i`<C-E>` --- abort an autocompletion (see `|ins-compl|` and `|popupmenu|`)
- i`<C-Y>` --- accept an autocompletion (see `|ins-compl|` and `|popupmenu|`)
- `gF` --- edit the file under the cursor at the line specified
- `<C-W>F` --- `gF` but in new window
- `gx` --- _netrw_ open the file under the cursor in external program
- `:cr<CR>` - `:lr<CR>` --- rewind to the first quickfix/location list item
- `:cope<CR>` - `:ccl<CR>` - `:lop<CR>` - `:lcl<CR>` --- open/close quickfix/location list window
- `:cnf<CR>` - `:cpf<CR>` - `:lnf<CR>` - `:lpf<CR>` --- `:cn`/`:cp`/`:lne`/`:lp` until a new file is hit
- `:chi<CR>` - `:lhi<CR>` --- display the quickfix/location list history
- `:col<CR>` - `:cnew<CR>` - `:lol<CR>` - `:lnew<CR>` --- go to older/newer quickfix/location list in history
- `:lne<CR>` - `:lp<CR>` - `:ll<CR>` - `:lli<CR>` --- `:cn`/`:cp`/`:cc`/`:cl` but for location list
- `:lmak` - `:lgr` - `:lv` - `:lh` --- `:mak`/`:gr`/`:vim`/`:helpg` but for location list
- v`O` --- switch the parity of v`o` in a blockwise selection
- v`g<C-A>` - v`g<C-X>` --- incrementally increment/decrement numbers in selection
- v`P` --- put from register without overwriting the unnamed register
- c`<C-R><C-W>` --- insert the word under the cursor
- c`<C-R><C-A>` --- insert the WORD under the cursor
- c`<C-R><C-L>` --- insert the line under the cursor
- `gn` - `gN` --- select next/previous match, applying an operator if one is pending
- o`v` - o`V` - o`<C-V>` --- force the operator to work charwise/linewise/blockwise
- o`v` --- when motion is charwise, toggle inclusive/exclusive
- o`2i'` - o`2i"` --- o`a'`/o`a"` but without surrounding whitespace
- i`<C-X><C-E>` - i`<C-X><C-Y>` --- scroll from within insert mode
- i`<C-X><C-L>` --- autocomplete the entire line, ignoring indent
- i`<C-X><C-L>` --- after `<C-X><C-L>`, autocomplete subsequent lines
- i`<C-X><C-F>` --- autocomplete from filenames in working directory
- i`<C-X><C-N>` - i`<C-X><C-P>` --- after `<C-N>`/`<C-P>`, autocomplete subsequent words
- i`<C-X><C-I>` - i`<C-X><C-D>` --- autocomplete from occurrences/definitions across includes
- `[i` - `[d` --- display first occurrence/definition of word under cursor across includes
- `[I` - `[D` --- display all occurrences/definitions of word under cursor across includes
- `[<C-I>` - `[<C-D>` --- go to first occurrence/definition of word under cursor across includes
- `]<C-I>` - `]<C-D>` --- go to next occurrence/definition of word under cursor across includes
- `<C-W>i` - `<C-W>d` --- `[<C-I>`/`[<C-D>` but in new window
- `1gd` - `1gD` --- `gd`/`gD` but ignore `{}` blocks before the cursor
- v`zy` --- yank a block, remove trailing whitespace at the end of each line
- v`zp` - v`zP` --- put a block, don't add trailing spaces to pad to the block's width
- c`<C-N>` - c`<C-P>` --- recall next/previous command line
- `:mes<CR>` --- view message history
- i`<C-G>k` - i`<C-G>j` --- jump to column where insert was started, one line up/down
- `[%` - `]%` --- _matchit.vim_ jump to beginning/end of `%`able group
- `g%` --- _matchit.vim_ cycle backward through `%`able groups
- `zs` - `ze` - scroll so the cursor is on the left/right of the window
- i`<C-G>U` --- prevent the next left/right cursor movement from closing the undo sequence
- `N<C-W>q` --- quit Nth window
- `:tabs<CR>` --- list open tabpages
- `:tabe<CR>` --- open new blank tabpage
- `:tabe FILE<CR>` - `:tabf FILE<CR>` --- `:e FILE<CR>`/`:fin FILE<CR>` but in new tabpage
- `:tab CMD<CR>` --- run `CMD` but open tabpages instead of windows
- `<C-W>T` --- move current window to new tabpage
- `<C-W>gf` - `<C-W>gF` --- `gf`/`gF` but in new tabpage
- `:tabc<CR>` --- close the current tabpage
- `:tabo<CR>` --- close all tabpages but the current one
- `:tabm<CR>` - `:tabmN<CR>` --- move current tabpage after last/Nth tabpage
- `:tabm#<CR>` --- move current tabpage after last accessed tabpage
- `:tabm+<CR>` - `:tabm-<CR>` --- move current tabpage right/left
- `gt` - `gT` - `Ngt` --- go to next/previous/Nth tabpage
- `g<Tab>` - `<C-W>g<Tab>` --- toggle between two most recent tabpages
- `:diffs FILE<CR>` --- open `FILE` in new window and enable diff mode
- `:diffp PATCH<CR>` --- apply `PATCH` in new window and enable diff mode
- `:difft<CR>` - `:diffo<CR>` --- add/remove current window to/from the diff windows
- `:diffo!<CR>` --- switch off diff mode for all windows of current tabpage
- `[c` - `]c` --- jump to previous/next diff change
- `Ndo` - `Ndp` --- obtain/put a diff change from/to buffer number N
- `:bw<CR>` --- `:bd` but actually delete the buffer; `:bd` just unlist it
- `:Nmat GRP /RE/<CR>` --- temporarily highlight `RE` with `GRP` in current window
- `:Nmat<CR>` --- clear previous `:Nmat GRP /RE/<CR>`
- i`<C-^>` - c`<C-^>` --- toggle `:lmap` mappings
- `:wind<CR>` - `:bufd<CR>` - `:tabd<CR>` - `:cfd<CR>` - `:lfd<CR>` - `:ld<CR>` --- shorter
- `:argdo<CR>` - `:cdo<CR>` --- can't shorten
- i`<C-R><C-O>` --- like i`<C-R><C-R>` but `.` uses register contents at the time of repeat
- `:1<CR>` - `:$<CR>` - `:N<CR>` --- `gg`/`G`/`Ngg` but without changing the jumplist
- `:cq<CR>` - `:cq0<CR>` --- shorter and more ergonomic `:qa!<CR>`
- `x` --- after i`<C-V>`, terminate character code and insert character (this is a bug)
- /`\%V` --- matches insid the visual area

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
- `o<Esc>` - `O<Esc>` --- insert a blank line below/above
- `Jx` --- join lines, removing all leading whitespace
- `Jde` --- join lines, removing leading word (like `//` [[c]] comments and `-` [[markdown]] lists)
- `xp` --- swap a character with the next
- `ddp` --- swap a line with the next
- `r<CR>` --- split a line at the cursor position
- `m'` --- push current cursor position onto the jumplist (well kind of)
- `==` --- push current text state onto the [[undo tree]] (well kind of)
- `99g+` --- jump to the latest change in the [[undo tree]]
- `99<C-R>` --- jump to the latest change in the current [[undo tree]] branch
- `*N` --- highlight the word under the cursor
- `0D` --- clear out the current line without deleting it
- `VP` --- replace the current line with the contents of the unnamed register
- `<CR>;` - `-;` --- repeat last `f`/`t` search on the next/previous line
- `gon` - `GN` --- repeat last `/`/`?` search from the start/end of the buffer
- `<C-^><C-W>^` --- reopen just-opened buffer in new window instead
- `<Space><BS>` - `<BS><Space>` --- set curswant to the current column number

some small tricks and workflows I use:

- peek at occurrences of a pattern---without clobbering the last search or cluttering up the jumplist---with `/`_re_, then `<C-G>` and `<C-T>`, then `<Esc>`
- quickly repeat a compound change by recording it with the usual `qq`_commands_`q` then mashing `Q` (Neovim only)
- perform an interactive substitution with `/`_re_, then `cgn`_replacement_`<Esc>` or `dgn`, then skip with `n` and repeat with `.` --- more flexible than `:s/.../c<CR>`
- interactively append a suffix to the end of matches with `/`_re_`/e<CR>`, then `a`_suffix_`<Esc>`, then skip with `n` and repeat with `.`
- keep or delete lines matching a pattern with `:g/`_re_`/d<CR>` and `:v/`_re_`/d<CR>`
- grep recursively from the working directory with `:vim/`_re_`/**<CR>`; matches are put in the quickfix list
  > **note** turn `:fin` into a fuzzy finder with `set wildmenu path+=**` --- <https://youtu.be/XA2WjJbmmoM?t=6m44s>
- when it exists, print the digraph for the character under the cursor using `ga`
  > **note** useful digraphs worth memorizing: `“”‘’‥…•·‾–—   §¶№¢ °′″‴ µΩÅ℃℉ ×÷−±∓∗∘∙⋅∶∷∴∵∼≈≡≤≥≮≯≠∞∝ √⌈⌉⌊⌋∫∏∑∂∆∇αβγ ∃∀∧∨¬∩∪∈∋∅⊂⊃⊆⊇ ⅠⅡⅢⅩⅪⅫⅰⅱⅲⅹⅺⅻ ½⅔¾₀₁₂₊₋₍₎⁰¹²⁺⁻⁽⁾ⁿ`
- if `'noruler'` is set, query the cursor position with `<C-G>`
- query the word count for a selection and for an entire buffer with `g<C-G>`
- append a suffix to the end of a range of lines with `<C-V>`_selection_`$A`_suffix_`<Esc>`
- edit the current command-line in normal mode with `<C-F>`
- move left and right, wrapping across lines, with `<BS>` and `<Space>` --- by default, `<BS>` and `<Space>` are in `'whichwrap'` while `h` and `l` are not
- jump to the first byte of a file with `go` --- `gg` won't go to the first byte when `'nostartofline'` is set
  > **resource** _Byte Positions Are Better Than Line Numbers_, by Casey Muratori --- [[../references/Byte Positions Are Better Than Line Numbers.pdf]] --- <https://www.computerenhance.com/p/byte-positions-are-better-than-line>
- hold the shift key to temporarily disable the mouse
- view a searchable digraph table with `:h euro<CR>`
- jump to a URL or path on the current line with `f/` and `F/` --- slashes are uncommon and URLs and paths usually contain them
- use undos from within insert mode by marking undo points with `<C-G>u` and undoing with `<C-O>u`. delete all entered characters with `<C-U>`
- temporarily isolate a window with `<C-W>|`/`<C-W>_` then revert to equal window size with `<C-W>=`
- insert something of the form _first second first third_ using `i`_first_`<Esc>a`_second_`<C-A>`_third_
- repeat a change with a different motion using `c`_motion_ _replacement_ then `c`_motion_`<C-A>`
- fill out one cell of a plaintext table with `gR`_cell contents_ then move to the next cell up/down with `<C-G>k`/`<C-G>j`
- perform a `*` without clobbering the last search with `]<Tab>` aka `]<C-I>`
- set curswant to the current column number by hitting `<Space>` and `<BS>` simultaneously
- delete the current buffer without closing the window by editing another buffer with say `<C-^>` then running `:bd#<CR>` or `:bw#<CR>`
- delete an entire `if/for/while (...) { ... }` construct with `dVaB`
- to edit binary files use `:e ++enc=ansi<CR>` or `:se fenc=ansi<CR>` --- each glyph is one byte, `ga` works, i`<C-V>` works, etc.
- put a blockwise register linewise using `:pu<CR>`; put a linewise register charwise using `vp`
- quit Vim without writing to the viminfo file with `:se vi=|q<CR>`
- insert the raw byte _XX_ (not the character _XX_) into the buffer with `i<C-R><C-O>="\x`_XX_`"<CR>`

Vim patterns support a `\&` [[operator]] that may look like [[regular expression]] intersection, but unfortunately it's just a lookahead because the subpattern matches are not required to end at the same positions. what a shame
