# JSON

_a simple data interchange format_

**see** [[yaml]]

> **resource** RFC 8259, _The JavaScript Object Notation (JSON) Data Interchange Format_ --- <https://www.rfc-editor.org/rfc/rfc8259.html>

> **resource** _Parsing JSON is a Minefield_ by Nicolas Seriot, on the subtleties of parsing [[json]] --- [[Parsing JSON is a Minefield.html]] --- <https://seriot.ch/projects/parsing_json.html>

> **resource** _jsonw_, my tiny RFC 8259-compliant, allocation-free [[json]] parser for [[c]] --- <https://github.com/Bricktech2000/JSONW>

[[json]] is **not** a [[set#subset]] of [[javascript]] because the [[unicode]] [[character]]s `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` can appear in [[json]] [[string]] literals but not in [[javascript]] [[string]] literals --- <https://seriot.ch/projects/parsing_json.html>
