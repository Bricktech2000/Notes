# Type

in [[functional-programming]], [[type]]s are not [[class]]es. they are simply a [[set]] containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]].

as examples, in Haskell, type `Bool` is a two-element [[set]] of `True` and `False` and type `Char` is a [[set]] of all possible unicode characters. &mdash; <https://youtu.be/aIOMRqiwziM?t=312>

## Algebraic Data Types

[[type]]s can be used with [[composition]] to create new [[type]]s. however, unlike with [[function]]s, they can be combined in two distinct ways.

### Sum Type

_`enum` in Rust_

> **AKA**: "or" type

### Product Type

_`struct` in Rust_

> **AKA**: "and" type, "choice" type, `pair`, `struct`

### example of ADT [[composition]]

```Rust
enum PaymentMethod {
  Cash,
  Check { checkNumber: u32 },
  CreditCard {
    cardType: enum CardType {
      Visa,
      Mastercard
    },
    cardNumber (String),
  },
};

enum PaymentAmount {
  EUR(u32),
  CAD(u32),
}

struct Payment {
  amount: PaymentAmount,
  method: PaymentMethod,
}
```
