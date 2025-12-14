# Lambda-Calculus

--- <https://ncatlab.org/nlab/show/lambda-calculus>

--- <https://youtu.be/233A3bN0UBE> and <https://youtu.be/R1dmeFEJyqI> and <https://youtu.be/K-4Mj3LpP2E> and <https://youtu.be/VrRVqHvy4PQ>

**see** [[combinatory logic]], [[recursion]]

> **resource** _SSA is Functional Programming_ "SSA is just another name for [[lambda-calculus]]" --- [[ssafun.pdf]] --- <https://www.cs.princeton.edu/~appel/papers/ssafun.pdf> --- <https://crypto.stanford.edu/~blynn/compiler/lambda.html>

the λ-calculus is a simple [[programming language]] and [[turing complete]] model of computation. it is the basis for most [[functional programming]] [[programming language]]s

**definition** _β-reduction_ is the process of [[substitution]] of bound variables with the argument to an abstraction

**definition** a λ-term _reduces_ to another if and only if the first can be converted into the second through a chain of _β-reductions_

**notation** _one-step β-reducibility_ $M \longrightarrow_\beta N$ --- <https://ncatlab.org/nlab/show/beta-reduction>

**notation** _many-step β-reducibility_ $M \longrightarrow_\beta^* N$ --- <https://ncatlab.org/nlab/show/beta-reduction>

> **note** _many-step β-reducibility_ is the reflexive transitive closure of _one-step β-reducibility_ --- <https://crypto.stanford.edu/~blynn/lambda/diamond.html>

**definition** two λ-terms are _β-equivalent_ if and only if they can be converted to eachother through a zigzag of _β-reductions_

**notation** _β-equivalence_ $M =_\beta N$ --- <https://ncatlab.org/nlab/show/beta-reduction>

> **note** _β-equivalence_ is the reflexive symmetric transitive closure of _one-step β-reducibility_ --- <https://cs.stackexchange.com/questions/634/what-is-beta-equivalence> and is thus a [[relation#equivalence relation]] --- <https://youtu.be/R1dmeFEJyqI?t=579> and <https://ncatlab.org/nlab/show/beta-reduction>

**definition** a λ-term is in _β-normal form_ if and only if it cannot be _β-reduced_ any further

**definition** a λ-term is _weakly normalizing_ if and only if there exists a chain of β-reductions on the term that reaches a _β-normal form_ --- <https://youtu.be/R1dmeFEJyqI?t=772>

**definition** a λ-term is _strongly normalizing_ if and only if every chain of β-reductions on the term reaches a _β-normal form_ --- <https://youtu.be/R1dmeFEJyqI?t=772>

**definition** _α-conversion_ is the process of renaming bound variables to avoid name collisions

**definition** two λ-terms are _α-equivalent_ if and only if they can be converted to eachother through _α-conversions_

**notation** _α-equivalence_ $M \equiv N$

> **note** λ-terms can be denoted canonically using De Bruijn indices, eliminating the need for α-conversion and α-equivalence --- <https://youtu.be/UUUQp8HvrH0?t=892>

**definition** _η-reduction_ and _η-expansion_---collectively, _η-conversion_---convert back and forth between a λ-term and the immediate abstraction of a free variable applied to the λ-term

> **note** η-reduction is "dual" to β-reduction in the sense that the former simplifies a _constructor_ applied to an _eliminator_ while the latter simplifies an _eliminator_ applied to a _constructor_ --- <https://ncatlab.org/nlab/show/eta-conversion>

## Syntax

--- <https://youtu.be/IOiZatlZtGU?t=292>

**see** [[backus--naur form]]

```bnf
<term> ::= <var>                        ; variable
         | "λ" <var> "." <term>         ; abstraction
         | "(" <term> " " <term> ")"    ; application
<var> ::= (? some lowercase latin letter ?)
```

## Simply Typed Lambda Calculus

**aka** _λ→_

every typeable λ→-term is _strongly normalizing_ --- <https://youtu.be/WHQ-OYFqp5w?t=393>; thus λ→ is not [[turing complete]]

self-application is not typeable in the simply typed λ-calculus --- <https://youtu.be/WHQ-OYFqp5w?t=462>; thus λ→ has no [[recursion]]

### Syntax

**see** [[backus--naur form]]

```bnf
<term> ::= <var>                                   ; variable
         | "λ" <var> ":" <type> "." <term>         ; abstraction
         | "(" <term> " " <term> ")"               ; application
<var> ::= (? some lowercase latin letter ?)
<type> ::= <base>                                  ; variable type
         | "(" <type> "→" <type> ")"               ; arrow type
<base> ::= (? some lowercase greek letter ?)
```

### Typing Rules

**see** [[inference rule]]

_variable_ $\displaystyle \frac{}{\Gamma \vdash x : \sigma}$ if $x : \sigma \in \Gamma$

_abstraction_ $\displaystyle \frac{\Gamma, x : \sigma \vdash e : \tau}{\Gamma \vdash (\lambda x : \sigma.\ e) : (\sigma \to \tau)}$

_application_ $\displaystyle \frac{\Gamma \vdash e_1 : \sigma \to \tau \quad \Gamma \vdash e_2 : \sigma}{\Gamma \vdash (e_1\ e_2) : \tau}$

