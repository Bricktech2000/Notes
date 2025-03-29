# Neural Network

**see** [[linear algebra]], [[optimization]]

**see**

[[loss function]]

[[activation function]]

[[automatic differentiation]]

a [[neural network]] is sort of a [[function]] from some input data to a prediction of some output data, parameterized by network weights; to evaluate the [[neural network]], we compose with a [[loss function]] to produce a _cost function_, which is sort of a [[function]] from network weights to cost, parameterized by training examples --- <https://youtu.be/IHZwWFHWa-w?t=274>. we can get the [[gradient]] of the cost function for free using reverse-mode [[automatic differentiation]], and from there we perform [[gradient#descent]] to train the network

proper [[gradient#descent]] on the cost function would have to be performed over all training examples; in practice that's too slow, so instead we use _stochastic gradient descent_, which is [[gradient#descent]] over smaller batches of randomized training examples

multilayer perceptrons need [[activation function]]s, because, without them, the network would reduce to a [[linear transformation]], up to a [[vector]]-valued offset if the perceptrons have biases

the "hello world" of neural networks is recognizing hand-written digits --- <https://youtu.be/IHZwWFHWa-w>. the _MNIST database_ contains labeled 28x28 images of hand-written digits---60000 for training and 10000 for testing

## ---

--- <https://youtu.be/aircAruvnKk>, <https://youtu.be/IHZwWFHWa-w>, <https://youtu.be/Ilg3gGewQ5U>, <https://youtu.be/tIeHLnjs5U8>

--- <https://youtu.be/VMj-3S1tku0>
