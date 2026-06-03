# Python

_a slow scripting language with batteries included_

#stub

[[python]]'s _comparison operators_ are `<`, `>`, `==`, `<=`, `>=`, `!=`, `is`, `is not`, `in`, `not in` --- <https://docs.python.org/3/reference/expressions.html#comparisons>. all comparison operators can form _chained comparisons_, so things can get quirky: --- <https://youtu.be/G2yPbg2fgQY?t=2285>

```python
False == False # True
False in [False] # True
False == False in [False] # True?!
```
