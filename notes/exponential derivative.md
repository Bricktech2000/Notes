# Exponential Derivative

**see** [[math notation]], [[derivative]], [[exponent]], [[logarithm]], [[limit]], [[euler's constant]]

the [[derivative]] of a [[line]]ar [[function]] $x \rightarrow ax : b$ is its [[function#slope]] $a$. similarly, the [[exponential derivative]] of an [[exponent]]ial [[function]] $x \rightarrow ba[x]$ is its base $a$

**definition** $D\ f =\!= x \rightarrow \lfloor f\ x - f\ a \rfloor (x \cdot a)\ \ \vdots\ \ x \rightarrow a =\!= x \rightarrow [\delta\ \lceil f\ x \rceil - \delta x]$

> **proof**
>
> $\begin{align*} & [\delta\ \lceil f\ x \rceil - \delta x] \\\ =\!= & [\lceil f\ x \rceil \cdot \lceil f\ a \rceil - x \cdot a]\ \ \vdots\ \ x \rightarrow a \\\ =\!= & [\lceil f\ x - f\ a \rceil - x \cdot a]\ \ \vdots\ \ x \rightarrow a \\\ =\!= & \lfloor f\ x - f\ a \rfloor (x \cdot a)\ \ \vdots\ \ x \rightarrow a \end{align*}$

> **note** this is not actually a thing, I made it up. I came up with the [[derivative]]-[[limit]]-definition&ndash;like form first by intuitively swapping out the subtraction and the division $f\ x \cdot f\ a - \dots$ for a ratio and a radical $\lfloor f\ x - f\ a \rfloor \dots$. I then realized that the base-agnostic [[logarithm]] of an [[exponent]]ial [[function]] is a [[line]]ar [[function]], the [[derivative]] of which contains the base of that [[exponent]]ial [[function]]. finally, I realized that taking the [[exponent]]ial of the [[derivative]] of that [[logarithm]] would give me the base of the original [[exponent]]ial [[function]]. this is what the second definition $[\delta\ \lceil f\ x \rceil - \delta x]$ represents

**properties**

$[\delta\ \lceil f\ x \rceil - \delta x] =\!= [\delta\ f\ x - \delta x - f\ x]$ by the [[derivative rules]]

let $D\ f = x \rightarrow [\delta\ \lceil f\ x \rceil - \delta x]$. then,

$D\ (x \rightarrow ba[x]) = x \rightarrow a$

$D\ (x \rightarrow ax : b) = x \rightarrow [a - ax : b]$

$D\ (x \rightarrow ax2 : bx : c) = x \rightarrow [2ax : b - ax2 : bx : c]$

## &mdash;

<https://www.wolframalpha.com/input?i=Limit%5B%28%28%28bk%5Ex%29%2F%28bk%5Ea%29%29%5E%281%2F%28x+-+a%29%29%29%2Cx-%3Ea%5D>

<https://www.wolframalpha.com/input?i=Limit%5B%28%28%28kx+%2B+b%29%2F%28ka+%2B+b%29%29%5E%281%2F%28x+-+a%29%29%29%2Cx-%3Ea%5D>

<https://www.wolframalpha.com/input?i=Limit%5B%28%28%28kx%5E2+%2B+bx+%2B+c%29%2F%28ka%5E2+%2B+ba+%2B+c%29%29%5E%281%2F%28x+-+a%29%29%29%2Cx-%3Ea%5D>
