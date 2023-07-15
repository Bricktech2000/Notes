# P-Adic

_the [[set]] of **`p`**-adic numbers for a given [[prime]] **`p`**_

**see** [[math notation]]

&mdash; <https://youtu.be/3gyHKCDq1YA>

**definition**

the [[real]] numbers can only have finitely many digits to the left of the decimal point. [[p-adic]] numbers can only have finitely many digits to the right of the decimal point. [[p-adic]] integers are [[p-adic]] numbers with no digits to the right of the decimal point

**properties**

**`QQ^p < UU`** for any [[prime]] **`p`**, see [[universal]]

the [[p-adic]]s are a [[metric space#completion]] of the [[rational]]s with the [[p-adic#absolute value]] [[metric space#metric]]. see [[real]]

**`...99999 : ...00001 = ...00000 = 0`** and therefore **`...99999 = .1`**. gererally, all negative [[integer]]s are present in the [[p-adic]] numbers

**`...66667 | ...00003 = ...00001 = 1`** and therefore **`...66667 = --3`**. gererally, all [[rational]]s are present in the [[p-adic]] numbers (but only some [[rational]]s are present in the [[p-adic]] integers) &mdash; <https://math.stackexchange.com/questions/3876767/are-rational-numbers-also-p-adic-numbers>

[[p-adic]] numbers support division

> **note** [[p-adic]] numbers supporting division is a consequence of **`p`** being a [[prime]] number &mdash; <https://youtu.be/3gyHKCDq1YA?t=606>. my [[improved expression evaluation]] would need to be extended to support **`n`**-adic numbers where **`n`** is not a [[prime]] number #think

> **note** [[p-adic]] numbers supporting division seems to be in [[contradiction]] with the following &mdash; me
>
> **`2[5[@@]] = 2[5[@@:1]]`** and therefore **`x = x5`** with **`x = 2[5[@@]]`** &mdash; <https://youtu.be/3gyHKCDq1YA?t=829>
>
> dividing both sides by **`x`**, we get **`1 = x4`**. taking the fourth root on both sides, we get **`1 = x`**. however, acconding to <https://youtu.be/3gyHKCDq1YA?t=829>, **`x = ii`**
>
> > **note** this [[contradiction]] could be eliminated by the following &mdash; me and <https://www.wolframalpha.com/input?i=1%5E%281%2F4%29>
> >
> > let **`1 = x4`**. taking the square root on both sides, we get **`x2 = {1 \/ .1}`**. taking the square root on both sides again, we get **`x = {1 \/ .1 \/ ii \/ .ii}`**. this resolves the contradiction
> >
> > #think superposition in [[improved expression evaluation]]

## Absolute Value

**aka** _[[p-adic]] metric_

**see** [[field#absolute value]], [[real#absolute value]]

[[real]]s are close when their first few digits are the same. [[p-adic]]s are close when their last few base-**`p`** digits are the same, see [[positional numeral system]]

**notation**

**`"abs"^p n`** with **`QQ^p n`**

**definition**

**`"abs"^p n = --p[yy n p]`**, where

- **`p[yy n p]`** is the highest power of **`p`** that divides **`n`**, see [[psi function]]
- **`"abs"^p n`** is the [[p-adic#absolute value]] of **`n`**

> **example** **`"abs"^10 1000 = -1000`**

> **example** **`p`**-adically, **`p[@@] = 0`**

> **example** **`2`**-adically, **`1 : 2 : 4 : 8 : ... = ...11111 = .1`**. more generally, **`p0 :  p1 : ... = .1`**

> **note** for the [[p-adic#absolute value]] to follow the [[field#absolute value]] [[axiom]]s, **`"abs"^p 0 = 0`** for all **`p`** &mdash; <https://youtu.be/vdjYiU6skgE?t=407>

> **note** in contrast to the [[real#absolute value]], the [[p-adic#absolute value]] only returns a "discrete" [[set]] of values **`x -> (x = p[n] /\ ZZ n \/ x = 0)`** &mdash; <https://youtu.be/vdjYiU6skgE?t=407>
