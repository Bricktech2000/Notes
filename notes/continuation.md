# Continuation

**aka** _evaluation context_

> **resource** David Madore's page on `call/cc`, not a good introduction to it but has some nuggets of wisdom --- [[../references/callcc.html]] --- <http://www.madore.org/~david/computers/callcc.html>

> **resource** _Teach Yourself Scheme in Fixnum Days_, Chapter 13 _Jumps_; a gentle introduction to `call/cc` with use-cases --- [[../references/t-y-scheme-Z-H-15.html]] --- <https://web.archive.org/web/20011020114101id_/https://www.cs.rice.edu/~dorai/t-y-scheme/t-y-scheme-Z-H-15.html> --- <https://www.cs.rice.edu/~dorai/t-y-scheme/t-y-scheme-Z-H-15.html>

> **resource** the continuation monad in the PNLC prelude --- <https://github.com/Bricktech2000/PNLC/blob/master/prelude.pnlc>

--- <https://youtu.be/DRFsodbxHQo> and <https://youtu.be/TE48LsgVlIU>, "Delimited Continuations, Demystified" by Alexis King

at their most general, [[continuation]]s are a **concept**, not a language feature: any language with a notion of evaluation has a notion of a [[continuation]], which stands for the context around the current redex --- <https://youtu.be/DRFsodbxHQo?t=276>. _first-class_ [[continuation]]s are the language feature. [[continuation]]s can be granted first-class citizenship by providing facilities---like `call/cc`---for _reifying_ them as [[function]]s, [[function]]s which, when called with an argument, plug the [[continuation]]'s hole with it --- <https://youtu.be/DRFsodbxHQo?t=1522> and me

notice that each is a special case of the next:

1. `break`/`continue`/[[goto]]s jump lexically within a stack frame
2. `longjmp`/[[exception]]s jump up the the call stack
3. [[continuation]]s jump to an earlier call stack state

_I mention this [escaping inner functions] here because there is an analogy with escaping continuations: escaping continuations do to return addresses what escaping inner functions do to data (i.e. making lifetimes become unpredictable and forcing a replacement of the simple stack model by a more complex, garbage-collected graph). We will return to this. [never returns to this]_ --- <http://www.madore.org/~david/computers/callcc.html>

you can use _small-step reduction semantics_ with [[continuation]]s in the reduction rules to describe the behavior of the control operators of a [[programming language]]. in what follows, $E[\cdot]$ and $C[\cdot]$ denote an _evaluation context_, as in, a [[continuation]]. --- <https://youtu.be/DRFsodbxHQo?t=4458> and <https://youtu.be/DRFsodbxHQo?t=1278>. the shape of evaluation contexts is constrained so as to match the evaluation semantics of the [[programming language]]; for example, you could have $E[x] = \texttt{if \(x\) then 1 else 0}$ or $E[x] = \texttt{6 + \(x\)}$ but not $E[x] = \texttt{if true then \(x\) else 0}$ or $E[x] = \texttt{2 * 3 + \(x\)}$ --- <https://youtu.be/DRFsodbxHQo?t=1171>.

