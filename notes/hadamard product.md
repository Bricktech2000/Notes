# Hadamard Product

**see** [[vector]], [[euclidean vector]], [[matrix]], [[math notation]]

--- <http://neuralnetworksanddeeplearning.com/chap2.html#the_hadamard_product_$s_\odot_t$>

--- <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Properties>

**definition** the [[hadamard product]] of **`s`** and **`t`** is **`st`**, where **`s`** and **`t`** have the same rank and the same shape. see [[polymorphism#rank polymorphism]]

> **example** **`[]1 && 2[] | []3 && 4[] = []1 | 3 && 2 | 4[] = []3 && 8[]`**

**properties**

let **`RR k /\ MM A /\ MM B /\ MM C`**

_commutative_ **`AB = BA`**

_associative_ **`A | BC = AB | C`**

_distributive_ **`A | B : C = AB : AC`**

_distributive with [[scalar]]s_ **`kA | B = A | kB = AB | k`**

_identity_ **`I | A = A | I = A`** with **`/\/\ I * * = 1`**

_zero_ **`O | A = A | O = O`** with **`/\/\ O * * = 0`**
