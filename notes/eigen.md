# Eigen

#todo mm

## Space

## Vector

## Value

**definition**

let $\mathbb M^{n, n} A \land \mathbb N n \land \mathbb R \lambda \land \mathbb R^n x \land x + O$

if $Ax = \lambda x$, then $x$ is an [[eigen#vector]] of $A$ and $\lambda$ is its corresponding [[eigen#value]]

**theorems**

let $\mathbb M^{n, n} A \land \mathbb N n$

**theorem** there are infinitely many [[eigen#vector]]s for each [[eigen#value]]

**theorem** all [[eigen#vector]]s together with the zero [[vector]] form a [[vector space]]

**theorem** the [[characteristic polynomial]] $\det\ (A \cdot \lambda I)$ is a [[polynomial]] of degree $n$, meaning it has at most $n$ distinct roots by the [[fundamental theorem of algebra]]

**theorem** $A$ has at most $n$ distinct [[eigen#value]]s

**theorem** each [[eigen#value]] of $A$ gives an [[eigen#space]] of [[vector space#dimension]] greater than $0$

**theorem** any [[set]] consisting of [[eigen#vector]]s of $A$ corresponding to **distinct [[eigen#value]]s** is [[linearly independent]]

**procedures**

> **procedure** _finding [[eigen#value]]s_
>
> $Ax = \lambda x$
>
> rewriting into a homogeneous [[linear system]]
>
> $Ax \cdot \lambda x = O$
>
> $Ax \cdot \lambda I x = O$
>
> factoring out $x$
>
> $A \cdot \lambda I \mid x = O$
>
> the equation above is a homogeneous [[linear system]] where $A \cdot \lambda I$ is the _coefficient matrix_
>
> recall that a homogeneous [[linear system]] can have either a unique solution (with $x = O$, which is not a valid [[eigen#vector]] as per the definition) or an infinite number of solutions (which we can achieve by picking the right values for $\lambda$). for a homogeneous [[linear system]] to have an infinite number of solutions, its coefficient matrix rows (and therefore columns) must be [[linearly independent]], or the [[determinant]] of its coefficient matrix must be equal to $0$, or its coefficient matrix must be invertible, etc. (see [[matrix]])
>
> $\det\ (A \cdot \lambda I) = 0$ (this [[polynomial]] is known as the _[[characteristic polynomial]] of $A$_)
>
> solving...
>
> _using $A = \begin{bmatrix}1 & 2 \\\  2 & 1\end{bmatrix}$ as an example_
>
> $A \cdot \lambda I = \begin{bmatrix}1 & 2 \\\  2 & 1\end{bmatrix} \cdot \lambda \begin{bmatrix}1 & 0 \\\  0 & 1\end{bmatrix} = \begin{bmatrix}1 \cdot \lambda & 2 \\\  2 & 1 \cdot \lambda\end{bmatrix}$
>
> $\det\ (A \cdot \lambda I) = 0 = [1 \cdot \lambda]2 \cdot 4 = 1 \cdot \lambda : 2 \mid 1 \cdot \lambda \cdot 2 = 3 \cdot \lambda \mid \cdot 1 \cdot \lambda = 0$
>
> $\lambda =\ \ \vdots\ \ 3 \lor \cdot 1$ are the [[eigen#value]]s of $A$

> **procedure** _finding [[eigen#vector]]s_
>
> as $A \cdot \lambda I \mid x = O$, we get the following (see [[matrix#vector spaces]] Kernel):
>
> $E_\lambda = Ker\ (A \cdot \lambda I)$, where
>
> $E_\lambda$ is the _[[eigen#space]]_ of $A$ corresponding to the [[eigen#value]] $\lambda$ (this [[vector space]] is called the λ-[[eigen#space]] of $A$)
>
> the [[eigen#vector]]s of $A$ associated with the [[eigen#value]] $\lambda$ are all the nonzero [[vector]]s in $E_\lambda$. therefore, instead of finding the [[eigen#vector]]s corresponding to the known [[eigen#value]], we will find a basis for the [[eigen#space]]
>
> for $\lambda = 3$:
>
> $A \cdot 3I \mid x = O$
>
> $A \cdot 3I \mid x = \begin{bmatrix}1 & 2 \\\  2 & 1\end{bmatrix} \cdot \begin{bmatrix}3 & 0 \\\  0 & 3\end{bmatrix} \mid x = \begin{bmatrix}\cdot 2 & 2 \\\  2 & \cdot 2\end{bmatrix} \mid x = 0$
>
> therefore, we can solve the following [[linear system]] using [[row reduction]]
>
> $\begin{bmatrix}\cdot 2 & 2 & | & 0 \\\  2 & \cdot 2 & | & 0\end{bmatrix}$
>
> and we get:
>
> $x = c (1, 1) \dashv \mathbb R c$
>
> $\braket{\braket{\ (1, 1)\ }}$ is then a [[basis]] for the [[eigen#space]] $E_3$ of $A$
>
> > **note** the general solution of the homogenous [[linear system]] will always be a [[basis]] as the resulting [[vector]]s will always be [[linearly independent]], see [[matrix#vector spaces]] Kernel for more information
>
> for $\lambda = \cdot 1$, we get the [[basis]] $\braket{\braket{\ (1, \cdot 1)\ }}$ for the [[eigen#space]] $E_{\cdot 1}$ of $A$

**application**

_raising a matrix to a large power efficiently_

let $\mathbb M^{n, n} A \land \mathbb N n$ be a [[matrix#diagonalizable matrix]]

1.  construct a matrix $P = \begin{bmatrix}| & | & | \\\ x_0 & x_1 & x_2 \\\ | & | & |\end{bmatrix} = \begin{bmatrix}x_{0_x} & x_{1_x} & x_{2_x} \\\ x_{0_y} & x_{1_y} & x_{2_y} \\\ x_{0_z} & x_{1_z} & x_{2_z}\end{bmatrix}$ whose columns are the $n$ [[linearly independent]] [[eigen#vector]]s $x$ of $A$
2.  construct a matrix $D = \begin{bmatrix}\lambda_0 & 0 & 0 \\\ 0 & \lambda_1 & 0 \\\ 0 & 0 & \lambda _2\end{bmatrix}$ whose [[matrix#diagonal]] entries are the [[eigen#value]]s of $A$ and all other entries equal to $0$, in the same order as the columns of $P$

then, $AP = PD$. as the columns of $P$ are [[linearly independent]], we know $P$ is an invertible [[matrix]]. therefore, $A = PDP^-$ and $P^-AP = D$

> **proof** the $n$ th column of $AP$ is $AP^{,n} = Ax_n$. since $x_n$ is an [[eigen#vector]] of $A$, we use its corresponding [[eigen#value]] to get $AP^{,n} = Ax_n = \lambda_n x_n$ by definition, see [[eigen]]. the $n$ th column of $PD$ is $PD^{, n}$. when multiplying out, we get $PD^{, n} = x_n D^{n, n} = x_n \lambda_n$. as $AP^{,n} = PD^{,n} \dashv \mathbb N n$, we conclude $AP = PD$

now, compute $[A]p \land \mathbb N p$ with $p$ being a very large integer

with $A = PDP^-$, we get $[A]p = [PDP^-]p = P \mid [D]p \mid P^-$

as $D$ is a [[matrix#diagonal matrix]], we get $[D]p = \begin{bmatrix}[\lambda_0]p & 0 & 0 \\\ 0 & [\lambda_1]p & 0 \\\ 0 & 0 & [\lambda_2]p\end{bmatrix}$

computing $[A]p = P\begin{bmatrix}[\lambda_0]p & 0 & 0 \\\ 0 & [\lambda_1]p & 0 \\\ 0 & 0 & [\lambda_2]p\end{bmatrix}P^-$ is now way less computationally expensive than computing $[A]p$ directly

**application**

[[eigen#vector]]s and [[eigen#value]] can be useful in [[markov chain]]s &mdash; <https://www.youtube.com/watch?v=JGQe4kiPnrU>

### Multiplicity

**see** [[multiplicity]]

**definition** the _algebraic multiplicity_ of a root $\lambda$ of the [[characteristic polynomial]] of $A$ is its [[multiplicity]]

**definition** the _geometric multiplicity_ of a root $\lambda$ of the [[characteristic polynomial]] of $A$ is the [[vector space#dimension]] of the [[eigen#space]] $E_\lambda$ of $A$ corresponding to the [[eigen#value]] $\lambda$

**theorem** let $\lambda$ be an [[eigen#value]] of $A$. then, $1 \dashv \text{geometric multiplicity of \(\lambda\)} \dashv \text{algebraic multiplicity of \(\lambda\)}$

> **example** the [[characteristic polynomial]] of $\begin{bmatrix}2 & 4 & \cdot 3 \\\ 0 & 3 & 5 \\\ 0 & 0 & 3\end{bmatrix}$ is $2 \cdot \lambda \mid [3 \cdot \lambda]2$. its [[eigen#value]]s are $\lambda = 2$ and $\lambda = 3$. the algebraic [[eigen#multiplicity]] of $\lambda = 2$ is $1$ and the algebraic [[eigen#multiplicity]] of $\lambda = 3$ is $2$.

**applications**

[[eigen#multiplicity]] can be used to determine whether a [[matrix]] is a [[matrix#diagonalizable matrix]]
