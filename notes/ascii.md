# ASCII

**see** [[utf-8]], [[math notation]]

> **resource** ANSI X3.4-1986, FIPS PUB 1-2, _7-Bit American National Standard Code for Information Interchange_ --- <https://www.unicode.org/L2/L2006/06388-review-incits4.pdf>

> **resource** _Plain Text_ talk (alias PIKE MATCHBOX) by Dylan Beattie --- <https://youtu.be/_mZBa3sqTrI>

[[ascii]] is a widely used 7-bit [[character]] encoding standard

a non-standard 8th bit is sometimes used for:

- [[utf-8]] encoding
- [[code page]] extensions
- parity checks and [[error correction]]

**properties**

lowercase and uppercase letters are offset by `0x20` or `0b00100000` or `' '`

`c & 0b11011111` where `c` is a lower[[case]] letter will return its upper[[case]] equivalent

`c | 0b00100000` where `c` is an upper[[case]] letter will return its lower[[case]] equivalent

`c & 0b00111111` where `c` is a letter will return its position in the alphabet, starting at **`1`**

`c & 0b00001111` where `c` is digit will return its value

`c & 0b11100000 != 0` will return whether `c` is a control character

for other nice properties of [[ascii]], see ANSI X3.4-1986, Appendices A 'Design Considerations for the Coded Character Set' and C 'Original Criteria'

**representation** --- ANSI X3.4-1986

