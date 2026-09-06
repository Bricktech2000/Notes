# Unicode

_a text encoding standard_

**see** [[ascii]], [[utf-8]], [[code page]]

**definitions** --- [[../references/glossary of unicode terms.html]] --- <https://www.unicode.org/glossary/>

- Code Point --- _Any value in the Unicode codespace; that is, the range of integers from 0x0 to 0x10FFFF. Not all code points are assigned to encoded characters. [...]_
- Unicode Scalar Value --- _Any Unicode code point except high-surrogate and low-surrogate code points. In other words, the ranges of integers 0x0 to 0xD7FF and 0xE000 to 0x10FFFF inclusive._
- Code Unit --- _The minimal bit combination that can represent a unit of encoded text for processing or interchange. The Unicode Standard uses 8-bit code units in the UTF-8 encoding form, 16-bit code units in the UTF-16 encoding form, and 32-bit code units in the UTF-32 encoding form._
- Well-Formed Code Unit Sequence --- _A code unit sequence that follows the specification of a Unicode encoding form._
- Ill-Formed Code Unit Sequence --- _A code unit sequence that does not follow the specification of a Unicode encoding form._
- Basic Multilingual Plane --- _Plane 0, abbreviated as BMP._
- BMP Character --- _A Unicode encoded character having a BMP code point._
- BMP Code Point --- _A Unicode code point between U+0000 and U+FFFF._
- Supplementary Planes --- _Planes 1 through 16, consisting of the supplementary code points._
- Supplementary Character --- _A Unicode encoded character having a supplementary code point._
- Supplementary Code Point --- _A Unicode code point between U+10000 and U+10FFFF._
- High-Surrogate Code Point --- _A Unicode code point in the range U+D800 to U+DBFF._
- High-Surrogate Code Unit --- _A 16-bit code unit in the range 0xD800 to 0xDBFF, used in UTF-16 as the leading code unit of a surrogate pair._
- Low-Surrogate Code Point --- _A Unicode code point in the range U+DC00 to U+DFFF._
- Low-Surrogate Code Unit --- _A 16-bit code unit in the range 0xDC00 to 0xDFFF, used in UTF-16 as the trailing code unit of a surrogate pair._
- Surrogate Code Point --- _A Unicode code point in the range U+D800..U+DFFF. Reserved for use by UTF-16, where a pair of surrogate code units (a high surrogate followed by a low surrogate) "stand in" for a supplementary code point._
- Surrogate Code Unit --- _This is a cover term for either a high-surrogate code unit or a low-surrogate code unit._
- Surrogate Pair --- _A representation for a single abstract character that consists of a sequence of two 16-bit code units, where the first value of the pair is a high-surrogate code unit, and the second is a low-surrogate code unit._
