# Linked List

**see** [[data structure]]

_a [[list]] where each element points to the next (and optionally previous) element_

time [[computational complexity]]:

|                                | Singly-Linked | Doubly-Linked |
| ------------------------------ | ------------- | ------------- |
| Search                         | **`O (*)`**   | **`O (*)`**   |
| isEmpty                        | **`O ->1`**   | **`O ->1`**   |
| Contains                       | **`O (*)`**   | **`O (*)`**   |
| Insert / Remove / Peek at head | **`O ->1`**   | **`O ->1`**   |
| Insert / Remove / Peek at tail | **`O (*)`**   | **`O ->1`**   |
| Insert / Remove / Peek at mid  | **`O (*)`**   | **`O (*)`**   |

**representation** _Singly-Linked List_

```mermaid
graph LR
  HEAD --> E1(element) --> E2(element) --> E3(element) --> TAIL
```

**representation** _Doubly Linked List_

```mermaid
graph LR
  HEAD --> E1(element) --> E2(element) --> E3(element) --> TAIL
  TAIL --> E3 --> E2 --> E1 --> HEAD
```

**applications**

can be used to implement [[list]]s, [[queue]]s and [[stack]]s because of their efficient insertion and deletion [[computational complexity]]

can be used in [[hash table#operations (separate chaining)]] implementations to deal with [[hash#collision]]s

often used in the implementation of adjacency lists for [[graph]]s
