# Matrix Factorization

**see** [[math notation]], [[linear algebra]]

> **note** this note is original; only later did I realize [[matrix factorization]] was well-known in the context of recommender systems. see <https://en.wikipedia.org/wiki/Matrix_factorization_(recommender_systems)> and <https://sifter.org/~simon/journal/20061211.html> for more information

some measures of "closeness" or "relatedness" between objects break transitivity. friendships are an example; someone may like different people for different reasons. [[dot product]]s tend to measure similarity, which gives rise to the idea of representing the objects as [[euclidean vector]]s in a high-dimensional space

**definition** _through [[matrix#multiplication]]_

**`L = S(rr T) .. G`** #todo mm and **`l = ::L2 -- # {ST}`**, where

- **`S`** is the [[list]] of source [[euclidean vector]]s
- **`T`** is the [[list]] of target [[euclidean vector]]s
- **`G`** is the measured scores [[matrix]]
- **`L`** is the cost/error/loss [[matrix]]
- **`l`** is the [[loss function#mean squared error]] of **`L`**

the higher the [[vector space#dimension]] of the source and target [[euclidean vector]]s, the more accurate the representation

> **note** **`#rr {S = T}`** is required but **`# {S = T}`** is not; see [[matrix#multiplication]]

both **`dd S. l`** and **`dd T. l`** are trivially computable, meaning [[gradient#descent]] can be used for the [[optimization]] of **`S`** and **`T`** given **`G`**. the [[algorithm]] has time [[computational complexity]] quadratic in the [[vector space#dimension]] of the source and target [[euclidean vector]]s and linear in their number

**applications**

> **example** if **`G p b`** represents how difficult person **`p`** finds bouldering problem **`b`**, then **`S`** represents people's abilities and **`T`** represents problems' difficulties and **`:(S p)(T b)`** is the expected difficulty of problem **`b`** for person **`p`**

> **example** if **`G`** is a weighted directed [[graph]] representing how much one person likes another, then **`S`** represents people's preferences and **`T`** represents people's qualities and choosing **`a`** and **`b`** maximizing similar **`:(S a)(T b)`** and **`:(S b)(T a)`** gives a dating app
