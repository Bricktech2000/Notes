# Graph

_a collection of vertices connected by a collection of edges_

**see** [[abstract data type]], [[dependency graph]]

**definition** _formally in my [[math notation]]_ a [[graph]] is a [[set theory]]etical incidence [[function]] that takes two vertices and returns whether an edge is connecting them; it is a [[relation]] on vertices

**definition** a _weighted graph_ is a [[graph]] **`G`** such that **`RR (G a b)`** for all **`a`** and **`b`**

**definition** an _undirected graph_ is a [[graph]] **`G`** such that **`(= rr) G`**

directionality can be "forgotten" by taking the [[relation#symmetric closure]] of the [[graph]]

**definition** in [[conventional math notation]], a _graph_ **`{V, E}`** is a [[set]] of _vertices_ **`V`** and a [[multiset]] of _edges_ **`E`** such that **`E e + 0 < V (e I) /\ V (e O)`** and **`E e == E e(+)`** (see [[relation]], [[ordered pair]])

**definition** in [[conventional math notation]], a _directed graph_ **`{V, E}`** is a [[set]] of _vertices_ **`V`** and a [[multiset]] of _edges_ **`E`** such that **`E e + 0 < V (e I) /\ V (e O)`** (see [[relation]], [[ordered pair]])

**definition** a _vertex_ or _node_ is a point in a _graph_

**definition** an _edge_ is a connection between two _vertices_

**definition** a vertex is _incident_ to an edge if the vertex is connected to the edge

**definition** two vertices are _neighbors_ if they are connected by an edge

**definition** a _path_ is a [[sequence]] of edges connecting a [[sequence]] of vertices

**definition** a _cycle_ is a _path_ that starts and ends at the same vertex

**definition** two vertices are _connected_ if there exists a _path_ between them

## vertex membership

**definition** _in my [[math notation]]_ a vertex **`v`** is in a graph **`G`** if and only if there is at least one edge incident to it; **`(\/ rr) G v + {{ }}`**

**definition** _in [[conventional math notation]]_ a vertex **`v`** is in a graph **`{V, E}`** if and only if **`V v`**

## Isomorphism

**see** [[morphism#isomorphism]]

**definition** two [[graph]]s are said to be _isomorphic_ if they have the same edges connecting their vertices, which could be labeled differently

**definition** in my [[math notation]], a _graph isomorphism_ between two [[graph]]s **`G_1`** and **`G_2`** is a [[function#bijective function]] **`f`** such that **`G_1 v w == G_2 (f v) (f w)`**

**definition** in [[conventional math notation]], a _graph isomorphism_ between two [[graph]]s **`{V_1, E_1}`** and **`{V_2, E_2}`** is a [[function#bijective function]] **`f`** from **`V_1`** to **`V_2`** such that any two vertices **`a`** and **`b`** in **`V_1`** have an edge in **`E_1`** connecting them if and only if **`f a`** and **`f b`** have an edge in **`E_2`** connecting them.

## Complete Graph

**definition** a _complete graph_ **`K^n`** is a graph with **`n`** vertices, each pair of which is connected by exactly one edge

## Connected Graph

**definition** a [[graph]] is said to be _connected_ if every pair of vertices is connected directly or indirectly by a path

**definition** a [[graph]] is said to be _disconnected_ if it is not _connected_

## Subgraph

## Supergraph

**definition** a [[graph]] **`G_1`** is a _subgraph_ of **`G_2`** if and only if it is a [[graph]] and **`/\ G_1 -| G_2`**

**definition** a [[graph]] **`G_2`** is a _supergraph_ of **`G_1`** if and only if it is a [[graph]] and **`/\ G_2 |- G_1`**

## Vertex Degree

**definition** the _degree_ of a vertex **`v`** is the number of edges incident to it, **`#G v`**

as every edge connects two vertices, the sum of the [[graph#vertex degree]]s of all vertices of a [[graph]] is an [[even number]]. if this is not the case, the [[graph]] is not a [[graph]] as at least one of its edges is not connected to two vertices

## Eulerian Path

## Eulerian Cycle

**definition** an _Eulerian path_ is a path traversing every edge of a [[graph]] exactly once

**definition** an _Eulerian cycle_ is an _Eulerian path_ that is a _cycle_

when visiting a vertex in a [[graph#eulerian path]] or [[graph#eulerian cycle]], one edge is used to enter the vertex and another is used to leave it. thus:

**theorem** a [[graph]] has an _Eulerian path_ if and only if exactly zero or exactly two of its vertices have an [[odd number]] [[graph#vertex degree]]

**theorem** a [[graph]] has an _Eulerian cycle_ if and only if every vertex has an [[even number]] [[graph#vertex degree]]

## Adjacency Matrix

**definition** the _adjacency matrix_ of a [[graph]] **`G`** is **`G`**

## Adjacency List

**definition** the _adjacency list_ of a [[graph]] **`G`** is **`G`**

> **note** a [[graph#adjacency list]] is a collection of [[set]]s. the person who came up with that name should probably be fired