--- <https://youtu.be/knD_5pBCmuI?t=621>

--- <https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus#Typing_rules>

### ---

--- <https://youtu.be/UUUQp8HvrH0>

--- <https://youtu.be/knD_5pBCmuI> and <https://youtu.be/WHQ-OYFqp5w>

--- <https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus>

---

# Constructions

--- _Church Encoding of Data Types Considered Harmful for Implementations_ <https://ifl2014.github.io/submissions/ifl2014_submission_13.pdf> (though lots of babble and grammar errors and typos)

## Non-Recursive Types

non-recursive [[type#algebraic data type]]s can be encoded naturally in the [[lambda-calculus]]. [[type#sum type]]s are [[function]]s that call one of their several parameters to emulate case analysis, and [[type#product type]]s are [[function]]s that call their single parameter with several arguments to emulate destructuring

[[lambda-calculus#church encoding]] and [[lambda-calculus#scott encoding]] coincide to this non-recursive encoding when the [[type#algebraic data type]] they encode is not recursive

### Booleans

**see** [[boolean]]

`data Bool = True | False` can be encoded in the [[lambda-calculus]] as follows:

- $\mathrm{true} = t.\ f.\ t$
- $\mathrm{false} = t.\ f.\ f$

we can then define the [[boolean#operator]]s:

- $\mathrm{not}\ p = p\ \mathrm{false}\ \mathrm{true}$
- $\mathrm{and}\ p\ q = p\ q\ p$
- $\mathrm{or}\ p\ q = p\ p\ q$

--- <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

### Pairs

**see** [[ordered pair]]

`data Pair x y = Pair x y` be encoded in the [[lambda-calculus]] as follows:

- $\mathrm{pair}\ f\ s = p.\ p\ f\ s$
- $\mathrm{fst}\ p = p\ (f.\ s.\ f)$
- $\mathrm{snd}\ p = p\ (f.\ s.\ s)$

## Church Encoding

--- <https://youtu.be/K-4Mj3LpP2E>

the Church encoding encodes recursive [[type#algebraic data type]]s by building up a generalized [[monoid#fold]] over the data. providing a fold [[function]] and a base case to a term β-reduces to the result of a fold over it. however, accessing the data of a recursive variant is tricky and generally not of constant time [[computational complexity]]

### Church Numerals

**see** [[natural]]

the Church encoding of `data Nat = Succ Nat | Zero` is as follows:

- $\mathrm{zero} = s.\ z.\ z$
- $\mathrm{succ}\ n = s.\ z.\ s\ (n\ s\ z)$

we can then define:

- $\mathrm{iszero}\ n = n\ (n.\ \mathrm{false})\ \mathrm{true}$

### lists

**see** [[list]]

the Church encoding of `data List a = Cons a (List a) | Nil` is as follows:

- $\mathrm{nil} = c.\ n.\ n$
- $\mathrm{cons}\ h\ t = c.\ n.\ c\ h\ (t\ c\ n)$

we can then define:

- $\mathrm{isnil}\ l = l\ (h.\ t.\ \mathrm{false})\ \mathrm{true}$
- $\mathrm{list1}\ h = c.\ n.\ c\ h\ (\mathrm{nil}\ c\ n)$
- $\mathrm{head}\ l = l\ (h.\ t.\ \mathrm{some}\ h)\ \mathrm{none}$

## Scott Encoding

--- <https://crypto.stanford.edu/~blynn/compiler/scott.html>

the Scott encoding encodes recursive [[type#algebraic data type]]s in the obvious way, building a decision tree of sorts. folding over a term requires explicit external [[recursion]], say by using a [[fixed point]] [[combinator]] such as the [[combinator#y combinator]]. that said, accessing the data of a recursive variant is trivial and of constant time [[computational complexity]]

### Scott Numbers

**see** [[natural]]

the Scott encoding of `data Nat = Succ Nat | Zero` is as follows:

- $\mathrm{zero} = s.\ z.\ z$
- $\mathrm{succ}\ n = s.\ z.\ s\ n$

we can then define:

- $\mathrm{iszero}\ n = n\ (n.\ \mathrm{false})\ \mathrm{true}$

unlike with [[lambda-calculus#church encoding]], we may easily define:

- $\mathrm{pred}\ n = s.\ z.\ n\ (n.\ n)\ z$

### lists

**see** [[list]]

the Scott encoding of `data List a = Cons a (List a) | Nil` is as follows:

- $\mathrm{nil} = c.\ n.\ n$
- $\mathrm{cons}\ h\ t = c.\ n.\ c\ h\ t$

we can then define:

- $\mathrm{isnil}\ l = l\ (h.\ t.\ \mathrm{false})\ \mathrm{true}$
- $\mathrm{list1}\ h = c.\ n.\ c\ h\ \mathrm{nil}$
- $\mathrm{head}\ l = l\ (h.\ t.\ \mathrm{some}\ h)\ \mathrm{none}$

unlike with [[lambda-calculus#church encoding]], we may easily define:

- $\mathrm{tail}\ l = l\ (h.\ t.\ \mathrm{some}\ t)\ \mathrm{none}$
