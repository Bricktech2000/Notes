# Forth

_the LISP of low-level programming_

> **resource** _Fitting a Forth in 512 bytes_, bootstrapping using Forth --- <https://compilercrim.es/bootstrap/miniforth/> and <https://compilercrim.es/bootstrap/branches/>

> **resource** _JONESFORTH_, literate Forth implementation in x86 assembly --- [[jonesforth.f]] and [[jonesforth.S]] --- <https://github.com/nornagon/jonesforth/blob/master/jonesforth.S> and <https://github.com/nornagon/jonesforth/blob/master/jonesforth.f>

[[forth]] is a concatenative [[programming language]] that compiles words to threaded code running on a stack machine

the [[forth]] _dictionary_ is a [[linked list]] of entries whose structure resembles the following:

```c
struct word {
  struct word *link; // next entry in dictionary linked list
  bool immed  : 1;   // if true, execute word even in compile mode
  bool _pad   : 1;   // padding so `len` and flags fit in an 8-bit byte
  bool hidden : 1;   // if true, ignore word during dictionary lookup
  uint8_t len : 5;   // length of word name
  char name[len];    // word name for dictionary lookup
  void (*interp)();  // pointer to an interpreter function for this word
  void *defn[];      // array of pointers to codewords forming this word
}
```

words defined within [[forth]] have their `w.interp = DOCOL`, an interpreter function that pushes the address of the next codeword in line to the _return stack_ then jumps to the first codeword in `w.defn` by calling `NEXT`, and have their `w.defn` end in `EXIT`, a codeword that pops a return address from the _return stack_ then jumps to it

primitive words can be written in assembly by storing their machine code directly in `w.defn` and setting their `w.interp = w.defn`. primitive words generally have their `w.defn` end in `NEXT`, a codeword that advances the instruction pointer to the next codeword in line then jumps to it

`STATE` is a word that pushes to the _parameter stack_ a pointer to a global flag that determines whether [[forth]] is in _compile mode_ `1`, where words are compiled into the current definition, or in _immediate mode_ `0`, where words are executed immediately

`IMMEDIATE` toggles the `w.immediate` flag of the latest word in the dictionary. immediate words get executed even in compile mode, effectively allowing the programmer to extend the compiler environment

> **example** `: [ 0 STATE ! ; IMMEDIATE : ] 1 STATE ! ; IMMEDIATE`

immediate words can use the parameter stack to store temporaries transparently **because they run at compile time**

> **example** `BEGIN` pushes the current address onto the parameter stack later to be consumed by `UNTIL` or `AGAIN`. despite this, `BEGIN` becomes transparent at runtime, such as with `0 BEGIN . 1 + DUP 10 < UNTIL`

`HIDE FOO` toggles the `w.hidden` flag of word `FOO` in the dictionary. hidden words are ignored during dictionary lookup, enabling the definition of "private" words

> **example** `: SUB ... ; : MAIN ... SUB ... ; HIDE SUB`

words `[` and `]` switch in and out of immediate mode, respectively, allowing for compile-time evaluation

> **example** `[ 3 4 * ]` within a `: ... ;` definition will codegen `12` and not a runtime call to `*`

> **note** [[forth]] lets you tickle the compiler and poke right through all [[abstraction]] layers down to machine code. on one hand, this makes bootstrapping and metaprogramming a breeze. on the other, you can find yourself in pragmatism hell wondering if you've covered all edge cases in an implementation that really should've been trivial; see, for example, [[jonesforth.f|jonesforth.f:1022-1107]], <https://github.com/nornagon/jonesforth/blob/d97a25bb0b06fb58da1975eac291f45618fd2ada/jonesforth.f#L1022-L1107>
