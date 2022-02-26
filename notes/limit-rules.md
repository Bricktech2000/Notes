# Limit Rules

see [[classical-math-notation]], [[math-notation]]

## General Rules

- $\lim_{x \to \infty} 1 / (x ^ r) = 0\ if\ r > 0$
- $\lim_{x \to 0} 1 / x = \infty$
- $\lim_{x \to a} \ne \varnothing\ \equiv\ \lim_{x \to a^+} = \lim_{x \to a^-} \ne \varnothing$

## Arithmetic Rules

let $c$ be a constant and ensure $\lim_{x \to a}f(x)$ and $\lim_{x \to a}g(x)$ are [[limit-that-exists]]

- $\lim_{x \to a}[f(x) + g(x)] = \lim_{x \to a}f(x) + \lim_{x \to a}g(x)$
- $\lim_{x \to a}[f(x) - g(x)] = \lim_{x \to a}f(x) - \lim_{x \to a}g(x)$
- $\lim_{x \to a}[c f(x)] = c\lim_{x \to a}f(x)$
- $\lim_{x \to a}[f(x) g(x)] = \lim_{x \to a}f(x) \times \lim_{x \to a}g(x)$
- $\lim_{x \to a}\frac{f(x)}{g(x)} = \frac{\lim_{x \to a}f(x)}{\lim_{x \to a}g(x)}$ if $\lim_{x \to a} g(x) \ne 0$
- $\lim_{x \to a}[f(x)]^n = [\lim_{x \to a} f(x)]^n$
- $\lim_{x \to a}\sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)}$. When $n\ \%\ 2 = 0$, we assume that $\lim_{x \to a} f(x) \ne 0$
