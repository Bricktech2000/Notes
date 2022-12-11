# Loss Function

**see** [[math notation]], [[function]], [[neural network]]

## Mean Squared Error

_the default [[loss function]] for regression problems_

**aka** _least squares objective function_ &mdash; <https://youtu.be/vIFKGFl1Cn8?t=1255>

> mathematically, it is the preferred [[loss function]] under the inference framework of maximum likelihood if the [[probability distribution]] of the target [[variable]] is normal. it is the [[loss function]] to be evaluated first and only changed if you have a good reason. &mdash; <https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/>

**definition**

$\text{MSE} = \,: [y \cdot \hat y]2 - \#\ y$, where

- $\text{MSE}$ is the _mean squared error_ of the values
- $y$ are the observed values
- $\hat y$ are the predicted values

> **note** squaring the [[distance]] between every $y$ and expected $\hat y$ makes it so that outliers have a greater effect on the result

> **equivalence** _[[variance]] and [[loss function#mean squared error]] with [[sample#mean]] as expected [[neural network]] output_
