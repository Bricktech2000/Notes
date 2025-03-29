# Loss Function

**see** [[math notation]], [[function]], [[neural network]]

## Mean Squared Error

_the default [[loss function]] for regression problems_

**aka** _least squares objective function_ --- <https://youtu.be/vIFKGFl1Cn8?t=1255>

> mathematically, it is the preferred [[loss function]] under the inference framework of maximum likelihood if the [[probability distribution]] of the target [[variable]] is normal. it is the [[loss function]] to be evaluated first and only changed if you have a good reason. --- <https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/>

**definition**

$\mathrm{MSE}\ y\ \hat y = \frac + \# (y - \hat y)^2$, where

- $\mathrm{MSE}$ is the _mean squared error_ of the values
- $y$ are the observed values
- $\hat y$ are the predicted values

> **note** squaring the [[distance]] between the $y$s and $\hat y$s means outliers have a greater effect on the result

**equiv** _[[variance]] and [[loss function#mean squared error]] with [[sample]] [[mean]] as expected [[neural network]] output_
