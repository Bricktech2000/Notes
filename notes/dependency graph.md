# Dependency Graph

--- Wikipedia

**see** [[graph]]

**definition** a _dependency graph_ is a (directed) [[graph]] whose edges represent some notion of dependency --- me

the [[relation#transitive closure]] of a [[dependency graph]] gives a [[relation]] that encodes transitive dependencies

an evaluation order may be found using a _topological sort_, which exists if and only if the [[dependency graph]] contains no directed cycles

**applications**

- build scripts like `make`
- dead code elimimation in compilers
- spreadsheet calculators
