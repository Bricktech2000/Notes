# Combinatory Logic

**see** [[lambda-calculus]], [[math notation]], [[combinator]]

**properties**

the [[combinator#s combinator]] and the [[combinator#k combinator]] can be composed to produce [[combinator]]s that are extentionally equal to any [[lambda-calculus]] term. consequently, **`S, K`** [[combinatory logic]] is [[turing complete]]

---

# Constructions

--- <https://youtu.be/gnrSedVucXs>

## Booleans

**equiv** _[[boolean algebra]]_

[[boolean]] values and [[boolean#operators]] can be defined as follows, see [[lambda-calculus#church booleans]]:

- **`"true" = x. y. x = K`**
- **`"false" = x. y. y = K I`**

we can then define:

- **`"not" = p. p "false" "true" = C (T "false") "true"`**

## Pairs

**equiv** _[[ordered pair]]_

[[ordered pair]]s can be defined as follows, see [[lambda-calculus#pairs]]:

- **`"pair" = x. y. z. z x y = B C T`**
- **`"fst" = p. p "true" = T "true"`**
- **`"snd" = p. p "false" = T "false"`**

## Naturals

**equiv** _[[natural]]s_

[[natural]] numbers can be defined as follows:

- **`"zero" = "pair" "true" "false"`** (equivalent to **`I`**)
- **`"succ" = n. "pair" "false" n = "pair" "false"`**

we can then define:

- **`"pred" = n. "snd" n = "snd"`**
- **`"iszero" = n. "fst" n = "fst"`**
