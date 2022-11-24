# Binary Search Tree

**see** [[tree]], [[tree#binary tree]], binary [[tree#binary tree traversal]]

**definition** a _binary search tree_ is a [[tree]] that supports the [[binary search tree#invariant]]

time [[computational complexity]]:

|        | Average              | Worst  |
| ------ | -------------------- | ------ |
| Insert | $O\ \lceil n \rceil$ | $O\ n$ |
| Remove | $O\ \lceil n \rceil$ | $O\ n$ |
| Search | $O\ \lceil n \rceil$ | $O\ n$ |

## Operations

> **procedure** _finding an element in a [[binary search tree]]_
>
> 1. if $n$ is `None`, stop
> 2. compare $v$ to the value of $n$
> 3. set $n$ to $n$'s left or right child according to the [[binary search tree#invariant]]
> 4. repeat until the value of $n$ is $v$

> **procedure** _inserting a node into a [[binary search tree]]_
>
> given a [[tree]] root node $n$ and a value $v$ to be inserted,
>
> 1. compare $v$ to the value of $n$
> 2. set $n$ to $n$'s left or right child to preserve the [[binary search tree#invariant]]
> 3. repeat until $n$ is `None`
> 4. insert $v$ as a new node at $n$

> **procedure** _removing a node from a [[binary search tree]]_
>
> given a [[tree]] root node $n$ and a value $v$ to be removed,
>
> 1. _find_ the node with value $v$ in the [[tree]] $n$
> 2. replace the value of the node with value $v$ with the value of its _successor_ if it exists
> 3. _remove_ the successor node if it exists (recursively if desired)

> **procedure** _finding the successor of a node in a [[binary search tree]]_
>
> given a [[tree]] node $n$,
>
> - if $n$ has no children, return `None`
> - if $n$ has a right or left child only, return that child
> - if $n$ has two children, return either:
>   - the leftmost node of $n$'s right subtree (the smallest value in the right subtree)
>   - the rightmost node of $n$'s left subtree (the largest value in the left subtree)

## Invariant

> **aka** [[binary search tree#invariant]]

**definition** the _binary search tree invariant_ is a property of [[tree]]s that requires every node to have a left sub[[tree]] with values no greater than its value and a right sub[[tree]] with values no less than its value

**applications**

used in the implementation of some [[map]] and [[set]] [[abstract data type]]s
