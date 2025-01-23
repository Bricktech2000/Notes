# Brainfuck

> **resource** [[brainfuck]] interpreter, transpiler targetting [[c]], just-in-time compiler and threaded virtual machine, all written in assembly --- <https://github.com/Bricktech2000/Atto-8/tree/master/test/musts/>

[[brainfuck]] is a tiny [[turing complete]] [[programming language]] and a sort of minimal practical incarnation of the [[turing machine]]

**representation** --- <https://github.com/Bricktech2000/Atto-8/blob/master/test/musts/bf%20transp.asm>

```c
#include<stdio.h>
char t[99],*p=t;int main(void){
```

| [[brainfuck]]  | [[c]] equivalent |
| -------------- | ---------------- |
| `>` move right | `++p;`           |
| `<` move left  | `--p;`           |
| `+` increment  | `++*p;`          |
| `-` decrement  | `--*p;`          |
| `.` output     | `putchar(*p);`   |
| `,` input      | `*p=getchar();`  |
| `[` loop begin | `while(*p){`     |
| `]` loop end   | `}`              |
| any other char | ` `              |

```c
}
```
