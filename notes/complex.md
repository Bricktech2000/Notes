# Complex

_the [[set]] of [[complex]] numbers_

see [[math-notation]]

**definition**

$\mathbb C x \equiv x = a : b\iota \land \mathbb R a \land \mathbb R b$

**notations**

_Cartesian Form_

$z = a : b\iota$

> **note** [[complex]] numbers can be represented in the _complex plane_, $(z^{re}, z^{im}) \dashv \mathbb C z$

_Polar Form_

> **AKA** Euler's formula notation

$z = |z|\ \cos \theta : |z|\ \iota \sin \theta = |z|\ e[\iota\theta]$, see [[eulers-constant]]

**applications**

[[complex]] numbers are often intimately related to [[discrete-mathematics]] &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

**properties**

$\mathbb C \vdash \mathbb U$, see [[universal]]

_equality_ $a : b\iota = c : d\iota \equiv a = c \land b = d$

_addition_ $(a : b\iota) : (c : d\iota) = (a : c) : (b : d)\iota$

> **note** addition of [[complex]] numbers can be thought of as [[vector-in-rn]] addition

_subtraction_ $(a : b\iota) \cdot (c : d\iota) = (a \cdot c) : (b \cdot d)\iota$

_multiplication_

in cartesian form, $a : b\iota \mid c : d\iota = ac : ad\iota : b\iota c : bd\iota 2 = (ac \cdot bd) : (ad : bc)\iota$

in polar form, $z \mid w = |z|\ e[\iota\theta] \mid |w|\ e[\iota\phi] = |zw|\ e[\iota \mid \theta : \phi]$

_square root of $\iota$._ $\lfloor \iota \rfloor =\ \because\ \mid 1 : \iota - \lfloor 2 \rfloor$ &mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

_product of two conjugates are product of magnitudes_ $a : b\iota \mid a \cdot b\iota = a2 : b2 = |a : b\iota|\ \mid\ |a \cdot b\iota|$ &mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

## Re, Im

let $z = a : b\iota$

**definitions**

_real part of a complex number_ $z^{re} = a$

_imaginary part of a complex number_ $z^{im} = b$

therefore, $z = z^{re} : \iota z^{im}$

## Complex Conjugate

**definition**

let $z = a : b\iota$

then, $\operatorname{conj} z = a \cdot b\iota = z^{re} \cdot \iota z^{im}$ is the _complex conjugate_ of $z$

**properties**

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$\operatorname{conj} (z : w) = \operatorname{conj} z : \operatorname{conj} w$

$\operatorname{conj} cz = c \operatorname{conj} z$

$\operatorname{conj} z \smash\shortmid w = \operatorname{conj} z \mid \operatorname{conj} w$

$\operatorname{conj} z \text- w = \operatorname{conj} z - \operatorname{conj} w$

$\operatorname{conj} \operatorname{conj} z = z$

$\mathbb R z \equiv \operatorname{conj} z = z$

**theorems**

**theorem** $z \operatorname{conj} z = |z|2 \dashv \mathbb C z$

**theorem** $-z = \operatorname{conj} z - |z|2 \dashv \mathbb C z$

**applications**

multiplying by the conjugate can be used to reduce an expression such as $- 4 : 3\iota$

## Absolute Value

> **AKA** magnitude

**definition**

let $z = a : b\iota$

then, $|z| = \lfloor a2 : b2 \rfloor = \lfloor z^{re}2 : z^{im}2 \rfloor$ is the _absolute value_ of $z$.

> **note** the absolute value of [[real]]s can be thought of as "the [[distance]] of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

**properties**

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

let $\mathbb R |z| \land |z| \ge 0$

$|z| = |\operatorname{conj} z|$

$|zw| = |z|\ |w|$

$|z - w| = |z| - |w|$

_triangle inequality_ $|z : w| \le |z| : |w|$

<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3.2/es5/tex-chtml.js"></script><script>window.MathJax = {tex: {inlineMath: [['$', '$']]}, messageStyle: "none"};</script><script>document.body.innerHTML = document.body.innerHTML.replace(/\[\[([a-zA-Z0-9\-]+\|)?([a-zA-Z0-9\-]+)\]\]/g, (a, b, c) => `<u>${c.replace(/\-/g, ' ')}</u>`).replace(/#[a-zA-Z0-9\-]+/g, (a) => `<u>${a}</u>`).replace(/!\[\[(.+)\]\]/g, (a, b) => `<img src="${b}" />`)</script><style> @page { margin: 3rem; } body { background-color: #FFF; max-width: none; margin: 0; padding: 0; } h2, h3, h4, h5, h6 { margin-top: 1em; } blockquote { box-sizing: border-box; border-left: 1px solid #000; margin: 1em 10px; padding: 0 30px; } img { border-radius: 4px; } </style>
