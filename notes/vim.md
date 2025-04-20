# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[muscle memory]], [[undo tree]]

> **resource** [[vim]] bindings cheat sheet --- [[YLInLlY.png]] --- <https://i.imgur.com/YLInLlY.png>

> **resource** `:h quickref`, specifically the key bindings --- <https://vimdoc.sourceforge.net/htmldoc/quickref.html>

> **resource** `:h registers` --- <https://vimdoc.sourceforge.net/htmldoc/change.html#registers>

> **resource** `:h help-summary` --- <https://vimdoc.sourceforge.net/htmldoc/usr_02.html#help-summary>

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
- v`O` --- switch the parity of v`o` in a visual block selection
- v`g<c-a>` - v`g<c-x>` --- incrementally increment/decrement numbers in selection
- v`P` --- put from register without overwriting the unnamed register
- c`<c-r><c-w>` --- insert the word under the cursor
- c`<c-r><c-a>` --- insert the WORD under the cursor
- c`<c-r><c-l>` --- insert the line under the cursor
- `gn` - `gN` --- select **next**/previous match, applying an operator if one is pending

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
- `0w` --- jump to first non-blank character of line --- quicker than both `^` and `_`
- `Jx` --- **join** lines, removing all leading whitespace
- `Jde` --- **join** lines, removing leading word (like `//` [[c]] comments and `-` [[markdown]] lists)
- `xp` --- swap a character with the next
- `ddp` --- swap a line with the next
- `r<cr>` --- split a line at the cursor position
- `==` --- push current text state onto the [[undo tree]] (well kind of)
- `99g+` --- jump to the latest change in the [[undo tree]]
- `99<c-r>` --- jump to the latest change in the current [[undo tree]] branch
- `*N` --- highlight the word under the cursor
- `0D` --- clear out the current line without deleting it

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
- search through digraphs with `:h dig<cr>`

---

# Bindings

