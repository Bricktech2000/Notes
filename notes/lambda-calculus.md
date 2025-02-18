# Lambda-Calculus

--- <https://ncatlab.org/nlab/show/lambda-calculus>

**see** [[combinatory logic]], [[recursion]]

> **resource** _SSA is Functional Programming_ "SSA is just another name for [[lambda-calculus]]" --- [[ssafun.pdf]] --- <https://www.cs.princeton.edu/~appel/papers/ssafun.pdf> --- <https://crypto.stanford.edu/~blynn/compiler/lambda.html>

the λ-calculus is a simple [[programming language]] and [[turing complete]] model of computation. it is the basis for most [[functional programming]] [[programming language]]s

**definition** _β-reduction_ is the process of replacing bound variables with the argument to an abstraction

**definition** a λ-term is in _β-normal form_ if it cannot be _β-reduced_ any further

**definition** _α-conversion_ is the process of renaming bound variables to avoid name collisions

**definition** two λ-terms are _α-equivalent_ if and only if one can be converted into the other through _α-conversion_

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

**properties** --- <https://youtu.be/WHQ-OYFqp5w?t=449>

every chain of β-reductions of simply typed λ-terms reaches the β-normal form, and so every program in the simply typed λ-calculus is terminating. consequently, it is not [[turing complete]]

self-application is not typeable in the simply typed λ-calculus. consequently, [[recursion]] is impossible

### Syntax

**see** [[backus--naur form]]

```bnf
<term> ::= <var>                                   ; variable
         | "λ" <var> ":" <type> "." <term>         ; abstraction
         | "(" <term> " " <term> ")"               ; application
<var> ::= (? some lowercase latin letter ?)
<type> ::= <base>                                  ; variable type
         | "(" <type> "->" <type> ")"              ; arrow type
<base> ::= (? some lowercase greek letter ?)
```

### Typing Rules

**see** [[inference rule]]

_variable_ $\displaystyle \frac{x : \sigma \in \Gamma}{\Gamma \vdash x : \sigma}$

_abstraction_ $\displaystyle \frac{\Gamma, x : \sigma \vdash e : \tau}{\Gamma \vdash (\lambda x : \sigma.\ e) : (\sigma \to \tau)}$

_application_ $\displaystyle \frac{\Gamma \vdash e_1 : \sigma \to \tau \quad \Gamma \vdash e_2 : \sigma}{\Gamma \vdash (e_1\ e_2) : \tau}$

--- <https://youtu.be/knD_5pBCmuI?t=621>

--- <https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus#Typing_rules>

### ---

--- <https://youtu.be/UUUQp8HvrH0>

--- <https://youtu.be/knD_5pBCmuI>

--- <https://youtu.be/WHQ-OYFqp5w>

--- <https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus>

---

# Constructions

--- _Church Encoding of Data Types Considered Harmful for Implementations_ <https://ifl2014.github.io/submissions/ifl2014_submission_13.pdf> (though lots of babble and grammar errors and typos)

**see** [[math notation]]

## Non-Recursive Types

non-recursive [[type#algebraic data type]]s can be encoded naturally in the [[lambda-calculus]]. [[type#sum type]]s are [[function]]s that call one of their several parameters to emulate case analysis, and [[type#product type]]s are [[function]]s that call their single parameter with several arguments to emulate destructuring

[[lambda-calculus#church encoding]] and [[lambda-calculus#scott encoding]] coincide to this non-recursive encoding when the [[type#algebraic data type]] they encode is not recursive

### Booleans

**see** [[boolean]]

`data Bool = True | False` can be encoded in the [[lambda-calculus]] as follows:

- **`"true" = x. y. x`**
- **`"false" = x. y. y`**

we can then define the [[boolean#operator]]s:

- **`"not" p = p "false" "true"`**
- **`"and" p q = p q p`**
- **`"or" p q = p p q`**

--- <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

### Pairs

**see** [[ordered pair]]

`data Pair x y = Pair x y` be encoded in the [[lambda-calculus]] as follows:

- **`"pair" x y = z. z x y`**
- **`"fst" p = p (x. y. x)`**
- **`"snd" p = p (x. y. y)`**

## Church Encoding

the Church encoding encodes recursive [[type#algebraic data type]]s by building up a generalized fold over the data; see [[reduce function]]. providing a fold [[function]] and a base case to a term β-reduces to the result of a fold over it. however, accessing the data of a recursive variant is tricky and generally not of constant time [[computational complexity]]

### Church Numerals

**see** [[natural]]

the Church encoding of `data Nat = Succ Nat | Zero` is as follows:

- **`"zero" = s. z. z`**
- **`"succ" n = s. z. s (n s z)`**

we can then define:

- **`"iszero" n = n (."false") "true"`**

### lists

**see** [[list]]

the Church encoding of `data List a = Cons a (List a) | Nil` is as follows:

- **`"nil" = c. n. n`**
- **`"cons" h t = c. n. c h (t c n)`**

we can then define:

- **`"isnil" l = l (.."false") "true"`**
- **`"list1" h = c. n. c h (nil c n)`**
- **`"head" l = l (h. f. some h) none`**

## Scott Encoding

--- <https://crypto.stanford.edu/~blynn/compiler/scott.html>

the Scott encoding encodes recursive [[type#algebraic data type]]s in the obvious way, building a decision tree of sorts. folding over a term requires explicit external [[recursion]], say by using a fixed-point combinator such as the [[combinator#y combinator]]. that said, accessing the data of a recursive variant is trivial and of constant time [[computational complexity]]

### Scott Numbers

**see** [[natural]]

the Scott encoding of `data Nat = Succ Nat | Zero` is as follows:

- **`"zero" = s. z. z`**
- **`"succ" n = s. z. s n`**

we can then define:

- **`"iszero" n = n (."false") "true"`**

unlike with [[lambda-calculus#church encoding]], we may easily define:

- **`"pred" n = s. z. n (n. n) z`**

### lists

**see** [[list]]

the Scott encoding of `data List a = Cons a (List a) | Nil` is as follows:

- **`"nil" = c. n. n`**
- **`"cons" h t = c. n. c h t`**

we can then define:

- **`"isnil" l = l (."false") "true"`**
- **`"list1" h = c. n. c h nil`**
- **`"head" l = l (h. t. some h) none`**

unlike with [[lambda-calculus#church encoding]], we may easily define:

- **`"tail" l = l (h. t. some t) none`**
