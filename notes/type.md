# Type

> **note** in [[functional programming]], [[type]]s are not [[class]]es. they are simply a [[set]] (assuming [[type]]s are modeled in the [[category]] of [[set]]s) containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]].

as examples, in Haskell, type `Bool` is a two-element [[set]] of `True` and `False` and type `Char` is a [[set]] of all possible unicode characters. &mdash; <https://youtu.be/aIOMRqiwziM?t=312>

## Algebraic Data Type

[[type]]s can be used with [[composition]] to create new [[type]]s. however, unlike with [[function]]s, they can be combined in two distinct ways.

> **example** _ADT [[composition]]_
>
> ```Rust
> enum PaymentMethod {
>   Cash,
>   Check { checkNumber: u32 },
>   CreditCard {
>     cardType: enum CardType {
>       Visa,
>       Mastercard
>     },
>     cardNumber (String),
>   },
> };
>
> enum PaymentAmount {
>   EUR(u32),
>   CAD(u32),
> }
>
> struct Payment {
>   amount: PaymentAmount,
>   method: PaymentMethod,
> }
> ```

**applications**

algebraic data [[type]]s can be used in [[programming language]]s to make invalid states unrepresentable by only modeling valid states

### Sum Type

#todo **equivalence** with [[rust]]

_`enum` in [[rust]]_

> **aka** "or" type

### Product Type

#todo **equivalence** with [[rust]]

_`struct` in [[rust]]_

> **aka** "and" type, "choice" type, `pair`, `struct`
