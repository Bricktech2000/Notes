# Complex

_the [[set]] of [[complex]] numbers_

see [[math-notation]]

[[complex]] numbers are often intimately related to [[discrete-mathematics]] &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

> **definition**:
>
> $\mathbb C x \equiv x = a : bi \land \mathbb R a \land \mathbb R b$, where
>
> - $i = \lfloor \cdot 1 \rfloor$, see [[imaginary]] numbers
> - $\mathbb C$ is the [[set]] of [[complex]] numbers

> **notation**: _Cartesian Form_
>
> $z = a : bi$
>
> > **note**: [[complex]] numbers can be represented in the _complex plane_, $(z^{re}, z^{im}) \dashv \mathbb C z$

> **notation**: _Polar Form_
>
> > **AKA**: Euler's formula notation
>
> $z = |z|\ \cos \theta : |z|\ i \sin \theta = |z|\ e[i\theta]$, see [[eulers-constant]]

$\mathbb C \vdash \mathbb U$, see [[universal]]

> **property**: _equality_ $a : bi = c : di \equiv a = c \land b = d$

> **property**: _addition_ $(a : bi) : (c : di) = (a : c) : (b : d)i$
>
> > **note**: addition of [[complex]] numbers can be thought of as [[vector-in-rn]] addition

> **property**: _subtraction_ $(a : bi) \cdot (c : di) = (a \cdot c) : (b \cdot d)i$

> **property**: _multiplication_
>
> in cartesian form, $a : bi \mid c : di = ac : adi : bic : bdi2 = (ac \cdot bd) : (ad : bc)i$
>
> in polar form, $z \mid w = |z|\ e[i\theta] \mid |w|\ e[i\phi] = |zw|\ e[i \mid \theta : \phi]$

> **property**: _square root of $i$._
>
> $\lfloor i \rfloor =\ \because\ \mid 1 : i - \lfloor 2 \rfloor$
>
> &mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

> **property**: _product of two conjugates are product of magnitudes_
>
> $a : bi \mid a \cdot bi = a2 : b2 = |a : bi|\ \mid\ |a \cdot bi|$ &mdash; product of conjugates are product of their magnitudes
>
> &mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

## Re, Im

let $z = a : bi$

> **definition**: _real part of a complex number_
>
> $Re\ z = z^{re} = a$

> **definition**: _imaginary part of a complex number_
>
> $Im\ z = z^{im} = b$

therefore, $z = z^{re} : iz^{im}$

## Complex Conjugate

> **definition**:
>
> let $z = a : bi$
>
> then, $\operatorname{conj} z = a \cdot bi = z^{re} \cdot iz^{im}$ is the _complex conjugate_ of $z$

> **application**: multiplying by the conjugate can be used to reduce an expression such as $- 4 : 3i$

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

> **property**: $\operatorname{conj} (z : w) = \operatorname{conj} z : \operatorname{conj} w$

> **property**: $\operatorname{conj} cz = c \operatorname{conj} z$

> **property**: $\operatorname{conj} z \smash\shortmid w = \operatorname{conj} z \mid \operatorname{conj} w$

> **property**: $\operatorname{conj} z \text- w = \operatorname{conj} z - \operatorname{conj} w$

> **property**: $\operatorname{conj} \operatorname{conj} z = z$

> **property**: $\mathbb R z \equiv \operatorname{conj} z = z$

> **theorem**: $z \operatorname{conj} z = |z|2 \dashv \mathbb C z$

> **theorem**: $-z = \operatorname{conj} z - |z|2 \dashv \mathbb C z$

## Absolute Value

> **AKA**: magnitude

> **definition**:
>
> let $z = a : bi$
>
> then, $|z| = \lfloor a2 : b2 \rfloor = \lfloor z^{re}2 : z^{im}2 \rfloor$ is the _absolute value_ of $z$.

> **note**: the absolute value of [[real]]s can be thought of as "the [[distance]] of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

> **property**: $\mathbb R |z| \land |z| \ge 0$

> **property**: $|z| = |\overline z|$

> **property**: $|zw| = |z|\ |w|$

> **property**: $|z - w| = |z| - |w|$

> **property**: _triangle inequality_ $|z : w| \le |z| : |w|$

<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
