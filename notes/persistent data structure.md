# Persistent Data Structure

**see** [[data structure]]

**definition** A _persistent data structure_ is a [[data structure]] that always preserves the previous version of itself when it is modified. Such [[data structure]]s are **effectively** immutable [&hellip;]. &mdash; Wikipedia

> **note** not to be confused with _persistent data storage_

[[persistent data structure]]s often use _structural sharing_ to improve performance

> **example** _implementing a [[stack]] as a [[persistent data structure]]_
>
> [[stack]]s can be implemented as a [[persistent data structure]] through a [[linked list]]. each `Stack` is a `top` element and a `Stack` `tail`, eventually pointing to an `EmptyStack` (see [[polymorphism]]). example visual representation below.
>
> ![[20220520161901.png]]
>
> only immutable types must be pushed to the [[stack]] to conserve the illusion of the [[stack]]'s immutability.
>
> &mdash; <https://youtu.be/APUCMSPiNh4?t=2830>

## examples

### git

Git is a type of [[persistent data structure]], as every commit is appended to the end of list of commits without changing any of the previous commits.

### blockchain

the [[blockchain]] used in [[cryptocurrency]]es is a type of [[persistent data structure]], as every block is appended to the end of the chain without changing any of the previous blocks.

## &mdash;

<https://youtu.be/APUCMSPiNh4>
