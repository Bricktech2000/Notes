# Automatic Differentiation

**aka** _autodiff_, _autograd_

**see** [[calculus]], [[optimization]]

#xxx

_forward-mode_ [[automatic differentiation]] gives one column of the [[jacobian#matrix]], computing the derivative of one [[function]] input with respect to several [[function]] outputs.

---

the problem with _numerical differentiation_---finite differences from the [[limit]] definition---is truncation errors. the problem with _symbolic differentiation_---automation of manual [[derivative rules]]---is expression swell

symbolic differentiation (automated [[derivative rules]]): blowout of expression size, requires closed form

forward mode gives one column of the jacobian; better with few inputs and many outputs

reverse mode gives one row of the jacobian; better with many inputs and few outputs

backpropagation in multilayer perceptron [[neural network]]s is special case of reverse-mode [[automatic differentiation]] --- Wikipedia

---

--- <https://youtu.be/wG_nF1awSSY>

--- <https://youtu.be/VMj-3S1tku0?t=3695> (Andrej Karpathy)

--- <https://youtu.be/HB5TrK7A4pI?t=16m17s> (Gerald Sussman on Strange Loop)