[[vim#motion]]s and [[vim#mark]]s move the cursor around. some [[vim#operator]]s are to be combined with [[vim#motion]]s; [[vim#text object]]s may replace motions within [[vim#operator]]s. [[vim#operator]]s may be prepended by a [[decimal]] [[natural]] to repeat their operation. some [[vim#operator]]s may be prepended by [[vim#register]]s to control where they store and retrieve text

[[vim#macro]]s record and play back sequences of bindings. [[vim#search]] and the [[vim#quickfix]] list help jump around more efficiently

[[vim#compound]]s --- me, are sequences of bindings that can be thought of as a unit, for [[muscle memory]]

## Mode

- `:` --- **command** [[vim#mode]]
- `R` --- **replace** [[vim#mode]]
- `v` --- **visual** [[vim#mode]]
- `V` --- **visual line** [[vim#mode]]
- `<c-v>` --- **visual block** [[vim#mode]]
- `i` --- **insert** [[vim#mode]]
- `I` --- **insert** [[vim#mode]] on first non-blank
- `gI` --- **insert** [[vim#mode]] in first column
- `a` --- insert [[vim#mode]] **after** cursor
- `A` --- insert [[vim#mode]] **after** end of line
- `o` --- insert [[vim#mode]] on **opened** line below
- `O` --- insert [[vim#mode]] on **opened** line above
- `gi` --- **insert** [[vim#mode]] at the position the last insert was stopped
- `gv` --- **visual** [[vim#mode]] reselecting the last selection

## Operator

- `.` --- repeat last change
- `u` - `<c-r>` --- **undo** and **redo**
- `g+` - `g-` --- go to newer/older text state in [[undo tree]]
- `r` --- **replace** character
- `J` --- **join** current line with next
- `gJ` --- **join** current line with next, without adding or removing whitespace
- _r_`x` --- delete character into (optional) [[vim#register]] _r_
- _r_`X` --- delete character before into (optional) [[vim#register]] _r_
- _r_`p` --- **put** from (optional) [[vim#register]] _r_ after
- _r_`P` --- **put** from (optional) [[vim#register]] _r_ before
- v*r*`p` --- write selection to unnamed register then **put** from (optional) [[vim#register]] _r_
- v*r*`P` --- without writing to unnamed register, **put** from (optional) [[vim#register]] _r_
- _r_`d`_m_ --- **delete** [[vim#motion]] _m_ into (optional) [[vim#register]] _r_
- _r_`y`_m_ --- **yank** [[vim#motion]] _m_ into (optional) [[vim#register]] _r_
- _r_`c`_m_ --- **change** [[vim#motion]] _m_ into (optional) [[vim#register]] _r_
- _r_`s` --- **substitute** character into (optional) [[vim#register]] _r_
- _r_`D` --- **delete** to end of line into (optional) [[vim#register]] _r_
- _r_`Y` --- **yank** to end of line into (optional) [[vim#register]] _r_
- _r_`C` --- **change** to end of line into (optional) [[vim#register]] _r_
- _r_`S` --- **substitute** line into (optional) [[vim#register]] _r_
- _r_`dd` --- **delete** line into (optional) [[vim#register]] _r_
- _r_`yy` --- **yank** line into (optional) [[vim#register]] _r_
- _r_`cc` --- **change** line into (optional) [[vim#register]] _r_
- `gU`_m_ --- make [[vim#motion]] _m_ **uppercase**
- `gu`_m_ --- make [[vim#motion]] _m_ lowercase
- `g~`_m_ --- swap [[vim#motion]] _m_ case
- `gUU` --- make line **uppercase**
- `guu` --- make line lowercase
- `g~~` --- swap line case
- `~` --- swap character case
- `g?`_m_ --- rot13 encode [[vim#motion]] _m_
- `g??` --- rot13 encode line
- `>`_m_ --- indent [[vim#motion]] _m_
- `<`_m_ --- unindent [[vim#motion]] _m_
- `=`_m_ --- reindent [[vim#motion]] _m_
- `>>` --- indent line
- `<<` --- unindent line
- `==` --- reindent line
- `<c-a>` - `<c-x>` --- increment/decrement number under or after cursor
- v`g<c-a>` - v`g<c-x>` --- incrementally increment/decrement numbers in visual selection
- v`I`_str_`<esc>` --- **insert** _str_ before all lines in block selection
- v`A`_str_`<esc>` --- **append** _str_ after all lines in block selection

## Register

- `""` --- unnamed [[vim#register]]
- `"_` --- black hole [[vim#register]]
- `"0` --- last yank [[vim#register]]
- `"1` --- last delete [[vim#register]]
- `"-` --- last small delete [[vim#register]]
- `"/` --- last search [[vim#register]]
- `"+` --- system clipboard [[vim#register]]
- `":` --- last command-line [[vim#register]]

## Motion

- `<c-o>` - `<c-i>` --- jump backward/forward in jump list
- `<c-^>` --- toggle between most recent two files
- `m`_m_ --- set local [[vim#mark]] _m_
- `m`_M_ --- set global [[vim#mark]] _M_
- `` ` ``_m_ --- jump to [[vim#mark]] _m_
- `'`_m_ --- jump to line containing [[vim#mark]] _m_
- `%` --- jump between `'matchpairs'` and [[c#preprocessor]] conditionals
- v`o` - v`O` --- jump to other end of visual selection
- `<bs>` - `<space>` --- same as `h` and `l` but included in `'whichwrap'`
- _n_`gg` - _n_`G` --- **goto** line number _n_
- _n_`|` --- jump to column number _n_
- _n_`go` --- jump to byte **offset** _n_ in buffer

  > **resource** _Byte Positions Are Better Than Line Numbers_, by Casey Muratori --- <https://www.computerenhance.com/p/byte-positions-are-better-than-line>

  > **note** use `go` to go to first byte of file. `gg` won't go to first byte when `'nostartofline'`

|              | next | prev | start | mid   | end  |
| ------------ | ---- | ---- | ----- | ----- | ---- |
| character    | `l`  | `h`  |       |       |      |
| word         | `w`  | `b`  | `ge`  |       | `e`  |
| WORD         | `W`  | `B`  | `gE`  |       | `E`  |
| sentence     | `)`  | `(`  |       |       |      |
| display line | `gj` | `gk` | `g0`  |       | `g$` |
| line         | `j`  | `k`  | `0`   | `gM`  | `$`  |
| paragraph    | `}`  | `{`  |       |       |      |
| screen       |      |      | `H`   | `M`   | `L`  |
| file         |      |      | `gg`  | `50%` | `G`  |

|             | next    | prev    | start | mid  | end  |
| ----------- | ------- | ------- | ----- | ---- | ---- |
| line        | `<c-e>` | `<c-y>` |       |      |      |
| half screen | `<c-d>` | `<c-u>` |       |      |      |
| screen      | `<c-f>` | `<c-b>` | `zb`  | `zz` | `zt` |

## Mark

- `''` --- [[vim#mark]] to last jump
- `'.` --- [[vim#mark]] to last change made
- `'"` --- [[vim#mark]] to cursor position when last exiting buffer
- `'<` - `'>` --- [[vim#mark]]s to beginning and end of last selection

## Text Object

|                 | **in** - **inner**     | **all** - **around**   |
| --------------- | ---------------------- | ---------------------- |
| **word**        | `iw`                   | `aw`                   |
| **WORD**        | `iW`                   | `aW`                   |
| **sentence**    | `is`                   | `as`                   |
| **paragraph**   | `ip`                   | `ap`                   |
| `<tag>` **tag** | `it`                   | `at`                   |
| `()` **block**  | `ib` - `i(` - `i)`     | `ab` - `a(` - `a)`     |
| `{}` **BLOCK**  | `iB` - `i{` - `i}`     | `aB` - `a{` - `a}`     |
| `` "'` ``       | `i"` - `i'` - `` i` `` | `a"` - `a'` - `` a` `` |
| `[]`            | `i[` - `i]`            | `a[` - `a]`            |
| `<>`            | `i<` - `i>`            | `a<` - `a>`            |

## Macro

- `q`_m_ --- start recording [[vim#macro]] _m_
- `q` --- stop recording [[vim#macro]]
- `@`_m_ --- play back [[vim#macro]] _m_
- `@@` --- repeat last [[vim#macro]] playback
- `Q` --- play back last recorded [[vim#macro]] (Neovim only)
- `@:` --- re-run last command-line

## Search

- c`<c-g>` - c`<c-t>` --- cycle through `'incsearch'` results
- `gn` - `gN` --- visually select **next**/previous match, applying an operator if one is pending
- `:fin` _file_ --- **find** _file_ in `'path'` then `:e`dit it
  > **note** use `set wildmenu path+=**` to turn `:fin` into a fuzzy finder --- <https://youtu.be/XA2WjJbmmoM?t=6m44s>
- `:vim/`_re_`/`_files_ --- grep for [[regular expression]] _re_ in _files_ into [[vim#quickfix]] list
  > **note** use `:vim/`_re_`/**` to grep recursively from working directory
- `:`_r_`g/`_re_`/d` --- delete lines matching _re_ in [[vim#range]] _r_
- `:`_r_`v/`_re_`/d` --- delete lines not matching _re_ in [[vim#range]] _r_
- `:`_r_`s/`_re_`/`_str_`/g` --- substitute all occurences of _re_ for _str_ in [[vim#range]] _r_

|                                      | forward    | backward   | next | prev |
| ------------------------------------ | ---------- | ---------- | ---- | ---- |
| search [[regular expression]] _re_   | `/`_re_    | `?`_re_    | `n`  | `N`  |
| search word under cursor             | `*` - `g*` | `#` - `g#` | `n`  | `N`  |
| **find** character _c_ in line       | `f`_c_     | `F`_c_     | `;`  | `,`  |
| jump **'till** character _c_ in line | `t`_c_     | `T`_c_     | `;`  | `,`  |

## Quickfix

- `:cope` --- **open** [[vim#quickfix]] window
- `:ccl` --- **close** [[vim#quickfix]] window
- `:cr` --- **rewind** to first [[vim#quickfix]] item
- `:cc` --- jump to **current** [[vim#quickfix]] item
- `:cn` --- jump to **next** [[vim#quickfix]] item
- `:cp` --- jump to **previous** [[vim#quickfix]] item
- `:chi` --- display [[vim#quickfix]] list **history**
- `:col` --- go to **older** [[vim#quickfix]] list in history
- `:cnew` --- go to **newer** [[vim#quickfix]] list in history

> **note** use `@:` to repeat `:cn`s and `:cp`s

## Compound

- `ea` --- insert **after word**
- `Ea` --- insert **after WORD**
- `0w` --- jump to first non-blank character of line
- `cgn` --- **change next** [[vim#search]] match
- `dgn` --- **delete next** [[vim#search]] match
- `Jx` --- **join** lines, removing leading whitespace
- `Jde` --- **join** lines, removing leading characters
- `xp` --- swap character with next
- `ddp` --- swap current line with next
- `r<cr>` --- split line at cursor
- `==` --- push text state onto [[undo tree]] (well kind of)
- `99g+` --- jump to latest change in [[undo tree]]
- `99<c-r>` --- jump to latest change in [[undo tree]] branch
- `*N` --- highlight word under cursor

## miscellanous

- _n_`K` --- open man page for word under cursor in optional section _n_
- `<c-g>` - `g<c-g>` --- show some cursor info and buffer info
- `gf` --- find in `'path'` and `:e`dit **file** under cursor
- `gF` --- find in `'path'` and `:e`dit **file** under cursor at line
- `gx` --- open file under cursor in **external** program (requires netrw)
- `gd` --- jump to local **definition** under cursor
- `gD` --- jump to global **declaration** under cursor
- `ga` --- **get [[ascii]]** value and other metadata for char under cursor
- `g8` --- **get [[utf-8]]** bytes for char under cursor
- `:!`_cmd_ --- show output of shell command _cmd_
- `!!`_cmd_ --- filter current line through shell command _cmd_
- `!`_m_ _cmd_ --- filter [[vim#motion]] _m_ through shell command _cmd_
- `:r!`_cmd_ --- **read in** output of shell command _cmd_
- `:u!` --- **undo** one change and remove it from [[undo tree]]
- `:pw` - `:cd` _path_ --- **print** and **change** working directory
- `:e` _file_ --- **edit** _file_
- `<c-w>r` --- **rotate** windows downwards
- `<c-w>w` --- jump to next **window**
- `<c-w>o` --- make current window the **only** one on screen
- `<c-w>q` --- **quit** current window
- i`<c-n>` - i`<c-p>` --- autocomplete word under cursor with **next**/**previous** match
- i`<c-e>` --- abort an autocompletion (see `:h ins-compl`)
- i`<c-v>` --- insert next keystroke **verbatim**
- i`<c-k>` --- insert a `:dig!`raph
  > **note** useful digraphs worth memorizing: `“”‘’…•‾–—   §¶ °′″‴ ×÷−±√≡≤≥≠∅∞ ∃∀∧∨¬ αβγ ½⅔¾₀₁₂⁰¹²` (use `ga` to see the digraph)
