# 🅲🅾🅽🆅🅴🅽🆃🅸🅾🅽🆂

## general conventions

### LaTeX

LaTeX is used for all mathematical equations through my custom [[math-notation]]

[[variable]]s are defined in separate lines using a _, where_ statement

whitespace in formulas follow programming-language-like conventions

[[international-system-of-units]] units and other units are to be written using `\text{}`

the $\ : $ [[operator]] must always be surrounded one space on either side, or written as the first character of an equation as `$\ : $`

the $\rightarrow$ [[operator]] is written as `\to` by default, and must be written as `\rightarrow` when it indicates a [[math-notation]] [[function]] definition

`\R`, `\N`, `\Z`, `\{` and `\}` must not be used, as they are not widely supported. `\mathbb R`, `\mathbb N`, `\mathbb Z`, `\lbrace` and `\rbrace` should be used instead, respectively.

`\\` must be replaced by `\\\` for them to work properly. see the following discussion: <https://github.com/mathjax/MathJax/issues/1301>

more information about supported features available at: <https://katex.org/docs/supported.html>

### headings

capitalized headings are for [[concept]]s

lowercease headings are for general titles

the following headings are commonly used:

- **definition**
- **notation**
- **representation**
- **types**
- **applications**
- **example**
- **counterexample**
- **theorems**
- **definitions**
- **properties**
- **procedure**
- **pros & cons**
- **see**

headers still in new:

- **types**
- **examples** (#todo rename, should represent "children" and not examples)

blockquotes added in new:

- **usage**
- **constant**
- **representation**
- **types**

---

- procedure
- notes
- example
- proof

&nbsp;

- theorem
- definition
- types

#todo use period when latex not parsing

### quotes, italics, bold, sources, URLs

blockquotes are used for [[fact]]ual information and definitions

italics are used for tricks and personal definitions and to replace quotation marks. bold is used for emphasis. italics must not be used for emphasis and quotation marks are to be avoided

_&mdash; ..._ statements are used for citing sources

all external URLs are denoted using _<...>_ statements

### note system

wiki links are generally avoided in headings

a page can link to itself

_see ..._ statements are for prerequisites

note names are mostly _-ing_ verbal groups or singular nominal groups, and sometimes adjectives when necessary

line breaks are used exclusively for how they look in the render and never to make the source code more readable (which is why almost no single line breaks are used)

horizontal rules are occasionally used to separate a whole file in different sections

each page has one title case first-level heading, which must correspond to the file name. occasional subsequent first-level headings must be preceded by a horizontal rule

in file names, spaces are replaced by [[dash]]es and apostrophes and diacritics are removed

box titles are generated with <https://lingojam.com/BoldTextGenerator>

all internal links are denoted using `[[note]]` and `![[image.png]]`, and all external links are denoted using `<https://example.com/>`

### note, theorem, proof, definition

all constructs below can be multiline

> **note**: this is a note to clarify the previous statement

> **theorem**: this is a theorem &mdash; this is an optional source

> **theorem**: _theorem name_
>
> this is a theorem &mdash; this is an optional source

> **proof**: this is a proof of the above theorem &mdash; this is an optional source

> **proof**: &mdash; this is a source

> **definition**: _term_ is a term that is defined here &mdash; this is an optional source

> **AKA**: this is a list of synonyms for a concept, "also known as"

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
> $\LaTeX$
>
> #tag
>
> [[index|wiki-link]]
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

### unused syntax

> $$
> \text{Block } \LaTeX
> $$
>
> emojis :smile:
>
> - [ ] task
> - [x] list
>
> ---
>
> horizontal rule

## PDF export conventions

see [[matrix]] for an example application of report-style PDF export conventions

the following scripts are to be appended to any page before it is exported

<!-- see `settings.json` for sources -->

```txt
<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
```

## report-style PDF export conventions

see [[eng1112-report-2]] for an example application of report-style PDF export conventions

the following stylesheet is to be appended to any report-style document

```txt
<style> p { text-indent: 40px; } blockquote > p { text-indent: 0; } hr { opacity: 0; page-break-after: always; } cite { display: inline-block; text-indent: -40px; margin-top: 1rem; font-style: inherit; text-align: justify; } </style>
```

### syntax used

> ---
>
> horizontal rules act as page breaks

paragraphs have their first line indented &mdash; lorem ipsum dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

<cite>citations have all but their first line indented &mdash; lorem ipsum dolor sit amet, consectetur adipiscing elit. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</cite>

### unused syntax

> <div class="theorem">This is a theorem.</div>
> <div class="lemma">This is a lemma.</div>
> <div class="definition">This is a definition.</div>
> <div class="proof">This is a proof.</div>

## presentation-style note conventions

see [[vim-talk]] and [[carbon-language-talk]] for example applications of presentation-style note conventions

presentation-style notes are viewed using Obisdian's _Start presentation_ feature

slides are seperated by using horizontal rules, `---`

headings and content can optionally be seperated using an HTML line break, `<br>`

personal comments and notes are to be written between `<?` and `?>` tags, and not between `<!--` and `-->` tags

level-3 headings are not used as they look too similar to level-2 headings on Obsidian. there can be multiple level-1 headings in one presentation

<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
