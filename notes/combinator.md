# Combinator

**definition** a _combinator_ is a closed [[lambda-calculus]] term --- <https://youtu.be/seVSlKazsNk>

**properties**

[[combinator]]s can be manipulated through [[combinatory logic]]

---

## Combinators

### I Combinator

_identity_

**aka** _identity_, _`id`_ in Haskell

**equiv** _[[function#identity]]_

**definition** **`I = x -> x = (*)`** #todo id

**definition** **`I = S K K`**

**definition** **`I = ii ii`**

**notation** **`(*) x`** #todo id

### K Combinator

_discards the second argument_

**aka** _constant_, _`const`_ in Haskell

**definition** **`K = x. y. x`**

**definition** **`K = ii (ii (ii ii))`**

**notation** **`.x y`**

### S Combinator

**aka** _substitution_, _`<*>`_ and _`ap`_ in Haskell

**definition** **`S = f. g. x. f x (g x)`**

**definition** **`S = ii (ii (ii (ii ii)))`**

**notation** **`(f g) x`** or equivalently **`(* f g) x`** #todo id

### B Combinator

_the [[function#composition]] of its arguments_

**aka** _compose_, _`(.)`_ and _`fmap`_ in Haskell, _"bluebird"_

**equiv** _[[function#composition]]_

**definition** **`B = f. g. x. f (g x)`**

**definition** **`B = S (K S) K`**

**definition** _in the [[lambda-calculus]]_ $B = \lambda fgx.\ f\ (g\ x)$

**notation** **``f`g x``**

--- <https://youtu.be/SmXB2K_5lcA?t=612>

### B1 Combinator

**aka** _"blackbird"_, _`.:`_ in Haskell

**definition** **`B_1 = f. g. x. y. f (g x y)`**

**definition** **`B_1 = B B B`**

**definition** `.: = (.) . (.)`

### C Combinator

_swaps the arguments to a function_

**aka** _flip_, _`flip`_ in Haskell

**equiv** _[[matrix#transpose]]_

**definition** **`C = f. x. y. f y x`**

**definition** **`C = S (B B S) (K K)`**

**notation** **`rr f x y`**

### W Combinator

_duplicates the second argument_

**aka** _duplication_, _'commute'_ or _'self'_ in APL, _`join`_ in Haskell

**definition** **`W = f. x. f x x`**

**definition** **`W = C S K`**

**notation** **`(f *) x`** or equivalently **`(* f *) x`** #todo id

### M Combinator

_applies a [[function]] to itself_

**aka** _mockingbird_, _ω_ combinator

**definition** **`M = f. f f`**

**definition** **`M = S I I`**

**notation** **`(* *) f`** #todo id

### KI Combinator

_discards the first argument_

**aka** _kite_, _`const id`_ in Haskell

**definition** **`K I = f. x. y. f y`**

**notation** **`.(*)`** #todo id

### T Combinator

_applies the first argument to the second argument_

**aka** _thrush_, _`&`_ in Haskell

**definition** **`T = x. f. f x`**

**definition** **`T = C I`**

### SBI Combinator

_applies a [[function]] twice_

**definition** **`S B I = f. x. f (f x)`**

### Sigma Combinator

**aka** _chain_, _`=<<`_ in Haskell, _S'_ combinator

**definition** **`SS = f. g. x. f (g x) x`**

**notation** **`(g f *) x`** #todo id

### Psi Combinator

**aka** _`on` in Haskell_

**definition** **`YY = f. g. x. y. f (g x) (g y)`**

**notation** **`g {x f y}`**

### Phi Combinator

**aka** _converge_, _`liftA2`_ and _`liftM2`_ and _`phoenix`_ and _`starling'`_ in Haskell, _S2_ combinator, _S'_ combinator, _'fork'_ in APL

**definition** **`FF = f. g. h. x. f (g x) (h x)`**

**notation** **`(g f h) x`**

### Phi1 Combinator

**definition** **`FF_1 = f. g. h. x. y. f (g x y) (h x y)`**

**notation** **`x (g f h) y`**

### Y Combinator

**aka** _fixed-point combinator_, _`fix`_ in Haskell

**see** [[fixed point]]

the [[combinator#y combinator]] lets us use recursion in [[programming language]]s that don't support it, which includes the [[lambda-calculus]]

**definition** **`Y = f. (x. f (x x)) (x. f (x x))`**

**definition** _using [[recursion]]_ **`Y = f. f (Y f)`**

**definition** _in the [[lambda-calculus]]_ $Y = \lambda f.\ (\lambda x.\ f\ (x\ x)) (\lambda x.\ f\ (x\ x))$

> **example** $\mathrm{fact} = Y\ (\lambda f\ n.\ (\mathrm{is0}\ n)\ 1\ (\mathrm{mul}\ n\ (f\ (\mathrm{pred}\ n))))$ --- <https://crypto.stanford.edu/~blynn/lambda/>

--- <https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator>

### Theta Combinator

**aka** _Turing combinator_

**see** [[fixed point]]

**definition** **`QQ = (x. y. y (x x y)) (x. y. y (x x y))`**

the advantage of the [[combinator#theta combinator]] over the [[combinator#y combinator]] is that **`QQ f`** β-reduces to **`f (QQ f)`** while **`Y f`** and **`f (Y f)`** only β-reduce to a common term

--- <https://en.wikipedia.org/wiki/Fixed-point_combinator#Other_fixed-point_combinators>

--- <https://crypto.stanford.edu/~blynn/lambda/quine.html#_curry>

### Iota Combinator

**definition** **`ii = x. x S K`**

we have **`ii ii = I /\ ii (ii ii) = S K /\ ii (ii (ii ii)) = K /\ ii (ii (ii (ii ii))) = S`**; the [[combinator#iota combinator]] can be used to define the [[combinator#s combinator]] and [[combinator#k combinator]], and can therefore be composed to produce [[combinator#combinator]]s that are extensionally equal to any term in the [[lambda-calculus]]. consequently, **`ii`** [[combinatory logic]] is [[turing complete]]

#### ---

--- <https://en.wikipedia.org/wiki/Combinatory_logic#One-point_basis>

--- <https://en.wikipedia.org/wiki/SKI_combinator_calculus#Informal_description>

--- <https://youtu.be/gnrSedVucXs?t=1678>

--- <https://en.wikipedia.org/wiki/Iota_and_Jot#Universal_iota>

### ---

--- <https://en.wikipedia.org/wiki/B,_C,_K,_W_system>

--- <https://en.wikipedia.org/wiki/SKI_combinator_calculus>

--- <https://youtu.be/gnrSedVucXs>

--- <https://youtu.be/Y0KKPYkeOTA>

--- <https://combinatorylogic.com/table.html> --- <https://youtu.be/Y0KKPYkeOTA>

--- <https://www.angelfire.com/tx4/cus/combinator/birds.html> --- <https://combinatorylogic.com/table.html> --- <https://youtu.be/Y0KKPYkeOTA>

--- <https://gist.github.com/Avaq/1f0636ec5c8d6aed2e45#file-combinators-md> --- <https://combinatorylogic.com/table.html> --- <https://youtu.be/Y0KKPYkeOTA>

--- <https://codegolf.stackexchange.com/questions/53250/optimizing-ski-compiler>

--- <https://cs.stackexchange.com/questions/13901/what-is-the-name-of-this-combinator>

--- <https://youtu.be/i1K_kUKJnE4?t=525>

--- <https://youtu.be/i1K_kUKJnE4?t=562>

--- <https://youtu.be/seVSlKazsNk?t=703>
