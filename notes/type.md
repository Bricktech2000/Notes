# Type

in [[functional-programming]], [[type]]s are not [[class]]es. they are simply a [[set]] containing all possible values that can be used with a given [[function]]. no behavior is defined in a [[type]].

## Algebraic Data Types

[[type]]s can be used with [[composition]] to create new [[type]]s. however, unlike with [[function]]s, they can be combined in two distinct ways.

### Sum Type

_`enum` in Rust_

> **AKA**: "or" type

### Product Type

_`struct` in Rust_

> **AKA**: "or" type, "choice" type

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

[[complete]]
