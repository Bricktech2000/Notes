# Depth-First Search

**see** [[stack]], [[set]]

**representation**

```python
def depth_first_search(start):
  stack = [start]
  visited = set()

  while stack:
    node = stack.pop(0)

    for neighbor in node.neighbors:
      if neighbor not in visited:
        stack.push(neighbor)
        visited.add(neighbor)
        yield neighbor
```
