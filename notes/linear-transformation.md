# Linear Transformation

see [[math-notation]]

## definition

let $U$ and $V$ be two [[vector-space]]s. a [[linear-transformation]] $T$ from $U$ to $V$ is a [[function]] from $U$ to $V$ that satisfies the following properties:

- $T\ (u_1 : u_2) = T\ u_1 : T\ u_2 \dashv U\ u_1 \land U\ u_2$
- $T\ cu = c \mid T\ u \dashv U\ u \land \mathbb R c$

$\mathbb T T$ if and only if $T$ is a [[linear-transformation]]

> **theorem**: $\mathbb T T \vdash T\ O = O$

## properties

$\mathbb T \vdash \mathbb F$, see [[function-vector-space]]

## examples

let the [[matrix]] $\mathbb M^{m, n} A$ and let $(T\ u = A \mid u) \land \mathbb R^n u$. prove $\mathbb T T$

> **proof**:
>
> let $\mathbb R^n u_1 \land \mathbb R^n u_2$. we then have $T\ (u_1 : u_2) = A \mid u_1 : u_2$. distributing, we get $T\ u_1 : T\ u_2 = A \smash\shortmid u_1 : A \smash\shortmid u_2$
>
> let $\mathbb R^n u \land \mathbb R c$. we then have $T\ cu = A \mid cu$. commutating, we get $c \mid T\ u = c \mid A \smash\shortmid u$.

[[vector-in-rn]] projections are [[linear-transformation]]s

## Standard Matrix

> **theorem**: for any $\mathbb T T$, there exists a [[matrix]] $A$ such that $(T\ u = A \mid u) \dashv \mathbb R^n u$. in other words, any [[linear-transformation]] can be represented as a [[matrix]] multiplication

> **note**: $A \ne \varnothing \not \vdash \mathbb T T$ (the existence of such a [[matrix]] $A$ does not imply that $T$ is a [[linear-transformation]])

in the theorem above, $A = \begin{bmatrix}| & & | \\\ T\ b_0 & \dots & T\ b_n \\\ | & & |\end{bmatrix}$ where $\lbrace b_0 \dots b_n \rbrace$ is the standard [[basis]] for $\mathbb R^n$, see #magic. $A$ is the _standard [[matrix]]_ of the [[linear-transformation]] $T$

### example

_computing the standard matrix_

let $\mathbb T T \land T\ (x, y, z) = (x : 5y : z, x \cdot 3z, y, y : 2z)$

compute $T\ (1, 0, 0) = (1, 1, 0, 0)$ and $T\ (0, 1, 0) = (5, 0, 1, 1)$ and $T\ (0, 0, 1) = (1, \cdot 3, 0, 2)$

then, the _standard [[matrix]]_ of $T$ $A$ is defined as follows:

$A = \begin{bmatrix}| & | & | \\\ T\ (1, 0, 0) & T\ (0, 1, 0) & T\ (0, 0, 1) \\\ | & | & |\end{bmatrix} = \begin{bmatrix}1 & 5 & 1 \\\ 1 & 0 & \cdot 3 \\\ 0 & 1 & 0 \\\ 0 & 1 & 2\end{bmatrix}$

### Projection to Matrix Multiplication

let $W = \operatorname{span} \lbrace (1, 0, 1), (0, 1, 0) \rbrace$ and $T\ u = proj_W\ u \land \mathbb R^3 u$

as the [[basis]] we are given is orthogonal, we define the projection as:

$proj_W\ u = (u^x : u^z - 2 \mid (1, 0, 1)) : (u^y - 1 \mid (0, 1, 0)) = (u^x : u^z - 2, u^y, u^x : u^z - 2)$ (see [[vector-in-rn]])

rearranging, we get $proj_W\ u = u^x (-2, 0, -2) : u^y (0, 1, 0) : u^z (-2, 0, -2) = \begin{bmatrix}-2 & 0 & -2 \\\ 0 & 1 & 0 \\\ -2 & 0 & -2\end{bmatrix} \begin{bmatrix}u^x \\\ u^y \\\ u^z\end{bmatrix} = \begin{bmatrix}-2 & 0 & -2 \\\ 0 & 1 & 0 \\\ -2 & 0 & -2\end{bmatrix} \mid u$, which is [[matrix]] multiplication

