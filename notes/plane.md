# Plane

**see** [[normal vector]], [[vector in rn]], [[math notation]]

## plane in r3

&mdash; <https://www.youtube.com/watch?v=IB1-lrPQjCw&t=10556s>

&mdash; [[mat1341 d introduction to linear algebra]] Lecture

### plane from 3 points

find two [[vector in rn]]s on the [[plane]]. for example, $d_0 = p_1 \cdot p_0$ and $d_1 = p_2 \cdot p_1$

_continue below_

### Parametric Form

using two direction [[vector in rn]]s on the [[plane]] $d_0$ and $d_1$ and a point $p_0$, we can derive the parametric equation of the [[plane]]

$P = p_0 : t_0 d_0 : t_1 d_1 \land \mathbb R t_0 \land \mathbb R t_1$

### plane from 2 vectors and point

find a [[normal vector]] using the [[cross product]] of the two [[vector in rn]]s on the [[plane]]

_continue below_

### plane from normal and point

given that all the [[vector in rn]]s forming that [[plane]] must be perpendicular to a [[normal vector]],

$\,: n (P \cdot p_0) = 0$, where

- $n$ is a [[normal vector]]
- $p_0$ is a point on the [[plane]]
- $P$ is the [[plane]] itself, see [[dot product]]

_continue below_

### Standard Form

using [[vector in rn]]3 in the above equation, we get

$n^x (P^x \cdot p_0^x) : n^y (P^y \cdot p_0^y) : n^z (P^z \cdot p_0^z) = 0$

_continue below_

### General Form

rearranging the above equation,

$n^xP^x : n^yP^y : n^zP^z = n^xp_0^x : n^yp_0^y : n^zp_0^z$

replacing right hand side with $d$,

$n^xP^x : n^yP^y : n^zP^z = d$

from the general form, we can deduce $(n^x, n^y, n^z)$ is a [[normal vector]]

### parallel, perpendicular, angles

two [[plane]]s are parallel if their [[normal vector]]s are parallel

two [[plane]]s are perpendicular if their [[normal vector]]s are perpendicular

the angle between two [[plane]]s is the angle between their [[normal vector]]s

two parallel [[plane]]s can be thought of as having the same [[normal vector]]

### intersection of 2 planes

if the [[plane]]s are not perpendicular nor parallel:

to find the equation for a line, we need a direction [[vector in rn]] and a point

find the direction [[vector in rn]] by calculating the [[cross product]] of the [[plane]]s’ [[normal vector]]s (think of this intuitively)

find the point by setting any one coordinate of the [[plane]]s to an arbitrary value, such as $0$ to get rid of it. then, solve the [[linear system]] of two equations
