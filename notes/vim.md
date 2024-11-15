# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[muscle memory]]

> **resource** [[vim#bindings]] crash course by Ben Awad --- <https://youtu.be/IiwGbcd8S7I>

> **resource** [[vim#bindings]] cheat sheet --- <https://i.imgur.com/YLInLlY.png>

---

# Bindings

[[vim#motion]]s move the cursor around. some [[vim#operator]]s are to be combined with [[vim#motion]]s; [[vim#text object]]s may replace motions within [[vim#operator]]s. [[vim#operator]]s may be prepended by a [[decimal]] number to repeat their operation. some [[vim#operator]]s may be prepended by [[vim#register]]s, allowing for storage and retrieval of text

[[vim#macro]]s allow for recording and playing back sequences of bindings. [[vim#search]] and [[vim#mark]]s allow for jumping around efficiently

[[vim#compound]]s --- me, are sequences of bindings that can be thought of as a single binding for the sake of [[muscle memory]]

## Mode

- `:` --- _command_ [[vim#mode]]
- `R` --- _replace_ [[vim#mode]]
- `v` --- _visual_ [[vim#mode]]
- `V` --- _visual line_ [[vim#mode]]
- `<c-v>` --- _visual block_ [[vim#mode]]
- `i` --- _insert_ [[vim#mode]]
- `I` --- _insert_ [[vim#mode]] at start of line
- `a` --- insert [[vim#mode]] _after_ cursor
- `A` --- insert [[vim#mode]] at end of line
- `o` --- insert [[vim#mode]] on _opened_ line below
- `O` --- insert [[vim#mode]] on _opened_ line above

## Operator

- `u` --- _undo_
- `<c-r>` --- _redo_
- `g+` --- go to newer text state in undo tree
- `g-` --- go to older text state in undo tree
- `.` --- repeat
- `r` --- _replace_ character
- `J` --- _join_ current line with next
- **r**`x` --- delete character into (optional) [[vim#register]] **r**
- **r**`X` --- delete character before into (optional) [[vim#register]] **r**
- **r**`p` --- _put_ from (optional) [[vim#register]] **r** after
- **r**`P` --- _put_ from (optional) [[vim#register]] **r** before
- **r**`d`**m** --- _delete_ [[vim#motion]] **m** into (optional) [[vim#register]] **r**
- **r**`y`**m** --- _yank_ [[vim#motion]] **m** into (optional) [[vim#register]] **r**
- **r**`c`**m** --- _change_ [[vim#motion]] **m** into (optional) [[vim#register]] **r**
- **r**`s` --- _substitute_ character into (optional) [[vim#register]] **r**
- **r**`D` --- _delete_ to end of line into (optional) [[vim#register]] **r**
- **r**`Y` --- _yank_ to end of line into (optional) [[vim#register]] **r**
- **r**`C` --- _change_ to end of line into (optional) [[vim#register]] **r**
- **r**`S` --- _substitute_ line into (optional) [[vim#register]] **r**
- **r**`dd` --- _delete_ line into (optional) [[vim#register]] **r**
- **r**`yy` --- _yank_ line into (optional) [[vim#register]] **r**
- **r**`cc` --- _change_ line into (optional) [[vim#register]] **r**
- `gU`**m** --- make [[vim#motion]] **m** _uppercase_
- `gu`**m** --- make [[vim#motion]] **m** lowercase
- `g~`**m** --- swap [[vim#motion]] **m** case
- `~` --- swap character case
- `>`**m** --- indent [[vim#motion]] **m**
- `<`**m** --- unindent [[vim#motion]] **m**
- `=`**m** --- reindent [[vim#motion]] **m**
- `>>` --- indent line
- `<<` --- unindent line
- `==` --- reindent line

## Register

- `""` --- unnamed [[vim#register]]
- `"_` --- black hole [[vim#register]]
- `"0` --- last yank [[vim#register]]
- `"1` --- last delete [[vim#register]]
- `"/` --- last search [[vim#register]]
- `"+` --- system clipboard [[vim#register]]
- `":` --- last command-line [[vim#register]]

## Motion

- `<c-o>` --- jump back in jump list
- `<c-i>` --- jump forward in jump list
- `<c-^>` --- jump to alternate file
- `''` --- jump back to last jump
- `` ` ``**m** --- jump to [[vim#mark]] **m**
- `'`**m** --- jump to line containing [[vim#mark]] **m**
- **n**`gg` - **n**`G` --- jump to line number **n**
- **n**`|` --- jump to column number **n**
- **n**`go` --- jump to byte number **n**
  > **resource** _Byte Positions Are Better Than Line Numbers_, by Casey Muratori --- <https://www.computerenhance.com/p/byte-positions-are-better-than-line>

|              | next | prev | start | mid   | end  |
| ------------ | ---- | ---- | ----- | ----- | ---- |
| character    | `l`  | `h`  |       |       |      |
| word         | `w`  | `b`  | `ge`  |       | `e`  |
| Word         | `W`  | `B`  | `gE`  |       | `E`  |
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

## Text Object

|               | _in_ - _inner_         | _all_ - _around_       |
| ------------- | ---------------------- | ---------------------- |
| _word_        | `iw`                   | `aw`                   |
| _Word_        | `iW`                   | `aW`                   |
| _sentence_    | `is`                   | `as`                   |
| _paragraph_   | `ip`                   | `ap`                   |
| `<>` _tag_    | `it`                   | `at`                   |
| `()` _braces_ | `ib` - `i(` - `i)`     | `ab` - `a(` - `a)`     |
| `{}` _Braces_ | `iB` - `i{` - `i}`     | `aB` - `a{` - `a}`     |
| `` "'` ``     | `i"` - `i'` - `` i` `` | `a"` - `a'` - `` a` `` |
| `[]`          | `i[` - `i]`            | `a[` - `a]`            |
| `<>`          | `i<` - `i>`            | `a<` - `a>`            |

## Macro

- `q`**m** --- start recording [[vim#macro]] **m**
- `q` --- stop recording [[vim#macro]]
- `@`**m** --- play back [[vim#macro]] **m**
- `@@` --- repeat last [[vim#macro]] playback
- `Q` --- play back last recorded [[vim#macro]] (Neovim only)
- `@:` --- re-run last command-line

## Search

- `cgn` --- change next [[vim#search]] match
- `dgn` --- delete next [[vim#search]] match

|                              | forward    | backward   | next | prev |
| ---------------------------- | ---------- | ---------- | ---- | ---- |
| search string **str**        | `/`**str** | `?`**str** | `n`  | `N`  |
| search word                  | `*` - `g*` | `#` - `g#` | `n`  | `N`  |
| find _first_ character **c** | `f`**c**   | `F`**c**   | `;`  | `,`  |
| find _upto_ character **c**  | `t`**c**   | `T`**c**   | `;`  | `,`  |

## Mark

- `m`**m** --- set local [[vim#mark]] **m**
- `m`**M** --- set global [[vim#mark]] **M**

## Compound

- `ea` --- insert after word
- `Ea` --- insert after Word
- `0w` --- first non-blank character of line
- `Jx` --- join lines without a space
- `Jde` --- join lines removing leading characters
- `xp` --- swap character with next
- `ddp` --- swap current line with next
- `r<cr>` --- split line at cursor
- `==` --- push text state onto undo tree (well kind of)
- `99g+` --- jump to latest change in undo tree
- `99<c-r>` --- jump to latest change in undo branch

## miscellanous

- `<c-g>` - `g<c-g>` --- show some buffer info
- `gv` --- re-select last _visual_ selection
- `gf` --- open _file_ under cursor
- `gd` --- jump to local _definition_ under cursor
- `gD` --- jump to global _declaration_ under cursor
- `:!`**cmd** --- run shell command **cmd**
- `!!`**cmd** --- run shell command **cmd** on current line
- `:%!`**cmd** --- run shell command **cmd** on entire file
- `:u!` --- undo one change and remove it from undo tree
