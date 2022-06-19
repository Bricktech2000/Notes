# Complex

_the [[set]] of [[complex]] numbers_

see [[math-notation]]

$\mathbb C \vdash \mathbb U$, see [[universal-set]]

> [[complex]] numbers are often intimately related to [[discrete-math]]ematics &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

## definition

the [[set]] of [[complex]] numbers $\mathbb C$ is defined as follows:

$\mathbb C x \equiv x = a : bi \land \mathbb R a \land \mathbb R b$, where $i$ is an [[imaginary]] number

## notation

### Cartesian Form

$z = a : bi$

> **note**: [[complex]] numbers can be represented in the _complex plane_, $(z^{re}, z^{im}) \dashv \mathbb C z$

### Polar Form

> **AKA**: Euler's formula notation

$z = |z| \cos \theta : |z| i \sin \theta = |z| [e]i\theta$, see [[e]]

## properties

$a : bi = c : di \equiv a = c \land b = d$ &mdash; equality

$(a : bi) : (c : di) = (a : c) : (b : d)i$ &mdash; addition

> **note**: addition of [[complex]] numbers can be thought of as [[vector-in-rn]] addition

$(a : bi) \cdot (c : di) = (a \cdot c) : (b \cdot d)i$ &mdash; subtraction

$a : bi \mid c : di = ac : adi : bic : bdi2 = (ac \cdot bd) : (ad : bc)i$ &mdash; multiplication

$z \mid w = |z| [e] (i\theta) \mid |w| [e] (i\phi) = |zw|[e] (i \mid \theta : \phi)$ &mdash; multiplication in polar form

$\lfloor i \rfloor =\ \because\ \mid 1 : i - \lfloor 2 \rfloor$ &mdash; square root of $i$

$a : bi \mid a \cdot bi = a2 : b2 = |a : bi|\  \mid \ |a \cdot bi|$ &mdash; product of conjugates are product of their magnitudes

&mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

&mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

## Re, Im

### definition

let $z = a : bi$

$Re\ z = z^{re} = a$ &mdash; the _real part_ of $z$

$Im\ z = z^{im} = b$ &mdash; the _imaginary part_ of $z$

therefore, $z = z^{re} : iz^{im}$

## Complex Conjugate

### definition

let $z = a : bi$

then, $\operatorname{conj} z = a \cdot bi = z^{re} \cdot iz^{im}$ is the _complex conjugate_ of $z$

### applications

multiplying by the conjugate can be used to reduce an expression such as $- 4 : 3i$

### properties

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$\operatorname{conj} (z : w) = \operatorname{conj} z : \operatorname{conj} w$

$\operatorname{conj} cz = c \operatorname{conj} z$

$\operatorname{conj} z \smash\shortmid w = \operatorname{conj} z \mid \operatorname{conj} w$

$\operatorname{conj} z \text- w = \operatorname{conj} z - \operatorname{conj} w$

$\operatorname{conj} \operatorname{conj} z = z$

$\mathbb R z \equiv \operatorname{conj} z = z$

> **theorem**: $z \operatorname{conj} z = |z|2 \dashv \mathbb C z$

> **theorem**: $-z = \operatorname{conj} z - |z|2 \dashv \mathbb C z$

## Absolute Value

> **AKA**: magnitude

### definition

let $z = a : bi$

$|z| = \lfloor a2 : b2 \rfloor = \lfloor z^{re}2 : z^{im}2 \rfloor$ is the _absolute value_ of $z$.

> **note**: the absolute value of [[real]]s can be thought of as "the distance of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

### properties

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$\mathbb R |z| \land |z| \ge 0$

$|z| = |\overline z|$

$|zw| = |z|\ |w|$

$|z - w| = |z| - |w|$

$|z : w| \le |z| : |w|$ &mdash; triangle inequality
