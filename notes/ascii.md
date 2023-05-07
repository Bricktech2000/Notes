# ASCII

**see** [[utf-8]], [[math notation]]

[[ascii]] is a widely used 7-bit character encoding standard

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

| encoding                                | character       | description               |
| --------------------------------------- | --------------- | ------------------------- |
| `0x00` &bull; `0b00000000` &bull; `0`   | NUL             | Null                      |
| `0x01` &bull; `0b00000001` &bull; `1`   | SOH             | Start of Heading          |
| `0x02` &bull; `0b00000010` &bull; `2`   | STX             | Start of Text             |
| `0x03` &bull; `0b00000011` &bull; `3`   | ETX             | End of Text               |
| `0x04` &bull; `0b00000100` &bull; `4`   | EOT             | End of Transmission       |
| `0x05` &bull; `0b00000101` &bull; `5`   | ENQ             | Enquiry                   |
| `0x06` &bull; `0b00000110` &bull; `6`   | ACK             | Acknowledgment            |
| `0x07` &bull; `0b00000111` &bull; `7`   | BEL             | Bell                      |
| `0x08` &bull; `0b00001000` &bull; `8`   | BS              | Backspace                 |
| `0x09` &bull; `0b00001001` &bull; `9`   | HT              | Horizontal Tab            |
| `0x0A` &bull; `0b00001010` &bull; `10`  | LF              | Line Feed                 |
| `0x0B` &bull; `0b00001011` &bull; `11`  | VT              | Vertical Tab              |
| `0x0C` &bull; `0b00001100` &bull; `12`  | FF              | Form Feed                 |
| `0x0D` &bull; `0b00001101` &bull; `13`  | CR              | Carriage Return           |
| `0x0E` &bull; `0b00001110` &bull; `14`  | SO              | Shift Out                 |
| `0x0F` &bull; `0b00001111` &bull; `15`  | SI              | Shift In                  |
| `0x10` &bull; `0b00010000` &bull; `16`  | DLE             | Data Link Escape          |
| `0x11` &bull; `0b00010001` &bull; `17`  | DC1             | Device Control 1          |
| `0x12` &bull; `0b00010010` &bull; `18`  | DC2             | Device Control 2          |
| `0x13` &bull; `0b00010011` &bull; `19`  | DC3             | Device Control 3          |
| `0x14` &bull; `0b00010100` &bull; `20`  | DC4             | Device Control 4          |
| `0x15` &bull; `0b00010101` &bull; `21`  | NAK             | Negative Acknowledgement  |
| `0x16` &bull; `0b00010110` &bull; `22`  | SYN             | Synchronous Idle          |
| `0x17` &bull; `0b00010111` &bull; `23`  | ETB             | End of Transmission Block |
| `0x18` &bull; `0b00011000` &bull; `24`  | CAN             | Cancel                    |
| `0x19` &bull; `0b00011001` &bull; `25`  | EM              | End of Medium             |
| `0x1A` &bull; `0b00011010` &bull; `26`  | SUB             | Substitute                |
| `0x1B` &bull; `0b00011011` &bull; `27`  | ESC             | Escape                    |
| `0x1C` &bull; `0b00011100` &bull; `28`  | FS              | File Separator            |
| `0x1D` &bull; `0b00011101` &bull; `29`  | GS              | Group Separator           |
| `0x1E` &bull; `0b00011110` &bull; `30`  | RS              | Record Separator          |
| `0x1F` &bull; `0b00011111` &bull; `31`  | US              | Unit Separator            |
| `0x20` &bull; `0b00100000` &bull; `32`  | **`'' ''`**     | Space                     |
| `0x21` &bull; `0b00100001` &bull; `33`  | **`''!''`**     | Exclamation Mark          |
| `0x22` &bull; `0b00100010` &bull; `34`  | **`''"''`**     | Quotation Mark            |
| `0x23` &bull; `0b00100011` &bull; `35`  | **`''#''`**     | Number Sign               |
| `0x24` &bull; `0b00100100` &bull; `36`  | **`''$''`**     | Dollar Sign               |
| `0x25` &bull; `0b00100101` &bull; `37`  | **`''%''`**     | Percent Sign              |
| `0x26` &bull; `0b00100110` &bull; `38`  | **`''&''`**     | Ampersand                 |
| `0x27` &bull; `0b00100111` &bull; `39`  | **`''\'''`**    | Apostrophe                |
| `0x28` &bull; `0b00101000` &bull; `40`  | **`''(''`**     | Left Parenthesis          |
| `0x29` &bull; `0b00101001` &bull; `41`  | **`'')''`**     | Right Parenthesis         |
| `0x2A` &bull; `0b00101010` &bull; `42`  | **`''*''`**     | Asterisk                  |
| `0x2B` &bull; `0b00101011` &bull; `43`  | **`''+''`**     | Plus Sign                 |
| `0x2C` &bull; `0b00101100` &bull; `44`  | **`'',''`**     | Comma                     |
| `0x2D` &bull; `0b00101101` &bull; `45`  | **`''-''`**     | Hyphen-Minus              |
| `0x2E` &bull; `0b00101110` &bull; `46`  | **`''.''`**     | Full Stop                 |
| `0x2F` &bull; `0b00101111` &bull; `47`  | **`''/''`**     | Solidus                   |
| `0x30` &bull; `0b00110000` &bull; `48`  | **`''0''`**     | Digit Zero                |
| `0x31` &bull; `0b00110001` &bull; `49`  | **`''1''`**     | Digit One                 |
| `0x32` &bull; `0b00110010` &bull; `50`  | **`''2''`**     | Digit Two                 |
| `0x33` &bull; `0b00110011` &bull; `51`  | **`''3''`**     | Digit Three               |
| `0x34` &bull; `0b00110100` &bull; `52`  | **`''4''`**     | Digit Four                |
| `0x35` &bull; `0b00110101` &bull; `53`  | **`''5''`**     | Digit Five                |
| `0x36` &bull; `0b00110110` &bull; `54`  | **`''6''`**     | Digit Six                 |
| `0x37` &bull; `0b00110111` &bull; `55`  | **`''7''`**     | Digit Seven               |
| `0x38` &bull; `0b00111000` &bull; `56`  | **`''8''`**     | Digit Eight               |
| `0x39` &bull; `0b00111001` &bull; `57`  | **`''9''`**     | Digit Nine                |
| `0x3A` &bull; `0b00111010` &bull; `58`  | **`'':''`**     | Colon                     |
| `0x3B` &bull; `0b00111011` &bull; `59`  | **`'';''`**     | Semicolon                 |
| `0x3C` &bull; `0b00111100` &bull; `60`  | **`''<''`**     | Less-Than Sign            |
| `0x3D` &bull; `0b00111101` &bull; `61`  | **`''=''`**     | Equals Sign               |
| `0x3E` &bull; `0b00111110` &bull; `62`  | **`''>''`**     | Greater-Than Sign         |
| `0x3F` &bull; `0b00111111` &bull; `63`  | **`''?''`**     | Question Mark             |
| `0x40` &bull; `0b01000000` &bull; `64`  | **`''@''`**     | Commercial At             |
| `0x41` &bull; `0b01000001` &bull; `65`  | **`''A''`**     | Latin Capital Letter A    |
| `0x42` &bull; `0b01000010` &bull; `66`  | **`''B''`**     | Latin Capital Letter B    |
| `0x43` &bull; `0b01000011` &bull; `67`  | **`''C''`**     | Latin Capital Letter C    |
| `0x44` &bull; `0b01000100` &bull; `68`  | **`''D''`**     | Latin Capital Letter D    |
| `0x45` &bull; `0b01000101` &bull; `69`  | **`''E''`**     | Latin Capital Letter E    |
| `0x46` &bull; `0b01000110` &bull; `70`  | **`''F''`**     | Latin Capital Letter F    |
| `0x47` &bull; `0b01000111` &bull; `71`  | **`''G''`**     | Latin Capital Letter G    |
| `0x48` &bull; `0b01001000` &bull; `72`  | **`''H''`**     | Latin Capital Letter H    |
| `0x49` &bull; `0b01001001` &bull; `73`  | **`''I''`**     | Latin Capital Letter I    |
| `0x4A` &bull; `0b01001010` &bull; `74`  | **`''J''`**     | Latin Capital Letter J    |
| `0x4B` &bull; `0b01001011` &bull; `75`  | **`''K''`**     | Latin Capital Letter K    |
| `0x4C` &bull; `0b01001100` &bull; `76`  | **`''L''`**     | Latin Capital Letter L    |
| `0x4D` &bull; `0b01001101` &bull; `77`  | **`''M''`**     | Latin Capital Letter M    |
| `0x4E` &bull; `0b01001110` &bull; `78`  | **`''N''`**     | Latin Capital Letter N    |
| `0x4F` &bull; `0b01001111` &bull; `79`  | **`''O''`**     | Latin Capital Letter O    |
| `0x50` &bull; `0b01010000` &bull; `80`  | **`''P''`**     | Latin Capital Letter P    |
| `0x51` &bull; `0b01010001` &bull; `81`  | **`''Q''`**     | Latin Capital Letter Q    |
| `0x52` &bull; `0b01010010` &bull; `82`  | **`''R''`**     | Latin Capital Letter R    |
| `0x53` &bull; `0b01010011` &bull; `83`  | **`''S''`**     | Latin Capital Letter S    |
| `0x54` &bull; `0b01010100` &bull; `84`  | **`''T''`**     | Latin Capital Letter T    |
| `0x55` &bull; `0b01010101` &bull; `85`  | **`''U''`**     | Latin Capital Letter U    |
| `0x56` &bull; `0b01010110` &bull; `86`  | **`''V''`**     | Latin Capital Letter V    |
| `0x57` &bull; `0b01010111` &bull; `87`  | **`''W''`**     | Latin Capital Letter W    |
| `0x58` &bull; `0b01011000` &bull; `88`  | **`''X''`**     | Latin Capital Letter X    |
| `0x59` &bull; `0b01011001` &bull; `89`  | **`''Y''`**     | Latin Capital Letter Y    |
| `0x5A` &bull; `0b01011010` &bull; `90`  | **`''Z''`**     | Latin Capital Letter Z    |
| `0x5B` &bull; `0b01011011` &bull; `91`  | **`''[''`**     | Left Square Bracket       |
| `0x5C` &bull; `0b01011100` &bull; `92`  | **`''\\''`**    | Reverse Solidus           |
| `0x5D` &bull; `0b01011101` &bull; `93`  | **`'']''`**     | Right Square Bracket      |
| `0x5E` &bull; `0b01011110` &bull; `94`  | **`''^''`**     | Circumflex Accent         |
| `0x5F` &bull; `0b01011111` &bull; `95`  | **`''_''`**     | Low Line                  |
| `0x60` &bull; `0b01100000` &bull; `96`  | **`` ''`'' ``** | Grave Accent              |
| `0x61` &bull; `0b01100001` &bull; `97`  | **`''a''`**     | Latin Small Letter A      |
| `0x62` &bull; `0b01100010` &bull; `98`  | **`''b''`**     | Latin Small Letter B      |
| `0x63` &bull; `0b01100011` &bull; `99`  | **`''c''`**     | Latin Small Letter C      |
| `0x64` &bull; `0b01100100` &bull; `100` | **`''d''`**     | Latin Small Letter D      |
| `0x65` &bull; `0b01100101` &bull; `101` | **`''e''`**     | Latin Small Letter E      |
| `0x66` &bull; `0b01100110` &bull; `102` | **`''f''`**     | Latin Small Letter F      |
| `0x67` &bull; `0b01100111` &bull; `103` | **`''g''`**     | Latin Small Letter G      |
| `0x68` &bull; `0b01101000` &bull; `104` | **`''h''`**     | Latin Small Letter H      |
| `0x69` &bull; `0b01101001` &bull; `105` | **`''i''`**     | Latin Small Letter I      |
| `0x6A` &bull; `0b01101010` &bull; `106` | **`''j''`**     | Latin Small Letter J      |
| `0x6B` &bull; `0b01101011` &bull; `107` | **`''k''`**     | Latin Small Letter K      |
| `0x6C` &bull; `0b01101100` &bull; `108` | **`''l''`**     | Latin Small Letter L      |
| `0x6D` &bull; `0b01101101` &bull; `109` | **`''m''`**     | Latin Small Letter M      |
| `0x6E` &bull; `0b01101110` &bull; `110` | **`''n''`**     | Latin Small Letter N      |
| `0x6F` &bull; `0b01101111` &bull; `111` | **`''o''`**     | Latin Small Letter O      |
| `0x70` &bull; `0b01110000` &bull; `112` | **`''p''`**     | Latin Small Letter P      |
| `0x71` &bull; `0b01110001` &bull; `113` | **`''q''`**     | Latin Small Letter Q      |
| `0x72` &bull; `0b01110010` &bull; `114` | **`''r''`**     | Latin Small Letter R      |
| `0x73` &bull; `0b01110011` &bull; `115` | **`''s''`**     | Latin Small Letter S      |
| `0x74` &bull; `0b01110100` &bull; `116` | **`''t''`**     | Latin Small Letter T      |
| `0x75` &bull; `0b01110101` &bull; `117` | **`''u''`**     | Latin Small Letter U      |
| `0x76` &bull; `0b01110110` &bull; `118` | **`''v''`**     | Latin Small Letter V      |
| `0x77` &bull; `0b01110111` &bull; `119` | **`''w''`**     | Latin Small Letter W      |
| `0x78` &bull; `0b01111000` &bull; `120` | **`''x''`**     | Latin Small Letter X      |
| `0x79` &bull; `0b01111001` &bull; `121` | **`''y''`**     | Latin Small Letter Y      |
| `0x7A` &bull; `0b01111010` &bull; `122` | **`''z''`**     | Latin Small Letter Z      |
| `0x7B` &bull; `0b01111011` &bull; `123` | **`''{''`**     | Left Curly Bracket        |
| `0x7C` &bull; `0b01111100` &bull; `124` | **`''\|''`**    | Vertical Line             |
| `0x7D` &bull; `0b01111101` &bull; `125` | **`''}''`**     | Right Curly Bracket       |
| `0x7E` &bull; `0b01111110` &bull; `126` | **`''~''`**     | Tilde                     |
| `0x7F` &bull; `0b01111111` &bull; `127` | DEL             | Delete                    |
