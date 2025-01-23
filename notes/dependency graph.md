# Dependency Graph

--- Wikipedia

**see** [[graph]]

**definition** a _dependency graph_ is a (directed) [[graph]] whose edges represent some notion of dependency --- me

the set of paths of a [[dependency graph]] form a [[preorder]] because so do the set of paths of any directed [[graph]]

the [[relation#transitive closure]] of a [[dependency graph]] gives a [[relation]] that encodes transitive dependency

an evaluation order may be found using a _topological sort_, which exists if and only if the [[dependency graph]] contains no directed cycles. in other words, if and only if the set of paths of a [[dependency graph]] forms not only a [[preorder]] but also a [[partial order]], then that [[partial order]] can be turned into a "compatible" [[total order]] (a _linear extension_ of the [[partial order]]) --- me and <https://en.wikipedia.org/wiki/Topological_sorting#Relation_to_partial_orders>. _In [[computer science]], [[algorithm]]s for finding linear extensions of [[partial order]]s (represented as the reachability orders of directed acyclic [[graph]]s) are called topological sorting._ --- <https://en.wikipedia.org/wiki/Partially_ordered_set#Linear_extension>

**applications**

- build scripts like `make`
- dead code elimimation in compilers
- spreadsheet calculators
