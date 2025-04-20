# Automatic Differentiation

**aka** _algorithmic differentiation_, _autodiff_, _autograd_

**see** [[calculus]], [[optimization]], [[computer science]]

> **resource** my autodiff library, static reverse-mode automatic differentiation in C --- <https://github.com/Bricktech2000/Autodiff>

> **resource** _Automatic Differentiation in Machine Learning: a Survey_ (abstract kinda sucks; see last paragraph of introduction) --- [[1502.05767v4.pdf]] --- <https://arxiv.org/pdf/1502.05767>

backpropagation in multilayer perceptron [[neural network]]s is a special case of [[automatic differentiation#reverse-mode automatic differentiation]] --- <https://arxiv.org/pdf/1502.05767>

## Forward-Mode Automatic Differentiation

_forward-mode_ [[automatic differentiation]] gives one column of the [[jacobian#matrix]]---the [[derivative]] of several [[function]] outputs $y_n$ with respect to one [[function]] input $x_0$. it can be implemented by augmenting every intermediate value $v_i$ (the _primal_) with $\dot v_i = \frac{\partial v_i}{\partial x_0}$ (the _tangent_). [[function]] inputs $x_n$ are seeded with tangents $\dot x_n = \frac{\partial x_n}{\partial x_0}$---$1$ for $\dot x_0$ and $0$ otherwise---and the seed is propagated forward in a single pass. or, more generally, the [[derivative#directional derivative]]s of $y_n$ with respect to $\hat x = r$, given by the [[jacobian#matrix]]--[[euclidean vector]] product

$\mathbf J_f \cdot r^\top = \begin{bmatrix}\frac{\partial f_0}{\partial x_0} & \cdots & \frac{\partial f_0}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_0} & \cdots & \frac{\partial f_m}{\partial x_n}\end{bmatrix} \begin{bmatrix}r_0 \\ \vdots \\ r_n \end{bmatrix}$,

can be computed by seeding $\dot x = r$

> **note** as a mathematical novelty, the [[dual number]]s can be used as a [[data structure]] for carrying primals together with their tangents; see <https://arxiv.org/pdf/1502.05767>, $3.1.1 'Dual Numbers'

## Reverse-Mode Automatic Differentiation

_reverse-mode_ [[automatic differentiation]] gives one row of the [[jacobian#matrix]]---the [[derivative]] of one [[function]] output $y_0$ with respect to several [[function]] inputs $x_n$. it can be implemented by augmenting every intermediate value $v_i$ (the _primal_) with $\bar v_i = \frac{\partial y_0}{\partial v_i}$ (the _adjoint_). in a first pass, primals are propagated forward and dependencies are recorded in a _computation graph_ through a bookkeeping procedure. then, [[function]] outputs $y_n$ are seeded with adjoints $\bar y_n = \frac{\partial y_n}{\partial y_0}$---$1$ for $\bar y_0$ and $0$ otherwise---and the seed is propagated backward in a second pass. or, more generally, the "dual" [[derivative#directional derivative]]s of $\hat y = r$ with respect to $x_n$, given by the [[matrix#transpose]] [[jacobian#matrix]]--[[euclidean vector]] product

$\mathbf J_f^\top \cdot r^\top = \begin{bmatrix}\frac{\partial f_0}{\partial x_0} & \cdots & \frac{\partial f_m}{\partial x_0} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_0}{\partial x_m} & \cdots & \frac{\partial f_m}{\partial x_n}\end{bmatrix} \begin{bmatrix}r_0 \\ \vdots \\ r_m \end{bmatrix}$,

can be computed by seeding $\bar y = r$

## Static Automatic Differentiation

## Dynamic Automatic Differentiation

--- <https://arxiv.org/pdf/1502.05767>, $4.2 'Neural Networks, Deep Learning, Differentiable Programming'

--- <https://stackoverflow.com/questions/43455320/difference-between-symbolic-differentiation-and-automatic-differentiation>

[[automatic differentiation]] can be performed _statically_ ("define-and-run", output is the [[derivative]] as a [[function]]) or _dynamically_ ("define-by-run", output is the [[derivative]] at a given point). static [[automatic differentiation]] can compute arbitrary-order [[derivative]]s while dynamic [[automatic differentiation]] can only compute given-order [[derivative]]s; typically, only first-order [[derivative]]s are computed. dynamic [[automatic differentiation]] handles branching, looping and recursion transparently without needing overloads, while static [[automatic differentiation]] requires closed-form expressions

dynamic [[automatic differentiation#forward-mode automatic differentiation]] has negligible overhead. dynamic [[automatic differentiation#reverse-mode automatic differentiation]] has greater overhead because for every forward pass a new computation graph must be built. static [[automatic differentiation#forward-mode automatic differentiation]] and [[automatic differentiation#reverse-mode automatic differentiation]] have low overhead once the computation graph has been built

## symbolic differentiation

in practice, computation graphs are directed acyclic [[graph]]s, and intermediate values are reused throughout. naive [[automatic differentiation#static automatic differentiation]] where computation graphs are expression [[tree]]s and where work is duplicated everywhere is called _symbolic differentiation_

> **example** --- me and <https://arxiv.org/pdf/1904.02990>
>
> ```python
> # underlying program
> def f(x1, x2):
>   t1 = x1 * x1 + x2
>   return sin(t1) * cos(t1)
> ```
>
> ```mermaid
> graph TD
>   subgraph expression tree
>     Y($$*$$)
>     Y --> X & R
>     X($$\cos$$)
>     W($$+$$)
>     V($$x_2$$)
>     U($$*$$)
>     T($$x_1$$)
>     S($$x_1$$)
>           W --> U --> S & T
>     X --> W --> V
>     R($$\sin$$)
>     Q($$+$$)
>     P($$x_2$$)
>     O($$*$$)
>     N($$x_1$$)
>     M($$x_1$$)
>           Q --> O --> M & N
>     R --> Q --> P
>   end
>   subgraph directed acyclic graph
>     G($$*$$)
>     F($$\cos$$)
>     E($$\sin$$)
>     D($$+$$)
>     C($$x_2$$)
>     B($$*$$)
>     A($$x_1$$)
>     G --> E & F --> D --> B & C
>     B --> A & A
>   end
> ```

---

--- <https://youtu.be/wG_nF1awSSY> (heavily "based" on <https://arxiv.org/pdf/1502.05767>)

--- <https://youtu.be/VMj-3S1tku0?t=3695> (Andrej Karpathy)

--- <https://youtu.be/HB5TrK7A4pI?t=16m17s> (Gerald Sussman on Strange Loop)

--- <https://en.wikipedia.org/wiki/Automatic_differentiation>

--- <https://en.wikipedia.org/wiki/Automatic_differentiation#Automatic_differentiation_using_dual_numbers>

--- _Automatic Differentiation in Machine Learning: a Survey_ --- [[1502.05767v4.pdf]] --- <https://arxiv.org/pdf/1502.05767>

--- _On the Equivalence of Automatic and Symbolic Differentiation_ --- [[1904.02990v4.pdf]] --- <https://arxiv.org/pdf/1904.02990> (preprint)
