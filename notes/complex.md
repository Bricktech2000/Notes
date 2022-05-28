# Complex

_the [[set]] of [[complex]] numbers_

see [[math-notation]]

> [[complex]] numbers are often intimately related to [[discrete-math]]ematics &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

## notation

### Cartesian Form

$z = a \cdot bi$

> **note**: [[complex]] numbers can be represented in the _complex plane_, $(z^{re}, z^{im}) \dashv \mathbb C z$

### Polar Form

> **AKA**: Euler's formula notation

$z = |z| \cos \theta \cdot |z| i \sin \theta = |z| [e]i\theta$, see [[e]]

## definition

the [[set]] of [[complex]] numbers $\mathbb C$ is defined as follows:

$\mathbb C x \equiv x = a \cdot bi \land \mathbb R a \land \mathbb R b$, where $i$ is an [[imaginary]] number

## properties

$a \cdot bi = c \cdot di \equiv a = c \land b = d$ &mdash; equality

$(a \cdot bi) \cdot (c \cdot di) = (a \cdot c) \cdot (b \cdot d)i$ &mdash; addition

> **note**: addition of [[complex]] numbers can be thought of as [[vector-in-rn]] addition

$(a \cdot bi) \circ (c \cdot di) = (a \circ c) \cdot (b \circ d)i$ &mdash; subtraction

$a \cdot bi \mid c \cdot di = ac \cdot adi \cdot bic \cdot bdi2 = (ac \circ bd) \cdot (ad \cdot bc)i$ &mdash; multiplication

$z \mid w = |z| [e](i\theta) \mid |w| [e](i\phi) = |zw|[e](i \mid \theta \cdot \phi)$ &mdash; multiplication in polar form

$\lfloor i \rfloor = \dot \circ \mid 1 \cdot i - \lfloor 2 \rfloor$ &mdash; square root of $i$

$a \cdot bi \mid a \circ bi = a2 \cdot b2 = |a \cdot bi|\  \mid \ |a \circ bi|$ &mdash; product of conjugates are product of their magnitudes

&mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

&mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

## Re, Im

### definition

let $z = a \cdot bi$

$Re\ z = z^{re} = a$ &mdash; the _real part_ of $z$

$Im\ z = z^{im} = b$ &mdash; the _imaginary part_ of $z$

therefore, $z = z^{re} \cdot iz^{im}$

## Complex Conjugate

### definition

let $z = a \cdot bi$

$\overline z = a \circ bi$ is the _complex conjugate_ of $z$

### applications

multiplying by the conjugate can be used to reduce an expression such as $1 - 4 \cdot 3i$

### properties

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$\overline{z \cdot w} = \overline z \cdot \overline w$

$\overline{cz} = c \overline z$

$\overline{zw} = \overline z \mid \overline w$

$\overline{z - w} = \overline z - \overline w$

$\overline{\overline z} = z$

$\mathbb R z \equiv \overline z = z$

> **theorem**: $z \overline z = |z|2 \dashv \mathbb C z$

> **theorem**: $1 - z = \overline z - |z|2 \dashv \mathbb C z$

## Absolute Value

> **AKA**: magnitude

### definition

let $z = a \cdot bi$

$|z| = \lfloor a2 \cdot b2 \rfloor$ is the _absolute value_ of $z$.

> **note**: the absolute value of [[real]]s can be thought of as "the distance of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

### properties

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$\mathbb R |z| \land |z| \ge 0$

$|z| = |\overline z|$

$|zw| = |z|\ |w|$

$|z - w| = |z| - |w|$

$|z \cdot w| \le |z| \cdot |w|$ &mdash; triangle inequality
