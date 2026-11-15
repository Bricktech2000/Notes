# APL

_A Programming Language_

> **resource** _Notation as a Tool of Thought_ by Kenneth E. Iverson, an introduction to APL (didn't read sections 2--4) --- [[../references/1283920.1283935.pdf]] --- <https://dl.acm.org/doi/pdf/10.1145/1283920.1283935>

[[apl]] is in denial of its identity. it purports to be a general-purpose mathematical notation, but forgets that most of [[mathematics]] is neither about [[number]]s nor their manipulation. at its core, [[apl]] is a [[programming language]], and that's okay. it's a terse, expressive, [[programming language]].

> **resource** the J Incunabulum by Arthur Whitney, an array language in 40 lines of C --- [[../references/iojATW.htm]] --- <https://www.jsoftware.com/ioj/iojATW.htm> --- [[../references/2025-06-06-readable-code-is-unreadable.html]] --- <https://blog.wilsonb.com/posts/2025-06-06-readable-code-is-unreadable.html>
>
> compile with `gcc -m32 -ansi`. if your `int`s are 16 bits you'll have to specify the missing `I` return type for `noun` and `verb`. **glossary**: `A` array, `t` type, `r` rank, `d` dimension, `p` payload, `V1` monadic verb, `V2` dyadic verb, `a` alpha, `w` omega, `ma` memory allocate, `mv` move, `tr` times-reduce, `ga` generate array, `rsh` reshape, `sha` shape, `pi` print integer, `nl` newline, `pr` print, `vt` verb tokens, `vd` dyadic verbs, `vm` monadic verbs, `st` store, `qp` query pronoun, `qv` query verb, `ex` execute, `wd` words
>
> the `find` implementation from [[../references/2025-06-06-readable-code-is-unreadable.html]] can be cleaned up:
>
> ```c
> V2(find){I r=w->r,*d=w->d,n=tr(r,d),j=n;DO(n,if(*a->p==w->p[i])j=i);
>  A z=ga(0,1,&w->r);DO(r,z->p[i]=j/tr(r-1-i,d+1+i)%d[i]);R z;}
> ```
