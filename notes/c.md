# C

_the OG with UB_

&mdash; <https://youtu.be/A3AdN7U24iU>

**pros**

- performance (fast, very little overhead, very little resources)
- portability (compilers support many different targets)
- simplicity (language is simple, not much syntax to learn)
- stability (code doesn't break or become obsolete)

**cons**

- memory unsafety (use after free, double free, memory leaks, buffer overreads and overwrites, [[null]] pointers, data races...)

## array indexing quirk

```Cpp
#include <iostream>

int main()
{
 short a[4] = {1, 2, 3, 4};

 std::cout << a[3] << std::endl; // 4
 std::cout << 3 [a] << std::endl; // 4
 std::cout << *(a + 3) << std::endl; // 4
 std::cout << *(3 + a) << std::endl; // 4
}
```

## undefined behavior

undefined benavior is a tool for the compiler to optimize programs even further

for example, as division by zero is undefined behavior, the compiler can assume the [[variable]] `a` in an expresion such as `1 / a` will never be zero
