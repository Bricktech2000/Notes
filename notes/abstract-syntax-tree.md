# Abstract Syntax Tree

_an intermediate representation for a [[programming-language]]_

&mdash; <https://youtu.be/4m7ubrdbWQU?t=429>

> **representation**:
>
> `7 + 3 * 4` can be represented using the following [[abstract-syntax-tree]]:
>
> ```mermaid
> graph TD;
> A(+)
> B(7)
> C(*)
> D(3)
> E(4)
> A --> B
> A --> C
> C --> D
> C --> E
> ```

> **representation**:
>
> `7 + 3 * 4` can be compiled to the following [[JavaScript]] representation:
>
> ```javascript
> ({
>   type: 'BinaryExpression',
>   operator: '+',
>   left: {
>     type: 'NumericLiteral',
>     value: 7,
>   },
>   right: {
>     type: 'BinaryExpression',
>     operator: '*',
>     left: {
>       type: 'NumericLiteral',
>       value: 3,
>     },
>     right: {
>       type: 'NumericLiteral',
>       value: 4,
>     },
>   },
> });
> ```
