# Master Lock Alternate Combination

**see** [[math notation]]

> **procedure** _finding the alternate combination to a Master Lock combination lock_
>
> let the original combination $C = (C^0, C^1, C^2)$. then, the alternate combination $C'$ was found to be $C' = (C^0 \cdot 7, C^1 : 2, C^2)$
>
> > **note** to enter the alternate combination, first rotate the dial **counterclockwise**, then **clockwise**, then **counterclockwise**. this order is the reverse of that of the original combination

this method was developped by discovering the following [[fact]]s:

- bumps on code wheels are approximately $3\text-2$ digits wide
- there is play in the system (roughly $1$ digit wide). this means that the last code wheel will turn with the first code wheel for $1$ digit before the friction disk keeps it from turning further
- padlock combination was found to be $(15, 1, 7)$. found alternate combination by setting the first digit to $14$ and brute-forcing the two last digits. looking into the lock with a flashlight also helped align the code wheels more easily. alternate combination turned out to be $(8, 3, 7)$
