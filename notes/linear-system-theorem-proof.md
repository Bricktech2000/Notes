# Linear System Theorem Proof

see backlink

- $1 \to 2$

  each column represents a variable

  every variable is a leading variable $\to$ there is a leading $1$ in each column of the [[RREF]] of $A$

- $2 \to 3$

  $Ax = 0$ is homogeneous $\to$ the system is consistent

  no free variables $\to$ there cannot be infinitely many solutions $\to$ it must have a single solution

- $3 \to 4$

  $Ax = 0$ has a unique solution $\to$ $x = O$ $\to$ $A^{,j}x^j \cdot \dots A^{,j}x^j = 0$ has a unique solution (all coefficients are $0$) $\to$ the columns of $A$ are [[linearly-independent]]

- $4 \to 5$

  the columns of $A$ are [[linearly-independent]] $\to$ $Ax = 0$ has a unique solution ($x = O$) $\to$ the [[matrix|null-space]] of $A$ is the set containing the zero [[vector]]

- $5 \to 6$

  the [[matrix|null-space]] of $A$ is the [[zero-space]] $\to$ the dimension of the [[zero-space]] is $0$

- $6 \to 7$

  $\dim Null\ A \cdot rank\ A = \text{number of columns in } A$ (see [[matrix]]) $\to$ as $\dim Null\ A = 0$, $rank\ A = \text{number of columns in } A = n$

- $7 \to 1$

  the [[matrix|rank]] of a [[matrix]] is the number leading variables in the matrix

  $rank\ A = n$ and $A$ has $n$ columns $\to$ every variable is a leading variable
