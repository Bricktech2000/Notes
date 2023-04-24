# Forward Propagation

**see** [[math notation]], [[neural network]], [[matrix]]

## mathematics

### calculating neuron outputs

#todo mm

given weights **`w`** from layer **`k`** to layer **`j`**, we define:

**`w_k->j []a_k & || & 1[] = z_j`** or more conventionally **`w^*_k->j a_k : b^* = z_j`**, where

- **`z_j`** are the **non-activated** neuron outputs of layer **`j`** and **`a_k`** are the neuron outputs of layer **`k`**
- **`w^*_k->j`** is the weight [[matrix]] from layer **`k`** to layer **`j`**
- **`b^*`** is the bias [[vector]] for layer **`j`**
- **`w_k->j`** is the weight [[matrix]] augmented with the bias [[matrix]], **`[]w^*_k->j & || & b^*[]`**

expanding,

**`[]w_k->j^0,0 & w_k->j^0,1 & ... & w_k->j^0,k & w_k->j^0,b && w_k->j^1,0 & w_k->j^1,1 & ... & w_k->j^1,k & w_k->j^1,b && ... & ... & ... & ... & ... && w_k->j^j,0 & w_k->j^j,1 & ... & w_k->j^j,k & w_k->j^j,b[] []a_k^0 && a_k^1 && ... && a_k^k && a_k^b[] = []z_j^0 && z_j^1 && ... && z_j^j[]`** with **`b = k : 1 /\ a_k^b = 1`**, where

- **`j`** is the number of neurons in layer **`j`** and **`k`** is the number of neurons in layer **`k`**, or layer **`j . 1`**
- **`z_j`** are the **non-activated** neuron outputs of layer **`j`** and **`a_k`** are the neuron outputs of layer **`k`**
- **`w_k->j^j,k`** is the weight from neuron **`a_k^k`** to neuron **`a_j^j`**
- **`a_k^b`** is the bias neuron (in layer **`k`**) for layer **`j`**
- **`w_k->j^j,b`** is the bias for neuron **`a_j^j`**

> **note** recall that superscripts have special meaning whereas subscript are just English [[character]]s. this means that neuron **`a_j^j`** is the **`j`**th neuron in the vector **`a_j`**; the subscript **`_j`** is part of the name **`a_j`** whereas the superscript **`^j`** is an index in **`a_j`**. see [[math notation]]

&mdash; <https://youtu.be/aircAruvnKk?t=807>

&mdash; me

### applying an activation function

applying an [[activation function]] is important, as, otherwise, every layer would be a [[linear combination]] of the layer before it. this would then mean that the network is just a very fancy [[linear regression]] as it wouldn't be able to produce more complex [[function]]s

&mdash; <https://youtu.be/w8yWXqWQYmU?t=309>

**`a_j = g z_j *`**, where

- **`z_j`** are the **non-activated** neuron outputs of layer **`j`**
- **`a_j`** are the neuron outputs of layer **`j`**
- **`g`** is an [[activation function]]

## implementation

using [[matrix#multiplication]] makes implementations of [[forward propagation]] in code much simpler and much faster as many libraries optimize "the heck out of" [[matrix#multiplication]] &mdash; <https://youtu.be/aircAruvnKk?t=907>

below is a sample `feedforward` function using _numpy_

```python
def feedforward(self, a):
  '''return the output of the network for an input vector `a`'''
  for b, w in zip(self.biases, self.weights):
    a = sigmoid(np.dot(w, a) + b)
  return a
```

&mdash; <https://youtu.be/aircAruvnKk?t=915>
