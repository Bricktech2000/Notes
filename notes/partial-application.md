# Partial Application

see [[functional-programming]], [[currying]]

> **Partial Application** is the action of applying only part of a [[function]]'s arguments to produce a new [[function]] that takes the remaining arguments

## example

```F#
let hello = printfn "Hello, %s"
let names = ["John", "Jane", "Mary"]

names
|> List.map hello
```

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" })</script>
<script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([A-Za-z\-]+)\]\]/g, (a, b, c) => `<u style="text-transform: capitalize;">${c.replace(/\-/g, ' ')}</u>`)</script>
