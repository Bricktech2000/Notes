# Data Compression

**see** [[information theory]]

**see** [[jpeg]], [[png]], [[entropy coding]], [[run-length encoding]], [[deflate]]

[[entropy coding]] lets us separate probabilistic modeling from coding --- <https://youtu.be/cJ_rhZ9DP9k?t=3486>. once we've developed a model that predicts $\mathrm P[x_{n}|x_0 \dots x_{n-1}]$, the [[probability]] of a next symbol given all previous symbols, we can feed it into an optimal [[entropy coding]] [[algorithm]] like arithmetic coding and out pops a [[data compression]] [[algorithm]]
