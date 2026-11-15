# Entropy Coding

--- <https://en.wikipedia.org/wiki/Entropy_coding>

--- <https://en.wikipedia.org/wiki/Arithmetic_coding>

**see** [[symbol code]], [[huffman coding]], [[arithmetic coding]]

**definition** _In [[information theory]], an [[entropy coding]] (or entropy encoding) is any lossless [[data compression]] method that attempts to approach the lower bound declared by Shannon's source coding theorem [...]._ --- Wikipedia

in the best possible case, $\forall w \in \Sigma^*.\ |c\ x| = \mathrm I[x]$. _$\mathrm I[x]$ is the compressed file length to which we should aspire_ --- <https://youtu.be/y5VdtQSqiAI?t=849>

the problem with [[symbol code]]s is that, even when optimal, their _expected codeword length_ can be up to one bit above the [[information entropy]]. with a message of length $N$, that's $N$ bits above entropy. for example, [[symbol code]]s can't devote less than one bit per source symbol even though in practice, with context-dependent modeling, it's often the case that the predictive distribution is very certain and the symbol to be coded has near-zero [[information content]]. --- <https://youtu.be/cJ_rhZ9DP9k?t=1260>

_arithmetic coding_ gets around this. to every [[string]] $w$ over some alphabet $\Sigma$ we can associate a sub[[interval]] of $[0, 1)$ $i\ w$ satisfying $\forall x \in \Sigma.\ i\ wx \subseteq i\ w$ and $|i\ w| = \mathrm P[w]$. for the source [[string]], $\mathrm P[w]$ comes from the probabilistic model, and for the coded [[binary]] [[string]], $\mathrm P[w] = \overline \exp_2\ |w|$. --- me. then, _we encode entire file---not just one character, the whole file---by transmitting a binary string whose interval lies within the source string's interval_ --- <https://youtu.be/cJ_rhZ9DP9k?t=2523>. arithmetic coding is almost optimal, satisfying $\forall w \in \Sigma^*.\ |c\ w| \leq \mathrm I[w] + 2$; the extra $2$ bits is because the coded [[binary]] [[string]]'s [[interval]] may have to be up to four times smaller than the source [[string]]'s [[interval]] to lie within it --- <https://youtu.be/cJ_rhZ9DP9k?t=3206>

**representation** _source and coded invervals of arithmetic coding_

![[../references/Screenshot From 2026-08-29 16-29-13.png]] --- <https://youtu.be/cJ_rhZ9DP9k?t=2523>

an alternative is _asymmetric numeral systems_, a family of [[entropy coding]] schemes introduced in 2014 that combines the near-optimality of arithmetic coding with the computational speed of [[huffman coding]] --- <https://en.wikipedia.org/wiki/Asymmetric_numeral_systems>
