# JPEG

_a widespread lossy [[data compression]] format for images_

**see** [[png]], [[data compression]]

## Compression

&mdash; <https://youtu.be/0me3guauqOU>

the initial step in [[jpeg#compression]] is converting the image to the [[ycbcr]] [[color space]]. human eyes are more sensitive to [[luma]] and less sensitive to [[chroma]]. therefore, reducing the resolution of the [[chroma]] components of an image has little effect on perceived image quality. _chroma subsamlping_ does so by **"choosing"** the [[chroma]] of one pixel and applying it to the surrounding pixels. _chroma downsampling_ does so by **averaging** the [[chroma]] of a group of pixels and applying it to the group

an image can be represented in the _frequency domain_ through [[discrete cosine transform]]s. real-world images tend to have more low-[[frequency]] components; human eyes are less sensitive to high-[[frequency]] components. therefore, discarding high-[[frequency]] components has little effect on perceived image quality. [[jpeg]] applies the [[discrete cosine transform]] to 8 by 8 pixel groups from each [[ycbcr]] channel. then, it divides through a [[hadamard product]] the [[frequency]] components by a _quantization table_ then rounds to the nearest [[integer]]; this process is called _quantization_. _quantization tables_ are provided by the [[jpeg]] standard, chosen through visual experiments to discard high-[[frequency]] components and are the main way for [[jpeg]] to define [[jpeg#compression]] quality

quantized [[frequency]] components are then compressed further through a combination of [[run-length encoding]] and [[huffman coding]]
