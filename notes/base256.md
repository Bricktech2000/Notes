# Base256

--- me

**see** [[ascii]]

[[base256]] is a binary-to-text encoding scheme. it encodes 8-bit bytes into single characters in such a way that printable [[ascii]] data is represented one-to-one and that the output can be decoded manually if necessary

[[base256]] is meant to be used to losslessly and compatcly store arbitrary data on sheets of paper as a ridiculously future-proof backup medium

> **example** the [[utf-8]] [[string]] `"did you know that τ > π"` which is [[hexadecimal]] `64 69 64 20 79 6f 75 20 6b 6e 6f 77 20 74 68 61 74 20 cf 84 20 3e 20 cf 80 3f 0a`, is equivalent to <code>"did⸱you⸱know⸱that⸱<u>Oε</u>⸱>⸱<u>Oα</u>?◾"</code> encoded in [[base256]]. see [[tau]]

**properties**

[[base256]] can be thought of as a [[set#superset]] of printable [[ascii]]

[[base256]] is whitespace-insensitive by design

**representation**

| [[hexadecimal]] - [[binary]] - [[ascii]] | [[base256]]  |
| ---------------------------------------- | ------------ |
| `0x00` - `0b00000000` - `NUL`            | `'α'`        |
| `0x01` - `0b00000001` - `SOH`            | `'β'`        |
| `0x02` - `0b00000010` - `STX`            | `'γ'`        |
| `0x03` - `0b00000011` - `ETX`            | `'δ'`        |
| `0x04` - `0b00000100` - `EOT`            | `'ε'`        |
| `0x05` - `0b00000101` - `ENQ`            | `'ζ'`        |
| `0x06` - `0b00000110` - `ACK`            | `'η'`        |
| `0x07` - `0b00000111` - `BEL`            | `'θ'`        |
| `0x08` - `0b00001000` - `BS`             | `'ι'`        |
| `0x09` - `0b00001001` - `HT`             | `'κ'`        |
| `0x0A` - `0b00001010` - `LF`             | `'◾'`       |
| `0x0B` - `0b00001011` - `VT`             | `'λ'`        |
| `0x0C` - `0b00001100` - `FF`             | `'μ'`        |
| `0x0D` - `0b00001101` - `CR`             | `'ν'`        |
| `0x0E` - `0b00001110` - `SO`             | `'ξ'`        |
| `0x0F` - `0b00001111` - `SI`             | `'π'`        |
| `0x10` - `0b00010000` - `DLE`            | `'ρ'`        |
| `0x11` - `0b00010001` - `DC1`            | `'σ'`        |
| `0x12` - `0b00010010` - `DC2`            | `'τ'`        |
| `0x13` - `0b00010011` - `DC3`            | `'υ'`        |
| `0x14` - `0b00010100` - `DC4`            | `'φ'`        |
| `0x15` - `0b00010101` - `NAK`            | `'χ'`        |
| `0x16` - `0b00010110` - `SYN`            | `'ψ'`        |
| `0x17` - `0b00010111` - `ETB`            | `'ω'`        |
| `0x18` - `0b00011000` - `CAN`            | `'Γ'`        |
| `0x19` - `0b00011001` - `EM`             | `'Δ'`        |
| `0x1A` - `0b00011010` - `SUB`            | `'Θ'`        |
| `0x1B` - `0b00011011` - `ESC`            | `'Λ'`        |
| `0x1C` - `0b00011100` - `FS`             | `'Ξ'`        |
| `0x1D` - `0b00011101` - `GS`             | `'∏'`        |
| `0x1E` - `0b00011110` - `RS`             | `'Σ'`        |
| `0x1F` - `0b00011111` - `US`             | `'Φ'`        |
| `0x20` - `0b00100000` - `' '`            | `'⸱'`        |
| `0x21` - `0b00100001` - `'!'`            | `'!'`        |
| `0x22` - `0b00100010` - `'"'`            | `'"'`        |
| `0x23` - `0b00100011` - `'#'`            | `'#'`        |
| `0x24` - `0b00100100` - `'$'`            | `'$'`        |
| `0x25` - `0b00100101` - `'%'`            | `'%'`        |
| `0x26` - `0b00100110` - `'&'`            | `'&'`        |
| `0x27` - `0b00100111` - `'\''`           | `'''`        |
| `0x28` - `0b00101000` - `'('`            | `'('`        |
| `0x29` - `0b00101001` - `')'`            | `')'`        |
| `0x2A` - `0b00101010` - `'*'`            | `'*'`        |
| `0x2B` - `0b00101011` - `'+'`            | `'+'`        |
| `0x2C` - `0b00101100` - `','`            | `','`        |
| `0x2D` - `0b00101101` - `'-'`            | `'-'`        |
| `0x2E` - `0b00101110` - `'.'`            | `'.'`        |
| `0x2F` - `0b00101111` - `'/'`            | `'/'`        |
| `0x30` - `0b00110000` - `'0'`            | `'0'`        |
| `0x31` - `0b00110001` - `'1'`            | `'1'`        |
| `0x32` - `0b00110010` - `'2'`            | `'2'`        |
| `0x33` - `0b00110011` - `'3'`            | `'3'`        |
| `0x34` - `0b00110100` - `'4'`            | `'4'`        |
| `0x35` - `0b00110101` - `'5'`            | `'5'`        |
| `0x36` - `0b00110110` - `'6'`            | `'6'`        |
| `0x37` - `0b00110111` - `'7'`            | `'7'`        |
| `0x38` - `0b00111000` - `'8'`            | `'8'`        |
| `0x39` - `0b00111001` - `'9'`            | `'9'`        |
| `0x3A` - `0b00111010` - `':'`            | `':'`        |
| `0x3B` - `0b00111011` - `';'`            | `';'`        |
| `0x3C` - `0b00111100` - `'<'`            | `'<'`        |
| `0x3D` - `0b00111101` - `'='`            | `'='`        |
| `0x3E` - `0b00111110` - `'>'`            | `'>'`        |
| `0x3F` - `0b00111111` - `'?'`            | `'?'`        |
| `0x40` - `0b01000000` - `'@'`            | `'@'`        |
| `0x41` - `0b01000001` - `'A'`            | `'A'`        |
| `0x42` - `0b01000010` - `'B'`            | `'B'`        |
| `0x43` - `0b01000011` - `'C'`            | `'C'`        |
| `0x44` - `0b01000100` - `'D'`            | `'D'`        |
| `0x45` - `0b01000101` - `'E'`            | `'E'`        |
| `0x46` - `0b01000110` - `'F'`            | `'F'`        |
| `0x47` - `0b01000111` - `'G'`            | `'G'`        |
| `0x48` - `0b01001000` - `'H'`            | `'H'`        |
| `0x49` - `0b01001001` - `'I'`            | `'I'`        |
| `0x4A` - `0b01001010` - `'J'`            | `'J'`        |
| `0x4B` - `0b01001011` - `'K'`            | `'K'`        |
| `0x4C` - `0b01001100` - `'L'`            | `'L'`        |
| `0x4D` - `0b01001101` - `'M'`            | `'M'`        |
| `0x4E` - `0b01001110` - `'N'`            | `'N'`        |
| `0x4F` - `0b01001111` - `'O'`            | `'O'`        |
| `0x50` - `0b01010000` - `'P'`            | `'P'`        |
| `0x51` - `0b01010001` - `'Q'`            | `'Q'`        |
| `0x52` - `0b01010010` - `'R'`            | `'R'`        |
| `0x53` - `0b01010011` - `'S'`            | `'S'`        |
| `0x54` - `0b01010100` - `'T'`            | `'T'`        |
| `0x55` - `0b01010101` - `'U'`            | `'U'`        |
| `0x56` - `0b01010110` - `'V'`            | `'V'`        |
| `0x57` - `0b01010111` - `'W'`            | `'W'`        |
| `0x58` - `0b01011000` - `'X'`            | `'X'`        |
| `0x59` - `0b01011001` - `'Y'`            | `'Y'`        |
| `0x5A` - `0b01011010` - `'Z'`            | `'Z'`        |
| `0x5B` - `0b01011011` - `'['`            | `'['`        |
| `0x5C` - `0b01011100` - `'\'`            | `'\'`        |
| `0x5D` - `0b01011101` - `']'`            | `']'`        |
| `0x5E` - `0b01011110` - `'^'`            | `'^'`        |
| `0x5F` - `0b01011111` - `'_'`            | `'_'`        |
| `0x60` - `0b01100000` - ``'`'``          | ``'`'``      |
| `0x61` - `0b01100001` - `'a'`            | `'a'`        |
| `0x62` - `0b01100010` - `'b'`            | `'b'`        |
| `0x63` - `0b01100011` - `'c'`            | `'c'`        |
| `0x64` - `0b01100100` - `'d'`            | `'d'`        |
| `0x65` - `0b01100101` - `'e'`            | `'e'`        |
| `0x66` - `0b01100110` - `'f'`            | `'f'`        |
| `0x67` - `0b01100111` - `'g'`            | `'g'`        |
| `0x68` - `0b01101000` - `'h'`            | `'h'`        |
| `0x69` - `0b01101001` - `'i'`            | `'i'`        |
| `0x6A` - `0b01101010` - `'j'`            | `'j'`        |
| `0x6B` - `0b01101011` - `'k'`            | `'k'`        |
| `0x6C` - `0b01101100` - `'l'`            | `'l'`        |
| `0x6D` - `0b01101101` - `'m'`            | `'m'`        |
| `0x6E` - `0b01101110` - `'n'`            | `'n'`        |
| `0x6F` - `0b01101111` - `'o'`            | `'o'`        |
| `0x70` - `0b01110000` - `'p'`            | `'p'`        |
| `0x71` - `0b01110001` - `'q'`            | `'q'`        |
| `0x72` - `0b01110010` - `'r'`            | `'r'`        |
| `0x73` - `0b01110011` - `'s'`            | `'s'`        |
| `0x74` - `0b01110100` - `'t'`            | `'t'`        |
| `0x75` - `0b01110101` - `'u'`            | `'u'`        |
| `0x76` - `0b01110110` - `'v'`            | `'v'`        |
| `0x77` - `0b01110111` - `'w'`            | `'w'`        |
| `0x78` - `0b01111000` - `'x'`            | `'x'`        |
| `0x79` - `0b01111001` - `'y'`            | `'y'`        |
| `0x7A` - `0b01111010` - `'z'`            | `'z'`        |
| `0x7B` - `0b01111011` - `'{'`            | `'{'`        |
| `0x7C` - `0b01111100` - `'\|'`           | `'\|'`       |
| `0x7D` - `0b01111101` - `'}'`            | `'}'`        |
| `0x7E` - `0b01111110` - `'~'`            | `'~'`        |
| `0x7F` - `0b01111111` - `DEL`            | `'Ψ'`        |
| `0x80` - `0b10000000` - `0x80 + NUL`     | `mod('α')`   |
| `0x81` - `0b10000001` - `0x80 + SOH`     | `mod('β')`   |
| `0x82` - `0b10000010` - `0x80 + STX`     | `mod('γ')`   |
| `0x83` - `0b10000011` - `0x80 + ETX`     | `mod('δ')`   |
| `0x84` - `0b10000100` - `0x80 + EOT`     | `mod('ε')`   |
| `0x85` - `0b10000101` - `0x80 + ENQ`     | `mod('ζ')`   |
| `0x86` - `0b10000110` - `0x80 + ACK`     | `mod('η')`   |
| `0x87` - `0b10000111` - `0x80 + BEL`     | `mod('θ')`   |
| `0x88` - `0b10001000` - `0x80 + BS`      | `mod('ι')`   |
| `0x89` - `0b10001001` - `0x80 + HT`      | `mod('κ')`   |
| `0x8A` - `0b10001010` - `0x80 + LF`      | `mod('◾)'   |
| `0x8B` - `0b10001011` - `0x80 + VT`      | `mod('λ')`   |
| `0x8C` - `0b10001100` - `0x80 + FF`      | `mod('μ')`   |
| `0x8D` - `0b10001101` - `0x80 + CR`      | `mod('ν')`   |
| `0x8E` - `0b10001110` - `0x80 + SO`      | `mod('ξ')`   |
| `0x8F` - `0b10001111` - `0x80 + SI`      | `mod('π')`   |
| `0x90` - `0b10010000` - `0x80 + DLE`     | `mod('ρ')`   |
| `0x91` - `0b10010001` - `0x80 + DC1`     | `mod('σ')`   |
| `0x92` - `0b10010010` - `0x80 + DC2`     | `mod('τ')`   |
| `0x93` - `0b10010011` - `0x80 + DC3`     | `mod('υ')`   |
| `0x94` - `0b10010100` - `0x80 + DC4`     | `mod('φ')`   |
| `0x95` - `0b10010101` - `0x80 + NAK`     | `mod('χ')`   |
| `0x96` - `0b10010110` - `0x80 + SYN`     | `mod('ψ')`   |
| `0x97` - `0b10010111` - `0x80 + ETB`     | `mod('ω')`   |
| `0x98` - `0b10011000` - `0x80 + CAN`     | `mod('Γ')`   |
| `0x99` - `0b10011001` - `0x80 + EM`      | `mod('Δ')`   |
| `0x9A` - `0b10011010` - `0x80 + SUB`     | `mod('Θ')`   |
| `0x9B` - `0b10011011` - `0x80 + ESC`     | `mod('Λ')`   |
| `0x9C` - `0b10011100` - `0x80 + FS`      | `mod('Ξ')`   |
| `0x9D` - `0b10011101` - `0x80 + GS`      | `mod('∏')`   |
| `0x9E` - `0b10011110` - `0x80 + RS`      | `mod('Σ')`   |
| `0x9F` - `0b10011111` - `0x80 + US`      | `mod('Φ')`   |
| `0xA0` - `0b10100000` - `0x80 + ' '`     | `mod('⸱')`   |
| `0xA1` - `0b10100001` - `0x80 + '!'`     | `mod('!')`   |
| `0xA2` - `0b10100010` - `0x80 + '"'`     | `mod('"')`   |
| `0xA3` - `0b10100011` - `0x80 + '#'`     | `mod('#')`   |
| `0xA4` - `0b10100100` - `0x80 + '$'`     | `mod('$')`   |
| `0xA5` - `0b10100101` - `0x80 + '%'`     | `mod('%')`   |
| `0xA6` - `0b10100110` - `0x80 + '&'`     | `mod('&')`   |
| `0xA7` - `0b10100111` - `0x80 + '\''`    | `mod(''')`   |
| `0xA8` - `0b10101000` - `0x80 + '('`     | `mod('(')`   |
| `0xA9` - `0b10101001` - `0x80 + ')'`     | `mod(')')`   |
| `0xAA` - `0b10101010` - `0x80 + '*'`     | `mod('*')`   |
| `0xAB` - `0b10101011` - `0x80 + '+'`     | `mod('+')`   |
| `0xAC` - `0b10101100` - `0x80 + ','`     | `mod(',')`   |
| `0xAD` - `0b10101101` - `0x80 + '-'`     | `mod('-')`   |
| `0xAE` - `0b10101110` - `0x80 + '.'`     | `mod('.')`   |
| `0xAF` - `0b10101111` - `0x80 + '/'`     | `mod('/')`   |
| `0xB0` - `0b10110000` - `0x80 + '0'`     | `mod('0')`   |
| `0xB1` - `0b10110001` - `0x80 + '1'`     | `mod('1')`   |
| `0xB2` - `0b10110010` - `0x80 + '2'`     | `mod('2')`   |
| `0xB3` - `0b10110011` - `0x80 + '3'`     | `mod('3')`   |
| `0xB4` - `0b10110100` - `0x80 + '4'`     | `mod('4')`   |
| `0xB5` - `0b10110101` - `0x80 + '5'`     | `mod('5')`   |
| `0xB6` - `0b10110110` - `0x80 + '6'`     | `mod('6')`   |
| `0xB7` - `0b10110111` - `0x80 + '7'`     | `mod('7')`   |
| `0xB8` - `0b10111000` - `0x80 + '8'`     | `mod('8')`   |
| `0xB9` - `0b10111001` - `0x80 + '9'`     | `mod('9')`   |
| `0xBA` - `0b10111010` - `0x80 + ':'`     | `mod(':')`   |
| `0xBB` - `0b10111011` - `0x80 + ';'`     | `mod(';')`   |
| `0xBC` - `0b10111100` - `0x80 + '<'`     | `mod('<')`   |
| `0xBD` - `0b10111101` - `0x80 + '='`     | `mod('=')`   |
| `0xBE` - `0b10111110` - `0x80 + '>'`     | `mod('>')`   |
| `0xBF` - `0b10111111` - `0x80 + '?'`     | `mod('?')`   |
| `0xC0` - `0b11000000` - `0x80 + '@'`     | `mod('@')`   |
| `0xC1` - `0b11000001` - `0x80 + 'A'`     | `mod('A')`   |
| `0xC2` - `0b11000010` - `0x80 + 'B'`     | `mod('B')`   |
| `0xC3` - `0b11000011` - `0x80 + 'C'`     | `mod('C')`   |
| `0xC4` - `0b11000100` - `0x80 + 'D'`     | `mod('D')`   |
| `0xC5` - `0b11000101` - `0x80 + 'E'`     | `mod('E')`   |
| `0xC6` - `0b11000110` - `0x80 + 'F'`     | `mod('F')`   |
| `0xC7` - `0b11000111` - `0x80 + 'G'`     | `mod('G')`   |
| `0xC8` - `0b11001000` - `0x80 + 'H'`     | `mod('H')`   |
| `0xC9` - `0b11001001` - `0x80 + 'I'`     | `mod('I')`   |
| `0xCA` - `0b11001010` - `0x80 + 'J'`     | `mod('J')`   |
| `0xCB` - `0b11001011` - `0x80 + 'K'`     | `mod('K')`   |
| `0xCC` - `0b11001100` - `0x80 + 'L'`     | `mod('L')`   |
| `0xCD` - `0b11001101` - `0x80 + 'M'`     | `mod('M')`   |
| `0xCE` - `0b11001110` - `0x80 + 'N'`     | `mod('N')`   |
| `0xCF` - `0b11001111` - `0x80 + 'O'`     | `mod('O')`   |
| `0xD0` - `0b11010000` - `0x80 + 'P'`     | `mod('P')`   |
| `0xD1` - `0b11010001` - `0x80 + 'Q'`     | `mod('Q')`   |
| `0xD2` - `0b11010010` - `0x80 + 'R'`     | `mod('R')`   |
| `0xD3` - `0b11010011` - `0x80 + 'S'`     | `mod('S')`   |
| `0xD4` - `0b11010100` - `0x80 + 'T'`     | `mod('T')`   |
| `0xD5` - `0b11010101` - `0x80 + 'U'`     | `mod('U')`   |
| `0xD6` - `0b11010110` - `0x80 + 'V'`     | `mod('V')`   |
| `0xD7` - `0b11010111` - `0x80 + 'W'`     | `mod('W')`   |
| `0xD8` - `0b11011000` - `0x80 + 'X'`     | `mod('X')`   |
| `0xD9` - `0b11011001` - `0x80 + 'Y'`     | `mod('Y')`   |
| `0xDA` - `0b11011010` - `0x80 + 'Z'`     | `mod('Z')`   |
| `0xDB` - `0b11011011` - `0x80 + '['`     | `mod('[')`   |
| `0xDC` - `0b11011100` - `0x80 + '\'`     | `mod('\')`   |
| `0xDD` - `0b11011101` - `0x80 + ']'`     | `mod(']')`   |
| `0xDE` - `0b11011110` - `0x80 + '^'`     | `mod('^')`   |
| `0xDF` - `0b11011111` - `0x80 + '_'`     | `mod('_')`   |
| `0xE0` - `0b11100000` - ``0x80 + '`'``   | ``mod('`')`` |
| `0xE1` - `0b11100001` - `0x80 + 'a'`     | `mod('a')`   |
| `0xE2` - `0b11100010` - `0x80 + 'b'`     | `mod('b')`   |
| `0xE3` - `0b11100011` - `0x80 + 'c'`     | `mod('c')`   |
| `0xE4` - `0b11100100` - `0x80 + 'd'`     | `mod('d')`   |
| `0xE5` - `0b11100101` - `0x80 + 'e'`     | `mod('e')`   |
| `0xE6` - `0b11100110` - `0x80 + 'f'`     | `mod('f')`   |
| `0xE7` - `0b11100111` - `0x80 + 'g'`     | `mod('g')`   |
| `0xE8` - `0b11101000` - `0x80 + 'h'`     | `mod('h')`   |
| `0xE9` - `0b11101001` - `0x80 + 'i'`     | `mod('i')`   |
| `0xEA` - `0b11101010` - `0x80 + 'j'`     | `mod('j')`   |
| `0xEB` - `0b11101011` - `0x80 + 'k'`     | `mod('k')`   |
| `0xEC` - `0b11101100` - `0x80 + 'l'`     | `mod('l')`   |
| `0xED` - `0b11101101` - `0x80 + 'm'`     | `mod('m')`   |
| `0xEE` - `0b11101110` - `0x80 + 'n'`     | `mod('n')`   |
| `0xEF` - `0b11101111` - `0x80 + 'o'`     | `mod('o')`   |
| `0xF0` - `0b11110000` - `0x80 + 'p'`     | `mod('p')`   |
| `0xF1` - `0b11110001` - `0x80 + 'q'`     | `mod('q')`   |
| `0xF2` - `0b11110010` - `0x80 + 'r'`     | `mod('r')`   |
| `0xF3` - `0b11110011` - `0x80 + 's'`     | `mod('s')`   |
| `0xF4` - `0b11110100` - `0x80 + 't'`     | `mod('t')`   |
| `0xF5` - `0b11110101` - `0x80 + 'u'`     | `mod('u')`   |
| `0xF6` - `0b11110110` - `0x80 + 'v'`     | `mod('v')`   |
| `0xF7` - `0b11110111` - `0x80 + 'w'`     | `mod('w')`   |
| `0xF8` - `0b11111000` - `0x80 + 'x'`     | `mod('x')`   |
| `0xF9` - `0b11111001` - `0x80 + 'y'`     | `mod('y')`   |
| `0xFA` - `0b11111010` - `0x80 + 'z'`     | `mod('z')`   |
| `0xFB` - `0b11111011` - `0x80 + '{'`     | `mod('{')`   |
| `0xFC` - `0b11111100` - `0x80 + '\|'`    | `mod('\|')`  |
| `0xFD` - `0b11111101` - `0x80 + '}'`     | `mod('}')`   |
| `0xFE` - `0b11111110` - `0x80 + '~'`     | `mod('~')`   |
| `0xFF` - `0b11111111` - `0x80 + DEL`     | `mod('Ψ')`   |

> **procedure** _derivation of the above table_
>
> 1. set bytes `0x20..=0x7E` to a copy of [[ascii]], bytes which correspond to printable [[character]]s
> 2. set byte `0x20` (Space) to `'⸱'` (Word Separator Middle Dot) and byte `0x0A` (Line Feed) to `'◾'` (Black Medium Small Square)
> 3. fill empty bytes in `0x00..=0x7F` with lower[[case]] then upper[[case]] greek letters whose glyphs look different from that of latin letters
>    > **note** the _lower[[case]] then upper[[case]] greek letters whose glyphs look different from that of latin letters_ are: _αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞ∏ΣΦΨΩ_
> 4. set every byte in `0x80..=0xFF` to the corresponding [[character]] in `0x00..=0x7F` with an unspecified modifier `mod` applied
>    > **note** any discernible modifier can be used, including font weight, font style, font family, font color, background color, and so on
