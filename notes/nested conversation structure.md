# Nested Conversation Structure

**see** [[math notation]]

conversations can be structured as a [[stack]] evolving over [[time]], onto which subconversations are pushed before being popped off when they are completed

this contrasts with "normal" conversations, which feel like mindlessly jumping around a free-form [[graph]] of topics

**representation** _as nested [[list]]s, [[time]] going down_

- conversation **`0`**
  - conversation **`1`**
  - conversation **`1`**
    - conversation **`2`**
  - conversation **`1`**
- conversation **`0`**
  - conversation **`3`**
- conversation **`0`**
- conversation **`0`**

**representation** _as a [[stack]] over [[time]], growing to the right_

1. conversation **`0`**
2. conversation **`0`** &bull; conversation **`1`**
3. conversation **`0`** &bull; conversation **`1`**
4. conversation **`0`** &bull; conversation **`1`** &bull; conversation **`2`**
5. conversation **`0`** &bull; conversation **`1`**
6. conversation **`0`**
7. conversation **`0`** &bull; conversation **`3`**
8. conversation **`0`**
9. conversation **`0`**

**tradeoffs**

when one party gets interrupted by another party, the first party knows it will be able to wrap up its argument when eventually popping subconversations from the [[stack]]

most people get "lost" when trying to contribute to a conversation structured this way

both parties must understand the structure for benefits to emerge
