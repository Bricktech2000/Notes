# Linked List

**see** [[data-structure]]

_a [[list]] where each element points to the next (and optionally previous) element_

time [[computational-complexity]]:

|                                | Singly-Linked | Doubly-Linked |
| ------------------------------ | ------------- | ------------- |
| Search                         | $\Omicron\ n$ | $\Omicron\ n$ |
| isEmpty                        | $\Omicron\ 1$ | $\Omicron\ 1$ |
| Contains                       | $\Omicron\ n$ | $\Omicron\ n$ |
| Insert / Remove / Peek at head | $\Omicron\ 1$ | $\Omicron\ 1$ |
| Insert / Remove / Peek at tail | $\Omicron\ n$ | $\Omicron\ 1$ |
| Insert / Remove / Peek at mid  | $\Omicron\ n$ | $\Omicron\ n$ |

**representation** _Singly-Linked List_

```mermaid
graph LR
  A(HEAD) --> B(element) --> C(element) --> D(element) --> E(TAIL)
```

**representation** _Doubly Linked List_

```mermaid
graph LR
 A(HEAD) --> B(element) --> C(element) --> D(element) --> E(TAIL)
 E --> D --> C --> B --> A
```

**applications**

can be used to implement [[list]]s, [[queue]]s and [[stack]]s because of their efficient insertion and deletion [[computational-complexity]]

can be used in [[hash-table]] implementations to deal with [[hash]] collisions

often used in the implementation of adjacency lists for [[graph]]s