- $\displaystyle \frac{E[\texttt{exit \(v\)}]}{\texttt{exit \(v\)}}$. for example, `1 + exit 5 * 3 = exit 5`
- $\displaystyle \frac{E[\texttt{catch \(C[\texttt{throw \(v\)}]\) \(f\)}]}{E[\texttt{\(f\) \(v\)}]}$. for example, `1 + catch (2 * throw 5) (n. 3 * n) = 1 + 3 * 5 = 16`
- $\displaystyle \frac{E[\texttt{call/cc \(f\)}]}{E[\texttt{\(f\) (x. abort \(E[\texttt x]\))]}}$ $\displaystyle \frac{E[\texttt{abort \(v\)}]}{v}$. for example, `1 + callcc (k. k 2 + k 5) = 1 + 2 = 3`
- $\displaystyle \frac{E[\texttt{reset \(C[\texttt{shift \(f\)}]\)}]}{E[\texttt{reset (\(f\) (x. reset \(C[\texttt x]\)))}]}$ $\displaystyle \frac{E[\texttt{reset \(v\)}]}{E[v]}$. for example, `1 + reset (2 * shift (k. k 3 + k 5)) = 1 + (2 * 3 + 2 * 5) = 17`
- $\displaystyle \frac{E[\texttt{prompt \(C[\texttt{control \(f\)}]\)}]}{E[\texttt{\(f\) (x. \(C[\texttt x]\))}]}$ $\displaystyle \frac{E[\texttt{prompt \(v\)}]}{E[v]}$. for example, `1 + prompt (2 * control (k. k 3 + k 5)) = 1 + (2 * 3 + 2 * 5) = 17`. note how $\texttt{(x. \(C[\texttt x]\))}$ is [[continuation]] $C$ reified as a [[function]]
- $\displaystyle \frac{E[\texttt{delimit \(C[\texttt{yield \(v\)}]\) \(f\)}]}{E[\texttt{\(f\) \(v\) (x. \(C[\texttt x]\))}]}$. for example, `1 + delimit (2 * yield ()) ((). k. k 3 + k 5) = 1 + (2 * 3 + 2 * 5) = 17`

--- <https://youtu.be/DRFsodbxHQo> and [[../references/6a375895-8e04-83ea-bb18-23c54f6bcb36.md]]

## Continuation-Passing Style

> **resource** _Definitional Interpreters for Higher-Order Programming Languages_ (Reynolds, 1972), section _Continuations_, manual conversion of a program to [[continuation#continuation-passing style]] --- [[../references/800194.805852.pdf]] --- <https://dl.acm.org/doi/10.1145/800194.805852>

_To eliminate this [order-of-application] dependence, we must first identify the circumstances under which an arbitrary program in the defining language will be affected by the order of application. The essential effect of switching from call-by-value to call-by-name is to postpone the evaluation of the operands of application expressions (and declaring subexpressions of let expressions), and to alter the number of times these operands are evaluated. We have already seen that in a purely applicative language, the only way in which this change can affect the meaning of a program is to avoid the evaluation of a non-terminating operand. Now suppose we define an expression to be **serious** if there is any possibility that its evaluation might not terminate. Then a sufficient condition for order-of-application independence is that a program should contain no serious operands or declaring expressions._

_[...]_

_At first sight, this condition appears to be so restrictive that it could not be met in a non-trivial program. As can be seen with a little thought, the condition implies that whenever some function calls a serious function, the calling function must return the same result as the called function, without performing any further computation. But any function which calls a serious function must be serious itself. Thus by induction, as soon as any serious function returns a result, every function must immediately return the same result, which must therefore be the final result of the entire program._

_Nevertheless, there is a method for transforming an arbitrary program into one which meets our apparently restrictive condition. The underlying idea has appeared in a variety of contexts, (19,20,21) but its application to definitional interpreters is due to Morris and Wadsworth. (15) Basically, one replaces each serious function $f_\mathrm{old}$ (except the main program) by a new serious function $f_\mathrm{new}$ which accepts an additional argument called a **continuation**. The continuation will be a function itself, and $f_\mathrm{new}$ is expected to compute the same result as $f_\mathrm{old}$, apply the continuation to this result, and then return the result of the continuation, i.e.,_

$$
f_\mathrm{new}(x_1, \dots, x_n, c) = c(f_\mathrm{old}(x_1, \dots, x_n))
$$

_This introduction of continuations provides an additional "degree of freedom" which can be used to meet our condition for order-of-evaluation independence. Essentially, instead of performing further actions after a serious function has returned, one imbeds the further actions in the continuation which is passed to the serious function._

--- _Definitional Interpreters for Higher-Order Programming Languages_ (Reynolds, 1972)
