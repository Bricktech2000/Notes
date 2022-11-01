# Breadth-First Search

**see** [[queue]], [[set]]

**representation**

```python
def breadth_first_search(start):
  queue = [start]
  visited = set()

  while queue:
    node = queue.pop(0)

    for neighbor in node.neighbors:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)
        yield neighbor
```
