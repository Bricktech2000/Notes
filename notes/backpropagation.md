# Backpropagation

_algorithm to compute the [[gradient]] of a [[neural network]] efficiently_

**see** [[math notation]], [[neural network]], [[calculus]], [[calculus notation]]

--- <https://youtu.be/kbGu60QBx2o>

--- <https://youtu.be/Ilg3gGewQ5U?t=698>

--- <http://neuralnetworksanddeeplearning.com/chap2.html#the_four_fundamental_equations_behind_backpropagation> summary

--- me

let **`g_* z = x -> dd g z^x -- dd x`**

## computing changes in loss

**`dd L -- dd a_y^y = (dd L -- dd a_y^y)`**, where

- **`L`** is the [[loss function]]
- **`a_y`** is the last layer of the network

to maximize **`dd L`**, **`dd a_y^y = (dd L -- dd a_y^y)`**, see [[gradient]]

written differently, **`dd a_y = (dd L -- dd a_y)`**

## computing changes in weight

**`dd a_j^j -- dd w_k->j^j,k = dd z_j^j -- dd w_k->j^j,k | dd a_j^j -- dd z_j^j`**

computing the [[derivative]]s using the chain [[derivative rules]],

**`dd z_j^j -- dd w_k->j^j,k = a_k^k`**, see [[forward propagation]]

**`dd a_j^j -- dd z_j^j = (dd g z_j^j -- dd z_j^j)`**, where **`g`** is the [[activation function]]

therefore, **`dd a_j^j -- dd w_k->j^j,k = a_k^k | (dd g z_j^j -- dd z_j^j)`**

to maximize **`dd L`**, **`dd w_k->j^j,k = a_k^k | (dd g z_j^j -- dd z_j^j) | dd a_j^j`**, see [[gradient]]

written using an [[outer product]], **`dd w_k->j = (dd a_j | g_* z_j) * | a_k *`**, see [[hadamard product]], [[outer product]]

written using [[matrix#multiplication]], **`dd w_k->j = (dd a_j | g_* z_j) | rr a_k`**, see [[hadamard product]], [[matrix#multiplication]] #todo mm

## computing changes in activation

**`dd a_j^j -- dd a_k^k = dd z_j^j -- dd a_k^k | dd a_j^j -- dd z_j^j`**

computing the [[derivative]]s using the chain [[derivative rules]],

**`dd z_j^j -- dd a_k^k = w_k->j^j,k`**, see [[forward propagation]]

**`dd a_j^j -- dd z_j^j = (dd g z_j^j -- dd z_j^j)`**, where **`g`** is the [[activation function]]

therefore, **`dd a_j^j -- dd a_k^k = w_k->j^j,k | (dd g z_j^j -- dd z_j^j)`**

to maximize **`dd L`**, **`dd a_k^k = w_k->j^j,k | (dd g z_j^j -- dd z_j^j) | dd a_j^j`** summed over all **`j`** , see [[gradient]]

written using [[matrix#multiplication]], **`dd a_j = rr w_k->j | (dd a_j | g_* z_j)`**, see [[hadamard product]], [[matrix#multiplication]] #todo mm

## propagating the gradient

**`dd w_k->j`** are averaged through a fixed-size batch of training examples

--- <https://youtu.be/tIeHLnjs5U8?t=310>

then,

**`w_*k->j = w_k->j : aa dd w_k->j`**, where

- **`w_k->j`** are the original weights from layer **`j`** to layer **`k`**
- **`w_*k->j`** are the updated weights from layer **`j`** to layer **`k`**
- **`aa`** is the _learning rate_ of the [[neural network]]

--- <https://youtu.be/w8yWXqWQYmU?t=627>
