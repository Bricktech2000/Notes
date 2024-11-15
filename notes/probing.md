# Probing

**see** [[math notation]]

probing [[function]]s include:

- linear probing: **`i k -> ai`**
- quadratic probing: **`i k -> ai2 : bi`**
- double hashing: **`i k -> i | H_2  k`**, where **`H_2`** is a secondary [[hash]] [[function]]
- PRNG: **`i k -> i | "PRNG" (H k) i`**, where **`"PRNG" (H k) i`** is a PRNG with seed **`H k`** and initial state **`i`**

> **note** double hashing reduces to linear probing at runtime when the value of **`k`** is known

## Cycle Length

**see** [[set]]

**definition** the _cycle length_ of a [[probing]] [[function]] **`P i k`** given a [[list]] length **`n`** is the minimum number of iterations of **`"mod" n (P i k)`** that must be performed before the sequence repeats.

the cycle length of a linear [[probing]] [[function]] **`i -> ai`** modulo **`n`** is **`n`** if and only if **`yy a __ yy n = (( ))`** , see [[psi function]] --- <https://youtu.be/RBSGKlAvoiM?t=17369>

the [[probing]] [[function]] **`i -> i`** is popular because it has a cycle length of **`n`** for any **`n`**

the cycle length of a quadratic [[probing]] [[function]] **`i -> ai2 : bi`** modulo **`n`** can be difficult to compute. a few examples of quadratic [[probing]] [[function]]s with cycle lengths of **`n`** are: --- <https://youtu.be/RBSGKlAvoiM?t=18191>

- **`i -> i2`** with **`n |- 4 /\ # yy n = 1`** (cycle length is not **`n`** and therefore it must be the case that **`aa -| -2`**, see [[hash table]])
- **`i -> i2 : i -- 2`** with **`n = 2[k] /\ NN k`**
- **`i -> [.1]x | x2`** with **`# yy n = 1 /\ "mod" n 4 = 3`**

the cycle length of a double hashing [[probing]] [[function]] **`i -> i | H_2  k`** modulo **`n`** is **`n`** if and only if **`yy (H_2  k) __ yy n = (( ))`**, see [[psi function]] --- <https://youtu.be/RBSGKlAvoiM?t=18571>. to prevent cycles of length less than **`n`**, a few solutions are available:

- choose an **`n`** such that **`# yy n = 1`**. comupte **`DD = "mod" n (H_2 k) ^^ c`** where **`c`** is a non-zero constant to ensure **`DD + 0`**. since **`n`** is [[prime]], this ensures **`yy DD __ yy n = (( ))`**. the value to be returned from the [[probing]] [[function]] is **`DD`**
