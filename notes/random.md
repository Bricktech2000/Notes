# Random

```mermaid
graph LR
  A---B
  B-->C(asdf)
  B-->D(asdf)
```

```mermaid
graph LR
  fa:fa-check-->fa:fa-coffee
```

## sum of `n` first squares

```python
sum(i ** 2 for i in range(n + 1))
```

$$
i^n = \prod_{i=0}^n i
$$

$$
\Sigma_{i + 1} = \Sigma_i + (i + 1)^2 \\
% \Sigma_{i + 2} = \Sigma_i + (i - 1)^2 + i^2 \\
% \Sigma_{i + 2} = \Sigma_i + 2i^2 - 2i + 1 \\
% \Sigma_{i + 3} = \Sigma_i + (i - 2)^2 + 2i^2 - 2i + 1 \\
% \Sigma_{i + 3} = \Sigma_i + 2i^2 - 4i + 4 + 2i^2 - 2i + 1 \\
% \Sigma_{i + 3} = \Sigma_i + 4i^2 - 6i + 5 \\
% \Sigma_{i + 4} = \Sigma_i + (i - 3) ^ 2 + 4i^2 - 6i + 5 \\
% \Sigma_{i + 4} = \Sigma_i + (i - 3) ^ 2 + 4i^2 - 6i + 5 \\
$$

$$
\Sigma_i = \Sigma_{i - 1} + i^2 \\
\Sigma_i = i * i^2 - 2 * sum(i - 1) * i + \Sigma_{i - 1} \\
\Sigma_i = i^3 - 2 * i * i(i + 1) / 2 + \Sigma_{i - 1} \\
i^3 - 2 * i^2(i + 1) / 2 = i^2 \\

% i^3 - i^2 - 2 * i(i + 1) / 2 = 0
$$

## school situation

```mermaid
graph LR

A([predicted improvement of classes])
B(enjoyment of classes)
C([status of accommodations])
D(busyness during summer)
E(choice of classes during summer)
F([result of job application])
G(decision on dual degree)
H(decision on data science option)

A --> B
C -.-> B --> G --> H

F --> D
D --> E --> D
G -.-> E
```

```
I(audit thing)
I -.-> A
E ==> I
```

$$
P\ = \delta f - \delta x \\
P\ x, y = (\delta f - \delta x)\ x, y \\
$$

$$
P\ x, y = \delta f - \delta x \\
P\ 1, 2 = (\delta f - \delta x)\ 1, 2
$$

[[book]]
