# Quine

_a program that outputs its own listing_

> **resource** the "de facto" [[quine]] quickstart by David Madore --- [[quine.html]] --- <http://www.madore.org/~david/computers/quine.html>

[[quine]]s are not the result of language-specific hacks; they exist, up to practical interpretation of program output, in every [[turing complete]] [[programming language]] for which there exists a total computable [[function]] that maps programs to their listings, as follows from the _fixed-point theorem_

> **example**
>
> [[quine]]s may not exist in the following [[turing complete]] [[programming language]] because mapping programs to their listings is undecideable as follows from form the [[halting problem]]
>
> ```python
> from brainfuck import bf # assumed to be Turing complete
>
> def eval(program, input):
>   fst, *snd = program.split('!', 1) #*
>   # make this language Turing complete
>   if input:
>     return bf(fst, input)
>   # if the input is empty, either return a hard-coded
>   # output or hang. the halting problem is undecideable
>   # and thus so is mapping programs to their listings
>   # in this language
>   if snd:
>     return snd[0]
>   while True:
>     pass
> ```
>
> --- me --- <https://stackoverflow.com/questions/2568020/is-it-possible-to-create-a-quine-in-every-turing-complete-language>

**representation** _constructive quine_

```python
intron = '''modify me and this program remains a quine'''
data = '''
quote = "'" * 3
# output a reconstruction of the intron in the format used above
print(f'intron = {quote}{intron}{quote}')
# output a reconstruction of the data in the format used above
print(f'data = {quote}{data}{quote}')
# output the data again as-is to produce the rest of the program
print(data)'''

quote = "'" * 3
# output a reconstruction of the intron in the format used above
print(f'intron = {quote}{intron}{quote}')
# output a reconstruction of the data in the format used above
print(f'data = {quote}{data}{quote}')
# output the data again as-is to produce the rest of the program
print(data)
```

**theorem** _s-m-n theorem_ [[partial application]] on computable [[function]]s is computable and outputs computable [[function]]s

**theorem** _fixed-point theorem_ any total computable [[function]] from programs to programs has a fixed point

> **proof** apply the _s-m-n theorem_ to the structure of the [[combinator#y combinator]] --- <http://www.madore.org/~david/computers/quine.html#sec_fp>.

_The fixed-point theorem has other amusing applications. Essentially, its intuitive (and effective) content is that [...] adding to a programming language the ability for a program to manipulate itself (its source code) does not add to its expressive power._ --- <http://www.madore.org/~david/computers/quine.html#sec_fp>. intuitively, performing β-reduction "running the program" on the [[combinator#y combinator]] gives back the transformation **`f`** applied to the original &lambda;-term (that is, a manipulation of its own source code)

> **note**
>
> _Quines are possible in any Turing-complete programming language, as a direct consequence of Kleene's recursion theorem_ --- <https://en.wikipedia.org/wiki/Quine_(computing)>. I believe this statement may be incorrect
>
> consider the following [[programming language]]. it is clearly [[turing complete]], yet a [[quine]] cannot be written in it
>
> ```python
> from brainfuck import bf # assumed to be Turing complete
>
> def eval(program, input):
>   # make this language Turing complete while ensuring
>   # its output when interpreted in this language will
>   # itself never output anything
>   return bf(program, input).replace('.', '')
> ```

> **note**
>
> _Any programming language which is Turing complete, and which is able to output any string (by a computable function of the string as program [...]) has a quine program [...] as follows by the fixed-point theorem_ --- <https://www.madore.org/~david/computers/quine.html#sec_intro>. I believe this statement may be incorrect
>
> consider the following [[programming language]]. it is clearly [[turing complete]], and the computable [[function]] `lambda s: '0' + s` clearly maps an arbitrary [[string]] to a program that outputs it, yet a [[quine]] cannot be written in it
>
> ```python
> from brainfuck import bf # assumed to be Turing complete
>
> def eval(program, input):
>   if program.startswith('0'):
>     # make this language able to output any string
>     return program[1:] # `program[1:] != program`
>   # make this language Turing complete while ensuring
>   # its output when interpreted in this language will
>   # itself output a string different from its program
>   return '0' + bf(rest, input)
> ```
>
> on another note, _[...] by a computable function of the string as program [...]_ appears redundant because the [[composition#identity]] is computable and therefore by the _s-m-n theorem_ we have that there indeed exists a computable [[function]] that maps any [[string]] to a computable program that outputs that [[string]]

## ---

--- <https://en.wikipedia.org/wiki/Quine_(computing)>

--- <https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem>

--- <https://en.wikipedia.org/wiki/Smn_theorem>

--- <https://cs.stackexchange.com/questions/80837/is-smn-theorem-the-same-concept-as-currying>
