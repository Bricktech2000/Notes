# Type

**see** [[type system]]

> **note** in [[functional programming]], [[type]]s are not [[class]]es. they are simply a [[set]] (assuming [[type]]s are modeled in the [[category]] of [[set]]s) containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]]

as examples, in Haskell, type `Bool` is a two-element [[set]] of `True` and `False` and type `Char` is the [[set]] of all possible [[unicode]] [[character]]s --- <https://youtu.be/aIOMRqiwziM?t=312>

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

[[type#algebraic data type]]s are one tool for _making illegal states unrepresentable_ --- Yaron Minsky --- <https://youtu.be/2JB1_e5wZmU?t=46m16s>

> **resource** _Domain Modeling Made Functional_, and why [[type#algebraic data type]]s matter --- <https://youtu.be/2JB1_e5wZmU>

> **example** _ADT [[composition]]_
>
> ```rust
> struct Payment {
>   amount: PaymentAmount,
>   method: PaymentMethod,
> };
>
> enum PaymentAmount {
>   EUR(u32),
>   CAD(u32),
> };
>
> enum PaymentMethod {
>   Cash,
>   Check(CheckNumber),
>   CreditCard(CardType, CardNumber),
> };
>
> struct CheckNumber(u32);
>
> struct CardNumber(u32);
>
> enum CardType {
>   Visa,
>   Mastercard
> };
> ```
>
> --- <https://youtu.be/mRwHZTNGdoY?t=2366>
>
> --- <https://youtu.be/2JB1_e5wZmU?t=23m46s>

### Sum Type

**aka** _"or" type_, _"choice" type_, Rust _`enum`_

**properties**

the [[set#cardinality]] of a [[type#sum type]] is the sum of the [[set#cardinality]]es of its constituent [[type]]s

### Product Type

**aka** _"and" type_, _`pair`_, _`struct`_

**properties**

the [[set#cardinality]] of a [[type#product type]] is the product of the [[set#cardinality]]es of its constituent [[type]]s
