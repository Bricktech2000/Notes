# Non-Copyable Data

_a random idea for creating data that cannot be copied_

1. take the data and encrypt it using the recipient’s public key
2. send the encrypted data to the recipient
3. get the recipient to decrypt the data, but there’s a twist: when they do, somehow, their private key gets leaked

step #3 is where the magic happens: the recipient cannot share the data with anyone else, as it would compromise their private key. it would need to be mathematically impossible to decrypt the file without exposing the recipient’s private key.

## stuff to flesh out

#think

- find a mathematical algorithm that exposes the recipient’s private key when decrypting the data
- find a way to incorporate the recipient’s private key inside the data itself
