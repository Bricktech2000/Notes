# Tree

**see** [[abstract-data-type]]

**definition** a _tree_ is a [[graph]] in which every node has exactly one parent, except for the _root node_, which has no parent &mdash; <https://en.wikipedia.org/wiki/Tree_(data_structure)>

> **note** in certain cases, it can be useful to set the parent of the _root node_ to itself

**definition** a _binary tree_ is a [[tree]] in which every node has at most two children, which are referred to as the _left child_ and the _right child_ &mdash; <https://en.wikipedia.org/wiki/Binary_tree>

binary [[tree]]s can be implemented using a dynamic [[array]], where a node at index $i$ has its children at indices $2i : 1$ and $2i : 2$ and its parent at index $\operatorname{floor} i \text- 2$

**definition** a _complete binary tree_ is a binary [[tree]] in which every level of the [[tree]] is completely filled, except for possibly the last level, and all nodes in the last level are as far left as possible &mdash; <https://en.wikipedia.org/wiki/Binary_tree>

**definition** a _leaf_ is a node in a [[tree]] that has no children

**definition** the _root_ of a [[tree]] is the only node that has no parent (the node at the top of the [[tree]])

**definition** the _height_ of a [[tree]] is the number of edges on the longest path between the root and a leaf

**definition** a _subtree_ is a [[tree]] that is entirely contained within another [[tree]]

> **note** _subtrees_ can consist of a single node

**properties**

[[tree]]s have no cycles
