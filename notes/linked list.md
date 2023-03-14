# Linked List

**see** [[data structure]]

_a [[list]] where each element points to the next (and optionally previous) element_

time [[computational complexity]]:

|                                | Singly-Linked | Doubly-Linked |
| ------------------------------ | ------------- | ------------- |
| Search                         | $O\ \circ$    | $O\ \circ$    |
| isEmpty                        | $O\ 1$        | $O\ 1$        |
| Contains                       | $O\ \circ$    | $O\ \circ$    |
| Insert / Remove / Peek at head | $O\ 1$        | $O\ 1$        |
| Insert / Remove / Peek at tail | $O\ \circ$    | $O\ 1$        |
| Insert / Remove / Peek at mid  | $O\ \circ$    | $O\ \circ$    |

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

can be used to implement [[list]]s, [[queue]]s and [[stack]]s because of their efficient insertion and deletion [[computational complexity]]

can be used in [[hash table#operations (separate chaining)]] implementations to deal with [[hash#collision]]s

often used in the implementation of adjacency lists for [[graph]]s
