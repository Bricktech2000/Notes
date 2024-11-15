# Dynamic Programming

--- <https://youtu.be/6z4ePR7YYa8>

--- <https://en.wikipedia.org/wiki/Dynamic_programming>

**see** [[divide and conquer]]

**definition** _dynamic programming_ is a method for efficiently solving through [[recursion]] problems with _optimal substructure_ and _overlapping subproblems_

**definition** a problem is said to have an _optimal substructure_ if an optimal solution can be constructed from optimal solutions of its subproblems

**definition** a problem is said to have _overlapping subproblems_ if it can be broken down into subproblems which are reused several times

> **example**
>
> ```python
> # naive solution that recomputes the same subproblems several times
>
> def fib(n):
>   return n if n <= 1 else fib(n-1) + fib(n-2)
> ```
>
> ```python
> # dynamic programming solution that memoizes the subproblems
>
> from functools import lru_cache
>
> @lru_cache(maxsize=None)
> def fib(n):
>   return n if n <= 1 else fib(n-1) + fib(n-2)
> ```
