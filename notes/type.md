# Type

**see** [[type system]]

> **note** in [[functional programming]], [[type]]s are not [[class]]es. they are simply a [[set]] (assuming [[type]]s are modeled in the [[category]] of [[set]]s) containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]]

as examples, in Haskell, type `Bool` is a two-element [[set]] of `True` and `False` and type `Char` is the [[set]] of all possible unicode [[character]]s &mdash; <https://youtu.be/aIOMRqiwziM?t=312>

## Top Type

&mdash; <https://en.wikipedia.org/wiki/Top_type>

**definition** the _top type_ is the [[type]] that is a [[type#supertype]] of all other [[type]]s

> **example** `Object` is [[javascript]]'s and [[java]]'s [[type#top type]] and `interface{}` is [[go]]'s [[type#top type]]

## Bottom Type

**definition** the _bottom type_ is the [[type]] that is a [[type#subtype]] of all other [[type]]s

> **example** `!` is [[rust]]'s [[type#bottom type]]

## Unit Type

&mdash; <https://en.wikipedia.org/wiki/Unit_type>

**definition** a _unit type_ is a [[type]] with exactly one inhabitant

all [[type#unit type]]s are isomorphic, and thus it is common to refer to one as _the_ [[type#unit type]]

the [[type#unit type]] can be thought of as the [[type#product type]] of zero [[type]]s, which is an empty tuple

> **equivalence** _[[set#singleton set]] and [[type#unit type]]_

> **example** `()` is [[rust]]'s and Haskell's [[type#unit type]] and `void` is [[c]]'s [[type#unit type]]

## Empty Type

&mdash; <https://en.wikipedia.org/wiki/Empty_type>

**definition** an _empty type_ is a [[type]] with no inhabitants

all [[type#empty type]]s are isomorphic, and thus it is common to refer to one as _the_ [[type#empty type]]

> **equivalence** _[[set#empty set]] and [[type#empty type]]_

> **example** `enum {}` and `!` are [[rust]]'s [[type#empty type]]s

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
>   Check {
>     checkNumber: CheckNumber
>   },
>   CreditCard {
>     cardType: CardType,
>     cardNumber: CardNumber,
>   },
> };
>
> type CheckNumber = u32;
>
> type CardNumber = u32;
>
> enum CardType {
>   Visa,
>   Mastercard
> };
> ```
>
> &mdash; <https://youtu.be/mRwHZTNGdoY?t=2366>
>
> &mdash; <https://youtu.be/2JB1_e5wZmU?t=23m46s>

**applications**

leveraging [[type#algebraic data type]]s allows us to _make illegal states unrepresentable_ &mdash; Yaron Minsky, &mdash; <https://youtu.be/2JB1_e5wZmU?t=46m16s>

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
