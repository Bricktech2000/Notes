# Discrete Cosine Transform

**see** [[math notation]], [[fourier transform]], [[linear algebra]], [[trigonometric function]]

--- <https://youtu.be/0me3guauqOU?t=1057>

**definition**

**`CC x f = :(S (# x) f)x`**, where

- **`x`** is a signal consisting of a [[list]] of samples
- **`S n f`** is a [[list]] of **`n`** samples of the cosine wave of frequency **`f`**, defined as **`i. "cos" (i:-2--n | -2tt | f)`**
- **`CC x f`** is the "amount of" cosine wave of frequency **`f`** in the signal **`x`**

**properties**

the [[discrete cosine transform]] is a [[linear map]]

the [[discrete cosine transform]] has a [[function#inverse]], the _inverse discrete cosine transform_

> **proof**
>
> define the [[function]] **`S`** such that, given a sample count **`n`** and a [[frequency]] **`f`**, returns a [[euclidean vector]] of **`n`** samples of the first half of a cosine wave of [[frequency]] **`f`**: **`S n f = i. "cos" (i-n | -2tt | f)`**
>
> we can then redefine **`S`** to shift the samples over by **`-2n`** so the **`i`**th sample lands in the middle of the [[interval]] **`i-n -| * -| i:1--n`**: **`S n f = i. "cos" (i:-2--n | -2tt | f)`**
>
> finally, we can define the [[discrete cosine transform]] **`CC`** of **`x`** as the [[dot product]] **`CC x f = :(S (# x) f)x`**, or equivalently as the [[matrix#multiplication]] **`CC x = :(S# x)x`**. what we're basically saying here is "the **`f`**th component of the [[discrete cosine transform]] is how much our input signal **`x`** looks like the cosine wave with frequency **`f`**". note that, under my [[math notation]], **`S# x`** is both a [[list]] of [[vector]]s and a [[matrix]]
>
> something interesting worth pointing out is that all row [[vector]]s in the [[matrix]] **`S# x`** are [[vector#linearly independent vector]]s --- <https://youtu.be/0me3guauqOU?t=1217>. this can be observed by the fact that the [[discrete cosine transform]] of a cosine wave of [[natural]] frequency yields a [[vector]] with a single component
>
> since we're mapping [[vector]]s in **`RR^#x`** to [[vector]]s in **`RR^#x`** through a [[linear combination]] of **`# x`** [[vector#linearly independent vector]]s, **`RR^#x`** and the [[set]] of all **`x`** and the [[set]] of all **`CC x`** form a [[vector space#isomorphism]]. consequently, the [[linear map]] **`u -> :(S# x)u`** is invertible. another way to phrase this is that since **`S# x`** is a square [[matrix]] and its rows are [[vector#linearly independent vector]]s, it has a [[matrix#inverse]], see [[matrix#invertability]]. consequently, the [[discrete cosine transform]] has a [[function#inverse]]
