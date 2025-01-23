# Exception

**aka** _`try-catch` exception_

[[exception]]s were [[invent]]ed

the central problem with using [[exception]]s for error handling is that errors are **not** exceptional --- <https://youtu.be/sbVxq7nNtgo?t=2m3s>. assuming the "happy path" and handling other cases by breaking normal control flow is not smart. that said, sometimes, breaking normal control flow and `longjmp`ing somewhere up the stack---regardless of whether errors are involved---is the most practical solution. and in those rare cases, [[exception]]s become a useful [[tool]]

> **example** my continuation-passing style [[regular expression]] engine reports matches and backtracks possessive quantifiers by `longjmp`ing up the stack --- <https://github.com/Bricktech2000/CPS-RE/blob/6e5535e73bc449c8e41c4c31cc0c7d7e3f15a973/cps-re.c#L23-L48>
