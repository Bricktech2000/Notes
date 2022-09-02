# Scope

> **definition** a _scope_ is a concept that refers to where values and functions can be accessed &mdash; <https://www.codecademy.com/learn/introduction-to-javascript/modules/learn-javascript-scope>

> **example** _Rust scope_
>
> ```rust
> fn main() {
>   let x = 1;
>   {
>     let x = 2;
>     println!("{}", x); // 2
>   }
>   println!("{}", x); // 1
> }
> ```
