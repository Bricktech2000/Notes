# 🅲🅾🅽🆅🅴🅽🆃🅸🅾🅽🆂

see [[matrix]] and [[complex]] for examples of [[conventions]]

## markup

- [[markdown]] is used **exclusively** semantically; a [[markdown]] element is never to be used for styling purposes
- custom [[markdown]] syntax, `` **`...`** ``, is used for all mathematical equations through my custom [[math notation]]
- [[variable]]s in equations are defined in separate lines using a `, where` statement followed by a [[markdown]] list
- [[international system of units]] units and chemical elements in equations are to be written within `"`. a space is to be added before a unit
- italics indicate "as-is" text (formal terms, direct quotations, titles of works...) and are used for "taglines" (easy-to-remember one-line summaries of a section)
- bold indicates emphasis; italics are not to be used for emphasis
- quotation marks indicate non-standard or informal usage of a word or phrase; quotation marks are not to be used for direct quotations
- `&mdash; ...` statements are used for citing sources
- HTML entities `&...;` are used for any non-[[ascii]] [[character]]s, such as &lambda; and &times; and &rarr;
- all internal links are denoted using `[[note]]` and `![[image.png]]` [[wikilink]]s, and all external links are denoted using `<https://example.com/>`. bare URLs are to be avoided

italics are used for informal and opinionated statements, and literal aoenuatosenuth #todo. [[trick]]s and personal definitions and to replace quotation marks

## headings

- title-case headings are for [[concept]]s that can be linked to using [[wikilink#anchor wikilink]]s and lowercease headings are for general titles

- some constructs, such as definitions and proofs, are very common. they are to be written as follows in [[markdown]]:

  ```md
  > **proof** _proof name_ this is an example of a proof used in a blockquote

  **definition** _definition name_ this is an example of a definition used inline
  ```

  the following headings are used in blockquotes:

  - **note**
  - **example**
  - **proof**
  - **procedure**
  - **equivalence**

  the following headings are used inline:

  - **see**
  - **aka**
  - **types**
  - **theorem**
  - **definition**
  - **properties**
  - **applications**
  - **tradeoffs**
  - **representation**
  - **examples**
  - **procedures**

## note system

- [[wikilink]]s are generally avoided in headings
- a page can link to itself
- most [[fact]]s, opinions and judgements are accompanied by their source and not just stated as an absolute truth
- note names are reduced to their simplest form. they are mostly singular nominal groups, and sometimes adjectives when more appropriate. diacritics are removed from them
- file names are lowercase. diacritics are removed from them
- line breaks are used exclusively for how they look in the render and never to make the [[markdown]] source more readable (which is why almost no single line breaks are used)
- horizontal rules are occasionally used to separate a whole file in different sections
- each page has one title-case first-level heading, which must correspond to the file name. occasional subsequent first-level headings must be preceded by a horizontal rule
- box titles such as that of the [[conventions]] page are generated using <https://lingojam.com/BoldTextGenerator>
- "lax" syntax and punctuation is used; that is,
  - the first word of a sentence is not capilatized
  - full stops seperate sentences; they do not end them

## syntax used

> # h1
>
> ## h2
>
> ### h3
>
> #### h4
>
> _italicized text_
>
> **bold text**
>
> `inline code`
>
> ```rust
> // code block
> println!("-> with ligatures <-");
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
> **`"equation"`**
>
> #tag
>
> [[wikilink]]
>
> <https://example.com/>
>
> ![[2022-03-19-00-57-20.png]]
>
> ```mermaid
> graph LR
>   A(mermaid) --> B(support)
> ```
>
> > blockquote
>
> | simple | table |
> | ------ | ----- |
> | 0      | foo   |
> | 1      | bar   |
> | 2      | baz   |
>
> ---
>
> horizontal rule

## unused syntax

> $\LaTeX$
>
> $$
> \text{Block } \LaTeX
> $$
>
> emoji :smile:
>
> [[wikilink|wikilink alias]]

## other

the [[graph]] in [[index]] is generated on Obsidian using the following settings:

```yaml
# if a property is not specified below,
# it is to be set to its default value

filters:
  tags: no
  attachments: no
  exisiting files only: no
  orphans: yes
groups:
  - query: '[[math notation]]'
    color: '#ffffff'
display:
  arrows: yes
forces:
  center force: 0.32
```

a screenshot of the [[graph]] is then taken using Obsidian's _Copy screenshot_ feature
