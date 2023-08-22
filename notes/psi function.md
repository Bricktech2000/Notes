# Psi Function

&mdash; MAT2348 Discrete Mathematics

**definition**

**`yy`** is a [[function]] that takes in a [[natural]] number **`n`** and returns the unique [[multiset]] of [[prime]] [[factor]]s of **`n`**

**properties**

**`| yy n = n`**

**`yy ab = yy {a : b}`**

**`a`** _divides_ **`b`** if and only if **`yy {a -| b}`**

**`n`** is a _square [[number]]_ if and only if **`EE (yy n)`**

**`n`** is a _[[prime]] [[number]]_ if and only if **`# yy n = 1`** and if and only if **`yy n = ((n,))`**

**`m`** and **`n`** are _co[[prime]]_ if and only if **`yy {m __ n} = (( ))`**

**`n = 1`** if and only if **`# yy n = 0`** and if and only if **`yy n = (( ))`**

the _greatest common divisor_ of **`a`** and **`b`** is **`| yy {a __ b}`**

the _least common multiple_ of **`a`** and **`b`** is **`| yy {a ^^ b}`**

by the [[fundamental theorem of arithmetic]], the [[psi function]] is a [[function#bijective function]]

**examples**

> **example** the [[category]] **`NN /\ +0, "divides"`** and the [[category]] **`"multiset of primes", "multisubset"`** are equivalent
>
> the [[psi function]] is a [[functor]] from the [[category]] **`NN /\ +0, "divides"`** to the [[category]] **`"multiset of primes", "multisubset"`**
>
> [[functor]]s [[map]] both [[category#morphism]]s and [[category#object]]s between [[category]]es. this means than:
>
> - [[category#product]]s in the first [[category]] represent the GCD of two [[natural]]s, and therefore [[category#product]]s in the second [[category]] represent the intersection of two [[multiset]]s
> - [[category#coproduct]]s in the first [[category]] represent the LCM of two [[natural]]s, and therefore [[category#coproduct]]s in the second [[category]] represent the union of two [[multiset]]s
> - the [[category#initial object]] in the first [[category]] represents the [[natural]] **`1`**, and therefore the [[category#initial object]] in the second [[category]] represents the empty [[multiset]] **`(( ))`**
> - the [[category#terminal object]] in the first [[category]] does not exist (it would be the [[natural]] **`0`**, which is not in **`NN /\ +0`**), and therefore the [[category#terminal object]] in the second [[category]] does not exist (it would be **`e -> @@`**, which is not a valid [[multiset]] of [[prime]]s because of its [[function#codomain]])
>
> it is also worth noting that this [[functor]] is a [[function#bijective function]] forming a [[category#isomorphism]], which means that the two [[category]]es are isomorphic
