# 🅲🅾🅽🆅🅴🅽🆃🅸🅾🅽🆂

## general conventions

see [[matrix]] and [[complex]] for examples of general conventions

### LaTeX

LaTeX is used for all mathematical equations through my custom [[math notation]]

[[variable]]s are defined in separate lines using a _, where_ statement followed by a list

whitespace in formulas follow [[programming language]]-like conventions

[[international system of units]] units and other units are to be written using `\text{}`

the $\, : \,$ [[operator]] must always be surrounded one space on either side, or written as the first or last character of an equation as `$\, : \,$`

the $\rightarrow$ [[operator]] is written as `\to` by default, and must be written as `\rightarrow` when it indicates a [[math notation]] [[function]] definition

when using the [[reduce function]] in my [[math notation]], the [[operator]] must be followed by a `\! `

`\R`, `\N`, `\Z`, `\{` and `\}` must not be used, as they are not widely supported. `\mathbb R`, `\mathbb N`, `\mathbb Z`, `\lbrace` and `\rbrace` should be used instead, respectively.

`\\` must be replaced by `\\\` for them to work properly. see the following discussion: <https://github.com/mathjax/MathJax/issues/1301>

more information about supported features available at <https://katex.org/docs/supported.html>

### Sections

capitalized headings are for [[concept]]s that can be linked to using `[[nested#wiki links]]` and lowercease headings are for general titles

some constructs, such as definitions and proofs, are very common. they are to be written as follows in markdown:

```md
> **proof** _proof name_ this is an example of a proof used in a blockquote

**definition** _definition name_ this is an example of a definition used inline
```

and they are rendered as follows:

> **proof** _proof name_ this is an example of a proof used in a blockquote

**definition** _definition name_ this is an example of a definition used inline

the following headings are used in blockquotes:

- **note**
- **example**
- **procedure**
- **proof**
- **[[mnemonic]]**
- **constant**
- **equivalence**
- **aka**

the following headings are used inline:

- **see**
- **types**
- **theorem**
- **definition**
- **properties**
- **applications**
- **pros**
- **cons**
- **pros & cons**
- **representation**
- **examples**
- **procedures**

### italics, bold, sources

italics are used for [[trick]]s and personal definitions and to replace quotation marks

bold is used for emphasis &mdash; italics must not be used for emphasis

`&mdash; ...` statements are used for citing sources

### note system

wiki links are generally avoided in headings

a page can link to itself

note names are mostly _-ing_ verbal groups or singular nominal groups, and sometimes adjectives when more appropriate

line breaks are used exclusively for how they look in the render and never to make the source code more readable (which is why almost no single line breaks are used)

horizontal rules are occasionally used to separate a whole file in different sections

each page has one title-case first-level heading, which must correspond to the file name. occasional subsequent first-level headings must be preceded by a horizontal rule

file names are all lowercase and apostrophes and diacritics are removed from them

box titles are generated with <https://lingojam.com/BoldTextGenerator>

all internal links are denoted using `[[note]]` and `![[image.png]]`, and all external links are denoted using `<https://example.com/>`

### syntax used

> # h1
>
> ## h2
>
> ### h3
>
> _italics_
>
> **bold**
>
> `inline code`
>
> ```javascript
> // code block
> console.log(() => 'Fira Code Ligatures');
> ```
>
> - unordered
> - list
>
> 1. ordered
> 2. list
>
> - [ ] task
> - [x] list
>
> $\LaTeX$
>
> #tag
>
> [[index|wiki links]]
>
> <https://example.com/>
>
> ![[2022-03-19-00-57-20.png]]
>
> ```mermaid
> graph LR
> mermaid --> support
> ```
>
> > blockquote
>
> | table |     |
> | ----- | --- |
> | 1     |     |
> | 2     |     |
> | 3     |     |
>
> ---
>
> horizontal rule

### unused syntax

> $$
> \text{Block } \LaTeX
> $$
>
> emojis :smile:

## presentation-style conventions

see [[vim talk]] and [[carbon language talk]] for examples of presentation-style conventions

presentation-style notes are viewed using Obisdian's _Start presentation_ feature

slides are seperated by using horizontal rules, `---`

headings and content can optionally be seperated using an HTML line break, `<br>`

personal comments and notes are to be written between `<?` and `?>` tags, and not between `<!--` and `-->` tags

level-3 headings are not used as they look too similar to level-2 headings on Obsidian. there can be multiple level-1 headings in one presentation
