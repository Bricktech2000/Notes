## Base256

&mdash; me

**see** [[ascii]]

[[base256]] is a binary-to-text encoding scheme. it encodes 8-bit bytes into single characters in such a way that printable [[ascii]] data is represented one-to-one and that the output can be decoded manually if necessary

[[base256]] is meant to be used to losslessly and compatcly store arbitrary data on sheets of paper as a ridiculously future-proof backup medium. it is fast and cheap to produce, and can be read by humans and machines alike

> **example** the [[utf-8]] [[string]] <code>"did you know that &tau; > &pi;?\n"</code>, which is [[hexadecimal]] `64 69 64 20 79 6f 75 20 6b 6e 6f 77 20 74 68 61 74 20 cf 84 20 3e 20 cf 80 3f 0a`, is equivalent to <code>"did&#x2E31;you&#x2E31;know&#x2E31;that&#x2E31;<u>O&epsilon;</u>&#x2E31;&gt;&#x2E31;<u>O&alpha;</u>?&#x25FE;"</code> encoded in [[base256]]. see [[tau]]

**properties**

[[base256]] can be thought of as a [[set#superset]] of printable [[ascii]]

[[base256]] is whitespace-insensitive by design

**representation**

| [[hexadecimal]] &bull; [[binary]] &bull; [[ascii]] | [[base256]]        |
| -------------------------------------------------- | ------------------ |
| `0x00` &bull; `0b00000000` &bull; `NUL`            | `'&alpha;'`        |
| `0x01` &bull; `0b00000001` &bull; `SOH`            | `'&beta;'`         |
| `0x02` &bull; `0b00000010` &bull; `STX`            | `'&gamma;'`        |
| `0x03` &bull; `0b00000011` &bull; `ETX`            | `'&delta;'`        |
| `0x04` &bull; `0b00000100` &bull; `EOT`            | `'&epsilon;'`      |
| `0x05` &bull; `0b00000101` &bull; `ENQ`            | `'&zeta;'`         |
| `0x06` &bull; `0b00000110` &bull; `ACK`            | `'&eta;'`          |
| `0x07` &bull; `0b00000111` &bull; `BEL`            | `'&theta;'`        |
| `0x08` &bull; `0b00001000` &bull; `BS`             | `'&iota;'`         |
| `0x09` &bull; `0b00001001` &bull; `HT`             | `'&kappa;'`        |
| `0x0A` &bull; `0b00001010` &bull; `LF`             | `'&#x25FE;'`       |
| `0x0B` &bull; `0b00001011` &bull; `VT`             | `'&lambda;'`       |
| `0x0C` &bull; `0b00001100` &bull; `FF`             | `'&mu;'`           |
| `0x0D` &bull; `0b00001101` &bull; `CR`             | `'&nu;'`           |
| `0x0E` &bull; `0b00001110` &bull; `SO`             | `'&xi;'`           |
| `0x0F` &bull; `0b00001111` &bull; `SI`             | `'&pi;'`           |
| `0x10` &bull; `0b00010000` &bull; `DLE`            | `'&rho;'`          |
| `0x11` &bull; `0b00010001` &bull; `DC1`            | `'&sigma;'`        |
| `0x12` &bull; `0b00010010` &bull; `DC2`            | `'&tau;'`          |
| `0x13` &bull; `0b00010011` &bull; `DC3`            | `'&upsilon;'`      |
| `0x14` &bull; `0b00010100` &bull; `DC4`            | `'&phi;'`          |
| `0x15` &bull; `0b00010101` &bull; `NAK`            | `'&chi;'`          |
| `0x16` &bull; `0b00010110` &bull; `SYN`            | `'&psi;'`          |
| `0x17` &bull; `0b00010111` &bull; `ETB`            | `'&omega;'`        |
| `0x18` &bull; `0b00011000` &bull; `CAN`            | `'&Gamma;'`        |
| `0x19` &bull; `0b00011001` &bull; `EM`             | `'&Delta;'`        |
| `0x1A` &bull; `0b00011010` &bull; `SUB`            | `'&Theta;'`        |
| `0x1B` &bull; `0b00011011` &bull; `ESC`            | `'&Lambda;'`       |
| `0x1C` &bull; `0b00011100` &bull; `FS`             | `'&Xi;'`           |
| `0x1D` &bull; `0b00011101` &bull; `GS`             | `'&Pi;'`           |
| `0x1E` &bull; `0b00011110` &bull; `RS`             | `'&Sigma;'`        |
| `0x1F` &bull; `0b00011111` &bull; `US`             | `'&Phi;'`          |
| `0x20` &bull; `0b00100000` &bull; `' '`            | `'&#x2E31;'`       |
| `0x21` &bull; `0b00100001` &bull; `'!'`            | `'!'`              |
| `0x22` &bull; `0b00100010` &bull; `'"'`            | `'"'`              |
| `0x23` &bull; `0b00100011` &bull; `'#'`            | `'#'`              |
| `0x24` &bull; `0b00100100` &bull; `'$'`            | `'$'`              |
| `0x25` &bull; `0b00100101` &bull; `'%'`            | `'%'`              |
| `0x26` &bull; `0b00100110` &bull; `'&'`            | `'&'`              |
| `0x27` &bull; `0b00100111` &bull; `'\''`           | `'''`              |
| `0x28` &bull; `0b00101000` &bull; `'('`            | `'('`              |
| `0x29` &bull; `0b00101001` &bull; `')'`            | `')'`              |
| `0x2A` &bull; `0b00101010` &bull; `'*'`            | `'*'`              |
| `0x2B` &bull; `0b00101011` &bull; `'+'`            | `'+'`              |
| `0x2C` &bull; `0b00101100` &bull; `','`            | `','`              |
| `0x2D` &bull; `0b00101101` &bull; `'-'`            | `'-'`              |
| `0x2E` &bull; `0b00101110` &bull; `'.'`            | `'.'`              |
| `0x2F` &bull; `0b00101111` &bull; `'/'`            | `'/'`              |
| `0x30` &bull; `0b00110000` &bull; `'0'`            | `'0'`              |
| `0x31` &bull; `0b00110001` &bull; `'1'`            | `'1'`              |
| `0x32` &bull; `0b00110010` &bull; `'2'`            | `'2'`              |
| `0x33` &bull; `0b00110011` &bull; `'3'`            | `'3'`              |
| `0x34` &bull; `0b00110100` &bull; `'4'`            | `'4'`              |
| `0x35` &bull; `0b00110101` &bull; `'5'`            | `'5'`              |
| `0x36` &bull; `0b00110110` &bull; `'6'`            | `'6'`              |
| `0x37` &bull; `0b00110111` &bull; `'7'`            | `'7'`              |
| `0x38` &bull; `0b00111000` &bull; `'8'`            | `'8'`              |
| `0x39` &bull; `0b00111001` &bull; `'9'`            | `'9'`              |
| `0x3A` &bull; `0b00111010` &bull; `':'`            | `':'`              |
| `0x3B` &bull; `0b00111011` &bull; `';'`            | `';'`              |
| `0x3C` &bull; `0b00111100` &bull; `'<'`            | `'<'`              |
| `0x3D` &bull; `0b00111101` &bull; `'='`            | `'='`              |
| `0x3E` &bull; `0b00111110` &bull; `'>'`            | `'>'`              |
| `0x3F` &bull; `0b00111111` &bull; `'?'`            | `'?'`              |
| `0x40` &bull; `0b01000000` &bull; `'@'`            | `'@'`              |
| `0x41` &bull; `0b01000001` &bull; `'A'`            | `'A'`              |
| `0x42` &bull; `0b01000010` &bull; `'B'`            | `'B'`              |
| `0x43` &bull; `0b01000011` &bull; `'C'`            | `'C'`              |
| `0x44` &bull; `0b01000100` &bull; `'D'`            | `'D'`              |
| `0x45` &bull; `0b01000101` &bull; `'E'`            | `'E'`              |
| `0x46` &bull; `0b01000110` &bull; `'F'`            | `'F'`              |
| `0x47` &bull; `0b01000111` &bull; `'G'`            | `'G'`              |
| `0x48` &bull; `0b01001000` &bull; `'H'`            | `'H'`              |
| `0x49` &bull; `0b01001001` &bull; `'I'`            | `'I'`              |
| `0x4A` &bull; `0b01001010` &bull; `'J'`            | `'J'`              |
| `0x4B` &bull; `0b01001011` &bull; `'K'`            | `'K'`              |
| `0x4C` &bull; `0b01001100` &bull; `'L'`            | `'L'`              |
| `0x4D` &bull; `0b01001101` &bull; `'M'`            | `'M'`              |
| `0x4E` &bull; `0b01001110` &bull; `'N'`            | `'N'`              |
| `0x4F` &bull; `0b01001111` &bull; `'O'`            | `'O'`              |
| `0x50` &bull; `0b01010000` &bull; `'P'`            | `'P'`              |
| `0x51` &bull; `0b01010001` &bull; `'Q'`            | `'Q'`              |
| `0x52` &bull; `0b01010010` &bull; `'R'`            | `'R'`              |
| `0x53` &bull; `0b01010011` &bull; `'S'`            | `'S'`              |
| `0x54` &bull; `0b01010100` &bull; `'T'`            | `'T'`              |
| `0x55` &bull; `0b01010101` &bull; `'U'`            | `'U'`              |
| `0x56` &bull; `0b01010110` &bull; `'V'`            | `'V'`              |
| `0x57` &bull; `0b01010111` &bull; `'W'`            | `'W'`              |
| `0x58` &bull; `0b01011000` &bull; `'X'`            | `'X'`              |
| `0x59` &bull; `0b01011001` &bull; `'Y'`            | `'Y'`              |
| `0x5A` &bull; `0b01011010` &bull; `'Z'`            | `'Z'`              |
| `0x5B` &bull; `0b01011011` &bull; `'['`            | `'['`              |
| `0x5C` &bull; `0b01011100` &bull; `'\'`            | `'\'`              |
| `0x5D` &bull; `0b01011101` &bull; `']'`            | `']'`              |
| `0x5E` &bull; `0b01011110` &bull; `'^'`            | `'^'`              |
| `0x5F` &bull; `0b01011111` &bull; `'_'`            | `'_'`              |
| `0x60` &bull; `0b01100000` &bull; ``'`'``          | ``'`'``            |
| `0x61` &bull; `0b01100001` &bull; `'a'`            | `'a'`              |
| `0x62` &bull; `0b01100010` &bull; `'b'`            | `'b'`              |
| `0x63` &bull; `0b01100011` &bull; `'c'`            | `'c'`              |
| `0x64` &bull; `0b01100100` &bull; `'d'`            | `'d'`              |
| `0x65` &bull; `0b01100101` &bull; `'e'`            | `'e'`              |
| `0x66` &bull; `0b01100110` &bull; `'f'`            | `'f'`              |
| `0x67` &bull; `0b01100111` &bull; `'g'`            | `'g'`              |
| `0x68` &bull; `0b01101000` &bull; `'h'`            | `'h'`              |
| `0x69` &bull; `0b01101001` &bull; `'i'`            | `'i'`              |
| `0x6A` &bull; `0b01101010` &bull; `'j'`            | `'j'`              |
| `0x6B` &bull; `0b01101011` &bull; `'k'`            | `'k'`              |
| `0x6C` &bull; `0b01101100` &bull; `'l'`            | `'l'`              |
| `0x6D` &bull; `0b01101101` &bull; `'m'`            | `'m'`              |
| `0x6E` &bull; `0b01101110` &bull; `'n'`            | `'n'`              |
| `0x6F` &bull; `0b01101111` &bull; `'o'`            | `'o'`              |
| `0x70` &bull; `0b01110000` &bull; `'p'`            | `'p'`              |
| `0x71` &bull; `0b01110001` &bull; `'q'`            | `'q'`              |
| `0x72` &bull; `0b01110010` &bull; `'r'`            | `'r'`              |
| `0x73` &bull; `0b01110011` &bull; `'s'`            | `'s'`              |
| `0x74` &bull; `0b01110100` &bull; `'t'`            | `'t'`              |
| `0x75` &bull; `0b01110101` &bull; `'u'`            | `'u'`              |
| `0x76` &bull; `0b01110110` &bull; `'v'`            | `'v'`              |
| `0x77` &bull; `0b01110111` &bull; `'w'`            | `'w'`              |
| `0x78` &bull; `0b01111000` &bull; `'x'`            | `'x'`              |
| `0x79` &bull; `0b01111001` &bull; `'y'`            | `'y'`              |
| `0x7A` &bull; `0b01111010` &bull; `'z'`            | `'z'`              |
| `0x7B` &bull; `0b01111011` &bull; `'{'`            | `'{'`              |
| `0x7C` &bull; `0b01111100` &bull; `'\|'`           | `'\|'`             |
| `0x7D` &bull; `0b01111101` &bull; `'}'`            | `'}'`              |
| `0x7E` &bull; `0b01111110` &bull; `'~'`            | `'~'`              |
| `0x7F` &bull; `0b01111111` &bull; `DEL`            | `'&Psi;'`          |
| `0x80` &bull; `0b10000000` &bull; `0x80 + NUL`     | `mod('&alpha;')`   |
| `0x81` &bull; `0b10000001` &bull; `0x80 + SOH`     | `mod('&beta;')`    |
| `0x82` &bull; `0b10000010` &bull; `0x80 + STX`     | `mod('&gamma;')`   |
| `0x83` &bull; `0b10000011` &bull; `0x80 + ETX`     | `mod('&delta;')`   |
| `0x84` &bull; `0b10000100` &bull; `0x80 + EOT`     | `mod('&epsilon;')` |
| `0x85` &bull; `0b10000101` &bull; `0x80 + ENQ`     | `mod('&zeta;')`    |
| `0x86` &bull; `0b10000110` &bull; `0x80 + ACK`     | `mod('&eta;')`     |
| `0x87` &bull; `0b10000111` &bull; `0x80 + BEL`     | `mod('&theta;')`   |
| `0x88` &bull; `0b10001000` &bull; `0x80 + BS`      | `mod('&iota;')`    |
| `0x89` &bull; `0b10001001` &bull; `0x80 + HT`      | `mod('&kappa;')`   |
| `0x8A` &bull; `0b10001010` &bull; `0x80 + LF`      | `mod('&#x25FE;')`  |
| `0x8B` &bull; `0b10001011` &bull; `0x80 + VT`      | `mod('&lambda;')`  |
| `0x8C` &bull; `0b10001100` &bull; `0x80 + FF`      | `mod('&mu;')`      |
| `0x8D` &bull; `0b10001101` &bull; `0x80 + CR`      | `mod('&nu;')`      |
| `0x8E` &bull; `0b10001110` &bull; `0x80 + SO`      | `mod('&xi;')`      |
| `0x8F` &bull; `0b10001111` &bull; `0x80 + SI`      | `mod('&pi;')`      |
| `0x90` &bull; `0b10010000` &bull; `0x80 + DLE`     | `mod('&rho;')`     |
| `0x91` &bull; `0b10010001` &bull; `0x80 + DC1`     | `mod('&sigma;')`   |
| `0x92` &bull; `0b10010010` &bull; `0x80 + DC2`     | `mod('&tau;')`     |
| `0x93` &bull; `0b10010011` &bull; `0x80 + DC3`     | `mod('&upsilon;')` |
| `0x94` &bull; `0b10010100` &bull; `0x80 + DC4`     | `mod('&phi;')`     |
| `0x95` &bull; `0b10010101` &bull; `0x80 + NAK`     | `mod('&chi;')`     |
| `0x96` &bull; `0b10010110` &bull; `0x80 + SYN`     | `mod('&psi;')`     |
| `0x97` &bull; `0b10010111` &bull; `0x80 + ETB`     | `mod('&omega;')`   |
| `0x98` &bull; `0b10011000` &bull; `0x80 + CAN`     | `mod('&Gamma;')`   |
| `0x99` &bull; `0b10011001` &bull; `0x80 + EM`      | `mod('&Delta;')`   |
| `0x9A` &bull; `0b10011010` &bull; `0x80 + SUB`     | `mod('&Theta;')`   |
| `0x9B` &bull; `0b10011011` &bull; `0x80 + ESC`     | `mod('&Lambda;')`  |
| `0x9C` &bull; `0b10011100` &bull; `0x80 + FS`      | `mod('&Xi;')`      |
| `0x9D` &bull; `0b10011101` &bull; `0x80 + GS`      | `mod('&Pi;')`      |
| `0x9E` &bull; `0b10011110` &bull; `0x80 + RS`      | `mod('&Sigma;')`   |
| `0x9F` &bull; `0b10011111` &bull; `0x80 + US`      | `mod('&Phi;')`     |
| `0xA0` &bull; `0b10100000` &bull; `0x80 + ' '`     | `mod('&#x2E31;')`  |
| `0xA1` &bull; `0b10100001` &bull; `0x80 + '!'`     | `mod('!')`         |
| `0xA2` &bull; `0b10100010` &bull; `0x80 + '"'`     | `mod('"')`         |
| `0xA3` &bull; `0b10100011` &bull; `0x80 + '#'`     | `mod('#')`         |
| `0xA4` &bull; `0b10100100` &bull; `0x80 + '$'`     | `mod('$')`         |
| `0xA5` &bull; `0b10100101` &bull; `0x80 + '%'`     | `mod('%')`         |
| `0xA6` &bull; `0b10100110` &bull; `0x80 + '&'`     | `mod('&')`         |
| `0xA7` &bull; `0b10100111` &bull; `0x80 + '\''`    | `mod(''')`         |
| `0xA8` &bull; `0b10101000` &bull; `0x80 + '('`     | `mod('(')`         |
| `0xA9` &bull; `0b10101001` &bull; `0x80 + ')'`     | `mod(')')`         |
| `0xAA` &bull; `0b10101010` &bull; `0x80 + '*'`     | `mod('*')`         |
| `0xAB` &bull; `0b10101011` &bull; `0x80 + '+'`     | `mod('+')`         |
| `0xAC` &bull; `0b10101100` &bull; `0x80 + ','`     | `mod(',')`         |
| `0xAD` &bull; `0b10101101` &bull; `0x80 + '-'`     | `mod('-')`         |
| `0xAE` &bull; `0b10101110` &bull; `0x80 + '.'`     | `mod('.')`         |
| `0xAF` &bull; `0b10101111` &bull; `0x80 + '/'`     | `mod('/')`         |
| `0xB0` &bull; `0b10110000` &bull; `0x80 + '0'`     | `mod('0')`         |
| `0xB1` &bull; `0b10110001` &bull; `0x80 + '1'`     | `mod('1')`         |
| `0xB2` &bull; `0b10110010` &bull; `0x80 + '2'`     | `mod('2')`         |
| `0xB3` &bull; `0b10110011` &bull; `0x80 + '3'`     | `mod('3')`         |
| `0xB4` &bull; `0b10110100` &bull; `0x80 + '4'`     | `mod('4')`         |
| `0xB5` &bull; `0b10110101` &bull; `0x80 + '5'`     | `mod('5')`         |
| `0xB6` &bull; `0b10110110` &bull; `0x80 + '6'`     | `mod('6')`         |
| `0xB7` &bull; `0b10110111` &bull; `0x80 + '7'`     | `mod('7')`         |
| `0xB8` &bull; `0b10111000` &bull; `0x80 + '8'`     | `mod('8')`         |
| `0xB9` &bull; `0b10111001` &bull; `0x80 + '9'`     | `mod('9')`         |
| `0xBA` &bull; `0b10111010` &bull; `0x80 + ':'`     | `mod(':')`         |
| `0xBB` &bull; `0b10111011` &bull; `0x80 + ';'`     | `mod(';')`         |
| `0xBC` &bull; `0b10111100` &bull; `0x80 + '<'`     | `mod('<')`         |
| `0xBD` &bull; `0b10111101` &bull; `0x80 + '='`     | `mod('=')`         |
| `0xBE` &bull; `0b10111110` &bull; `0x80 + '>'`     | `mod('>')`         |
| `0xBF` &bull; `0b10111111` &bull; `0x80 + '?'`     | `mod('?')`         |
| `0xC0` &bull; `0b11000000` &bull; `0x80 + '@'`     | `mod('@')`         |
| `0xC1` &bull; `0b11000001` &bull; `0x80 + 'A'`     | `mod('A')`         |
| `0xC2` &bull; `0b11000010` &bull; `0x80 + 'B'`     | `mod('B')`         |
| `0xC3` &bull; `0b11000011` &bull; `0x80 + 'C'`     | `mod('C')`         |
| `0xC4` &bull; `0b11000100` &bull; `0x80 + 'D'`     | `mod('D')`         |
| `0xC5` &bull; `0b11000101` &bull; `0x80 + 'E'`     | `mod('E')`         |
| `0xC6` &bull; `0b11000110` &bull; `0x80 + 'F'`     | `mod('F')`         |
| `0xC7` &bull; `0b11000111` &bull; `0x80 + 'G'`     | `mod('G')`         |
| `0xC8` &bull; `0b11001000` &bull; `0x80 + 'H'`     | `mod('H')`         |
| `0xC9` &bull; `0b11001001` &bull; `0x80 + 'I'`     | `mod('I')`         |
| `0xCA` &bull; `0b11001010` &bull; `0x80 + 'J'`     | `mod('J')`         |
| `0xCB` &bull; `0b11001011` &bull; `0x80 + 'K'`     | `mod('K')`         |
| `0xCC` &bull; `0b11001100` &bull; `0x80 + 'L'`     | `mod('L')`         |
| `0xCD` &bull; `0b11001101` &bull; `0x80 + 'M'`     | `mod('M')`         |
| `0xCE` &bull; `0b11001110` &bull; `0x80 + 'N'`     | `mod('N')`         |
| `0xCF` &bull; `0b11001111` &bull; `0x80 + 'O'`     | `mod('O')`         |
| `0xD0` &bull; `0b11010000` &bull; `0x80 + 'P'`     | `mod('P')`         |
| `0xD1` &bull; `0b11010001` &bull; `0x80 + 'Q'`     | `mod('Q')`         |
| `0xD2` &bull; `0b11010010` &bull; `0x80 + 'R'`     | `mod('R')`         |
| `0xD3` &bull; `0b11010011` &bull; `0x80 + 'S'`     | `mod('S')`         |
| `0xD4` &bull; `0b11010100` &bull; `0x80 + 'T'`     | `mod('T')`         |
| `0xD5` &bull; `0b11010101` &bull; `0x80 + 'U'`     | `mod('U')`         |
| `0xD6` &bull; `0b11010110` &bull; `0x80 + 'V'`     | `mod('V')`         |
| `0xD7` &bull; `0b11010111` &bull; `0x80 + 'W'`     | `mod('W')`         |
| `0xD8` &bull; `0b11011000` &bull; `0x80 + 'X'`     | `mod('X')`         |
| `0xD9` &bull; `0b11011001` &bull; `0x80 + 'Y'`     | `mod('Y')`         |
| `0xDA` &bull; `0b11011010` &bull; `0x80 + 'Z'`     | `mod('Z')`         |
| `0xDB` &bull; `0b11011011` &bull; `0x80 + '['`     | `mod('[')`         |
| `0xDC` &bull; `0b11011100` &bull; `0x80 + '\'`     | `mod('\')`         |
| `0xDD` &bull; `0b11011101` &bull; `0x80 + ']'`     | `mod(']')`         |
| `0xDE` &bull; `0b11011110` &bull; `0x80 + '^'`     | `mod('^')`         |
| `0xDF` &bull; `0b11011111` &bull; `0x80 + '_'`     | `mod('_')`         |
| `0xE0` &bull; `0b11100000` &bull; `0x80 + '`' ``   | ``mod('`') ``      |
| `0xE1` &bull; `0b11100001` &bull; `0x80 + 'a'`     | `mod('a')`         |
| `0xE2` &bull; `0b11100010` &bull; `0x80 + 'b'`     | `mod('b')`         |
| `0xE3` &bull; `0b11100011` &bull; `0x80 + 'c'`     | `mod('c')`         |
| `0xE4` &bull; `0b11100100` &bull; `0x80 + 'd'`     | `mod('d')`         |
| `0xE5` &bull; `0b11100101` &bull; `0x80 + 'e'`     | `mod('e')`         |
| `0xE6` &bull; `0b11100110` &bull; `0x80 + 'f'`     | `mod('f')`         |
| `0xE7` &bull; `0b11100111` &bull; `0x80 + 'g'`     | `mod('g')`         |
| `0xE8` &bull; `0b11101000` &bull; `0x80 + 'h'`     | `mod('h')`         |
| `0xE9` &bull; `0b11101001` &bull; `0x80 + 'i'`     | `mod('i')`         |
| `0xEA` &bull; `0b11101010` &bull; `0x80 + 'j'`     | `mod('j')`         |
| `0xEB` &bull; `0b11101011` &bull; `0x80 + 'k'`     | `mod('k')`         |
| `0xEC` &bull; `0b11101100` &bull; `0x80 + 'l'`     | `mod('l')`         |
| `0xED` &bull; `0b11101101` &bull; `0x80 + 'm'`     | `mod('m')`         |
| `0xEE` &bull; `0b11101110` &bull; `0x80 + 'n'`     | `mod('n')`         |
| `0xEF` &bull; `0b11101111` &bull; `0x80 + 'o'`     | `mod('o')`         |
| `0xF0` &bull; `0b11110000` &bull; `0x80 + 'p'`     | `mod('p')`         |
| `0xF1` &bull; `0b11110001` &bull; `0x80 + 'q'`     | `mod('q')`         |
| `0xF2` &bull; `0b11110010` &bull; `0x80 + 'r'`     | `mod('r')`         |
| `0xF3` &bull; `0b11110011` &bull; `0x80 + 's'`     | `mod('s')`         |
| `0xF4` &bull; `0b11110100` &bull; `0x80 + 't'`     | `mod('t')`         |
| `0xF5` &bull; `0b11110101` &bull; `0x80 + 'u'`     | `mod('u')`         |
| `0xF6` &bull; `0b11110110` &bull; `0x80 + 'v'`     | `mod('v')`         |
| `0xF7` &bull; `0b11110111` &bull; `0x80 + 'w'`     | `mod('w')`         |
| `0xF8` &bull; `0b11111000` &bull; `0x80 + 'x'`     | `mod('x')`         |
| `0xF9` &bull; `0b11111001` &bull; `0x80 + 'y'`     | `mod('y')`         |
| `0xFA` &bull; `0b11111010` &bull; `0x80 + 'z'`     | `mod('z')`         |
| `0xFB` &bull; `0b11111011` &bull; `0x80 + '{'`     | `mod('{')`         |
| `0xFC` &bull; `0b11111100` &bull; `0x80 + '\|'`    | `mod('\|')`        |
| `0xFD` &bull; `0b11111101` &bull; `0x80 + '}'`     | `mod('}')`         |
| `0xFE` &bull; `0b11111110` &bull; `0x80 + '~'`     | `mod('~')`         |
| `0xFF` &bull; `0b11111111` &bull; `0x80 + DEL`     | `mod('&Psi;')`     |

> **procedure** _derivation of the above table_
>
> 1. set bytes `0x20..=0x7E` to a copy of [[ascii]], bytes which correspond to printable [[character]]s
> 2. set byte `0x20` (Space) to `'&#x2E31;'` (Word Separator Middle Dot) and byte `0x0A` (Line Feed) to `'&#x25FE;'` (Black Medium Small Square)
> 3. fill empty bytes in `0x00..=0x7F` with lower[[case]] then upper[[case]] greek letters whose glyphs look different from that of latin letters
>    > **note** the _lower[[case]] then upper[[case]] greek letters whose glyphs look different from that of latin letters_ are as follows: _&alpha;&beta;&gamma;&delta;&epsilon;&zeta;&eta;&theta;&iota;&kappa;&lambda;&mu;&nu;&xi;&pi;&rho;&sigma;&tau;&upsilon;&phi;&chi;&psi;&omega;&Gamma;&Delta;&Theta;&Lambda;&Xi;&Pi;&Sigma;&Phi;&Psi;&Omega;_
> 4. set every byte in `0x80..=0xFF` to the corresponding [[character]] in `0x00..=0x7F` with an unspecified modifier `mod` applied
>    > **note** any discernible modifier can be used, including font weight, font style, font family, font color, background color, and so on
