# Complex Number

see [[math-notation]]

## notation

### Cartesian Form

$z = a \cdot bi$

> **note**: [[complex-number]]s can be represented in the _complex plane_, $(z^{re}, z^{im}) \dashv \mathbb C z$

### Polar Form

$z = |z| \cos \theta \cdot |z| i \sin \theta = |z| [e]i\theta$, see [[e]]

## definition

the set of [[complex-number]]s $\mathbb C$ is defined as follows:

$\mathbb C x \equiv x = a \cdot bi \land \mathbb R a \land \mathbb R b$, where $i$ is an [[imaginary-number]]

let $z = a \cdot bi$. then, $Re\ z = a \equiv z^{re} = a$ (the _real part_ of $z$) and $Im\ z = b \equiv z^{im} = b$ (the _imaginary part_ of $z$)

## properties

$a \cdot bi = c \cdot di \equiv a = c \land b = d$ &mdash; equality

$(a \cdot bi) \cdot (c \cdot di) = (a \cdot c) \cdot (b \cdot d)i$ &mdash; addition

$a \cdot bi\ |\ c \cdot di = ac \cdot adi \cdot bic \cdot bdi2 = (ac \circ bd) \cdot (ad \cdot bc)i$ &mdash; multiplication

$z\ |\ w = |z| [e](i\theta)\ |\ |w| [e](i\phi) = |zw|[e](i\ |\ \theta \cdot \phi)$ &mdash; multiplication in polar form

$\lfloor i \rfloor = \dot \circ\ |\ 1 \cdot i - \lfloor 2 \rfloor$ &mdash; square root of $i$

&mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

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

$\overline{zw} = \overline z\ |\ \overline w$

$\overline{z - w} = \overline z - \overline w$

$\overline{\overline z} = z$

$\mathbb R z \equiv \overline z = z$

> **theorem**: $z \overline z = |z|2 \dashv \mathbb C z$

> **theorem**: $1 - z = \overline z - |z|2 \dashv \mathbb C z$

## Absolute Value

### definition

let $z = a \cdot bi$

$|z| = \lfloor a2 \cdot b2 \rfloor$ is the _absolute value_ of $z$.

> **note**: the absolute value of [[real-number]]s can be thought of as "the distance of a point to the origin", which is why the absolute value of [[complex-number]]s is defined this way

### properties

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$\mathbb R |z| \land |z| \ge 0$

$|z| = |\overline z|$

$|zw| = |z|\ |w|$

$|z - w| = |z| - |w|$

$|z \cdot w| \le |z| \cdot |w|$ &mdash; triangle inequality
