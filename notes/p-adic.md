# P-Adic

_the [[set]] of $p$-adic numbers for a given prime $p$._

**see** [[math notation]]

&mdash; <https://youtu.be/3gyHKCDq1YA>

**definition**

the [[real]] numbers can only have finitely many digits to the left of the decimal point. [[p-adic]] numbers can only have finitely many digits to the right of the decimal point. [[p-adic]] integers are [[p-adic]] numbers with no digits to the right of the decimal point

**properties**

$\mathbb Q^p \vdash \mathbb U$ for any prime $p$, see [[universal]]

the [[p-adic]]s are a completion of the [[rational]]s just like the [[real]]s are a completion of the [[rational]]s

$(\dots 99999) : (\dots 00001) = (\dots 00000) = 0$ and therefore $(\dots 99999) = \cdot 1$. gererally, all negative [[integer]]s are present in the [[p-adic]] numbers

$(\dots 66667) \mid (\dots 00003) = (\dots 00001) = 1$ and therefore $(\dots 66667) = -3$. gererally, all [[rational]]s are present in the [[p-adic]] numbers (but only some [[rational]]s are present in the [[p-adic]] integers) &mdash; <https://math.stackexchange.com/questions/3876767/are-rational-numbers-also-p-adic-numbers>

[[p-adic]] numbers support division

> **note** [[p-adic]] numbers supporting division is a consequence of $p$ being a prime number &mdash; <https://youtu.be/3gyHKCDq1YA?t=606>. my [[improved expression evaluation]] would need to be extended to support $n$-adic numbers where $n$ is not a prime number #todo

> **note** [[p-adic]] numbers supporting division seems to be in [[contradiction]] with the following &mdash; me
>
> $2[5[n]]\ \ \vdots\ \ n \rightarrow \infty = 2[5[n : 1]]\ \ \vdots\ \ n \rightarrow \infty$ and therefore $x = x5$ with $x = 2[5[n]]\ \ \vdots\ \ n \rightarrow \infty$ &mdash; <https://youtu.be/3gyHKCDq1YA?t=829>
>
> dividing both sides by $x$, we get $1 = x4$. taking the fourth root on both sides, we get $1 = x$. however, acconding to <https://youtu.be/3gyHKCDq1YA?t=829>, $x = \iota$
>
> > **note** this [[contradiction]] could be eliminated by the following &mdash; me and <https://www.wolframalpha.com/input?i=1%5E%281%2F4%29>
> >
> > let $1 = x4$. taking the square root on both sides, we get $x2 =\ \ \vdots\ \ 1 \lor \cdot 1$. taking the square root on both sides again, we get $x =\ \ \vdots\ \ 1 \lor \cdot 1 \lor \iota \lor \cdot \iota$. this resolves the contradiction
> >
> > #think superposition in [[improved expression evaluation]]

## Absolute Value

[[real]]s are close when their first few digits are the same. [[p-adic]]s are close when their last few base-$p$ digits are the same, see [[positional numeral system]]

**definition**

$|n|^p = 1 - \text{highest power of \(p\) that divides \(n\)}$

> **example** $|1000|^{10} = -1000 = 0.001$

> **example** $||^p\ \ \vdots\ \ (p[n]\ \ \vdots\ \ n \rightarrow \infty) = 0$ for any $p$
