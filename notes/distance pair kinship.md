# Distance Pair Kinship

**see** [[math notation]]

_kinship terminology_ is unintuitive at best; see <https://www.tfcg.ca/family-relationship-chart> and <https://en.wikipedia.org/wiki/Kinship_terminology>. the [[ordered pair]] of [[distance]]s from a common ancestor to two relatives is sufficient to describe the kinship between them. this is the basis of [[distance pair kinship]]

> **example** _representation of an uncle_
>
> ```
>     grandparent
>         / \
>        /   \
>    parent  uncle
>       |
>       |
>     SELF
> ```
>
> in this case, _grandparent_ is the common ancestor, which is a [[distance]] of **`2`** from _SELF_ and a [[distance]] of **`1`** from _uncle_. therefore, _SELF_'s _uncle_ would be referred to as their **`{2, 1}`**

> **examples** _useful equivalences_
>
> - **`{0, 0}`** is one's **significant other**
> - **`{1, 0}`** is one's parent
> - **`{2, 0}`** is one's grandparent
> - **`{3, 0}`** is one's great-grandparent
> - **`{0, 1}`** is one's child
> - **`{1, 1}`** is one's **sibling**
> - **`{2, 1}`** is one's uncle
> - **`{3, 1}`** is one's great-uncle
> - **`{0, 2}`** is one's grandchild
> - **`{1, 2}`** is one's nephew or niece
> - **`{2, 2}`** is one's **cousin**
> - **`{3, 2}`** is one's first cousin once removed
> - **`{0, 3}`** is one's great-grandchild
> - **`{1, 3}`** is one's great-nephew or niece
> - **`{2, 3}`** is one's first cousin once removed
> - **`{3, 3}`** is one's **second cousin**

**properties**

let **`K`** represent kinship according to [[distance pair kinship]]. then,

- **`=K`** indicates that the relatives belong to the same generation
- **`--2[:K]`** is the amount of DNA the relatives share
- the greater **`:K`**, the "further away" the relatives are
- the greater **`{^^.__} K`**, the greater the generation gap between the relatives

**tradeoffs**

[[distance pair kinship]] has a high [[switching cost]]

[[distance pair kinship]] makes reasoning about kinship more intuitive
