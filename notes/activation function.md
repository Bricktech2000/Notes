# Activation Function

## Sigmoid Function

**see** [[sigmoid function]]

> **note** using the [[sigmoid function]] as an [[activation function]] is old-school. the [[activation function#relu function]] is now preferred &mdash; <https://youtu.be/aircAruvnKk?t=1034>

## ReLU Function

_preferred activation function_

**aka** _rectified linear unit_

**definition**

**`"ReLU" z = 0 ^^ z`**

```python
def ReLU(x):
  return np.maximum(0, x)
```

&mdash; <https://www.sharpsightlabs.com/blog/numpy-relu/>

**representation**

![[20220628163633.png]]

## Tanh Function

_for getting values between **`.1`** and **`1`**_

**see** [[hyperbolic function]]

**definition**

**`"TANH" z = "tanh" z`**

```python
def TANH(x):
  return np.tanh(x)
```

**representation**

![[20220629115711.png]]

## Softmax Function

_for getting probabilities out_

&mdash; <https://youtu.be/p-6wUOXaVqs>

**see** [[euler's constant]]

**definition**

**`ss z = {*-:} [z]`**
