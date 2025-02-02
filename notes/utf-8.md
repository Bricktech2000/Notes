# UTF-8

_a brilliant and beautiful hack_

--- <https://youtu.be/_mZBa3sqTrI?t=2407>

--- <https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/>

> **resource** RFC 3629, _UTF-8, a transformation format of ISO 10646_ --- <https://www.rfc-editor.org/rfc/rfc3629.html>

> **resource** _UTF-8 history_ email chain, a trip to the past --- [[utf-8-history.txt]] --- <https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt>

**properties**

[[utf-8]] is a [[set#superset]] of [[ascii]]; every valid 7-bit [[ascii]] [[string]] is a valid [[utf-8]] [[string]]. furthermore, no 7-bit [[ascii]] bytes appear within [[utf-8]] multi-byte sequences, and thus programs expecting [[ascii]] sentinels such as the `\0` terminator and the `/` path separator do not misbehave when processing [[utf-8]]. for other nice properties of [[utf-8]], see RFC 3629, $1 'Introduction' <https://www.rfc-editor.org/rfc/rfc3629.html#section-1>

**representation**

| encoding                                      | bits | description                  |
| --------------------------------------------- | ---- | ---------------------------- |
| `0b0vvvvvvv`                                  | 7    | one-byte encoding sequence   |
| `0b110vvvvv 0b10vvvvvv`                       | 11   | two-byte encoding sequence   |
| `0b1110vvvv 0b10vvvvvv 0b10vvvvvv`            | 16   | three-byte encoding sequence |
| `0b11110vvv 0b10vvvvvv 0b10vvvvvv 0b10vvvvvv` | 21   | four-byte encoding sequence  |
