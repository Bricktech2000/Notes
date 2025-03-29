# Activation Function

**see** [[function]], [[neural network]]

## Sigmoid Function

> **note** using the sigmoid function as an [[activation function]] is old school. the [[activation function#relu function]] is now preferred --- <https://youtu.be/aircAruvnKk?t=1034>

**definition**

```python
def sigmoid(x):
  return 1 / (1 + np.exp(-x))
```

## ReLU Function

_preferred activation function_

**aka** _rectified linear unit_

**definition**

```python
def relu(x):
  return np.maximum(0, x)
```

--- <https://www.sharpsightlabs.com/blog/numpy-relu/>

## Tanh Function

_for getting values in $[-1, 1]$_

**see** [[hyperbolic function]]

**definition**

```python
def tanh(x):
  e_2x = np.exp(2 * x)
  return (e_2x - 1) / (e_2x + 1)
  # or equivalently
  return np.tanh(x)
```

## Softmax Function

_for getting a [[probability distribution]] out_

--- <https://youtu.be/p-6wUOXaVqs>

**see** [[euler's constant]]

**definition**

```python
def softmax(x):
  return np.exp(x) / sum(np.exp(x))
```

--- <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.softmax.html>
