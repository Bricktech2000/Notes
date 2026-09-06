# Information Content

--- <https://www.youtube.com/@JakobFoerster/videos>

**aka** _self-information_, _surprisal_, _Shannon information_

**see** [[symbol code]]

**definition** the _information content_ $\mathrm I[x]$ of an [[outcome]] $x$ is $\mathrm I[x] = -\log_b \mathrm P[x]$. with $b = 2$ it is measured in [[shannon]]s; with $b = e$ it is measured in [[nat]]s

**definition** the _information content_ $\mathrm I[w]$ of a word $w = xyz\cdots$ is $\mathrm I[w] = \mathrm I[xyz\cdots] = \mathrm I[x] + \mathrm I[y|x] + \mathrm I[z|xy] + \cdots$

**properties**

- $\mathrm P[x] = 1 \to \mathrm I[x] = 0$ --- an [[outcome]] that is certain to occur has zero [[information content]]
- $\mathrm P[x] < \mathrm P[y] \to \mathrm I[x] > \mathrm I[x]$ --- an [[outcome]] that is less likely to occur has more [[information content]]
- $\mathrm P[x \cap y] = \mathrm P[x] \cdot \mathrm P[y] \to \mathrm I[x \cap y] = \mathrm I[x] + \mathrm I[Y]$ --- the [[information content]] of two independent [[outcome]]s is the sum of the [[information content]] of each [[outcome]]

and in fact, the only [[function]]s satisfying these properties are of the form $\mathrm I[x] = -\log_b \mathrm P[x]$ --- <https://youtu.be/B3y0RsVCyrw?t=483>
