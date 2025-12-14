# UTF-8

_a brilliant and beautiful hack_

--- <https://youtu.be/_mZBa3sqTrI?t=2407>

--- <https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/>

> **resource** RFC 3629, _UTF-8, a transformation format of ISO 10646_ --- <https://www.rfc-editor.org/rfc/rfc3629.html>

> **resource** _UTF-8 history_ email chain, a trip to the past --- [[utf-8-history.txt]] --- <https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt>

**properties**

[[utf-8]] is a [[set#superset]] of [[ascii]]: every valid 7-bit [[ascii]] byte is a valid [[utf-8]] one-byte sequence. furthermore, no 7-bit [[ascii]] bytes appear within [[utf-8]] multi-byte sequences, and so programs expecting [[ascii]] sentinels such as the `\0` terminator and the `/` path separator do not misbehave when processing [[utf-8]]. for other nice properties of [[utf-8]], see RFC 3629, $1 'Introduction' <https://www.rfc-editor.org/rfc/rfc3629.html#section-1>

**representation**

| encoding                                      | bits | codepoints             | description                  |
| --------------------------------------------- | ---- | ---------------------- | ---------------------------- |
| `0b0yyyzzzz`                                  | 7    | `U+0000`--`U+007F`     | one-byte encoding sequence   |
| `0b110xxxyy 0b10yyzzzz`                       | 11   | `U+0080`--`U+07FF`     | two-byte encoding sequence   |
| `0b1110wwww 0b10xxxxyy 0b10yyzzzz`            | 16   | `U+0800`--`U+FFFF`     | three-byte encoding sequence |
| `0b11110uvv 0b10vvwwww 0b10xxxxyy 0b10yyzzzz` | 21   | `U+100000`--`U+10FFFF` | four-byte encoding sequence  |
