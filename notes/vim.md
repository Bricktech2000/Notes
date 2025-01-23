# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[muscle memory]]

> **resource** [[vim#bindings]] crash course by Ben Awad --- <https://youtu.be/IiwGbcd8S7I>

> **resource** [[vim#bindings]] cheat sheet --- [[YLInLlY.png]] --- <https://i.imgur.com/YLInLlY.png>

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
- `I` --- **insert** [[vim#mode]] at start of line
- `a` --- insert [[vim#mode]] **after** cursor
- `A` --- insert [[vim#mode]] **after** end of line
- `o` --- insert [[vim#mode]] on **opened** line below
- `O` --- insert [[vim#mode]] on **opened** line above
- `gi` --- insert [[vim#mode]] at the position the last insert was stopped

## Operator

- `u` --- **undo**
- `<c-r>` --- **redo**
- `g+` --- go to newer text state in [[undo tree]]
- `g-` --- go to older text state in [[undo tree]]
- `.` --- repeat
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
- `<c-a>` --- increment number under or after cursor
- `<c-x>` --- decrement number under or after cursor
- v`g<c-a>` --- incrementally increment numbers in visual selection
- v`g<c-x>` --- incrementally decrement numbers in visual selection

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

- `<c-o>` --- jump back in jump list
- `<c-i>` --- jump forward in jump list
- `<c-^>` --- toggle between most recent two files
- `m`_m_ --- set local [[vim#mark]] _m_
- `m`_M_ --- set global [[vim#mark]] _M_
- `` ` ``_m_ --- jump to [[vim#mark]] _m_
- `'`_m_ --- jump to line containing [[vim#mark]] _m_
- `%` --- jump between `'matchpairs'` and [[c#preprocessor]] conditionals
- v`o` - v`O` --- jump to other end of visual selection
- _n_`gg` - _n_`G` --- **goto** line number _n_
- _n_`|` --- jump to column number _n_
- _n_`go` --- jump to byte **offset** _n_ in buffer

  > **resource** _Byte Positions Are Better Than Line Numbers_, by Casey Muratori --- <https://www.computerenhance.com/p/byte-positions-are-better-than-line>

  > **note** use `go` to go to first byte of file

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
- `'<` - `'>` --- [[vim#mark]] to beginning and end of last selection

## Text Object

|                 | **in** - **inner**     | **all** - **around**   |
| --------------- | ---------------------- | ---------------------- |
| **word**        | `iw`                   | `aw`                   |
| **WORD**        | `iW`                   | `aW`                   |
| **sentence**    | `is`                   | `as`                   |
| **paragraph**   | `ip`                   | `ap`                   |
| `<tag>` **tag** | `it`                   | `at`                   |
| `()` **block**  | `ib` - `i(` - `i)`     | `ab` - `a(` - `a)`     |
| `{}` **Block**  | `iB` - `i{` - `i}`     | `aB` - `a{` - `a}`     |
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

- `:fin` _file_ --- **find** _file_ in `'path'` then `:e`dit it
  > **note** use `set wildmenu path+=**` to turn `:fin` into a fuzzy finder --- <https://youtu.be/XA2WjJbmmoM?t=6m44s>
- `:vim/`_re_`/`_files_ --- grep for [[regular expression]] _re_ in _files_ into [[vim#quickfix]] list
  > **note** use `:vim/`_re_`/**` to grep recursively from working directory
- `:`_r_`g/`_re_`/d` --- delete lines matching _re_ in [[vim#range]] _r_
- `:`_r_`v/`_re_`/d` --- delete lines not matching _re_ in [[vim#range]] _r_
- `:`_r_`s/`_re_`/`_str_`/g` --- substitute all accurences of _re_ for _str_ in [[vim#range]] _r_

|                                      | forward    | backward   | next | prev |
| ------------------------------------ | ---------- | ---------- | ---- | ---- |
| search [[regular expression]] _re_   | `/`_re_    | `?`_re_    | `n`  | `N`  |
| search word under cursor             | `*` - `g*` | `#` - `g#` | `n`  | `N`  |
| **find** character _c_ in line       | `f`_c_     | `F`_c_     | `;`  | `,`  |
| jump **'till** character _c_ in line | `t`_c_     | `T`_c_     | `;`  | `,`  |

## Quickfix

- `:cope` --- **open** [[vim#quickfix]] window
- `:ccl` --- **close** [[vim#quickfix]] window
- `:cfir` --- jump to **first** [[vim#quickfix]] item
- `:cla` --- jump to **last** [[vim#quickfix]] item
- `:cn` --- jump to **next** [[vim#quickfix]] item
- `:cp` --- jump to **previous** [[vim#quickfix]] item

> **note** use `@:` to repeat `:cn`s and `:cp`s

## Compound

- `ea` --- insert **after word**
- `Ea` --- insert **after WORD**
- `0w` --- jump to first non-blank character of line
- `cgn` --- **change next** [[vim#search]] match
- `dgn` --- **delete next** [[vim#search]] match
- `Jx` --- **join** lines without a space
- `Jde` --- **join** lines removing leading characters
- `xp` --- swap character with next
- `ddp` --- swap current line with next
- `r<cr>` --- split line at cursor
- `==` --- push text state onto [[undo tree]] (well kind of)
- `99g+` --- jump to latest change in [[undo tree]]
- `99<c-r>` --- jump to latest change in [[undo tree]] branch
- `*N` --- highlight word under cursor

## miscellanous

- _n_`K` --- open man page for word under cursor in optional section _n_
- `<c-g>` - `g<c-g>` --- show some cursor and buffer info
- `gv` --- reselect last **visual** selection
- `gf` --- find in `'path'` and `:e`dit **file** under cursor
- `gF` --- find in `'path'` and `:e`dit **file** under cursor at line
- `gx` --- open file under cursor in **external** program (requires netrw)
- `gd` --- jump to local **definition** under cursor
- `gD` --- jump to global **declaration** under cursor
- `ga` --- **get [[ascii]]** value and metadata for char under cursor
- `g8` --- **get [[utf-8]]** bytes for char under cursor
- `:!`_cmd_ --- show output of shell command _cmd_
- `!!`_cmd_ --- filter current line through shell command _cmd_
- `!`_m_ _cmd_ --- filter [[vim#motion]] _m_ through shell command _cmd_
- `:u!` --- **undo** one change and remove it from [[undo tree]]
- `:pw` - `:cd` _path_ --- **print** and **change** working directory
- `:e` _file_ --- **edit** _file_
- `<c-w>r` --- **rotate** windows downwards
- `<c-w>w` --- jump to next **window**
- `<c-w>o` --- make current window the **only** one on screen
- `<c-w>q` --- **quit** current window
- i`<c-n>` - i`<c-p>` --- autocomplete word under cursor
- i`<c-v>` --- insert next keystroke **verbatim**
- i`<c-k>` --- insert a `:dig!`raph
  > **note** useful digraphs worth memorizing: `“”‘’…•‾–—   §¶ °′″‴ ×÷−±√≡≤≥≠∅∞ ∃∀∧∨¬ αβγ ½⅔¾₀₁₂⁰¹²` (use `ga` to see the digraph)
