# Hash Table

**see** [[data-structure]]

_a [[map]] implemented using a [[hash]] [[function]]_

> **AKA** hash map

time [[computational-complexity]]:

|        | Average | Worst  |
| ------ | ------- | ------ |
| Insert | $O\ 1$  | $O\ n$ |
| Remove | $O\ 1$  | $O\ n$ |
| Lookup | $O\ 1$  | $O\ n$ |

> **note** time [[computational-complexity]] is $O\ 1$ only if the [[hash]] [[function]] is uniform

**definition** the _load factor_ of a [[hash-table]] is the ratio of the number of elements in the [[hash-table]] to the number of slots in the [[hash-table]]

**definition** the _maximum load factor_ $\alpha$ of a [[hash-table]] load factor allowed before the [[hash-table]] is resized

## Hash Table Operations (Separate Chaining)

let a [[list]] of $n$ buckets (such as a [[list]], a [[tree]], a [[set]], etc.) be used to store keys and values

> **procedure** _computing the [[hash]] of a key_
>
> given a key $k$ and a [[hash]] [[function]] $H$,
>
> 1. return $H\ k \bmod n$

> **procedure** _inserting into a hash table_
>
> given a key $k$ and a value $v$,
>
> 1. _compute_ the [[hash]] $h$ of $k$
> 2. insert (or update) $k, v$ into the bucket at index $h$ in the [[list]]
> 3. _resize_ the [[hash-table]]

> **procedure** _removing from a hash table_
>
> given a key $k$,
>
> 1. _compute_ the [[hash]] $h$ of $k$
> 2. remove $k, v$ from the bucket at index $h$ in the [[list]]
> 3. _resize_ the [[hash-table]]

> **procedure** _looking up a value in a hash table_
>
> given a key $k$,
>
> 1. _compute_ the [[hash]] $h$ of $k$
> 2. look up $k$ in the bucket at index $h$ in the [[list]]
> 3. _resize_ the [[hash-table]]

## Hash Table Operations (Open Addressing)

**see** [[math-notation]]

let a [[list]] of $n$ elements be used to store keys and values

let a [[probing]] [[function]] $P$ be used to find the next bucket to probe. typically, $P$ has a cycle length of $n$.

> **procedure** _computing the [[hash]] of a key_
>
> given a key $k$ and a [[hash]] [[function]] $H$,
>
> 1. return $H\ k \bmod n$

> **procedure** _computing the next value in a probing sequence_
>
> given the current probing sequence value $i$ and a key $k$:
>
> 1. return $k : P\ i\ k \bmod n$

> **procedure** _inserting into a hash table_
>
> given a key $k$ and a value $v$,
>
> 1. _compute_ the [[hash]] $h$ of $k$
> 2. if index $h$ of the [[list]] is empty, insert (or update) $k, v$ into index $h$ of the [[list]]. otherwise, set $h$ to the next value in its _probing sequence_ and repeat this step
> 3. _resize_ the [[hash-table]]

> **procedure** _removing from a hash table_
>
> #todo this procedure is invalid when removing a key that previously caused a collision
>
> given a key $k$,
>
> 1. _compute_ the [[hash]] $h$ of $k$
> 2. if index $h$ of the [[list]] contains $k$, remove $k, v$ from index $h$ of the [[list]]. otherwise, set $h$ to the next value in its _probing sequence_ and repeat this step
> 3. _resize_ the [[hash-table]]

> **procedure** _looking up a value in a hash table_
>
> given a key $k$,
>
> 1. _compute_ the [[hash]] $h$ of $k$
> 2. if index $h$ of the [[list]] contains $k$, return the value associated with $k$. otherwise, set $h$ to the next value in its _probing sequence_ and repeat this step
> 3. _resize_ the [[hash-table]]
