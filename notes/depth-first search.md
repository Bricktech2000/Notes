# Depth-First Search

**see** [[stack]], [[set]], [[graph]]

**representation**

```python
def depth_first_search(start):
  stack = [start]
  visited = set()

  while stack:
    node = stack.pop()

    for neighbor in node.neighbors:
      if neighbor not in visited:
        stack.append(neighbor)
        visited.add(neighbor)
        yield neighbor
```