alternatively, we can use the following, see #magic:

$B = \begin{bmatrix}| & & | \\\ b_0 & \dots & b_n \\\ | & & |\end{bmatrix}$ where $\lbrace b_0 \dots b_n \rbrace$ is a [[basis]] for $W$ that does **not** have to be orthogonal. in this case, $b_0 = (1, 0, 1)$ and $b_1 = (0, 1, 0)$

then, $proj_W\ u = A \mid u$ with $A = B (B^\intercal B)^- B^\intercal = \begin{bmatrix}-2 & 0 & -2 \\\ 0 & 1 & 0 \\\ -2 & 0 & -2\end{bmatrix}$, see #magic. $A$ is the _standard [[matrix]]_ of the [[linear-transformation]] $T$

### computing the 2D Rotation Matrix

let a unit [[vector]] on the $x$ axis $\hat \imath$ and let a unit [[vector]] on the $y$ axis $\hat \jmath$

let a unit [[vector]] on the $x'$ axis $\hat \imath' = (\cos \alpha, \sin \alpha)$ and let a unit [[vector]] on the $y'$ axis $\hat \jmath' = (\cdot \sin \alpha, \cos \alpha)$

let $(c, f\ c) = \hat \imath c : \hat \jmath f\ c$ be a point on a [[function]] $f$. replacing $\hat \imath, \hat \jmath$ by $\hat \imath', \hat \jmath'$, we get the point $\hat \imath' c : \hat \jmath' f\ c = (\cos \alpha, \sin \alpha) c : (\cdot \sin \alpha, \cos \alpha) f\ c = (c(\cos \alpha) : (f\ c)(\cdot \sin \alpha), c(\sin \alpha) : (f\ c)(\cos \alpha))$.

with $(c, f\ c) = (x, y)$, we get the point $(x \cos \alpha \cdot y \sin \alpha,  x \sin \alpha : y \cos \alpha)$, which can be graphed as $x \sin \alpha : y \cos \alpha = f\ (x \cos \alpha \cdot y \sin \alpha)$

computing the standard [[matrix]] of the [[linear-transformation]]:

with $(c, f\ c) = (x, y)$, we get the [[linear-transformation]] $T\ (x, y) = (x \cos \alpha \cdot y \sin \alpha,  x \sin \alpha : y \cos \alpha)$. its standard [[matrix]] is $\begin{bmatrix} | & | \\\ T\ (1, 0) & T\ (0, 1) \\\ | & | \end{bmatrix} = \begin{bmatrix} \cos \alpha & \cdot \sin \alpha \\\ \sin \alpha & \cos \alpha \end{bmatrix}$. defining $T$ using [[matrix]] multiplication, we get $T\ (x, y) = \begin{bmatrix} \cos \alpha & \cdot \sin \alpha \\\ \sin \alpha & \cos \alpha \end{bmatrix} \begin{bmatrix} x \\\ y \end{bmatrix} = \begin{bmatrix} x \cos \alpha \cdot y \sin \alpha \\\ x \sin \alpha : y \cos \alpha\end{bmatrix}$, which can also be graphed as $x \sin \alpha : y \cos \alpha = f\ (x \cos \alpha \cdot y \sin \alpha)$

&mdash; me

## Kernel, Image (Range)

### notation

$Ker\ T$

$Im\ T$

### definition

$(Ker\ T)\ x \equiv T\ x = 0 \land \mathbb T T$

$(Im\ T)\ x \equiv T\ u = x \land \mathbb T T \land \mathbb U u$, see [[universal]]

### properties

let $\mathbb M^{m, n} A$ be the _standard [[matrix]]_ of the [[linear-transformation]] $T$

> **theorem**:
>
> $Ker\ T = Null\ A$, see [[matrix]] null space
>
> $Im\ T = Col\ A$, see [[matrix]] column space

> **theorem**: $\dim Ker\ T : \dim Im\ T = \dim Null\ A : \dim Col\ A = n$, where $n$ is the dimension of the domain of $T$
