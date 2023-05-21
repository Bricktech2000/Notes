# Root of Unity

**aka** _De Moivre numbers_

**see** [[complex]] numbers

**definition** an **`n`**th [[root of unity]] is a [[complex]] number **`z`** such that **`[z]n = 1 /\ NN n`**

**definition** an **`n`**th [[root of unity]] **`z`** is said to be _primitive_ if **`NN m /\ m -| n . 1 < [z]m + 1`**

**theorem** if **`# yy n = 1`**, then all **`n`**th [[root of unity]]s except **`1`** are primitive, see [[psi function]]

**theorem** **`[z]n = 1 == z = [ii'k-n'tt] /\ NN k`** &mdash; <https://tauday.com/tau-manifesto>

**properties**

every **`n`**th [[root of unity]] is a primitive **`a`**th [[root of unity]] for some **`a -| n`**

any [[integer]] power of an **`n`**th [[root of unity]] is also an **`n`**th [[root of unity]]

> **proof** **`[z]n = 1 == [[z]n]k = [1]k = 1 == [[z]k]n = [1]k = 1`**. by definition, both **`z`** and **`[z]k`** are [[root of unity]]s

if **`z`** is an **`n`**th [[root of unity]] and **`"mod" n {a = b}`**, then **`[z]a = [z]b`**

> **proof** let **`ZZ k`**. then, **`[z]a = z[b : kn] = [z]b [[z]n]k = [z]b[1]k = [z]b`**

let **`z`** be a primitive **`n`**th [[root of unity]]. then, **`z0 ... z[n.1]`** are all **`n`**th [[root of unity]]s and are all distinct

> **proof** if **`[z]a = [z]b`** with **`0 -| a {-|/\+} b -| n .1`**, then **`[z]b -- [z]a = 1 = z[b.a]`**, which would imply that **`z`** is not primitive

since an **`n`**th degree [[polynomial]] equation over a [[field]] (in this case the [[field]] of [[complex]] numbers) has at most **`n`** solutions by the [[fundamental theorem of algebra]], **`z0 ... z[n.1]`** are all of the **`n`**th [[root of unity]]s

the [[set]] of all [[root of unity]]s and the [[set]] of all **`n`**th [[root of unity]]s both form an [[abelian group]] under multiplication. the [[group]] of **`n`**th [[root of unity]]s form the cyclic [[group]] of [[group#order]] **`n`** &mdash; <https://en.wikipedia.org/wiki/Root_of_unity#Group_properties>

**applications**

discrete [[fourier transform]]

## &mdash;

&mdash; <https://youtu.be/bOXCLR3Wric?t=1986>

&mdash; <https://en.wikipedia.org/wiki/Root_of_unity>
