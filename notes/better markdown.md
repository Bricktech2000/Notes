# Better Markdown

this [[better markdown]] idea is meant to address the main shortcoming of [[markdown]] in my opinion: inconsistency. formal markup doesn't have to be verbose and lightweight markup doesn't have to be informal; see also RFC 7764, $1.1 'On Formats' <https://www.rfc-editor.org/rfc/rfc7764.html#section-1.1>. [[markdown]] is human-first while [[better markdown]] is machine-first

in [[better markdown]],

- constructs have a clear semantic meaning
- constructs have block and inline equivalents
- every meta[[character]] can be escaped with a `\`, with no ambiguous exceptions
- constructs can be nested, and in a way that is actually consistent

_a [[markdown]]-formatted document should be publishable as-is, as plain text, without looking like it's been marked up with tags or formatting instructions_ --- <https://daringfireball.net/projects/markdown/syntax>. this is not a goal of [[better markdown]]. [[better markdown]] aims to be a consistent, extensible, formally-defined, lightweight markup language

## syntax

#todo complete

#xxx look into <https://github.com/nvim-neorg/norg-specs/blob/main/1.0-specification.norg>

#todo rewrite everything above (and excluding) `<block-specifier>` as none of it makes much sense

```bnf
<document> ::= <block-element>*

<block-element> ::= <block-specifier>* <element-metadata>? <inline-element>
<block-specifier> ::= <control-character> <space-character>
<element-metadata> ::= <character-unit>* <metadata-character> <space-character>

<inline-element> ::= TODO

<character-unit> ::= <escape-sequence> | <unicode-character>
<escape-sequence> ::= <escape-character> (<control-character> | <space-character> | <escape-character> | <metadata-character> | <unicode-name> | <entity-name> | <emoji-name>)
<unicode-name> ::= TODO
<entity-name> ::= TODO
<emoji-name> ::= TODO

<control-character> ::= "#" | "|" | "-" | "=" | "<" | ">" | "[" | "]" | "!" | "*" | "`" | "/" | "+" | "~" | "$"
<space-character> ::= " " | "\t"
<escape-character> ::= "\"
<newline-character> ::= "\n"
<metadata-character> ::= ":"
```

#xxx

- syntax for:
  - N-dimensional tables
  - tags
  - dates `date`
  - keyboard keys `kbd`
  - emoji
  - images
  - ~~subscript `sub`~~
  - ~~superscript `sup`~~
  - paragraphs `p`
  - ...
  - non-[[ascii]] characters such as × and —
- support for running code blocks and parsing their `stdout` as markup
- support for graphs and plots
- do we really want double newlines to be paragraphs?
- do we really want single newlines to be line breaks?
- formalize grammar for inline constructs. inline constructs should be surrounded by either whitespace or other inline constructs
  - what about plural with inline code? i.e. `Object`s
- `<>` and `[]` work differently from rest of syntax (instead of one character, uses two "reflected" ones). do we want this?
- what is the inline equivalent of `#`? what are the block equivalent of `[]` and `<>`?

## ---

--- <https://textile-lang.com/>

--- <https://github.com/BradSharp/Remark>

--- <https://docs.asciidoctor.org/asciidoc/latest/syntax-quick-reference/>

--- <http://tantek.pbworks.com/w/page/59905776/Markdown>

--- <https://squidfunk.github.io/mkdocs-material/reference/admonitions/>

--- <https://developer.mozilla.org/en-US/docs/Web/HTML/Element>

--- <https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=all>

---

# constructs

`#` represents a document section

`|` represents a direct quotation

`-` represents a [[set]] of items

`=` represents a [[list]] of items

`<>` represents a link

`[]` represents a citation

`!` represents an admonition

`*` represents emphasis

`` ` `` represents computer code

`/` represents temporary content

`+` represents inserted content

`~` represents removed content

`$` represents mathematical content

## examples

```
first paragraph
second line

second paragraph

third paragraph
second line
third line

# name of section:
  content of section
  continuation of content

| quote
  second line
  third line
| second quote
| third quote

- some item
- some item
- some item
  second ine
= first item
= second item
= third item
  second line

* emphasis
  block
` code
  block
$ \text{block}
  \LaTeX
/ block comment
  second line
  third line
+ inserted
  content
  block
~ deleted
  content
  block

|direct quote|
-set item-
=list item=
*emphasis*
`computer code`
/inline comment/
$\LaTeX$
<https://example.com/>
+inserted text+
~deleted text~
```

## source

```
| quote
  | nested quote
  # section in quote:
    - some item
    - some item

= first, a quote:
  | quote in a list
= then, some code:
  ` rust:
    if true {
      println!("true");
    }

if you're interested, click <here: https://example.com/>!

with my <conceptual notes: index>

this person said |it isn't fair| [the person]

he wrote the following:
| This is \*very\* important.
  *so important* that I escaped the asterisks

~rambling is the state of rambles which are rambling in a rambling manner~ +rambling is wordy+.

so that's how it happened /you should rephrase this/

supported languages include -HTML--Markdown--LaTeX-.

the main steps are =preparation==execution==analysis==conclusion=.

! theorem:
  it is a theorem that $x = y$

! note:
  this theorem only works for certain values of $x$
  therefore, some values of $y$ are not possible

- _: this is to be done
- x: this is done

this is |hello world| in Python:
` python:
  # hello_world.py
  print("hello world")
you can run it with `python hello_world.py`
```

## result

<blockquote>
  quote<br />
  <blockquote>
    nested quote<br />
    <h4>section in quote</h4>
    <ul>
      <li>some item</li>
      <li>some item</li>
    </ul>
  </blockquote>
</blockquote>

<ol>
  <li>
    first, a quote:
    <blockquote>quote in a list</blockquote>
  </li>
  <li>
    then, some code:
    <pre><code class="language-rust">if true {
  println!("true");
}</code></pre>
  </li>
</ol>

<p>if you're interested, click <a href="https://example.com/">here</a>!</p>

<p>with my <a href="index">conceptual notes</a></p>

<p>
  this person said <i><q>it isn't fair</q></i>
  &mdash; the person&ensp;
</p>

<p>he wrote the following:</p>

<blockquote>
  This is *very* important. <br />
  <b>so important</b> that I escaped the asterisks
</blockquote>

<p>
  <del>
    rambling is the state of rambles which are rambling in a rambling manner
  </del>
  <ins>rambling is wordy</ins>.
</p>

<p>
  so that's how it happened
  <u style="text-decoration: underline dashed">you should rephrase this</u>
</p>

<p>supported languages include&ensp;HTML &bull; Markdown &bull; LaTeX&ensp;.</p>

<p>
  the main steps are&ensp;preparation &blacktriangleright; execution
  &blacktriangleright; analysis &blacktriangleright; conclusion&ensp;.
</p>

<blockquote>
  <b>theorem</b>
  <p>it is a theorem that <span class="math inline">x = y</span></p>
</blockquote>

<blockquote>
  <b>note</b>
  <p>
    this theorem only works for certain values of
    <span class="math inline">x</span><br />
    therefore, some values of <span class="math inline">y</span> are not
    possible
  </p>
</blockquote>

<p>
  <input type="checkbox" disabled />this is to be done<br />
  <input type="checkbox" checked disabled />this is done
</p>

<p>
  this is <i><q>hello world</q></i> in Python:
</p>

<pre><code class="language-python"># hello_world.py
print("hello world")
</code></pre>

<p>you can run it with <code>python hello_world.py</code></p>
