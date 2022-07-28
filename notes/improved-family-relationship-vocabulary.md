# Improved Family Relationship Vocabulary

who thought this would be an intuitive way to describe family relationships? let's fix that.

![[20220519150236.png]]

## vocabulary

all that is needed to describe the relationship between two people in a family is the two [[distance]]s between them and a common ancestor. below is an example of the representation of an _uncle_.

```
    grandparent
        / \
       /   \
   parent  uncle
      |
      |
    SELF

```

in this case, _grandparent_ is the common ancestor, which is a [[distance]] of `2` from _SELF_ and a [[distance]] of `1` from _uncle_. therefore, _SELF_'s _uncle_ would be called their `2-1`.

below are some useful equivalences.

- `0-0` is one's **significant other**
- `1-0` is one's parent
- `2-0` is one's grandparent
- `3-0` is one's great-grandparent
- `0-1` is one's child
- `1-1` is one's **sibling**
- `2-1` is one's uncle
- `3-1` is one's great-uncle
- `0-2` is one's grandchild
- `1-2` is one's nephew or niece
- `2-2` is one's **cousin**
- `3-2` is one's first cousin once removed
- `0-3` is one's great-grandchild
- `1-3` is one's great-nephew or niece
- `2-3` is one's first cousin once removed
- `3-3` is one's **second cousin**

## benefits

see [[math-notation]]

let $m$ and $n$ be the two numbers representing the [[distance]] between two people in a family.

- $m = n$ indicates both people are in the same generation
- $-2[m : n]$ is the amount of DNA two people have in common (excluding significant others)
- the larger $m : n$, the further away the people are
- the larger $|m \cdot n|$, the greater age difference between the people

## limits

- dumb vocabulary already exists to describe the relationship between two people in a family, so getting the general public on board is not an easy task
