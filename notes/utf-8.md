# UTF-8

_a beautiful and brilliant hack_

--- <https://youtu.be/_mZBa3sqTrI?t=2407>

> **resource** RFC 3629, _UTF-8, a transformation format of ISO 10646_ --- <https://www.rfc-editor.org/rfc/rfc3629.html>

> **resource** _UTF-8 history_ email chain, a trip to the past --- [[../references/utf-8-history.txt]] --- <https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt>

> **resource** _The WTF-8 Encoding_, a [[set#superset]] of UTF-8 that can also encode unpaired surrogates --- [[../references/The WTF-8 encoding.html]] --- <https://wtf-8.codeberg.page/#unicode-scalar-value>

**properties**

[[utf-8]] is a [[set#superset]] of [[ascii]]: 7-bit [[ascii]] is encoded to [[utf-8]] as itself. furthermore, no 7-bit [[ascii]] bytes appear within [[utf-8]] multi-byte sequences, and so programs expecting [[ascii]] sentinels such as `\0` terminators and `/` path separators do not misbehave when processing [[utf-8]]. for other nice properties of [[utf-8]], see RFC 3629, $1 'Introduction' <https://www.rfc-editor.org/rfc/rfc3629.html#section-1>

**representation**

| encoding                                      | bits | code points            | description                  |
| --------------------------------------------- | ---- | ---------------------- | ---------------------------- |
| `0b0yyyzzzz`                                  | 7    | `U+0000`--`U+007F`     | one-byte encoding sequence   |
| `0b110xxxyy 0b10yyzzzz`                       | 11   | `U+0080`--`U+07FF`     | two-byte encoding sequence   |
| `0b1110wwww 0b10xxxxyy 0b10yyzzzz`            | 16   | `U+0800`--`U+FFFF`     | three-byte encoding sequence |
| `0b11110uvv 0b10vvwwww 0b10xxxxyy 0b10yyzzzz` | 21   | `U+100000`--`U+10FFFF` | four-byte encoding sequence  |
