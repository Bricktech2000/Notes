# ASCII

**see** [[utf-8]], [[math notation]]

[[ascii]] is a widely used 7-bit [[character]] encoding standard

a non-standard 8th bit is sometimes used for:

- [[utf-8]] encoding
- code page extensions
- parity checks and [[error correction]]

**properties**

lowercase and uppercase letters are offset by `0x20` or `0b00100000` or `' '`

`c & 0b11011111` where `c` is a lowercase letter will return its uppercase equivalent

`c | 0b00100000` where `c` is an uppercase letter will return its lowercase equivalent

`c & 0b00111111` where `c` is a letter will return its position in the alphabet, starting at **`1`**

`c & 0b00001111` where `c` is digit will return its value

`c & 0b11100000 != 0` will return whether `c` is a control character

**representation**

| [[hexadecimal]] &bull; [[binary]] | [[character]] | description               |
| --------------------------------- | ------------- | ------------------------- |
| `0x00` &bull; `0b00000000`        | NUL           | Null                      |
| `0x01` &bull; `0b00000001`        | SOH           | Start of Heading          |
| `0x02` &bull; `0b00000010`        | STX           | Start of Text             |
| `0x03` &bull; `0b00000011`        | ETX           | End of Text               |
| `0x04` &bull; `0b00000100`        | EOT           | End of Transmission       |
| `0x05` &bull; `0b00000101`        | ENQ           | Enquiry                   |
| `0x06` &bull; `0b00000110`        | ACK           | Acknowledgment            |
| `0x07` &bull; `0b00000111`        | BEL           | Bell                      |
| `0x08` &bull; `0b00001000`        | BS            | Backspace                 |
| `0x09` &bull; `0b00001001`        | HT            | Horizontal Tab            |
| `0x0A` &bull; `0b00001010`        | LF            | Line Feed                 |
| `0x0B` &bull; `0b00001011`        | VT            | Vertical Tab              |
| `0x0C` &bull; `0b00001100`        | FF            | Form Feed                 |
| `0x0D` &bull; `0b00001101`        | CR            | Carriage Return           |
| `0x0E` &bull; `0b00001110`        | SO            | Shift Out                 |
| `0x0F` &bull; `0b00001111`        | SI            | Shift In                  |
| `0x10` &bull; `0b00010000`        | DLE           | Data Link Escape          |
| `0x11` &bull; `0b00010001`        | DC1           | Device Control 1          |
| `0x12` &bull; `0b00010010`        | DC2           | Device Control 2          |
| `0x13` &bull; `0b00010011`        | DC3           | Device Control 3          |
| `0x14` &bull; `0b00010100`        | DC4           | Device Control 4          |
| `0x15` &bull; `0b00010101`        | NAK           | Negative Acknowledgement  |
| `0x16` &bull; `0b00010110`        | SYN           | Synchronous Idle          |
| `0x17` &bull; `0b00010111`        | ETB           | End of Transmission Block |
| `0x18` &bull; `0b00011000`        | CAN           | Cancel                    |
| `0x19` &bull; `0b00011001`        | EM            | End of Medium             |
| `0x1A` &bull; `0b00011010`        | SUB           | Substitute                |
| `0x1B` &bull; `0b00011011`        | ESC           | Escape                    |
| `0x1C` &bull; `0b00011100`        | FS            | File Separator            |
| `0x1D` &bull; `0b00011101`        | GS            | Group Separator           |
| `0x1E` &bull; `0b00011110`        | RS            | Record Separator          |
| `0x1F` &bull; `0b00011111`        | US            | Unit Separator            |
| `0x20` &bull; `0b00100000`        | `' '`         | Space                     |
| `0x21` &bull; `0b00100001`        | `'!'`         | Exclamation Mark          |
| `0x22` &bull; `0b00100010`        | `'"'`         | Quotation Mark            |
| `0x23` &bull; `0b00100011`        | `'#'`         | Number Sign               |
| `0x24` &bull; `0b00100100`        | `'$'`         | Dollar Sign               |
| `0x25` &bull; `0b00100101`        | `'%'`         | Percent Sign              |
| `0x26` &bull; `0b00100110`        | `'&'`         | Ampersand                 |
| `0x27` &bull; `0b00100111`        | `'\''`        | Apostrophe                |
| `0x28` &bull; `0b00101000`        | `'('`         | Left Parenthesis          |
| `0x29` &bull; `0b00101001`        | `')'`         | Right Parenthesis         |
| `0x2A` &bull; `0b00101010`        | `'*'`         | Asterisk                  |
| `0x2B` &bull; `0b00101011`        | `'+'`         | Plus Sign                 |
| `0x2C` &bull; `0b00101100`        | `','`         | Comma                     |
| `0x2D` &bull; `0b00101101`        | `'-'`         | Hyphen-Minus              |
| `0x2E` &bull; `0b00101110`        | `'.'`         | Full Stop                 |
| `0x2F` &bull; `0b00101111`        | `'/'`         | Solidus                   |
| `0x30` &bull; `0b00110000`        | `'0'`         | Digit Zero                |
| `0x31` &bull; `0b00110001`        | `'1'`         | Digit One                 |
| `0x32` &bull; `0b00110010`        | `'2'`         | Digit Two                 |
| `0x33` &bull; `0b00110011`        | `'3'`         | Digit Three               |
| `0x34` &bull; `0b00110100`        | `'4'`         | Digit Four                |
| `0x35` &bull; `0b00110101`        | `'5'`         | Digit Five                |
| `0x36` &bull; `0b00110110`        | `'6'`         | Digit Six                 |
| `0x37` &bull; `0b00110111`        | `'7'`         | Digit Seven               |
| `0x38` &bull; `0b00111000`        | `'8'`         | Digit Eight               |
| `0x39` &bull; `0b00111001`        | `'9'`         | Digit Nine                |
| `0x3A` &bull; `0b00111010`        | `':'`         | Colon                     |
| `0x3B` &bull; `0b00111011`        | `';'`         | Semicolon                 |
| `0x3C` &bull; `0b00111100`        | `'<'`         | Less-Than Sign            |
| `0x3D` &bull; `0b00111101`        | `'='`         | Equals Sign               |
| `0x3E` &bull; `0b00111110`        | `'>'`         | Greater-Than Sign         |
| `0x3F` &bull; `0b00111111`        | `'?'`         | Question Mark             |
| `0x40` &bull; `0b01000000`        | `'@'`         | Commercial At             |
| `0x41` &bull; `0b01000001`        | `'A'`         | Latin Capital Letter A    |
| `0x42` &bull; `0b01000010`        | `'B'`         | Latin Capital Letter B    |
| `0x43` &bull; `0b01000011`        | `'C'`         | Latin Capital Letter C    |
| `0x44` &bull; `0b01000100`        | `'D'`         | Latin Capital Letter D    |
| `0x45` &bull; `0b01000101`        | `'E'`         | Latin Capital Letter E    |
| `0x46` &bull; `0b01000110`        | `'F'`         | Latin Capital Letter F    |
| `0x47` &bull; `0b01000111`        | `'G'`         | Latin Capital Letter G    |
| `0x48` &bull; `0b01001000`        | `'H'`         | Latin Capital Letter H    |
| `0x49` &bull; `0b01001001`        | `'I'`         | Latin Capital Letter I    |
| `0x4A` &bull; `0b01001010`        | `'J'`         | Latin Capital Letter J    |
| `0x4B` &bull; `0b01001011`        | `'K'`         | Latin Capital Letter K    |
| `0x4C` &bull; `0b01001100`        | `'L'`         | Latin Capital Letter L    |
| `0x4D` &bull; `0b01001101`        | `'M'`         | Latin Capital Letter M    |
| `0x4E` &bull; `0b01001110`        | `'N'`         | Latin Capital Letter N    |
| `0x4F` &bull; `0b01001111`        | `'O'`         | Latin Capital Letter O    |
| `0x50` &bull; `0b01010000`        | `'P'`         | Latin Capital Letter P    |
| `0x51` &bull; `0b01010001`        | `'Q'`         | Latin Capital Letter Q    |
| `0x52` &bull; `0b01010010`        | `'R'`         | Latin Capital Letter R    |
| `0x53` &bull; `0b01010011`        | `'S'`         | Latin Capital Letter S    |
| `0x54` &bull; `0b01010100`        | `'T'`         | Latin Capital Letter T    |
| `0x55` &bull; `0b01010101`        | `'U'`         | Latin Capital Letter U    |
| `0x56` &bull; `0b01010110`        | `'V'`         | Latin Capital Letter V    |
| `0x57` &bull; `0b01010111`        | `'W'`         | Latin Capital Letter W    |
| `0x58` &bull; `0b01011000`        | `'X'`         | Latin Capital Letter X    |
| `0x59` &bull; `0b01011001`        | `'Y'`         | Latin Capital Letter Y    |
| `0x5A` &bull; `0b01011010`        | `'Z'`         | Latin Capital Letter Z    |
| `0x5B` &bull; `0b01011011`        | `'['`         | Left Square Bracket       |
| `0x5C` &bull; `0b01011100`        | `'\'`         | Reverse Solidus           |
| `0x5D` &bull; `0b01011101`        | `']'`         | Right Square Bracket      |
| `0x5E` &bull; `0b01011110`        | `'^'`         | Circumflex Accent         |
| `0x5F` &bull; `0b01011111`        | `'_'`         | Low Line                  |
| `0x60` &bull; `0b01100000`        | `` '`' ``     | Grave Accent              |
| `0x61` &bull; `0b01100001`        | `'a'`         | Latin Small Letter A      |
| `0x62` &bull; `0b01100010`        | `'b'`         | Latin Small Letter B      |
| `0x63` &bull; `0b01100011`        | `'c'`         | Latin Small Letter C      |
| `0x64` &bull; `0b01100100`        | `'d'`         | Latin Small Letter D      |
| `0x65` &bull; `0b01100101`        | `'e'`         | Latin Small Letter E      |
| `0x66` &bull; `0b01100110`        | `'f'`         | Latin Small Letter F      |
| `0x67` &bull; `0b01100111`        | `'g'`         | Latin Small Letter G      |
| `0x68` &bull; `0b01101000`        | `'h'`         | Latin Small Letter H      |
| `0x69` &bull; `0b01101001`        | `'i'`         | Latin Small Letter I      |
| `0x6A` &bull; `0b01101010`        | `'j'`         | Latin Small Letter J      |
| `0x6B` &bull; `0b01101011`        | `'k'`         | Latin Small Letter K      |
| `0x6C` &bull; `0b01101100`        | `'l'`         | Latin Small Letter L      |
| `0x6D` &bull; `0b01101101`        | `'m'`         | Latin Small Letter M      |
| `0x6E` &bull; `0b01101110`        | `'n'`         | Latin Small Letter N      |
| `0x6F` &bull; `0b01101111`        | `'o'`         | Latin Small Letter O      |
| `0x70` &bull; `0b01110000`        | `'p'`         | Latin Small Letter P      |
| `0x71` &bull; `0b01110001`        | `'q'`         | Latin Small Letter Q      |
| `0x72` &bull; `0b01110010`        | `'r'`         | Latin Small Letter R      |
| `0x73` &bull; `0b01110011`        | `'s'`         | Latin Small Letter S      |
| `0x74` &bull; `0b01110100`        | `'t'`         | Latin Small Letter T      |
| `0x75` &bull; `0b01110101`        | `'u'`         | Latin Small Letter U      |
| `0x76` &bull; `0b01110110`        | `'v'`         | Latin Small Letter V      |
| `0x77` &bull; `0b01110111`        | `'w'`         | Latin Small Letter W      |
| `0x78` &bull; `0b01111000`        | `'x'`         | Latin Small Letter X      |
| `0x79` &bull; `0b01111001`        | `'y'`         | Latin Small Letter Y      |
| `0x7A` &bull; `0b01111010`        | `'z'`         | Latin Small Letter Z      |
| `0x7B` &bull; `0b01111011`        | `'{'`         | Left Curly Bracket        |
| `0x7C` &bull; `0b01111100`        | `'\|'`        | Vertical Line             |
| `0x7D` &bull; `0b01111101`        | `'}'`         | Right Curly Bracket       |
| `0x7E` &bull; `0b01111110`        | `'~'`         | Tilde                     |
| `0x7F` &bull; `0b01111111`        | DEL           | Delete                    |
