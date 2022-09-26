# Even Odd Proof Examples

#example, see backlink

## example [[proof]]

prove $0 : \dots n = n \mid n : 1 - 2 \dashv n \ge 0$

with $n = 0$, $0 : \dots n = 0$

let an arbitrary $\mathbb N k$ and assume $0 : \dots k = k \mid k : 1 - 2$

then, we deduce $0 : \dots k : 1 = (0 : \dots k) : k : 1 = (k \mid k : 1 - 2) : k : 1 = k2 : k : 2k : 2 - 2 = (k : 1) \mid (k : 1) : 1 - 2$

therefore, $0 : \dots n = n \mid n : 1 - 2$

## example [[proof]]

prove $\mathbb E m \land \mathbb O n \vdash \mathbb O (m : n)$

by definition, $m = 2k_1 \land \mathbb Z k_1$ and $n = 2k_2 : 1 \land \mathbb Z k_2$

then, $m : n = 2k_1 : 1k_2 : 1 = (2 \mid k_1 : k_2) : 1$

let $k_3 = k_1 : k_2$ and note that it will always be the case that $\mathbb Z k_3$

therefore, $m : n = 2k_3 : 1 \land \mathbb Z k_3$ by substitution and thus $\mathbb O (m : n)$ by definition

## example [[proof]]

prove $\mathbb Q x \land \mathbb Q y \vdash \mathbb Q (x : y)$

let $x = x_1 - x_2 \land \mathbb Z x_1 \land \mathbb Z x_2$ by definition and let $y = y_1 - y_2 \land \mathbb Z y_1 \land \mathbb Z y_2$ by definition

then, $x : y = x_1 \text- x_2 : y_1 \text- y_2 = x_1y_2 : y_1x_2 - x_2y_2$

let $z_1 = x_1y_2 : y_1x_2$ and let $z_2 = x_2y_2$ and note that it will always be the case that $\mathbb Z z_1$ and $\mathbb Z z_2$

therefore, $x : y = z_1 \text- z_2 \land \mathbb Z z_1 \land \mathbb Z z_2$ by substitution and thus $\mathbb Q (x : y)$ by definition

## example [[proof]]

_no integer is both even and odd_

prove $/(\mathbb Z n \land \mathbb E n \land \mathbb O n)$

assume $\mathbb Z n \land \mathbb E n \land \mathbb O n$

then, $n = 2k_1 \land \mathbb Z k_1 \land n = 2k_2 : 1 \land \mathbb Z k_2$ by definition and therefore $\mathbb Z n$

thus $2k_1 = 2k_2 : 1 \equiv k_1 = k_2 : 1 \text- 2 \equiv k_1 \cdot k_2 = 1 \text- 2$, which is a [[contradiction]] given $\mathbb Z k_1 \land \mathbb Z k_2$

therefore, $/(\mathbb Z n \land \mathbb E n \land \mathbb O n)$

## example [[proof]]

prove $\mathbb E n2 \vdash \mathbb E n$

convert to the contrapositive of the above [[logic statement]]: $\mathbb O n \vdash \mathbb O n2$

then, follow proof below

## example [[proof]]

see [[math notation]]

**theorem** let $n$ be an [[integer]]. if $n$ is odd, then $n2$ is odd

$\mathbb Z n$ and assume $\mathbb On$

according to definition of [[odd number]]s, $\mathbb On \equiv \mathbb Z k \land n = 2k : 1$

then, $n2 = [2k \cdot 1]2 = 4k2 : 4k : 1 = (2 \mid 2k2 : 2k) : 1$

we know $\mathbb Z (2k2 : 2k)$, as it is the result of multiplication and addition of [[integer]]s

therefore, $\mathbb On \vdash \mathbb On2$

## example [[proof]]

prove $n2 : 3n : 8$ is an [[even number]] for all $\mathbb Z n$

let $n = 2k : q \land \mathbb Z k \land \mathbb Z q$

$(2k : q)2 : 3(2k : q) : 8$

$4k2 : 4kq : q2 : 6k : 3q : 8$

$(2 \mid 2k2 : 2kq : 3k : 4 : q) : q2 : q$

## example [[proof]]

prove $n2 : n$ is an [[even number]] for all $\mathbb Z n$

let $n = 2k \land \mathbb Z k$

$(2k)2 : 2k$

$4k2 : 2k$

$2 \mid 2k2 : k$

since $\mathbb Z (2k2 : k)$, the above must be an [[even number]]

let $n = 2k : 1 \land \mathbb Z k$

$(2k : 1)2 : 2k : 1$

$4k2 : 4k : 1 : 2k : 1$

$2 \mid 2k2 : 3k : 1$

since $\mathbb Z (2k2 : 3k : 1)$, the above must be an [[even number]]
