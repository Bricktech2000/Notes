# Complex

_the [[set]] of [[complex]] numbers_

**see** [[math notation]]

**definition**

$\mathbb C x \equiv x = a : b\iota \land \mathbb R a \land \mathbb R b$

**notations**

_Cartesian Form_ $z = a : b\iota$

_Polar Form_ $z = |z|\ \cos \theta : |z|\ \iota \sin \theta = |z| \operatorname{cis} \theta = |z|\ e[\iota\theta]$, see [[eulers constant]], where $\operatorname{cis} = \cos : \iota \sin = \theta \rightarrow e[\iota\theta]$

> **aka** Euler's formula notation

**applications**

[[complex]] numbers are often intimately related to [[discrete mathematics]] &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

**properties**

$\mathbb C \vdash \mathbb U$, see [[universal]]

_equality_ $a : b\iota = c : d\iota \equiv a = c \land b = d$

_addition_ $(a : b\iota) : (c : d\iota) = (a : c) : (b : d)\iota$

_subtraction_ $(a : b\iota) \cdot (c : d\iota) = (a \cdot c) : (b \cdot d)\iota$

_multiplication_

in cartesian form, $a : b\iota \mid c : d\iota = ac : ad\iota : b\iota c : bd\iota 2 = (ac \cdot bd) : (ad : bc)\iota$

in polar form, $z \mid w = |z|\ e[\iota\theta] \mid |w|\ e[\iota\phi] = |zw|\ e[\iota \mid \theta : \phi]$

_square root of $\iota$._ $\lfloor \iota \rfloor =\ \because\ \mid 1 : \iota - \lfloor 2 \rfloor$ &mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

_product of two [[complex#conjugate]]s are product of [[complex#modulus]]es_ $a : b\iota \mid a \cdot b\iota = a2 : b2 = |a : b\iota|\ \mid\ |a \cdot b\iota|$ &mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

**theorem** _De Moivre's Theorem_ $[\operatorname{cis} \theta]n = \operatorname{cis} n\theta \dashv \mathbb Z n \dashv \mathbb R \theta$ &mdash; <https://en.wikipedia.org/wiki/De_Moivre%27s_formula>

> **proof** $\operatorname{cis} \theta = e[\iota\theta]$. since $[e[\iota\theta]]n = e[n\iota\theta]$, it must be that $[\operatorname{cis} \theta]n = \operatorname{cis} n\theta$ &mdash; me

## Real Part

## Imaginary Part

let $z = a : b\iota$

**definitions**

_real part of a complex number_ $z^{re} = a$

_imaginary part of a complex number_ $z^{im} = b$

therefore, $z = z^{re} : \iota z^{im}$

## Conjugate

_[[complex#conjugate]]_

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

**theorem** $z \operatorname{conj} z = |z|2 \dashv \mathbb C z$

**theorem** $-z = \operatorname{conj} z - |z|2 \dashv \mathbb C z$

**applications**

multiplying by the conjugate can be used to reduce an expression such as $- 4 : 3\iota$

## Modulus

> **aka** magnitude, absolute value

**definition** $|z| = \lfloor z^{re}2 : z^{im}2 \rfloor$ where $|z|$ is the _absolute value_ of $z$.

> **note** the absolute value of [[real]]s can be thought of as "the [[distance]] of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

**properties**

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$|z| = |\operatorname{conj} z|$

$|zw| = |z|\ |w|$

$|z - w| = |z| - |w|$

_triangle inequality_ $|z : w| \le |z| : |w|$

## Argument

> **aka** phase

**definition** the _argument_ of a [[complex]] number $z$ is the counterclockwise [[angle]] between the positive [[real]] axis and the [[line]] segment from the origin to the point $(z^{re}, z^{im})$

**definition** $z = |z|\ e[\iota \arg z]$ where $\arg z$ is the _argument_ of $z$
