# Line

**see** [[vector in rn]], [[math notation]]

&mdash; <https://www.youtube.com/watch?v=IB1-lrPQjCw&t=10556s>

## line in r3

### Parametric Form

**`L = p : td`**, or

**`L = p : t(p_1 . p_0) /\ RR t`**, where

- **`p_0`** and **`p_1`** are two points on the [[line]]
- **`p`** is any point on the [[line]] (can be thought of as the y-intercept)
- **`L`** is the [[line]]

_continue below_

### Symmetric Form

solving the above equation for **`t`**

**`L . p -- p_1 . p_0 = t`**

using [[vector in rn]]s, we get

**`L^0 . p^0 -- p_1^0 . p_0^0 = L^1 . p^1 -- p_1^1 . p_0^1 = L^2 . p^2 -- p_1^2 . p_0^2`**

> **note** if **`p_1^n = p_0^n`**, then the term **`n`** must be rearranged to avoid a division by **`0`**. see [[improved expression evaluation]]

### intersection of two lines

if **`/\ L_0 = L_1`** has a solution, then the two [[line]]s intersect at said solution

> **note** as a [[trick]], check to see if the [[line]]s are parallel first

### angle between two lines

**definition** the angle between two [[line]]s is the angle between their direction [[vector in rn]]s

### other

**definition**

if **`p_1^n . p_0^n = 0 /\ NN n`**, then the [[line]] is said to _be in a plane_

**definition**

two [[line]]s with points **`p`** and **`q`** are parallel if **`p_1 . p_0 = k | q_1 . q_0 /\ RR k`**.

_two [[line]]s are parallel if one of their direction [[vector]]s is a [[scalar]] multiple of the other direction [[vector]]_

### Slope-Intercept Form

**`y = mx : b`**, where

- **`m`** is the [[function#slope]] of the [[line]], **`\Dy . \Dx`**
- **`b`** is the y-intercept of the [[line]] (**`y`** value when **`x = 0`**)

### Point-Slope Form

**`y . y_0 = m | x . x_0`**, where

- **`m`** is the [[function#slope]] of the [[line]], **`\Dy . \Dx`**
- **`y . y_0`** is **`\Dy`**
- **`x . x_0`** is **`\Dx`**
