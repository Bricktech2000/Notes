# JSON

_a simple data interchange format_

**see** [[yaml]]

> **resource** RFC 8259, _The JavaScript Object Notation (JSON) Data Interchange Format_ &mdash; <https://www.rfc-editor.org/rfc/rfc8259.html>

> **resource** _jsmn_, a 300-SLOC, allocation-free [[json]] parser in [[c]] &mdash; <https://github.com/zserge/jsmn/blob/master/jsmn.h>

the design of JSMN is neat. [[parser]] output is an [[array]] of possibly overlapping [[string]] slices "tokens" pointing into the source [[json]] [[string]]. `[ ... ]` "array" and `{ ... }` "object" tokens also hold as metadata the number of children they have, which is sufficient to rebuild the entire [[json]] [[tree]] hierarchy
