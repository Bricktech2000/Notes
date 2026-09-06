# Fourier Transform

--- <https://youtu.be/spUNpyF58BY>

--- <https://en.wikipedia.org/wiki/Fourier_transform>

**definition** $\mathcal F\ f\ \nu = \int_{-\infty}^\infty t.\ (f\ t)e^{-\iota\tau\nu t}$, where

- $f\ t$ is the amplitude of a wave $f$ at time $t$
- $\mathcal F\ f$ represents the [[frequency]] components of the wave, where
  - $\operatorname{abs}\ (\mathcal F\ f\ \nu)$ is the amplitude of the [[frequency]] component $\nu$, see [[complex]]
  - $\operatorname{arg}\ (\mathcal F\ f\ \nu)$ is the phase of the [[frequency]] component $\nu$, see [[complex]]

**representation**

![[../references/20221103111349.png]] --- <https://youtu.be/spUNpyF58BY?t=666>

**properties**

$\int_{-\infty}^\infty f = \mathcal F\ f\ 0$, by definition --- <https://youtu.be/851U557j6HE?t=823> and <https://youtu.be/UOuxo6SA8Uc?t=961>

**theorem** _convolution theorem_ $\mathcal F\ (f \ast g) = (\mathcal F\ f)(\mathcal F\ g)$ and $\mathcal F\ fg = \mathcal F\ f \ast \mathcal F\ g$, where $f \ast g$ is the [[convolution]] of $f$ and $g$ --- <https://youtu.be/851U557j6HE?t=974> and <https://en.wikipedia.org/wiki/Convolution_theorem#Convolution_theorem_for_inverse_Fourier_transform>
