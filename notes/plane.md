# Plane

**see** [[normal vector]], [[euclidean vector]], [[math notation]]

## plane in r3

--- <https://www.youtube.com/watch?v=IB1-lrPQjCw&t=10556s>

--- MAT1341 Introduction to Linear Algebra

### plane from 3 points

find two [[euclidean vector]]s on the [[plane]]. for example, **`d_0 = p_1 . p_0`** and **`d_1 = p_2 . p_1`**

_continue below_

### Parametric Form

using two direction [[euclidean vector]]s on the [[plane]] **`d_0`** and **`d_1`** and a point **`p_0`**, we can derive the parametric equation of the [[plane]]

**`P = p_0 : t_0 d_0 : t_1 d_1 /\ RR {t_0 /\ t_1}`**

### plane from 2 vectors and point

find a [[normal vector]] using the [[cross product]] of the two [[euclidean vector]]s on the [[plane]]

_continue below_

### plane from normal and point

given that all the [[euclidean vector]]s forming that [[plane]] must be perpendicular to a [[normal vector]],

**`:n(P . p_0) = 0`**, where

- **`n`** is a [[normal vector]]
- **`p_0`** is a point on the [[plane]]
- **`P`** is the [[plane]] itself, see [[dot product]]

_continue below_

### Standard Form

using [[euclidean vector]]3 in the above equation, we get

**`n^0 (P^0 . p_0^0) : n^1 (P^1 . p_0^1) : n^2 (P^2 . p_0^2) = 0`**

_continue below_

### General Form

rearranging the above equation,

**`n^0 P^0 : n^1 P^1 : n^2 P^2 = n^0 p_0^0 : n^1 p_0^1 : n^2 p_0^2`**

replacing right hand side with **`d`**,

**`n^0 P^0 : n^1 P^1 : n^2 P^2 = d`**

from the general form, we can deduce **`(n^0 , n^1 , n^2)`** is a [[normal vector]]

### parallel, perpendicular, angles

two [[plane]]s are parallel if their [[normal vector]]s are parallel

two [[plane]]s are perpendicular if their [[normal vector]]s are perpendicular

the angle between two [[plane]]s is the angle between their [[normal vector]]s

two parallel [[plane]]s can be thought of as having the same [[normal vector]]

### intersection of 2 planes

if the [[plane]]s are not perpendicular nor parallel:

to find the equation for a line, we need a direction [[euclidean vector]] and a point

find the direction [[euclidean vector]] by calculating the [[cross product]] of the [[plane]]s' [[normal vector]]s (think of this intuitively)

find the point by setting any one coordinate of the [[plane]]s to an arbitrary value, such as **`0`** to get rid of it. then, solve the [[linear system]] of two equations
