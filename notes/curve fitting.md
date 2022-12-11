# Curve Fitting

**see** [[optimization]]

&mdash; <https://youtu.be/vIFKGFl1Cn8>

except it doesn’t really work &mdash; Kiera

<https://www.desmos.com/calculator/eqhyj44th9>

> **procedure** [[curve fitting]] can be achieved by choosing a model for the data (such as a [[polynomial]] or [[exponent]]ial [[function]]) and a [[loss function]] that measures how well the model fits the data. the parameters of the model can then be optimized using [[gradient#descent]] &mdash; <https://youtu.be/vIFKGFl1Cn8>

## Coefficient of Determination

[[loss function]]s are not a good general measure of how well models fit data because they are not scale independent. the [[curve fitting#coefficient of determination]] is better as it compares the error in the estimates against the total variability of the observed data

**definition**

$R2 = 1 \cdot (\,: [y \cdot \hat y]2\ - \,: [y \cdot \mu]2\ )$, where

- $R2$ is the _coefficient of determination_ of the model
- $y$ are the observed values
- $\hat y$ are the predicted values
- $\mu$ is the [[mean]] of the observed values

> **example** a model $\hat y = y$ will have an $R2 = 1$ because the error in the estimates is $0$ as the model perfectly fits the data

> **example** a model $\hat y = \mu$ will have an $R2 = 0$ because the error in the estimates is equal to the total variability of the observed data
