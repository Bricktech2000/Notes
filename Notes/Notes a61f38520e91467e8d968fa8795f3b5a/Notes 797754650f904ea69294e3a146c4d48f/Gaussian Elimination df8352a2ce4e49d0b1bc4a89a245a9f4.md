# Gaussian Elimination

*a process for putting a matrix in reduced row echelon form*

see [Linear System](Linear%20System%20e82ac17271f149e28a79944967d9c2c6.md), [Linear Equation](Linear%20Equation%2078b86d9cec314c4e9a56c8e9c226a439.md), [Matrix](Matrix%206026e6fbedbc408786c22ac9d716a282.md)

## algorithm

*eliminate $x_0$ from all lines below $L_0$, eliminate $x_1$ from all lines below $L_1$, and so on*

- if the matrix is zero, stop. if one row remains, stop.
- bring a non-zero entry to the first row of the left-most non-zero column
- annihilate the rest of the column using the first row
- ignore the first row and go back to the first step

the matrix is now in REF. to get it in RREF,

*make all pivots be a $1$. make all pivot columns contain only zeros (apart from their pivot)*

- if the right-most pivot is in the first row, stop
- multiply the row containing the right-most pivot by a scalar to make the pivot a $1$
- take this pivot to annihilate all other entries in the column
- ignore the row with the right-most pivot and go back to the first step