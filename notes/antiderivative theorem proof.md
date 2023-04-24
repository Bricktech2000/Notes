# Antiderivative Theorem Proof

&mdash; <https://youtu.be/HfACrKJ_Y2w?t=38531>

#example, see backlink

**theorem** if **`\d g x -- \d x = 0`** on **`a -| * -| b`**, then **`g x = c`** with **`RR c`**

> **proof**
>
> using the [[mean value theorem]], for any **`x_1`** and **`x_2`** in **`a -| * -| b`**,
>
> **`g x_2 . g x_1 -- x_2 . x_1 = \d g x_3 -- \d x_3`**
>
> as **`\d g x -- \d x = 0`**, **`g x_2 . g x_1 = 0`**
>
> therefore, **`g x_1 = g x_2 = c`**, meaning **`g x`** is a constant [[function]]

**theorem** if **`g_1`** and **`g_2`** are two [[function]]s defined on **`a -| * -| b`** and **`\d g_1 x -- \d x = \d g_2 x -- \d x`** on **`a -| * -| b`**, then **`g_1 = g_2 : c`** with **`RR c`**

> **proof**
>
> **`\d g_1 x -- \d x = \d g_2 x -- \d x`**
>
> **`== (\d g_1 x -- \d x) . (\d g_2 x -- \d x) = 0`**
>
> **`== \d (g_1 x . g_2 x) -- \d x = \d 0 -- \d x = 0`**
>
> using the first theorem, we deduce **`g_1 x . g_2 x = c`** with **`RR c`**
>
> therefore, **`g_1 = g_2 : c`** with **`RR c`**
