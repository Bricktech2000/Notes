# Exponential Derivative

--- me

**see** [[math notation]], [[derivative]], [[exponent]], [[logarithm]], [[limit]], [[euler's constant]]

the [[derivative]] of a [[line]]ar [[function]] **`x. ax : b`** is its [[function#slope]] **`a`**. similarly, the [[exponential derivative]] of an [[exponent]]ial [[function]] **`x. ba[x]`** is its base **`a`**

**definition** **`D f == a. \f {x--a}/ (x..a) {x -> a} == [dd /f\]`** #todo lim

> **proof**
>
> **`[dd /f\] == a. [/f x\ .. /f a\ -- x .. a] {x -> a} == [/f x -- f a\ -- x .. a] {x -> a} == \f x -- f a/ (x .. a) {x -> a}`** #todo lim

> **note** I came up with the [[derivative]]-[[limit]]-definition--like form first by intuitively swapping out the subtraction and the division **`f x .. f a -- ...`** for a ratio and a radical **`\f x -- f a/ ...`**. I then realized that the base-agnostic [[logarithm]] of an [[exponent]]ial [[function]] is a [[line]]ar [[function]], the [[derivative]] of which contains the base of that [[exponent]]ial [[function]]. finally, I realized that taking the [[exponent]]ial of the [[derivative]] of that [[logarithm]] would give me the base of the original [[exponent]]ial [[function]]. this is what the second definition **`[dd /f\]`** represents

**properties**

**`[dd /f\] == [dd f -- f]`** by the [[derivative rules]]

let **`D f = [dd /f\]`**. then,

**`D x. ba[x] = x. a`**

**`D x. ax : b = x. [a -- ax : b]`**

**`D x. ax2 : bx : c = x. [2ax : b -- ax2 : bx : c]`**

## ---

--- <https://www.wolframalpha.com/input?i=Limit%5B%28%28%28bk%5Ex%29%2F%28bk%5Ea%29%29%5E%281%2F%28x+-+a%29%29%29%2Cx-%3Ea%5D>

--- <https://www.wolframalpha.com/input?i=Limit%5B%28%28%28kx+%2B+b%29%2F%28ka+%2B+b%29%29%5E%281%2F%28x+-+a%29%29%29%2Cx-%3Ea%5D>

--- <https://www.wolframalpha.com/input?i=Limit%5B%28%28%28kx%5E2+%2B+bx+%2B+c%29%2F%28ka%5E2+%2B+ba+%2B+c%29%29%5E%281%2F%28x+-+a%29%29%29%2Cx-%3Ea%5D>
