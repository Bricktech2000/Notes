# Lambda Calculus

**see** [[combinatory logic]], [[recursion]]

&mdash; <https://youtu.be/eis11j_iGMs>

used for backlinks

**properties**

[[lambda calculus]] and [[turing machine]]s are equivalent

[[function]]s in [[lambda calculus]] are pure [[function]]s

[[lambda calculus]] is Turing complete, see [[turing machine]]

[[lambda calculus]] is the basis for most [[functional programming]] languages

## Church Booleans

[[boolean]] values and [[boolean logic]] [[operator]]s can be defined as follows:

$\text{true} = x\ y \rightarrow x$

$\text{false} = x\ y \rightarrow y$

&mdash; <https://youtu.be/eis11j_iGMs?t=413>

$\text{not} = p \rightarrow p\ \text{false}\ \text{true}$

$\text{and} = p\ q \rightarrow p\ q\ p$

$\text{or} = p\ q\ \rightarrow q\ p\ q$

&mdash; <https://youtu.be/eis11j_iGMs?t=484>

&mdash; <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

## Iteration in Lambda Calculus

[[iteration]] is defined as $(x \rightarrow x\ x)\ (x \rightarrow x\ x)$ in my [[math notation]] or as $(\lambda x.\ x\ x) (\lambda x.\ x\ x)$ in [[conventional math notation]]. evaluating this [[function]] call once yields itself. this definition is equivalent to $\operatorname{rec}\ (x \rightarrow x)$ in my [[math notation]] or to $\operatorname{rec} \lambda x.\ x$ in [[conventional math notation]], see [[recursion]] &mdash; <https://youtu.be/9T8A89jgeTI?t=544>

## Recursion in Lambda Calculus

general [[recursion]] in [[lambda calculus]] can be defined using the [[combinatory logic]] Y combinator

$\operatorname{rec} f \equiv Y\ f$

&mdash; <https://youtu.be/9T8A89jgeTI?t=627>
