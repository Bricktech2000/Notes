# Color Science

[[color science]] is all about capturing and reproducing [[color]]s so they look accurate to the human eye

our eyes see [[color]] in a way that can be described as a [[euclidean vector]] of three [[real]]s in the [[lms]] [[color space]]. this means that many colors we percieve to be the same have different [[spectral power distribution]]s. two colors are called _metamers_ if they are perceived to be the same color, which is an effect called _metamerism_

**see**

[[color]], [[luminance]], [[lightness]], [[gamma correction]]

[[color space]], [[color gamut]], [[color correction]]

[[cie 1931]], [[cie diagram]], [[cielab]]

## ---

--- <https://youtu.be/AS1OHMW873s>

--- <https://en.wikipedia.org/wiki/Metamerism_(color)>

--- <https://youtu.be/M47YdERx11s>

--- <https://youtu.be/gnUYoQ1pwes>

---

#xxx guiding questions:

- come up with a color theory for hexachromacy
- why do glasses have no effect on red-green colorblind people

---

#xxx

only reason color is 3D is we have 3 types of cones

_metamers_ are colors with different spectra that map to the same 3D vector and thus look the same

A continuous spectral power distribution of light S ( λ) {\displaystyle S(\lambda )} is converted to the discrete tristimulus values (in this case L {\displaystyle L}, M {\displaystyle M} & S {\displaystyle S}) by integrating over a spectral sensitivity of one of the cone classes ( L ¯ ( λ) {\displaystyle {\overline {L}}(\lambda )}, M ¯ ( λ) {\displaystyle {\overline {M}}(\lambda )}, or S ¯ ( λ) {\displaystyle {\overline {S}}(\lambda )}): # L ∫ 0 ∞ S ( λ) L ¯ ( λ) d λ , M = ∫ 0 ∞ S ( λ) M ¯ ( λ) d λ , S = ∫ 0 ∞ S ( λ) S ¯ ( λ) d λ . {\displaystyle {\begin{aligned}L&=\int _{0}^{\infty }S(\lambda )\,{\overline {L}}(\lambda )\,d\lambda ,\\[6mu]M&=\int _{0}^{\infty }S(\lambda )\,{\overline {M}}(\lambda )\,d\lambda ,\\[6mu]S&=\int \_{0}^{\infty }S(\lambda )\,{\overline {S}}(\lambda )\,d\lambda .\end{aligned}}}

These are all inner products and can be thought of as a projection of an infinite-dimensional spectrum to a three-dimensional color.

can't represent all visible colors from finite set of primaries --- before <https://youtu.be/AS1OHMW873s?t=993>. instead use "negative color" on the other side of the equality

cie-rgb is the original color space

to preserve "mathematical behavior" (adding vectors corresponds to putting light sources on top of each other) you want color spaces to be a linear transformation of cie-rgb

if we choose our primaries to be "imaginary" (outside visible colors) then we can engineer a color space where all values positive; result is cie-xyz

cie-xyz is linear transformation of cie-rgb which is based on experimental data of human vision

if want to make a new color space, need to provide a (invertible?) linear map into cie-xyz; proves that "math" "works" in your color space and that it can represent all visible colors etc.

since [[srgb]] not linear cs gamma correction, math looks wrong

"grayscaling" is also a perceptual operation, so shd iu smth' la cielab --- <https://youtu.be/AS1OHMW873s?t=1848>

table comparing different color spaces: <https://youtu.be/AS1OHMW873s?t=1899>

cielab can represent all visible colors

---

color is not a property of the physical world; it's just a subjective sensation --- <https://youtu.be/99v96TL-tuY?t=130>

metamerism: different SPDs can result in the same perceived color --- <https://youtu.be/99v96TL-tuY?t=318>

monitors don't produce same SPD as what the camera captured; rather, produces SPDs that are trichromatic metamers of what the camera captured

CIE diagram is every possible chromaticity at a given luminance level --- <https://youtu.be/99v96TL-tuY?t=538>

---

color is not an inherent property of light; instead, it's a phychological phenomenon that relates to wavelength but only indirectly --- <https://youtu.be/gnUYoQ1pwes?t=100>

responsivity VS normalized responsivity: <https://youtu.be/gnUYoQ1pwes?t=178>

#xxx surprising: mapping from cone response to color is not so straightforward; green is M+L cones, peak of L cone we see as yellow, and red is L cone with almost no M cone --- <https://youtu.be/gnUYoQ1pwes?t=192>. good diagram: <https://youtu.be/gnUYoQ1pwes?t=265>

the spectral colors are the colors we perceive when seeing light of a single wavelength (monochromatic light) --- <https://youtu.be/gnUYoQ1pwes?t=814>. all colors of the visible gamut are a weighted average of spectral colors. "hypergreen" is an _impossible color_ that we woud see if M cone activated while L&S cones not activated, but that's not possible because any wavelength that activates M will also activate one of L,S --- <https://youtu.be/gnUYoQ1pwes?t=907>

defn of chromaticity: <https://youtu.be/gnUYoQ1pwes?t=987>

the LMS color space is based on **normalized** cone responses: <https://youtu.be/gnUYoQ1pwes?t=1040>

cie-xyz is linear transform of LMS color space where Y axis roughly corresponds to _relative luminance_ (confusing term because nothing to do with actual luminance) --- <https://youtu.be/gnUYoQ1pwes?t=1099>

construction of CIE diagram: <https://youtu.be/gnUYoQ1pwes?t=1122>. the outline of a CIE diagram is **not** the spectral colors; it's the max-luminance, same-chromaticity versions of the spectral colors

_dispersive prisms_ and rainbows produce spectral colors --- me and <https://youtu.be/gnUYoQ1pwes?t=1489> and <https://en.wikipedia.org/wiki/Dispersive_prism>

the lms color space is linear and thus "respects math" cs at the end of the day it's governed by photons hitting cone cells --- me

rgb & hsl: <https://youtu.be/gnUYoQ1pwes?t=1955>. seems that hsl is just a different coordinate system for the rgb cube

diagram of color names: <https://youtu.be/gnUYoQ1pwes?t=2486>

---

#xxx tabs:

- <https://www.youtube.com/watch?v=AS1OHMW873s>
- <https://www.youtube.com/watch?v=99v96TL-tuY>
- <https://www.youtube.com/watch?v=M47YdERx11s>
- <https://www.youtube.com/watch?v=gnUYoQ1pwes>
- <https://en.wikipedia.org/wiki/Spectral_power_distribution>
- <https://en.wikipedia.org/wiki/CIE_1931_color_space#Color_vision>
- <https://en.wikipedia.org/wiki/Dispersive_prism>

#xxx files:

- [[color science]]
- [[cie 1931]]
- [[srgb]]
- [[linear srgb]]
- [[cielab]]
- [[luminance]]
- [[chromaticity]]

#xxx in file [[luminance]], _[[luminance]] can be though of a "counting the number of [[photon]]s" hitting a given [[area]]_ can't be right, because it's weighted by the spectral sensitivity of human visual perception, see <https://en.wikipedia.org/wiki/Candela> and [[luminous intensity]]. I think luminance is linear to luminous intensity which is linear to number of photons, while [[lightness]] is linear to human perception. I think that's the difference. _While luminance is a linear measurement of light, lightness is a linear prediction of the human perception of that light._ --- <https://en.wikipedia.org/wiki/Lightness>. that last Wikipedia link has a good table with lumen/candela/luminance etc
