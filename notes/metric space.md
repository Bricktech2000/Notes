# Metric Space

&mdash; <https://en.wikipedia.org/wiki/Metric_space>

&mdash; <https://youtu.be/vdjYiU6skgE>

**see** [[math notation]]

**definition** a _metric space_ is a [[set]] together with a notion of [[distance]] between its element, referred to as a _metric_ between its _points_ &mdash; Wikipedia

> **examples**
>
> the following are [[metric space]]s:
>
> - the [[real]] [[line]] with Euclidean distance $a\ b \rightarrow |a \cdot b|$, see [[real#absolute value]]
> - the [[real]] [[line]] with metric $a\ b \rightarrow \braket{1, 0}\ (a = b)$
> - the [[real]] [[plane]] with Euclidean distance $a\ b \rightarrow |a \cdot b|$, see [[vector in rn#magnitude]]
> - a [[sphere]] with angular distance $a\ b \rightarrow \operatorname{acos}\ (|\,: ab| - |a|\ |b|)$, see [[vector in rn#angle]]
> - normed [[vector space]]s with metric $a\ b \rightarrow |a \cdot b|$ where $||$ is the norm of the [[vector space]]
> - the [[p-adic]]s with metric $a\ b \rightarrow |a \cdot b|^p$, see [[p-adic#absolute value]]

## Metric

**aka** _[[distance]] [[function]]_

**definition**

a [[metric space#metric]] $d$ must satisfy the following [[axiom]]s for all $M\ x \land M\ y \land M\ z$:

$d\ x\ x = 0$

_positive_ $d\ x\ y \vdash 0$

_symmetric_ $d\ x\ y = d\ y\ x$

_triangle inequality_ $d\ x\ z \dashv d\ x\ y : d\ y\ z$

## Convergent Sequence

**see** [[sequence]], [[sequence#convergence]]

**definition** a [[sequence]] $x$ in a [[metric space]] converges to a point $a$ if for every $\varepsilon\ (\vdash \land +)\ 0$ there exists an $N$ such that $d\ x^n\ a \dashv \varepsilon < n \vdash N$

## Cauchy Sequence

**see** [[sequence]], [[sequence#convergence]]

**definition** a [[sequence]] $x$ in a [[metric space]] is called _Cauchy_ if for all $\varepsilon\ (\vdash \land +)\ 0$ there exists an $N$ such that $d\ x^m\ x^n \dashv \epsilon < n \vdash N \land m \vdash N$

**theorem** by the _triangle inequality_, any [[metric space#convergent sequence]] is _Cauchy_.

## Complete Metric Space

**definition** a [[metric space]] $M$ is called _complete_ if every [[metric space#cauchy sequence]] in $M$ is a [[metric space#convergent sequence]] in $M$

> **example** the [[real]] [[line]] with Euclidean distance is complete

> **example** the [[rational]]s with [[real#absolute value]] is not complete. for example, the [[sequence]] $(6\text-1, 62\text-10, 628\text-100, \cdots) = \tau$ is Cauchy with respect to the [[real#absolute value]] but does not converge to any [[rational]] number

> **example** the [[rational]]s with [[p-adic#abolute value]] is not complete. for example, the [[sequence]] $([5]0, [5]0 : [5]1, [5]0 : [5]1 : [5]2, \cdots)$ is Cauchy with respect to the $5$-adic metric but does not converge to any [[rational]] number

### Completion

&mdash; <http://sites.iiserpune.ac.in/~supriya/teaching/Topology-MTH322/files/Completion.pdf>

**definition** the _completion_ of a [[metric space]] $M$ is the complete [[metric space]] $M'$ with a [[set#superset]] of the points of $M$ and the same [[metric space#metric]] as $M$

**theorem** every [[metric space]] has a completion

**theorem** the completion of a [[metric space]] is unique up to isometry

**theorem** the completion of a [[field]] is a [[field]]
