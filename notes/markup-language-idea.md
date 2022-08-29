# Markup Language Idea

this [[markup-language-idea]] is meant to address the main issue with Markdown in my opinion: inconsistency.

in this [[programming-language]],

- most constructs have a clear semantic meaning
- most constructs have block-level and inline equivalents
- every control character can be escaped with a `\`, with no ambiguous exceptions
- constructs can be nested, and in a way that is actually consistent

---

# Constructs

## semantic constructs

`#` represents a section of a file (not a heading)

`|` represents content that was sourced somewhere else

`-` represents a set of items

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

# tables
  / TODO: find better syntax for tables

  | header 1  header   |
              number 2
  | ------------------ |
  | data 1    data 2   |
    data 1.1   data 2.1
  | data 3    data 4   |

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

with my conceptual\ notes <conceptual-note-taking>

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

### representation

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

with my [conceptual notes](conceptual-note-taking)

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
