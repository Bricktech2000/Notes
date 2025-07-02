# Type

**see** [[type system]], [[type inference]], [[type-driven design]]

--- <https://youtu.be/6hAeJmKXRfo>

## Top Type

--- <https://en.wikipedia.org/wiki/Top_type>

**definition** the _top type_ is the [[type]] that is a [[type#supertype]] of all other [[type]]s

> **example** `Object` is [[javascript]]'s and [[java]]'s [[type#top type]] and `interface{}` is [[go]]'s [[type#top type]]

## Bottom Type

**definition** the _bottom type_ is the [[type]] that is a [[type#subtype]] of all other [[type]]s

> **example** `!` is [[rust]]'s [[type#bottom type]]

## Empty Type

--- <https://en.wikipedia.org/wiki/Empty_type>

**equiv** _[[set#empty set]]_

**definition** an _empty type_ is a [[type]] with no terms

all [[type#empty type]]s are isomorphic, and thus it is common to refer to one as _the_ [[type#empty type]]

the [[type#empty type]] can be thought of as the [[type#sum type]] of no [[type]]s

> **example** `enum {}` and `!` are [[rust]]'s [[type#empty type]]s

## Unit Type

--- <https://en.wikipedia.org/wiki/Unit_type>

**equiv** _[[set#singleton set]]_

**definition** a _unit type_ is a [[type]] with exactly one term

all [[type#unit type]]s are isomorphic, and thus it is common to refer to one as _the_ [[type#unit type]]

the [[type#unit type]] can be thought of as the [[type#product type]] of no [[type]]s

> **example** `()` is [[rust]]'s and Haskell's [[type#unit type]] and `void` is [[c]]'s [[type#unit type]]

## Subtype

## Supertype

**equiv** _[[set#subset]]_

**equiv** _[[set#superset]]_

**definition** a [[type]] `A` is a [[type#subtype]] of a [[type]] `B` if all terms of `A` are also terms of `B`

**definition** a [[type]] `A` is a [[type#supertype]] of a [[type]] `B` if all terms of `B` are also terms of `A`

**properties**

the _subtype_ [[relation]] is a [[partial order]] --- <https://youtu.be/hy1wjkcIBCU?t=1926>

## Refinement Type

--- <https://en.wikipedia.org/wiki/Refinement_type>

**definition** a _refinement type_ is a [[type]] equipped with a [[predicate]] that is assumed to hold for all terms of the refinement type

> **example**
>
> ```rust
> use non_zero_u8::*; //*
> mod non_zero_u8 {
>   pub struct NonZeroU8(u8);
>   impl NonZeroU8 {
>     pub fn new(n: u8) -> Option<Self> { (n != 0).then_some(Self(n)) }
>     pub fn get(&self) -> u8 { self.0 }
>   }
> }
> ```
>
> --- <https://youtu.be/KWB-gDVuy_I?t=375>

refinement types may be used to assert pre- and post-conditions at the [[type system]] level

## Algebraic Data Type

[[type#algebraic data type]]s are one tool for _making illegal states unrepresentable_ --- Yaron Minsky --- <https://youtu.be/2JB1_e5wZmU?t=46m16s> in [[type-driven design]]

### Sum Type

**aka** _"or" type_, _"choice" type_, Rust _`enum`_

**properties**

the [[set#cardinality]] of a [[type#sum type]] is the sum of the [[set#cardinality]]es of its constituent [[type]]s: $|A + B| = |A| + |B|$

### Product Type

**aka** _"and" type_, _`pair`_, _`struct`_

**properties**

the [[set#cardinality]] of a [[type#product type]] is the product of the [[set#cardinality]]es of its constituent [[type]]s: $|A \times B| = |A| \cdot |B|$

## Exponential Type

**aka** _function type_

--- <https://youtu.be/6hAeJmKXRfo?t=322>

the [[set#cardinality]] of a [[type#exponential type]] is the [[set#cardinality]] of its [[function#codomain]] to the power of the [[set#cardinality]] of its [[function#domain]]: $|A \to B| = |B|^{|A|}$ aka $|B^A| = |B|^{|A|}$

> **note** intuitively, to each of the $|A|$ possible inputs we associate one of $|B|$ possible outputs
