# Plane in R3

see [[normal-vector]], [[vector-in-rn]], [[math-notation]]

&mdash; <https://www.youtube.com/watch?v=IB1-lrPQjCw&t=10556s>

&mdash; [[mat1341-d-introduction-to-linear-algebra]] Lecture

## Plane From 3 Points

find two vectors on the plane. for example, $d_0 = p_1 \cdot p_0$ and $d_1 = p_2 \cdot p_1$

_continue below_

## Parametric Form

using two direction vectors on the plane $d_0$ and $d_1$ and a point $p_0$, we can derive the parametric equation of the plane

$P = p_0 : t_0 d_0 : t_1 d_1 \land \mathbb R t_0 \land \mathbb R t_1$

## Plane From 2 Vectors and Point

find a [[normal-vector]] using the [[cross-product]] of the two vectors on the plane

_continue below_

## Plane From Normal and Point

given that all the vectors forming that plane must be perpendicular to a [[normal-vector]],

$n\ \dot\mid\ P \cdot p_0 = 0$, where $n$ is a [[normal-vector]], $p_0$ is a point on the plane and $P$ is the plane itself, see [[dot-product]]

_continue below_

## Standard Form

using [[vector-in-rn]]3 in the above equation, we get

$n^x (P^x \cdot p_0^x) : n^y (P^y \cdot p_0^y) : n^z (P^z \cdot p_0^z) = 0$

_continue below_

## General Form

rearranging the above equation,

$n^xP^x : n^yP^y : n^zP^z = n^xp_0^x : n^yp_0^y : n^zp_0^z$

replacing right hand side with $d$,

$n^xP^x : n^yP^y : n^zP^z = d$

from the general form, we can deduce $(n^x, n^y, n^z)$ is a [[normal-vector]]

## Parallel, Perpendicular, Angles

two planes are parallel if their [[normal-vector]]s are parallel

two planes are perpendicular if their [[normal-vector]]s are perpendicular

the angle between two planes is the angle between their [[normal-vector]]s

two parallel planes can be thought of as having the same [[normal-vector]]

## Intersection of 2 Planes

if the planes are not perpendicular nor parallel:

to find the equation for a line, we need a direction vector and a point

find the direction vector by calculating the [[cross-product]] of the two planes’ [[normal-vector]] (think of this intuitively)

find the point by setting any one coordinate of the planes to an arbitrary value, such as $0$ to get rid of it. then, solve the system of two equations
