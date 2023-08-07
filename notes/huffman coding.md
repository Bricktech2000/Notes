# Huffman Coding

**definition** _huffman coding_ is a lossless [[data compression]] [[algorithm]] that uses variable-length codes to represent data, where more frequently used symbols are assigned shorter codes

> **procedure** _huffman coding_ given a huffman [[tree]] and a [[list]] of symbols, for every symbol, encode it as the path from the root to the symbol, where taking a left branch corresponds to a `0` and taking a right branch corresponds to a `1`

> **procedure** _huffman decoding_ given a huffman [[tree]] and a [[binary]] string, starting from the root, for every `0` take the left branch and for every `1` take the right branch, until a leaf is reached, which corresponds to a decoded symbol

> **procedure** _huffman tree construction_
>
> ```python
> def huffman_tree(probs, symbols):
>   trees = zip(probs, symbols)
>   while len(trees) > 1:
>     trees.sort(reverse=True) # by probability
>     probs, roots = zip(trees.pop(), trees.pop())
>     trees.append((sum(probs), (roots)))
>   prob, root = trees[0]
>   assert prob == 1.0
>   return root
> ```

**representation** _sample huffman tree_

![[Pasted image 20230628214746.png]]

&mdash; Wikipedia
