# Backpropagation

_algorithm to compute the [[gradient]] of a [[neural network]] efficiently_

**see** [[math notation]], [[neural network]], [[calculus]], [[calculus notation]]

&mdash; <https://youtu.be/kbGu60QBx2o>

&mdash; <https://youtu.be/Ilg3gGewQ5U?t=698>

&mdash; <http://neuralnetworksanddeeplearning.com/chap2.html#the_four_fundamental_equations_behind_backpropagation> summary

&mdash; me

let **`g_* z = x -> \d g z^x -- \d x`**

## computing changes in loss

**`\d L -- \d a_y^y = (\d L -- \d a_y^y )`**, where

- **`L`** is the [[loss function]]
- **`a_y`** is the last layer of the network

to maximize **`\D L`**, **`\D a_y^y = (\d L -- \d a_y^y )`**, see [[gradient]]

written differently, **`\D a_y = (\d L -- \d a_y )`**

## computing changes in weight

**`\d a_j^j -- \d w_k->j^j,k = \d z_j^j -- \d w_k->j^j,k | \d a_j^j -- \d z_j^j`**

computing the [[derivative]]s using the chain [[derivative rules]],

**`\d z_j^j -- \d w_k->j^j,k = a_k^k`**, see [[forward propagation]]

**`\d a_j^j -- \d z_j^j = (\d g z_j^j -- \d z_j^j )`**, where **`g`** is the [[activation function]]

therefore, **`\d a_j^j -- \d w_k->j^j,k = a_k^k | (\d g z_j^j -- \d z_j^j )`**

to maximize **`\D L`**, **`\D w_k->j^j,k = a_k^k | (\d g z_j^j -- \d z_j^j ) | \D a_j^j`**, see [[gradient]]

written using an [[outer product]], **`\D w_k->j = (\D a_j | g_* z_j ) * | a_k *`**, see [[hadamard product]], [[outer product]]

written using [[matrix#multiplication]], **`\D w_k->j = (\D a_j | g_* z_j) | \r a_k`**, see [[hadamard product]], [[matrix#multiplication]] #todo mm

## computing changes in activation

**`\d a_j^j -- \d a_k^k = \d z_j^j -- \d a_k^k | \d a_j^j -- \d z_j^j`**

computing the [[derivative]]s using the chain [[derivative rules]],

**`\d z_j^j -- \d a_k^k = w_k->j^j,k`**, see [[forward propagation]]

**`\d a_j^j -- \d z_j^j = (\d g z_j^j -- \d z_j^j )`**, where **`g`** is the [[activation function]]

therefore, **`\d a_j^j -- \d a_k^k = w_k->j^j,k | (\d g z_j^j -- \d z_j^j )`**

to maximize **`\D L`**, **`\D a_k^k = w_k->j^j,k | (\d g z_j^j -- \d z_j^j ) | \D a_j^j`** summed over all **`j`** , see [[gradient]]

written using [[matrix#multiplication]], **`\D a_j = \r w_k->j | (\D a_j | g_* z_j )`**, see [[hadamard product]], [[matrix#multiplication]] #todo mm

## propagating the gradient

**`\D w_k->j`** are averaged through a fixed-size batch of training examples

&mdash; <https://youtu.be/tIeHLnjs5U8?t=310>

then,

**`w_*k->j = w_k->j : \a \D w_k->j`**, where

- **`w_k->j`** are the original weights from layer **`j`** to layer **`k`**
- **`w_*k->j`** are the updated weights from layer **`j`** to layer **`k`**
- **`\a`** is the _learning rate_ of the [[neural network]]

&mdash; <https://youtu.be/w8yWXqWQYmU?t=627>
