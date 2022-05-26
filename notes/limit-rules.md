# Limit Rules

see [[math-notation]]

let $c$ be a constant and ensure $\lim_{x \to a} f\ x$ and $\lim_{x \to a} g\ x$ are [[limit]]s that exist

## General Rules

$\lim_{x \to \infty} -[x]r = 0 \dashv r > 0$

$\lim_{x \to 0} -x = \infty$

## Sum Rule

$\lim_{x \to a} (f\ x \cdot g\ x) = \lim_{x \to a} f\ x \cdot \lim_{x \to a} g\ x$

## Difference Rule

$\lim_{x \to a} (f\ x \circ g\ x) = \lim_{x \to a} f\ x \circ \lim_{x \to a} g\ x$

## Constant Multiple Rule

$\lim_{x \to a} (c\ |\ f\ x) = c\ |\ \lim_{x \to a} f\ x$

## Product Rule

$\lim_{x \to a} (f\ x\ |\ g\ x) = \lim_{x \to a} f\ x\ |\ \lim_{x \to a} g\ x$

## Quotient Rule

$\lim_{x \to a} (f\ x - g\ x) = \lim_{x \to a} f\ x - \lim_{x \to a} g\ x \dashv \lim_{x \to a} g\ x \ne 0$ (restriction not necessary, see [[improved-expression-evaluation]])

## Power Rule

$\lim_{x \to a} [f\ x]n = [\lim_{x \to a} f\ x]n$

### derived Root Rule

$\lim_{x \to a} \lfloor f\ x \rfloor n = \lfloor \lim_{x \to a} f\ x \rfloor n$. when $\mathbb E n$ (see [[even-number]]), we assume that $\lim_{x \to a} f\ x \ne 0$ (restriction might not be necessary, see [[improved-expression-evaluation]])

## Composition Rule

$\lim_{x \to a} (f\ g\ x) = f \lim_{x \to a} g\ x$ if $f$ is continuous (see [[function]]) at $a$

## Infinity Rules

$\lim_{x \to \dot \circ \infty} [x]r = 0 \dashv r < 0$

$\lim_{x \to 0} -x = \dot \circ \infty$

## Squeeze Theorem

let $f\ x \leq g\ x \leq h\ x$ for $x$ near a value $a$

if $\lim_{x \to a} f\ x = \lim_{x \to a} h\ x = L$, then $\lim_{x \to a} g\ x = L$
