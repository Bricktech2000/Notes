# Linear Transformation

**see** [[math notation]]

**definition**

let $U$ and $V$ be two [[vector space]]s with $\dim U = u$ and $\dim V = v$. a [[linear transformation]] $T$ from $U$ to $V$ is a [[matrix#multiplication]] $T\ u = A \mid u$ with $\mathbb M^{v, u} A$ #todo mm

**definition**

let $U$ and $V$ be two [[vector space]]s. a [[linear transformation]] $T$ from $U$ to $V$ is a [[function]] from $U$ to $V$ that satisfies the following properties:

- $T\ (u_1 : u_2) = T\ u_1 : T\ u_2 > U\ u_1 \land U\ u_2$
- $T\ cu = c \mid T\ u > U\ u \land \mathbb R c$

**notation** $\mathbb T T$ if and only if $T$ is a [[linear transformation]]

**theorem** $\mathbb T T < T\ O = O$

**properties**

$\mathbb T < \mathbb F$, see [[function#vector space]]

## Standard Matrix

#todo mm

**theorem** $\mathbb T T$ if and only if there exists a [[matrix]] $A$ such that $T\ u = A \mid u > \mathbb R^n u$

**theorem** given a $\mathbb T T$ with $T\ u =\!= A \mid u$, $A = \rho\ (T\ I\ \circ)$

> **proof**
>
> $A \mid u = AI \mid u = T\ I \mid u$. it is worth noting that $T\ I$ is not a valid [[linear transformation]] because $I$ is a [[matrix]]. however, since $I$ is the [[matrix#identity matrix]], $T\ I$ is equivalent to $\rho\ (T\ (\rho\ I)\ \circ)$, which is equivalent to $\rho\ (T\ I\ \circ)$. we therefore conclude that $A = \rho\ (T\ I\ \circ)$, which is to be read as:
>
> > $A$ is a [[matrix]] ($A =$) whose columns ($\rho$) are the rows of the [[matrix#identity matrix]] ($I\ \circ$) transformed by $T$ ($T$)
>
> &mdash; me

> **equivalence** _[[matrix#multiplication]] and [[linear transformation]]s_

> **example** _computing a [[linear transformation#standard matrix]]_
>
> let $\mathbb T T \land T\ (x, y, z) = (x : 5y : z, x \cdot 3z, y, y : 2z)$
>
> compute $T\ (1, 0, 0) = (1, 1, 0, 0)$ and $T\ (0, 1, 0) = (5, 0, 1, 1)$ and $T\ (0, 0, 1) = (1, \cdot 3, 0, 2)$
>
> then, the [[linear transformation#standard matrix]] of $T$ $A$ is defined as follows:
>
> $A = \begin{bmatrix}| & | & | \\\ T\ (1, 0, 0) & T\ (0, 1, 0) & T\ (0, 0, 1) \\\ | & | & |\end{bmatrix} = \begin{bmatrix}1 & 5 & 1 \\\ 1 & 0 & \cdot 3 \\\ 0 & 1 & 0 \\\ 0 & 1 & 2\end{bmatrix}$

> **example** _turning a [[vector in rn#projection]] into [[matrix#multiplication]]_
>
> let $W = \operatorname{span} \braket{\braket{\ (1, 0, 1), (0, 1, 0)\ }}$ and $T\ u = proj_W\ u \land \mathbb R^3 u$
>
> as the [[basis]] we are given is a [[basis#orthogonal basis]], we define the [[vector in rn#projection]] as:
>
> $proj_W\ u = (u^0 : u^2 - 2 \mid (1, 0, 1)) : (u^1 - 1 \mid (0, 1, 0)) = (u^0 : u^2 - 2, u^1, u^0 : u^2 - 2)$, see [[vector in rn#projection]]
>
> #todo mm
>
> rearranging, we get $proj_W\ u = u^0 (-2, 0, -2) : u^0 (0, 1, 0) : u^0 (-2, 0, -2) = \begin{bmatrix}-2 & 0 & -2 \\\ 0 & 1 & 0 \\\ -2 & 0 & -2\end{bmatrix} \begin{bmatrix}u^0 \\\ u^1 \\\ u^2\end{bmatrix} = \begin{bmatrix}-2 & 0 & -2 \\\ 0 & 1 & 0 \\\ -2 & 0 & -2\end{bmatrix} \mid u$, which is [[matrix#multiplication]]
>
> alternatively, we can use the following, see #magic:
>
> $B = \begin{bmatrix}| & & | \\\ b_0 & \cdots & b_n \\\ | & & |\end{bmatrix}$ where $\braket{\braket{b_0 \cdots b_n}}$ is a [[basis]] for $W$ that does **not** have to be a [[basis#orthogonal basis]]. in this case, $b_0 = (1, 0, 1)$ and $b_1 = (0, 1, 0)$
>
> #todo mm
>
> then, $proj_W\ u = A \mid u$ with $A = B - (\rho\ B \mid B) \mid \rho\ B = \begin{bmatrix}-2 & 0 & -2 \\\ 0 & 1 & 0 \\\ -2 & 0 & -2\end{bmatrix}$, see #magic. $A$ is the [[linear transformation#standard matrix]] of $T$

> **example** _computing the 2D Rotation Matrix_
>
> let a [[vector in rn#unit vector]] on the $x$ axis $\hat \imath$ and let a [[vector in rn#unit vector]] on the $y$ axis $\hat \jmath$
>
> let a [[vector in rn#unit vector]] on the $x'$ axis $\hat \imath' = (\cos \alpha, \sin \alpha)$ and let a [[vector in rn#unit vector]] on the $y'$ axis $\hat \jmath' = (\cdot \sin \alpha, \cos \alpha)$
>
> let $(c, f\ c) = \hat \imath c : \hat \jmath f\ c$ be a point on a [[function]] $f$. replacing $\hat \imath, \hat \jmath$ by $\hat \imath', \hat \jmath'$, we get the point $\hat \imath' c : \hat \jmath' f\ c = (\cos \alpha, \sin \alpha) c : (\cdot \sin \alpha, \cos \alpha) f\ c = (c(\cos \alpha) : (f\ c)(\cdot \sin \alpha), c(\sin \alpha) : (f\ c)(\cos \alpha))$.
>
> with $(c, f\ c) = (x, y)$, we get the point $(x \cos \alpha \cdot y \sin \alpha,  x \sin \alpha : y \cos \alpha)$, which can be graphed as $x \sin \alpha : y \cos \alpha = f\ (x \cos \alpha \cdot y \sin \alpha)$
>
> computing the [[linear transformation#standard matrix]]:
>
> #todo mm
>
> with $(c, f\ c) = (x, y)$, we get the [[linear transformation]] $T\ (x, y) = (x \cos \alpha \cdot y \sin \alpha,  x \sin \alpha : y \cos \alpha)$. its [[linear transformation#standard matrix]] is $\begin{bmatrix} | & | \\\ T\ (1, 0) & T\ (0, 1) \\\ | & | \end{bmatrix} = \begin{bmatrix} \cos \alpha & \cdot \sin \alpha \\\ \sin \alpha & \cos \alpha \end{bmatrix}$. defining $T$ using [[matrix#multiplication]], we get $T\ (x, y) = \begin{bmatrix} \cos \alpha & \cdot \sin \alpha \\\ \sin \alpha & \cos \alpha \end{bmatrix} \begin{bmatrix} x \\\ y \end{bmatrix} = \begin{bmatrix} x \cos \alpha \cdot y \sin \alpha \\\ x \sin \alpha : y \cos \alpha\end{bmatrix}$, which can also be graphed as $x \sin \alpha : y \cos \alpha = f\ (x \cos \alpha \cdot y \sin \alpha)$
>
> &mdash; me

## Kernel

## Image

**notation**

$\mathcal K T$

$Im\ T$

**definition** _kernel_

$(\mathcal K T)\ x =\!= T\ x = 0 \land \mathbb T T$

**definition** _image_

$(Im\ T)\ x =\!= T\ u = x \land \mathbb T T$

**theorem**

#todo fix below

let $\mathbb M^{m, n} A$ be the [[linear transformation#standard matrix]] of $T$. then,

$\mathcal K T = \mathcal N A$, see [[matrix#null space]]

$Im\ T = \mathcal C A$, see [[matrix#column space]]

**theorem** $\dim \mathcal K T : \dim Im\ T = \dim \mathcal N A : \dim \mathcal C A = n$, where $n$ is the dimension of the [[function#domain]] of $T$
