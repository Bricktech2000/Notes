# Category

&mdash; <https://youtu.be/yAi3XWCBkDo>

**see** [[category theory]], [[functor]]

**types**

[[set]]s

[[group]]s

**definition**

a category $\mathcal C$ consists of [[category#object]]s and [[category#morphism]]s with [[category#composition]] and [[category#identity morphism]] all subject to the [[category#associativity law]] and the [[category#identity law]]

> **example** [[real]]s and the $\dashv$ operator form a [[category]] &mdash; <https://youtu.be/yAi3XWCBkDo?t=652>

[[category#object]]s and [[category#morphism]]s do not contain any information; [[category#composition]] and [[category#identity morphism]]s do. the goal is to encode everything in composition and identities

[[category]]es are often represented visually as [[graph]]s. however, not all [[graph]]s represent "valid" [[category]]es

## Object

every category has a collection of _objects_. even though [[category#object]]s can be anything, they are usually taken to be mathematical objects

objects of a category are generally specificed by writing them in a [[set]], denoted $\braket{\braket{1, 2, 3}}$ in my [[math notation]]. however, objects of a category do **not** (necessarily) form a (mathematical) [[set]]

### Initial Object

### Terminal Object

&mdash; <https://youtu.be/Gai-liKAUPo?t=153>

**definition** the _initial object_ of a [[category]] is the [[category#object]] that has exactly one [[category#morphism]] going to every object in the [[category]].

**definition** the _terminal object_ of a [[category]] is the [[category#object]] that has exactly one [[category#morphism]] coming to it from every object in the [[category]].

> **note** _terminal object_ should really have been named _coinitial object_ to match with terms such as _co[[monad]]_ and _coproduct_

**properties**

[[category#terminal object]]s are unique up to unique isomorphism

## Morphism

for any pair of [[category#object]]s $A$ and $B$, the category has a (mathematical) [[set]] of _morphisms_ from $A$ to $B$ known as their _hom-set_, denoted $\mathcal C(A, B) = \braket{\braket{f, g, \cdots}}$ in [[conventional math notation]].

a morphism from $A$ to $B$ is denoted $f: A \to B$ in [[conventional math notation]]. even though $A$ is related to $B$, $B$ is not necessarily related to $A$. they can be thought of as [[function]]s, but don't necessarily have to be.

any number of [[category#morphism]]s between two [[category#object]]s can exist. this includes zero morphisms to an infinity of morphisms.

### Isomorphism

**definition** an _isomorphism_ is a [[category#morphism]] with a corresponding inverse. let $f : A \to B$ and let $f^- : B \to A$ and let $\circ$ be the [[composition]] [[operator]]. then, there exists an _isomorphism_ between $A$ and $B$ if and only if $f \circ f^- = \textbf{id}_B$ and $f^- \circ f = \textbf{id}_A$

**definition** if there exists a [[category#isomorphism]] between two [[category#object]]s $A$ and $B$, they are said to be _isomorphic_, denoted $A \cong B$ in [[conventional math notation]].

> **note** a [[category#morphism]] being both _epic_ and _monic_ does not imply that it is a [[category#isomorphism]]

> **example**
>
> in the commutative diagram below, $\alpha$ (or the pair $\braket{\alpha, \alpha^{-1}}$) is an isomorphism
>
> ```mermaid
> graph LR
>   A(<span class=math>A</span>)
>   B(<span class=math>B</span>)
>
>   A -- <span class=math>id_A</span> --> A
>   B -- <span class=math>id_B</span> --> B
>   A -- <span class=math>\alpha</span> --> B
>   B -- <span class=math>\alpha^.1</span> --> A
> ```
>
> &mdash; <https://youtu.be/Gai-liKAUPo?t=483>
>
> &mdash; <https://youtu.be/yAi3XWCBkDo?t=954>

> "isomorphism captures the idea that objects can be functionally the same, where the meaning of _functionally_ depends on the working category" &mdash; <https://youtu.be/yAi3XWCBkDo?t=1012>

**properties**

[[category#isomorphism]]s are [[category#morphism]]s that are bijective, see [[function#bijective function]]

### Monomorphism

**definition** let $f : A \to B$, let $g_1 : C \to A$ and $g_2 : C \to A$, and let $\circ$ be the [[composition]] [[operator]]. then, $f$ is a _monomorphism from $A$ to $B$_ if and only if $f \circ g_1 = f \circ g_2 < g_1 = g_2$ for all $\mathcal C(C, A)\ g_1$ and $\mathcal C(C, A)\ g_2$ and for all $C$

> **note** this definition works because if $f$ mapped two different [[category#object]]s in $A$ to the same [[category#object]] in $B$, then there could exist two different [[category#morphism]]s $g_1$ and $g_2$ that would map elements of $C$ to $A$ differently which could then be mapped identically to $B$ by $f$

**properties**

monomorphisms are [[category#morphism]]s that are injective, see [[function#injective function]]

### Epimorphism

**definition** let $f : A \to B$, let $g_1 : B \to C$ and $g_2 : B \to C$, and let $\circ$ be the [[composition]] [[operator]]. then, $f$ is an _epimorphism from $A$ to $B$_ if and only if $g_1 \circ f = g_2 \circ f < g_1 = g_2$ for all $\mathcal C(B, C)\ g_1$ and $\mathcal C(B, C)\ g_2$ and for all $C$

> **note** this definition works because if the [[function#range]] $R$ of $f$ was a [[set#subset]] of its [[function#domain]] $B$, then there could exist two different [[category#morphism]]s $g_1$ and $g_2$ that would map elements in $R$ identically but would map elements in $B / R$ differently

**properties**

epimorphisms are [[category#morphism]]s that are surjective, see [[function#surjective function]]

## Composition

**see** [[composition]]

let $f : A \to B$ and $g : B \to C$ be morphisms from $A$ to $B$ and $B$ to $C$. then, there must exist a morphism $h : A \to C$ from $A$ to $C$ that is the [[composition]] of $f$ and $g$.

composition is denoted through the [[operator]] $\circ$ in [[conventional math notation]] and read as _after_ or _then_. for example, $f \circ g$ is read as _f after g_ or _f then g_.

### Associativity Law

[[composition]] in a category is required to be associative

let $\circ$ be the [[composition]] [[operator]]. then, $h \circ (g \circ f) = (h \circ g) \circ f$

## Identity Morphism

identities are [[category#morphism]]s that [[map]] a [[category#object]] to itself. in a category, each object must have an identity morphism. the [[set]] of all identities in a category is denoted $\mathcal C(A, A) = \braket{\braket{1_A, \cdots}}$ in [[conventional math notation]].

an identity is denoted $1_A: A \to A$ or as $\textbf{id}_A : A \to A$ in [[conventional math notation]].

### Identity Law

for every [[category#object]] $A$ there is an arrow which is a unit of [[composition]]. let $f : A \to B$ and let $\circ$ be the [[composition]] [[operator]]. then,

$f \circ \textbf{id}_A = f$

$\textbf{id}_B \circ f = f$

in Haskell, let `id :: a -> a`. then, `id x = x`

## Functor

[[functor]]s are [[map]]s between [[category]]es which respect categorical structure &mdash; <https://youtu.be/yAi3XWCBkDo?t=1238>. this leads to the [[category]] of [[category]]es

to do so, they must use a pair of [[function]]s to [[map]] both [[category#object]]s and [[category#morphism]]s between the [[category]]es and preserve the identity and composition laws

### Forgetful Functor

**definition** a _forgetful functor_ is a [[functor]] that forgets some information about the [[category]] it is mapping from &mdash; Github Copilot

> **example**
>
> the [[category#functor]] from the [[category]] of [[group]]s to the [[category]] of [[set]]s is a forgetful functor because it forgets the [[group#operation]] and [[group#identity element]]

## Opposite Category

**aka** _Duality_

&mdash; <https://youtu.be/Gai-liKAUPo?t=190>

**definition** for any [[category]] $\mathcal C$, one can define the _opposite category_ $\mathcal C^{op}$ by reversing all its morphisms

this can be thought of as "reversing the direction" of the "arrows" in the [[graph]] the [[category]]

## Product

## Coproduct

products between [[category#object]]s are basically [[type#product type]]s

coproducts between [[category#object]]s are basically [[type#sum type]]s

> A _product_ of two [[category#object]]s $A$ and $B$ is the object $P$ equipped with two projections such that for any other object $P'$ equipped with two projections there is a unique [[category#morphism]] $m$ from $P'$ to $P$ that factorizes those projections.

#todo "factorizes those projections" means that the diagram _commutes_ (composing two of the marphisms gives the third one)

&mdash; <https://miklos-martin.github.io/learn/fp/category-theory/2018/02/01/adventures-in-category-theory-the-algebra-of-types.html>

factorizes &mdash; <https://youtu.be/Bsdl_NKbNnU?t=1011>

#think <https://youtu.be/Gai-liKAUPo?t=327>

**representation** _[[category#product]]_

```mermaid
graph TD
  A(<span class=math>A</span>)
  B(<span class=math>B</span>)
  P(<span class=math>P</span>)
  P_(<span class=math>P'</span>)

  P -- <span class=math>f_1</span> --> A
  P -- <span class=math>f_2</span> --> B

  P_ -- <span class=math>f_1 \circ m</span> --> A
  P_ -. <span class=math>m</span> .-> P
  P_ -- <span class=math>f_2 \circ m</span> --> B
```

**representation** _[[category#coproduct]]_

```mermaid
graph BT
  A(<span class=math>A</span>)
  B(<span class=math>B</span>)
  Q(<span class=math>Q</span>)
  Q_(<span class=math>Q'</span>)

  A -- <span class=math>f_1</span> --> Q
  B -- <span class=math>f_2</span> --> Q

  A -- <span class=math>m \circ f_1</span> --> Q_
  Q -. <span class=math>m</span> .-> Q_
  B -- <span class=math>m \circ f_2</span> --> Q_
```
