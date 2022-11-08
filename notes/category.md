# Category

&mdash; <https://youtu.be/yAi3XWCBkDo>

**see** [[category theory]], [[functor]]

**types**

[[set]]s

[[group]]s

**definition**

a category $\mathcal C$ consists of _objects_ and _morphisms_ with _composition_ and _identities_ all subject to the _associativity law_ and the _identity law_

> **example** [[real]]s and the $\le$ operator form a [[category]] &mdash; <https://youtu.be/yAi3XWCBkDo?t=652>

objects and morphisms do not contain any information; composition and identities do. the goal is to encode everything in composition and identities

[[category]]es are often represented visually as [[graph]]s. however, not all [[graph]]s represent "valid" [[category]]es

## Objects

every category has a collection of _objects_. even though objects can be anything, they are usually taken to be mathematical objects

objects of a category are generally specificed by writing them in a [[set]], denoted $\braket{\braket{1, 2, 3}}$ in my [[math notation]]. however, objects of a category do **not** (necessarily) form a (mathematical) [[set]]

### Initial and Terminal Objects

&mdash; <https://youtu.be/Gai-liKAUPo?t=153>

**definition** the _initial object_ of a [[category]] is the object that has exactly one morphism going to every object in the [[category]].

**definition** the _terminal object_ of a [[category]] is the object that has exactly one morphism coming to it from every object in the [[category]].

> **note** _terminal object_ should really have been named _coinitial object_ to match with terms such as _co[[monad]]_ and _coproduct_

**properties**

terminal objects are unique up to unique isomorphism

## Morphisms

for any pair of objects $A$ and $B$, the category has a (mathematical) [[set]] of _morphisms_ from $A$ to $B$ known as their _hom-set_, denoted $\mathcal C(A, B) = \braket{\braket{f, g, \dots}}$ in [[conventional math notation]].

a morphism from $A$ to $B$ is denoted $f: A \to B$ in [[conventional math notation]]. even though $A$ is related to $B$, $B$ is not necessarily related to $A$. they can be thought of as [[function]]s, but don't necessarily have to be.

any number of morphisms between two objects can exist. this includes zero morphisms to an infinity of morphisms.

### Isomorphism

**definition** an _isomorphism_ is a morphism with a corresponding inverse. let $f : A \to B$ and let $f^- : B \to A$ and let $\circ$ be the [[composition]] [[operator]]. then, there exists an _isomorphism_ between $A$ and $B$ if and only if $f \circ f^- = \textbf{id}_B$ and $f^- \circ f = \textbf{id}_A$

**definition** if there exists an isomorphism between two objects $A$ and $B$, they are said to be _isomorphic_, denoted $A \cong B$ in [[conventional math notation]].

> **note** a morphism being both _epic_ and _monic_ does not imply that it is an isomorphism

> **example**
>
> in the commutative diagram below, $\alpha$ (or the pair $\braket{\alpha, \alpha^{-1}}$) is an isomorphism
>
> ![[20220708044859.png]] &mdash; <https://youtu.be/Gai-liKAUPo?t=483>
>
> &mdash; <https://youtu.be/yAi3XWCBkDo?t=954>

> "isomorphism captures the idea that objects can be functionally the same, where the meaning of _functionally_ depends on the working category" &mdash; <https://youtu.be/yAi3XWCBkDo?t=1012>

**properties**

isomorphisms are morphisms that are bijective, see [[function]]

### Monomorphism

**definition** let $f : A \to B$, let $g_1 : C \to A$ and $g_2 : C \to A$, and let $\circ$ be the [[composition]] [[operator]]. then, $f$ is a _monomorphism from $A$ to $B$._ if and only if $f \circ g_1 = f \circ g_2 \vdash g_1 = g_2$ for all $\mathcal C(C, A)\ g_1$ and $\mathcal C(C, A)\ g_2$ and for all $C$

> **note** this definition works because if $f$ mapped two different objects in $A$ to the same object in $B$, then there could exist two different morphisms $g_1$ and $g_2$ that would map elements of $C$ to $A$ differently which could then be mapped identically to $B$ by $f$

**properties**

monomorphisms are morphisms that are injective, see [[function]]

### Epimorphism

**definition** let $f : A \to B$, let $g_1 : B \to C$ and $g_2 : B \to C$, and let $\circ$ be the [[composition]] [[operator]]. then, $f$ is an _epimorphism from $A$ to $B$._ if and only if $g_1 \circ f = g_2 \circ f \vdash g_1 = g_2$ for all $\mathcal C(B, C)\ g_1$ and $\mathcal C(B, C)\ g_2$ and for all $C$

> **note** this definition works because if the range $R$ of $f$ was a subset of its domain $B$, then there could exist two different morphisms $g_1$ and $g_2$ that would map elements in $R$ identically but would map elements in $B / R$ differently

**properties**

epimorphisms are morphisms that are surjective, see [[function]]

## Composition

**see** [[composition]]

let $f : A \to B$ and $g : B \to C$ be morphisms from $A$ to $B$ and $B$ to $C$. then, there must exist a morphism $h : A \to C$ from $A$ to $C$ that is the [[composition]] of $f$ and $g$.

composition is denoted through the [[operator]] $\circ$ in [[conventional math notation]] and read as _after_ or _then_. for example, $f \circ g$ is read as _f after g_ or _f then g_.

### Associativity Law

[[composition]] in a category is required to be associative

let $\circ$ be the [[composition]] [[operator]]. then, $h \circ (g \circ f) = (h \circ g) \circ f$

## Identities

identities are morphisms that [[map]] an object to itself. in a category, each object must have an identity morphism. the [[set]] of all identities in a category is denoted $\mathcal C(A, A) = \braket{\braket{1_A, \dots}}$ in [[conventional math notation]].

an identity is denoted $1_A: A \to A$ or as $\textbf{id}_A : A \to A$ in [[conventional math notation]].

### Identity Law

for every object $A$ there is an arrow which is a unit of [[composition]]. let $f : A \to B$ and let $\circ$ be the [[composition]] [[operator]]. then,

$f \circ \textbf{id}_A = f$

$\textbf{id}_B \circ f = f$

in Haskell, let `id :: a -> a`. then, `id x = x`

## Functors

[[functor]]s are morphisms that [[map]] a [[category]] to another [[category]]. this leads to [[category]]es of [[category]]es

to do so, they must use a pair of [[function]]s to [[map]] both objects and morphisms between the [[category]]es and preserve the identity and composition laws

## Opposite Category

> **AKA** Duality

&mdash; <https://youtu.be/Gai-liKAUPo?t=190>

**definition** for any [[category]] $\mathcal C$, one can define the _opposite category_ $\mathcal C^{op}$ by reversing all its morphisms

this can be thought of as _reversing the direction of the arrows_ in the [[graph]] the [[category]].

## Product, Coproduct

Products between objects are basically product [[type]]s

Coproducts between objects are basically sum [[type]]s

#think <https://youtu.be/Gai-liKAUPo?t=327>
