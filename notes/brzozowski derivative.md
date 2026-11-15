# Brzozowski Derivative

**see** [[formal language]], [[regular expression]]

> **resource** _Derivatives of Regular Expressions_ by Janusz A. Brzozowski --- [[../references/321239.321249.pdf]] --- <https://dl.acm.org/doi/pdf/10.1145/321239.321249>

> **resource** _Regular-expression derivatives reexamined_ by Owens, Reppy and Turon --- [[../references/re-deriv.pdf]] --- <https://www.ccs.neu.edu/home/turon/re-deriv.pdf>

> **resource** NU-RE, my tiny [[regular expression]] engine based on [[brzozowski derivative]]s --- <https://github.com/Bricktech2000/NU-RE>

**definition** the _Brzozowski derivative_ $\overline u L$ of a [[set]] of [[string]]s $L$ with respect to a [[character]] $u$ is $v.\ uv \in L$, the [[set]] of all [[string]]s that, if prepended by the [[character]] $u$, would have been in the original [[set]] $L$

> **example** $\overline c \{\mathrm{cat}, \mathrm{cow}, \mathrm{dog}\} = \{\mathrm{at}, \mathrm{ow}\}$ --- Wikipedia

> **procedure** _using [[brzozowski derivative]]s for [[regular expression]] matching_ --- _Regular-expression derivatives reexamined_ by Owens, Reppy and Turon
>
> [[brzozowski derivative]]s [[under]] accepted [[formal language]] can be computed structurally on [[regular expression#extended regular expression]]s. a [[regular expression]] $r$ accepts a [[string]] $w$ if and only if $\nu\ \delta_w\ r$, where:
>
> - $\delta_\varepsilon\ r = r$
> - $\delta_{aw}\ r = \delta_w\ \partial_a\ r$
>
> where:
>
> - $\partial_a\ \varnothing = \varnothing$
> - $\partial_a\ \varepsilon = \varnothing$
> - $\partial_a\ a = \varepsilon$
> - $\partial_a\ b = \varnothing$ for $b \neq a$
> - $\partial_a\ r^* = \partial_a\ r \cdot r^*$
> - $\partial_a\ (r \cdot s) = \partial_a\ r \cdot s$ for $\lnot \nu\ r$
> - $\partial_a\ (r \cdot s) = \partial_a\ r \cdot s \mid \partial_a\ s$ for $\nu\ r$
> - $\partial_a\ (r \mid s) = \partial_a\ r \mid \partial_a\ s$
> - $\partial_a\ (r \mathbin\& s) = \partial_a\ r \mathbin\& \partial_a\ s$
> - $\partial_a\ \mathop! r = \mathop! \partial_a\ r$
>
> and where:
>
> - $\nu\ \varnothing = \bot$
> - $\nu\ \varepsilon = \top$
> - $\nu\ a = \bot$
> - $\nu\ r^* = \top$
> - $\nu\ (r \cdot s) = \nu\ r \land \nu\ s$
> - $\nu\ (r \mid s) = \nu\ r \lor \nu\ s$
> - $\nu\ (r \mathbin\& s) = \nu\ r \land \nu\ s$
> - $\nu\ \mathop! r = \lnot \nu\ r$

> **note**
>
> if we adjust
>
> - $\partial_a\ (r \cdot s) = \partial_a\ r \cdot s \mid r \cdot \partial_a\ s$ to match the usual product rule, and
> - $\partial_a\ r^* = r^* \cdot \partial_a\ r \cdot r^*$ so $\partial$ respects $r^* = \varepsilon \mid r \cdot r^*$,
>
> then we obtain a different kind of derivative that removes a character not from the front of the string, but from anywhere in the string
>
> --- [[../references/Semantic Domain_ Five (and a Half) Derivatives in Language Theory.pdf]] --- <https://semantic-domain.blogspot.com/2021/02/five-and-half-derivatives-in-language.html>