| [[hexadecimal]] - [[binary]] | abbr. or glyph | `category` NAMES (ISO 646-1983 NAME) [DIACRITICAL USE] |
| ---------------------------- | -------------- | ------------------------------------------------------ |
| `0x00` - `0b00000000`        | NUL            | `O` NULL                                               |
| `0x01` - `0b00000001`        | SOH            | `T` START OF HEADING                                   |
| `0x02` - `0b00000010`        | STX            | `T` START OF TEXT                                      |
| `0x03` - `0b00000011`        | ETX            | `T` END OF TEXT                                        |
| `0x04` - `0b00000100`        | EOT            | `T` END OF TRANSMISSION                                |
| `0x05` - `0b00000101`        | ENQ            | `T` ENQUIRY                                            |
| `0x06` - `0b00000110`        | ACK            | `T` ACKNOWLEDGE                                        |
| `0x07` - `0b00000111`        | BEL            | `O` BELL                                               |
| `0x08` - `0b00001000`        | BS             | `F` BACKSPACE                                          |
| `0x09` - `0b00001001`        | HT             | `F` HORIZONTAL TABULATION                              |
| `0x0A` - `0b00001010`        | LF             | `F` LINE FEED                                          |
| `0x0B` - `0b00001011`        | VT             | `F` VERTICAL TABULATION                                |
| `0x0C` - `0b00001100`        | FF             | `F` FORM FEED                                          |
| `0x0D` - `0b00001101`        | CR             | `F` CARRIAGE RETURN                                    |
| `0x0E` - `0b00001110`        | SO             | `X` SHIFT-OUT                                          |
| `0x0F` - `0b00001111`        | SI             | `X` SHIFT-IN                                           |
| `0x10` - `0b00010000`        | DLE            | `T` DATA LINK ESCAPE                                   |
| `0x11` - `0b00010001`        | DC1            | `D` DEVICE CONTROL ONE                                 |
| `0x12` - `0b00010010`        | DC2            | `D` DEVICE CONTROL TWO                                 |
| `0x13` - `0b00010011`        | DC3            | `D` DEVICE CONTROL THREE                               |
| `0x14` - `0b00010100`        | DC4            | `D` DEVICE CONTROL FOUR                                |
| `0x15` - `0b00010101`        | NAK            | `T` NEGATIVE ACKNOWLEDGE                               |
| `0x16` - `0b00010110`        | SYN            | `T` SYNCHRONOUS IDLE                                   |
| `0x17` - `0b00010111`        | ETB            | `T` END OF TRANSMISSION BLOCK                          |
| `0x18` - `0b00011000`        | CAN            | `O` CANCEL                                             |
| `0x19` - `0b00011001`        | EM             | `O` END OF MEDIUM                                      |
| `0x1A` - `0b00011010`        | SUB            | `O` SUBSTITUTE CHARACTER                               |
| `0x1B` - `0b00011011`        | ESC            | `X` ESCAPE                                             |
| `0x1C` - `0b00011100`        | FS             | `S` FILE SEPARATOR (INFORMATION SEPARATOR FOUR)        |
| `0x1D` - `0b00011101`        | GS             | `S` GROUP SEPARATOR (INFORMATION SEPARATOR THREE)      |
| `0x1E` - `0b00011110`        | RS             | `S` RECORD SEPARATOR (INFORMATION SEPARATOR TWO)       |
| `0x1F` - `0b00011111`        | US             | `S` UNIT SEPARATOR (INFORMATION SEPARATOR ONE)         |
| `0x20` - `0b00100000`        | SP / `' '`     | `F` SPACE / SPACE                                      |
| `0x21` - `0b00100001`        | `'!'`          | EXCLAMATION POINT                                      |
| `0x22` - `0b00100010`        | `'"'`          | QUOTATION MARK [DIAERESIS]                             |
| `0x23` - `0b00100011`        | `'#'`          | NUMBER SIGN                                            |
| `0x24` - `0b00100100`        | `'$'`          | DOLLAR SIGN                                            |
| `0x25` - `0b00100101`        | `'%'`          | PERCENT SIGN                                           |
| `0x26` - `0b00100110`        | `'&'`          | AMPERSAND                                              |
| `0x27` - `0b00100111`        | `'\''`         | APOSTROPHE, RIGHT SINGLE QUOTATION MARK [ACUTE ACCENT] |
| `0x28` - `0b00101000`        | `'('`          | LEFT PARENTHESIS                                       |
| `0x29` - `0b00101001`        | `')'`          | RIGHT PARENTHESIS                                      |
| `0x2A` - `0b00101010`        | `'*'`          | ASTERISK                                               |
| `0x2B` - `0b00101011`        | `'+'`          | PLUS SIGN                                              |
| `0x2C` - `0b00101100`        | `','`          | COMMA [CEDILLA]                                        |
| `0x2D` - `0b00101101`        | `'-'`          | HYPHEN, MINUS SIGN                                     |
| `0x2E` - `0b00101110`        | `'.'`          | PERIOD, DECIMAL POINT (FULL STOP)                      |
| `0x2F` - `0b00101111`        | `'/'`          | SLANT (SOLIDUS)                                        |
| `0x30` - `0b00110000`        | `'0'`          | DIGIT ZERO                                             |
| `0x31` - `0b00110001`        | `'1'`          | DIGIT ONE                                              |
| `0x32` - `0b00110010`        | `'2'`          | DIGIT TWO                                              |
| `0x33` - `0b00110011`        | `'3'`          | DIGIT THREE                                            |
| `0x34` - `0b00110100`        | `'4'`          | DIGIT FOUR                                             |
| `0x35` - `0b00110101`        | `'5'`          | DIGIT FIVE                                             |
| `0x36` - `0b00110110`        | `'6'`          | DIGIT SIX                                              |
| `0x37` - `0b00110111`        | `'7'`          | DIGIT SEVEN                                            |
| `0x38` - `0b00111000`        | `'8'`          | DIGIT EIGHT                                            |
| `0x39` - `0b00111001`        | `'9'`          | DIGIT NINE                                             |
| `0x3A` - `0b00111010`        | `':'`          | COLON                                                  |
| `0x3B` - `0b00111011`        | `';'`          | SEMICOLON                                              |
| `0x3C` - `0b00111100`        | `'<'`          | LESS-THAN SIGN                                         |
| `0x3D` - `0b00111101`        | `'='`          | EQUALS SIGN                                            |
| `0x3E` - `0b00111110`        | `'>'`          | GREATER-THAN SIGN                                      |
| `0x3F` - `0b00111111`        | `'?'`          | QUESTION MARK                                          |
| `0x40` - `0b01000000`        | `'@'`          | COMMERCIAL AT                                          |
| `0x41` - `0b01000001`        | `'A'`          | CAPITAL LETTER A                                       |
| `0x42` - `0b01000010`        | `'B'`          | CAPITAL LETTER B                                       |
| `0x43` - `0b01000011`        | `'C'`          | CAPITAL LETTER C                                       |
| `0x44` - `0b01000100`        | `'D'`          | CAPITAL LETTER D                                       |
| `0x45` - `0b01000101`        | `'E'`          | CAPITAL LETTER E                                       |
| `0x46` - `0b01000110`        | `'F'`          | CAPITAL LETTER F                                       |
| `0x47` - `0b01000111`        | `'G'`          | CAPITAL LETTER G                                       |
| `0x48` - `0b01001000`        | `'H'`          | CAPITAL LETTER H                                       |
| `0x49` - `0b01001001`        | `'I'`          | CAPITAL LETTER I                                       |
| `0x4A` - `0b01001010`        | `'J'`          | CAPITAL LETTER J                                       |
| `0x4B` - `0b01001011`        | `'K'`          | CAPITAL LETTER K                                       |
| `0x4C` - `0b01001100`        | `'L'`          | CAPITAL LETTER L                                       |
| `0x4D` - `0b01001101`        | `'M'`          | CAPITAL LETTER M                                       |
| `0x4E` - `0b01001110`        | `'N'`          | CAPITAL LETTER N                                       |
| `0x4F` - `0b01001111`        | `'O'`          | CAPITAL LETTER O                                       |
| `0x50` - `0b01010000`        | `'P'`          | CAPITAL LETTER P                                       |
| `0x51` - `0b01010001`        | `'Q'`          | CAPITAL LETTER Q                                       |
| `0x52` - `0b01010010`        | `'R'`          | CAPITAL LETTER R                                       |
| `0x53` - `0b01010011`        | `'S'`          | CAPITAL LETTER S                                       |
| `0x54` - `0b01010100`        | `'T'`          | CAPITAL LETTER T                                       |
| `0x55` - `0b01010101`        | `'U'`          | CAPITAL LETTER U                                       |
| `0x56` - `0b01010110`        | `'V'`          | CAPITAL LETTER V                                       |
| `0x57` - `0b01010111`        | `'W'`          | CAPITAL LETTER W                                       |
| `0x58` - `0b01011000`        | `'X'`          | CAPITAL LETTER X                                       |
| `0x59` - `0b01011001`        | `'Y'`          | CAPITAL LETTER Y                                       |
| `0x5A` - `0b01011010`        | `'Z'`          | CAPITAL LETTER Z                                       |
| `0x5B` - `0b01011011`        | `'['`          | LEFT BRACKET (LEFT SQUARE BRACKET)                     |
| `0x5C` - `0b01011100`        | `'\'`          | REVERSE SLANT (REVERSE SOLIDUS)                        |
| `0x5D` - `0b01011101`        | `']'`          | RIGHT BRACKET (RIGHT SQUARE BRACKET)                   |
| `0x5E` - `0b01011110`        | `'^'`          | CIRCUMFLEX ACCENT [CIRCUMFLEX]                         |
| `0x5F` - `0b01011111`        | `'_'`          | UNDERLINE (LOW LINE)                                   |
| `0x60` - `0b01100000`        | ``'`'``        | LEFT SINGLE QUOTATION MARK [GRAVE ACCENT]              |
| `0x61` - `0b01100001`        | `'a'`          | SMALL LETTER a                                         |
| `0x62` - `0b01100010`        | `'b'`          | SMALL LETTER b                                         |
| `0x63` - `0b01100011`        | `'c'`          | SMALL LETTER c                                         |
| `0x64` - `0b01100100`        | `'d'`          | SMALL LETTER d                                         |
| `0x65` - `0b01100101`        | `'e'`          | SMALL LETTER e                                         |
| `0x66` - `0b01100110`        | `'f'`          | SMALL LETTER f                                         |
| `0x67` - `0b01100111`        | `'g'`          | SMALL LETTER g                                         |
| `0x68` - `0b01101000`        | `'h'`          | SMALL LETTER h                                         |
| `0x69` - `0b01101001`        | `'i'`          | SMALL LETTER i                                         |
| `0x6A` - `0b01101010`        | `'j'`          | SMALL LETTER j                                         |
| `0x6B` - `0b01101011`        | `'k'`          | SMALL LETTER k                                         |
| `0x6C` - `0b01101100`        | `'l'`          | SMALL LETTER l                                         |
| `0x6D` - `0b01101101`        | `'m'`          | SMALL LETTER m                                         |
| `0x6E` - `0b01101110`        | `'n'`          | SMALL LETTER n                                         |
| `0x6F` - `0b01101111`        | `'o'`          | SMALL LETTER o                                         |
| `0x70` - `0b01110000`        | `'p'`          | SMALL LETTER p                                         |
| `0x71` - `0b01110001`        | `'q'`          | SMALL LETTER q                                         |
| `0x72` - `0b01110010`        | `'r'`          | SMALL LETTER r                                         |
| `0x73` - `0b01110011`        | `'s'`          | SMALL LETTER s                                         |
| `0x74` - `0b01110100`        | `'t'`          | SMALL LETTER t                                         |
| `0x75` - `0b01110101`        | `'u'`          | SMALL LETTER u                                         |
| `0x76` - `0b01110110`        | `'v'`          | SMALL LETTER v                                         |
| `0x77` - `0b01110111`        | `'w'`          | SMALL LETTER w                                         |
| `0x78` - `0b01111000`        | `'x'`          | SMALL LETTER x                                         |
| `0x79` - `0b01111001`        | `'y'`          | SMALL LETTER y                                         |
| `0x7A` - `0b01111010`        | `'z'`          | SMALL LETTER z                                         |
| `0x7B` - `0b01111011`        | `'{'`          | LEFT BRACE (LEFT CURLY BRACKET)                        |
| `0x7C` - `0b01111100`        | `'\|'`         | VERTICAL LINE                                          |
| `0x7D` - `0b01111101`        | `'}'`          | RIGHT BRACE (RIGHT CURLY BRACKET)                      |
| `0x7E` - `0b01111110`        | `'~'`          | TILDE (OVERLINE) [TILDE]                               |
| `0x7F` - `0b01111111`        | DEL            | `O` DELETE                                             |

a legend for control character categories follows. for more information, see ANSI X3.4-1986, $4.1 'Control Characters'

- `T` --- Transmission Control Characters
- `F` --- Format Effectors
- `X` --- Code Extension Control Characters
- `D` --- Device Control Characters
- `S` --- Information Separators
- `O` --- Other Control Characters

the standard does not restrict the meaning of graphic characters; their names are intented to reflect their customary meaning --- ANSI X3.4-1986, $4 'Specification of the Coded Character Set'. SPACE is both a graphic character and a control character --- ANSI X3.4-1986, $4.2 'SPACE'. the ability for BS to compose characters by overstriking is not required by the standard --- ANSI X3.4-1986, $5 'Composite Graphic Characters' and $D4.3 'Composite Characters Using BS'. for more information on the meanings of control characters, see ANSI X3.4-1986, $7 'Description of the Control Characters'
