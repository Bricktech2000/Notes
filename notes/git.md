# Git

**see** [[math notation]], [[hash]]

> **resource** talk by Linus Torvalds on the fundamental ideas behind [[git]] &mdash; <https://youtu.be/MjIPv8a0hU8>

## Data Model

&mdash; <https://missing.csail.mit.edu/2020/version-control/>

&mdash; <https://eagain.net/articles/git-for-computer-scientists/>

&mdash; <https://youtu.be/u0VotuGzD_w?t=13m49s>

a [[git]] history is a directed acyclic [[graph]] of snapshots forming a [[persistent data structure]]. **`H a b`** means node **`a`** depends on and cannot exist without node **`b`** in history **`H`**

[[git]] refs are post-it notes stuck to nodes in the history; they are not part of the history and are therefore mutable

a [[git]] rebase creates new commits from a different parent then moves all refs to the new commits

[[git]] commits with multiple parents **`#H c |- 2`** are merge commits; [[git]] commits with no parents **`#H c = 0`** are root commits

**representation**

```rust
// `&`s are stored internally as SHA-1 hashes

struct Blob(Vec<u8>); // file contents

enum TreeOrBlob { Tree(Tree), Blob(Blob) }
struct Tree(HashMap<Path, &TreeOrBlob>); // directory contents

struct Commit {
  parents: Vec<&Commit>,
  message: String,
  tree: &Tree,
}

enum Object {
  Blob(Blob),
  Tree(Tree),
  Commit(Commit),
}

struct Repo {
  objects: HashSet<&Object>,
  refs: HashMap<String, &Commit>,
}
```
