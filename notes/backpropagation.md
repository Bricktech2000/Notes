# Backpropagation

_algorithm to compute the [[gradient]] of a [[neural network]] efficiently_

**see** [[math notation]], [[neural network]], [[calculus]], [[calculus notation]]

&mdash; <https://youtu.be/kbGu60QBx2o>

&mdash; <https://youtu.be/Ilg3gGewQ5U?t=698>

&mdash; <http://neuralnetworksanddeeplearning.com/chap2.html#the_four_fundamental_equations_behind_backpropagation> summary

&mdash; me

let $g'\ z = \begin{bmatrix} (\delta\ g\ z^0 - \delta z^0) \\\ \vdots \\\ (\delta\ g\ z^n - \delta z^n) \end{bmatrix}$

let $g \begin{bmatrix}x^0 \\\ x^1 \\\ \vdots\end{bmatrix} \equiv \begin{bmatrix}g x^0 \\\ g x^1 \\\ \vdots\end{bmatrix}$ (duplicate)

## computing changes in loss

$\delta \mathcal L - \delta a_y^y = (\delta \mathcal L - \delta a_y^y)$, where

$\mathcal L$ is the [[loss function]]

$a_y$ is the last layer of the network

to maximize $\Delta \mathcal L$, $\Delta a_y^y = (a_y^y \rightarrow \delta \mathcal L - \delta a_y^y)\ a_y^y$, see [[gradient]]

written differently, $\Delta a_y = (\delta a_y^y \rightarrow \delta \mathcal L - \delta a_y)\ a_y$

## computing changes in weight

$\delta a_j^j - \delta w_{k \to j}^{j, k} = \delta z_j^j - \delta w_{k \to j}^{j, k} \mid \delta a_j^j - \delta z_j^j$

computing the [[derivative]]s using the chain [[derivative rules]],

$\delta z_j^j - \delta w_{k \to j}^{j, k} = a_k^k$, see [[forward propagation]]

$\delta a_j^j - \delta z_j^j = (\delta\ g\ z_j^j - \delta z_j^j)$, where $g$ is the [[activation function]]

therefore, $\delta a_j^j - \delta w_{k \to j}^{j, k} = a_k^k \mid (\delta\ g\ z_j^j - \delta z_j^j)$

to maximize $\Delta L$, $\Delta w_{k \to j}^{j, k} = a_k^k \mid (z_j^j \rightarrow \delta\ g\ z_j^j - \delta z_j^j)\ z_j \mid \Delta a_j^j$, see [[gradient]]

written differently, $\Delta w_{k \to j} = \Delta a_j\ \mathring\shortmid\ g'\ z_j\ \dot\mid\ {a_k}^{\intercal}$, see [[hadamard product]], [[dot product]]

## computing changes in activation

$\delta a_j^j - \delta a_k^k = \delta z_j^j - \delta a_k^k \mid \delta a_j^j - \delta z_j^j$

computing the [[derivative]]s using the chain [[derivative rules]],

$\delta z_j^j - \delta a_k^k = w_{k \to j}^{j, k}$, see [[forward propagation]]

$\delta a_j^j - \delta z_j^j = (\delta\ g z_j^j - \delta z_j^j)$, where $g$ is the [[activation function]]

therefore, $\delta a_j^j - \delta a_k^k = w_{k \to j}^{j, k} \mid (\delta\ g\ z_j^j - \delta z_j^j)$

to maximize $\Delta L$, $\Delta a_k^k = w_{k \to j}^{j, k} \mid (z_j^j \rightarrow \delta\ g\ z_j^j - \delta z_j^j)\ z_j \mid \Delta a_j^j$ summed over all $j$ , see [[gradient]]

written differently, $\Delta a_j = {w_{k \to j}}^{\intercal}\ \dot\mid\ \Delta a_j\ \mathring\shortmid\ g'\ z_j$, see [[hadamard product]], [[dot product]]

## propagating the gradient

$\Delta w_{k \to j}$ are averaged through a fixed-size batch of training examples

&mdash; <https://youtu.be/tIeHLnjs5U8?t=310>

then,

$w'_{k \to j} = w_{k \to j} : \alpha \shortmid \Delta w_{k \to j}$, where

$w_{k \to j}$ are the original weights from layer $j$ to layer $k$

$w'_{k \to j}$ are the updated weights from layer $j$ to layer $k$

$\alpha$ is the _learning rate_ of the network

&mdash; <https://youtu.be/w8yWXqWQYmU?t=627>
