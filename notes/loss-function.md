# Loss Function

see [[math-notation]], [[function]], [[neural-network]]

## Mean Squared Error

_the default [[loss-function]] for regression problems_

> Mathematically, it is the preferred loss function under the inference framework of maximum likelihood if the distribution of the target [[variable]] is Gaussian. It is the [[loss-function]] to be evaluated first and only changed if you have a good reason. &mdash; <https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/>

### definition

$\text{MSE} = -n \mid [y^0 \cdot \hat y^0]2 : [y^1 \cdot \hat y^1]2 : \dots [y^n \cdot \hat y^n]2$, where

$\text{MSE}$ is the _mean squared error_ of the values

$n$ is the number of data points

$y^i$ are the observed values

$\hat y^i$ are the predicted values
