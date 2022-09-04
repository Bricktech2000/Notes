# Lambda Calculus

see [[combinatory-logic]], [[recursion]]

&mdash; <https://youtu.be/eis11j_iGMs>

used for backlinks

**properties**

[[lambda-calculus]] and [[turing-machine]]s are equivalent

[[function]]s in [[lambda-calculus]] are pure [[function]]s

[[lambda-calculus]] is Turing complete, see [[turing-machine]]

[[lambda-calculus]] is the basis for most [[functional-programming]] languages

## Church Booleans

[[boolean]] values and [[boolean-logic]] [[operator]]s can be defined as follows:

$\text{true} = \lambda x.\ \lambda y.\ x$

$\text{false} = \lambda x.\ \lambda y.\ y$

&mdash; <https://youtu.be/eis11j_iGMs?t=413>

$\text{not} = \lambda p.\ p\ \text{false}\ \text{true}$

$\text{and} = \lambda p.\ \lambda q.\ p\ q\ p$

$\text{or} = \lambda p.\ \lambda q.\ q\ p\ q$

&mdash; <https://youtu.be/eis11j_iGMs?t=484>

&mdash; <https://en.wikipedia.org/wiki/Lambda_calculus#Logic_and_predicates>

## Iteration in Lambda Calculus

[[iteration]] is defined as $(\lambda x.\ x\ x) (\lambda x.\ x\ x)$. evaluating this [[function]] call once yields itself. this definition is equivalent to $\operatorname{rec} \lambda x.\ x$, see [[recursion]] &mdash; <https://youtu.be/9T8A89jgeTI?t=544>

## Recursion in Lambda Calculus

general [[recursion]] in [[lambda-calculus]] can be defined using the [[combinatory-logic]] Y combinator

$\operatorname{rec} f \equiv Y\ f$

&mdash; <https://youtu.be/9T8A89jgeTI?t=627>
