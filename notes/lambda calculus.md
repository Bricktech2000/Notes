# Lambda Calculus

**aka** _&lambda;-calculus_

**see** [[combinatory logic]], [[recursion]]

> **resource** _SSA is Functional Programming_ "SSA is just another name for [[lambda calculus]]" &mdash; <https://www.cs.princeton.edu/~appel/papers/ssafun.pdf> &mdash; <https://crypto.stanford.edu/~blynn/compiler/lambda.html>

**definition** _&beta;-reduction_ is the process of replacing bound variables with the argument to an abstraction

**definition** a &lambda;-term is in _&beta;-normal form_ if it cannot be _&beta;-reduced_ any further

**definition** _&alpha;-conversion_ is the process of renaming bound variables to avoid name collisions

**definition** two &lambda;-terms are _&alpha;-equivalent_ if and only if one can be converted into the other through _&alpha;-conversion_

> **note** &lambda;-terms can be denoted canonically using De Bruijn indices, eliminating the need for &alpha;-conversion and &alpha;-equivalence &mdash; <https://youtu.be/UUUQp8HvrH0?t=892>

**properties**

[[function]]s in the [[lambda calculus]] are [[function#pure function]]s

the [[lambda calculus]] is [[turing complete]]

the [[lambda calculus]] is the basis for most [[functional programming]] [[programming language]]s

## Syntax

&mdash; <https://youtu.be/IOiZatlZtGU?t=292>

**see** [[backus-naur form]]

_in [[conventional math notation]]_

```bnf
<expr> ::= <var>                        ; variable
         | "(" <expr> " " <expr> ")"    ; application
         | "(" "λ" <var> "." <expr> ")" ; abstraction
<var> ::= (? some lowercase latin letter ?)
```

_in my [[math notation]]_

```bnf
<expr> ::= <var>             ; variable
         | <expr> " " <expr> ; application
         | <var> "->" <expr> ; abstraction
         | "(" <expr> ")"    ; grouping
<var> ::= (? some lowercase latin letter ?)
```

## Simply Typed Lambda Calculus

**aka** &lambda; &#8407;-calculus

**properties** &mdash; <https://youtu.be/WHQ-OYFqp5w?t=449>

every chain of &beta;-reductions of &lambda; &#8407;-terms reaches the &beta;-normal form, and so every program in the &lambda; &#8407;-calculus is terminating. consequently, it is not [[turing complete]]

self-application is not typeable in the &lambda; &#8407;-calculus. consequently, [[recursion]] is impossible

### Syntax

**see** [[backus-naur form]]

_in [[conventional math notation]]_

```bnf
<expr> ::= <var>                                   ; variable
         | "(" <expr> " " <expr> ")"               ; application
         | "(" "λ" <var> ":" <type> "." <expr> ")" ; abstraction
<var> ::= (? some lowercase latin letter ?)
<type> ::= <base>                                  ; variable type
         | "(" <type> "->" <type> ")"              ; arrow type
<base> ::= (? some lowercase greek letter ?)
```

### Typing Rules

_variable_ $\displaystyle\frac{x : \sigma \in \Gamma}{\Gamma \vdash x : \sigma}$

_application_ $\displaystyle\frac{\Gamma \vdash e_1 : \sigma \to \tau \quad \Gamma \vdash e_2 : \sigma}{\Gamma \vdash (e_1\ e_2) : \tau}$

_abstraction_ $\displaystyle\frac{\Gamma, x : \sigma \vdash e : \tau}{\Gamma \vdash (\lambda x : \sigma.\ e) : (\sigma \to \tau)}$

&mdash; <https://youtu.be/knD_5pBCmuI?t=621>

&mdash; <https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus#Typing_rules>

### &mdash;

&mdash; <https://youtu.be/UUUQp8HvrH0>

&mdash; <https://youtu.be/knD_5pBCmuI>

&mdash; <https://youtu.be/WHQ-OYFqp5w>

&mdash; <https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus>

---

# Constructions

&mdash; _Church Encoding of Data Types Considered Harmful for Implementations_ <https://ifl2014.github.io/submissions/ifl2014_submission_13.pdf> (though lots of babble and grammar errors and typos)

## Non-Recursive Types

non-recursive [[type#algebraic data type]]s can be encoded naturally in the [[lambda calculus]]. [[type#sum type]]s are [[function]]s that call one of their several parameters to emulate case analysis, and [[type#product type]]s are [[function]]s that call their single parameter with several arguments to emulate destructuring

[[lambda calculus#church encoding]] and [[lambda calculus#scott encoding]] coincide to this non-recursive encoding when the [[type#algebraic data type]] they encode is not recursive

### Booleans

**see** [[boolean]]

`data Bool = True | False` can be encoded in the [[lambda calculus]] as follows:

- **`"true" = x. y. x`**
- **`"false" = x. y. y`**

we can then define the [[boolean#operator]]s:

- **`"not" p = p "false" "true"`**
- **`"and" p q = p q p`**
- **`"or" p q = p p q`**

&mdash; <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

### Pairs

**see** [[ordered pair]]

`data Pair x y = Pair x y` be encoded in the [[lambda calculus]] as follows:

- **`"pair" x y = z. z x y`**
- **`"fst" p = p (x. y. x)`**
- **`"snd" p = p (x. y. y)`**

## Church Encoding

the Church encoding encodes recursive [[type#algebraic data type]]s by building up a generalized fold over the data; see [[reduce function]]. providing a fold [[function]] and a base case to a term &beta;-reduces to the result of a fold over it. however, accessing the data of a recursive variant is tricky and generally not of constant time [[computational complexity]]

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

&mdash; <https://crypto.stanford.edu/~blynn/compiler/scott.html>

the Scott encoding encodes recursive [[type#algebraic data type]]s in the obvious way, building a decision tree of sorts. folding over a term requires explicit external [[recursion]], say by using a fixed-point combinator such as the [[combinator#y combinator]]. that said, accessing the data of a recursive variant is trivial and of constant time [[computational complexity]]

### Scott Numbers

**see** [[natural]]

the Scott encoding of `data Nat = Succ Nat | Zero` is as follows:

- **`"zero" = s. z. z`**
- **`"succ" n = s. z. s n`**

we can then define:

- **`"iszero" n = n (."false") "true"`**

unlike with [[lambda calculus#church encoding]], we may easily define:

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

unlike with [[lambda calculus#church encoding]], we may easily define:

- **`"tail" l = l (h. t. some t) none`**
