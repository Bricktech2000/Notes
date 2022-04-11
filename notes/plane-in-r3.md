# Plane in R3

see [[normal-vector]], [[vector-in-rn]], [[math-notation]]

&mdash; <https://www.youtube.com/watch?v=IB1-lrPQjCw&t=10556s>

&mdash; [[mat1341-d-introduction-to-linear-algebra]] Lecture

## Plane From 3 Points

find two vectors on the plane. for example, $p_1 \circ p_0$ and $p_2 \circ p_1$

_continue below_

## Parametric Form

using two direction vectors on the plane $d_0$ and $d_1$ and a point $p_0$, we can derive the parametric equation of the plane

$P = p_0 + t_0d_0 + t_1d_1 \land \mathbb R t_0 \land \mathbb R t_1$

## Plane From 2 Vectors and Point

find a [[normal-vector]] using the [[cross-product]] of the two vectors on the plane

_continue below_

## Plane From Normal and Point

given that all the vectors forming that plane must be perpendicular to a [[normal-vector]],

$n\ |\ P \circ p_0 = 0$, where $n$ is a [[normal-vector]], $p_0$ is a point on the plane and $P$ is the plane itself (note that the $|$ operator represents a dot product, see [[math-notation]] and [[vector-in-rn]])

_continue below_

## Standard Form

using [[vector-in-rn]]3 in the above equation, we get

$n^x (P^x \circ p_0^x) \cdot n^y (P^y \circ p_0^y) \cdot n^z (P^z \circ p_0^z) = 0$ (useful when we have a normal and a point)

_continue below_

## General Form

rearranging above equation,

$n^xP^x \cdot n^yP^y \cdot n^zP^z = n^xp_0^x \cdot n^yp_0^y \cdot n^zp_0^z$

replacing right hand side with $d$,

$n^xP^x \cdot n^yP^y \cdot n^zP^z = d$

then, we can deduce $(n^x, n^y, n^z)$ is a [[normal-vector]]

## Parallel, Perpendicular, Angles

two planes are parallel if their [[normal-vector]]s are parallel

two planes are perpendicular if their [[normal-vector]]s are perpendicular

the angle between two planes is the angle between their [[normal-vector]]s

**note**

two parallel planes can be thought of as having the same [[normal-vector]]

## Intersection of 2 Planes

if the planes are not perpendicular or parallel:

to find the equation for a line, we need a direction vector and a point

find the direction vector by calculating the [[cross-product]] of the two planes’ [[normal-vector]] (think of this intuitively)

find the point, set one of the coordinates of the plane ($x, y, z$) to $0$ to get rid of it. then, solve the system of two equations
