# Cross-Entropy

--- <https://youtu.be/GlYgs6v2YfU>

**see** [[information entropy]], [[information content]], [[information theory]]

**notation** $H(P, Q)$, $H(P \parallel Q)$, $H_Q(P)$, $\mathbb E_P[-\log Q]$, $\langle -\log Q \rangle_P$

**definition** the _cross-entropy_ of a [[probability distribution]] $P$ _with respect to_ a [[probability distribution]] $Q$ is $\mathrm H[P \parallel Q] = +x \in X.\ \mathrm P_P[x] \cdot \mathrm I_Q[x] = +x \in X.\ -\mathrm P_P[x] \log \mathrm P_Q[x]$

**definition** $\mathrm H[P \parallel Q] = \mathrm E_{x \sim P}[\mathrm I_Q[x]]$---the [[cross-entropy]] of $P$ with respect to $Q$ is the expected value, as weighted by $P$, of the [[information content]], as measured by $Q$, of their [[outcome]]s

an intuition is that [[cross-entropy]] is the expected length of a message over $P$ when compressed using a coding optimal for $Q$

thus [[cross-entropy]] is minimal at $P = Q$ and that minimum value is $\mathrm H[P]$ --- <https://youtu.be/GlYgs6v2YfU?t=727>
