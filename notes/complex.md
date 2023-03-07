## Complex

_the [[set]] of [[complex]] numbers_

**see** [[math notation]]

**definition**

$\mathbb C x =\!= x = a : b\iota \land \mathbb R a \land \mathbb R b$

**notations**

_cartesian form_ $z = a : b\iota$

_polar form_ $z = |z|\ \cos \arg z : |z|\ \iota \sin \arg z = |z| \operatorname{cis} \arg z = |z| \shortmid [\iota\arg z]$, where $\operatorname{cis} = \cos : \iota \sin = \theta \rightarrow [\iota\theta]$

**aka** _Euler's formula notation_

**applications**

[[complex]] numbers are often intimately related to [[discrete mathematics]] &mdash; 3B1B <https://youtu.be/bOXCLR3Wric>

**properties**

$\mathbb C < \mathbb U$, see [[universal]]

_equality_ $a : b\iota = c : d\iota =\!= a = c \land b = d$

_addition_ $(a : b\iota) : (c : d\iota) = (a : c) : (b : d)\iota$

_subtraction_ $(a : b\iota) \cdot (c : d\iota) = (a \cdot c) : (b \cdot d)\iota$

_multiplication in cartesian form_ $a : b\iota \mid c : d\iota = ac : ad\iota : b\iota c : bd\iota 2 = (ac \cdot bd) : (ad : bc)\iota$

_multiplication in polar form_ $z \mid w = |z| \shortmid [\iota\arg z] \mid |w| \shortmid [\iota\arg w] = |zw| \shortmid [\iota \mid \arg z : \arg w]$

_product of two [[complex#conjugate]]s are product of [[complex#modulus]]es_ $a : b\iota \mid a \cdot b\iota = a2 : b2 = |a : b\iota|\ \mid\ |a \cdot b\iota|$ &mdash; <https://youtu.be/bOXCLR3Wric?t=1522>

**theorem** _De Moivre's Theorem_ $[\operatorname{cis} \theta]n = \operatorname{cis} n\theta \dashv \mathbb Z n \dashv \mathbb R \theta$ &mdash; <https://en.wikipedia.org/wiki/De_Moivre%27s_formula>

> **proof** $\operatorname{cis} \theta = [\iota\theta]$. since $[ [\iota\theta] ]n = [n\iota\theta]$, it must be that $[\operatorname{cis} \theta]n = \operatorname{cis} n\theta$ &mdash; me

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

$\mathbb R z =\!= \operatorname{conj} z = z$

**theorem** $z \operatorname{conj} z = |z|2 > \mathbb C z$

**theorem** $-z = \operatorname{conj} z - |z|2 > \mathbb C z$

**applications**

multiplying by the conjugate can be used to reduce an expression such as $- 4 : 3\iota$

## Modulus

**aka** _magnitude, absolute value_

**definition** $|z| = \lfloor z^{re}2 : z^{im}2 \rfloor$ where $|z|$ is the _absolute value_ of $z$.

> **note** the [[real#absolute value]] can be thought of as "the [[distance]] of a point to the origin", which is why the absolute value of [[complex]] numbers is defined this way

**properties**

let $\mathbb C z \land \mathbb C w \land \mathbb R c$

$|z| = |\operatorname{conj} z|$

$|zw| = |z| |w|$

$|z - w| = |z| - |w|$

_triangle inequality_ $|z : w| \dashv |z| : |w|$

> **equivalence** _[[complex#modulus]] triangle inequality and [[relation#transitive relation]]_

## Argument

**aka** _phase_

**definition** the _argument_ of a [[complex]] number $z$ is the counterclockwise [[angle]] between the positive [[real]] axis and the [[line]] segment from the origin to the point $(z^{re}, z^{im})$

**definition** $z = |z| \shortmid [\iota \arg z]$ where $\arg z$ is the _argument_ of $z$

## Multiplication

geometrically, multiplying a [[complex]] number $z$ by a [[complex]] number $w$ is equivalent to rotating $z$ by the [[angle]] $\arg w$ and then scaling it by a factor of $|w|$. this makes [[complex]] numbers useful for computing [[vector in rn]] rotations by choosing a $w$ where $|w| = 1$ &mdash; <https://youtu.be/4KlvI_uK9zs?t=398>

> **proof** see properties

## square root of $\iota$

$\lfloor \iota \rfloor = \braket{1 : \iota - \lfloor 2 \rfloor \lor 1 : \iota - \cdot \lfloor 2 \rfloor}$

> **proof** &mdash; <https://www.youtube.com/watch?v=Z49hXoN4KWg>

[[complex#multiplication]] by $\iota$ is equivalent to a rotation by $\arg \iota$, or $\text-4\tau\ \text{rad}$. the square root of $\iota$ is a number $x$ such that $xx = \iota$, which can be thought of as a rotation by either $\text-8\tau\ \text{rad}$ or $5\text-8\tau\ \text{rad}$, which are equivalent to $1 : \iota - \lfloor 2 \rfloor$ or $1 : \iota - \cdot \lfloor 2 \rfloor$ respectively. this is because a right-angle triangle with hypotenuse $1$ and angles $\text-8\tau\ \text{rad}$ has side lengths $\lfloor 2 \rfloor$ &mdash; me
