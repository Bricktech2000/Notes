# Combinator

**definition** a _combinator_ is a [[lambda calculus]] expression that refers only to its arguments &mdash; <https://youtu.be/seVSlKazsNk>

**properties**

[[combinator]]s can be manipulated through [[combinatory logic]]

---

## Combinators

### I Combinator

_identity_

**aka** _identity, `id` in Haskell_

**definition** **`I = x -> x = {*}`**

**definition** **`I = S K K`**

**definition** **`I = ii ii`**

**notation** **`{*} x`**

> **equivalence** _[[combinator#i combinator]] and [[composition#identity]]_

### K Combinator

_discards the second argument_

**aka** _constant, `const` in Haskell_

**definition** **`K = f x y -> f x`**

**definition** **`K = ii (ii (ii ii))`**

**notation** **`{->} x y`**

### S Combinator

**aka** _substitution, `<*>` and `ap` in Haskell_

**definition** **`S = f g x -> f x (g x)`**

**definition** **`S = ii (ii (ii (ii ii)))`**

**notation** **`{f g} x`** or equivalently **`{* f g} x`**

### B Combinator

_the [[composition]] of its arguments_

**aka** _compose, `(.)` and `fmap` in Haskell, "bluebird"_

**definition** **`B = f g x -> f (g x)`**

**definition** **`B = S (K S) K`**

**definition** _in [[lambda calculus]]_ $B = \lambda fgx.\ f\ (g\ x)$

**notation** **`(f g *) x`**

> **equivalence** _[[combinator#b combinator]] and [[function]] [[composition]]_

&mdash; <https://youtu.be/SmXB2K_5lcA?t=612>

### B1 Combinator

**aka** _"blackbird", `.:` in Haskell_

**definition** **`B_1 = f g x y -> f (g x y)`**

**definition** **`B_1 = B B B`**

**definition** `.: = (.) . (.)`

**notation** **`(f g * *) x y`**

### C Combinator

_swaps the arguments to a function_

**aka** _flip, `flip` in Haskell_

**definition** **`C = f x y -> f y x`**

**definition** **`C = S (B B S) (K K)`**

**notation** **`rr f x y`**

> **equivalence** _[[combinator#c combinator]] and [[matrix#transpose]]_

### W Combinator

_duplicates the second argument_

**aka** _duplication, 'commute' or 'self' in APL, `join` in Haskell_

**definition** **`W = f x -> f x x`**

**definition** **`W = C S K`**

**notation** **`{f *} x`** or equivalently **`{* f *} x`**

### M Combinator

_applies a [[function]] to itself_

**aka** _mockingbird, **`ww`** combinator_

**definition** **`M = f -> f f`**

**definition** **`M = S I I`**

**notation** **`{* *} f`**

### KI Combinator

_discards the first argument_

**aka** _kite, `const id` in Haskell_

**definition** **`K I = f x y -> f y`**

**notation** **`{->} {*}`**

### T Combinator

_applies the first argument to the second argument_

**aka** _thrush, `&` in Haskell_

**definition** **`T = x f -> f x`**

**definition** **`T = C I`**

### SBI Combinator

_applies a [[function]] twice_

**definition** **`S B I = f x -> f (f x)`**

### Sigma Combinator

**aka** _chain, `=<<` in Haskell, S' combinator_

**definition** **`SS = f g x -> f (g x) x`**

**notation** **`{g f *} x`**

### Psi Combinator

**aka** _`on` in Haskell_

**definition** **`YY = f g x y -> f (g x) (g y)`**

**notation** **`g {x f y}`**

### Phi Combinator

**aka** _converge, `liftA2` and `liftM2` and `phoenix` and `starling'` in Haskell, S2 combinator, S' combinator, 'fork' in APL_

**definition** **`FF = f g h x -> f (g x) (h x)`**

**notation** **`{g f h} x`**

### Phi1 Combinator

**definition** **`FF_1 = f g h x y -> f (g x y) (h x y)`**

**notation** **`x {g f h} y`**

### Y Combinator

_allows for [[lambda calculus#recursion]]_

_used to formally define recursive [[function]]s in a [[functional programming]] language that does not support [[recursion]]_

> **equivalence** _[[combinator#y combinator]] and [[recursion#general recursion]]_

**aka** _fixed-point [[combinator]], `fix` in Haskell_

**definition** **`Y = f -> (x -> f (x x)) (x -> f (x x))`**

**definition** _using [[recursion]]_ **`Y = f -> f (Y f)`**

**definition** _in [[lambda calculus]]_ $Y = \lambda f.\ (\lambda x.\ f\ (x\ x)) (\lambda x.\ f\ (x\ x))$

**definition** _using [[combinator]]s_ **`Y = f -> {* *} (f {* *} *)`**

_it is not recursive but it encodes [[recursion]]_ &mdash; <https://youtu.be/9T8A89jgeTI?t=678>

&mdash; <https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator>

### Iota Combinator

**definition** **`ii = x -> x S K`**

the [[combinator#iota combinator]] can be used to define the [[combinator#s combinator]] and [[combinator#k combinator]], and can therefore be composed to produce [[combinator#combinator]]s that are extentionally equal to any [[lambda calculus]] term. consequently, **`ii`** [[combinatory logic]] is Turing complete, see [[turing machine]]

#### &mdash;

&mdash; <https://en.wikipedia.org/wiki/Combinatory_logic#One-point_basis>

&mdash; <https://en.wikipedia.org/wiki/SKI_combinator_calculus#Informal_description>

&mdash; <https://youtu.be/gnrSedVucXs?t=1678>

&mdash; <https://en.wikipedia.org/wiki/Iota_and_Jot#Universal_iota>

### &mdash;

&mdash; <https://en.wikipedia.org/wiki/B,_C,_K,_W_system>

&mdash; <https://en.wikipedia.org/wiki/SKI_combinator_calculus>

&mdash; <https://youtu.be/Y0KKPYkeOTA>

&mdash; <https://youtu.be/gnrSedVucXs>

&mdash; <https://combinatorylogic.com/table.html> &mdash; <https://youtu.be/Y0KKPYkeOTA>

&mdash; <https://www.angelfire.com/tx4/cus/combinator/birds.html> &mdash; <https://combinatorylogic.com/table.html> &mdash; <https://youtu.be/Y0KKPYkeOTA>

&mdash; <https://gist.github.com/Avaq/1f0636ec5c8d6aed2e45#file-combinators-md> &mdash; <https://combinatorylogic.com/table.html> &mdash; <https://youtu.be/Y0KKPYkeOTA>

&mdash; <https://codegolf.stackexchange.com/questions/53250/optimizing-ski-compiler>

&mdash; <https://cs.stackexchange.com/questions/13901/what-is-the-name-of-this-combinator>

&mdash; <https://youtu.be/i1K_kUKJnE4?t=525>

&mdash; <https://youtu.be/i1K_kUKJnE4?t=562>

&mdash; <https://youtu.be/seVSlKazsNk?t=703>
