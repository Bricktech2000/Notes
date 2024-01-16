# Vim

_a highly customizable text editor with efficient key bindings_

**see** [[muscle memory]]

> **resource** [[vim#bindings]] crash course by Ben Awad &mdash; <https://youtu.be/IiwGbcd8S7I>

> **resource** [[vim#bindings]] cheat sheet &mdash; <https://i.imgur.com/YLInLlY.png>

---

# Bindings

[[vim#motion]]s move the cursor around. some [[vim#operator]]s are to be combined with [[vim#motion]]s; [[vim#text object]]s may replace motions within [[vim#operator]]s. [[vim#operator]]s may be prepended by a [[decimal]] number to repeat their operation. some [[vim#operator]]s may be prepended by [[vim#register]]s, allowing for storage and retrieval of text

[[vim#macro]]s allow for recording and playing back sequences of bindings. [[vim#search]] and [[vim#mark]]s allow for jumping around efficiently

[[vim#compound]]s &mdash; me, are sequences of bindings that can be thought of as a single binding for the sake of [[muscle memory]]

## Mode

- `:` &mdash; _command_ [[vim#mode]]
- `R` &mdash; _replace_ [[vim#mode]]
- `v` &mdash; _visual_ [[vim#mode]]
- `V` &mdash; _visual line_ [[vim#mode]]
- `<C-v>` &mdash; _visual block_ [[vim#mode]]
- `i` &mdash; _insert_ [[vim#mode]]
- `I` &mdash; _insert_ [[vim#mode]] at start of line
- `a` &mdash; insert [[vim#mode]] _after_ cursor
- `A` &mdash; insert [[vim#mode]] at end of line
- `o` &mdash; insert [[vim#mode]] on _opened_ line below
- `O` &mdash; insert [[vim#mode]] on _opened_ line above

## Operator

- `u` &mdash; _undo_
- `<C-r>` &mdash; _redo_
- `g+` &mdash; go to next change in undo tree
- `g-` &mdash; go to previous change in undo tree
- `.` &mdash; repeat
- `r` &mdash; _replace_ character
- `J` &mdash; _join_ current line with next
- **r**`x` &mdash; delete character into (optional) [[vim#register]] **r**
- **r**`X` &mdash; delete character before into (optional) [[vim#register]] **r**
- **r**`p` &mdash; _put_ from (optional) [[vim#register]] **r** after
- **r**`P` &mdash; _put_ from (optional) [[vim#register]] **r** before
- **r**`d`**m** &mdash; _delete_ [[vim#motion]] **m** into (optional) [[vim#register]] **r**
- **r**`y`**m** &mdash; _yank_ [[vim#motion]] **m** into (optional) [[vim#register]] **r**
- **r**`c`**m** &mdash; _change_ [[vim#motion]] **m** into (optional) [[vim#register]] **r**
- **r**`s` &mdash; _substitute_ character into (optional) [[vim#register]] **r**
- **r**`D` &mdash; _delete_ to end of line into (optional) [[vim#register]] **r**
- **r**`Y` &mdash; _yank_ to end of line into (optional) [[vim#register]] **r**
- **r**`C` &mdash; _change_ to end of line into (optional) [[vim#register]] **r**
- **r**`S` &mdash; _substitute_ line into (optional) [[vim#register]] **r**
- **r**`dd` &mdash; _delete_ line into (optional) [[vim#register]] **r**
- **r**`yy` &mdash; _yank_ line into (optional) [[vim#register]] **r**
- **r**`cc` &mdash; _change_ line into (optional) [[vim#register]] **r**
- `gU`**m** &mdash; make [[vim#motion]] **m** _uppercase_
- `gu`**m** &mdash; make [[vim#motion]] **m** lowercase
- `g~`**m** &mdash; swap [[vim#motion]] **m** case
- `~` &mdash; swap character case
- `>`**m** &mdash; indent [[vim#motion]] **m**
- `<`**m** &mdash; unindent [[vim#motion]] **m**
- `=`**m** &mdash; reindent [[vim#motion]] **m**
- `>>` &mdash; indent line
- `<<` &mdash; unindent line
- `==` &mdash; reindent line

## Register

- `""` &mdash; unnamed [[vim#register]]
- `"_` &mdash; black hole [[vim#register]]
- `"0` &mdash; last yank [[vim#register]]
- `"/` &mdash; last search [[vim#register]]
- `":` &mdash; last command [[vim#register]]
- `"+` &mdash; system clipboard [[vim#register]]

## Motion

- `<C-o>` &mdash; jump back in jump list
- `<C-i>` &mdash; jump forward in jump list
- `''` &mdash; jump back to last jump
- `` ` ``**m** &mdash; jump to mark **m**
- `'`**m** &mdash; jump to line containing mark **m**
- **n**`gg` &bull; **n**`G` &mdash; jump to line number **n**

|              | next | prev | start | mid   | end  |
| ------------ | ---- | ---- | ----- | ----- | ---- |
| character    | `l`  | `h`  |       |       |      |
| word         | `w`  | `b`  | `ge`  |       | `e`  |
| Word         | `W`  | `B`  | `gE`  |       | `E`  |
| sentence     | `)`  | `(`  |       |       |      |
| display line | `gj` | `gk` | `g0`  |       | `g$` |
| line         | `j`  | `k`  | `0`   |       | `$`  |
| paragraph    | `}`  | `{`  |       |       |      |
| screen       |      |      | `H`   | `M`   | `L`  |
| file         |      |      | `gg`  | `50%` | `G`  |

|             | next    | prev    | start | mid  | end  |
| ----------- | ------- | ------- | ----- | ---- | ---- |
| line        | `<C-e>` | `<C-y>` |       |      |      |
| half screen | `<C-d>` | `<C-u>` |       |      |      |
| screen      | `<C-f>` | `<C-b>` | `zb`  | `zz` | `zt` |

## Text Object

|               | _in_ &bull; _inner_              | _all_ &bull; _around_            |
| ------------- | -------------------------------- | -------------------------------- |
| _word_        | `iw`                             | `aw`                             |
| _Word_        | `iW`                             | `aW`                             |
| _sentence_    | `is`                             | `as`                             |
| _paragraph_   | `ip`                             | `ap`                             |
| `<>` _tag_    | `it`                             | `at`                             |
| `()` _braces_ | `ib` &bull; `i(` &bull; `i)`     | `ab` &bull; `a(` &bull; `a)`     |
| `{}` _Braces_ | `iB` &bull; `i{` &bull; `i}`     | `aB` &bull; `a{` &bull; `a}`     |
| `` "'` ``     | `i"` &bull; `i'` &bull; `` i` `` | `a"` &bull; `a'` &bull; `` a` `` |
| `[]`          | `i[` &bull; `i]`                 | `a[` &bull; `a]`                 |
| `<>`          | `i<` &bull; `i>`                 | `a<` &bull; `a>`                 |

## Macro

- `q`**m** &mdash; start recording [[vim#macro]] **m**
- `q` &mdash; stop recording [[vim#macro]]
- `@`**m** &mdash; play back [[vim#macro]] **m**
- `@@` &mdash; repeat last [[vim#macro]] playback
- `Q` &mdash; play back last recorded [[vim#macro]]

## Search

- `cgn` &mdash; change next [[vim#search]] match
- `dgn` &mdash; delete next [[vim#search]] match

|                              | forward    | backward   | next | prev |
| ---------------------------- | ---------- | ---------- | ---- | ---- |
| search string **str**        | `/`**str** | `?`**str** | `n`  | `N`  |
| search word                  | `*`        | `#`        | `n`  | `N`  |
| find _first_ character **c** | `f`**c**   | `F`**c**   | `;`  | `,`  |
| find _upto_ character **c**  | `t`**c**   | `T`**c**   | `;`  | `,`  |

## Mark

- `m`**m** &mdash; set local [[vim#mark]] **m**
- `m`**M** &mdash; set global [[vim#mark]] **M**

## Compound

- `ea` &mdash; insert after word
- `Ea` &mdash; insert after Word
- `0w` &mdash; first non-blank character of line
- `Jx` &mdash; join lines without a space
- `Jde` &mdash; join lines removing leading characters
- `xp` &mdash; swap character with next
- `ddp` &mdash; swap current line with next
- `r<cr>` &mdash; split line at cursor

## Miscellanous

- `<C-g>` &bull; `g<C-g>` &mdash; show some buffer info
- `gv` &mdash; re-select last _visual_ selection
- `gf` &mdash; open _file_ under cursor
- `gd` &mdash; jump to local _definition_ under cursor
- `gD` &mdash; jump to global _declaration_ under cursor
- `:!`**cmd** &mdash; run shell command **cmd**
- `!!`**cmd** &mdash; run shell command **cmd** on current line
