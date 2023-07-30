# Better Markdown

this [[better markdown]] idea is meant to address the main issue with [[markdown]] in my opinion: inconsistency

in [[better markdown]],

- most constructs have a clear semantic meaning
- most constructs have block-level and inline equivalents
- every markup [[character]] can be escaped with a `\`, with no ambiguous exceptions
- constructs can be nested, and in a way that is actually consistent

_a [[markdown]]-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions_ &mdash; <https://daringfireball.net/projects/markdown/syntax>. this is not a goal of [[better markdown]]. [[better markdown]] aims to be a consistent, extensible, formally-defined, light-weight markup language

## things to iron out

#think

- syntax for:
  - tables
  - checkboxes
  - tags
  - dates
  - keyboard shortcuts
  - currencies
  - inserted text
  - deleted text
  - emoji
  - admonitions aka call-outs
  - ...
- support for running code blocks and parsing their `stdout` as markup
- support for graphs and plots

other things to think about:

- `\` for preformatted blocks?
  ```
  \ pre block maybe?
  ```
- `#` and `` ` `` contain "metadata" (heading content and [[programming language]] name). do we want that?
- `<` and `>` work differently from the rest of the syntax. probably want to fix that
- probably want to remove `###`
- probably want to remove `$`
- `~` for removed text and strikethrough, `+` for inserted text and underline?
- what if lists had "metadata" for whether they are checked, which would be displayed as a checkbox? what if links had "metadata" to replace the link text?
- `!` with metadata for admonitions aka call-outs?
- what about `:` for metadata:
  - `! note: this is a note`
  - `! warning: this is a warning`
  - `! theorem: this is a theorem`
  - `- _: todo`
  - `- x: done`
  - `- o: in progress`
  - `` ` rust: println!("hello world") ``
  - `# Heading: content`
- non-[[ascii]] characters such as &times; and &mdash;
- inline lists can be repeated `-a-b-c` but not other constructs

## &mdash;

&mdash; <https://textile-lang.com/>

&mdash; <https://github.com/BradSharp/Remark>

&mdash; <https://docs.asciidoctor.org/asciidoc/latest/syntax-quick-reference/>

&mdash; <http://tantek.pbworks.com/w/page/59905776/Markdown>

&mdash; <https://squidfunk.github.io/mkdocs-material/reference/admonitions/>

---

# constructs

## semantic constructs

`#` represents a section of a file (not a heading)

`|` represents content that was sourced somewhere else

`-` represents a [[set]] or [[list]] of items

`>` and `<>` represent external files

`*` represents an important or emphasized item

`_` replaces quotation marks when mentioning something

`` ` `` represents computer code

`###` represents a file-wide separation (not a horizontal rule)

## not-so-semantic constructs

`/` is used for comments

`$` is used for LaTeX mathematical equations

`\` is used for escaping control characters

## block-level examples

```
first paragraph
second line

second paragraph

third paragraph
second line
third line

# headings
  # name of section
    content of section
    continuation of content

# quotes
  | quote
    second line
    third line
  | second quote
  | third quote

# lists
  - first item
  - second item
  - third item
    second ine

# includes
  > filename.incl

# other
  * bold
    text block
  _ italicized
    block
  ` language
    code block
  $ \text{block}
    \LaTeX

  / block comment
    second line
    third line
```

## inline examples

```
|quote|

###

-list-

*bold*

_italics_

`code`

/inline comment/

$\LaTeX$

<filename.link>
```

## nesting examples

### source code

```
| quote
  | nested quote
  # heading in quote
  - list item 1
  - list item 2

- first, a quote:
  | quote in a list
- then, some code:
  ` rust
    if true {
      println!("true");
    }

if you're interested, click here! <https://example.com/>

with my conceptual\ notes <index>

this person said that |it wasn't fair|

he wrote the following:
| This is \*\*very\*\* important.
  so important that I escaped the asterisks

so that's how it happened /comment: rephrase this/

supported languages include -HTML-Markdown-LaTeX-.

| * theorem
  it is a theorem that $x = y$

| * note
  this theorem only works for certain values of $x$
  therefore, some values of $y$ are not possible

this is _hello world_ in Python:
` python
  # hello_world.py
  print("hello world")
you can run it with `python hello_world.py`
```

### result

> quote
>
> > nested quote
>
> ### heading inside quote
>
> - list item 1
> - list item 2

- first, a quote:
  > quote in a list
- then, some code:
  ```rust
  if true {
    println!("true");
  }
  ```

if you're interested, click [here!](https://example.com/)

with my [conceptual notes](index)

this person said that _"it wasn't fair"_

he wrote the following:

> This is \*\*very\*\* important.
>
> so important that I escaped the asterisks

so that's how it happened <!-- comment: rephrase this -->

supported languages include HTML &bull; Markdown &bull; LaTeX.

> **theorem**
>
> it is a theorem that $x = y$

> **note**
>
> this theorem only works for certain values of $x$
> therefore, some values of $y$ are not possible

this is _hello world_ in Python:

```python
# hello_world.py
print("hello world")
```

you can run it with `python hello_world.py`
