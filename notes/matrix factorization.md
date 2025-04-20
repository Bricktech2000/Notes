# Matrix Factorization

**see** [[linear algebra]], [[optimization]], [[gradient#descent]]

> **note** this note was original; only later did I realize [[matrix factorization]] was already in use in recommender systems. for more information, see <https://en.wikipedia.org/wiki/Matrix_factorization_(recommender_systems)> and <https://sifter.org/~simon/journal/20061211.html> "Netflix Update: Try This at Home" by Simon Funk

some measures of "closeness" or "relatedness" between objects break transitivity. friendships are an example; someone may like different people for different reasons. [[dot product]]s tend to measure similarity, which gives rise to the idea of representing the objects as [[euclidean vector]]s in some latent [[vector space]]

**definition** $\min_{S, T}\ l$ with $l = \frac + \# (ST^\top - G)^{\circ 2}$, where

- $S$ is a [[list]] of source [[euclidean vector]]s
- $T$ is a [[list]] of target [[euclidean vector]]s
- $G$ is a rating [[matrix]] or rating [[graph]]
- $l$ is the [[loss function#mean squared error]] between $G$ and the prediction $ST^\top$

the source and target [[euclidean vector]]s may not match in number but must match in [[vector space#dimension]]. and of course, the higher their [[vector space#dimension]], the more expressive the model, but the more likely overfitting is to occur

$\frac{\mathrm d l}{\mathrm d S} = \frac{2}{\# G} (ST^\top - G) T$ and $\frac{\mathrm d l}{\mathrm d T} = \frac{2}{\# G} (ST^\top - G)^\top S$ --- me and <https://github.com/Bricktech2000/Autodiff>, and from there [[gradient#descent]] can be used for the [[optimization]] of $l$ for some $G$, parameterized by $S$ and $T$

**applications**

> **example** if $G_{p\ b}$ is how difficult person $p$ finds bouldering problem $b$, then $S$ is people's abilities and $T$ is problems' difficulties and $S_pT_b^\top$ is the expected difficulty of problem $b$ for person $p$

> **example** if $G$ is a weighted directed [[graph]] of how much people like eachother, then $S$ is people's preferences and $T$ is people's attributes and choosing $a$ and $b$ maximizing similar $S_aT_b^\top$ and $S_bT_a^\top$, say using a harmonic [[mean]] like with $\max_{a, b}\ \frac 1 \cdot \frac + \# \frac 1 \cdot\  (S_aT_b^\top, S_bT_a^\top)$, gives likely friendships
