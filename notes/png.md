# PNG

_a rather complex and slow lossless [[compression]] format for images_

**see** [[jpeg]], [[compression]]

## Compression

&mdash; <https://youtu.be/EFUYNoFRHQI>

the first step in [[png#compression]] is to attempt to create redundancy in the data through a process called _filtering_; one _filter_ is applied to each row of the image. available filters are _none_, _sub_, _up_, _average_ and _paeth_. the filter that produces the smallest entropy as calculated by the _sum of absolute differences_ is chosen

the second step in [[png#compression]] is to compress the filtered data using _[[deflate]]_
