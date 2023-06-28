# JPEG

#todo

---

# Compression

## Color Space Conversion

the initial step in [[jpeg#compression]] is converting the image to the [[ycbcr]] [[color space]]

## Chroma Subsampling

human eyes are more sensitive to [[luma]] and less sensitive to [[chroma]]. therefore, reducing the resolution of the [[chroma]] components of an image has little effect on perceived image quality

[[jpeg#chroma subsamlping]] does so by **"choosing"** the [[chroma]] of one pixel and applying it to the surrounding pixels

_chroma downsampling_ does so by **averaging** the [[chroma]] of a group of pixels and applying it to the group

## Discrete Cosine Transform

an image can be represented in the _frequency domain_ through [[fourier transform]]s. real-world images tend to have more low-[[frequency]] components; human eyes are less sensitive to high-[[frequency]] components. therefore, discarding high-[[frequency]] components has little effect on perceived image quality

the [[jpeg#discrete cosine transform]] does so for every [[ycbrc]] channel

[[discrete cosine transform]]
