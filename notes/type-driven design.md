# Type-Driven Design

**see** [[hungarian notation]], [[comment]], [[type#algebraic data type]], [[type#refinement type]], [[function#total function]]

> **resource** _parse, don’t validate_ by Alexis King (_validators_ just return whether some data is valid whereas _parsers_ return [[type]]-level knowledge that the data is valid) --- <https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/>

> **resource** _Type-Driven API Design in Rust_ by Will Crichton, leveraging [[rust]] [[trait]]s to design a great progress bar API using the "type state" pattern --- <https://youtu.be/bnnacleqg6k>

> **resource** _Domain Modeling Made Functional_ by Scott Wlaschin, and why [[type#algebraic data type]]s matter --- <https://youtu.be/2JB1_e5wZmU>

> **resource** _Moving IO to the edges of your app_ by Scott Wlaschin, including why `void f(void);` [[function]]s bad --- <https://youtu.be/P1vES9AgfC4>

the core ideas of [[type-driven design]] are (1) write [[function#total function]]s, and (2) move validation outward. in practice, this means:

- establish invariants early using [[type#refinement type]]s. from there the [[type system]] enforces your invariants, so there's no need to defensively check them in your core logic --- <https://youtu.be/2JB1_e5wZmU?t=2102>
- _make invalid states unrepresentable_ --- Yaron Minsky. _avoid denormalized representations of data, especially if it's mutable. duplicating the same data in multiple places introduces a trivially representable illegal state: the places getting out of sync_ --- Alexis King
- use `newtype`s extensively and avoid "primitive obsession": URLs and email addresses are not `String`s, and custommer IDs are not `int`s. you can't send an email to a URL and you can't take the square root of a customer ID. --- <https://youtu.be/2JB1_e5wZmU?t=1838>

with [[type-driven design]], band-aids like [[hungarian notation]] (prepending onto [[variable]] names information not available in their [[type]]) and _negative-space programming_ (placing assertions throughout your code so it fails fast and early) become unnecessary

here's a fun one, _shotgun parsing_:

> _Shotgun parsing_ is a programming antipattern whereby parsing and input-validating code is mixed with and spread across processing code---throwing a cloud of checks at the input, and hoping, without any systematic justification, that one or another would catch all the "bad" cases. --- _The Seven Turrets of Babel: A Taxonomy of LangSec Errors and How to Expunge Them_ --- <http://langsec.org/papers/langsec-cwes-secdev2016.pdf>
