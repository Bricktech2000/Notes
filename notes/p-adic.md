# P-Adic

_the [[set]] of $p$-adic numbers for a given prime $p$_

**see** [[math notation]]

&mdash; <https://youtu.be/3gyHKCDq1YA>

**definition**

the [[real]] numbers can only have finitely many digits to the left of the decimal point. [[p-adic]] numbers can only have finitely many digits to the right of the decimal point. [[p-adic]] integers are [[p-adic]] numbers with no digits to the right of the decimal point

**properties**

$\mathbb Q^p < \mathbb U$ for any prime $p$, see [[universal]]

the [[p-adic]]s are a [[metric space#completion]] of the [[rational]]s with the [[p-adic#absolute value]] [[metric space#metric]]. see [[real]]

$\dots 99999 : \dots 00001 = \dots 00000 = 0$ and therefore $\dots 99999 = \cdot 1$. gererally, all negative [[integer]]s are present in the [[p-adic]] numbers

$\dots 66667 \mid \dots 00003 = \dots 00001 = 1$ and therefore $\dots 66667 = -3$. gererally, all [[rational]]s are present in the [[p-adic]] numbers (but only some [[rational]]s are present in the [[p-adic]] integers) &mdash; <https://math.stackexchange.com/questions/3876767/are-rational-numbers-also-p-adic-numbers>

[[p-adic]] numbers support division

> **note** [[p-adic]] numbers supporting division is a consequence of $p$ being a prime number &mdash; <https://youtu.be/3gyHKCDq1YA?t=606>. my [[improved expression evaluation]] would need to be extended to support $n$-adic numbers where $n$ is not a prime number #think

> **note** [[p-adic]] numbers supporting division seems to be in [[contradiction]] with the following &mdash; me
>
> $2[5[n]]\ \braket{n \rightarrow \infty} = 2[5[n : 1]]\ \braket{n \rightarrow \infty}$ and therefore $x = x5$ with $x = 2[5[n]]\ \braket{n \rightarrow \infty}$ &mdash; <https://youtu.be/3gyHKCDq1YA?t=829>
>
> dividing both sides by $x$, we get $1 = x4$. taking the fourth root on both sides, we get $1 = x$. however, acconding to <https://youtu.be/3gyHKCDq1YA?t=829>, $x = \iota$
>
> > **note** this [[contradiction]] could be eliminated by the following &mdash; me and <https://www.wolframalpha.com/input?i=1%5E%281%2F4%29>
> >
> > let $1 = x4$. taking the square root on both sides, we get $x2 = \braket{1 \lor \cdot 1}$. taking the square root on both sides again, we get $x = \braket{1 \lor \cdot 1 \lor \iota \lor \cdot \iota}$. this resolves the contradiction
> >
> > #think superposition in [[improved expression evaluation]]

## Absolute Value

**aka** _[[p-adic]] metric_

**see** [[field#absolute value]], [[real#absolute value]]

[[real]]s are close when their first few digits are the same. [[p-adic]]s are close when their last few base-$p$ digits are the same, see [[positional numeral system]]

**notation**

$|n|^p$ with $\mathbb Q^p n$

**definition**

$|n|^p = -p[\psi\ n\ p]$, where

- $p[\psi\ n\ p]$ is the highest power of $p$ that divides $n$, see [[psi function in mat2348]]
- $|n|^p$ is the [[p-adic#absolute value]] of $n$

> **example** $|1000|^{10} = \text-1000$

> **example** $p$-adically, $p[n]\ \braket{n \rightarrow \infty} = 0$

> **example** $2$-adically, $1 : 2 : 4 : 8 : \cdots = \dots 11111 = \cdot 1$. more generally, $p0 :  p1 : \cdots = \cdot 1$

> **note** for the [[p-adic#absolute value]] to follow the [[field#absolute value]] [[axiom]]s, $|0|^p = 0$ for all $p$ &mdash; <https://youtu.be/vdjYiU6skgE?t=407>

> **note** in contrast to the [[real#absolute value]], the [[p-adic#absolute value]] only returns a "discrete" [[set]] of values $x \rightarrow x = p[n] \land \mathbb Z n \lor x = 0$ &mdash; <https://youtu.be/vdjYiU6skgE?t=407>
