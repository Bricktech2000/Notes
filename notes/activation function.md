# Activation Function

## [[sigmoid function]]

**see** [[sigmoid function]]

> **note** using a [[sigmoid function]] as an [[activation function]] is old-school. ReLU is now preferred &mdash; <https://youtu.be/aircAruvnKk?t=1034>

## ReLU Function

_preferred activation function_

> **aka** rectified linear unit

**definition**

$\text{ReLU}\ z = 0 \lor z$

```python
def ReLU(x):
  return np.maximum(0, x)
```

&mdash; <https://www.sharpsightlabs.com/blog/numpy-relu/>

**representation**

![[20220628163633.png]]

## Tanh Function

_for getting values between $\cdot 1$ and $1$_

**see** [[hyperbolic function]]

**definition**

$\text{TANH}\ z = \tanh z$

```python
def TANH(x):
  return np.tanh(x)
```

**representation**

![[20220629115711.png]]

## Softmax Function

_for getting probabilities out_

**definition**

$\sigma^i\ z = e[z^i] - :\! e[z]$, where

- $\sigma^i\ z$ is the softmax [[activation function]] of $z$ at $z^i$
- $e$ is [[eulers constant]]
