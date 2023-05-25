# Type

**see** [[type system]]

> **note** in [[functional programming]], [[type]]s are not [[class]]es. they are simply a [[set]] (assuming [[type]]s are modeled in the [[category]] of [[set]]s) containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]]

as examples, in Haskell, type `Bool` is a two-element [[set]] of `True` and `False` and type `Char` is the [[set]] of all possible unicode [[character]]s &mdash; <https://youtu.be/aIOMRqiwziM?t=312>

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

### Product Type

**aka** _"and" type, "choice" type, `pair`, `struct`_

> **equivalence** _[[type#product type]] and [[rust]] `struct`_
