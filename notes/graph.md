# Graph

_a collection of vertices connected by a collection of edges_

**definition** _formally in my [[math notation]]_ a [[graph]] is a [[set theory]]etical [[function]] with domain at least $\braket{v, w} \rightarrow \top$ that takes an [[ordered pair]] of vertices as an index and returns whether an edge is connecting them

**definition** an _undirected graph_ is a [[graph]] $G$ such that $G = G^\intercal$

**definition** in [[conventional math notation]], a _graph_ $\braket{V, E}$ is a [[set]] of _vertices_ $V$ and a [[multiset]] of _edges_ $E$ such that $\smash\ne E\ e \vdash (V\ \acute\mid\ V)\ e$ and $E\ e \equiv E\ e^\intercal$ (see [[relation]], [[ordered pair]])

**definition** in [[conventional math notation]], a _directed graph_ $\braket{V, E}$ is a [[set]] of _vertices_ $V$ and a [[multiset]] of _edges_ $E$ such that $\smash\ne E\ e \vdash (V\ \acute\mid\ V)\ e$ (see [[relation]], [[ordered pair]])

**definition** a _vertex_ or _node_ is a point in a _graph_

**definition** an _edge_ is a connection between two _vertices_

**definition** a vertex is _incident_ to an edge if the vertex is one of the two vertices the edge connects

**representation**

below are two equivalent representations of a sample graph

![[20220718021503.png]]

![[20220718021524.png]]

## vertex membership

**definition**

_in my [[math notation]]_ a vertex $v$ is in a graph $G$ if and only if there is at least one edge incident to $v$: $G\ v \equiv G^{v,} \ne O \lor G^{, v} \ne O$

_in [[conventional math notation]]_ a vertex $v$ is in a graph $\braket{V, E}$ if and only if $V\ v$

## Graph Isomorphism

**see** [[category]], [[category theory]]

**definition** two [[graph]]s are said to be _isomorphic_ if they have the same edges connecting their vertices, which could be labelled differently

**definition** in my [[math notation]], a _graph isomorphism_ between two [[graph]]s $G_1$ and $G_2$ is a bijective [[function]] $f$ such that $G_1^{v, w} \equiv G_2^{f\ v, f\ w}$

**definition** in [[conventional math notation]], a _graph isomorphism_ between two [[graph]]s $\braket{V_1, E_1}$ and $\braket{V_2, E_2}$ is a bijective [[function]] $f$ from $V_1$ to $V_2$ such that any two vertices $a$ and $b$ in $V_1$ have an edge in $E_1$ connecting them if and only if $f\ a$ and $f\ b$ have an edge in $E_2$ connecting them.

## Complete Graph

**definition** a _complete graph_ $K^n$ is a graph with $n$ vertices, each pair of which is connected by exactly one edge

## Connected Graph

**definition** a [[graph]] is said to be _connected_ if every pair of vertices are connected directly or indirectly by a path

**definition** a [[graph]] is said to be _disconnected_ if it is not _connected_

## Subgraph

**definition** a [[graph]] $G_1$ is a _subgraph_ of $G_2$ if and only if it is a [[graph]] and $G_1^e \le G_2^e$

**definition** a [[graph]] $G_1$ is an _induced subgraph_ of $G_2$ if and only if it is a _subgraph_ of $G_2$ and $G_1\ e^\bot \land G_1\ e^\top \vdash G_1^e = G_2^e$ (the subgraph must contain all the original edges connecting its vertices)

## Vertex Degree

**definition** the _degree_ of a vertex $v$ is the number of edges incident to $v$

as every edge connects two vertices, the sum of the degrees of all vertices of a [[graph]] is an [[even number]]. if this is not the case, the [[graph]] is not a [[graph]] as at least one of its edges is not connected to two vertices

## Euler Path and Circuit

**definition** an _Euler path_ is a path traversing every edge of a [[graph]] exactly once

**definition** an _Euler circuit_ is an _Euler path_ that starts and ends at the same vertex

when visiting a vertex in an Euler path or circuit, one edge is used to go to the vertex and another edge is used to leave it. from this fact the following theorems are derived:

**theorem** a [[graph]] has an _Euler path_ if and only if exactly zero or exactly two of its vertices have an [[odd number]] degree

**theorem** a [[graph]] has an _Euler circuit_ if and only if every vertex has an [[even number]] degree
