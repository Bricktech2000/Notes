# Type

**see** [[type system]]

> **note** in [[functional programming]], [[type]]s are not [[class]]es. they are simply a [[set]] (assuming [[type]]s are modeled in the [[category]] of [[set]]s) containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]]

as examples, in Haskell, type `Bool` is a two-element [[set]] of `True` and `False` and type `Char` is the [[set]] of all possible unicode [[character]]s &mdash; <https://youtu.be/aIOMRqiwziM?t=312>

## Top Type

&mdash; <https://en.wikipedia.org/wiki/Top_type>

**definition** the _top type_ is the [[type]] that is a [[type#supertype]] of all other [[type]]s

> **equivalence** _[[set#universal set]] and [[type#top type]]_

> **example** `Object` is [[javascript]]'s and [[java]]'s [[type#top type]] and `interface{}` is [[go]]'s [[type#top type]]

## Bottom Type

**definition** the _bottom type_ is the [[type]] that is a [[type#subtype]] of all other [[type]]s

> **equivalence** _[[set#empty set]] and [[type#bottom type]]_

> **example** `!` is [[rust]]'s [[type#bottom type]]

## Unit Type

&mdash; <https://en.wikipedia.org/wiki/Unit_type>

**definition** a _unit type_ is a [[type]] with exactly one inhabitant

all [[type#unit type]]s are isomorphic, and thus it is common to refer to one as _the_ [[type#unit type]]

the [[type#unit type]] can be thought of as the [[type#product type]] of zero [[type]]s, which is an empty tuple

> **equivalence** _[[set#singleton set]] and [[type#unit type]]_

> **example** `()` is [[rust]]'s and Haskell's [[type#unit type]] and `void` is [[c]]'s [[type#unit type]]

## Subtype

## Supertype

**definition** a [[type]] `A` is a [[type#subtype]] of a [[type]] `B` if all inhabitants of `A` are also inhabitants of `B`

**definition** a [[type]] `A` is a [[type#supertype]] of a [[type]] `B` if all inhabitants of `B` are also inhabitants of `A`

> **equivalence** _[[set#subset]] and [[type#subtype]]_

> **equivalence** _[[set#superset]] and [[type#supertype]]_

**properties**

the _subtype_ [[relation]] is a [[partial order]] &mdash; <https://youtu.be/hy1wjkcIBCU?t=1926>

## Algebraic Data Type

[[type]]s can be used with [[composition]] to create new [[type]]s. however, unlike with [[function]]s, they can be combined in two distinct ways

> **example** _ADT [[composition]]_
>
> ```rust
> enum PaymentMethod {
>   Cash,
>   Check { checkNumber: u32 },
>   CreditCard {
>     cardType: CardType,
>     cardNumber: String,
>   },
> };
>
> enum CardType {
>   Visa,
>   Mastercard
> };
>
> enum PaymentAmount {
>   EUR(u32),
>   CAD(u32),
> };
>
> struct Payment {
>   amount: PaymentAmount,
>   method: PaymentMethod,
> };
> ```
>
> &mdash; <https://youtu.be/mRwHZTNGdoY?t=2366>

**applications**

algebraic data [[type]]s can be used in [[programming language]]s to make invalid states unrepresentable by only modeling valid states

### Sum Type

**aka** _"or" type_

> **equivalence** _[[type#sum type]] and [[rust]] `enum`_

**properties**

the [[set#cardinality]] of a [[type#sum type]] is the sum of the [[set#cardinality]]es of its constituent [[type]]s

### Product Type

**aka** _"and" type, "choice" type, `pair`, `struct`_

> **equivalence** _[[type#product type]] and [[rust]] `struct`_

**properties**

the [[set#cardinality]] of a [[type#product type]] is the product of the [[set#cardinality]]es of its constituent [[type]]s
