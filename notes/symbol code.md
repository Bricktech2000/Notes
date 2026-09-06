# Symbol Code

--- <https://youtu.be/eHGqNvkL4n4>

--- <https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality>

**see** [[information theory]], [[data compression]], [[entropy coding]]

**see** [[information content]], [[information entropy]], [[huffman coding]]

**definition** a _symbol code_ is a map $c : \Sigma \to \{0, 1\}^*$ from the _symbols_ of an _alphabet_ $\Sigma$ to [[binary]] [[string]]s called _codewords_; see [[monoid#free monoid]]

we may overload $c$ to _words_ by defining $c\ (w \in \Sigma^*) = c\ xyz\cdots := (c\ x)(c\ y)(c\ z)\cdots$

**definition** a [[symbol code]] is called _uniquely decodable_ when and only when $\forall u, v \in \Sigma^*.\ u \neq v \to c\ u \ne c\ v$, that is, $c$ on words is a [[function#injective function]]

**theorem** _Kraft--McMillian inequality_ if a [[symbol code]] is uniquely decodable then $+x \in X.\ \overline \exp_2\ |c\ x| \leq 1$

the Kraft--McMillian inequality witnesses that unique decodability constrains the length of codewords. there's a budget to be spent on codewords, with shorter words being more expensive

**definition** a _prefix code_ is a [[symbol code]] satisfying $\forall x, y \in \Sigma.\ \forall w \in \{0, 1\}^+.\ (c\ x) \neq (c\ y)w$---no codeword is a prefix of another codeword

this implies $\forall u, v \in \Sigma^*.\ \forall w \in \{0, 1\}^+.\ (c\ u) \neq (c\ v)w$ by induction

prefix code are uniquely decodable. importantly, they are easy to decode. they can be represented as [[tree#binary tree]]s whose leaves are the symbols of the alphabet. the encoding of a symbol is its path from the root

**representation** _a (complete) prefix-free [[symbol code]]_

![[../references/Screenshot From 2026-08-29 22-48-25.png]] --- <https://youtu.be/l6DKRf-fAAM?t=602>

**theorem** _Kraft inequality_ $+i.\ \overline \exp_2\ \ell_i \leq 1$ if and only if there exists a prefix code with codeword lengths $\ell$

and thus for any uniquely decodable [[symbol code]] there is a prefix code with the same codeword lengths --- <https://youtu.be/cJ_rhZ9DP9k?t=293>

**definition** the _expected codeword length_ of a [[symbol code]] $c$ under a [[probability distribution]] $X$ is $L = \mathrm E_{x \sim X}[\,|c\ x|\,] = +x \in X.\ |c\ x| \mathrm P[x]$

any uniquely decodable [[symbol code]] for a [[probability distribution]] $X$ satisfies $L \geq \mathrm H[X]$

$L = \mathrm H[X]$ if and only if $\forall x \in X.\ |c\ x| = \mathrm I[x]$. when the [[information content]] of every [[outcome]] is a [[natural]], there exists such a $c$ that is uniquely decodable

for any [[probability distribution]] $X$ there is an optimal uniquely decodable [[symbol code]] satisfying $\mathrm H[X] \leq L < \mathrm H[X] + 1$. [[huffman coding]] constructs such optimal [[symbol code]]s
