# Kullback--Leibler Divergence

--- <https://youtu.be/GlYgs6v2YfU?t=1894>

**see** [[cross-entropy]], [[information entropy]], [[information content]]

**definition** $\mathrm{D_{KL}}[P \parallel Q] = +x \in X.\ \mathrm H[P \parallel Q] - \mathrm H[P \parallel P] = +x \in X.\ \mathrm P_P[x] \log \frac{\mathrm P_P[x]}{\mathrm P_Q[x]}$

an intuition is that [[kullback--leibler divergence]] is the expected excess length of a message over $P$ when compressed using a coding optimal for $Q$ instead of $P$

**theorem** _Gibbs' inequality_ $\mathrm{D_KL}[P \parallel Q] \geq 0$, and $\mathrm{D_KL}[P \parallel Q] = 0 \iff P = Q$
