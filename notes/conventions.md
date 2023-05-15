# 🅲🅾🅽🆅🅴🅽🆃🅸🅾🅽🆂

## general conventions

see [[matrix]] and [[complex]] for examples of general conventions

### markup

- [[markdown]] is used **excllusively** semantically; a [[markdown]] element should never be used for styling purposes
- custom [[markdown]] syntax, `` **`...`** ``, is used for all mathematical equations through my custom [[math notation]]
- [[variable]]s in equations are defined in separate lines using a `, where` statement followed by a [[markdown]] list
- [[international system of units]] units and chemical elements are to be written within `"`. a space is to be added before a unit
- italics are used for [[trick]]s and personal definitions and to replace quotation marks
- bold is used for emphasis; italics are not to be used for emphasis
- `&mdash; ...` statements are used for citing sources
- HTML entities `&...;` are used for any non-[[ascii]] [[character]]s, such as &lambda; and &times;
- all internal links are denoted using `[[note]]` and `![[image.png]]` [[wikilink]]s, and all external links are denoted using `<https://example.com/>`. bare URLs are to be avoided

### sections

- title-case headings are for [[concept]]s that can be linked to using [[wikilink#nested wikilink]]s and lowercease headings are for general titles

- some constructs, such as definitions and proofs, are very common. they are to be written as follows in [[markdown]]:

  ```md
  > **proof** _proof name_ this is an example of a proof used in a blockquote

  **definition** _definition name_ this is an example of a definition used inline
  ```

  the following headings are used in blockquotes:

  - **note**
  - **example**
  - **procedure**
  - **proof**
  - **[[mnemonic]]**
  - **constant**
  - **equivalence**

  the following headings are used inline:

  - **see**
  - **aka**
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

### note system

- [[wikilink]]s are generally avoided in headings
- a page can link to itself
- note names are mostly singular nominal groups, and sometimes adjectives when more appropriate. diacritics are removed from them
- file names are lowercase. diacritics are removed from them
- line breaks are used exclusively for how they look in the render and never to make the [[markdown]] source more readable (which is why almost no single line breaks are used)
- horizontal rules are occasionally used to separate a whole file in different sections
- each page has one title-case first-level heading, which must correspond to the file name. occasional subsequent first-level headings must be preceded by a horizontal rule
- box titles such as that of the [[conventions]] page are generated using <https://lingojam.com/BoldTextGenerator>
- "lax syntax and punctuation" is used; that is,
  - the first word of a sentence does not have to be capilatized
  - full stops seperate sentences; they do not end them

### syntax used

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

### unused syntax

> $\LaTeX$
>
> $$
> \text{Block } \LaTeX
> $$
>
> emoji :smile:
>
> [[wikilink|wikilink alias]]

## presentation-style conventions

see [[vim talk]] and [[carbon language talk]] for examples of presentation-style conventions

presentation-style notes are viewed using Obisdian's _Start presentation_ feature

### markup

- [[markdown]] is used non-semantically for styling purposes
- slides are seperated by using horizontal rules, `---`
- headings and content can optionally be seperated using an HTML line break, `<br />`
- personal comments and notes are to be written between `<!--` and `-->` tags

### note system

- level-3 headings are not used as they look too similar to level-2 headings on Obsidian. there may be multiple level-1 headings in one presentation

## other conventions

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
