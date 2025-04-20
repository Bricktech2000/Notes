# Hadamard Product

_multiplication [[under]] [[polymorphism#rank polymorphism]]_

**see** [[vector]], [[euclidean vector]], [[matrix]]

--- <http://neuralnetworksanddeeplearning.com/chap2.html#the_hadamard_product_$s_\odot_t$>

--- <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)#Properties>

**definition** $s \odot t = {}_{i.\ } s_it_i$ over all dimensions, where $s$ and $t$ have the same shape

> **example** $\begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix} \odot \begin{bmatrix}5 & 6 \\ 7 & 8\end{bmatrix} = \begin{bmatrix}5 & 12 \\ 21 & 32\end{bmatrix}$

**properties** _for all [[real]] $k$ and [[matrix]]es $A, B, C$_

_commutative_ $A \odot B = B \odot A$

_associative_ $A \odot (B \odot C) = (A \odot B) \odot C$

_distributive over addition_ $A \odot (B + C) = (A \odot B) + (A \odot C)$

_distributive over [[scalar]] multiplication_ $k(A \odot B) = kA \odot B = A \odot kB$

_identity_ $1 \odot A = A \odot 1 = A$ where $\forall i.\ 1_i = 1$

_annihilation_ $0 \odot A = A \odot 0 = 0$ where $\forall i.\ 0_i = 0$
